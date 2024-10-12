

# AzureDevopsServicesIntegration

Configuration details for the Azure DevOps Services integration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether the integration is enabled or disabled |  [optional] |
|**id** | **UUID** | ID of the integration |  [optional] [readonly] |
|**name** | **String** | The display name of the integration. Must be unique among all integrations configured for the given API version. |  |
|**branch** | **String** | The branch to synchronize to. If it does not exist in the repository, it will be created based on the default branch. Branch name must not contain whitespace characters.  |  |
|**ignoredPaths** | **List&lt;String&gt;** | Ignored Paths: These files and folders (if exist) will remain as is and will not be changed in any way. Paths are relative to the &#x60;outputFolder&#x60;. Use forward slashes &#x60;/&#x60; as folder separators, but do not add &#x60;/&#x60; at the beginning of the paths.  |  [optional] |
|**managedPaths** | **List&lt;String&gt;** | Fully Managed Paths: These files and folders will be completely managed by the integration. New files will be added, the existing files will be overwritten, and the files that are no longer used will be deleted.  Paths are relative to the &#x60;outputFolder&#x60;. Use forward slashes &#x60;/&#x60; as folder separators, but do not add &#x60;/&#x60; at the beginning of the paths. &#x60;*&#x60; means all files in the &#x60;outputFolder&#x60;.  |  [optional] |
|**outputFile** | **String** | Required if &#x60;target&#x60; is \&quot;YAML (Resolved)\&quot;, \&quot;YAML (Unresolved)\&quot;, \&quot;JSON (Resolved)\&quot;, or \&quot;JSON (Unresolved)\&quot;. Specifies the file name for the generated definition. |  [optional] |
|**outputFolder** | **String** | The output folder for the generated code or definition, relative to the repository root. If this folder does not exist, it will be created. If the output folder is not specified, SwaggerHub will create files and folders in the repository root. Use forward slashes &#x60;/&#x60; as path separators, but do not add &#x60;/&#x60; at the beginning.  |  |
|**providedPaths** | **List&lt;String&gt;** | Partially Managed Paths: These files and folders will be created only if they do not exist. Existing files will not be modified. Paths are relative to the &#x60;outputFolder&#x60;. Use forward slashes &#x60;/&#x60; as folder separators, but do not add &#x60;/&#x60; at the beginning of the paths. &#x60;*&#x60; means all files in the &#x60;outputFolder&#x60;.  |  [optional] |
|**repository** | **String** | The repository to synchronize with |  |
|**syncMethod** | [**SyncMethodEnum**](#SyncMethodEnum) | \&quot;Basic Sync\&quot; or \&quot;Advanced Sync\&quot;. Basic Sync will manage all files and folders in the branch. Advanced Sync allows you to define which files and folders will be managed by SwaggerHub. Note: If \&quot;Advanced Sync\&quot; is used, you must specify either &#x60;providedPaths&#x60; or &#x60;managedPaths&#x60;.  |  |
|**target** | **String** | The type of code to generate and push to the repository. For the possible values, start creating any source control integration manually and check the \&quot;Generated API Code\&quot; values. Note that the available codegens for OAS2 and OAS3 vary.  |  |
|**configType** | [**ConfigTypeEnum**](#ConfigTypeEnum) | Integration type |  |
|**organization** | **String** | The Azure DevOps organization that contains the target repository |  |
|**personalAccessToken** | **String** | A [personal access token](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view&#x3D;azure-devops&amp;tabs&#x3D;preview-page#create-a-pat) for accessing the target repository. The token must have the _Code &gt; Read &amp; write_ scope. Write-only property. Required to create and update the integration.  |  [optional] |
|**project** | **String** | Team Project which contains the target repository |  |



## Enum: SyncMethodEnum

| Name | Value |
|---- | -----|
| BASIC_SYNC | &quot;Basic Sync&quot; |
| ADVANCED_SYNC | &quot;Advanced Sync&quot; |



## Enum: ConfigTypeEnum

| Name | Value |
|---- | -----|
| AZURE_DEVOPS_SERVICES | &quot;AZURE_DEVOPS_SERVICES&quot; |



