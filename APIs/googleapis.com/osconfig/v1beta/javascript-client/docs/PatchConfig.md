# OsConfigApi.PatchConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apt** | [**AptSettings**](AptSettings.md) |  | [optional] 
**goo** | **Object** | Googet patching is performed by running &#x60;googet update&#x60;. | [optional] 
**migInstancesAllowed** | **Boolean** | Allows the patch job to run on Managed instance groups (MIGs). | [optional] 
**postStep** | [**ExecStep**](ExecStep.md) |  | [optional] 
**preStep** | [**ExecStep**](ExecStep.md) |  | [optional] 
**rebootConfig** | **String** | Post-patch reboot settings. | [optional] 
**windowsUpdate** | [**WindowsUpdateSettings**](WindowsUpdateSettings.md) |  | [optional] 
**yum** | [**YumSettings**](YumSettings.md) |  | [optional] 
**zypper** | [**ZypperSettings**](ZypperSettings.md) |  | [optional] 



## Enum: RebootConfigEnum


* `REBOOT_CONFIG_UNSPECIFIED` (value: `"REBOOT_CONFIG_UNSPECIFIED"`)

* `DEFAULT` (value: `"DEFAULT"`)

* `ALWAYS` (value: `"ALWAYS"`)

* `NEVER` (value: `"NEVER"`)




