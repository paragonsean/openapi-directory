# ProximityBeaconApi.Diagnostics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | **[String]** | An unordered list of Alerts that the beacon has. | [optional] 
**beaconName** | **String** | Resource name of the beacon. For Eddystone-EID beacons, this may be the beacon&#39;s current EID, or the beacon&#39;s \&quot;stable\&quot; Eddystone-UID. | [optional] 
**estimatedLowBatteryDate** | [**ModelDate**](ModelDate.md) |  | [optional] 



## Enum: [AlertsEnum]


* `ALERT_UNSPECIFIED` (value: `"ALERT_UNSPECIFIED"`)

* `WRONG_LOCATION` (value: `"WRONG_LOCATION"`)

* `LOW_BATTERY` (value: `"LOW_BATTERY"`)

* `LOW_ACTIVITY` (value: `"LOW_ACTIVITY"`)




