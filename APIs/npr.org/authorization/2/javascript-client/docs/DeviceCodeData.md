# NprAuthorizationService.DeviceCodeData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviceCode** | **String** | 40-character code for the device to input into the /token endpoint, not for display to the user | 
**expiresIn** | **Number** | The number of seconds for which this set of codes will be valid, after which they will be purged | [default to 1800]
**interval** | **Number** | The number of seconds the client application should maintain between requests to the /token endpoint | [default to 5]
**userCode** | **String** | 6-character alphanumeric code for the user to enter at http://npr.org/device, to be displayed by the client application | 
**verificationUri** | **String** | The URL where the user should input their code, to be displayed by the client application | [default to &#39;http://npr.org/device&#39;]


