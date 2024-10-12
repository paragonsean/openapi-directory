# GitHubV3RestApi.CodeScanningAnalysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysisKey** | **String** | Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name. | 
**category** | **String** | Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code. | [optional] 
**commitSha** | **String** | The SHA of the commit to which the analysis you are uploading relates. | 
**createdAt** | **Date** | The time that the analysis was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**deletable** | **Boolean** |  | 
**environment** | **String** | Identifies the variable values associated with the environment in which this analysis was performed. | 
**error** | **String** |  | 
**id** | **Number** | Unique identifier for this analysis. | 
**ref** | **String** | The full Git reference, formatted as &#x60;refs/heads/&lt;branch name&gt;&#x60;, &#x60;refs/pull/&lt;number&gt;/merge&#x60;, or &#x60;refs/pull/&lt;number&gt;/head&#x60;. | 
**resultsCount** | **Number** | The total number of results in the analysis. | 
**rulesCount** | **Number** | The total number of rules used in the analysis. | 
**sarifId** | **String** | An identifier for the upload. | 
**tool** | [**CodeScanningAnalysisTool**](CodeScanningAnalysisTool.md) |  | 
**url** | **String** | The REST API URL of the analysis resource. | [readonly] 
**warning** | **String** | Warning generated when processing the analysis | 


