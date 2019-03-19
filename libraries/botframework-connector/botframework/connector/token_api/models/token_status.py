# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TokenStatus(Model):
    """The status of a particular token.

    :param channel_id: The channelId of the token status pertains to
    :type channel_id: str
    :param connection_name: The name of the connection the token status
     pertains to
    :type connection_name: str
    :param has_token: True if a token is stored for this ConnectionName
    :type has_token: bool
    :param service_provider_display_name: The display name of the service
     provider for which this Token belongs to
    :type service_provider_display_name: str
    """

    _attribute_map = {
        'channel_id': {'key': 'channelId', 'type': 'str'},
        'connection_name': {'key': 'connectionName', 'type': 'str'},
        'has_token': {'key': 'hasToken', 'type': 'bool'},
        'service_provider_display_name': {'key': 'serviceProviderDisplayName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TokenStatus, self).__init__(**kwargs)
        self.channel_id = kwargs.get('channel_id', None)
        self.connection_name = kwargs.get('connection_name', None)
        self.has_token = kwargs.get('has_token', None)
        self.service_provider_display_name = kwargs.get('service_provider_display_name', None)