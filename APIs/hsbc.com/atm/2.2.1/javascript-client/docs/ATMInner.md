# AtmLocatorApi.ATMInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aTMServices** | **[String]** | Describes the type of transaction available for a customer on an ATM. | [optional] 
**access24HoursIndicator** | **Boolean** | Indicates that the ATM is available for use by customers 24 hours per day | [optional] 
**accessibility** | **[String]** | Indicates Types of Accessibility | [optional] 
**branch** | **Object** | Information that locates and identifies a specific branch of a financial institution. | [optional] 
**identification** | **String** | ATM terminal device identification for the acquirer and the issuer. | 
**location** | **Object** | Location of the ATM. | 
**minimumPossibleAmount** | **String** | Minimum amount allowed for a transaction in the service. | [optional] 
**note** | **[String]** | Summary description of the ATM. | [optional] 
**otherATMServices** | [**[OtherATMServicesInner]**](OtherATMServicesInner.md) | Enter a new code , name and description for any other ATM Service | [optional] 
**otherAccessibility** | [**[OtherAccessibilityInner]**](OtherAccessibilityInner.md) | Enter a new code , name and description for any other ATM accessibility options | [optional] 
**supportedCurrencies** | **[String]** | All ISO 4217 defined currency  supported by the ATM. | 
**supportedLanguages** | **[String]** | Identification of the language name according to the ISO 639-1 codes. The type is validated by the list of values coded with two alphabetic characters, defined in the standard. | [optional] 



## Enum: [ATMServicesEnum]


* `Balance` (value: `"Balance"`)

* `BillPayments` (value: `"BillPayments"`)

* `CashDeposits` (value: `"CashDeposits"`)

* `CharityDonation` (value: `"CharityDonation"`)

* `ChequeDeposits` (value: `"ChequeDeposits"`)

* `CashWithdrawal` (value: `"CashWithdrawal"`)

* `EnvelopeDeposit` (value: `"EnvelopeDeposit"`)

* `FastCash` (value: `"FastCash"`)

* `MobileBankingRegistration` (value: `"MobileBankingRegistration"`)

* `MobilePaymentRegistration` (value: `"MobilePaymentRegistration"`)

* `MobilePhoneTopUp` (value: `"MobilePhoneTopUp"`)

* `OrderStatement` (value: `"OrderStatement"`)

* `Other` (value: `"Other"`)

* `PINActivation` (value: `"PINActivation"`)

* `PINChange` (value: `"PINChange"`)

* `PINUnblock` (value: `"PINUnblock"`)

* `MiniStatement` (value: `"MiniStatement"`)





## Enum: [AccessibilityEnum]


* `AudioCashMachine` (value: `"AudioCashMachine"`)

* `AutomaticDoors` (value: `"AutomaticDoors"`)

* `ExternalRamp` (value: `"ExternalRamp"`)

* `InductionLoop` (value: `"InductionLoop"`)

* `InternalRamp` (value: `"InternalRamp"`)

* `LevelAccess` (value: `"LevelAccess"`)

* `LowerLevelCounter` (value: `"LowerLevelCounter"`)

* `Other` (value: `"Other"`)

* `WheelchairAccess` (value: `"WheelchairAccess"`)




