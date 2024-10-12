# CloudIoTApi.SendCommandToDeviceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binaryData** | **Blob** | Required. The command data to send to the device. | [optional] 
**subfolder** | **String** | Optional subfolder for the command. If empty, the command will be delivered to the /devices/{device-id}/commands topic, otherwise it will be delivered to the /devices/{device-id}/commands/{subfolder} topic. Multi-level subfolders are allowed. This field must not have more than 256 characters, and must not contain any MQTT wildcards (\&quot;+\&quot; or \&quot;#\&quot;) or null characters. | [optional] 


