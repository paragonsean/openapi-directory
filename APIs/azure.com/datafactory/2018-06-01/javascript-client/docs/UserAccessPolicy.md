# DataFactoryManagementClient.UserAccessPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessResourcePath** | **String** | The resource path to get access relative to factory. Currently only empty string is supported which corresponds to the factory resource. | [optional] 
**expireTime** | **String** | Expiration time for the token. Maximum duration for the token is eight hours and by default the token will expire in eight hours. | [optional] 
**permissions** | **String** | The string with permissions for Data Plane access. Currently only &#39;r&#39; is supported which grants read only access. | [optional] 
**profileName** | **String** | The name of the profile. Currently only the default is supported. The default value is DefaultProfile. | [optional] 
**startTime** | **String** | Start time for the token. If not specified the current time will be used. | [optional] 


