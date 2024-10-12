

# GoogleLocation

Represents a Location that is present on Google. This can be a location that has been claimed by the user, someone else, or could be unclaimed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | [**Location**](Location.md) |  |  [optional] |
|**name** | **String** | Resource name of this GoogleLocation, in the format &#x60;googleLocations/{googleLocationId}&#x60;. |  [optional] |
|**requestAdminRightsUri** | **String** | A URL that will redirect the user to the request admin rights UI. This field is only present if the location has already been claimed by any user, including the current user. |  [optional] |



