

# As2PartnerEntity

Create As2 Partner

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**as2StationId** | **Integer** | Id of the AS2 Station associated with this partner. |  [optional] |
|**enableDedicatedIps** | **Boolean** | &#x60;true&#x60; if remote server only accepts connections from dedicated IPs |  [optional] |
|**hexPublicCertificateSerial** | **String** | Serial of public certificate used for message security in hex format. |  [optional] |
|**id** | **Integer** | Id of the AS2 Partner. |  [optional] |
|**name** | **String** | The partner&#39;s formal AS2 name. |  [optional] |
|**publicCertificateIssuer** | **String** | Issuer of public certificate used for message security. |  [optional] |
|**publicCertificateMd5** | **String** | MD5 hash of public certificate used for message security. |  [optional] |
|**publicCertificateNotAfter** | **String** | Not after value of public certificate used for message security. |  [optional] |
|**publicCertificateNotBefore** | **String** | Not before value of public certificate used for message security. |  [optional] |
|**publicCertificateSerial** | **String** | Serial of public certificate used for message security. |  [optional] |
|**publicCertificateSubject** | **String** | Subject of public certificate used for message security. |  [optional] |
|**serverCertificate** | [**ServerCertificateEnum**](#ServerCertificateEnum) | Remote server certificate security setting |  [optional] |
|**uri** | **String** | Public URI for sending AS2 message to. |  [optional] |



## Enum: ServerCertificateEnum

| Name | Value |
|---- | -----|
| REQUIRE_MATCH | &quot;require_match&quot; |
| ALLOW_ANY | &quot;allow_any&quot; |



