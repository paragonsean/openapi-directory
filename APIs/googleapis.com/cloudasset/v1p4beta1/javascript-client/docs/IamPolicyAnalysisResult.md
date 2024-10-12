# CloudAssetApi.IamPolicyAnalysisResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessControlLists** | [**[GoogleCloudAssetV1p4beta1AccessControlList]**](GoogleCloudAssetV1p4beta1AccessControlList.md) | The access control lists derived from the iam_binding that match or potentially match resource and access selectors specified in the request. | [optional] 
**attachedResourceFullName** | **String** | The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the resource to which the iam_binding policy attaches. | [optional] 
**fullyExplored** | **Boolean** | Represents whether all analyses on the iam_binding have successfully finished. | [optional] 
**iamBinding** | [**Binding**](Binding.md) |  | [optional] 
**identityList** | [**GoogleCloudAssetV1p4beta1IdentityList**](GoogleCloudAssetV1p4beta1IdentityList.md) |  | [optional] 


