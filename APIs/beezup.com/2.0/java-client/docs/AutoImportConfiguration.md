

# AutoImportConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**duplicateProductConfiguration** | [**DuplicateProductValueConfiguration**](DuplicateProductValueConfiguration.md) |  |  |
|**input** | [**InputConfiguration**](InputConfiguration.md) |  |  |
|**inputConfiguredByUserId** | **String** | The user identifier |  |
|**pauseStatusChangedByUserId** | **String** | The user identifier |  [optional] |
|**pauseStatusChangedUtcDate** | **OffsetDateTime** | Indicate when the pause status has changed in UTC date. |  [optional] |
|**paused** | **Boolean** | Indicate if the auto import is in pause or not. |  |
|**scheduledByUserId** | **String** | The user identifier |  [optional] |
|**schedulingLocalTimeZoneName** | **String** | Indicate the time zone name of the scheduling. If the scheduling type is \&quot;Schedule\&quot; |  [optional] |
|**schedulingType** | **SchedulingType** |  |  |
|**schedulingValue** | **List&lt;String&gt;** | Indicate the scheduling value. If the scheduling type is Interval then the value will be a duration otherwise the values will be the time. |  |



