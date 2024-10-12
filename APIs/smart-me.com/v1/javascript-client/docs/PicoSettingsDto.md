# SmartMe.PicoSettingsDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationType** | **String** | The authentication type | [optional] 
**carIdDetection** | **Boolean** | Flag if the car id detection is enabled | [optional] 
**displayBrightness** | **Blob** | The Brightness of the LCD Matrix display. 0 &#x3D; minimum, 255 &#x3D; maximum | [optional] 
**dnsName** | **String** | The DNS name of the pico&#39;s internal ip | [optional] 
**fixCableLockEnable** | **Boolean** | Enable the fix lock of the charging cable | [optional] 
**idleImageUrl** | **String** | The url of the idle image | [optional] 
**internalIp** | **String** | The internal IP address | [optional] 
**loadmanagementGroupId** | **String** | The ID of the loadmanagement group | [optional] 
**maxCurrent** | **Number** | The max current of this station (in A) | [optional] 
**minCurrent** | **Number** | The max current of this station (in A) | [optional] 
**modbusTcp** | **Boolean** | Flag if ModbusTcp is enabled | [optional] 
**name** | **String** | The name of the station | [optional] 
**serialNumber** | **String** | The Serial number of the station | [optional] 



## Enum: AuthenticationTypeEnum


* `None` (value: `"None"`)

* `Backend` (value: `"Backend"`)




