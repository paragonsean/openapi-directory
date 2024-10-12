# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1UsageSignal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commonUsageWithinTimeRange** | [**{String: GoogleCloudDatacatalogV1CommonUsageStats}**](GoogleCloudDatacatalogV1CommonUsageStats.md) | Common usage statistics over each of the predefined time ranges. Supported time ranges are &#x60;{\&quot;24H\&quot;, \&quot;7D\&quot;, \&quot;30D\&quot;, \&quot;Lifetime\&quot;}&#x60;. | [optional] 
**favoriteCount** | **String** | Favorite count in the source system. | [optional] 
**updateTime** | **String** | The end timestamp of the duration of usage statistics. | [optional] 
**usageWithinTimeRange** | [**{String: GoogleCloudDatacatalogV1UsageStats}**](GoogleCloudDatacatalogV1UsageStats.md) | Output only. BigQuery usage statistics over each of the predefined time ranges. Supported time ranges are &#x60;{\&quot;24H\&quot;, \&quot;7D\&quot;, \&quot;30D\&quot;}&#x60;. | [optional] [readonly] 


