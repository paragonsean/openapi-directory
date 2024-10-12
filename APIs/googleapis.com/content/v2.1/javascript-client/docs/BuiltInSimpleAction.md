# ContentApiForShopping.BuiltInSimpleAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalContent** | [**BuiltInSimpleActionAdditionalContent**](BuiltInSimpleActionAdditionalContent.md) |  | [optional] 
**attributeCode** | **String** | The attribute that needs to be updated. Present when the type is &#x60;EDIT_ITEM_ATTRIBUTE&#x60;. This field contains a code for attribute, represented in snake_case. You can find a list of product&#39;s attributes, with their codes [here](https://support.google.com/merchants/answer/7052112). | [optional] 
**type** | **String** | The type of action that represents a functionality that is expected to be available in third-party application. | [optional] 



## Enum: TypeEnum


* `BUILT_IN_SIMPLE_ACTION_TYPE_UNSPECIFIED` (value: `"BUILT_IN_SIMPLE_ACTION_TYPE_UNSPECIFIED"`)

* `VERIFY_PHONE` (value: `"VERIFY_PHONE"`)

* `CLAIM_WEBSITE` (value: `"CLAIM_WEBSITE"`)

* `ADD_PRODUCTS` (value: `"ADD_PRODUCTS"`)

* `ADD_CONTACT_INFO` (value: `"ADD_CONTACT_INFO"`)

* `LINK_ADS_ACCOUNT` (value: `"LINK_ADS_ACCOUNT"`)

* `ADD_BUSINESS_REGISTRATION_NUMBER` (value: `"ADD_BUSINESS_REGISTRATION_NUMBER"`)

* `EDIT_ITEM_ATTRIBUTE` (value: `"EDIT_ITEM_ATTRIBUTE"`)

* `FIX_ACCOUNT_ISSUE` (value: `"FIX_ACCOUNT_ISSUE"`)

* `SHOW_ADDITIONAL_CONTENT` (value: `"SHOW_ADDITIONAL_CONTENT"`)




