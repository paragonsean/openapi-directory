

# CreateSlotRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**slotName** | **String** | The name of the slot. Slot names must be unique within the bot that contains the slot. |  |
|**description** | **String** | A description of the slot. Use this to help identify the slot in lists. |  [optional] |
|**slotTypeId** | **String** | The unique identifier for the slot type associated with this slot. The slot type determines the values that can be entered into the slot. |  [optional] |
|**valueElicitationSetting** | [**CreateSlotRequestValueElicitationSetting**](CreateSlotRequestValueElicitationSetting.md) |  |  |
|**obfuscationSetting** | [**CreateSlotRequestObfuscationSetting**](CreateSlotRequestObfuscationSetting.md) |  |  [optional] |
|**multipleValuesSetting** | [**CreateSlotRequestMultipleValuesSetting**](CreateSlotRequestMultipleValuesSetting.md) |  |  [optional] |
|**subSlotSetting** | [**CreateSlotRequestSubSlotSetting**](CreateSlotRequestSubSlotSetting.md) |  |  [optional] |



