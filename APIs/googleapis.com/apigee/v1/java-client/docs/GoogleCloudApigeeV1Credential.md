

# GoogleCloudApigeeV1Credential


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiProducts** | [**List&lt;GoogleCloudApigeeV1ApiProductRef&gt;**](GoogleCloudApigeeV1ApiProductRef.md) | List of API products this credential can be used for. |  [optional] |
|**attributes** | [**List&lt;GoogleCloudApigeeV1Attribute&gt;**](GoogleCloudApigeeV1Attribute.md) | List of attributes associated with this credential. |  [optional] |
|**consumerKey** | **String** | Consumer key. |  [optional] |
|**consumerSecret** | **String** | Secret key. |  [optional] |
|**expiresAt** | **String** | Time the credential will expire in milliseconds since epoch. |  [optional] |
|**issuedAt** | **String** | Time the credential was issued in milliseconds since epoch. |  [optional] |
|**scopes** | **List&lt;String&gt;** | List of scopes to apply to the app. Specified scopes must already exist on the API product that you associate with the app. |  [optional] |
|**status** | **String** | Status of the credential. Valid values include &#x60;approved&#x60; or &#x60;revoked&#x60;. |  [optional] |



