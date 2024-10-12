

# DeductionType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCode** | **String** | See Accounts |  [optional] |
|**currentRecord** | **Boolean** | Is the current record |  [optional] |
|**deductionCategory** | [**DeductionCategoryEnum**](#DeductionCategoryEnum) |  |  [optional] |
|**deductionTypeID** | **UUID** | Xero identifier |  [optional] |
|**isExemptFromW1** | **Boolean** | Boolean to determine if the deduction type is reportable or exempt from W1 |  [optional] |
|**name** | **String** | Name of the earnings rate (max length &#x3D; 100) |  [optional] |
|**reducesSuper** | **Boolean** | Most deductions don’t reduce your superannuation guarantee contribution liability, so typically you will not set any value for this. |  [optional] |
|**reducesTax** | **Boolean** | Indicates that this is a pre-tax deduction that will reduce the amount of tax you withhold from an employee. |  [optional] |
|**updatedDateUTC** | **String** | Last modified timestamp |  [optional] [readonly] |



## Enum: DeductionCategoryEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| UNIONFEES | &quot;UNIONFEES&quot; |
| WORKPLACEGIVING | &quot;WORKPLACEGIVING&quot; |



