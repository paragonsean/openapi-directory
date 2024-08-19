# BusinessRegistries.Individual

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**[IndividualAddress]**](IndividualAddress.md) |  | [optional] 
**dateOfBirth** | **Date** | The individual&#39;s date of birth, for example, &#x60;1979-01-13&#x60; (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format). | 
**electronicAddresses** | [**[ElectronicAddress]**](ElectronicAddress.md) |  | [optional] 
**fromDate** | **Date** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 
**gender** | **String** | The individual&#39;s gender. | [optional] [default to &#39;Male&#39;]
**id** | [**PartyId**](PartyId.md) | The party&#39;s unique identifier. | [optional] [readonly] 
**names** | [**[IndividualName]**](IndividualName.md) |  | [optional] 
**placeOfBirth** | **String** | The individual&#39;s place of birth, for example, &#x60;Tamworth&#x60;. | 
**toDate** | **Date** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 



## Enum: GenderEnum


* `Female` (value: `"Female"`)

* `Male` (value: `"Male"`)

* `Not Applicable` (value: `"Not Applicable"`)

* `Not Known` (value: `"Not Known"`)




