

# SystemInfo

System information (default language and authentication methods)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authMethods** | [**List&lt;AuthMethod&gt;**](AuthMethod.md) | &amp;#128679; Deprecated since v4.13.0  Authentication methods:  * &#x60;sql&#x60;  * &#x60;active_directory&#x60;  * &#x60;radius&#x60;  * &#x60;openid&#x60;  use &#x60;authData&#x60; instead |  |
|**hideLoginInputFields** | **Boolean** | &amp;#128679; Deprecated since v4.42.0  Defines if login fields should be hidden |  |
|**languageDefault** | **String** | System default language  cf. [RFC 5646](https://tools.ietf.org/html/rfc5646) |  |
|**s3EnforceDirectUpload** | **Boolean** | &amp;#128640; Since v4.15.0  Determines whether S3 direct upload is enforced or not |  |
|**s3Hosts** | **List&lt;String&gt;** | &amp;#128640; Since v4.14.0  List of S3 Hosts for CSP header |  |
|**useS3Storage** | **Boolean** | &amp;#128640; Since v4.21.0  Defines if S3 is used as storage backend |  |



