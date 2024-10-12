# PtvTimetableApiVersion3.V3VehiclePosition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bearing** | **Number** | Compass bearing of the vehicle when known, clockwise from True North, i.e., 0 is North and 90 is East. May be null.              Only available for some bus runs. | [optional] 
**datetimeUtc** | **Date** | Date and time that the vehicle position data was supplied. | [optional] 
**direction** | **String** | CIS - Metro Train Vehicle Location Direction | [optional] 
**easting** | **Number** | CIS - Metro Train Vehicle Location Easting coordinate | [optional] 
**expiryTime** | **Date** | CIS - Metro Train Vehicle Location data expiry time | [optional] 
**latitude** | **Number** | Geographic coordinate of latitude of the vehicle when known. May be null.              Only available for some bus runs. | [optional] 
**longitude** | **Number** | Geographic coordinate of longitude of the vehicle when known.               Only available for some bus runs. | [optional] 
**northing** | **Number** | CIS - Metro Train Vehicle Location Northing coordinate | [optional] 
**supplier** | **String** | Supplier of vehicle position data. | [optional] 


