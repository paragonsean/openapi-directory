

# CloudServiceConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentOSVersion** | **String** | This may differ from targetOSVersion if the pool state is Upgrading. In this case some virtual machines may be on the targetOSVersion and some may be on the currentOSVersion during the upgrade process. Once all virtual machines have upgraded, currentOSVersion is updated to be the same as targetOSVersion. |  [optional] |
|**osFamily** | **String** | Possible values are: 2 - OS Family 2, equivalent to Windows Server 2008 R2 SP1. 3 - OS Family 3, equivalent to Windows Server 2012. 4 - OS Family 4, equivalent to Windows Server 2012 R2. 5 - OS Family 5, equivalent to Windows Server 2016. For more information, see Azure Guest OS Releases (https://azure.microsoft.com/documentation/articles/cloud-services-guestos-update-matrix/#releases). |  |
|**targetOSVersion** | **String** | The default value is * which specifies the latest operating system version for the specified OS family. |  [optional] |



