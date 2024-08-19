# ShipEngineApi.ShippingAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressLine1** | **String** | The first line of the street address.  For some addresses, this may be the only line.  Other addresses may require 2 or 3 lines.  | 
**addressLine2** | **String** | The second line of the street address.  For some addresses, this line may not be needed.  | [optional] 
**addressLine3** | **String** | The third line of the street address.  For some addresses, this line may not be needed.  | [optional] 
**addressResidentialIndicator** | [**AddressResidentialIndicator**](AddressResidentialIndicator.md) | Indicates whether this is a residential address. | 
**cityLocality** | **String** | The name of the city or locality | 
**companyName** | **String** | If this is a business address, then the company name should be specified here.  | [optional] 
**countryCode** | **String** | The two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)  | 
**email** | **String** | Email for the address owner.  | [optional] 
**name** | **String** | The name of a contact person at this address.  This field may be set instead of - or in addition to - the &#x60;company_name&#x60; field.  | 
**phone** | **String** | The phone number of a contact person at this address.  The format of this phone number varies depending on the country.  | 
**postalCode** | **String** | postal code | 
**stateProvince** | **String** | The state or province.  For some countries (including the U.S.) only abbreviations are allowed.  Other countries allow the full name or abbreviation.  | 
**instructions** | **String** | Additional text about how to handle the shipment at this address.  | [optional] 


