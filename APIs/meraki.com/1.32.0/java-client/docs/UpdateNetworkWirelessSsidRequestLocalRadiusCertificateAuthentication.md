

# UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthentication

The current setting for certificate verification.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRootCaCertificate** | [**UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthenticationClientRootCaCertificate**](UpdateNetworkWirelessSsidRequestLocalRadiusCertificateAuthenticationClientRootCaCertificate.md) |  |  [optional] |
|**enabled** | **Boolean** | Whether or not to use EAP-TLS certificate-based authentication to validate wireless clients. |  [optional] |
|**ocspResponderUrl** | **String** | (Optional) The URL of the OCSP responder to verify client certificate status. |  [optional] |
|**useLdap** | **Boolean** | Whether or not to verify the certificate with LDAP. |  [optional] |
|**useOcsp** | **Boolean** | Whether or not to verify the certificate with OCSP. |  [optional] |



