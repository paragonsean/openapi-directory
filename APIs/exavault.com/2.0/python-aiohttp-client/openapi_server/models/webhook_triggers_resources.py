# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class WebhookTriggersResources(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, compress: bool=None, copy: bool=None, create_folder: bool=None, delete: bool=None, download: bool=None, extract: bool=None, move: bool=None, rename: bool=None, upload: bool=None):
        """WebhookTriggersResources - a model defined in OpenAPI

        :param compress: The compress of this WebhookTriggersResources.
        :param copy: The copy of this WebhookTriggersResources.
        :param create_folder: The create_folder of this WebhookTriggersResources.
        :param delete: The delete of this WebhookTriggersResources.
        :param download: The download of this WebhookTriggersResources.
        :param extract: The extract of this WebhookTriggersResources.
        :param move: The move of this WebhookTriggersResources.
        :param rename: The rename of this WebhookTriggersResources.
        :param upload: The upload of this WebhookTriggersResources.
        """
        self.openapi_types = {
            'compress': bool,
            'copy': bool,
            'create_folder': bool,
            'delete': bool,
            'download': bool,
            'extract': bool,
            'move': bool,
            'rename': bool,
            'upload': bool
        }

        self.attribute_map = {
            'compress': 'compress',
            'copy': 'copy',
            'create_folder': 'createFolder',
            'delete': 'delete',
            'download': 'download',
            'extract': 'extract',
            'move': 'move',
            'rename': 'rename',
            'upload': 'upload'
        }

        self._compress = compress
        self._copy = copy
        self._create_folder = create_folder
        self._delete = delete
        self._download = download
        self._extract = extract
        self._move = move
        self._rename = rename
        self._upload = upload

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WebhookTriggersResources':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WebhookTriggers_resources of this WebhookTriggersResources.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def compress(self):
        """Gets the compress of this WebhookTriggersResources.

        Send webhook messages when resources are compressed into an archive.

        :return: The compress of this WebhookTriggersResources.
        :rtype: bool
        """
        return self._compress

    @compress.setter
    def compress(self, compress):
        """Sets the compress of this WebhookTriggersResources.

        Send webhook messages when resources are compressed into an archive.

        :param compress: The compress of this WebhookTriggersResources.
        :type compress: bool
        """

        self._compress = compress

    @property
    def copy(self):
        """Gets the copy of this WebhookTriggersResources.

        Send webhook messages when resources are copied.

        :return: The copy of this WebhookTriggersResources.
        :rtype: bool
        """
        return self._copy

    @copy.setter
    def copy(self, copy):
        """Sets the copy of this WebhookTriggersResources.

        Send webhook messages when resources are copied.

        :param copy: The copy of this WebhookTriggersResources.
        :type copy: bool
        """

        self._copy = copy

    @property
    def create_folder(self):
        """Gets the create_folder of this WebhookTriggersResources.

        Send webhook messages when a new folder is created.

        :return: The create_folder of this WebhookTriggersResources.
        :rtype: bool
        """
        return self._create_folder

    @create_folder.setter
    def create_folder(self, create_folder):
        """Sets the create_folder of this WebhookTriggersResources.

        Send webhook messages when a new folder is created.

        :param create_folder: The create_folder of this WebhookTriggersResources.
        :type create_folder: bool
        """

        self._create_folder = create_folder

    @property
    def delete(self):
        """Gets the delete of this WebhookTriggersResources.

        Send webhook messages when resources are deleted

        :return: The delete of this WebhookTriggersResources.
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this WebhookTriggersResources.

        Send webhook messages when resources are deleted

        :param delete: The delete of this WebhookTriggersResources.
        :type delete: bool
        """

        self._delete = delete

    @property
    def download(self):
        """Gets the download of this WebhookTriggersResources.

        Send webhook messages when resources are downloaded.

        :return: The download of this WebhookTriggersResources.
        :rtype: bool
        """
        return self._download

    @download.setter
    def download(self, download):
        """Sets the download of this WebhookTriggersResources.

        Send webhook messages when resources are downloaded.

        :param download: The download of this WebhookTriggersResources.
        :type download: bool
        """

        self._download = download

    @property
    def extract(self):
        """Gets the extract of this WebhookTriggersResources.

        Send webhook messages when resources are extracted from an archive.

        :return: The extract of this WebhookTriggersResources.
        :rtype: bool
        """
        return self._extract

    @extract.setter
    def extract(self, extract):
        """Sets the extract of this WebhookTriggersResources.

        Send webhook messages when resources are extracted from an archive.

        :param extract: The extract of this WebhookTriggersResources.
        :type extract: bool
        """

        self._extract = extract

    @property
    def move(self):
        """Gets the move of this WebhookTriggersResources.

        Send webhook messages when resources are moved.

        :return: The move of this WebhookTriggersResources.
        :rtype: bool
        """
        return self._move

    @move.setter
    def move(self, move):
        """Sets the move of this WebhookTriggersResources.

        Send webhook messages when resources are moved.

        :param move: The move of this WebhookTriggersResources.
        :type move: bool
        """

        self._move = move

    @property
    def rename(self):
        """Gets the rename of this WebhookTriggersResources.

        Send webhook messages when resources are renamed.

        :return: The rename of this WebhookTriggersResources.
        :rtype: bool
        """
        return self._rename

    @rename.setter
    def rename(self, rename):
        """Sets the rename of this WebhookTriggersResources.

        Send webhook messages when resources are renamed.

        :param rename: The rename of this WebhookTriggersResources.
        :type rename: bool
        """

        self._rename = rename

    @property
    def upload(self):
        """Gets the upload of this WebhookTriggersResources.

        Send webhook messages when resources are uploaded.

        :return: The upload of this WebhookTriggersResources.
        :rtype: bool
        """
        return self._upload

    @upload.setter
    def upload(self, upload):
        """Sets the upload of this WebhookTriggersResources.

        Send webhook messages when resources are uploaded.

        :param upload: The upload of this WebhookTriggersResources.
        :type upload: bool
        """

        self._upload = upload
