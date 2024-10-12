

# Asset

An asset in Google Cloud. An asset can be any resource in the Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy). See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessLevel** | [**GoogleIdentityAccesscontextmanagerV1AccessLevel**](GoogleIdentityAccesscontextmanagerV1AccessLevel.md) |  |  [optional] |
|**accessPolicy** | [**GoogleIdentityAccesscontextmanagerV1AccessPolicy**](GoogleIdentityAccesscontextmanagerV1AccessPolicy.md) |  |  [optional] |
|**assetType** | **String** | The type of the asset. Example: &#x60;compute.googleapis.com/Disk&#x60; See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information. |  [optional] |
|**iamPolicy** | [**Policy**](Policy.md) |  |  [optional] |
|**name** | **String** | The full name of the asset. Example: &#x60;//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1&#x60; See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information. |  [optional] |
|**orgPolicy** | [**List&lt;GoogleCloudOrgpolicyV1Policy&gt;**](GoogleCloudOrgpolicyV1Policy.md) | A representation of an [organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy). There can be more than one organization policy with different constraints set on a given resource. |  [optional] |
|**resource** | [**Resource**](Resource.md) |  |  [optional] |
|**servicePerimeter** | [**GoogleIdentityAccesscontextmanagerV1ServicePerimeter**](GoogleIdentityAccesscontextmanagerV1ServicePerimeter.md) |  |  [optional] |



