

# GoogleCloudApigeeV1TlsInfo

TLS configuration information for virtual hosts and TargetServers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ciphers** | **List&lt;String&gt;** | The SSL/TLS cipher suites to be used. For programmable proxies, it must be one of the cipher suite names listed in: http://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#ciphersuites. For configurable proxies, it must follow the configuration specified in: https://commondatastorage.googleapis.com/chromium-boringssl-docs/ssl.h.html#Cipher-suite-configuration. This setting has no effect for configurable proxies when negotiating TLS 1.3. |  [optional] |
|**clientAuthEnabled** | **Boolean** | Optional. Enables two-way TLS. |  [optional] |
|**commonName** | [**GoogleCloudApigeeV1TlsInfoCommonName**](GoogleCloudApigeeV1TlsInfoCommonName.md) |  |  [optional] |
|**enabled** | **Boolean** | Required. Enables TLS. If false, neither one-way nor two-way TLS will be enabled. |  [optional] |
|**ignoreValidationErrors** | **Boolean** | If true, Edge ignores TLS certificate errors. Valid when configuring TLS for target servers and target endpoints, and when configuring virtual hosts that use 2-way TLS. When used with a target endpoint/target server, if the backend system uses SNI and returns a cert with a subject Distinguished Name (DN) that does not match the hostname, there is no way to ignore the error and the connection fails. |  [optional] |
|**keyAlias** | **String** | Required if &#x60;client_auth_enabled&#x60; is true. The resource ID for the alias containing the private key and cert. |  [optional] |
|**keyStore** | **String** | Required if &#x60;client_auth_enabled&#x60; is true. The resource ID of the keystore. |  [optional] |
|**protocols** | **List&lt;String&gt;** | The TLS versioins to be used. |  [optional] |
|**trustStore** | **String** | The resource ID of the truststore. |  [optional] |



