# ApigeeApi.GoogleCloudApigeeV1App

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiProducts** | [**[GoogleCloudApigeeV1ApiProductRef]**](GoogleCloudApigeeV1ApiProductRef.md) | List of API products associated with the app. | [optional] 
**appGroup** | **String** | Name of the AppGroup | [optional] 
**appId** | **String** | ID of the app. | [optional] 
**attributes** | [**[GoogleCloudApigeeV1Attribute]**](GoogleCloudApigeeV1Attribute.md) | List of attributes. | [optional] 
**callbackUrl** | **String** | Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to apps. | [optional] 
**companyName** | **String** | Name of the company that owns the app. | [optional] 
**createdAt** | **String** | Output only. Unix time when the app was created. | [optional] [readonly] 
**credentials** | [**[GoogleCloudApigeeV1Credential]**](GoogleCloudApigeeV1Credential.md) | Output only. Set of credentials for the app. Credentials are API key/secret pairs associated with API products. | [optional] [readonly] 
**developerEmail** | **String** | Email of the developer. | [optional] 
**developerId** | **String** | ID of the developer. | [optional] 
**keyExpiresIn** | **String** | Duration, in milliseconds, of the consumer key that will be generated for the app. The default value, -1, indicates an infinite validity period. Once set, the expiration can&#39;t be updated. json key: keyExpiresIn | [optional] 
**lastModifiedAt** | **String** | Output only. Last modified time as milliseconds since epoch. | [optional] [readonly] 
**name** | **String** | Name of the app. | [optional] 
**scopes** | **[String]** | Scopes to apply to the app. The specified scope names must already exist on the API product that you associate with the app. | [optional] 
**status** | **String** | Status of the credential. | [optional] 


