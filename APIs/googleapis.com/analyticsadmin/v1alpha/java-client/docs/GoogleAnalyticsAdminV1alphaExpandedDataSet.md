

# GoogleAnalyticsAdminV1alphaExpandedDataSet

A resource message representing a GA4 ExpandedDataSet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataCollectionStartTime** | **String** | Output only. Time when expanded data set began (or will begin) collecing data. |  [optional] [readonly] |
|**description** | **String** | Optional. The description of the ExpandedDataSet. Max 50 chars. |  [optional] |
|**dimensionFilterExpression** | [**GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression**](GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression.md) |  |  [optional] |
|**dimensionNames** | **List&lt;String&gt;** | Immutable. The list of dimensions included in the ExpandedDataSet. See the [API Dimensions](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions) for the list of dimension names. |  [optional] |
|**displayName** | **String** | Required. The display name of the ExpandedDataSet. Max 200 chars. |  [optional] |
|**metricNames** | **List&lt;String&gt;** | Immutable. The list of metrics included in the ExpandedDataSet. See the [API Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics) for the list of dimension names. |  [optional] |
|**name** | **String** | Output only. The resource name for this ExpandedDataSet resource. Format: properties/{property_id}/expandedDataSets/{expanded_data_set} |  [optional] [readonly] |



