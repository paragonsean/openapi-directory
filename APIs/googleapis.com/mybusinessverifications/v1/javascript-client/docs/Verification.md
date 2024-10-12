# MyBusinessVerificationsApi.Verification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement** | **String** | Optional. Response announcement set only if the method is VETTED_PARTNER. | [optional] 
**createTime** | **String** | The timestamp when the verification is requested. | [optional] 
**method** | **String** | The method of the verification. | [optional] 
**name** | **String** | Resource name of the verification. | [optional] 
**state** | **String** | The state of the verification. | [optional] 



## Enum: MethodEnum


* `VERIFICATION_METHOD_UNSPECIFIED` (value: `"VERIFICATION_METHOD_UNSPECIFIED"`)

* `ADDRESS` (value: `"ADDRESS"`)

* `EMAIL` (value: `"EMAIL"`)

* `PHONE_CALL` (value: `"PHONE_CALL"`)

* `SMS` (value: `"SMS"`)

* `AUTO` (value: `"AUTO"`)

* `VETTED_PARTNER` (value: `"VETTED_PARTNER"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `COMPLETED` (value: `"COMPLETED"`)

* `FAILED` (value: `"FAILED"`)




