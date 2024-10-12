# ApigeeApi.GoogleCloudApigeeV1DeveloperAppKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiProducts** | **[Object]** | List of API products for which the credential can be used. **Note**: Do not specify the list of API products when creating a consumer key and secret for a developer app. Instead, use the UpdateDeveloperAppKey API to make the association after the consumer key and secret are created. | [optional] 
**attributes** | [**[GoogleCloudApigeeV1Attribute]**](GoogleCloudApigeeV1Attribute.md) | List of attributes associated with the credential. | [optional] 
**consumerKey** | **String** | Consumer key. | [optional] 
**consumerSecret** | **String** | Secret key. | [optional] 
**expiresAt** | **String** | Time the developer app expires in milliseconds since epoch. | [optional] 
**expiresInSeconds** | **String** | Input only. Expiration time, in seconds, for the consumer key. If not set or left to the default value of &#x60;-1&#x60;, the API key never expires. The expiration time can&#39;t be updated after it is set. | [optional] 
**issuedAt** | **String** | Time the developer app was created in milliseconds since epoch. | [optional] 
**scopes** | **[String]** | Scopes to apply to the app. The specified scope names must already be defined for the API product that you associate with the app. | [optional] 
**status** | **String** | Status of the credential. Valid values include &#x60;approved&#x60; or &#x60;revoked&#x60;. | [optional] 


