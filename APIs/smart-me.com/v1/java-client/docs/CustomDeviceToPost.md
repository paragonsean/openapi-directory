

# CustomDeviceToPost

Container Class for the Web API

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The ID of the device |  [optional] |
|**name** | **String** | The Name of the Device |  [optional] |
|**serial** | **Long** | The Serial number |  [optional] |
|**valueDate** | **OffsetDateTime** | The Date of the Value (in UTC). If this is null the Server Time is used. |  [optional] |
|**values** | [**List&lt;CustomDeviceValues&gt;**](CustomDeviceValues.md) | The Values of the custom Device |  [optional] |



