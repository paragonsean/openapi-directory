

# IamPolicyAnalysis

An analysis message to group the query and results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analysisQuery** | [**IamPolicyAnalysisQuery**](IamPolicyAnalysisQuery.md) |  |  [optional] |
|**analysisResults** | [**List&lt;IamPolicyAnalysisResult&gt;**](IamPolicyAnalysisResult.md) | A list of IamPolicyAnalysisResult that matches the analysis query, or empty if no result is found. |  [optional] |
|**fullyExplored** | **Boolean** | Represents whether all entries in the analysis_results have been fully explored to answer the query. |  [optional] |
|**nonCriticalErrors** | [**List&lt;IamPolicyAnalysisState&gt;**](IamPolicyAnalysisState.md) | A list of non-critical errors happened during the query handling. |  [optional] |



