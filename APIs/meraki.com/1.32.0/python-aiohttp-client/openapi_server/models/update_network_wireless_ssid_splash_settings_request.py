# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_network_wireless_ssid_splash_settings_request_billing import UpdateNetworkWirelessSsidSplashSettingsRequestBilling
from openapi_server.models.update_network_wireless_ssid_splash_settings_request_guest_sponsorship import UpdateNetworkWirelessSsidSplashSettingsRequestGuestSponsorship
from openapi_server.models.update_network_wireless_ssid_splash_settings_request_sentry_enrollment import UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment
from openapi_server.models.update_network_wireless_ssid_splash_settings_request_splash_image import UpdateNetworkWirelessSsidSplashSettingsRequestSplashImage
from openapi_server.models.update_network_wireless_ssid_splash_settings_request_splash_logo import UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo
from openapi_server.models.update_network_wireless_ssid_splash_settings_request_splash_prepaid_front import UpdateNetworkWirelessSsidSplashSettingsRequestSplashPrepaidFront
from openapi_server import util


class UpdateNetworkWirelessSsidSplashSettingsRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, allow_simultaneous_logins: bool=None, billing: UpdateNetworkWirelessSsidSplashSettingsRequestBilling=None, block_all_traffic_before_sign_on: bool=None, controller_disconnection_behavior: str=None, guest_sponsorship: UpdateNetworkWirelessSsidSplashSettingsRequestGuestSponsorship=None, redirect_url: str=None, sentry_enrollment: UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment=None, splash_image: UpdateNetworkWirelessSsidSplashSettingsRequestSplashImage=None, splash_logo: UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo=None, splash_prepaid_front: UpdateNetworkWirelessSsidSplashSettingsRequestSplashPrepaidFront=None, splash_timeout: int=None, splash_url: str=None, use_redirect_url: bool=None, use_splash_url: bool=None, welcome_message: str=None):
        """UpdateNetworkWirelessSsidSplashSettingsRequest - a model defined in OpenAPI

        :param allow_simultaneous_logins: The allow_simultaneous_logins of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param billing: The billing of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param block_all_traffic_before_sign_on: The block_all_traffic_before_sign_on of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param controller_disconnection_behavior: The controller_disconnection_behavior of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param guest_sponsorship: The guest_sponsorship of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param redirect_url: The redirect_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param sentry_enrollment: The sentry_enrollment of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param splash_image: The splash_image of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param splash_logo: The splash_logo of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param splash_prepaid_front: The splash_prepaid_front of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param splash_timeout: The splash_timeout of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param splash_url: The splash_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param use_redirect_url: The use_redirect_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param use_splash_url: The use_splash_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :param welcome_message: The welcome_message of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        """
        self.openapi_types = {
            'allow_simultaneous_logins': bool,
            'billing': UpdateNetworkWirelessSsidSplashSettingsRequestBilling,
            'block_all_traffic_before_sign_on': bool,
            'controller_disconnection_behavior': str,
            'guest_sponsorship': UpdateNetworkWirelessSsidSplashSettingsRequestGuestSponsorship,
            'redirect_url': str,
            'sentry_enrollment': UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment,
            'splash_image': UpdateNetworkWirelessSsidSplashSettingsRequestSplashImage,
            'splash_logo': UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo,
            'splash_prepaid_front': UpdateNetworkWirelessSsidSplashSettingsRequestSplashPrepaidFront,
            'splash_timeout': int,
            'splash_url': str,
            'use_redirect_url': bool,
            'use_splash_url': bool,
            'welcome_message': str
        }

        self.attribute_map = {
            'allow_simultaneous_logins': 'allowSimultaneousLogins',
            'billing': 'billing',
            'block_all_traffic_before_sign_on': 'blockAllTrafficBeforeSignOn',
            'controller_disconnection_behavior': 'controllerDisconnectionBehavior',
            'guest_sponsorship': 'guestSponsorship',
            'redirect_url': 'redirectUrl',
            'sentry_enrollment': 'sentryEnrollment',
            'splash_image': 'splashImage',
            'splash_logo': 'splashLogo',
            'splash_prepaid_front': 'splashPrepaidFront',
            'splash_timeout': 'splashTimeout',
            'splash_url': 'splashUrl',
            'use_redirect_url': 'useRedirectUrl',
            'use_splash_url': 'useSplashUrl',
            'welcome_message': 'welcomeMessage'
        }

        self._allow_simultaneous_logins = allow_simultaneous_logins
        self._billing = billing
        self._block_all_traffic_before_sign_on = block_all_traffic_before_sign_on
        self._controller_disconnection_behavior = controller_disconnection_behavior
        self._guest_sponsorship = guest_sponsorship
        self._redirect_url = redirect_url
        self._sentry_enrollment = sentry_enrollment
        self._splash_image = splash_image
        self._splash_logo = splash_logo
        self._splash_prepaid_front = splash_prepaid_front
        self._splash_timeout = splash_timeout
        self._splash_url = splash_url
        self._use_redirect_url = use_redirect_url
        self._use_splash_url = use_splash_url
        self._welcome_message = welcome_message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkWirelessSsidSplashSettingsRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkWirelessSsidSplashSettings_request of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def allow_simultaneous_logins(self):
        """Gets the allow_simultaneous_logins of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        Whether or not to allow simultaneous logins from different devices.

        :return: The allow_simultaneous_logins of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: bool
        """
        return self._allow_simultaneous_logins

    @allow_simultaneous_logins.setter
    def allow_simultaneous_logins(self, allow_simultaneous_logins):
        """Sets the allow_simultaneous_logins of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        Whether or not to allow simultaneous logins from different devices.

        :param allow_simultaneous_logins: The allow_simultaneous_logins of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type allow_simultaneous_logins: bool
        """

        self._allow_simultaneous_logins = allow_simultaneous_logins

    @property
    def billing(self):
        """Gets the billing of this UpdateNetworkWirelessSsidSplashSettingsRequest.


        :return: The billing of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: UpdateNetworkWirelessSsidSplashSettingsRequestBilling
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this UpdateNetworkWirelessSsidSplashSettingsRequest.


        :param billing: The billing of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type billing: UpdateNetworkWirelessSsidSplashSettingsRequestBilling
        """

        self._billing = billing

    @property
    def block_all_traffic_before_sign_on(self):
        """Gets the block_all_traffic_before_sign_on of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        How restricted allowing traffic should be. If true, all traffic types are blocked until the splash page is acknowledged. If false, all non-HTTP traffic is allowed before the splash page is acknowledged.

        :return: The block_all_traffic_before_sign_on of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: bool
        """
        return self._block_all_traffic_before_sign_on

    @block_all_traffic_before_sign_on.setter
    def block_all_traffic_before_sign_on(self, block_all_traffic_before_sign_on):
        """Sets the block_all_traffic_before_sign_on of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        How restricted allowing traffic should be. If true, all traffic types are blocked until the splash page is acknowledged. If false, all non-HTTP traffic is allowed before the splash page is acknowledged.

        :param block_all_traffic_before_sign_on: The block_all_traffic_before_sign_on of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type block_all_traffic_before_sign_on: bool
        """

        self._block_all_traffic_before_sign_on = block_all_traffic_before_sign_on

    @property
    def controller_disconnection_behavior(self):
        """Gets the controller_disconnection_behavior of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        How login attempts should be handled when the controller is unreachable. Can be either 'open', 'restricted', or 'default'.

        :return: The controller_disconnection_behavior of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: str
        """
        return self._controller_disconnection_behavior

    @controller_disconnection_behavior.setter
    def controller_disconnection_behavior(self, controller_disconnection_behavior):
        """Sets the controller_disconnection_behavior of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        How login attempts should be handled when the controller is unreachable. Can be either 'open', 'restricted', or 'default'.

        :param controller_disconnection_behavior: The controller_disconnection_behavior of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type controller_disconnection_behavior: str
        """
        allowed_values = ["default", "open", "restricted"]  # noqa: E501
        if controller_disconnection_behavior not in allowed_values:
            raise ValueError(
                "Invalid value for `controller_disconnection_behavior` ({0}), must be one of {1}"
                .format(controller_disconnection_behavior, allowed_values)
            )

        self._controller_disconnection_behavior = controller_disconnection_behavior

    @property
    def guest_sponsorship(self):
        """Gets the guest_sponsorship of this UpdateNetworkWirelessSsidSplashSettingsRequest.


        :return: The guest_sponsorship of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: UpdateNetworkWirelessSsidSplashSettingsRequestGuestSponsorship
        """
        return self._guest_sponsorship

    @guest_sponsorship.setter
    def guest_sponsorship(self, guest_sponsorship):
        """Sets the guest_sponsorship of this UpdateNetworkWirelessSsidSplashSettingsRequest.


        :param guest_sponsorship: The guest_sponsorship of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type guest_sponsorship: UpdateNetworkWirelessSsidSplashSettingsRequestGuestSponsorship
        """

        self._guest_sponsorship = guest_sponsorship

    @property
    def redirect_url(self):
        """Gets the redirect_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        The custom redirect URL where the users will go after the splash page.

        :return: The redirect_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        The custom redirect URL where the users will go after the splash page.

        :param redirect_url: The redirect_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type redirect_url: str
        """

        self._redirect_url = redirect_url

    @property
    def sentry_enrollment(self):
        """Gets the sentry_enrollment of this UpdateNetworkWirelessSsidSplashSettingsRequest.


        :return: The sentry_enrollment of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment
        """
        return self._sentry_enrollment

    @sentry_enrollment.setter
    def sentry_enrollment(self, sentry_enrollment):
        """Sets the sentry_enrollment of this UpdateNetworkWirelessSsidSplashSettingsRequest.


        :param sentry_enrollment: The sentry_enrollment of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type sentry_enrollment: UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment
        """

        self._sentry_enrollment = sentry_enrollment

    @property
    def splash_image(self):
        """Gets the splash_image of this UpdateNetworkWirelessSsidSplashSettingsRequest.


        :return: The splash_image of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: UpdateNetworkWirelessSsidSplashSettingsRequestSplashImage
        """
        return self._splash_image

    @splash_image.setter
    def splash_image(self, splash_image):
        """Sets the splash_image of this UpdateNetworkWirelessSsidSplashSettingsRequest.


        :param splash_image: The splash_image of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type splash_image: UpdateNetworkWirelessSsidSplashSettingsRequestSplashImage
        """

        self._splash_image = splash_image

    @property
    def splash_logo(self):
        """Gets the splash_logo of this UpdateNetworkWirelessSsidSplashSettingsRequest.


        :return: The splash_logo of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo
        """
        return self._splash_logo

    @splash_logo.setter
    def splash_logo(self, splash_logo):
        """Sets the splash_logo of this UpdateNetworkWirelessSsidSplashSettingsRequest.


        :param splash_logo: The splash_logo of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type splash_logo: UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo
        """

        self._splash_logo = splash_logo

    @property
    def splash_prepaid_front(self):
        """Gets the splash_prepaid_front of this UpdateNetworkWirelessSsidSplashSettingsRequest.


        :return: The splash_prepaid_front of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: UpdateNetworkWirelessSsidSplashSettingsRequestSplashPrepaidFront
        """
        return self._splash_prepaid_front

    @splash_prepaid_front.setter
    def splash_prepaid_front(self, splash_prepaid_front):
        """Sets the splash_prepaid_front of this UpdateNetworkWirelessSsidSplashSettingsRequest.


        :param splash_prepaid_front: The splash_prepaid_front of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type splash_prepaid_front: UpdateNetworkWirelessSsidSplashSettingsRequestSplashPrepaidFront
        """

        self._splash_prepaid_front = splash_prepaid_front

    @property
    def splash_timeout(self):
        """Gets the splash_timeout of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        Splash timeout in minutes. This will determine how often users will see the splash page.

        :return: The splash_timeout of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: int
        """
        return self._splash_timeout

    @splash_timeout.setter
    def splash_timeout(self, splash_timeout):
        """Sets the splash_timeout of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        Splash timeout in minutes. This will determine how often users will see the splash page.

        :param splash_timeout: The splash_timeout of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type splash_timeout: int
        """

        self._splash_timeout = splash_timeout

    @property
    def splash_url(self):
        """Gets the splash_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        [optional] The custom splash URL of the click-through splash page. Note that the URL can be configured without necessarily being used. In order to enable the custom URL, see 'useSplashUrl'

        :return: The splash_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: str
        """
        return self._splash_url

    @splash_url.setter
    def splash_url(self, splash_url):
        """Sets the splash_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        [optional] The custom splash URL of the click-through splash page. Note that the URL can be configured without necessarily being used. In order to enable the custom URL, see 'useSplashUrl'

        :param splash_url: The splash_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type splash_url: str
        """

        self._splash_url = splash_url

    @property
    def use_redirect_url(self):
        """Gets the use_redirect_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        The Boolean indicating whether the the user will be redirected to the custom redirect URL after the splash page. A custom redirect URL must be set if this is true.

        :return: The use_redirect_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: bool
        """
        return self._use_redirect_url

    @use_redirect_url.setter
    def use_redirect_url(self, use_redirect_url):
        """Sets the use_redirect_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        The Boolean indicating whether the the user will be redirected to the custom redirect URL after the splash page. A custom redirect URL must be set if this is true.

        :param use_redirect_url: The use_redirect_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type use_redirect_url: bool
        """

        self._use_redirect_url = use_redirect_url

    @property
    def use_splash_url(self):
        """Gets the use_splash_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        [optional] Boolean indicating whether the users will be redirected to the custom splash url. A custom splash URL must be set if this is true. Note that depending on your SSID's access control settings, it may not be possible to use the custom splash URL.

        :return: The use_splash_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: bool
        """
        return self._use_splash_url

    @use_splash_url.setter
    def use_splash_url(self, use_splash_url):
        """Sets the use_splash_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        [optional] Boolean indicating whether the users will be redirected to the custom splash url. A custom splash URL must be set if this is true. Note that depending on your SSID's access control settings, it may not be possible to use the custom splash URL.

        :param use_splash_url: The use_splash_url of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type use_splash_url: bool
        """

        self._use_splash_url = use_splash_url

    @property
    def welcome_message(self):
        """Gets the welcome_message of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        The welcome message for the users on the splash page.

        :return: The welcome_message of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :rtype: str
        """
        return self._welcome_message

    @welcome_message.setter
    def welcome_message(self, welcome_message):
        """Sets the welcome_message of this UpdateNetworkWirelessSsidSplashSettingsRequest.

        The welcome message for the users on the splash page.

        :param welcome_message: The welcome_message of this UpdateNetworkWirelessSsidSplashSettingsRequest.
        :type welcome_message: str
        """

        self._welcome_message = welcome_message
