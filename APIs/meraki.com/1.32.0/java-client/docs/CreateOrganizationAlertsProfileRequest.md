

# CreateOrganizationAlertsProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertCondition** | [**CreateOrganizationAlertsProfileRequestAlertCondition**](CreateOrganizationAlertsProfileRequestAlertCondition.md) |  |  |
|**description** | **String** | User supplied description of the alert |  [optional] |
|**networkTags** | **List&lt;String&gt;** | Networks with these tags will be monitored for the alert |  |
|**recipients** | [**CreateOrganizationAlertsProfileRequestRecipients**](CreateOrganizationAlertsProfileRequestRecipients.md) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) | The alert type |  |



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



