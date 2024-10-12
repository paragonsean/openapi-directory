# DispatchApi.FailoverProperty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditionStatus** | **String** | Set the status the message must reach in the expiry_time before failing over. Options are delivered or read. | [optional] 
**expiryTime** | **Number** | In seconds. Minimum value is 15 and maximum value is 86,400 seconds (1 day). | [optional] 



## Enum: ConditionStatusEnum


* `delivered` (value: `"delivered"`)

* `read` (value: `"read"`)




