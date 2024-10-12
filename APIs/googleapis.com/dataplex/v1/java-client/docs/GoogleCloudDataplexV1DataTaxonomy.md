

# GoogleCloudDataplexV1DataTaxonomy

DataTaxonomy represents a set of hierarchical DataAttributes resources, grouped with a common theme Eg: 'SensitiveDataTaxonomy' can have attributes to manage PII data. It is defined at project level.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeCount** | **Integer** | Output only. The number of attributes in the DataTaxonomy. |  [optional] [readonly] |
|**classCount** | **Integer** | Output only. The number of classes in the DataTaxonomy. |  [optional] [readonly] |
|**createTime** | **String** | Output only. The time when the DataTaxonomy was created. |  [optional] [readonly] |
|**description** | **String** | Optional. Description of the DataTaxonomy. |  [optional] |
|**displayName** | **String** | Optional. User friendly display name. |  [optional] |
|**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. User-defined labels for the DataTaxonomy. |  [optional] |
|**name** | **String** | Output only. The relative resource name of the DataTaxonomy, of the form: projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id}. |  [optional] [readonly] |
|**uid** | **String** | Output only. System generated globally unique ID for the dataTaxonomy. This ID will be different if the DataTaxonomy is deleted and re-created with the same name. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the DataTaxonomy was last updated. |  [optional] [readonly] |



