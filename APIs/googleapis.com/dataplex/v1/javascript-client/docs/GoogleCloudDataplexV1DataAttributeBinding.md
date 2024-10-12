# CloudDataplexApi.GoogleCloudDataplexV1DataAttributeBinding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **[String]** | Optional. List of attributes to be associated with the resource, provided in the form: projects/{project}/locations/{location}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id} | [optional] 
**createTime** | **String** | Output only. The time when the DataAttributeBinding was created. | [optional] [readonly] 
**description** | **String** | Optional. Description of the DataAttributeBinding. | [optional] 
**displayName** | **String** | Optional. User friendly display name. | [optional] 
**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Etags must be used when calling the DeleteDataAttributeBinding and the UpdateDataAttributeBinding method. | [optional] 
**labels** | **{String: String}** | Optional. User-defined labels for the DataAttributeBinding. | [optional] 
**name** | **String** | Output only. The relative resource name of the Data Attribute Binding, of the form: projects/{project_number}/locations/{location}/dataAttributeBindings/{data_attribute_binding_id} | [optional] [readonly] 
**paths** | [**[GoogleCloudDataplexV1DataAttributeBindingPath]**](GoogleCloudDataplexV1DataAttributeBindingPath.md) | Optional. The list of paths for items within the associated resource (eg. columns and partitions within a table) along with attribute bindings. | [optional] 
**resource** | **String** | Optional. Immutable. The resource name of the resource that is associated to attributes. Presently, only entity resource is supported in the form: projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/entities/{entity_id} Must belong in the same project and region as the attribute binding, and there can only exist one active binding for a resource. | [optional] 
**uid** | **String** | Output only. System generated globally unique ID for the DataAttributeBinding. This ID will be different if the DataAttributeBinding is deleted and re-created with the same name. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the DataAttributeBinding was last updated. | [optional] [readonly] 


