from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_entity import BundleEntity
from openapi_server import util


async def delete_bundles_id(request: web.Request, id) -> web.Response:
    """Delete Bundle

    Delete Bundle

    :param id: Bundle ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_bundles(request: web.Request, user_id=None, cursor=None, per_page=None, sort_by=None, filter=None, filter_gt=None, filter_gteq=None, filter_lt=None, filter_lteq=None) -> web.Response:
    """List Bundles

    List Bundles

    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[created_at]&#x3D;desc&#x60;). Valid fields are &#x60;created_at&#x60; and &#x60;code&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter: dict | bytes
    :param filter_gt: If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter_gt: dict | bytes
    :param filter_gteq: If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter_gteq: dict | bytes
    :param filter_lt: If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter_lt: dict | bytes
    :param filter_lteq: If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter_lteq: dict | bytes

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_gt = .from_dict(filter_gt)
    filter_gteq = .from_dict(filter_gteq)
    filter_lt = .from_dict(filter_lt)
    filter_lteq = .from_dict(filter_lteq)
    return web.Response(status=200)


async def get_bundles_id(request: web.Request, id) -> web.Response:
    """Show Bundle

    Show Bundle

    :param id: Bundle ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_bundles_id(request: web.Request, id, clickwrap_id=None, code=None, description=None, dont_separate_submissions_by_folder=None, expires_at=None, form_field_set_id=None, inbox_id=None, max_uses=None, note=None, password=None, path_template=None, paths=None, permissions=None, preview_only=None, require_registration=None, require_share_recipient=None, send_email_receipt_to_uploader=None, skip_company=None, skip_email=None, skip_name=None, watermark_attachment_delete=None, watermark_attachment_file=None) -> web.Response:
    """Update Bundle

    Update Bundle

    :param id: Bundle ID.
    :type id: int
    :param clickwrap_id: ID of the clickwrap to use with this bundle.
    :type clickwrap_id: int
    :param code: Bundle code.  This code forms the end part of the Public URL.
    :type code: str
    :param description: Public description
    :type description: str
    :param dont_separate_submissions_by_folder: Do not create subfolders for files uploaded to this share. Note: there are subtle security pitfalls with allowing anonymous uploads from multiple users to live in the same folder. We strongly discourage use of this option unless absolutely required.
    :type dont_separate_submissions_by_folder: bool
    :param expires_at: Bundle expiration date/time
    :type expires_at: str
    :param form_field_set_id: Id of Form Field Set to use with this bundle
    :type form_field_set_id: int
    :param inbox_id: ID of the associated inbox, if available.
    :type inbox_id: int
    :param max_uses: Maximum number of times bundle can be accessed
    :type max_uses: int
    :param note: Bundle internal note
    :type note: str
    :param password: Password for this bundle.
    :type password: str
    :param path_template: Template for creating submission subfolders. Can use the uploader&#39;s name, email address, ip, company, and any custom form data.
    :type path_template: str
    :param paths: A list of paths to include in this bundle.
    :type paths: List[str]
    :param permissions: Permissions that apply to Folders in this Share Link.
    :type permissions: str
    :param preview_only: Restrict users to previewing files only?
    :type preview_only: bool
    :param require_registration: Show a registration page that captures the downloader&#39;s name and email address?
    :type require_registration: bool
    :param require_share_recipient: Only allow access to recipients who have explicitly received the share via an email sent through the Files.com UI?
    :type require_share_recipient: bool
    :param send_email_receipt_to_uploader: Send delivery receipt to the uploader. Note: For writable share only
    :type send_email_receipt_to_uploader: bool
    :param skip_company: BundleRegistrations can be saved without providing company?
    :type skip_company: bool
    :param skip_email: BundleRegistrations can be saved without providing email?
    :type skip_email: bool
    :param skip_name: BundleRegistrations can be saved without providing name?
    :type skip_name: bool
    :param watermark_attachment_delete: If true, will delete the file stored in watermark_attachment
    :type watermark_attachment_delete: bool
    :param watermark_attachment_file: Preview watermark image applied to all bundle items.
    :type watermark_attachment_file: str

    """
    expires_at = util.deserialize_datetime(expires_at)
    return web.Response(status=200)


async def post_bundles(request: web.Request, paths, clickwrap_id=None, code=None, description=None, dont_separate_submissions_by_folder=None, expires_at=None, form_field_set_id=None, inbox_id=None, max_uses=None, note=None, password=None, path_template=None, permissions=None, preview_only=None, require_registration=None, require_share_recipient=None, send_email_receipt_to_uploader=None, skip_company=None, skip_email=None, skip_name=None, user_id=None, watermark_attachment_file=None) -> web.Response:
    """Create Bundle

    Create Bundle

    :param paths: A list of paths to include in this bundle.
    :type paths: List[str]
    :param clickwrap_id: ID of the clickwrap to use with this bundle.
    :type clickwrap_id: int
    :param code: Bundle code.  This code forms the end part of the Public URL.
    :type code: str
    :param description: Public description
    :type description: str
    :param dont_separate_submissions_by_folder: Do not create subfolders for files uploaded to this share. Note: there are subtle security pitfalls with allowing anonymous uploads from multiple users to live in the same folder. We strongly discourage use of this option unless absolutely required.
    :type dont_separate_submissions_by_folder: bool
    :param expires_at: Bundle expiration date/time
    :type expires_at: str
    :param form_field_set_id: Id of Form Field Set to use with this bundle
    :type form_field_set_id: int
    :param inbox_id: ID of the associated inbox, if available.
    :type inbox_id: int
    :param max_uses: Maximum number of times bundle can be accessed
    :type max_uses: int
    :param note: Bundle internal note
    :type note: str
    :param password: Password for this bundle.
    :type password: str
    :param path_template: Template for creating submission subfolders. Can use the uploader&#39;s name, email address, ip, company, and any custom form data.
    :type path_template: str
    :param permissions: Permissions that apply to Folders in this Share Link.
    :type permissions: str
    :param preview_only: Restrict users to previewing files only?
    :type preview_only: bool
    :param require_registration: Show a registration page that captures the downloader&#39;s name and email address?
    :type require_registration: bool
    :param require_share_recipient: Only allow access to recipients who have explicitly received the share via an email sent through the Files.com UI?
    :type require_share_recipient: bool
    :param send_email_receipt_to_uploader: Send delivery receipt to the uploader. Note: For writable share only
    :type send_email_receipt_to_uploader: bool
    :param skip_company: BundleRegistrations can be saved without providing company?
    :type skip_company: bool
    :param skip_email: BundleRegistrations can be saved without providing email?
    :type skip_email: bool
    :param skip_name: BundleRegistrations can be saved without providing name?
    :type skip_name: bool
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param watermark_attachment_file: Preview watermark image applied to all bundle items.
    :type watermark_attachment_file: str

    """
    expires_at = util.deserialize_datetime(expires_at)
    return web.Response(status=200)


async def post_bundles_id_share(request: web.Request, id, note=None, recipients=None, to=None) -> web.Response:
    """Send email(s) with a link to bundle

    Send email(s) with a link to bundle

    :param id: Bundle ID.
    :type id: int
    :param note: Note to include in email.
    :type note: str
    :param recipients: A list of recipients to share this bundle with. Required unless &#x60;to&#x60; is used.
    :type recipients: List[]
    :param to: A list of email addresses to share this bundle with. Required unless &#x60;recipients&#x60; is used.
    :type to: List[str]

    """
    return web.Response(status=200)
