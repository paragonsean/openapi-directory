# CloudAssetApi.IamPolicySearchResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**explanation** | [**Explanation**](Explanation.md) |  | [optional] 
**policy** | [**Policy**](Policy.md) |  | [optional] 
**project** | **String** | The project that the associated Google Cloud resource belongs to, in the form of &#x60;projects/{project_number}&#x60;. If an IAM policy is set on a resource -- such as a Compute Engine instance or a Cloud Storage bucket -- the project field will indicate the project that contains the resource. If an IAM policy is set on a folder or orgnization, the project field will be empty. | [optional] 
**resource** | **String** | The [full resource name](https://cloud.google.com/apis/design/resource_names#full_resource_name) of the resource associated with this IAM policy. | [optional] 


