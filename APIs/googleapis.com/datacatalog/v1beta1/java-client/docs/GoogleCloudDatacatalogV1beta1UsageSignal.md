

# GoogleCloudDatacatalogV1beta1UsageSignal

The set of all usage signals that we store in Data Catalog.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**updateTime** | **String** | The timestamp of the end of the usage statistics duration. |  [optional] |
|**usageWithinTimeRange** | [**Map&lt;String, GoogleCloudDatacatalogV1beta1UsageStats&gt;**](GoogleCloudDatacatalogV1beta1UsageStats.md) | Usage statistics over each of the pre-defined time ranges, supported strings for time ranges are {\&quot;24H\&quot;, \&quot;7D\&quot;, \&quot;30D\&quot;}. |  [optional] |



