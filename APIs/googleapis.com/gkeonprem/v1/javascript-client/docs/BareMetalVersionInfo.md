# AnthosOnPremApi.BareMetalVersionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencies** | [**[UpgradeDependency]**](UpgradeDependency.md) | The list of upgrade dependencies for this version. | [optional] 
**hasDependencies** | **Boolean** | If set, the cluster dependencies (e.g. the admin cluster, other user clusters managed by the same admin cluster, version skew policy, etc) must be upgraded before this version can be installed or upgraded to. | [optional] 
**version** | **String** | Version number e.g. 1.13.1. | [optional] 


