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

    def items_to_html(self, items, title=None, **kwargs) -> str:
        """
        Convert a list of dicts to an HTML table.
        :param items: list of dict to convert
        :param title: optional title to include
        :param kwargs: keys in the dict and its header value to include in the table
        :return: HTML code
        """
        if not isinstance(items, list):
            raise AnsibleFilterError('items must be a list')

        if title and not isinstance(title, str):
            raise AnsibleFilterError('title must be a string')

        if kwargs:
            for value in kwargs.values():
                if not isinstance(value, str):
                    raise AnsibleFilterError('kwargs values must be strings')

        header = list(kwargs.values()) if kwargs else list(items[0].keys())
        keys = list(kwargs.keys()) if kwargs else list(items[0].keys())

        template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% if title %}
    <title>{{ title }}</title>
    {% endif %}
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        table {
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            border-collapse: collapse;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        th, td {
            padding: 12px;
            text-align: center;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #2baecf;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    {% if title %}
        <h1>{{ title }}</h1>
    {% endif %}
    <table>
        <thead>
            <tr>
            {% for i in header %}
                <th>{{ i }}</th>
            {% endfor %}
            </tr>
        </thead>
        <tbody>
        {% for item in items %}
            <tr>
            {% for key in keys %}
                <td>{{ item[key] }}</td>
            {% endfor %}
            </tr>
        {% endfor %}
        </tbody>
    </table>
</body>
</html>
        """)

        return template.render(items=items, header=header, keys=keys, title=title)
