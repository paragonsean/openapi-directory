# StorageImportExport.LocationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternateLocations** | **[String]** | A list of location IDs that should be used to ship shipping drives to for jobs created against the current location. If the current location is active, it will be part of the list. If it is temporarily closed due to maintenance, this list may contain other locations.  | [optional] 
**city** | **String** | The city name to use when shipping the drives to the Azure data center.  | [optional] 
**countryOrRegion** | **String** | The country or region to use when shipping the drives to the Azure data center.  | [optional] 
**phone** | **String** | The phone number for the Azure data center.  | [optional] 
**postalCode** | **String** | The postal code to use when shipping the drives to the Azure data center.  | [optional] 
**recipientName** | **String** | The recipient name to use when shipping the drives to the Azure data center.  | [optional] 
**stateOrProvince** | **String** | The state or province to use when shipping the drives to the Azure data center.  | [optional] 
**streetAddress1** | **String** | The first line of the street address to use when shipping the drives to the Azure data center.  | [optional] 
**streetAddress2** | **String** | The second line of the street address to use when shipping the drives to the Azure data center.  | [optional] 
**supportedCarriers** | **[String]** | A list of carriers that are supported at this location.  | [optional] 


