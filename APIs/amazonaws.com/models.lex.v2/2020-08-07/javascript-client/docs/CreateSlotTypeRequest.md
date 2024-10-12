# AmazonLexModelBuildingV2.CreateSlotTypeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slotTypeName** | **String** | The name for the slot. A slot type name must be unique within the intent. | 
**description** | **String** | A description of the slot type. Use the description to help identify the slot type in lists. | [optional] 
**slotTypeValues** | [**[SlotTypeValue]**](SlotTypeValue.md) | A list of &lt;code&gt;SlotTypeValue&lt;/code&gt; objects that defines the values that the slot type can take. Each value can have a list of synonyms, additional values that help train the machine learning model about the values that it resolves for a slot. | [optional] 
**valueSelectionSetting** | [**CreateSlotTypeRequestValueSelectionSetting**](CreateSlotTypeRequestValueSelectionSetting.md) |  | [optional] 
**parentSlotTypeSignature** | **String** | &lt;p&gt;The built-in slot type used as a parent of this slot type. When you define a parent slot type, the new slot type has the configuration of the parent slot type.&lt;/p&gt; &lt;p&gt;Only &lt;code&gt;AMAZON.AlphaNumeric&lt;/code&gt; is supported.&lt;/p&gt; | [optional] 
**externalSourceSetting** | [**CreateSlotTypeRequestExternalSourceSetting**](CreateSlotTypeRequestExternalSourceSetting.md) |  | [optional] 
**compositeSlotTypeSetting** | [**CreateSlotTypeRequestCompositeSlotTypeSetting**](CreateSlotTypeRequestCompositeSlotTypeSetting.md) |  | [optional] 


