# LegalEntityManagementApi.BankAccountInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | The bank account number (without separators).   When this is provided, the &#x60;branchCode&#x60; is also required. | [optional] 
**accountType** | **String** | The type of bank account. | [optional] 
**bankBicSwift** | **String** | The bank&#39;s BIC or SWIFT code. | [optional] 
**bankCity** | **String** | The city where the bank is located. | [optional] 
**bankCode** | **String** | The bank code of the banking institution with which the bank account is registered. | [optional] 
**bankName** | **String** | The name of the banking institution where the bank account is held. | [optional] 
**branchCode** | **String** | The branch code of the branch under which the bank account is registered.  Required when you provide an &#x60;accountNumber&#x60;.   In the following countries, this value corresponds to:   * United States: routing number * United Kingdom: sort code * Germany: Bankleitzahl | [optional] 
**checkCode** | **String** | The check code of the bank account. | [optional] 
**countryCode** | **String** | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the bank account is registered. For example, **NL**. | [optional] 
**currencyCode** | **String** | The account&#39;s three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). For example, **EUR**. | 
**iban** | **String** | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. | [optional] 
**trustedSource** | **Boolean** | Identifies if the bank account was created through [instant bank verification](https://docs.adyen.com/release-notes/platforms-and-financial-products#releaseNote&#x3D;2023-05-08-hosted-onboarding). | [optional] [readonly] 


