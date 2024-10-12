# ChecksApi.HookOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hooks** | [**[Hook]**](Hook.md) | List of hooks in current page. | [optional] 
**next** | **String** | Next page URL | [optional] 
**self** | **String** | Current page URL | [optional] 
**signingKey** | **String** | HMAC key needed to decode the JWTs you will receive. All events are sent in JWT format, this key is needed in order to ensure that only authorized users can decode the information. | [optional] 


