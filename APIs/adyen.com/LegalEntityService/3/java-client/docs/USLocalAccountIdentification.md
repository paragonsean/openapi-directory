

# USLocalAccountIdentification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | The bank account number, without separators or whitespace. |  |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | The bank account type.  Possible values: **checking** or **savings**. Defaults to **checking**. |  [optional] |
|**formFactor** | **String** | The form factor of the account.  Possible values: **physical**, **virtual**. Default value: **physical**. |  [optional] |
|**routingNumber** | **String** | The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace. |  |
|**type** | [**TypeEnum**](#TypeEnum) | **usLocal** |  |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| CHECKING | &quot;checking&quot; |
| SAVINGS | &quot;savings&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| US_LOCAL | &quot;usLocal&quot; |



