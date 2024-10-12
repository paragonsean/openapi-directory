

# Pose

Raw pose measurement for an entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accuracyMeters** | **Float** | The estimated horizontal accuracy of this pose in meters with 68% confidence (one standard deviation). For example, on Android, this value is available from this method: https://developer.android.com/reference/android/location/Location#getAccuracy(). Other platforms have different methods of obtaining similar accuracy estimations. |  [optional] |
|**altitude** | **Double** | Altitude of the pose in meters above WGS84 ellipsoid. NaN indicates an unmeasured quantity. |  [optional] |
|**gpsRecordTimestampUnixEpoch** | **String** | Time of the GPS record since UTC epoch. |  [optional] |
|**heading** | **Double** | The following pose parameters pertain to the center of the photo. They match https://developers.google.com/streetview/spherical-metadata. Compass heading, measured at the center of the photo in degrees clockwise from North. Value must be &gt;&#x3D;0 and &lt;360. NaN indicates an unmeasured quantity. |  [optional] |
|**latLngPair** | [**LatLng**](LatLng.md) |  |  [optional] |
|**level** | [**Level**](Level.md) |  |  [optional] |
|**pitch** | **Double** | Pitch, measured at the center of the photo in degrees. Value must be &gt;&#x3D;-90 and &lt;&#x3D; 90. A value of -90 means looking directly down, and a value of 90 means looking directly up. NaN indicates an unmeasured quantity. |  [optional] |
|**roll** | **Double** | Roll, measured in degrees. Value must be &gt;&#x3D; 0 and &lt;360. A value of 0 means level with the horizon. NaN indicates an unmeasured quantity. |  [optional] |



