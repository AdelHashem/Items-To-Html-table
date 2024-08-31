#!/bin/python3
"""
Custom Ansible filter plugin to convert a list of items to an HTML list.
coded by: Adel Hashem
repo: https://github.com/AdelHashem/Items-To-Html-table

"""

from ansible.errors import AnsibleFilterError
from jinja2 import Template

class FilterModule(object):
    def filters(self):
        return {
            'items_to_html': self.items_to_html
        }

    def items_to_html(self, items, title=None):
        """
        Convert a list of dicts to an HTML table.
        :param items: list of dict to convert
        :param title: optional title to include
        :return: HTML code
        """
        if not isinstance(items, list):
            raise AnsibleFilterError('items must be a list')

        if title and not isinstance(title, str):
            raise AnsibleFilterError('title must be a string')

        template = Template("""
        """)

        return template.render(items=items, title=title)
