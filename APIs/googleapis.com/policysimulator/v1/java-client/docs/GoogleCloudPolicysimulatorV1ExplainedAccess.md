

# GoogleCloudPolicysimulatorV1ExplainedAccess

Details about how a set of policies, listed in ExplainedPolicy, resulted in a certain AccessState when replaying an access tuple.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessState** | [**AccessStateEnum**](#AccessStateEnum) | Whether the principal in the access tuple has permission to access the resource in the access tuple under the given policies. |  [optional] |
|**errors** | [**List&lt;GoogleRpcStatus&gt;**](GoogleRpcStatus.md) | If the AccessState is &#x60;UNKNOWN&#x60;, this field contains a list of errors explaining why the result is &#x60;UNKNOWN&#x60;. If the &#x60;AccessState&#x60; is &#x60;GRANTED&#x60; or &#x60;NOT_GRANTED&#x60;, this field is omitted. |  [optional] |
|**policies** | [**List&lt;GoogleCloudPolicysimulatorV1ExplainedPolicy&gt;**](GoogleCloudPolicysimulatorV1ExplainedPolicy.md) | If the AccessState is &#x60;UNKNOWN&#x60;, this field contains the policies that led to that result. If the &#x60;AccessState&#x60; is &#x60;GRANTED&#x60; or &#x60;NOT_GRANTED&#x60;, this field is omitted. |  [optional] |



## Enum: AccessStateEnum

| Name | Value |
|---- | -----|
| ACCESS_STATE_UNSPECIFIED | &quot;ACCESS_STATE_UNSPECIFIED&quot; |
| GRANTED | &quot;GRANTED&quot; |
| NOT_GRANTED | &quot;NOT_GRANTED&quot; |
| UNKNOWN_CONDITIONAL | &quot;UNKNOWN_CONDITIONAL&quot; |
| UNKNOWN_INFO_DENIED | &quot;UNKNOWN_INFO_DENIED&quot; |



