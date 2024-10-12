

# DeviceCodeData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceCode** | **String** | 40-character code for the device to input into the /token endpoint, not for display to the user |  |
|**expiresIn** | **Integer** | The number of seconds for which this set of codes will be valid, after which they will be purged |  |
|**interval** | **Integer** | The number of seconds the client application should maintain between requests to the /token endpoint |  |
|**userCode** | **String** | 6-character alphanumeric code for the user to enter at http://npr.org/device, to be displayed by the client application |  |
|**verificationUri** | **String** | The URL where the user should input their code, to be displayed by the client application |  |



