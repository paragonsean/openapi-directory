

# CredasApiModelsBankAccountsAccountVerificationResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address1** | **String** |  |  [optional] |
|**city** | **String** |  |  [optional] |
|**forename** | **String** |  |  [optional] |
|**middleName** | **String** |  |  [optional] |
|**postCode** | **String** |  |  [optional] |
|**surname** | **String** |  |  [optional] |
|**accountNumber** | **String** |  |  [optional] |
|**accountNumberValidation** | [**AccountNumberValidationEnum**](#AccountNumberValidationEnum) | Unknown &#x3D; 0, NoMatch &#x3D; 1, Valid &#x3D; 2, Invalid &#x3D; 3, SevenDigitsMatched &#x3D; 4, SixDigitsMatched &#x3D; 5 |  [optional] |
|**accountNumberValidationText** | **String** |  |  [optional] [readonly] |
|**accountStatus** | [**AccountStatusEnum**](#AccountStatusEnum) | Unknown &#x3D; 0, NoMatch &#x3D; 1, Live &#x3D; 2, ClosedOrSettled &#x3D; 3 |  [optional] |
|**accountStatusText** | **String** |  |  [optional] [readonly] |
|**accountValid** | **Boolean** |  |  [optional] |
|**addressValidation** | [**AddressValidationEnum**](#AddressValidationEnum) | Unknown &#x3D; 0, NoMatch &#x3D; 1, CurrentAddress &#x3D; 2, PreviousAddress &#x3D; 3, ForwardingAddress &#x3D; 4 |  [optional] |
|**addressValidationText** | **String** |  |  [optional] [readonly] |
|**checkDate** | **OffsetDateTime** |  |  [optional] |
|**checkId** | **UUID** |  |  [optional] |
|**checkStatus** | [**CheckStatusEnum**](#CheckStatusEnum) | Unknown &#x3D; 0, Pass &#x3D; 1, Refer &#x3D; 2, Fail &#x3D; 3 |  [optional] |
|**error** | **Boolean** |  |  [optional] |
|**hasBeenOverridden** | **Boolean** |  |  [optional] |
|**nameValidation** | [**NameValidationEnum**](#NameValidationEnum) | Unknown &#x3D; 0, NoMatch &#x3D; 1, Valid &#x3D; 2 |  [optional] |
|**nameValidationText** | **String** |  |  [optional] [readonly] |
|**referenceId** | **String** |  |  [optional] |
|**sortcode** | **String** |  |  [optional] |
|**sortcodeValidation** | [**SortcodeValidationEnum**](#SortcodeValidationEnum) | Unknown &#x3D; 0, NoMatch &#x3D; 1, Valid &#x3D; 2, Invalid &#x3D; 3, FiveDigitsMatched &#x3D; 4 |  [optional] |
|**sortcodeValidationText** | **String** |  |  [optional] [readonly] |



## Enum: AccountNumberValidationEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |



## Enum: AccountStatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |



## Enum: AddressValidationEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



## Enum: CheckStatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |



## Enum: NameValidationEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: SortcodeValidationEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



