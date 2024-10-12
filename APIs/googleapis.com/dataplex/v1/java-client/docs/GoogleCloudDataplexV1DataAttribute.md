

# GoogleCloudDataplexV1DataAttribute

Denotes one dataAttribute in a dataTaxonomy, for example, PII. DataAttribute resources can be defined in a hierarchy. A single dataAttribute resource can contain specs of multiple types PII - ResourceAccessSpec : - readers :foo@bar.com - DataAccessSpec : - readers :bar@foo.com 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeCount** | **Integer** | Output only. The number of child attributes present for this attribute. |  [optional] [readonly] |
|**createTime** | **String** | Output only. The time when the DataAttribute was created. |  [optional] [readonly] |
|**dataAccessSpec** | [**GoogleCloudDataplexV1DataAccessSpec**](GoogleCloudDataplexV1DataAccessSpec.md) |  |  [optional] |
|**description** | **String** | Optional. Description of the DataAttribute. |  [optional] |
|**displayName** | **String** | Optional. User friendly display name. |  [optional] |
|**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. User-defined labels for the DataAttribute. |  [optional] |
|**name** | **String** | Output only. The relative resource name of the dataAttribute, of the form: projects/{project_number}/locations/{location_id}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}. |  [optional] [readonly] |
|**parentId** | **String** | Optional. The ID of the parent DataAttribute resource, should belong to the same data taxonomy. Circular dependency in parent chain is not valid. Maximum depth of the hierarchy allowed is 4. a -&gt; b -&gt; c -&gt; d -&gt; e, depth &#x3D; 4 |  [optional] |
|**resourceAccessSpec** | [**GoogleCloudDataplexV1ResourceAccessSpec**](GoogleCloudDataplexV1ResourceAccessSpec.md) |  |  [optional] |
|**uid** | **String** | Output only. System generated globally unique ID for the DataAttribute. This ID will be different if the DataAttribute is deleted and re-created with the same name. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the DataAttribute was last updated. |  [optional] [readonly] |



