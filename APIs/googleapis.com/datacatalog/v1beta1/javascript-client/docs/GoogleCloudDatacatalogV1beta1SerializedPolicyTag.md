# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1beta1SerializedPolicyTag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**childPolicyTags** | [**[GoogleCloudDatacatalogV1beta1SerializedPolicyTag]**](GoogleCloudDatacatalogV1beta1SerializedPolicyTag.md) | Children of the policy tag if any. | [optional] 
**description** | **String** | Description of the serialized policy tag. The length of the description is limited to 2000 bytes when encoded in UTF-8. If not set, defaults to an empty description. | [optional] 
**displayName** | **String** | Required. Display name of the policy tag. Max 200 bytes when encoded in UTF-8. | [optional] 
**policyTag** | **String** | Resource name of the policy tag. This field will be ignored when calling ImportTaxonomies. | [optional] 


