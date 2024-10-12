

# StorageAccountPropertiesUpdateParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | Gets or sets the account type. Note that StandardZRS and PremiumLRS accounts cannot be changed to other account types, and other account types cannot be changed to StandardZRS or PremiumLRS. |  [optional] |
|**customDomain** | [**CustomDomain**](CustomDomain.md) |  |  [optional] |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| STANDARD_LRS | &quot;Standard_LRS&quot; |
| STANDARD_ZRS | &quot;Standard_ZRS&quot; |
| STANDARD_GRS | &quot;Standard_GRS&quot; |
| STANDARD_RAGRS | &quot;Standard_RAGRS&quot; |
| PREMIUM_LRS | &quot;Premium_LRS&quot; |



