

# GoogleCloudApigeeV1AppGroupAppKey

AppGroupAppKey contains all the information associated with the credentials.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiProducts** | [**List&lt;GoogleCloudApigeeV1APIProductAssociation&gt;**](GoogleCloudApigeeV1APIProductAssociation.md) | Output only. List of API products and its status for which the credential can be used. **Note**: Use UpdateAppGroupAppKeyApiProductRequest API to make the association after the consumer key and secret are created. |  [optional] [readonly] |
|**attributes** | [**List&lt;GoogleCloudApigeeV1Attribute&gt;**](GoogleCloudApigeeV1Attribute.md) | List of attributes associated with the credential. |  [optional] |
|**consumerKey** | **String** | Immutable. Consumer key. |  [optional] |
|**consumerSecret** | **String** | Secret key. |  [optional] |
|**expiresAt** | **String** | Output only. Time the AppGroup app expires in milliseconds since epoch. |  [optional] [readonly] |
|**expiresInSeconds** | **String** | Immutable. Expiration time, in seconds, for the consumer key. If not set or left to the default value of &#x60;-1&#x60;, the API key never expires. The expiration time can&#39;t be updated after it is set. |  [optional] |
|**issuedAt** | **String** | Output only. Time the AppGroup app was created in milliseconds since epoch. |  [optional] [readonly] |
|**scopes** | **List&lt;String&gt;** | Scopes to apply to the app. The specified scope names must already be defined for the API product that you associate with the app. |  [optional] |
|**status** | **String** | Status of the credential. Valid values include &#x60;approved&#x60; or &#x60;revoked&#x60;. |  [optional] |



