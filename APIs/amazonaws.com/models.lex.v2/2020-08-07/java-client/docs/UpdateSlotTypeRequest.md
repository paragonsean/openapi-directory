

# UpdateSlotTypeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**slotTypeName** | **String** | The new name of the slot type. |  |
|**description** | **String** | The new description of the slot type. |  [optional] |
|**slotTypeValues** | [**List&lt;SlotTypeValue&gt;**](SlotTypeValue.md) | A new list of values and their optional synonyms that define the values that the slot type can take. |  [optional] |
|**valueSelectionSetting** | [**CreateSlotTypeRequestValueSelectionSetting**](CreateSlotTypeRequestValueSelectionSetting.md) |  |  [optional] |
|**parentSlotTypeSignature** | **String** | The new built-in slot type that should be used as the parent of this slot type. |  [optional] |
|**externalSourceSetting** | [**CreateSlotTypeRequestExternalSourceSetting**](CreateSlotTypeRequestExternalSourceSetting.md) |  |  [optional] |
|**compositeSlotTypeSetting** | [**CreateSlotTypeRequestCompositeSlotTypeSetting**](CreateSlotTypeRequestCompositeSlotTypeSetting.md) |  |  [optional] |



