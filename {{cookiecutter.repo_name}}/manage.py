#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    sys.path = [
        os.path.abspath(os.path.join(__file__, '..', 'site', 'apps')),
        os.path.abspath(os.path.join(__file__, '..', 'site')),
    ] + sys.path

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
