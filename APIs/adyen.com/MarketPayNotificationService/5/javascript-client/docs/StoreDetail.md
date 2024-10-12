# ClassicPlatformsNotifications.StoreDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**ViasAddress**](ViasAddress.md) | The address of the physical store where the account holder will process payments from. | 
**fullPhoneNumber** | **String** | The phone number of the store provided as a single string.  It will be handled as a landline phone.  Examples: \&quot;0031 6 11 22 33 44\&quot;, \&quot;+316/1122-3344\&quot;, \&quot;(0031) 611223344\&quot; | [optional] 
**logo** | **String** | Store logo for payment method setup. | [optional] 
**merchantAccount** | **String** | The merchant account to which the store belongs. | 
**merchantCategoryCode** | **String** | The merchant category code (MCC) that classifies the business of the account holder. | 
**merchantHouseNumber** | **String** | Merchant house number for payment method setup. | [optional] 
**phoneNumber** | [**ViasPhoneNumber**](ViasPhoneNumber.md) | The phone number of the store. | [optional] 
**shopperInteraction** | **String** | The sales channel. Possible values: **Ecommerce**, **POS**. | [optional] 
**splitConfigurationUUID** | **String** | The unique reference for the split configuration, returned when you configure splits in your Customer Area. When this is provided, the &#x60;virtualAccount&#x60; is also required. Adyen uses the configuration and the &#x60;virtualAccount&#x60; to split funds between accounts in your platform. | [optional] 
**status** | **String** | The status of the store. Possible values: **Pending**, **Active**, **Inactive**, **InactiveWithModifications**, **Closed**. | [optional] 
**store** | **String** | Adyen-generated unique alphanumeric identifier (UUID) for the store, returned in the response when you create a store. Required when updating an existing store in an &#x60;/updateAccountHolder&#x60; request. | [optional] 
**storeName** | **String** | The name of the account holder&#39;s store. This value is shown in shopper statements.  * Length: Between 3 to 22 characters   * The following characters are *not* supported: **:;}{$#@!|&lt;&gt;%^*+&#x3D;\\\\** | [optional] 
**storeReference** | **String** | Your unique identifier for the store. The Customer Area also uses this value for the store description.   * Length: Between 3 to 128 characters  * The following characters are *not* supported: **:;}{$#@!|&lt;&gt;%^*+&#x3D;\\\\** | [optional] 
**virtualAccount** | **String** | The account holder&#39;s &#x60;accountCode&#x60; where the split amount will be sent. Required when you provide the &#x60;splitConfigurationUUID&#x60;. | [optional] 
**webAddress** | **String** | URL of the ecommerce store. | [optional] 



## Enum: ShopperInteractionEnum


* `Ecommerce` (value: `"Ecommerce"`)

* `POS` (value: `"POS"`)





## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Closed` (value: `"Closed"`)

* `Inactive` (value: `"Inactive"`)

* `InactiveWithModifications` (value: `"InactiveWithModifications"`)

* `Pending` (value: `"Pending"`)




