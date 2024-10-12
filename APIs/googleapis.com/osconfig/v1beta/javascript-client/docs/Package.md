# OsConfigApi.Package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desiredState** | **String** | The desired_state the agent should maintain for this package. The default is to ensure the package is installed. | [optional] 
**manager** | **String** | Type of package manager that can be used to install this package. If a system does not have the package manager, the package is not installed or removed no error message is returned. By default, or if you specify &#x60;ANY&#x60;, the agent attempts to install and remove this package using the default package manager. This is useful when creating a policy that applies to different types of systems. The default behavior is ANY. | [optional] 
**name** | **String** | Required. The name of the package. A package is uniquely identified for conflict validation by checking the package name and the manager(s) that the package targets. | [optional] 



## Enum: DesiredStateEnum


* `DESIRED_STATE_UNSPECIFIED` (value: `"DESIRED_STATE_UNSPECIFIED"`)

* `INSTALLED` (value: `"INSTALLED"`)

* `UPDATED` (value: `"UPDATED"`)

* `REMOVED` (value: `"REMOVED"`)





## Enum: ManagerEnum


* `MANAGER_UNSPECIFIED` (value: `"MANAGER_UNSPECIFIED"`)

* `ANY` (value: `"ANY"`)

* `APT` (value: `"APT"`)

* `YUM` (value: `"YUM"`)

* `ZYPPER` (value: `"ZYPPER"`)

* `GOO` (value: `"GOO"`)




