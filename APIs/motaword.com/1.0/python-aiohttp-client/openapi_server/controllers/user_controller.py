from typing import List, Dict
from aiohttp import web

from openapi_server.models.active_widget import ActiveWidget
from openapi_server.models.client_project_stats import ClientProjectStats
from openapi_server.models.earnings import Earnings
from openapi_server.models.email import Email
from openapi_server.models.error import Error
from openapi_server.models.filter_vendor_request import FilterVendorRequest
from openapi_server.models.location_update_content import LocationUpdateContent
from openapi_server.models.notification_subscription import NotificationSubscription
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.password_update_content import PasswordUpdateContent
from openapi_server.models.payment_info import PaymentInfo
from openapi_server.models.permission_list import PermissionList
from openapi_server.models.popular_language_pairs import PopularLanguagePairs
from openapi_server.models.profile_picture_upload import ProfilePictureUpload
from openapi_server.models.responsivity_list import ResponsivityList
from openapi_server.models.send_email_confirmation200_response import SendEmailConfirmation200Response
from openapi_server.models.send_user_email_confirmation200_response import SendUserEmailConfirmation200Response
from openapi_server.models.send_user_email_confirmation202_response import SendUserEmailConfirmation202Response
from openapi_server.models.stats import Stats
from openapi_server.models.suspend_user_request import SuspendUserRequest
from openapi_server.models.update_payment_info import UpdatePaymentInfo
from openapi_server.models.user import User
from openapi_server.models.user_group_list import UserGroupList
from openapi_server.models.user_list import UserList
from openapi_server.models.user_update_content import UserUpdateContent
from openapi_server.models.vendor_tag import VendorTag
from openapi_server import util


async def approve_vendor_application(request: web.Request, user_id) -> web.Response:
    """approve_vendor_application

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def create_user(request: web.Request, notify=None, body=None) -> web.Response:
    """Create a new user

    Create a new platform user

    :param notify: Send a welcome email to the user
    :type notify: bool
    :param body: 
    :type body: dict | bytes

    """
    body = User.from_dict(body)
    return web.Response(status=200)


async def delete_account(request: web.Request, ) -> web.Response:
    """Delete your account

    Delete your MotaWord account. Be careful; once deleted, you will not have access to MotaWord via API or your dashboards.


    """
    return web.Response(status=200)


async def delete_user_account(request: web.Request, user_id) -> web.Response:
    """Delete requester account

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def downgrade_proofreader(request: web.Request, ) -> web.Response:
    """downgrade_proofreader

    


    """
    return web.Response(status=200)


async def downgrade_user_proofreader(request: web.Request, user_id) -> web.Response:
    """downgrade_user_proofreader

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def freeze_account(request: web.Request, ) -> web.Response:
    """Freeze account

    Freeze your account temporarily, especially to stop receiving project notifications.


    """
    return web.Response(status=200)


async def freeze_user_account(request: web.Request, user_id) -> web.Response:
    """Freeze requester account for project notifications

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_all_vendor_tags(request: web.Request, ) -> web.Response:
    """Returns all vendor tags for vendors filter

    Returns all vendor tags for vendors filter


    """
    return web.Response(status=200)


async def get_earnings(request: web.Request, ) -> web.Response:
    """View your vendor earnings

    View your vendor earnings from your translation activites. Includes real-time earnings from ongoing projects, and fixed earnings from completed projects, as well as total earnings and string edits.


    """
    return web.Response(status=200)


async def get_filtered_vendors(request: web.Request, page=None, per_page=None, order_by=None, order=None, body=None) -> web.Response:
    """Filter vendors based on provided parameters

    Get a list of vendors available for the criteria given

    :param page: The page number
    :type page: int
    :param per_page: The number of items per page
    :type per_page: int
    :param order_by: The field to order the results by
    :type order_by: str
    :param order: The order to sort the results by (ascending or descending)
    :type order: str
    :param body: 
    :type body: dict | bytes

    """
    body = FilterVendorRequest.from_dict(body)
    return web.Response(status=200)


