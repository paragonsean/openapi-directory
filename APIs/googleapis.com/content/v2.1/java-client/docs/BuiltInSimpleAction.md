

# BuiltInSimpleAction

Action that is implemented and performed in (your) third-party application. Represents various functionality that is expected to be available to merchant and will help them with resolving the issue. The application should point the merchant to the place, where they can access the corresponding functionality. If the functionality is not supported, it is recommended to explain the situation to merchant and provide them with instructions how to solve the issue.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalContent** | [**BuiltInSimpleActionAdditionalContent**](BuiltInSimpleActionAdditionalContent.md) |  |  [optional] |
|**attributeCode** | **String** | The attribute that needs to be updated. Present when the type is &#x60;EDIT_ITEM_ATTRIBUTE&#x60;. This field contains a code for attribute, represented in snake_case. You can find a list of product&#39;s attributes, with their codes [here](https://support.google.com/merchants/answer/7052112). |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of action that represents a functionality that is expected to be available in third-party application. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BUILT_IN_SIMPLE_ACTION_TYPE_UNSPECIFIED | &quot;BUILT_IN_SIMPLE_ACTION_TYPE_UNSPECIFIED&quot; |
| VERIFY_PHONE | &quot;VERIFY_PHONE&quot; |
| CLAIM_WEBSITE | &quot;CLAIM_WEBSITE&quot; |
| ADD_PRODUCTS | &quot;ADD_PRODUCTS&quot; |
| ADD_CONTACT_INFO | &quot;ADD_CONTACT_INFO&quot; |
| LINK_ADS_ACCOUNT | &quot;LINK_ADS_ACCOUNT&quot; |
| ADD_BUSINESS_REGISTRATION_NUMBER | &quot;ADD_BUSINESS_REGISTRATION_NUMBER&quot; |
| EDIT_ITEM_ATTRIBUTE | &quot;EDIT_ITEM_ATTRIBUTE&quot; |
| FIX_ACCOUNT_ISSUE | &quot;FIX_ACCOUNT_ISSUE&quot; |
| SHOW_ADDITIONAL_CONTENT | &quot;SHOW_ADDITIONAL_CONTENT&quot; |



