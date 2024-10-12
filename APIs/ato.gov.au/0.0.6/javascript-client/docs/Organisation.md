# BusinessRegistries.Organisation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**[OrganisationAddress]**](OrganisationAddress.md) |  | [optional] 
**electronicAddresses** | [**[ElectronicAddress]**](ElectronicAddress.md) |  | [optional] 
**establishmentDate** | **Date** | The organisation&#39;s establishment date, for example, &#x60;1928-03-03&#x60; (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format). | 
**fromDate** | **Date** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 
**id** | [**PartyId**](PartyId.md) | The party&#39;s unique identifier. | [optional] [readonly] 
**legalEntityType** | **String** | The organisation&#39;s legal entity type. | [default to &#39;Company&#39;]
**names** | [**[OrganisationName]**](OrganisationName.md) |  | [optional] 
**registeredIdentifiers** | [**[RegisteredIdentifier]**](RegisteredIdentifier.md) |  | [optional] 
**toDate** | **Date** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 



## Enum: LegalEntityTypeEnum


* `Company` (value: `"Company"`)

* `Partnership` (value: `"Partnership"`)

* `Trust` (value: `"Trust"`)

* `Joint Venture` (value: `"Joint Venture"`)




