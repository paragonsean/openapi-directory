# DataformApi.CompilationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codeCompilationConfig** | [**CodeCompilationConfig**](CodeCompilationConfig.md) |  | [optional] 
**compilationErrors** | [**[CompilationError]**](CompilationError.md) | Output only. Errors encountered during project compilation. | [optional] [readonly] 
**dataformCoreVersion** | **String** | Output only. The version of &#x60;@dataform/core&#x60; that was used for compilation. | [optional] [readonly] 
**gitCommitish** | **String** | Immutable. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples: - a commit SHA: &#x60;12ade345&#x60; - a tag: &#x60;tag1&#x60; - a branch name: &#x60;branch1&#x60; | [optional] 
**name** | **String** | Output only. The compilation result&#39;s name. | [optional] [readonly] 
**releaseConfig** | **String** | Immutable. The name of the release config to compile. Must be in the format &#x60;projects/_*_/locations/_*_/repositories/_*_/releaseConfigs/_*&#x60;. | [optional] 
**resolvedGitCommitSha** | **String** | Output only. The fully resolved Git commit SHA of the code that was compiled. Not set for compilation results whose source is a workspace. | [optional] [readonly] 
**workspace** | **String** | Immutable. The name of the workspace to compile. Must be in the format &#x60;projects/_*_/locations/_*_/repositories/_*_/workspaces/_*&#x60;. | [optional] 


