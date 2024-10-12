

# GoogleCloudDatacatalogV1UsageSignal

The set of all usage signals that Data Catalog stores. Note: Usually, these signals are updated daily. In rare cases, an update may fail but will be performed again on the next day.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonUsageWithinTimeRange** | [**Map&lt;String, GoogleCloudDatacatalogV1CommonUsageStats&gt;**](GoogleCloudDatacatalogV1CommonUsageStats.md) | Common usage statistics over each of the predefined time ranges. Supported time ranges are &#x60;{\&quot;24H\&quot;, \&quot;7D\&quot;, \&quot;30D\&quot;, \&quot;Lifetime\&quot;}&#x60;. |  [optional] |
|**favoriteCount** | **String** | Favorite count in the source system. |  [optional] |
|**updateTime** | **String** | The end timestamp of the duration of usage statistics. |  [optional] |
|**usageWithinTimeRange** | [**Map&lt;String, GoogleCloudDatacatalogV1UsageStats&gt;**](GoogleCloudDatacatalogV1UsageStats.md) | Output only. BigQuery usage statistics over each of the predefined time ranges. Supported time ranges are &#x60;{\&quot;24H\&quot;, \&quot;7D\&quot;, \&quot;30D\&quot;}&#x60;. |  [optional] [readonly] |



