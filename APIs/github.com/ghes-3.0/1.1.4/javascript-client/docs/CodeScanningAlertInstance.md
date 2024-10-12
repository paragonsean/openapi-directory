# GitHubV3RestApi.CodeScanningAlertInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysisKey** | **String** | Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name. | [optional] 
**category** | **String** | Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code. | [optional] 
**classifications** | [**[CodeScanningAlertClassification]**](CodeScanningAlertClassification.md) | Classifications that have been applied to the file that triggered the alert. For example identifying it as documentation, or a generated file. | [optional] 
**commitSha** | **String** |  | [optional] 
**environment** | **String** | Identifies the variable values associated with the environment in which the analysis that generated this alert instance was performed, such as the language that was analyzed. | [optional] 
**htmlUrl** | **String** |  | [optional] 
**location** | [**CodeScanningAlertLocation**](CodeScanningAlertLocation.md) |  | [optional] 
**message** | [**CodeScanningAlertInstanceMessage**](CodeScanningAlertInstanceMessage.md) |  | [optional] 
**ref** | **String** | The full Git reference, formatted as &#x60;refs/heads/&lt;branch name&gt;&#x60;, &#x60;refs/pull/&lt;number&gt;/merge&#x60;, or &#x60;refs/pull/&lt;number&gt;/head&#x60;. | [optional] 
**state** | [**CodeScanningAlertState**](CodeScanningAlertState.md) |  | [optional] 


