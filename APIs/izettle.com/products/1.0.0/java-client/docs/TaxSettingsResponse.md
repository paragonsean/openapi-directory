

# TaxSettingsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**organizationUuid** | **UUID** |  |  [optional] |
|**taxationMode** | [**TaxationModeEnum**](#TaxationModeEnum) |  |  [optional] |
|**taxationType** | [**TaxationTypeEnum**](#TaxationTypeEnum) |  |  [optional] |



## Enum: TaxationModeEnum

| Name | Value |
|---- | -----|
| EXCLUSIVE | &quot;EXCLUSIVE&quot; |
| INCLUSIVE | &quot;INCLUSIVE&quot; |



## Enum: TaxationTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| SALES_TAX | &quot;SALES_TAX&quot; |
| VAT | &quot;VAT&quot; |



