

# ImpactedServiceRegion

Azure region impacted by the service health event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**impactedRegion** | **String** | Impacted region name. |  [optional] |
|**impactedSubscriptions** | **List&lt;String&gt;** | List subscription impacted by the service health event. |  [optional] |
|**lastUpdateTime** | **OffsetDateTime** | It provides the Timestamp for when the last update for the service health event. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of event in the region. |  [optional] |
|**updates** | [**List&lt;Update&gt;**](Update.md) | List of updates for given service health event. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| RESOLVED | &quot;Resolved&quot; |



