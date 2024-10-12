

# HKLocalAccountIdentification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | The 9- to 15-character bank account number (alphanumeric), without separators or whitespace. Starts with the 3-digit branch code. |  |
|**clearingCode** | **String** | The 3-digit clearing code, without separators or whitespace. |  |
|**formFactor** | **String** | The form factor of the account.  Possible values: **physical**, **virtual**. Default value: **physical**. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **hkLocal** |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HK_LOCAL | &quot;hkLocal&quot; |



