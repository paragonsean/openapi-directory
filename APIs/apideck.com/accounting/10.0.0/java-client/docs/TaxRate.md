

# TaxRate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Tax code assigned to identify this tax rate. |  [optional] |
|**components** | [**List&lt;TaxComponentsInner&gt;**](TaxComponentsInner.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**description** | **String** | Description of tax rate |  [optional] |
|**effectiveTaxRate** | **BigDecimal** | Effective tax rate |  [optional] |
|**id** | **String** | ID assigned to identify this tax rate. |  [optional] |
|**name** | **String** | Name assigned to identify this tax rate. |  [optional] |
|**originalTaxRateId** | **String** | ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities. |  [optional] |
|**reportTaxType** | **String** | Report Tax type to aggregate tax collected or paid for reporting purposes |  [optional] |
|**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Tax rate status |  [optional] |
|**taxPayableAccountId** | **String** | Unique identifier for the account for tax collected. |  [optional] |
|**taxRemittedAccountId** | **String** | Unique identifier for the account for tax remitted. |  [optional] |
|**totalTaxRate** | **BigDecimal** | Not compounded sum of the components of a tax rate |  [optional] |
|**type** | **String** | Tax type used to indicate the source of tax collected or paid |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| ARCHIVED | &quot;archived&quot; |