async def get_me(request: web.Request, ) -> web.Response:
    """View your account info

    Get your user information, including client, corporate account and vendor account information.


    """
    return web.Response(status=200)


async def get_payment_info(request: web.Request, ) -> web.Response:
    """View your payment and billing info

    Returns billing and saved credit card information for user, and their corporate account if present &amp; allowed.


    """
    return web.Response(status=200)


async def get_permissions(request: web.Request, ) -> web.Response:
    """View your permissions

    View a list of permissions that your user account is authorized for, configured either by default, or by your account administator.


    """
    return web.Response(status=200)


async def get_responsivity(request: web.Request, period=None) -> web.Response:
    """View your vendor responsiveness

    View your statistical analysis of responsiveness to our translation projects, invitations, notifications and such.

    :param period: Time period to calculate your responsiveness
    :type period: str

    """
    return web.Response(status=200)


async def get_stats(request: web.Request, ) -> web.Response:
    """View your account statistics

    View your client and vendor statistics.


    """
    return web.Response(status=200)


async def get_this_user_groups(request: web.Request, user_id) -> web.Response:
    """Returns a list of user groups that this user belongs to.

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_user(request: web.Request, user_id) -> web.Response:
    """Get user information, including client or vendor specific info.

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_user_earnings(request: web.Request, user_id) -> web.Response:
    """Returns your vendor earnings. Includes real-time earnings from ongoing projects, and fixed earnings from completed projects. Also includes total earnings and string edits.

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_user_groups(request: web.Request, ) -> web.Response:
    """View your user groups

    View the user groups that your user account belongs to. This is typically configured by your account administator&#39;s dashboard.


    """
    return web.Response(status=200)


async def get_user_payment_info(request: web.Request, user_id) -> web.Response:
    """View user&#39;s payment and billing info

    Returns billing and saved credit card information for user, and their corporate account if present &amp; allowed.

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_user_permissions(request: web.Request, user_id) -> web.Response:
    """Returns a list of permissions that this user is authorized for.

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_user_popular_pairs(request: web.Request, user_id) -> web.Response:
    """Returns the language pairs that the user has ordered most.

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_user_project_stats(request: web.Request, user_id) -> web.Response:
    """Returns a user&#39;s project statistics.

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_user_responsivity(request: web.Request, user_id, period=None) -> web.Response:
    """Returns a user&#39;s vendor responsivity stats

    

    :param user_id: User ID
    :type user_id: int
    :param period: Period for calcualtion.
    :type period: str

    """
    return web.Response(status=200)


async def get_user_stats(request: web.Request, user_id) -> web.Response:
    """Returns a user&#39;s client and vendor statistics. This used to be called \&quot;summary\&quot; (\\@deprecated).

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_users(request: web.Request, page=None, per_page=None, user_type=None, search=None, email=None) -> web.Response:
    """Get a list of platform users

    Get a list of platform users

    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param user_type: 
    :type user_type: str
    :param search: 
    :type search: str
    :param email: 
    :type email: str

    """
    return web.Response(status=200)


async def log_location(request: web.Request, body=None) -> web.Response:
    """Log user&#39;s current location. This data is used in our Intelligent Project Manager for various data analysis, including project prioritization for vendors and account validation.

    

    :param body: 
    :type body: dict | bytes

    """
    body = LocationUpdateContent.from_dict(body)
    return web.Response(status=200)


async def make_proofreader(request: web.Request, ) -> web.Response:
    """make_proofreader

    


    """
    return web.Response(status=200)


async def make_user_proofreader(request: web.Request, user_id) -> web.Response:
    """make_user_proofreader

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def reject_vendor_application(request: web.Request, user_id) -> web.Response:
    """reject_vendor_application

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def send_email_confirmation(request: web.Request, ) -> web.Response:
    """Sends email confirmation email for current user

    


    """
    return web.Response(status=200)


