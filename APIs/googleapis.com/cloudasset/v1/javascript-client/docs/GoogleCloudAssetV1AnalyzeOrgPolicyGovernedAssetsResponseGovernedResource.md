# CloudAssetApi.GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetType** | **String** | The asset type of the AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource.full_resource_name Example: &#x60;cloudresourcemanager.googleapis.com/Project&#x60; See [Cloud Asset Inventory Supported Asset Types](https://cloud.google.com/asset-inventory/docs/supported-asset-types) for all supported asset types. | [optional] 
**effectiveTags** | [**[EffectiveTagDetails]**](EffectiveTagDetails.md) | The effective tags on this resource. | [optional] 
**folders** | **[String]** | The folder(s) that this resource belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to one or more folders. | [optional] 
**fullResourceName** | **String** | The [full resource name] (https://cloud.google.com/asset-inventory/docs/resource-name-format) of the Google Cloud resource. | [optional] 
**organization** | **String** | The organization that this resource belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to an organization. | [optional] 
**parent** | **String** | The [full resource name] (https://cloud.google.com/asset-inventory/docs/resource-name-format) of the parent of AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource.full_resource_name. | [optional] 
**project** | **String** | The project that this resource belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the resource belongs to a project. | [optional] 


