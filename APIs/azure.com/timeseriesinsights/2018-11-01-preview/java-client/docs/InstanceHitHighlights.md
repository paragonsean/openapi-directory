

# InstanceHitHighlights

Highlighted text of time series instance to be displayed to the user. Highlighting inserts <hit> and </hit> tags in the portions of text that matched the search string. Do not use any of the highlighted properties to do further API calls.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Highlighted description of time series instance. May be null. |  [optional] [readonly] |
|**hierarchyIds** | **List&lt;UUID&gt;** | List of highlighted time series hierarchy IDs that time series instance belongs to. Cannot be used to lookup hierarchies. May be null. |  [optional] [readonly] |
|**hierarchyNames** | **List&lt;String&gt;** | List of highlighted time series hierarchy names that time series instance belongs to. Cannot be used to lookup hierarchies. May be null. |  [optional] [readonly] |
|**instanceFieldNames** | **List&lt;String&gt;** | List of highlighted time series instance field names. May be null. |  [optional] [readonly] |
|**instanceFieldValues** | **List&lt;String&gt;** | List of highlighted time series instance field values. May be null. |  [optional] [readonly] |
|**name** | **String** | Highlighted name of time series instance. May be null. |  [optional] [readonly] |
|**timeSeriesId** | **List&lt;String&gt;** | List of highlighted string values of Time Series ID for displaying. Cannot be used to lookup instance. |  [optional] [readonly] |
|**typeName** | **String** | Highlighted time series type name that this instance belongs to. |  [optional] [readonly] |



