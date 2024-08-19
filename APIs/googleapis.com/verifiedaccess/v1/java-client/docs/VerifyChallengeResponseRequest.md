

# VerifyChallengeResponseRequest

signed ChallengeResponse

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**challengeResponse** | [**SignedData**](SignedData.md) |  |  [optional] |
|**expectedIdentity** | **String** | Service can optionally provide identity information about the device or user associated with the key. For an EMK, this value is the enrolled domain. For an EUK, this value is the user&#39;s email address. If present, this value will be checked against contents of the response, and verification will fail if there is no match. |  [optional] |