async def send_password_reminder(request: web.Request, body=None) -> web.Response:
    """Sends password reset email to the user&#39;s registered email address

    

    :param body: 
    :type body: dict | bytes

    """
    body = Email.from_dict(body)
    return web.Response(status=200)


async def send_user_email_confirmation(request: web.Request, user_id) -> web.Response:
    """Sends email confirmation email for a user

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def subscribe_notification(request: web.Request, body=None) -> web.Response:
    """Subscribe to push notifications

    Subscribe to push notifications to receive project and platform notifications.

    :param body: 
    :type body: dict | bytes

    """
    body = NotificationSubscription.from_dict(body)
    return web.Response(status=200)


async def subscribe_user_notification(request: web.Request, user_id, body=None) -> web.Response:
    """subscribe_user_notification

    

    :param user_id: User ID
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = NotificationSubscription.from_dict(body)
    return web.Response(status=200)


async def suspend_user(request: web.Request, user_id, body=None) -> web.Response:
    """suspend_user

    

    :param user_id: User ID
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SuspendUserRequest.from_dict(body)
    return web.Response(status=200)


async def unfreeze_account(request: web.Request, ) -> web.Response:
    """Defreeze your account

    Reactive your account to start receiving notifications.


    """
    return web.Response(status=200)


async def unfreeze_user_account(request: web.Request, user_id) -> web.Response:
    """Unfreeze requester account for project notifications

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def unsubscribe_notification(request: web.Request, body=None) -> web.Response:
    """unsubscribe_notification

    

    :param body: 
    :type body: dict | bytes

    """
    body = NotificationSubscription.from_dict(body)
    return web.Response(status=200)


async def unsubscribe_user_notification(request: web.Request, user_id, body=None) -> web.Response:
    """unsubscribe_user_notification

    

    :param user_id: User ID
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = NotificationSubscription.from_dict(body)
    return web.Response(status=200)


async def update_me(request: web.Request, body=None) -> web.Response:
    """Update your account info

    

    :param body: 
    :type body: dict | bytes

    """
    body = UserUpdateContent.from_dict(body)
    return web.Response(status=200)


async def update_password(request: web.Request, body=None) -> web.Response:
    """Update your account password

    Password should contain at least one uppercase, lowercase character and one number

    :param body: 
    :type body: dict | bytes

    """
    body = PasswordUpdateContent.from_dict(body)
    return web.Response(status=200)


async def update_payment_info(request: web.Request, body=None) -> web.Response:
    """Update payment info

    Update your billing and saved credit card information

    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePaymentInfo.from_dict(body)
    return web.Response(status=200)


async def update_user(request: web.Request, user_id, body=None) -> web.Response:
    """update_user

    

    :param user_id: User ID
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UserUpdateContent.from_dict(body)
    return web.Response(status=200)


async def update_user_group(request: web.Request, user_id, body=None) -> web.Response:
    """update_user_group

    

    :param user_id: User ID
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ActiveWidget.from_dict(body)
    return web.Response(status=200)


async def update_user_payment_info(request: web.Request, user_id, body=None) -> web.Response:
    """Update user payment info

    Update user&#39;s billing and saved credit card information

    :param user_id: User ID
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentInfo.from_dict(body)
    return web.Response(status=200)


async def upload_profile_picture(request: web.Request, body=None) -> web.Response:
    """Upload profile picture

    Upload a profile picture on your account. This is used where your profile is mentioned throughout the platform. Your picture is not used publicly.

    :param body: 
    :type body: dict | bytes

    """
    body = ProfilePictureUpload.from_dict(body)
    return web.Response(status=200)


async def upload_user_profile_picture(request: web.Request, user_id, body=None) -> web.Response:
    """upload_user_profile_picture

    

    :param user_id: User ID
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProfilePictureUpload.from_dict(body)
    return web.Response(status=200)
