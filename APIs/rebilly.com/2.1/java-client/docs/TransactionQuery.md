

# TransactionQuery


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** | The transaction&#39;s amount. |  [optional] [readonly] |
|**currency** | **String** | ISO 4217 alphabetic currency code. |  [optional] [readonly] |
|**result** | [**ResultEnum**](#ResultEnum) | Transaction result. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Transaction status. |  [optional] [readonly] |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| ABANDONED | &quot;abandoned&quot; |
| APPROVED | &quot;approved&quot; |
| CANCELED | &quot;canceled&quot; |
| DECLINED | &quot;declined&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| COMPLETED | &quot;completed&quot; |
| CONN_ERROR | &quot;conn-error&quot; |
| DISPUTED | &quot;disputed&quot; |
| NEVER_SENT | &quot;never-sent&quot; |
| OFFSITE | &quot;offsite&quot; |
| PARTIALLY_REFUNDED | &quot;partially-refunded&quot; |
| PENDING | &quot;pending&quot; |
| REFUNDED | &quot;refunded&quot; |
| SENDING | &quot;sending&quot; |
| SUSPENDED | &quot;suspended&quot; |
| TIMEOUT | &quot;timeout&quot; |
| VOIDED | &quot;voided&quot; |
| WAITING_APPROVAL | &quot;waiting-approval&quot; |
| WAITING_CAPTURE | &quot;waiting-capture&quot; |
| WAITING_GATEWAY | &quot;waiting-gateway&quot; |
| WAITING_REFUND | &quot;waiting-refund&quot; |



