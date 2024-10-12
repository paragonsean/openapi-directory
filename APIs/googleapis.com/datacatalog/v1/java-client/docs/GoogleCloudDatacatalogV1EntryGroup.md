

# GoogleCloudDatacatalogV1EntryGroup

Entry group metadata. An `EntryGroup` resource represents a logical grouping of zero or more Data Catalog Entry resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataCatalogTimestamps** | [**GoogleCloudDatacatalogV1SystemTimestamps**](GoogleCloudDatacatalogV1SystemTimestamps.md) |  |  [optional] |
|**description** | **String** | Entry group description. Can consist of several sentences or paragraphs that describe the entry group contents. Default value is an empty string. |  [optional] |
|**displayName** | **String** | A short name to identify the entry group, for example, \&quot;analytics data - jan 2011\&quot;. Default value is an empty string. |  [optional] |
|**name** | **String** | The resource name of the entry group in URL format. Note: The entry group itself and its child resources might not be stored in the location specified in its name. |  [optional] |



