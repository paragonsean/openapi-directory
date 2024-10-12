# ChromeVerifiedAccessApi.VerifyChallengeResponseRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challengeResponse** | **Blob** | Required. The generated response to the challenge, the bytes representation of SignedData. | [optional] 
**expectedIdentity** | **String** | Optional. Service can optionally provide identity information about the device or user associated with the key. For an EMK, this value is the enrolled domain. For an EUK, this value is the user&#39;s email address. If present, this value will be checked against contents of the response, and verification will fail if there is no match. | [optional] 


