# AnthosOnPremApi.VmwareVersionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencies** | [**[UpgradeDependency]**](UpgradeDependency.md) | The list of upgrade dependencies for this version. | [optional] 
**hasDependencies** | **Boolean** | If set, the cluster dependencies (e.g. the admin cluster, other user clusters managed by the same admin cluster) must be upgraded before this version can be installed or upgraded to. | [optional] 
**isInstalled** | **Boolean** | If set, the version is installed in the admin cluster. Otherwise, the version bundle must be downloaded and installed before a user cluster can be created at or upgraded to this version. | [optional] 
**version** | **String** | Version number e.g. 1.13.1-gke.1000. | [optional] 


