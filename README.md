# Items-To-Html-Table Ansible Filter Plugin

## Overview

This Ansible filter plugin allows you to generate an HTML table from a list of dictionaries, making it easier to create visually appealing reports. It's especially useful for creating HTML content that can be sent via email, providing a clean and organized view of the data.

## Key Features

- Converts a list of dictionaries into an HTML table.
- Simplifies the process of sending data as an HTML email.
- Customizable table columns and titles.

## How to Use

1. **Copy the Plugin**  
   Copy `itemstohtml.py` to your filter directory, typically located at `/usr/share/ansible/plugins/filter` (Default path).

2. **Usage in Playbook**  
   Here's an example of how to use the plugin in an Ansible playbook:

   ```yaml
   ---
   - name: Gather Facts
     hosts: all
     gather_facts: true
     vars:
       list_of_facts: "{{ ansible_play_hosts | map('extract', hostvars) | list }}"
     tasks:
       - name: Create HTML table of some keys
         ansible.builtin.copy:
           content: "{{ list_of_facts | items_to_html(title='Report', ansible_hostname='Host Name', ansible_distribution='Distribution') }}"
           dest: facts_report.html
         run_once: true

       - name: Send Email
         ansible.builtin.mail:
           host: smtp.freesmtpservers.com
           port: 25
           from: ansible-playbook@testing.com
           to:
             - adelhashem@testing.com
           subject: "Facts Report"
           body: "{{ list_of_facts | items_to_html(title='Report', ansible_hostname='Host Name', ansible_distribution='Distribution') }}"
           subtype: html
         run_once: true
   ```

## Parameters

- `title`: The title of the HTML table.
- Additional key-value pairs: Specify which keys to include in the table and optionally rename them. By default, the filter will include all keys with their original names.

## Example
![image](https://github.com/user-attachments/assets/2d766d50-c134-4f55-9942-b4dd6fb944f7)

In the example above:
- The playbook gathers facts from all hosts.
- It generates an HTML table with specific columns (`ansible_hostname`, `ansible_distribution`), and saves it as `facts_report.html`.
- The same table is sent via email using the `ansible.builtin.mail` module.

## Conclusion

This plugin streamlines the process of converting data into a well-formatted HTML table and is ideal for sending reports via email. By following the steps above, you can easily integrate it into your Ansible workflows.
