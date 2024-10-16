# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.access_mode import AccessMode
from openapi_server.models.share_message import ShareMessage
from openapi_server.models.share_recipient import ShareRecipient
from openapi_server import util


class WebhookV2EventDataShareInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_description: str=None, access_mode: AccessMode=None, assets: List[str]=None, created: datetime=None, embed: bool=None, expiration: str=None, expired: bool=None, file_drop_create_folders: bool=None, form_id: int=None, has_notification: bool=None, has_password: bool=None, hash: str=None, id: int=None, inherited: bool=None, is_public: bool=None, messages: List[ShareMessage]=None, modified: datetime=None, name: str=None, owner_hash: str=None, paths: List[str]=None, recipients: List[ShareRecipient]=None, require_email: bool=None, resent: bool=None, status: int=None, tracking_status: str=None, type: str=None):
        """WebhookV2EventDataShareInner - a model defined in OpenAPI

        :param access_description: The access_description of this WebhookV2EventDataShareInner.
        :param access_mode: The access_mode of this WebhookV2EventDataShareInner.
        :param assets: The assets of this WebhookV2EventDataShareInner.
        :param created: The created of this WebhookV2EventDataShareInner.
        :param embed: The embed of this WebhookV2EventDataShareInner.
        :param expiration: The expiration of this WebhookV2EventDataShareInner.
        :param expired: The expired of this WebhookV2EventDataShareInner.
        :param file_drop_create_folders: The file_drop_create_folders of this WebhookV2EventDataShareInner.
        :param form_id: The form_id of this WebhookV2EventDataShareInner.
        :param has_notification: The has_notification of this WebhookV2EventDataShareInner.
        :param has_password: The has_password of this WebhookV2EventDataShareInner.
        :param hash: The hash of this WebhookV2EventDataShareInner.
        :param id: The id of this WebhookV2EventDataShareInner.
        :param inherited: The inherited of this WebhookV2EventDataShareInner.
        :param is_public: The is_public of this WebhookV2EventDataShareInner.
        :param messages: The messages of this WebhookV2EventDataShareInner.
        :param modified: The modified of this WebhookV2EventDataShareInner.
        :param name: The name of this WebhookV2EventDataShareInner.
        :param owner_hash: The owner_hash of this WebhookV2EventDataShareInner.
        :param paths: The paths of this WebhookV2EventDataShareInner.
        :param recipients: The recipients of this WebhookV2EventDataShareInner.
        :param require_email: The require_email of this WebhookV2EventDataShareInner.
        :param resent: The resent of this WebhookV2EventDataShareInner.
        :param status: The status of this WebhookV2EventDataShareInner.
        :param tracking_status: The tracking_status of this WebhookV2EventDataShareInner.
        :param type: The type of this WebhookV2EventDataShareInner.
        """
        self.openapi_types = {
            'access_description': str,
            'access_mode': AccessMode,
            'assets': List[str],
            'created': datetime,
            'embed': bool,
            'expiration': str,
            'expired': bool,
            'file_drop_create_folders': bool,
            'form_id': int,
            'has_notification': bool,
            'has_password': bool,
            'hash': str,
            'id': int,
            'inherited': bool,
            'is_public': bool,
            'messages': List[ShareMessage],
            'modified': datetime,
            'name': str,
            'owner_hash': str,
            'paths': List[str],
            'recipients': List[ShareRecipient],
            'require_email': bool,
            'resent': bool,
            'status': int,
            'tracking_status': str,
            'type': str
        }

        self.attribute_map = {
            'access_description': 'accessDescription',
            'access_mode': 'accessMode',
            'assets': 'assets',
            'created': 'created',
            'embed': 'embed',
            'expiration': 'expiration',
            'expired': 'expired',
            'file_drop_create_folders': 'fileDropCreateFolders',
            'form_id': 'formId',
            'has_notification': 'hasNotification',
            'has_password': 'hasPassword',
            'hash': 'hash',
            'id': 'id',
            'inherited': 'inherited',
            'is_public': 'isPublic',
            'messages': 'messages',
            'modified': 'modified',
            'name': 'name',
            'owner_hash': 'ownerHash',
            'paths': 'paths',
            'recipients': 'recipients',
            'require_email': 'requireEmail',
            'resent': 'resent',
            'status': 'status',
            'tracking_status': 'trackingStatus',
            'type': 'type'
        }

        self._access_description = access_description
        self._access_mode = access_mode
        self._assets = assets
        self._created = created
        self._embed = embed
        self._expiration = expiration
        self._expired = expired
        self._file_drop_create_folders = file_drop_create_folders
        self._form_id = form_id
        self._has_notification = has_notification
        self._has_password = has_password
        self._hash = hash
        self._id = id
        self._inherited = inherited
        self._is_public = is_public
        self._messages = messages
        self._modified = modified
        self._name = name
        self._owner_hash = owner_hash
        self._paths = paths
        self._recipients = recipients
        self._require_email = require_email
        self._resent = resent
        self._status = status
        self._tracking_status = tracking_status
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WebhookV2EventDataShareInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WebhookV2EventData_share_inner of this WebhookV2EventDataShareInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_description(self):
        """Gets the access_description of this WebhookV2EventDataShareInner.

        Human readable description of what visitors are allowed to do with the receive folder

        :return: The access_description of this WebhookV2EventDataShareInner.
        :rtype: str
        """
        return self._access_description

    @access_description.setter
    def access_description(self, access_description):
        """Sets the access_description of this WebhookV2EventDataShareInner.

        Human readable description of what visitors are allowed to do with the receive folder

        :param access_description: The access_description of this WebhookV2EventDataShareInner.
        :type access_description: str
        """

        self._access_description = access_description

    @property
    def access_mode(self):
        """Gets the access_mode of this WebhookV2EventDataShareInner.


        :return: The access_mode of this WebhookV2EventDataShareInner.
        :rtype: AccessMode
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this WebhookV2EventDataShareInner.


        :param access_mode: The access_mode of this WebhookV2EventDataShareInner.
        :type access_mode: AccessMode
        """

        self._access_mode = access_mode

    @property
    def assets(self):
        """Gets the assets of this WebhookV2EventDataShareInner.

        List of items included in the share

        :return: The assets of this WebhookV2EventDataShareInner.
        :rtype: List[str]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this WebhookV2EventDataShareInner.

        List of items included in the share

        :param assets: The assets of this WebhookV2EventDataShareInner.
        :type assets: List[str]
        """

        self._assets = assets

    @property
    def created(self):
        """Gets the created of this WebhookV2EventDataShareInner.

        Date and ti

        :return: The created of this WebhookV2EventDataShareInner.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this WebhookV2EventDataShareInner.

        Date and ti

        :param created: The created of this WebhookV2EventDataShareInner.
        :type created: datetime
        """

        self._created = created

    @property
    def embed(self):
        """Gets the embed of this WebhookV2EventDataShareInner.

        Whether the receive folder can be embedded within a web page

        :return: The embed of this WebhookV2EventDataShareInner.
        :rtype: bool
        """
        return self._embed

    @embed.setter
    def embed(self, embed):
        """Sets the embed of this WebhookV2EventDataShareInner.

        Whether the receive folder can be embedded within a web page

        :param embed: The embed of this WebhookV2EventDataShareInner.
        :type embed: bool
        """

        self._embed = embed

    @property
    def expiration(self):
        """Gets the expiration of this WebhookV2EventDataShareInner.

        Date and time when the receive folder will no longer be 

        :return: The expiration of this WebhookV2EventDataShareInner.
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this WebhookV2EventDataShareInner.

        Date and time when the receive folder will no longer be 

        :param expiration: The expiration of this WebhookV2EventDataShareInner.
        :type expiration: str
        """

        self._expiration = expiration

    @property
    def expired(self):
        """Gets the expired of this WebhookV2EventDataShareInner.

        Whether access to the receive folder has expired

        :return: The expired of this WebhookV2EventDataShareInner.
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this WebhookV2EventDataShareInner.

        Whether access to the receive folder has expired

        :param expired: The expired of this WebhookV2EventDataShareInner.
        :type expired: bool
        """

        self._expired = expired

    @property
    def file_drop_create_folders(self):
        """Gets the file_drop_create_folders of this WebhookV2EventDataShareInner.

        Whether files should be automatically placed in subfolders of the receive folder

        :return: The file_drop_create_folders of this WebhookV2EventDataShareInner.
        :rtype: bool
        """
        return self._file_drop_create_folders

    @file_drop_create_folders.setter
    def file_drop_create_folders(self, file_drop_create_folders):
        """Sets the file_drop_create_folders of this WebhookV2EventDataShareInner.

        Whether files should be automatically placed in subfolders of the receive folder

        :param file_drop_create_folders: The file_drop_create_folders of this WebhookV2EventDataShareInner.
        :type file_drop_create_folders: bool
        """

        self._file_drop_create_folders = file_drop_create_folders

    @property
    def form_id(self):
        """Gets the form_id of this WebhookV2EventDataShareInner.

        ID of the associated form

        :return: The form_id of this WebhookV2EventDataShareInner.
        :rtype: int
        """
        return self._form_id

    @form_id.setter
    def form_id(self, form_id):
        """Sets the form_id of this WebhookV2EventDataShareInner.

        ID of the associated form

        :param form_id: The form_id of this WebhookV2EventDataShareInner.
        :type form_id: int
        """

        self._form_id = form_id

    @property
    def has_notification(self):
        """Gets the has_notification of this WebhookV2EventDataShareInner.

        Whether delivery receipts are enabled for this share

        :return: The has_notification of this WebhookV2EventDataShareInner.
        :rtype: bool
        """
        return self._has_notification

    @has_notification.setter
    def has_notification(self, has_notification):
        """Sets the has_notification of this WebhookV2EventDataShareInner.

        Whether delivery receipts are enabled for this share

        :param has_notification: The has_notification of this WebhookV2EventDataShareInner.
        :type has_notification: bool
        """

        self._has_notification = has_notification

    @property
    def has_password(self):
        """Gets the has_password of this WebhookV2EventDataShareInner.

        Whether the receive folder requires visitors to enter a password

        :return: The has_password of this WebhookV2EventDataShareInner.
        :rtype: bool
        """
        return self._has_password

    @has_password.setter
    def has_password(self, has_password):
        """Sets the has_password of this WebhookV2EventDataShareInner.

        Whether the receive folder requires visitors to enter a password

        :param has_password: The has_password of this WebhookV2EventDataShareInner.
        :type has_password: bool
        """

        self._has_password = has_password

    @property
    def hash(self):
        """Gets the hash of this WebhookV2EventDataShareInner.

        Hash value of the receive

        :return: The hash of this WebhookV2EventDataShareInner.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this WebhookV2EventDataShareInner.

        Hash value of the receive

        :param hash: The hash of this WebhookV2EventDataShareInner.
        :type hash: str
        """

        self._hash = hash

    @property
    def id(self):
        """Gets the id of this WebhookV2EventDataShareInner.

        Unique ID of associated receive folder

        :return: The id of this WebhookV2EventDataShareInner.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookV2EventDataShareInner.

        Unique ID of associated receive folder

        :param id: The id of this WebhookV2EventDataShareInner.
        :type id: int
        """

        self._id = id

    @property
    def inherited(self):
        """Gets the inherited of this WebhookV2EventDataShareInner.

        Whether this share is inherited from a parent fol

        :return: The inherited of this WebhookV2EventDataShareInner.
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """Sets the inherited of this WebhookV2EventDataShareInner.

        Whether this share is inherited from a parent fol

        :param inherited: The inherited of this WebhookV2EventDataShareInner.
        :type inherited: bool
        """

        self._inherited = inherited

    @property
    def is_public(self):
        """Gets the is_public of this WebhookV2EventDataShareInner.

        Whether visitors can acccess the receive folder without an invitation link

        :return: The is_public of this WebhookV2EventDataShareInner.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this WebhookV2EventDataShareInner.

        Whether visitors can acccess the receive folder without an invitation link

        :param is_public: The is_public of this WebhookV2EventDataShareInner.
        :type is_public: bool
        """

        self._is_public = is_public

    @property
    def messages(self):
        """Gets the messages of this WebhookV2EventDataShareInner.

        Invitation messages sent for receive folder

        :return: The messages of this WebhookV2EventDataShareInner.
        :rtype: List[ShareMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this WebhookV2EventDataShareInner.

        Invitation messages sent for receive folder

        :param messages: The messages of this WebhookV2EventDataShareInner.
        :type messages: List[ShareMessage]
        """

        self._messages = messages

    @property
    def modified(self):
        """Gets the modified of this WebhookV2EventDataShareInner.

        Date and time when the share was last changed

        :return: The modified of this WebhookV2EventDataShareInner.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this WebhookV2EventDataShareInner.

        Date and time when the share was last changed

        :param modified: The modified of this WebhookV2EventDataShareInner.
        :type modified: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this WebhookV2EventDataShareInner.

        Name of receiv

        :return: The name of this WebhookV2EventDataShareInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebhookV2EventDataShareInner.

        Name of receiv

        :param name: The name of this WebhookV2EventDataShareInner.
        :type name: str
        """

        self._name = name

    @property
    def owner_hash(self):
        """Gets the owner_hash of this WebhookV2EventDataShareInner.

        Hash value of the user who \"owns\" the receive fo

        :return: The owner_hash of this WebhookV2EventDataShareInner.
        :rtype: str
        """
        return self._owner_hash

    @owner_hash.setter
    def owner_hash(self, owner_hash):
        """Sets the owner_hash of this WebhookV2EventDataShareInner.

        Hash value of the user who \"owns\" the receive fo

        :param owner_hash: The owner_hash of this WebhookV2EventDataShareInner.
        :type owner_hash: str
        """

        self._owner_hash = owner_hash

    @property
    def paths(self):
        """Gets the paths of this WebhookV2EventDataShareInner.

        List

        :return: The paths of this WebhookV2EventDataShareInner.
        :rtype: List[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this WebhookV2EventDataShareInner.

        List

        :param paths: The paths of this WebhookV2EventDataShareInner.
        :type paths: List[str]
        """

        self._paths = paths

    @property
    def recipients(self):
        """Gets the recipients of this WebhookV2EventDataShareInner.

        List of recipients invited  to the receive folder

        :return: The recipients of this WebhookV2EventDataShareInner.
        :rtype: List[ShareRecipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this WebhookV2EventDataShareInner.

        List of recipients invited  to the receive folder

        :param recipients: The recipients of this WebhookV2EventDataShareInner.
        :type recipients: List[ShareRecipient]
        """

        self._recipients = recipients

    @property
    def require_email(self):
        """Gets the require_email of this WebhookV2EventDataShareInner.

        Whether visitors must enter their email addresses to access the receive folder

        :return: The require_email of this WebhookV2EventDataShareInner.
        :rtype: bool
        """
        return self._require_email

    @require_email.setter
    def require_email(self, require_email):
        """Sets the require_email of this WebhookV2EventDataShareInner.

        Whether visitors must enter their email addresses to access the receive folder

        :param require_email: The require_email of this WebhookV2EventDataShareInner.
        :type require_email: bool
        """

        self._require_email = require_email

    @property
    def resent(self):
        """Gets the resent of this WebhookV2EventDataShareInner.

        Whether invitations to the receive folder have been re-sent to recipients

        :return: The resent of this WebhookV2EventDataShareInner.
        :rtype: bool
        """
        return self._resent

    @resent.setter
    def resent(self, resent):
        """Sets the resent of this WebhookV2EventDataShareInner.

        Whether invitations to the receive folder have been re-sent to recipients

        :param resent: The resent of this WebhookV2EventDataShareInner.
        :type resent: bool
        """

        self._resent = resent

    @property
    def status(self):
        """Gets the status of this WebhookV2EventDataShareInner.

        1 if share is active. 0 if not.

        :return: The status of this WebhookV2EventDataShareInner.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebhookV2EventDataShareInner.

        1 if share is active. 0 if not.

        :param status: The status of this WebhookV2EventDataShareInner.
        :type status: int
        """

        self._status = status

    @property
    def tracking_status(self):
        """Gets the tracking_status of this WebhookV2EventDataShareInner.

        Status of invitations sent for this receive folder

        :return: The tracking_status of this WebhookV2EventDataShareInner.
        :rtype: str
        """
        return self._tracking_status

    @tracking_status.setter
    def tracking_status(self, tracking_status):
        """Sets the tracking_status of this WebhookV2EventDataShareInner.

        Status of invitations sent for this receive folder

        :param tracking_status: The tracking_status of this WebhookV2EventDataShareInner.
        :type tracking_status: str
        """

        self._tracking_status = tracking_status

    @property
    def type(self):
        """Gets the type of this WebhookV2EventDataShareInner.

        Type of share **\"receive\"**

        :return: The type of this WebhookV2EventDataShareInner.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebhookV2EventDataShareInner.

        Type of share **\"receive\"**

        :param type: The type of this WebhookV2EventDataShareInner.
        :type type: str
        """

        self._type = type
