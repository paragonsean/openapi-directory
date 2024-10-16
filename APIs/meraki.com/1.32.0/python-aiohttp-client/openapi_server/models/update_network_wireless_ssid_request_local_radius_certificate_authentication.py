# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_network_wireless_ssid_request_local_radius_certificate_authentication_client_root_ca_certificate import UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthenticationClientRootCaCertificate
from openapi_server import util


class UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, client_root_ca_certificate: UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthenticationClientRootCaCertificate=None, enabled: bool=None, ocsp_responder_url: str=None, use_ldap: bool=None, use_ocsp: bool=None):
        """UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication - a model defined in OpenAPI

        :param client_root_ca_certificate: The client_root_ca_certificate of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :param enabled: The enabled of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :param ocsp_responder_url: The ocsp_responder_url of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :param use_ldap: The use_ldap of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :param use_ocsp: The use_ocsp of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        """
        self.openapi_types = {
            'client_root_ca_certificate': UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthenticationClientRootCaCertificate,
            'enabled': bool,
            'ocsp_responder_url': str,
            'use_ldap': bool,
            'use_ocsp': bool
        }

        self.attribute_map = {
            'client_root_ca_certificate': 'clientRootCaCertificate',
            'enabled': 'enabled',
            'ocsp_responder_url': 'ocspResponderUrl',
            'use_ldap': 'useLdap',
            'use_ocsp': 'useOcsp'
        }

        self._client_root_ca_certificate = client_root_ca_certificate
        self._enabled = enabled
        self._ocsp_responder_url = ocsp_responder_url
        self._use_ldap = use_ldap
        self._use_ocsp = use_ocsp

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkWirelessSsid_request_localRadius_certificateAuthentication of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_root_ca_certificate(self):
        """Gets the client_root_ca_certificate of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.


        :return: The client_root_ca_certificate of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :rtype: UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthenticationClientRootCaCertificate
        """
        return self._client_root_ca_certificate

    @client_root_ca_certificate.setter
    def client_root_ca_certificate(self, client_root_ca_certificate):
        """Sets the client_root_ca_certificate of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.


        :param client_root_ca_certificate: The client_root_ca_certificate of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :type client_root_ca_certificate: UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthenticationClientRootCaCertificate
        """

        self._client_root_ca_certificate = client_root_ca_certificate

    @property
    def enabled(self):
        """Gets the enabled of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.

        Whether or not to use EAP-TLS certificate-based authentication to validate wireless clients.

        :return: The enabled of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.

        Whether or not to use EAP-TLS certificate-based authentication to validate wireless clients.

        :param enabled: The enabled of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def ocsp_responder_url(self):
        """Gets the ocsp_responder_url of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.

        (Optional) The URL of the OCSP responder to verify client certificate status.

        :return: The ocsp_responder_url of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :rtype: str
        """
        return self._ocsp_responder_url

    @ocsp_responder_url.setter
    def ocsp_responder_url(self, ocsp_responder_url):
        """Sets the ocsp_responder_url of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.

        (Optional) The URL of the OCSP responder to verify client certificate status.

        :param ocsp_responder_url: The ocsp_responder_url of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :type ocsp_responder_url: str
        """

        self._ocsp_responder_url = ocsp_responder_url

    @property
    def use_ldap(self):
        """Gets the use_ldap of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.

        Whether or not to verify the certificate with LDAP.

        :return: The use_ldap of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :rtype: bool
        """
        return self._use_ldap

    @use_ldap.setter
    def use_ldap(self, use_ldap):
        """Sets the use_ldap of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.

        Whether or not to verify the certificate with LDAP.

        :param use_ldap: The use_ldap of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :type use_ldap: bool
        """

        self._use_ldap = use_ldap

    @property
    def use_ocsp(self):
        """Gets the use_ocsp of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.

        Whether or not to verify the certificate with OCSP.

        :return: The use_ocsp of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :rtype: bool
        """
        return self._use_ocsp

    @use_ocsp.setter
    def use_ocsp(self, use_ocsp):
        """Sets the use_ocsp of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.

        Whether or not to verify the certificate with OCSP.

        :param use_ocsp: The use_ocsp of this UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication.
        :type use_ocsp: bool
        """

        self._use_ocsp = use_ocsp
