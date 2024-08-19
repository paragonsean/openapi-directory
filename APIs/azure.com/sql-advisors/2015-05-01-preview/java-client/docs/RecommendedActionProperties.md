

# RecommendedActionProperties

Properties for a Database, Server or Elastic Pool Recommended Action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **Map&lt;String, Object&gt;** | Gets additional details specific to this recommended action. |  [optional] [readonly] |
|**errorDetails** | [**RecommendedActionErrorInfo**](RecommendedActionErrorInfo.md) |  |  [optional] |
|**estimatedImpact** | [**List&lt;RecommendedActionImpactRecord&gt;**](RecommendedActionImpactRecord.md) | Gets the estimated impact info for this recommended action e.g., Estimated CPU gain, Estimated Disk Space change |  [optional] [readonly] |
|**executeActionDuration** | **String** | Gets the time taken for applying this recommended action on user resource. e.g., time taken for index creation |  [optional] [readonly] |
|**executeActionInitiatedBy** | [**ExecuteActionInitiatedByEnum**](#ExecuteActionInitiatedByEnum) | Gets if approval for applying this recommended action was given by user/system. |  [optional] [readonly] |
|**executeActionInitiatedTime** | **OffsetDateTime** | Gets the time when this recommended action was approved for execution. |  [optional] [readonly] |
|**executeActionStartTime** | **OffsetDateTime** | Gets the time when system started applying this recommended action on the user resource. e.g., index creation start time |  [optional] [readonly] |
|**implementationDetails** | [**RecommendedActionImplementationInfo**](RecommendedActionImplementationInfo.md) |  |  [optional] |
|**isArchivedAction** | **Boolean** | Gets if this recommended action was suggested some time ago but user chose to ignore this and system added a new recommended action again. |  [optional] [readonly] |
|**isExecutableAction** | **Boolean** | Gets if this recommended action is actionable by user |  [optional] [readonly] |
|**isRevertableAction** | **Boolean** | Gets if changes applied by this recommended action can be reverted by user |  [optional] [readonly] |
|**lastRefresh** | **OffsetDateTime** | Gets time when this recommended action was last refreshed. |  [optional] [readonly] |
|**linkedObjects** | **List&lt;String&gt;** | Gets the linked objects, if any. |  [optional] [readonly] |
|**observedImpact** | [**List&lt;RecommendedActionImpactRecord&gt;**](RecommendedActionImpactRecord.md) | Gets the observed/actual impact info for this recommended action e.g., Actual CPU gain, Actual Disk Space change |  [optional] [readonly] |
|**recommendationReason** | **String** | Gets the reason for recommending this action. e.g., DuplicateIndex |  [optional] [readonly] |
|**revertActionDuration** | **String** | Gets the time taken for reverting changes of this recommended action on user resource. e.g., time taken for dropping the created index. |  [optional] [readonly] |
|**revertActionInitiatedBy** | [**RevertActionInitiatedByEnum**](#RevertActionInitiatedByEnum) | Gets if approval for reverting this recommended action was given by user/system. |  [optional] [readonly] |
|**revertActionInitiatedTime** | **OffsetDateTime** | Gets the time when this recommended action was approved for revert. |  [optional] [readonly] |
|**revertActionStartTime** | **OffsetDateTime** | Gets the time when system started reverting changes of this recommended action on user resource. e.g., time when index drop is executed. |  [optional] [readonly] |
|**score** | **Integer** | Gets the impact of this recommended action. Possible values are 1 - Low impact, 2 - Medium Impact and 3 - High Impact |  [optional] [readonly] |
|**state** | [**RecommendedActionStateInfo**](RecommendedActionStateInfo.md) |  |  |
|**timeSeries** | [**List&lt;RecommendedActionMetricInfo&gt;**](RecommendedActionMetricInfo.md) | Gets the time series info of metrics for this recommended action e.g., CPU consumption time series |  [optional] [readonly] |
|**validSince** | **OffsetDateTime** | Gets the time since when this recommended action is valid. |  [optional] [readonly] |



## Enum: ExecuteActionInitiatedByEnum

| Name | Value |
|---- | -----|
| USER | &quot;User&quot; |
| SYSTEM | &quot;System&quot; |



## Enum: RevertActionInitiatedByEnum

| Name | Value |
|---- | -----|
| USER | &quot;User&quot; |
| SYSTEM | &quot;System&quot; |



