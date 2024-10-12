

# GoogleCloudDatacatalogV1beta1EntryGroup

EntryGroup Metadata. An EntryGroup resource represents a logical grouping of zero or more Data Catalog Entry resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataCatalogTimestamps** | [**GoogleCloudDatacatalogV1beta1SystemTimestamps**](GoogleCloudDatacatalogV1beta1SystemTimestamps.md) |  |  [optional] |
|**description** | **String** | Entry group description, which can consist of several sentences or paragraphs that describe entry group contents. Default value is an empty string. |  [optional] |
|**displayName** | **String** | A short name to identify the entry group, for example, \&quot;analytics data - jan 2011\&quot;. Default value is an empty string. |  [optional] |
|**name** | **String** | The resource name of the entry group in URL format. Example: * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id} Note that this EntryGroup and its child resources may not actually be stored in the location in this name. |  [optional] |



