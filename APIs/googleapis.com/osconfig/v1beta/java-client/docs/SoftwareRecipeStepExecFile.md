

# SoftwareRecipeStepExecFile

Executes an artifact or local file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedExitCodes** | **List&lt;Integer&gt;** | Defaults to [0]. A list of possible return values that the program can return to indicate a success. |  [optional] |
|**args** | **List&lt;String&gt;** | Arguments to be passed to the provided executable. |  [optional] |
|**artifactId** | **String** | The id of the relevant artifact in the recipe. |  [optional] |
|**localPath** | **String** | The absolute path of the file on the local filesystem. |  [optional] |



