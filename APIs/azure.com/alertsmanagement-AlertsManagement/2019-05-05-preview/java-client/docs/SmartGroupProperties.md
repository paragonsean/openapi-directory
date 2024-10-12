

# SmartGroupProperties

Properties of smart group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertSeverities** | [**List&lt;SmartGroupAggregatedProperty&gt;**](SmartGroupAggregatedProperty.md) | Summary of alertSeverities in the smart group |  [optional] |
|**alertStates** | [**List&lt;SmartGroupAggregatedProperty&gt;**](SmartGroupAggregatedProperty.md) | Summary of alertStates in the smart group |  [optional] |
|**alertsCount** | **Integer** | Total number of alerts in smart group |  [optional] |
|**lastModifiedDateTime** | **OffsetDateTime** | Last updated time of smart group. Date-Time in ISO-8601 format. |  [optional] [readonly] |
|**lastModifiedUserName** | **String** | Last modified by user name. |  [optional] [readonly] |
|**monitorConditions** | [**List&lt;SmartGroupAggregatedProperty&gt;**](SmartGroupAggregatedProperty.md) | Summary of monitorConditions in the smart group |  [optional] |
|**monitorServices** | [**List&lt;SmartGroupAggregatedProperty&gt;**](SmartGroupAggregatedProperty.md) | Summary of monitorServices in the smart group |  [optional] |
|**nextLink** | **String** | The URI to fetch the next page of alerts. Call ListNext() with this URI to fetch the next page alerts. |  [optional] |
|**resourceGroups** | [**List&lt;SmartGroupAggregatedProperty&gt;**](SmartGroupAggregatedProperty.md) | Summary of target resource groups in the smart group |  [optional] |
|**resourceTypes** | [**List&lt;SmartGroupAggregatedProperty&gt;**](SmartGroupAggregatedProperty.md) | Summary of target resource types in the smart group |  [optional] |
|**resources** | [**List&lt;SmartGroupAggregatedProperty&gt;**](SmartGroupAggregatedProperty.md) | Summary of target resources in the smart group |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Severity of smart group is the highest(Sev0 &gt;... &gt; Sev4) severity of all the alerts in the group. |  [optional] [readonly] |
|**smartGroupState** | [**SmartGroupStateEnum**](#SmartGroupStateEnum) | Smart group state |  [optional] [readonly] |
|**startDateTime** | **OffsetDateTime** | Creation time of smart group. Date-Time in ISO-8601 format. |  [optional] [readonly] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEV0 | &quot;Sev0&quot; |
| SEV1 | &quot;Sev1&quot; |
| SEV2 | &quot;Sev2&quot; |
| SEV3 | &quot;Sev3&quot; |
| SEV4 | &quot;Sev4&quot; |



## Enum: SmartGroupStateEnum

| Name | Value |
|---- | -----|
| NEW | &quot;New&quot; |
| ACKNOWLEDGED | &quot;Acknowledged&quot; |
| CLOSED | &quot;Closed&quot; |



