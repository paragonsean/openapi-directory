# ApigeeApi.GoogleCloudApigeeV1DeveloperApp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiProducts** | **[String]** | List of API products associated with the developer app. | [optional] 
**appFamily** | **String** | Developer app family. | [optional] 
**appId** | **String** | ID of the developer app. | [optional] 
**attributes** | [**[GoogleCloudApigeeV1Attribute]**](GoogleCloudApigeeV1Attribute.md) | List of attributes for the developer app. | [optional] 
**callbackUrl** | **String** | Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to developer apps. | [optional] 
**createdAt** | **String** | Output only. Time the developer app was created in milliseconds since epoch. | [optional] [readonly] 
**credentials** | [**[GoogleCloudApigeeV1Credential]**](GoogleCloudApigeeV1Credential.md) | Output only. Set of credentials for the developer app consisting of the consumer key/secret pairs associated with the API products. | [optional] [readonly] 
**developerId** | **String** | ID of the developer. | [optional] 
**keyExpiresIn** | **String** | Expiration time, in milliseconds, for the consumer key that is generated for the developer app. If not set or left to the default value of &#x60;-1&#x60;, the API key never expires. The expiration time can&#39;t be updated after it is set. | [optional] 
**lastModifiedAt** | **String** | Output only. Time the developer app was modified in milliseconds since epoch. | [optional] [readonly] 
**name** | **String** | Name of the developer app. | [optional] 
**scopes** | **[String]** | Scopes to apply to the developer app. The specified scopes must already exist for the API product that you associate with the developer app. | [optional] 
**status** | **String** | Status of the credential. Valid values include &#x60;approved&#x60; or &#x60;revoked&#x60;. | [optional] 


