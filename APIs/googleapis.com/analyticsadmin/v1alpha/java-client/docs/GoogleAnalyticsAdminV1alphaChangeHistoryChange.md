

# GoogleAnalyticsAdminV1alphaChangeHistoryChange

A description of a change to a single Google Analytics resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | The type of action that changed this resource. |  [optional] |
|**resource** | **String** | Resource name of the resource whose changes are described by this entry. |  [optional] |
|**resourceAfterChange** | [**GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource**](GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource.md) |  |  [optional] |
|**resourceBeforeChange** | [**GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource**](GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource.md) |  |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ACTION_TYPE_UNSPECIFIED | &quot;ACTION_TYPE_UNSPECIFIED&quot; |
| CREATED | &quot;CREATED&quot; |
| UPDATED | &quot;UPDATED&quot; |
| DELETED | &quot;DELETED&quot; |



