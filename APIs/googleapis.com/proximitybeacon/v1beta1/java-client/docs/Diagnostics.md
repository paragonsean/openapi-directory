

# Diagnostics

Diagnostics for a single beacon.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alerts** | [**List&lt;AlertsEnum&gt;**](#List&lt;AlertsEnum&gt;) | An unordered list of Alerts that the beacon has. |  [optional] |
|**beaconName** | **String** | Resource name of the beacon. For Eddystone-EID beacons, this may be the beacon&#39;s current EID, or the beacon&#39;s \&quot;stable\&quot; Eddystone-UID. |  [optional] |
|**estimatedLowBatteryDate** | [**Date**](Date.md) |  |  [optional] |



## Enum: List&lt;AlertsEnum&gt;

| Name | Value |
|---- | -----|
| ALERT_UNSPECIFIED | &quot;ALERT_UNSPECIFIED&quot; |
| WRONG_LOCATION | &quot;WRONG_LOCATION&quot; |
| LOW_BATTERY | &quot;LOW_BATTERY&quot; |
| LOW_ACTIVITY | &quot;LOW_ACTIVITY&quot; |



