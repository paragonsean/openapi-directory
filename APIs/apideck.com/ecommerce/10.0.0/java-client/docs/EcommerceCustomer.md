

# EcommerceCustomer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addresses** | [**List&lt;AddressesInner&gt;**](AddressesInner.md) | An array of addresses for the customer. |  [optional] |
|**companyName** | **String** | Company name of the customer |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**emails** | [**List&lt;Email&gt;**](Email.md) | An array of email addresses for the customer. |  [optional] |
|**firstName** | **String** | First name of the customer |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [readonly] |
|**lastName** | **String** | Last name of the customer |  [optional] |
|**name** | **String** | Full name of the customer |  [optional] |
|**orders** | [**List&lt;LinkedEcommerceOrder&gt;**](LinkedEcommerceOrder.md) |  |  [optional] |
|**phoneNumbers** | [**List&lt;PhoneNumber&gt;**](PhoneNumber.md) | An array of phone numbers for the customer. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the customer |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



