# MagentoB2B.CatalogDataCategoryAttributeInterface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applyTo** | **[String]** | Apply to value for the element | [optional] 
**attributeCode** | **String** | Code of the attribute. | 
**attributeId** | **Number** | Id of the attribute. | [optional] 
**backendModel** | **String** | Backend model | [optional] 
**backendType** | **String** | Backend type. | [optional] 
**customAttributes** | [**[FrameworkAttributeInterface]**](FrameworkAttributeInterface.md) | Custom attributes values. | [optional] 
**defaultFrontendLabel** | **String** | Frontend label for default store | [optional] 
**defaultValue** | **String** | Default value for the element. | [optional] 
**entityTypeId** | **String** | Entity type id | 
**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\Catalog\\Api\\Data\\EavAttributeInterface | [optional] 
**frontendClass** | **String** | Frontend class of attribute | [optional] 
**frontendInput** | **String** | HTML for input element. | 
**frontendLabels** | [**[EavDataAttributeFrontendLabelInterface]**](EavDataAttributeFrontendLabelInterface.md) | Frontend label for each store | 
**isComparable** | **String** | The attribute can be compared on the frontend | [optional] 
**isFilterable** | **Boolean** | It used in layered navigation | [optional] 
**isFilterableInGrid** | **Boolean** | It is filterable in catalog product grid | [optional] 
**isFilterableInSearch** | **Boolean** | It is used in search results layered navigation | [optional] 
**isHtmlAllowedOnFront** | **Boolean** | The HTML tags are allowed on the frontend | [optional] 
**isRequired** | **Boolean** | Attribute is required. | 
**isSearchable** | **String** | The attribute can be used in Quick Search | [optional] 
**isUnique** | **String** | This is a unique attribute | [optional] 
**isUsedForPromoRules** | **String** | The attribute can be used for promo rules | [optional] 
**isUsedInGrid** | **Boolean** | It is used in catalog product grid | [optional] 
**isUserDefined** | **Boolean** | Current attribute has been defined by a user. | [optional] 
**isVisible** | **Boolean** | Attribute is visible on frontend. | [optional] 
**isVisibleInAdvancedSearch** | **String** | The attribute can be used in Advanced Search | [optional] 
**isVisibleInGrid** | **Boolean** | It is visible in catalog product grid | [optional] 
**isVisibleOnFront** | **String** | The attribute is visible on the frontend | [optional] 
**isWysiwygEnabled** | **Boolean** | WYSIWYG flag | [optional] 
**note** | **String** | The note attribute for the element. | [optional] 
**options** | [**[EavDataAttributeOptionInterface]**](EavDataAttributeOptionInterface.md) | Options of the attribute (key &#x3D;&gt; value pairs for select) | [optional] 
**position** | **Number** | Position | [optional] 
**scope** | **String** | Attribute scope | [optional] 
**sourceModel** | **String** | Source model | [optional] 
**usedForSortBy** | **Boolean** | It is used for sorting in product listing | [optional] 
**usedInProductListing** | **String** | The attribute can be used in product listing | [optional] 
**validationRules** | [**[EavDataAttributeValidationRuleInterface]**](EavDataAttributeValidationRuleInterface.md) | Validation rules. | [optional] 


