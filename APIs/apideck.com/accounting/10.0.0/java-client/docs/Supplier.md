

# Supplier


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  |  [optional] |
|**addresses** | [**List&lt;Address&gt;**](Address.md) |  |  [optional] |
|**bankAccounts** | [**List&lt;BankAccount&gt;**](BankAccount.md) |  |  [optional] |
|**channel** | **String** | The channel through which the transaction is processed. |  [optional] |
|**companyName** | **String** | The name of the company. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**displayId** | **String** | Display ID |  [optional] |
|**displayName** | **String** | Display name |  [optional] |
|**downstreamId** | **String** | The third-party API ID of original entity |  [optional] [readonly] |
|**emails** | [**List&lt;Email&gt;**](Email.md) |  |  [optional] |
|**firstName** | **String** | The first name of the person. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [readonly] |
|**individual** | **Boolean** | Is this an individual or business supplier |  [optional] |
|**lastName** | **String** | The last name of the person. |  [optional] |
|**middleName** | **String** | Middle name of the person. |  [optional] |
|**notes** | **String** | Some notes about this supplier |  [optional] |
|**paymentMethod** | **String** | Payment method used for the transaction, such as cash, credit card, bank transfer, or check |  [optional] |
|**phoneNumbers** | [**List&lt;PhoneNumber&gt;**](PhoneNumber.md) |  |  [optional] |
|**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Supplier status |  [optional] |
|**suffix** | **String** |  |  [optional] |
|**taxNumber** | **String** |  |  [optional] |
|**taxRate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  |  [optional] |
|**title** | **String** | The job title of the person. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |
|**websites** | [**List&lt;Website&gt;**](Website.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| ARCHIVED | &quot;archived&quot; |
| GDPR_ERASURE_REQUEST | &quot;gdpr-erasure-request&quot; |
| UNKNOWN | &quot;unknown&quot; |



