# XeroAccountingApi.Contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | A user defined account number. This can be updated via the API and the Xero UI (max length &#x3D; 50) | [optional] 
**accountsPayableTaxType** | **String** | The tax type from TaxRates | [optional] 
**accountsReceivableTaxType** | **String** | The tax type from TaxRates | [optional] 
**addresses** | [**[Address]**](Address.md) | Store certain address types for a contact – see address types | [optional] 
**attachments** | [**[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 
**balances** | [**Balances**](Balances.md) |  | [optional] 
**bankAccountDetails** | **String** | Bank account number of contact | [optional] 
**batchPayments** | [**BatchPaymentDetails**](BatchPaymentDetails.md) |  | [optional] 
**brandingTheme** | [**BrandingTheme**](BrandingTheme.md) |  | [optional] 
**contactGroups** | [**[ContactGroup]**](ContactGroup.md) | Displays which contact groups a contact is included in | [optional] 
**contactID** | **String** | Xero identifier | [optional] 
**contactNumber** | **String** | This can be updated via the API only i.e. This field is read only on the Xero contact screen, used to identify contacts in external systems (max length &#x3D; 50). If the Contact Number is used, this is displayed as Contact Code in the Contacts UI in Xero. | [optional] 
**contactPersons** | [**[ContactPerson]**](ContactPerson.md) | See contact persons | [optional] 
**contactStatus** | **String** | Current status of a contact – see contact status types | [optional] 
**defaultCurrency** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**discount** | **Number** | The default discount rate for the contact (read only) | [optional] [readonly] 
**emailAddress** | **String** | Email address of contact person (umlauts not supported) (max length  &#x3D; 255) | [optional] 
**firstName** | **String** | First name of contact person (max length &#x3D; 255) | [optional] 
**hasAttachments** | **Boolean** | A boolean to indicate if a contact has an attachment | [optional] [default to false]
**hasValidationErrors** | **Boolean** | A boolean to indicate if a contact has an validation errors | [optional] [default to false]
**isCustomer** | **Boolean** | true or false – Boolean that describes if a contact has any AR invoices entered against them. Cannot be set via PUT or POST – it is automatically set when an accounts receivable invoice is generated against this contact. | [optional] 
**isSupplier** | **Boolean** | true or false – Boolean that describes if a contact that has any AP  invoices entered against them. Cannot be set via PUT or POST – it is automatically set when an accounts payable invoice is generated against this contact. | [optional] 
**lastName** | **String** | Last name of contact person (max length &#x3D; 255) | [optional] 
**name** | **String** | Full name of contact/organisation (max length &#x3D; 255) | [optional] 
**paymentTerms** | [**PaymentTerm**](PaymentTerm.md) |  | [optional] 
**phones** | [**[Phone]**](Phone.md) | Store certain phone types for a contact – see phone types | [optional] 
**purchasesDefaultAccountCode** | **String** | The default purchases account code for contacts | [optional] 
**purchasesTrackingCategories** | [**[SalesTrackingCategory]**](SalesTrackingCategory.md) | The default purchases tracking categories for contacts | [optional] 
**salesDefaultAccountCode** | **String** | The default sales account code for contacts | [optional] 
**salesTrackingCategories** | [**[SalesTrackingCategory]**](SalesTrackingCategory.md) | The default sales tracking categories for contacts | [optional] 
**skypeUserName** | **String** | Skype user name of contact | [optional] 
**statusAttributeString** | **String** | Status of object | [optional] 
**taxNumber** | **String** | Tax number of contact – this is also known as the ABN (Australia), GST Number (New Zealand), VAT Number (UK) or Tax ID Number (US and global) in the Xero UI depending on which regionalized version of Xero you are using (max length &#x3D; 50) | [optional] 
**trackingCategoryName** | **String** | The name of the Tracking Category assigned to the contact under SalesTrackingCategories and PurchasesTrackingCategories | [optional] 
**trackingCategoryOption** | **String** | The name of the Tracking Option assigned to the contact under SalesTrackingCategories and PurchasesTrackingCategories | [optional] 
**updatedDateUTC** | **String** | UTC timestamp of last update to contact | [optional] [readonly] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays validation errors returned from the API | [optional] 
**website** | **String** | Website address for contact (read only) | [optional] [readonly] 
**xeroNetworkKey** | **String** | Store XeroNetworkKey for contacts. | [optional] 



## Enum: ContactStatusEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `ARCHIVED` (value: `"ARCHIVED"`)

* `GDPRREQUEST` (value: `"GDPRREQUEST"`)




