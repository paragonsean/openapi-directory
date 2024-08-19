

# AutomaticOSUpgradePolicy

The configuration parameters used for performing automatic OS upgrade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableAutomaticRollback** | **Boolean** | Whether OS image rollback feature should be disabled. Default value is false. |  [optional] |
|**enableAutomaticOSUpgrade** | **Boolean** | Indicates whether OS upgrades should automatically be applied to scale set instances in a rolling fashion when a newer version of the OS image becomes available. Default value is false. &lt;br&gt;&lt;br&gt; If this is set to true for Windows based scale sets, [enableAutomaticUpdates](https://docs.microsoft.com/dotnet/api/microsoft.azure.management.compute.models.windowsconfiguration.enableautomaticupdates?view&#x3D;azure-dotnet) is automatically set to false and cannot be set to true. |  [optional] |



