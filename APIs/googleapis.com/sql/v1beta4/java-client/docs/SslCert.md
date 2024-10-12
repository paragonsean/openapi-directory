

# SslCert

SslCerts Resource

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cert** | **String** | PEM representation. |  [optional] |
|**certSerialNumber** | **String** | Serial number, as extracted from the certificate. |  [optional] |
|**commonName** | **String** | User supplied name. Constrained to [a-zA-Z.-_ ]+. |  [optional] |
|**createTime** | **String** | The time when the certificate was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. |  [optional] |
|**expirationTime** | **String** | The time when the certificate expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. |  [optional] |
|**instance** | **String** | Name of the database instance. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#sslCert&#x60;. |  [optional] |
|**selfLink** | **String** | The URI of this resource. |  [optional] |
|**sha1Fingerprint** | **String** | Sha1 Fingerprint. |  [optional] |



