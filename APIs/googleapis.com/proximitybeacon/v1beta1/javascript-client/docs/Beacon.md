# ProximityBeaconApi.Beacon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertisedId** | [**AdvertisedId**](AdvertisedId.md) |  | [optional] 
**beaconName** | **String** | Resource name of this beacon. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. This field must be left empty when registering. After reading a beacon, clients can use the name for future operations. | [optional] 
**description** | **String** | Free text used to identify and describe the beacon. Maximum length 140 characters. Optional. | [optional] 
**ephemeralIdRegistration** | [**EphemeralIdRegistration**](EphemeralIdRegistration.md) |  | [optional] 
**expectedStability** | **String** | Expected location stability. This is set when the beacon is registered or updated, not automatically detected in any way. Optional. | [optional] 
**indoorLevel** | [**IndoorLevel**](IndoorLevel.md) |  | [optional] 
**latLng** | [**LatLng**](LatLng.md) |  | [optional] 
**placeId** | **String** | The [Google Places API](/places/place-id) Place ID of the place where the beacon is deployed. This is given when the beacon is registered or updated, not automatically detected in any way. Optional. | [optional] 
**properties** | **{String: String}** | Properties of the beacon device, for example battery type or firmware version. Optional. | [optional] 
**provisioningKey** | **Blob** | Some beacons may require a user to provide an authorization key before changing any of its configuration (e.g. broadcast frames, transmit power). This field provides a place to store and control access to that key. This field is populated in responses to &#x60;GET /v1beta1/beacons/3!beaconId&#x60; from users with write access to the given beacon. That is to say: If the user is authorized to write the beacon&#39;s confidential data in the service, the service considers them authorized to configure the beacon. Note that this key grants nothing on the service, only on the beacon itself. | [optional] 
**status** | **String** | Current status of the beacon. Required. | [optional] 



## Enum: ExpectedStabilityEnum


* `STABILITY_UNSPECIFIED` (value: `"STABILITY_UNSPECIFIED"`)

* `STABLE` (value: `"STABLE"`)

* `PORTABLE` (value: `"PORTABLE"`)

* `MOBILE` (value: `"MOBILE"`)

* `ROVING` (value: `"ROVING"`)





## Enum: StatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DECOMMISSIONED` (value: `"DECOMMISSIONED"`)

* `INACTIVE` (value: `"INACTIVE"`)




