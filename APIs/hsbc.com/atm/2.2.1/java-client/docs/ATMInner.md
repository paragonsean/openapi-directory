

# ATMInner

ATM information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atMServices** | [**List&lt;AtMServicesEnum&gt;**](#List&lt;AtMServicesEnum&gt;) | Describes the type of transaction available for a customer on an ATM. |  [optional] |
|**access24HoursIndicator** | **Boolean** | Indicates that the ATM is available for use by customers 24 hours per day |  [optional] |
|**accessibility** | [**List&lt;AccessibilityEnum&gt;**](#List&lt;AccessibilityEnum&gt;) | Indicates Types of Accessibility |  [optional] |
|**branch** | **Object** | Information that locates and identifies a specific branch of a financial institution. |  [optional] |
|**identification** | **String** | ATM terminal device identification for the acquirer and the issuer. |  |
|**location** | **Object** | Location of the ATM. |  |
|**minimumPossibleAmount** | **String** | Minimum amount allowed for a transaction in the service. |  [optional] |
|**note** | **List&lt;String&gt;** | Summary description of the ATM. |  [optional] |
|**otherATMServices** | [**List&lt;OtherATMServicesInner&gt;**](OtherATMServicesInner.md) | Enter a new code , name and description for any other ATM Service |  [optional] |
|**otherAccessibility** | [**List&lt;OtherAccessibilityInner&gt;**](OtherAccessibilityInner.md) | Enter a new code , name and description for any other ATM accessibility options |  [optional] |
|**supportedCurrencies** | **List&lt;String&gt;** | All ISO 4217 defined currency  supported by the ATM. |  |
|**supportedLanguages** | **List&lt;String&gt;** | Identification of the language name according to the ISO 639-1 codes. The type is validated by the list of values coded with two alphabetic characters, defined in the standard. |  [optional] |



## Enum: List&lt;AtMServicesEnum&gt;

| Name | Value |
|---- | -----|
| BALANCE | &quot;Balance&quot; |
| BILL_PAYMENTS | &quot;BillPayments&quot; |
| CASH_DEPOSITS | &quot;CashDeposits&quot; |
| CHARITY_DONATION | &quot;CharityDonation&quot; |
| CHEQUE_DEPOSITS | &quot;ChequeDeposits&quot; |
| CASH_WITHDRAWAL | &quot;CashWithdrawal&quot; |
| ENVELOPE_DEPOSIT | &quot;EnvelopeDeposit&quot; |
| FAST_CASH | &quot;FastCash&quot; |
| MOBILE_BANKING_REGISTRATION | &quot;MobileBankingRegistration&quot; |
| MOBILE_PAYMENT_REGISTRATION | &quot;MobilePaymentRegistration&quot; |
| MOBILE_PHONE_TOP_UP | &quot;MobilePhoneTopUp&quot; |
| ORDER_STATEMENT | &quot;OrderStatement&quot; |
| OTHER | &quot;Other&quot; |
| PIN_ACTIVATION | &quot;PINActivation&quot; |
| PIN_CHANGE | &quot;PINChange&quot; |
| PIN_UNBLOCK | &quot;PINUnblock&quot; |
| MINI_STATEMENT | &quot;MiniStatement&quot; |



## Enum: List&lt;AccessibilityEnum&gt;

| Name | Value |
|---- | -----|
| AUDIO_CASH_MACHINE | &quot;AudioCashMachine&quot; |
| AUTOMATIC_DOORS | &quot;AutomaticDoors&quot; |
| EXTERNAL_RAMP | &quot;ExternalRamp&quot; |
| INDUCTION_LOOP | &quot;InductionLoop&quot; |
| INTERNAL_RAMP | &quot;InternalRamp&quot; |
| LEVEL_ACCESS | &quot;LevelAccess&quot; |
| LOWER_LEVEL_COUNTER | &quot;LowerLevelCounter&quot; |
| OTHER | &quot;Other&quot; |
| WHEELCHAIR_ACCESS | &quot;WheelchairAccess&quot; |



