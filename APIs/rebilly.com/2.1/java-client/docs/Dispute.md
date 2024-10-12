

# Dispute


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**embedded** | [**List&lt;DisputeEmbeddedInner&gt;**](DisputeEmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. |  [optional] [readonly] |
|**links** | [**List&lt;DisputeLinksInner&gt;**](DisputeLinksInner.md) | The links related to resource. |  [optional] [readonly] |
|**acquirerReferenceNumber** | **String** | The dispute&#39;s acquirer reference number. |  [optional] |
|**amount** | **Double** | The dispute amount. |  |
|**caseId** | **String** | The case ID for the dispute. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | The dispute&#39;s category. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | Dispute created time. |  [optional] [readonly] |
|**currency** | **String** | ISO 4217 alphabetic currency code. |  |
|**customerId** | **String** | The dispute&#39;s customer ID. |  [optional] [readonly] |
|**deadlineTime** | **OffsetDateTime** | Dispute deadline time. |  [optional] |
|**id** | **String** | The dispute identifier string. |  [optional] [readonly] |
|**postedTime** | **OffsetDateTime** | Dispute posted time. |  |
|**rawResponse** | **String** | Dispute raw response from gateway. |  [optional] [readonly] |
|**reasonCode** | [**ReasonCodeEnum**](#ReasonCodeEnum) | The dispute&#39;s reason code. |  |
|**resolvedTime** | **OffsetDateTime** | Dispute resolved time. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The dispute&#39;s status. |  |
|**transactionId** | **String** | The dispute&#39;s transaction ID. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The dispute&#39;s type. |  |
|**updatedTime** | **OffsetDateTime** | Dispute updated time. |  [optional] [readonly] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| FRAUD | &quot;fraud&quot; |
| UNRECOGNIZED | &quot;unrecognized&quot; |
| PRODUCT_NOT_RECEIVED | &quot;product-not-received&quot; |
| PRODUCT_UNACCEPTABLE | &quot;product-unacceptable&quot; |
| PRODUCT_NOT_REFUNDED | &quot;product-not-refunded&quot; |
| DUPLICATE | &quot;duplicate&quot; |
| SUBSCRIPTION_CANCELED | &quot;subscription-canceled&quot; |
| UNCATEGORIZED | &quot;uncategorized&quot; |



## Enum: ReasonCodeEnum

| Name | Value |
|---- | -----|
| _1000 | &quot;1000&quot; |
| _10_1 | &quot;10.1&quot; |
| _10_2 | &quot;10.2&quot; |
| _10_3 | &quot;10.3&quot; |
| _10_4 | &quot;10.4&quot; |
| _10_5 | &quot;10.5&quot; |
| _11_1 | &quot;11.1&quot; |
| _11_2 | &quot;11.2&quot; |
| _11_3 | &quot;11.3&quot; |
| _12 | &quot;12&quot; |
| _12_1 | &quot;12.1&quot; |
| _12_2 | &quot;12.2&quot; |
| _12_3 | &quot;12.3&quot; |
| _12_4 | &quot;12.4&quot; |
| _12_5 | &quot;12.5&quot; |
| _12_6 | &quot;12.6&quot; |
| _12_7 | &quot;12.7&quot; |
| _13_1 | &quot;13.1&quot; |
| _13_2 | &quot;13.2&quot; |
| _13_3 | &quot;13.3&quot; |
| _13_4 | &quot;13.4&quot; |
| _13_5 | &quot;13.5&quot; |
| _13_6 | &quot;13.6&quot; |
| _13_7 | &quot;13.7&quot; |
| _13_8 | &quot;13.8&quot; |
| _13_9 | &quot;13.9&quot; |
| _2 | &quot;2&quot; |
| _30 | &quot;30&quot; |
| _31 | &quot;31&quot; |
| _35 | &quot;35&quot; |
| _37 | &quot;37&quot; |
| _40 | &quot;40&quot; |
| _41 | &quot;41&quot; |
| _42 | &quot;42&quot; |
| _46 | &quot;46&quot; |
| _47 | &quot;47&quot; |
| _49 | &quot;49&quot; |
| _50 | &quot;50&quot; |
| _53 | &quot;53&quot; |
| _54 | &quot;54&quot; |
| _55 | &quot;55&quot; |
| _57 | &quot;57&quot; |
| _59 | &quot;59&quot; |
| _60 | &quot;60&quot; |
| _62 | &quot;62&quot; |
| _7 | &quot;7&quot; |
| _70 | &quot;70&quot; |
| _71 | &quot;71&quot; |
| _722 | &quot;72&quot; |
| _73 | &quot;73&quot; |
| _74 | &quot;74&quot; |
| _75 | &quot;75&quot; |
| _76 | &quot;76&quot; |
| _77 | &quot;77&quot; |
| _79 | &quot;79&quot; |
| _8 | &quot;8&quot; |
| _80 | &quot;80&quot; |
| _81 | &quot;81&quot; |
| _82 | &quot;82&quot; |
| _83 | &quot;83&quot; |
| _85 | &quot;85&quot; |
| _86 | &quot;86&quot; |
| _93 | &quot;93&quot; |
| _00 | &quot;00&quot; |
| _63 | &quot;63&quot; |
| A01 | &quot;A01&quot; |
| A02 | &quot;A02&quot; |
| A08 | &quot;A08&quot; |
| F10 | &quot;F10&quot; |
| F14 | &quot;F14&quot; |
| F22 | &quot;F22&quot; |
| F24 | &quot;F24&quot; |
| F29 | &quot;F29&quot; |
| C02 | &quot;C02&quot; |
| C04 | &quot;C04&quot; |
| C05 | &quot;C05&quot; |
| C08 | &quot;C08&quot; |
| C14 | &quot;C14&quot; |
| C18 | &quot;C18&quot; |
| C28 | &quot;C28&quot; |
| C31 | &quot;C31&quot; |
| C32 | &quot;C32&quot; |
| M10 | &quot;M10&quot; |
| M49 | &quot;M49&quot; |
| P01 | &quot;P01&quot; |
| P03 | &quot;P03&quot; |
| P04 | &quot;P04&quot; |
| P05 | &quot;P05&quot; |
| P07 | &quot;P07&quot; |
| P08 | &quot;P08&quot; |
| P22 | &quot;P22&quot; |
| P23 | &quot;P23&quot; |
| R03 | &quot;R03&quot; |
| R13 | &quot;R13&quot; |
| M01 | &quot;M01&quot; |
| FR1 | &quot;FR1&quot; |
| FR4 | &quot;FR4&quot; |
| FR6 | &quot;FR6&quot; |
| AL | &quot;AL&quot; |
| AP | &quot;AP&quot; |
| AW | &quot;AW&quot; |
| CA | &quot;CA&quot; |
| CD | &quot;CD&quot; |
| CR | &quot;CR&quot; |
| DA | &quot;DA&quot; |
| DP | &quot;DP&quot; |
| DP1 | &quot;DP1&quot; |
| EX | &quot;EX&quot; |
| IC | &quot;IC&quot; |
| IN | &quot;IN&quot; |
| IS | &quot;IS&quot; |
| LP | &quot;LP&quot; |
| N | &quot;N&quot; |
| NA | &quot;NA&quot; |
| NC | &quot;NC&quot; |
| P | &quot;P&quot; |
| RG | &quot;RG&quot; |
| RM | &quot;RM&quot; |
| RN1 | &quot;RN1&quot; |
| RN2 | &quot;RN2&quot; |
| SV | &quot;SV&quot; |
| TF | &quot;TF&quot; |
| TNM | &quot;TNM&quot; |
| UA01 | &quot;UA01&quot; |
| UA02 | &quot;UA02&quot; |
| UA32 | &quot;UA32&quot; |
| UA99 | &quot;UA99&quot; |
| UA03 | &quot;UA03&quot; |
| UA10 | &quot;UA10&quot; |
| UA11 | &quot;UA11&quot; |
| UA12 | &quot;UA12&quot; |
| UA18 | &quot;UA18&quot; |
| UA20 | &quot;UA20&quot; |
| UA21 | &quot;UA21&quot; |
| UA22 | &quot;UA22&quot; |
| UA23 | &quot;UA23&quot; |
| UA28 | &quot;UA28&quot; |
| UA30 | &quot;UA30&quot; |
| UA31 | &quot;UA31&quot; |
| UA38 | &quot;UA38&quot; |
| DUPLICATE | &quot;duplicate&quot; |
| FRAUDULENT | &quot;fraudulent&quot; |
| SUBSCRIPTION_CANCELED | &quot;subscription_canceled&quot; |
| PRODUCT_UNACCEPTABLE | &quot;product_unacceptable&quot; |
| PRODUCT_NOT_RECEIVED | &quot;product_not_received&quot; |
| UNRECOGNIZED | &quot;unrecognized&quot; |
| CREDIT_NOT_PROCESSED | &quot;credit_not_processed&quot; |
| CUSTOMER_INITIATED | &quot;customer_initiated&quot; |
| INCORRECT_ACCOUNT_DETAILS | &quot;incorrect_account_details&quot; |
| INSUFFICIENT_FUNDS | &quot;insufficient_funds&quot; |
| BANK_CANNOT_PROCESS | &quot;bank_cannot_process&quot; |
| DEBIT_NOT_AUTHORIZED | &quot;debit_not_authorized&quot; |
| GENERAL | &quot;general&quot; |
| PRE_CHARGEBACK_ALERT | &quot;pre-chargeback-alert&quot; |
| _0 | &quot;0&quot; |
| _1 | &quot;1&quot; |
| _22 | &quot;2&quot; |
| _3 | &quot;3&quot; |
| _4 | &quot;4&quot; |
| _5 | &quot;5&quot; |
| _6 | &quot;6&quot; |
| _72 | &quot;7&quot; |
| _9 | &quot;9&quot; |
| _51 | &quot;51&quot; |
| A | &quot;A&quot; |
| B | &quot;B&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RESPONSE_NEEDED | &quot;response-needed&quot; |
| UNDER_REVIEW | &quot;under-review&quot; |
| FORFEITED | &quot;forfeited&quot; |
| WON | &quot;won&quot; |
| LOST | &quot;lost&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INFORMATION_REQUEST | &quot;information-request&quot; |
| FIRST_CHARGEBACK | &quot;first-chargeback&quot; |
| SECOND_CHARGEBACK | &quot;second-chargeback&quot; |
| ARBITRATION | &quot;arbitration&quot; |
| FRAUD | &quot;fraud&quot; |
| ETHOCA_ALERT | &quot;ethoca-alert&quot; |
| VERIFI_ALERT | &quot;verifi-alert&quot; |



