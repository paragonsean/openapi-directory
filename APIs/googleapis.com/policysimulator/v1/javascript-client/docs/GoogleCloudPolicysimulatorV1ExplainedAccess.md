# PolicySimulatorApi.GoogleCloudPolicysimulatorV1ExplainedAccess

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessState** | **String** | Whether the principal in the access tuple has permission to access the resource in the access tuple under the given policies. | [optional] 
**errors** | [**[GoogleRpcStatus]**](GoogleRpcStatus.md) | If the AccessState is &#x60;UNKNOWN&#x60;, this field contains a list of errors explaining why the result is &#x60;UNKNOWN&#x60;. If the &#x60;AccessState&#x60; is &#x60;GRANTED&#x60; or &#x60;NOT_GRANTED&#x60;, this field is omitted. | [optional] 
**policies** | [**[GoogleCloudPolicysimulatorV1ExplainedPolicy]**](GoogleCloudPolicysimulatorV1ExplainedPolicy.md) | If the AccessState is &#x60;UNKNOWN&#x60;, this field contains the policies that led to that result. If the &#x60;AccessState&#x60; is &#x60;GRANTED&#x60; or &#x60;NOT_GRANTED&#x60;, this field is omitted. | [optional] 



## Enum: AccessStateEnum


* `ACCESS_STATE_UNSPECIFIED` (value: `"ACCESS_STATE_UNSPECIFIED"`)

* `GRANTED` (value: `"GRANTED"`)

* `NOT_GRANTED` (value: `"NOT_GRANTED"`)

* `UNKNOWN_CONDITIONAL` (value: `"UNKNOWN_CONDITIONAL"`)

* `UNKNOWN_INFO_DENIED` (value: `"UNKNOWN_INFO_DENIED"`)




