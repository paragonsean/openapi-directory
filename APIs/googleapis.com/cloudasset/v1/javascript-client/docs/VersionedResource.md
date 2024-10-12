# CloudAssetApi.VersionedResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **{String: Object}** | JSON representation of the resource as defined by the corresponding service providing this resource. Example: If the resource is an instance provided by Compute Engine, this field will contain the JSON representation of the instance as defined by Compute Engine: &#x60;https://cloud.google.com/compute/docs/reference/rest/v1/instances&#x60;. You can find the resource definition for each supported resource type in this table: &#x60;https://cloud.google.com/asset-inventory/docs/supported-asset-types&#x60; | [optional] 
**version** | **String** | API version of the resource. Example: If the resource is an instance provided by Compute Engine v1 API as defined in &#x60;https://cloud.google.com/compute/docs/reference/rest/v1/instances&#x60;, version will be \&quot;v1\&quot;. | [optional] 


