# CloudAssetApi.AnalyzeIamPolicyResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fullyExplored** | **Boolean** | Represents whether all entries in the main_analysis and service_account_impersonation_analysis have been fully explored to answer the query in the request. | [optional] 
**mainAnalysis** | [**IamPolicyAnalysis**](IamPolicyAnalysis.md) |  | [optional] 
**nonCriticalErrors** | [**[GoogleCloudAssetV1p4beta1AnalysisState]**](GoogleCloudAssetV1p4beta1AnalysisState.md) | A list of non-critical errors happened during the request handling to explain why &#x60;fully_explored&#x60; is false, or empty if no error happened. | [optional] 
**serviceAccountImpersonationAnalysis** | [**[IamPolicyAnalysis]**](IamPolicyAnalysis.md) | The service account impersonation analysis if AnalyzeIamPolicyRequest.analyze_service_account_impersonation is enabled. | [optional] 


