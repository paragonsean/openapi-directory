

# RelatedAsset

An asset identifier in Google Cloud which contains its name, type and ancestors. An asset can be any resource in the Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy). See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ancestors** | **List&lt;String&gt;** | The ancestors of an asset in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. Example: &#x60;[\&quot;projects/123456789\&quot;, \&quot;folders/5432\&quot;, \&quot;organizations/1234\&quot;]&#x60; |  [optional] |
|**asset** | **String** | The full name of the asset. Example: &#x60;//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1&#x60; See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information. |  [optional] |
|**assetType** | **String** | The type of the asset. Example: &#x60;compute.googleapis.com/Disk&#x60; See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information. |  [optional] |
|**relationshipType** | **String** | The unique identifier of the relationship type. Example: &#x60;INSTANCE_TO_INSTANCEGROUP&#x60; |  [optional] |



