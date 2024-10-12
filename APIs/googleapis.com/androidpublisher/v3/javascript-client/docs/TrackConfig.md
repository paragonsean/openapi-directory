# GooglePlayAndroidDeveloperApi.TrackConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formFactor** | **String** | Required. Form factor of the new track. Defaults to the default track. | [optional] 
**track** | **String** | Required. Identifier of the new track. For default tracks, this field consists of the track alias only. Form factor tracks have a special prefix as an identifier, for example &#x60;wear:production&#x60;, &#x60;automotive:production&#x60;. This prefix must match the value of the &#x60;form_factor&#x60; field, if it is not a default track. [More on track name](https://developers.google.com/android-publisher/tracks#ff-track-name) | [optional] 
**type** | **String** | Required. Type of the new track. Currently, the only supported value is closedTesting. | [optional] 



## Enum: FormFactorEnum


* `FORM_FACTOR_UNSPECIFIED` (value: `"FORM_FACTOR_UNSPECIFIED"`)

* `DEFAULT` (value: `"DEFAULT"`)

* `WEAR` (value: `"WEAR"`)

* `AUTOMOTIVE` (value: `"AUTOMOTIVE"`)





## Enum: TypeEnum


* `TRACK_TYPE_UNSPECIFIED` (value: `"TRACK_TYPE_UNSPECIFIED"`)

* `CLOSED_TESTING` (value: `"CLOSED_TESTING"`)




