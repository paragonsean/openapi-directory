# TwilioApi.ApiV2010AccountToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Token resource. | [optional] 
**dateCreated** | **String** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **String** | The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**iceServers** | [**[ApiV2010AccountTokenIceServersInner]**](ApiV2010AccountTokenIceServersInner.md) | An array representing the ephemeral credentials and the STUN and TURN server URIs. | [optional] 
**password** | **String** | The temporary password that the username will use when authenticating with Twilio. | [optional] 
**ttl** | **String** | The duration in seconds for which the username and password are valid. | [optional] 
**username** | **String** | The temporary username that uniquely identifies a Token. | [optional] 


