# CloudAssetApi.GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetType** | **String** | The asset type of the AnalyzeOrgPolicyGovernedAssetsResponse.GovernedIamPolicy.attached_resource. Example: &#x60;cloudresourcemanager.googleapis.com/Project&#x60; See [Cloud Asset Inventory Supported Asset Types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for all supported asset types. | [optional] 
**attachedResource** | **String** | The full resource name of the resource on which this IAM policy is set. Example: &#x60;//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1&#x60;. See [Cloud Asset Inventory Resource Name Format](https://cloud.google.com/asset-inventory/docs/resource-name-format) for more information. | [optional] 
**folders** | **[String]** | The folder(s) that this IAM policy belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the IAM policy belongs (directly or cascadingly) to one or more folders. | [optional] 
**organization** | **String** | The organization that this IAM policy belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the IAM policy belongs (directly or cascadingly) to an organization. | [optional] 
**policy** | [**Policy**](Policy.md) |  | [optional] 
**project** | **String** | The project that this IAM policy belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the IAM policy belongs to a project. | [optional] 


