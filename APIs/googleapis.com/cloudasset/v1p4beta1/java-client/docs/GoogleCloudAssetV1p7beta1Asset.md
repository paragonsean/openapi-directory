

# GoogleCloudAssetV1p7beta1Asset

An asset in Google Cloud. An asset can be any resource in the Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. Cloud IAM policy). See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessLevel** | [**GoogleIdentityAccesscontextmanagerV1AccessLevel**](GoogleIdentityAccesscontextmanagerV1AccessLevel.md) |  |  [optional] |
|**accessPolicy** | [**GoogleIdentityAccesscontextmanagerV1AccessPolicy**](GoogleIdentityAccesscontextmanagerV1AccessPolicy.md) |  |  [optional] |
|**ancestors** | **List&lt;String&gt;** | The ancestry path of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. If the asset is a project, folder, or organization, the ancestry path starts from the asset itself. Example: &#x60;[\&quot;projects/123456789\&quot;, \&quot;folders/5432\&quot;, \&quot;organizations/1234\&quot;]&#x60; |  [optional] |
|**assetType** | **String** | The type of the asset. Example: &#x60;compute.googleapis.com/Disk&#x60; See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information. |  [optional] |
|**iamPolicy** | [**Policy**](Policy.md) |  |  [optional] |
|**name** | **String** | The full name of the asset. Example: &#x60;//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1&#x60; See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information. |  [optional] |
|**orgPolicy** | [**List&lt;GoogleCloudOrgpolicyV1Policy&gt;**](GoogleCloudOrgpolicyV1Policy.md) | A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource. |  [optional] |
|**relatedAssets** | [**GoogleCloudAssetV1p7beta1RelatedAssets**](GoogleCloudAssetV1p7beta1RelatedAssets.md) |  |  [optional] |
|**resource** | [**GoogleCloudAssetV1p7beta1Resource**](GoogleCloudAssetV1p7beta1Resource.md) |  |  [optional] |
|**servicePerimeter** | [**GoogleIdentityAccesscontextmanagerV1ServicePerimeter**](GoogleIdentityAccesscontextmanagerV1ServicePerimeter.md) |  |  [optional] |
|**updateTime** | **String** | The last update timestamp of an asset. update_time is updated when create/update/delete operation is performed. |  [optional] |



