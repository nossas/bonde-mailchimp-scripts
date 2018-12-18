#!/usr/bin/env python
# coding: utf-8
import click
import re
import requests
from readcsv import member_list_id


class Mailchimp(object):
    """Class based to authenticate methods on API"""

    def __init__(self, token):
        # Getter dc value on token
        regex = re.search(r'(?<=-)\w+', token)
        self.uri = 'https://{dc}.api.mailchimp.com/3.0'.format(
            dc=regex.group(0)
        )
        self.auth = ('Bearer', token)

    def endpoint(self, keypath):
        """
        Getter pattern endpoint

        Keypaths:
            - members_detail: /lists/{0}/members/{1}
        """
        paths = dict(members_detail='/lists/{0}/members/{1}')
        return self.uri + paths.get(keypath)

    def unsubscribed(self, list_id, member_id):
        """Unsubscribe a member on list"""
        path = self.endpoint('members_detail').format(list_id, member_id)
        json = dict(status='unsubscribed')
        response = requests.put(path, json=json, auth=self.auth)
        return response.status_code == 200, response

    def delete(self, list_id, member_id):
        """Delete a member on list"""
        path = self.endpoint('members_detail').format(list_id, member_id)
        response = requests.delete(path, auth=self.auth)
        return response.status_code == 204, response

    def status(self, list_id, member_id):
        """Unsubscribe a member on list"""
        path = self.endpoint('members_detail').format(list_id, member_id)
        response = requests.get(path, auth=self.auth)
        return response.status_code == 200, response


def execute_method(mailchimp, method, list_id, member_id):
    successfully, resp = getattr(mailchimp, method)(
        list_id=list_id,
        member_id=member_id
    )

    if successfully:
        print('{0} to member {1} on list {2} with success;'.format(
            method, member_id, list_id
        ))
        if resp.request.method == 'GET':
            print('Status {0}'.format(resp.json().get('status')))
    else:
        if resp.status_code != 405:
            print('Failed on {0} method to member {1};'.format(
                method, member_id
            ))
            print(resp.json())


@click.command()
@click.option('--token', help='Mailchimp api token')
@click.option('--list_id', help='List ID of Mailchimp group')
@click.option('--member_id', help='Member ID of Mailchimp list')
@click.option('--csv', help='CSV file with email of member on first column')
@click.argument('method')
def cli(method, token, list_id, member_id=None, csv=None):
    mailchimp = Mailchimp(token)

    if not csv:
        execute_method(mailchimp, method, list_id, member_id)
    elif method != 'status':
        for member_hash in member_list_id(csv):
            execute_method(mailchimp, method, list_id, member_hash)
    else:
        print('The options --csv or --member_id are required.')


if __name__ == '__main__':
    cli()
