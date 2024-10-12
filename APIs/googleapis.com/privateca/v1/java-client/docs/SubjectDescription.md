

# SubjectDescription

These values describe fields in an issued X.509 certificate such as the distinguished name, subject alternative names, serial number, and lifetime.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hexSerialNumber** | **String** | The serial number encoded in lowercase hexadecimal. |  [optional] |
|**lifetime** | **String** | For convenience, the actual lifetime of an issued certificate. |  [optional] |
|**notAfterTime** | **String** | The time after which the certificate is expired. Per RFC 5280, the validity period for a certificate is the period of time from not_before_time through not_after_time, inclusive. Corresponds to &#39;not_before_time&#39; + &#39;lifetime&#39; - 1 second. |  [optional] |
|**notBeforeTime** | **String** | The time at which the certificate becomes valid. |  [optional] |
|**subject** | [**Subject**](Subject.md) |  |  [optional] |
|**subjectAltName** | [**SubjectAltNames**](SubjectAltNames.md) |  |  [optional] |



