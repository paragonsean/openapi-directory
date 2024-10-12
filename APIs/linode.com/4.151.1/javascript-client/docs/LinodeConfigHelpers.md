# LinodeApi.LinodeConfigHelpers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devtmpfsAutomount** | **Boolean** | Populates the /dev directory early during boot without udev.  Defaults to false.  | [optional] 
**distro** | **Boolean** | Helps maintain correct inittab/upstart console device. | [optional] 
**modulesDep** | **Boolean** | Creates a modules dependency file for the Kernel you run. | [optional] 
**network** | **Boolean** | Automatically configures static networking. | [optional] 
**updatedbDisabled** | **Boolean** | Disables updatedb cron job to avoid disk thrashing. | [optional] 


