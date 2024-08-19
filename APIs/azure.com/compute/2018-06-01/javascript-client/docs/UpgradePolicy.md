# ComputeManagementClient.UpgradePolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoOSUpgradePolicy** | [**AutoOSUpgradePolicy**](AutoOSUpgradePolicy.md) |  | [optional] 
**automaticOSUpgrade** | **Boolean** | Whether OS upgrades should automatically be applied to scale set instances in a rolling fashion when a newer version of the image becomes available. | [optional] 
**mode** | **String** | Specifies the mode of an upgrade to virtual machines in the scale set.&lt;br /&gt;&lt;br /&gt; Possible values are:&lt;br /&gt;&lt;br /&gt; **Manual** - You  control the application of updates to virtual machines in the scale set. You do this by using the manualUpgrade action.&lt;br /&gt;&lt;br /&gt; **Automatic** - All virtual machines in the scale set are  automatically updated at the same time. | [optional] 
**rollingUpgradePolicy** | [**RollingUpgradePolicy**](RollingUpgradePolicy.md) |  | [optional] 



## Enum: ModeEnum


* `Automatic` (value: `"Automatic"`)

* `Manual` (value: `"Manual"`)

* `Rolling` (value: `"Rolling"`)




