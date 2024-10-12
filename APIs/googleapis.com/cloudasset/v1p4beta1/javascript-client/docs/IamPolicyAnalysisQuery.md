# CloudAssetApi.IamPolicyAnalysisQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessSelector** | [**AccessSelector**](AccessSelector.md) |  | [optional] 
**identitySelector** | [**IdentitySelector**](IdentitySelector.md) |  | [optional] 
**parent** | **String** | Required. The relative name of the root asset. Only resources and IAM policies within the parent will be analyzed. This can only be an organization number (such as \&quot;organizations/123\&quot;), a folder number (such as \&quot;folders/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;). To know how to get organization id, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). To know how to get folder or project id, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). | [optional] 
**resourceSelector** | [**ResourceSelector**](ResourceSelector.md) |  | [optional] 


