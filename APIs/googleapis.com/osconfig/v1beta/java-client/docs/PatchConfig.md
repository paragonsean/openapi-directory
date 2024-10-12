

# PatchConfig

Patch configuration specifications. Contains details on how to apply the patch(es) to a VM instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apt** | [**AptSettings**](AptSettings.md) |  |  [optional] |
|**goo** | **Object** | Googet patching is performed by running &#x60;googet update&#x60;. |  [optional] |
|**migInstancesAllowed** | **Boolean** | Allows the patch job to run on Managed instance groups (MIGs). |  [optional] |
|**postStep** | [**ExecStep**](ExecStep.md) |  |  [optional] |
|**preStep** | [**ExecStep**](ExecStep.md) |  |  [optional] |
|**rebootConfig** | [**RebootConfigEnum**](#RebootConfigEnum) | Post-patch reboot settings. |  [optional] |
|**windowsUpdate** | [**WindowsUpdateSettings**](WindowsUpdateSettings.md) |  |  [optional] |
|**yum** | [**YumSettings**](YumSettings.md) |  |  [optional] |
|**zypper** | [**ZypperSettings**](ZypperSettings.md) |  |  [optional] |



## Enum: RebootConfigEnum

| Name | Value |
|---- | -----|
| REBOOT_CONFIG_UNSPECIFIED | &quot;REBOOT_CONFIG_UNSPECIFIED&quot; |
| DEFAULT | &quot;DEFAULT&quot; |
| ALWAYS | &quot;ALWAYS&quot; |
| NEVER | &quot;NEVER&quot; |



