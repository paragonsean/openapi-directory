# TwilioNumbers.NumbersV2RegulatoryComplianceRegulation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endUserType** | [**RegulationEnumEndUserType**](RegulationEnumEndUserType.md) |  | [optional] 
**friendlyName** | **String** | A human-readable description that is assigned to describe the Regulation resource. Examples can include Germany: Mobile - Business. | [optional] 
**isoCountry** | **String** | The ISO country code of the phone number&#39;s country. | [optional] 
**numberType** | **String** | The type of phone number restricted by the regulatory requirement. For example, Germany mobile phone numbers provisioned by businesses require a business name with commercial register proof from the Handelsregisterauszug and a proof of address from Handelsregisterauszug or a trade license by Gewerbeanmeldung. | [optional] 
**requirements** | **Object** | The SID of an object that holds the regulatory information of the phone number country, phone number type, and end user type. | [optional] 
**sid** | **String** | The unique string that identifies the Regulation resource. | [optional] 
**url** | **String** | The absolute URL of the Regulation resource. | [optional] 


