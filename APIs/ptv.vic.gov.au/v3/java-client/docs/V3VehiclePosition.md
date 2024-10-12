

# V3VehiclePosition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bearing** | **Double** | Compass bearing of the vehicle when known, clockwise from True North, i.e., 0 is North and 90 is East. May be null.              Only available for some bus runs. |  [optional] |
|**datetimeUtc** | **OffsetDateTime** | Date and time that the vehicle position data was supplied. |  [optional] |
|**direction** | **String** | CIS - Metro Train Vehicle Location Direction |  [optional] |
|**easting** | **Double** | CIS - Metro Train Vehicle Location Easting coordinate |  [optional] |
|**expiryTime** | **OffsetDateTime** | CIS - Metro Train Vehicle Location data expiry time |  [optional] |
|**latitude** | **Double** | Geographic coordinate of latitude of the vehicle when known. May be null.              Only available for some bus runs. |  [optional] |
|**longitude** | **Double** | Geographic coordinate of longitude of the vehicle when known.               Only available for some bus runs. |  [optional] |
|**northing** | **Double** | CIS - Metro Train Vehicle Location Northing coordinate |  [optional] |
|**supplier** | **String** | Supplier of vehicle position data. |  [optional] |



