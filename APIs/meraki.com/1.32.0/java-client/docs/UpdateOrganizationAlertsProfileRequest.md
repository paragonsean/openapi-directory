

# UpdateOrganizationAlertsProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertCondition** | [**CreateOrganizationAlertsProfileRequestAlertCondition**](CreateOrganizationAlertsProfileRequestAlertCondition.md) |  |  [optional] |
|**description** | **String** | User supplied description of the alert |  [optional] |
|**enabled** | **Boolean** | Is the alert config enabled |  [optional] |
|**networkTags** | **List&lt;String&gt;** | Networks with these tags will be monitored for the alert |  [optional] |
|**recipients** | [**CreateOrganizationAlertsProfileRequestRecipients**](CreateOrganizationAlertsProfileRequestRecipients.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The alert type |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| APP_OUTAGE | &quot;appOutage&quot; |
| VOIP_JITTER | &quot;voipJitter&quot; |
| VOIP_MOS | &quot;voipMos&quot; |
| VOIP_PACKET_LOSS | &quot;voipPacketLoss&quot; |
| WAN_LATENCY | &quot;wanLatency&quot; |
| WAN_PACKET_LOSS | &quot;wanPacketLoss&quot; |
| WAN_STATUS | &quot;wanStatus&quot; |
| WAN_UTILIZATION | &quot;wanUtilization&quot; |



