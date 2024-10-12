

# RadiusConfigCreateRequest

Request model for creating a RADIUS configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failoverServer** | [**FailoverServer**](FailoverServer.md) |  |  [optional] |
|**ipAddress** | **String** | RADIUS Server IP Address |  |
|**otpPinFirst** | **Boolean** | Sequence order of concatenated PIN and one-time token |  [optional] |
|**port** | **Integer** | RADIUS Server Port |  |
|**sharedSecret** | **String** | Shared Secret to access the RADIUS server |  |



