# AccountAndTransactionApiSpecificationUk.OBAccount6

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**[OBCashAccount5]**](OBCashAccount5.md) | Provides the details to identify an account. | [optional] 
**accountId** | **String** | A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner. | 
**accountSubType** | [**OBExternalAccountSubType1Code**](OBExternalAccountSubType1Code.md) |  | 
**accountType** | [**OBExternalAccountType1Code**](OBExternalAccountType1Code.md) |  | 
**currency** | **String** | Identification of the currency in which the account is held.  Usage: Currency should only be used in case one and the same account number covers several currencies and the initiating party needs to identify which currency needs to be used for settlement on the account. | 
**description** | **String** | Specifies the description of the account type. | [optional] 
**nickname** | **String** | The nickname of the account, assigned by the account owner in order to provide an additional means of identification of the account. | [optional] 
**openingDate** | **Date** | Date on which the account and related basic services are effectively operational for the account owner.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00 | [optional] 
**servicer** | [**OBBranchAndFinancialInstitutionIdentification5**](OBBranchAndFinancialInstitutionIdentification5.md) |  | [optional] 


