# EcommerceApi.EcommerceCustomer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**[AddressesInner]**](AddressesInner.md) | An array of addresses for the customer. | [optional] 
**companyName** | **String** | Company name of the customer | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**emails** | [**[Email]**](Email.md) | An array of email addresses for the customer. | [optional] 
**firstName** | **String** | First name of the customer | [optional] 
**id** | **String** | A unique identifier for an object. | [readonly] 
**lastName** | **String** | Last name of the customer | [optional] 
**name** | **String** | Full name of the customer | [optional] 
**orders** | [**[LinkedEcommerceOrder]**](LinkedEcommerceOrder.md) |  | [optional] 
**phoneNumbers** | [**[PhoneNumber]**](PhoneNumber.md) | An array of phone numbers for the customer. | [optional] 
**status** | **String** | The current status of the customer | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `archived` (value: `"archived"`)




