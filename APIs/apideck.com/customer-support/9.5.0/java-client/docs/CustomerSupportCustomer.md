

# CustomerSupportCustomer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addresses** | [**List&lt;Address&gt;**](Address.md) |  |  [optional] |
|**bankAccounts** | [**BankAccount**](BankAccount.md) |  |  [optional] |
|**companyName** | **String** | The name of the company. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**emails** | [**List&lt;Email&gt;**](Email.md) |  |  [optional] |
|**firstName** | **String** | The first name of the person. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**individual** | **Boolean** |  |  [optional] |
|**lastName** | **String** | The last name of the person. |  [optional] |
|**notes** | **String** |  |  [optional] |
|**phoneNumbers** | [**List&lt;PhoneNumber&gt;**](PhoneNumber.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Customer status |  [optional] |
|**taxNumber** | **String** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |
| GDPR_ERASURE_REQUEST | &quot;gdpr-erasure-request&quot; |
| UNKNOWN | &quot;unknown&quot; |



