

# AccountInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountAgeIndicator** | [**AccountAgeIndicatorEnum**](#AccountAgeIndicatorEnum) | Indicator for the length of time since this shopper account was created in the merchant&#39;s environment. Allowed values: * notApplicable * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days |  [optional] |
|**accountChangeDate** | **OffsetDateTime** | Date when the shopper&#39;s account was last changed. |  [optional] |
|**accountChangeIndicator** | [**AccountChangeIndicatorEnum**](#AccountChangeIndicatorEnum) | Indicator for the length of time since the shopper&#39;s account was last updated. Allowed values: * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days |  [optional] |
|**accountCreationDate** | **OffsetDateTime** | Date when the shopper&#39;s account was created. |  [optional] |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | Indicates the type of account. For example, for a multi-account card product. Allowed values: * notApplicable * credit * debit |  [optional] |
|**addCardAttemptsDay** | **Integer** | Number of attempts the shopper tried to add a card to their account in the last day. |  [optional] |
|**deliveryAddressUsageDate** | **OffsetDateTime** | Date the selected delivery address was first used. |  [optional] |
|**deliveryAddressUsageIndicator** | [**DeliveryAddressUsageIndicatorEnum**](#DeliveryAddressUsageIndicatorEnum) | Indicator for the length of time since this delivery address was first used. Allowed values: * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days |  [optional] |
|**homePhone** | **String** | Shopper&#39;s home phone number (including the country code). |  [optional] |
|**mobilePhone** | **String** | Shopper&#39;s mobile phone number (including the country code). |  [optional] |
|**passwordChangeDate** | **OffsetDateTime** | Date when the shopper last changed their password. |  [optional] |
|**passwordChangeIndicator** | [**PasswordChangeIndicatorEnum**](#PasswordChangeIndicatorEnum) | Indicator when the shopper has changed their password. Allowed values: * notApplicable * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days |  [optional] |
|**pastTransactionsDay** | **Integer** | Number of all transactions (successful and abandoned) from this shopper in the past 24 hours. |  [optional] |
|**pastTransactionsYear** | **Integer** | Number of all transactions (successful and abandoned) from this shopper in the past year. |  [optional] |
|**paymentAccountAge** | **OffsetDateTime** | Date this payment method was added to the shopper&#39;s account. |  [optional] |
|**paymentAccountIndicator** | [**PaymentAccountIndicatorEnum**](#PaymentAccountIndicatorEnum) | Indicator for the length of time since this payment method was added to this shopper&#39;s account. Allowed values: * notApplicable * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days |  [optional] |
|**purchasesLast6Months** | **Integer** | Number of successful purchases in the last six months. |  [optional] |
|**suspiciousActivity** | **Boolean** | Whether suspicious activity was recorded on this account. |  [optional] |
|**workPhone** | **String** | Shopper&#39;s work phone number (including the country code). |  [optional] |



## Enum: AccountAgeIndicatorEnum

| Name | Value |
|---- | -----|
| NOT_APPLICABLE | &quot;notApplicable&quot; |
| THIS_TRANSACTION | &quot;thisTransaction&quot; |
| LESS_THAN30_DAYS | &quot;lessThan30Days&quot; |
| FROM30_TO60_DAYS | &quot;from30To60Days&quot; |
| MORE_THAN60_DAYS | &quot;moreThan60Days&quot; |



## Enum: AccountChangeIndicatorEnum

| Name | Value |
|---- | -----|
| THIS_TRANSACTION | &quot;thisTransaction&quot; |
| LESS_THAN30_DAYS | &quot;lessThan30Days&quot; |
| FROM30_TO60_DAYS | &quot;from30To60Days&quot; |
| MORE_THAN60_DAYS | &quot;moreThan60Days&quot; |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| NOT_APPLICABLE | &quot;notApplicable&quot; |
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



## Enum: DeliveryAddressUsageIndicatorEnum

| Name | Value |
|---- | -----|
| THIS_TRANSACTION | &quot;thisTransaction&quot; |
| LESS_THAN30_DAYS | &quot;lessThan30Days&quot; |
| FROM30_TO60_DAYS | &quot;from30To60Days&quot; |
| MORE_THAN60_DAYS | &quot;moreThan60Days&quot; |



## Enum: PasswordChangeIndicatorEnum

| Name | Value |
|---- | -----|
| NOT_APPLICABLE | &quot;notApplicable&quot; |
| THIS_TRANSACTION | &quot;thisTransaction&quot; |
| LESS_THAN30_DAYS | &quot;lessThan30Days&quot; |
| FROM30_TO60_DAYS | &quot;from30To60Days&quot; |
| MORE_THAN60_DAYS | &quot;moreThan60Days&quot; |



## Enum: PaymentAccountIndicatorEnum

| Name | Value |
|---- | -----|
| NOT_APPLICABLE | &quot;notApplicable&quot; |
| THIS_TRANSACTION | &quot;thisTransaction&quot; |
| LESS_THAN30_DAYS | &quot;lessThan30Days&quot; |
| FROM30_TO60_DAYS | &quot;from30To60Days&quot; |
| MORE_THAN60_DAYS | &quot;moreThan60Days&quot; |



