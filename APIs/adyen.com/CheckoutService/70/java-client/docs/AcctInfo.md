

# AcctInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chAccAgeInd** | [**ChAccAgeIndEnum**](#ChAccAgeIndEnum) | Length of time that the cardholder has had the account with the 3DS Requestor.  Allowed values: * **01** — No account * **02** — Created during this transaction * **03** — Less than 30 days * **04** — 30–60 days * **05** — More than 60 days |  [optional] |
|**chAccChange** | **String** | Date that the cardholder’s account with the 3DS Requestor was last changed, including Billing or Shipping address, new payment account, or new user(s) added.  Format: **YYYYMMDD** |  [optional] |
|**chAccChangeInd** | [**ChAccChangeIndEnum**](#ChAccChangeIndEnum) | Length of time since the cardholder’s account information with the 3DS Requestor was last changed, including Billing or Shipping address, new payment account, or new user(s) added.  Allowed values: * **01** — Changed during this transaction * **02** — Less than 30 days * **03** — 30–60 days * **04** — More than 60 days |  [optional] |
|**chAccPwChange** | **String** | Date that cardholder’s account with the 3DS Requestor had a password change or account reset.  Format: **YYYYMMDD** |  [optional] |
|**chAccPwChangeInd** | [**ChAccPwChangeIndEnum**](#ChAccPwChangeIndEnum) | Indicates the length of time since the cardholder’s account with the 3DS Requestor had a password change or account reset.  Allowed values: * **01** — No change * **02** — Changed during this transaction * **03** — Less than 30 days * **04** — 30–60 days * **05** — More than 60 days |  [optional] |
|**chAccString** | **String** | Date that the cardholder opened the account with the 3DS Requestor.  Format: **YYYYMMDD** |  [optional] |
|**nbPurchaseAccount** | **String** | Number of purchases with this cardholder account during the previous six months. Max length: 4 characters. |  [optional] |
|**paymentAccAge** | **String** | String that the payment account was enrolled in the cardholder’s account with the 3DS Requestor.  Format: **YYYYMMDD** |  [optional] |
|**paymentAccInd** | [**PaymentAccIndEnum**](#PaymentAccIndEnum) | Indicates the length of time that the payment account was enrolled in the cardholder’s account with the 3DS Requestor.  Allowed values: * **01** — No account (guest checkout) * **02** — During this transaction * **03** — Less than 30 days * **04** — 30–60 days * **05** — More than 60 days |  [optional] |
|**provisionAttemptsDay** | **String** | Number of Add Card attempts in the last 24 hours. Max length: 3 characters. |  [optional] |
|**shipAddressUsage** | **String** | String when the shipping address used for this transaction was first used with the 3DS Requestor.  Format: **YYYYMMDD** |  [optional] |
|**shipAddressUsageInd** | [**ShipAddressUsageIndEnum**](#ShipAddressUsageIndEnum) | Indicates when the shipping address used for this transaction was first used with the 3DS Requestor.  Allowed values: * **01** — This transaction * **02** — Less than 30 days * **03** — 30–60 days * **04** — More than 60 days |  [optional] |
|**shipNameIndicator** | [**ShipNameIndicatorEnum**](#ShipNameIndicatorEnum) | Indicates if the Cardholder Name on the account is identical to the shipping Name used for this transaction.  Allowed values: * **01** — Account Name identical to shipping Name * **02** — Account Name different to shipping Name |  [optional] |
|**suspiciousAccActivity** | [**SuspiciousAccActivityEnum**](#SuspiciousAccActivityEnum) | Indicates whether the 3DS Requestor has experienced suspicious activity (including previous fraud) on the cardholder account.  Allowed values: * **01** — No suspicious activity has been observed * **02** — Suspicious activity has been observed |  [optional] |
|**txnActivityDay** | **String** | Number of transactions (successful and abandoned) for this cardholder account with the 3DS Requestor across all payment accounts in the previous 24 hours. Max length: 3 characters. |  [optional] |
|**txnActivityYear** | **String** | Number of transactions (successful and abandoned) for this cardholder account with the 3DS Requestor across all payment accounts in the previous year. Max length: 3 characters. |  [optional] |



## Enum: ChAccAgeIndEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |
| _03 | &quot;03&quot; |
| _04 | &quot;04&quot; |
| _05 | &quot;05&quot; |



## Enum: ChAccChangeIndEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |
| _03 | &quot;03&quot; |
| _04 | &quot;04&quot; |



## Enum: ChAccPwChangeIndEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |
| _03 | &quot;03&quot; |
| _04 | &quot;04&quot; |
| _05 | &quot;05&quot; |



## Enum: PaymentAccIndEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |
| _03 | &quot;03&quot; |
| _04 | &quot;04&quot; |
| _05 | &quot;05&quot; |



## Enum: ShipAddressUsageIndEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |
| _03 | &quot;03&quot; |
| _04 | &quot;04&quot; |



## Enum: ShipNameIndicatorEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |



## Enum: SuspiciousAccActivityEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |



