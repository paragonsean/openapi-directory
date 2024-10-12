

# SubContractor3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address2**](Address2.md) |  |  [optional] |
|**bankAccount** | [**BankAccount2**](BankAccount2.md) |  |  [optional] |
|**businessType** | [**BusinessTypeEnum**](#BusinessTypeEnum) | The sub contractors&#39; business type |  [optional] |
|**companyName** | **String** | The sub contractors&#39; company name |  [optional] |
|**companyRegistrationNumber** | **String** | The sub contractors&#39; company registration number |  [optional] |
|**deactivated** | **Boolean** | The sub contractors&#39; deactivated |  [optional] |
|**effectiveDate** | **LocalDate** | The sub contractors&#39; effective date |  [optional] |
|**firstName** | **String** | The sub contractors&#39; first name |  [optional] |
|**initials** | **String** | The sub contractors&#39; initials |  [optional] |
|**lastName** | **String** | The sub contractors&#39; last name |  [optional] |
|**metaData** | **Object** | The sub contractors&#39; meta data |  [optional] |
|**middleName** | **String** | The sub contractors&#39; middle name |  [optional] |
|**nextRevisionDate** | **LocalDate** | The sub contractors&#39; next revision date |  [optional] |
|**niNumber** | **String** | The sub contractors&#39; ni number |  [optional] |
|**partnershipName** | **String** | The sub contractors&#39; partnership name |  [optional] |
|**partnershipUniqueTaxReference** | **String** | The sub contractors&#39; partnership unique tax reference |  [optional] |
|**payFrequency** | [**PayFrequencyEnum**](#PayFrequencyEnum) | The sub contractors&#39; pay frequency |  [optional] |
|**paymentMethod** | [**PaymentMethodEnum**](#PaymentMethodEnum) | The sub contractors&#39; payment method |  [optional] |
|**region** | [**RegionEnum**](#RegionEnum) | The sub contractors&#39; region |  [optional] |
|**revision** | **Integer** | The sub contractors&#39; revision |  [optional] |
|**taxationStatus** | [**TaxationStatusEnum**](#TaxationStatusEnum) | The sub contractors&#39; taxation status |  [optional] |
|**telephone** | **String** | The sub contractors&#39; telephone |  [optional] |
|**territory** | [**TerritoryEnum**](#TerritoryEnum) | The sub contractors&#39; territory |  [optional] |
|**title** | **String** | The sub contractors&#39; title |  [optional] |
|**tradingName** | **String** | The sub contractors&#39; trading name |  [optional] |
|**uniqueTaxReference** | **String** | The sub contractors&#39; unique tax reference |  [optional] |
|**vatRegistered** | **Boolean** | The sub contractors&#39; vat registered |  [optional] |
|**vatRegistrationNumber** | **String** | The sub contractors&#39; vat registration number |  [optional] |
|**verificationDate** | **OffsetDateTime** | The sub contractors&#39; verification date |  [optional] |
|**verificationNumber** | **String** | The sub contractors&#39; verification number |  [optional] |
|**worksNumber** | **String** | The sub contractors&#39; works number |  [optional] |



## Enum: BusinessTypeEnum

| Name | Value |
|---- | -----|
| SOLE_TRADER | &quot;SoleTrader&quot; |
| COMPANY | &quot;Company&quot; |
| PARTNERSHIP | &quot;Partnership&quot; |
| TRUST | &quot;Trust&quot; |



## Enum: PayFrequencyEnum

| Name | Value |
|---- | -----|
| MONTHLY | &quot;Monthly&quot; |
| WEEKLY | &quot;Weekly&quot; |



## Enum: PaymentMethodEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| CASH | &quot;Cash&quot; |
| CHEQUE | &quot;Cheque&quot; |
| BACS | &quot;BACS&quot; |
| FASTER_PAYMENTS | &quot;FasterPayments&quot; |
| OTHER | &quot;Other&quot; |



## Enum: RegionEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| ENGLAND | &quot;England&quot; |
| SCOTLAND | &quot;Scotland&quot; |
| WALES | &quot;Wales&quot; |



## Enum: TaxationStatusEnum

| Name | Value |
|---- | -----|
| UNMATCHED | &quot;Unmatched&quot; |
| NET | &quot;Net&quot; |
| GROSS | &quot;Gross&quot; |



## Enum: TerritoryEnum

| Name | Value |
|---- | -----|
| UNITED_KINGDOM | &quot;UnitedKingdom&quot; |



