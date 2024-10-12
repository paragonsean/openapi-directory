# CloudAssetApi.StandardResourceMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalAttributes** | **[String]** | Additional searchable attributes of this resource. Informational only. The exact set of attributes is subject to change. For example: project id, DNS name etc. | [optional] 
**assetType** | **String** | The type of this resource. For example: \&quot;compute.googleapis.com/Disk\&quot;. | [optional] 
**description** | **String** | One or more paragraphs of text description of this resource. Maximum length could be up to 1M bytes. | [optional] 
**displayName** | **String** | The display name of this resource. | [optional] 
**labels** | **{String: String}** | Labels associated with this resource. See [Labelling and grouping Google Cloud resources](https://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources) for more information. | [optional] 
**location** | **String** | Location can be \&quot;global\&quot;, regional like \&quot;us-east1\&quot;, or zonal like \&quot;us-west1-b\&quot;. | [optional] 
**name** | **String** | The full resource name. For example: &#x60;//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1&#x60;. See [Resource Names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information. | [optional] 
**networkTags** | **[String]** | Network tags associated with this resource. Like labels, network tags are a type of annotations used to group Google Cloud resources. See [Labelling Google Cloud resources](lhttps://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources) for more information. | [optional] 
**project** | **String** | The project that this resource belongs to, in the form of &#x60;projects/{project_number}&#x60;. | [optional] 


