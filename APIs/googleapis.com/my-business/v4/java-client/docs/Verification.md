

# Verification

A verification represents a verification attempt on a location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The timestamp when the verification is requested. |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) | The method of the verification. |  [optional] |
|**name** | **String** | Resource name of the verification. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the verification. |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| VERIFICATION_METHOD_UNSPECIFIED | &quot;VERIFICATION_METHOD_UNSPECIFIED&quot; |
| ADDRESS | &quot;ADDRESS&quot; |
| EMAIL | &quot;EMAIL&quot; |
| PHONE_CALL | &quot;PHONE_CALL&quot; |
| SMS | &quot;SMS&quot; |
| AUTO | &quot;AUTO&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| VERIFICATION_STATE_UNSPECIFIED | &quot;VERIFICATION_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| FAILED | &quot;FAILED&quot; |



