

# UpdateFailureState


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **String** | Details about the last failed update attempt. |  [optional] |
|**failedConfiguration** | **Map&lt;String, Object&gt;** | What the component configuration would have been if the update had succeeded. This field may not be populated by xDS clients due to storage overhead. |  [optional] |
|**lastUpdateAttempt** | **String** | Time of the latest failed update attempt. |  [optional] |
|**versionInfo** | **String** | This is the version of the rejected resource. [#not-implemented-hide:] |  [optional] |



