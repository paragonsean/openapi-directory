

# LocationKey

Alternate/surrogate key references for a location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**explicitNoPlaceId** | **Boolean** | Output only. A value of true indicates that an unset place ID is deliberate, which is different from no association being made yet. |  [optional] |
|**placeId** | **String** | If this location has been verified and is connected to/appears on Google Maps, this field is populated with the place ID for the location. This ID can be used in various Places APIs. If this location is unverified, this field may be populated if the location has been associated with a place that appears on Google Maps. This field can be set during Create calls, but not for Update. The additional &#x60;explicit_no_place_id&#x60; bool qualifies whether an unset place ID is deliberate or not. |  [optional] |
|**plusPageId** | **String** | Output only. If this location has a Google+ page associated with it, this is populated with the Google+ page ID for this location. |  [optional] |
|**requestId** | **String** | Output only. The &#x60;request_id&#x60; used to create this location. May be empty if this location was created outside of the Google My Business API or Business Profile Locations. |  [optional] |



