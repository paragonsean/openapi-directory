

# UpgradePolicy

Describes an upgrade policy - automatic, manual, or rolling.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automaticOSUpgradePolicy** | [**AutomaticOSUpgradePolicy**](AutomaticOSUpgradePolicy.md) |  |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Specifies the mode of an upgrade to virtual machines in the scale set.&lt;br /&gt;&lt;br /&gt; Possible values are:&lt;br /&gt;&lt;br /&gt; **Manual** - You  control the application of updates to virtual machines in the scale set. You do this by using the manualUpgrade action.&lt;br /&gt;&lt;br /&gt; **Automatic** - All virtual machines in the scale set are  automatically updated at the same time. |  [optional] |
|**rollingUpgradePolicy** | [**RollingUpgradePolicy**](RollingUpgradePolicy.md) |  |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| AUTOMATIC | &quot;Automatic&quot; |
| MANUAL | &quot;Manual&quot; |
| ROLLING | &quot;Rolling&quot; |



