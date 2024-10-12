# SqlManagementClient.RecommendedActionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **{String: Object}** | Gets additional details specific to this recommended action. | [optional] [readonly] 
**errorDetails** | [**RecommendedActionErrorInfo**](RecommendedActionErrorInfo.md) |  | [optional] 
**estimatedImpact** | [**[RecommendedActionImpactRecord]**](RecommendedActionImpactRecord.md) | Gets the estimated impact info for this recommended action e.g., Estimated CPU gain, Estimated Disk Space change | [optional] [readonly] 
**executeActionDuration** | **String** | Gets the time taken for applying this recommended action on user resource. e.g., time taken for index creation | [optional] [readonly] 
**executeActionInitiatedBy** | **String** | Gets if approval for applying this recommended action was given by user/system. | [optional] [readonly] 
**executeActionInitiatedTime** | **Date** | Gets the time when this recommended action was approved for execution. | [optional] [readonly] 
**executeActionStartTime** | **Date** | Gets the time when system started applying this recommended action on the user resource. e.g., index creation start time | [optional] [readonly] 
**implementationDetails** | [**RecommendedActionImplementationInfo**](RecommendedActionImplementationInfo.md) |  | [optional] 
**isArchivedAction** | **Boolean** | Gets if this recommended action was suggested some time ago but user chose to ignore this and system added a new recommended action again. | [optional] [readonly] 
**isExecutableAction** | **Boolean** | Gets if this recommended action is actionable by user | [optional] [readonly] 
**isRevertableAction** | **Boolean** | Gets if changes applied by this recommended action can be reverted by user | [optional] [readonly] 
**lastRefresh** | **Date** | Gets time when this recommended action was last refreshed. | [optional] [readonly] 
**linkedObjects** | **[String]** | Gets the linked objects, if any. | [optional] [readonly] 
**observedImpact** | [**[RecommendedActionImpactRecord]**](RecommendedActionImpactRecord.md) | Gets the observed/actual impact info for this recommended action e.g., Actual CPU gain, Actual Disk Space change | [optional] [readonly] 
**recommendationReason** | **String** | Gets the reason for recommending this action. e.g., DuplicateIndex | [optional] [readonly] 
**revertActionDuration** | **String** | Gets the time taken for reverting changes of this recommended action on user resource. e.g., time taken for dropping the created index. | [optional] [readonly] 
**revertActionInitiatedBy** | **String** | Gets if approval for reverting this recommended action was given by user/system. | [optional] [readonly] 
**revertActionInitiatedTime** | **Date** | Gets the time when this recommended action was approved for revert. | [optional] [readonly] 
**revertActionStartTime** | **Date** | Gets the time when system started reverting changes of this recommended action on user resource. e.g., time when index drop is executed. | [optional] [readonly] 
**score** | **Number** | Gets the impact of this recommended action. Possible values are 1 - Low impact, 2 - Medium Impact and 3 - High Impact | [optional] [readonly] 
**state** | [**RecommendedActionStateInfo**](RecommendedActionStateInfo.md) |  | 
**timeSeries** | [**[RecommendedActionMetricInfo]**](RecommendedActionMetricInfo.md) | Gets the time series info of metrics for this recommended action e.g., CPU consumption time series | [optional] [readonly] 
**validSince** | **Date** | Gets the time since when this recommended action is valid. | [optional] [readonly] 



## Enum: ExecuteActionInitiatedByEnum


* `User` (value: `"User"`)

* `System` (value: `"System"`)





## Enum: RevertActionInitiatedByEnum


* `User` (value: `"User"`)

* `System` (value: `"System"`)




