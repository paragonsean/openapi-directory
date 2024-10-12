

# CALocalAccountIdentification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | The 5- to 12-digit bank account number, without separators or whitespace. |  |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | The bank account type.  Possible values: **checking** or **savings**. Defaults to **checking**. |  [optional] |
|**institutionNumber** | **String** | The 3-digit institution number, without separators or whitespace. |  |
|**transitNumber** | **String** | The 5-digit transit number, without separators or whitespace. |  |
|**type** | [**TypeEnum**](#TypeEnum) | **caLocal** |  |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| CHECKING | &quot;checking&quot; |
| SAVINGS | &quot;savings&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CA_LOCAL | &quot;caLocal&quot; |



