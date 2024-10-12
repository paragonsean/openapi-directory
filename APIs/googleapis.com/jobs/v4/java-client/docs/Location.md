

# Location

A resource that represents a location with full geographic information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**latLng** | [**LatLng**](LatLng.md) |  |  [optional] |
|**locationType** | [**LocationTypeEnum**](#LocationTypeEnum) | The type of a location, which corresponds to the address lines field of google.type.PostalAddress. For example, \&quot;Downtown, Atlanta, GA, USA\&quot; has a type of LocationType.NEIGHBORHOOD, and \&quot;Kansas City, KS, USA\&quot; has a type of LocationType.LOCALITY. |  [optional] |
|**postalAddress** | [**PostalAddress**](PostalAddress.md) |  |  [optional] |
|**radiusMiles** | **Double** | Radius in miles of the job location. This value is derived from the location bounding box in which a circle with the specified radius centered from google.type.LatLng covers the area associated with the job location. For example, currently, \&quot;Mountain View, CA, USA\&quot; has a radius of 6.17 miles. |  [optional] |



## Enum: LocationTypeEnum

| Name | Value |
|---- | -----|
| LOCATION_TYPE_UNSPECIFIED | &quot;LOCATION_TYPE_UNSPECIFIED&quot; |
| COUNTRY | &quot;COUNTRY&quot; |
| ADMINISTRATIVE_AREA | &quot;ADMINISTRATIVE_AREA&quot; |
| SUB_ADMINISTRATIVE_AREA | &quot;SUB_ADMINISTRATIVE_AREA&quot; |
| LOCALITY | &quot;LOCALITY&quot; |
| POSTAL_CODE | &quot;POSTAL_CODE&quot; |
| SUB_LOCALITY | &quot;SUB_LOCALITY&quot; |
| SUB_LOCALITY_1 | &quot;SUB_LOCALITY_1&quot; |
| SUB_LOCALITY_2 | &quot;SUB_LOCALITY_2&quot; |
| NEIGHBORHOOD | &quot;NEIGHBORHOOD&quot; |
| STREET_ADDRESS | &quot;STREET_ADDRESS&quot; |



