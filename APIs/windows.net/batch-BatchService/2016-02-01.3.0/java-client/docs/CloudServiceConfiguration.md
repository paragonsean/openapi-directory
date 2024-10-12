

# CloudServiceConfiguration

The configuration for nodes in a pool based on the Azure Cloud Services platform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentOSVersion** | **String** | The Azure Guest OS Version currently installed on the virtual machines in the pool. This may differ from TargetOSVersion if the pool state is Upgrading. |  [optional] |
|**osFamily** | **String** | The Azure Guest OS family to be installed on the virtual machines in the pool. |  |
|**targetOSVersion** | **String** | The Azure Guest OS version to be installed on the virtual machines in the pool. The default value is * which specifies the latest operating system version for the specified OS family. |  [optional] |



