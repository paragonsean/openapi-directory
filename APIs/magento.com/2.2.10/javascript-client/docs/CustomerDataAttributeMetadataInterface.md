# MagentoB2B.CustomerDataAttributeMetadataInterface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributeCode** | **String** | Code of the attribute. | 
**backendType** | **String** | Backend type. | 
**dataModel** | **String** | Data model for attribute. | 
**frontendClass** | **String** | Class which is used to display the attribute on frontend. | 
**frontendInput** | **String** | HTML for input element. | 
**frontendLabel** | **String** | Label which supposed to be displayed on frontend. | 
**inputFilter** | **String** | Template used for input (e.g. \&quot;date\&quot;) | 
**isFilterableInGrid** | **Boolean** | It is filterable in customer grid | [optional] 
**isSearchableInGrid** | **Boolean** | It is searchable in customer grid | [optional] 
**isUsedInGrid** | **Boolean** | It is used in customer grid | [optional] 
**isVisibleInGrid** | **Boolean** | It is visible in customer grid | [optional] 
**multilineCount** | **Number** | Of lines of the attribute value. | 
**note** | **String** | The note attribute for the element. | 
**options** | [**[CustomerDataOptionInterface]**](CustomerDataOptionInterface.md) | Options of the attribute (key &#x3D;&gt; value pairs for select) | 
**required** | **Boolean** | Attribute is required. | 
**sortOrder** | **Number** | Attributes sort order. | 
**storeLabel** | **String** | Label of the store. | 
**system** | **Boolean** | This is a system attribute. | 
**userDefined** | **Boolean** | Current attribute has been defined by a user. | 
**validationRules** | [**[CustomerDataValidationRuleInterface]**](CustomerDataValidationRuleInterface.md) | Validation rules. | 
**visible** | **Boolean** | Attribute is visible on frontend. | 


