

# GoogleCloudDataplexV1DataAttributeBindingPath

Represents a subresource of the given resource, and associated bindings with it. Currently supported subresources are column and partition schema fields within a table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | **List&lt;String&gt;** | Optional. List of attributes to be associated with the path of the resource, provided in the form: projects/{project}/locations/{location}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id} |  [optional] |
|**name** | **String** | Required. The name identifier of the path. Nested columns should be of the form: &#39;address.city&#39;. |  [optional] |



