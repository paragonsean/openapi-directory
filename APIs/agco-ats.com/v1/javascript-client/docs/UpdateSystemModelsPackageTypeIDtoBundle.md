# AgcoApi.UpdateSystemModelsPackageTypeIDtoBundle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundleID** | **String** | The bundle to include the package in. | 
**packageTypeID** | **String** | The package type id of the package to include | 
**packageVersion** | **Number** | The package version of the package to include | 
**priority** | **Number** | The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority. | 
**subscriptionType** | **String** | Optional. The type of subscription supported.  The default subscription type is Required. | [optional] 



## Enum: SubscriptionTypeEnum


* `Required` (value: `"Required"`)

* `IncludeByDefault` (value: `"IncludeByDefault"`)

* `ExcludeByDefault` (value: `"ExcludeByDefault"`)




