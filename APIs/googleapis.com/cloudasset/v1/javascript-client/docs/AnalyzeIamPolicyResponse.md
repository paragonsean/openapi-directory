# CloudAssetApi.AnalyzeIamPolicyResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fullyExplored** | **Boolean** | Represents whether all entries in the main_analysis and service_account_impersonation_analysis have been fully explored to answer the query in the request. | [optional] 
**mainAnalysis** | [**IamPolicyAnalysis**](IamPolicyAnalysis.md) |  | [optional] 
**serviceAccountImpersonationAnalysis** | [**[IamPolicyAnalysis]**](IamPolicyAnalysis.md) | The service account impersonation analysis if AnalyzeIamPolicyRequest.analyze_service_account_impersonation is enabled. | [optional] 


