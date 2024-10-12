# CloudAssetApi.Asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessLevel** | [**GoogleIdentityAccesscontextmanagerV1AccessLevel**](GoogleIdentityAccesscontextmanagerV1AccessLevel.md) |  | [optional] 
**accessPolicy** | [**GoogleIdentityAccesscontextmanagerV1AccessPolicy**](GoogleIdentityAccesscontextmanagerV1AccessPolicy.md) |  | [optional] 
**ancestors** | **[String]** | The ancestry path of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. If the asset is a project, folder, or organization, the ancestry path starts from the asset itself. Example: &#x60;[\&quot;projects/123456789\&quot;, \&quot;folders/5432\&quot;, \&quot;organizations/1234\&quot;]&#x60; | [optional] 
**assetType** | **String** | The type of the asset. Example: &#x60;compute.googleapis.com/Disk&#x60; See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information. | [optional] 
**iamPolicy** | [**Policy**](Policy.md) |  | [optional] 
**name** | **String** | The full name of the asset. Example: &#x60;//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1&#x60; See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information. | [optional] 
**orgPolicy** | [**[GoogleCloudOrgpolicyV1Policy]**](GoogleCloudOrgpolicyV1Policy.md) | A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource. | [optional] 
**osInventory** | [**Inventory**](Inventory.md) |  | [optional] 
**relatedAsset** | [**RelatedAsset**](RelatedAsset.md) |  | [optional] 
**relatedAssets** | [**RelatedAssets**](RelatedAssets.md) |  | [optional] 
**resource** | [**Resource**](Resource.md) |  | [optional] 
**servicePerimeter** | [**GoogleIdentityAccesscontextmanagerV1ServicePerimeter**](GoogleIdentityAccesscontextmanagerV1ServicePerimeter.md) |  | [optional] 
**updateTime** | **String** | The last update timestamp of an asset. update_time is updated when create/update/delete operation is performed. | [optional] 


