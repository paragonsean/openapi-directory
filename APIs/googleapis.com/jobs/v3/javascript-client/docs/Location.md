# CloudTalentSolutionApi.Location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latLng** | [**LatLng**](LatLng.md) |  | [optional] 
**locationType** | **String** | The type of a location, which corresponds to the address lines field of PostalAddress. For example, \&quot;Downtown, Atlanta, GA, USA\&quot; has a type of LocationType#NEIGHBORHOOD, and \&quot;Kansas City, KS, USA\&quot; has a type of LocationType#LOCALITY. | [optional] 
**postalAddress** | [**PostalAddress**](PostalAddress.md) |  | [optional] 
**radiusInMiles** | **Number** | Radius in miles of the job location. This value is derived from the location bounding box in which a circle with the specified radius centered from LatLng covers the area associated with the job location. For example, currently, \&quot;Mountain View, CA, USA\&quot; has a radius of 6.17 miles. | [optional] 



## Enum: LocationTypeEnum


* `LOCATION_TYPE_UNSPECIFIED` (value: `"LOCATION_TYPE_UNSPECIFIED"`)

* `COUNTRY` (value: `"COUNTRY"`)

* `ADMINISTRATIVE_AREA` (value: `"ADMINISTRATIVE_AREA"`)

* `SUB_ADMINISTRATIVE_AREA` (value: `"SUB_ADMINISTRATIVE_AREA"`)

* `LOCALITY` (value: `"LOCALITY"`)

* `POSTAL_CODE` (value: `"POSTAL_CODE"`)

* `SUB_LOCALITY` (value: `"SUB_LOCALITY"`)

* `SUB_LOCALITY_1` (value: `"SUB_LOCALITY_1"`)

* `SUB_LOCALITY_2` (value: `"SUB_LOCALITY_2"`)

* `NEIGHBORHOOD` (value: `"NEIGHBORHOOD"`)

* `STREET_ADDRESS` (value: `"STREET_ADDRESS"`)




