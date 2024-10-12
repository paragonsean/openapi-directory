

# UpdateSystemModelsPackageTypeIDtoBundle


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bundleID** | **String** | The bundle to include the package in. |  |
|**packageTypeID** | **String** | The package type id of the package to include |  |
|**packageVersion** | **Integer** | The package version of the package to include |  |
|**priority** | **Integer** | The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority. |  |
|**subscriptionType** | [**SubscriptionTypeEnum**](#SubscriptionTypeEnum) | Optional. The type of subscription supported.  The default subscription type is Required. |  [optional] |



## Enum: SubscriptionTypeEnum

| Name | Value |
|---- | -----|
| REQUIRED | &quot;Required&quot; |
| INCLUDE_BY_DEFAULT | &quot;IncludeByDefault&quot; |
| EXCLUDE_BY_DEFAULT | &quot;ExcludeByDefault&quot; |



