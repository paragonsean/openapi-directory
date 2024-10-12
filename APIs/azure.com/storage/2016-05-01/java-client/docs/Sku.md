

# Sku

The SKU of the storage account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**NameEnum**](#NameEnum) | Gets or sets the sku name. Required for account creation; optional for update. Note that in older versions, sku name was called accountType. |  |
|**tier** | [**TierEnum**](#TierEnum) | Gets the sku tier. This is based on the SKU name. |  [optional] [readonly] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| STANDARD_LRS | &quot;Standard_LRS&quot; |
| STANDARD_GRS | &quot;Standard_GRS&quot; |
| STANDARD_RAGRS | &quot;Standard_RAGRS&quot; |
| STANDARD_ZRS | &quot;Standard_ZRS&quot; |
| PREMIUM_LRS | &quot;Premium_LRS&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |



