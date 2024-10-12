# TwilioVerify.VerifyV2ServiceAccessToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique SID identifier of the Account. | [optional] 
**dateCreated** | **Date** | The date that this access token was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**entityIdentity** | **String** | The unique external identifier for the Entity of the Service. | [optional] 
**factorFriendlyName** | **String** | A human readable description of this factor, up to 64 characters. For a push factor, this can be the device&#39;s name. | [optional] 
**factorType** | [**AccessTokenEnumFactorTypes**](AccessTokenEnumFactorTypes.md) |  | [optional] 
**serviceSid** | **String** | The unique SID identifier of the Verify Service. | [optional] 
**sid** | **String** | A 34 character string that uniquely identifies this Access Token. | [optional] 
**token** | **String** | The access token generated for enrollment, this is an encrypted json web token. | [optional] 
**ttl** | **Number** | How long, in seconds, the access token is valid. Max: 5 minutes | [optional] 
**url** | **String** | The URL of this resource. | [optional] 


