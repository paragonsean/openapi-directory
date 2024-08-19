

# DisplayOutput

It contains a complete display operation for a Display or an Input Device type. For the Input Devices, Diagnosis and EnableService, ResponseRequiredFlag and MinimumDisplayTime shall be absent. Information to display and the way to process the display.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**device** | **Device** |  |  |
|**infoQualify** | **InfoQualify** |  |  |
|**menuEntry** | [**List&lt;MenuEntry&gt;**](MenuEntry.md) |  |  [optional] |
|**minimumDisplayTime** | **Integer** | Number of seconds the message has to be displayed. |  [optional] |
|**outputContent** | [**OutputContent**](OutputContent.md) |  |  |
|**outputSignature** | **String** | If protection has to be provided to the vendor on the text to display or print. |  [optional] |
|**responseRequiredFlag** | **Boolean** | Request of a message response. |  [optional] |



