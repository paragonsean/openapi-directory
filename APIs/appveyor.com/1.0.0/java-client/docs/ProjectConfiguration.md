

# ProjectConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**afterBuildScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**afterDeployScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**afterTestScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**artifacts** | [**List&lt;Artifact&gt;**](Artifact.md) |  |  [optional] |
|**assemblyFileVersionFormat** | **String** |  |  [optional] |
|**assemblyInfoFile** | **String** |  |  [optional] |
|**assemblyInformationalVersionFormat** | **String** |  |  [optional] |
|**assemblyVersionFormat** | **String** |  |  [optional] |
|**beforeBuildScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**beforeDeployScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**beforePackageScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**beforeTestScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**branchesMode** | **ProjectBranchesMode** |  |  [optional] |
|**buildCloud** | [**List&lt;StringValueObject&gt;**](StringValueObject.md) |  |  [optional] |
|**buildMode** | **BuildMode** |  |  [optional] |
|**buildScripts** | [**List&lt;Script&gt;**](Script.md) | Only set/used when &#x60;buildMode&#x60; is &#x60;script&#x60;. |  [optional] |
|**cacheEntries** | [**List&lt;StringValueObject&gt;**](StringValueObject.md) |  |  [optional] |
|**cloneDepth** | **Integer** |  |  [optional] |
|**cloneFolder** | **String** |  |  [optional] |
|**cloneScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**_configuration** | [**List&lt;StringValueObject&gt;**](StringValueObject.md) |  |  [optional] |
|**configureNuGetAccountSource** | **Boolean** |  |  [optional] |
|**configureNuGetProjectSource** | **Boolean** |  |  [optional] |
|**deployMode** | **DeployMode** |  |  [optional] |
|**deployScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**deployments** | [**List&lt;DeploymentProvider&gt;**](DeploymentProvider.md) |  |  [optional] |
|**disableNuGetPublishForOctopusPackages** | **Boolean** |  |  [optional] |
|**disableNuGetPublishOnPullRequests** | **Boolean** |  |  [optional] |
|**doNotIncrementBuildNumberOnPullRequests** | **Boolean** |  |  [optional] |
|**dotnetCsprojAssemblyVersionFormat** | **String** |  |  [optional] |
|**dotnetCsprojFile** | **String** |  |  [optional] |
|**dotnetCsprojFileVersionFormat** | **String** |  |  [optional] |
|**dotnetCsprojInformationalVersionFormat** | **String** |  |  [optional] |
|**dotnetCsprojPackageVersionFormat** | **String** |  |  [optional] |
|**dotnetCsprojVersionFormat** | **String** |  |  [optional] |
|**environmentVariables** | [**List&lt;StoredNameValue&gt;**](StoredNameValue.md) |  |  [optional] |
|**environmentVariablesMatrix** | [**List&lt;StoredNameValueMatrix&gt;**](StoredNameValueMatrix.md) |  |  [optional] |
|**excludeBranches** | [**List&lt;StringValueObject&gt;**](StringValueObject.md) |  |  [optional] |
|**forceHttpsClone** | **Boolean** |  |  [optional] |
|**hostsEntries** | [**List&lt;HostEntry&gt;**](HostEntry.md) |  |  [optional] |
|**hotFixScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**includeBranches** | [**List&lt;StringValueObject&gt;**](StringValueObject.md) |  |  [optional] |
|**includeNuGetReferences** | **Boolean** |  |  [optional] |
|**initScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**installScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**matrixAllowFailures** | [**List&lt;StoredNameValueMatrix&gt;**](StoredNameValueMatrix.md) | Although the names and values are not enforced, the combinations which are meaningful are documented at https://www.appveyor.com/docs/build-configuration/#allow-failing-jobs |  [optional] |
|**matrixExcept** | [**List&lt;StoredNameValueMatrix&gt;**](StoredNameValueMatrix.md) |  |  [optional] |
|**matrixExclude** | [**List&lt;StoredNameValueMatrix&gt;**](StoredNameValueMatrix.md) |  |  [optional] |
|**matrixFastFinish** | **Boolean** |  |  [optional] |
|**matrixOnly** | [**List&lt;StoredNameValueMatrix&gt;**](StoredNameValueMatrix.md) |  |  [optional] |
|**maxJobs** | **Integer** |  |  [optional] |
|**msBuildInParallel** | **Boolean** |  |  [optional] |
|**msBuildProjectFileName** | **String** |  |  [optional] |
|**msBuildVerbosity** | **MSBuildVerbosity** |  |  [optional] |
|**notifications** | [**List&lt;NotificationProviderSettings&gt;**](NotificationProviderSettings.md) |  |  [optional] |
|**onBuildErrorScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**onBuildFinishScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**onBuildSuccessScripts** | [**List&lt;Script&gt;**](Script.md) |  |  [optional] |
|**onlyCommitsFiles** | [**List&lt;StringValueObject&gt;**](StringValueObject.md) |  |  [optional] |
|**operatingSystem** | [**List&lt;BuildWorkerImageInner&gt;**](BuildWorkerImageInner.md) |  |  [optional] |
|**packageAspNetCoreProjects** | **Boolean** |  |  [optional] |
|**packageAzureCloudServiceProjects** | **Boolean** |  |  [optional] |
|**packageDotnetConsoleProjects** | **Boolean** |  |  [optional] |
|**packageNuGetProjects** | **Boolean** |  |  [optional] |
|**packageNuGetSymbols** | **Boolean** |  |  [optional] |
|**packageWebApplicationProjects** | **Boolean** |  |  [optional] |
|**packageWebApplicationProjectsBeanstalk** | **Boolean** |  |  [optional] |
|**packageWebApplicationProjectsOctopus** | **Boolean** |  |  [optional] |
|**packageWebApplicationProjectsXCopy** | **Boolean** |  |  [optional] |
|**patchAssemblyInfo** | **Boolean** |  |  [optional] |
|**patchDotnetCsproj** | **Boolean** |  |  [optional] |
|**platform** | [**List&lt;ProjectConfigurationPlatformInner&gt;**](ProjectConfigurationPlatformInner.md) |  |  [optional] |
|**services** | [**List&lt;OSServicesToStartDuringTheBuildProcessInner&gt;**](OSServicesToStartDuringTheBuildProcessInner.md) |  |  [optional] |
|**shallowClone** | **Boolean** |  |  [optional] |
|**skipBranchWithPullRequests** | **Boolean** |  |  [optional] |
|**skipCommitsFiles** | [**List&lt;StringValueObject&gt;**](StringValueObject.md) |  |  [optional] |
|**skipNonTags** | **Boolean** |  |  [optional] |
|**skipTags** | **Boolean** |  |  [optional] |
|**stacks** | **List&lt;UnknownType&gt;** |  |  [optional] |
|**testAssemblies** | [**List&lt;StringValueObject&gt;**](StringValueObject.md) |  |  [optional] |
|**testCategories** | [**List&lt;StringValueObject&gt;**](StringValueObject.md) |  |  [optional] |
|**testCategoriesMatrix** | [**List&lt;ProjectConfigurationTestCategoriesMatrixInner&gt;**](ProjectConfigurationTestCategoriesMatrixInner.md) |  |  [optional] |
|**testCategoriesMode** | [**TestCategoriesModeEnum**](#TestCategoriesModeEnum) |  |  [optional] |
|**testMode** | **TestMode** |  |  [optional] |
|**testScripts** | [**List&lt;Script&gt;**](Script.md) | Only set/used when &#x60;testMode&#x60; is &#x60;script&#x60;. |  [optional] |
|**xamarinRegisterAndroidProduct** | **Boolean** |  |  [optional] |
|**xamarinRegisterIosProduct** | **Boolean** |  |  [optional] |



## Enum: TestCategoriesModeEnum

| Name | Value |
|---- | -----|
| EXCLUDE | &quot;exclude&quot; |
| INCLUDE | &quot;include&quot; |



