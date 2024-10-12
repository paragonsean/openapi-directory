

# IpFilterRule

The IP filter rules for the IoT hub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | The desired action for requests captured by this rule. |  |
|**filterName** | **String** | The name of the IP filter rule. |  |
|**ipMask** | **String** | A string that contains the IP address range in CIDR notation for the rule. |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ACCEPT | &quot;Accept&quot; |
| REJECT | &quot;Reject&quot; |



