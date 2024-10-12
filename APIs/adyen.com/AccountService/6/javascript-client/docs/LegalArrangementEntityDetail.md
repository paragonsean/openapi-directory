# AccountApi.LegalArrangementEntityDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**ViasAddress**](ViasAddress.md) | The address of the entity. | [optional] 
**businessDetails** | [**BusinessDetails**](BusinessDetails.md) | Required when creating an entity with &#x60;legalEntityType&#x60; **Business**, **NonProfit**, **PublicCompany**, or **Partnership**. | [optional] 
**email** | **String** | The e-mail address of the entity. | [optional] 
**fullPhoneNumber** | **String** | The phone number of the contact provided as a single string.  It will be handled as a landline phone. **Examples:** \&quot;0031 6 11 22 33 44\&quot;, \&quot;+316/1122-3344\&quot;, \&quot;(0031) 611223344\&quot; | [optional] 
**individualDetails** | [**IndividualDetails**](IndividualDetails.md) | Required when creating an entity with &#x60;legalEntityType&#x60; **Individual**. | [optional] 
**legalArrangementEntityCode** | **String** | Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a legal arrangement entity. Use only when updating an account holder. If you include this field when creating an account holder, the request will fail. | [optional] 
**legalArrangementEntityReference** | **String** | Your reference for the legal arrangement entity. | [optional] 
**legalArrangementMembers** | **[String]** | An array containing the roles of the entity in the legal arrangement.  The possible values depend on the legal arrangement &#x60;type&#x60;.  - For &#x60;type&#x60; **Association**: **ControllingPerson** and **Shareholder**.  - For &#x60;type&#x60; **Partnership**: **Partner** and **Shareholder**.  - For &#x60;type&#x60; **Trust**: **Trustee**, **Settlor**, **Protector**, **Beneficiary**,  and **Shareholder**.   | [optional] 
**legalEntityType** | **String** | The legal entity type.  Possible values: **Business**, **Individual**, **NonProfit**, **PublicCompany**, or **Partnership**.  | [optional] 
**phoneNumber** | [**ViasPhoneNumber**](ViasPhoneNumber.md) | The phone number of the entity. | [optional] 
**webAddress** | **String** | The URL of the website of the contact. | [optional] 



## Enum: [LegalArrangementMembersEnum]


* `Beneficiary` (value: `"Beneficiary"`)

* `ControllingPerson` (value: `"ControllingPerson"`)

* `Partner` (value: `"Partner"`)

* `Protector` (value: `"Protector"`)

* `Settlor` (value: `"Settlor"`)

* `Shareholder` (value: `"Shareholder"`)

* `Trustee` (value: `"Trustee"`)





## Enum: LegalEntityTypeEnum


* `Business` (value: `"Business"`)

* `Individual` (value: `"Individual"`)

* `NonProfit` (value: `"NonProfit"`)

* `Partnership` (value: `"Partnership"`)

* `PublicCompany` (value: `"PublicCompany"`)




