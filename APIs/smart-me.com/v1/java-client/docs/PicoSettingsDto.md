

# PicoSettingsDto

DTO for the pico charging station settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationType** | [**AuthenticationTypeEnum**](#AuthenticationTypeEnum) | The authentication type |  [optional] |
|**carIdDetection** | **Boolean** | Flag if the car id detection is enabled |  [optional] |
|**displayBrightness** | **byte[]** | The Brightness of the LCD Matrix display. 0 &#x3D; minimum, 255 &#x3D; maximum |  [optional] |
|**dnsName** | **String** | The DNS name of the pico&#39;s internal ip |  [optional] |
|**fixCableLockEnable** | **Boolean** | Enable the fix lock of the charging cable |  [optional] |
|**idleImageUrl** | **String** | The url of the idle image |  [optional] |
|**internalIp** | **String** | The internal IP address |  [optional] |
|**loadmanagementGroupId** | **String** | The ID of the loadmanagement group |  [optional] |
|**maxCurrent** | **Integer** | The max current of this station (in A) |  [optional] |
|**minCurrent** | **Integer** | The max current of this station (in A) |  [optional] |
|**modbusTcp** | **Boolean** | Flag if ModbusTcp is enabled |  [optional] |
|**name** | **String** | The name of the station |  [optional] |
|**serialNumber** | **String** | The Serial number of the station |  [optional] |



## Enum: AuthenticationTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| BACKEND | &quot;Backend&quot; |



