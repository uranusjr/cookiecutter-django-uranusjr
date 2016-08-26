import shutil
import tempfile

import pytest

from django.conf import settings
from django.test.html import parse_html
from django.utils import timezone


class HTMLParser:
    """Parse an HTML response or string for validation.

    The parser is based on HTML DOM Parser.
    <http://thehtmldom.sourceforge.net/>

    Usage::

    def test_thing(rf):
        response = some_view(rf.get('/'))
        document = HTMLParser().parse(response)
        assert len(document.find('div')) == 1
    """
    def parse(self, response=None, *, text=None, status_code=200):
        if response is not None and text is not None:
            raise ValueError(
                'Provide exactly one of "response" and "text" to parse.',
            )
        if response is not None:
            if status_code is not None:
                assert response.status_code == status_code
            text = response.rendered_content
        htmldom = pytest.importorskip('htmldom.htmldom')
        document = htmldom.HtmlDom().createDom(text)
        return document

    def arrange(self, element):
        """Arrange an HTML node for comparison.

        This method uses Django's ``parse_html`` testing utility to build
        an HTML node for asserting purposes. Usage::

            def test_div_foo(client, parser):
                body = parser.parse(client.get('/foo/'))
                expected = parser.arrange('<body><div>foo</div></body>')
                assert parser.arrage(body) == expected

        :param element: An HTML element. This can be either an htmldom node,
            or a string containing valid HTML. If a node is passed in,
            it is converted to string by calling ``html()`` first.
        """
        htmldom = pytest.importorskip('htmldom.htmldom')
        if isinstance(element, (htmldom.HtmlDomNode, htmldom.HtmlNodeList)):
            html = element.html()
        else:
            html = element
        if isinstance(html, bytes):
            html = html.decode('utf-8')
        return parse_html(html)


@pytest.fixture
def parser():
    return HTMLParser()


@pytest.fixture
def now():
    return timezone.now()


@pytest.fixture(scope='session', autouse=True)
def temp_media_root(request):
    media_root = settings.MEDIA_ROOT

    def teardown():
        if media_root.startswith(tempfile.gettempdir()):
            shutil.rmtree(media_root)

    request.addfinalizer(teardown)
    return media_root
