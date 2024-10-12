# AccountApi.DocumentDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderCode** | **String** | The code of account holder, to which the document applies. | [optional] 
**bankAccountUUID** | **String** | The Adyen-generated [&#x60;bankAccountUUID&#x60;](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-bankAccountDetails-bankAccountUUID) to which the document must be linked. Refer to [Bank account check](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-checks/bank-account-check#uploading-a-bank-statement) for details on when a document should be submitted. &gt;Required if the &#x60;documentType&#x60; is **BANK_STATEMENT**, where a document is being submitted in order to verify a bank account.  | [optional] 
**description** | **String** | Description of the document. | [optional] 
**documentType** | **String** | The type of the document. Refer to [Verification checks](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-checks) for details on when each document type should be submitted and for the accepted file formats.  Permitted values: * **BANK_STATEMENT**: A file containing a bank statement or other document proving ownership of a specific bank account. * **COMPANY_REGISTRATION_SCREENING** (Supported from v5 and later): A file containing a company registration document. * **CONSTITUTIONAL_DOCUMENT**: A file containing information about the account holder&#39;s legal arrangement. * **PASSPORT**: A file containing the identity page(s) of a passport. * **ID_CARD_FRONT**: A file containing only the front of the ID card. In order for a document to be usable, both the **ID_CARD_FRONT** and **ID_CARD_BACK** must be submitted. * **ID_CARD_BACK**: A file containing only the back of the ID card. In order for a document to be usable, both the **ID_CARD_FRONT** and **ID_CARD_BACK** must be submitted. * **DRIVING_LICENCE_FRONT**: A file containing only the front of the driving licence. In order for a document to be usable, both the **DRIVING_LICENCE_FRONT** and **DRIVING_LICENCE_BACK** must be submitted. * **DRIVING_LICENCE_BACK**: A file containing only the back of the driving licence. In order for a document to be usable, both the **DRIVING_LICENCE_FRONT** and **DRIVING_LICENCE_FRONT** must be submitted.  | 
**filename** | **String** | Filename of the document. | [optional] 
**shareholderCode** | **String** | The Adyen-generated [&#x60;shareholderCode&#x60;](https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-businessDetails-shareholders-shareholderCode) to which the document must be linked. Refer to [Verification checks](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-checks) for details on when a document should be submitted. &gt;Required if the account holder has a &#x60;legalEntity&#x60; of type **Business** and the &#x60;documentType&#x60; is either **PASSPORT**, **ID_CARD_FRONT**, **ID_CARD_BACK**, **DRIVING_LICENCE_FRONT**, or **DRIVING_LICENCE_BACK**.  | [optional] 
**signatoryCode** | **String** | The Adyen-generated [&#x60;signatoryCode&#x60;](https://docs.adyen.com/api-explorer/#/Account/v6/post/createAccountHolder__resParam_accountHolderDetails-businessDetails-signatories-signatoryCode) to which the document must be linked. | [optional] 



## Enum: DocumentTypeEnum


* `BANK_STATEMENT` (value: `"BANK_STATEMENT"`)

* `BSN` (value: `"BSN"`)

* `DRIVING_LICENCE` (value: `"DRIVING_LICENCE"`)

* `DRIVING_LICENCE_BACK` (value: `"DRIVING_LICENCE_BACK"`)

* `DRIVING_LICENCE_FRONT` (value: `"DRIVING_LICENCE_FRONT"`)

* `ID_CARD` (value: `"ID_CARD"`)

* `ID_CARD_BACK` (value: `"ID_CARD_BACK"`)

* `ID_CARD_FRONT` (value: `"ID_CARD_FRONT"`)

* `PASSPORT` (value: `"PASSPORT"`)

* `PROOF_OF_RESIDENCY` (value: `"PROOF_OF_RESIDENCY"`)

* `SSN` (value: `"SSN"`)




