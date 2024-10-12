

# ModelPackage

Package is a reference to the software package to be installed or removed. The agent on the VM instance uses the system package manager to apply the config. These are the commands that the agent uses to install or remove packages. Apt install: `apt-get update && apt-get -y install package1 package2 package3` remove: `apt-get -y remove package1 package2 package3` Yum install: `yum -y install package1 package2 package3` remove: `yum -y remove package1 package2 package3` Zypper install: `zypper install package1 package2 package3` remove: `zypper rm package1 package2` Googet install: `googet -noconfirm install package1 package2 package3` remove: `googet -noconfirm remove package1 package2 package3`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**desiredState** | [**DesiredStateEnum**](#DesiredStateEnum) | The desired_state the agent should maintain for this package. The default is to ensure the package is installed. |  [optional] |
|**manager** | [**ManagerEnum**](#ManagerEnum) | Type of package manager that can be used to install this package. If a system does not have the package manager, the package is not installed or removed no error message is returned. By default, or if you specify &#x60;ANY&#x60;, the agent attempts to install and remove this package using the default package manager. This is useful when creating a policy that applies to different types of systems. The default behavior is ANY. |  [optional] |
|**name** | **String** | Required. The name of the package. A package is uniquely identified for conflict validation by checking the package name and the manager(s) that the package targets. |  [optional] |



## Enum: DesiredStateEnum

| Name | Value |
|---- | -----|
| DESIRED_STATE_UNSPECIFIED | &quot;DESIRED_STATE_UNSPECIFIED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| UPDATED | &quot;UPDATED&quot; |
| REMOVED | &quot;REMOVED&quot; |



## Enum: ManagerEnum

| Name | Value |
|---- | -----|
| MANAGER_UNSPECIFIED | &quot;MANAGER_UNSPECIFIED&quot; |
| ANY | &quot;ANY&quot; |
| APT | &quot;APT&quot; |
| YUM | &quot;YUM&quot; |
| ZYPPER | &quot;ZYPPER&quot; |
| GOO | &quot;GOO&quot; |



