# PolicySimulatorApi.GoogleCloudPolicysimulatorV1betaResourceContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ancestors** | **[String]** | The ancestry path of the resource in Google Cloud [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), represented as a list of relative resource names. An ancestry path starts with the closest ancestor in the hierarchy and ends at root. If the resource is a project, folder, or organization, the ancestry path starts from the resource itself. Example: &#x60;[\&quot;projects/123456789\&quot;, \&quot;folders/5432\&quot;, \&quot;organizations/1234\&quot;]&#x60; | [optional] 
**assetType** | **String** | The asset type of the resource as defined by CAIS. Example: &#x60;compute.googleapis.com/Firewall&#x60; See [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for more information. | [optional] 
**resource** | **String** | The full name of the resource. Example: &#x60;//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1&#x60; See [Resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information. | [optional] 


