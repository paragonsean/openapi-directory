

# ImageTemplateRestartCustomizer

Reboots a VM and waits for it to come back online (Windows). Corresponds to Packer windows-restart provisioner

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**restartCheckCommand** | **String** | Command to check if restart succeeded [Default: &#39;&#39;] |  [optional] |
|**restartCommand** | **String** | Command to execute the restart [Default: &#39;shutdown /r /f /t 0 /c \&quot;packer restart\&quot;&#39;] |  [optional] |
|**restartTimeout** | **String** | Restart timeout specified as a string of magnitude and unit, e.g. &#39;5m&#39; (5 minutes) or &#39;2h&#39; (2 hours) [Default: &#39;5m&#39;] |  [optional] |



