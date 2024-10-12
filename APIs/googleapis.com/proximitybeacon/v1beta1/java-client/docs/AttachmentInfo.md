

# AttachmentInfo

A subset of attachment information served via the `beaconinfo.getforobserved` method, used when your users encounter your beacons.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **byte[]** | An opaque data container for client-provided data. |  [optional] |
|**maxDistanceMeters** | **Double** | The distance away from the beacon at which this attachment should be delivered to a mobile app. Setting this to a value greater than zero indicates that the app should behave as if the beacon is \&quot;seen\&quot; when the mobile device is less than this distance away from the beacon. Different attachments on the same beacon can have different max distances. Note that even though this value is expressed with fractional meter precision, real-world behavior is likley to be much less precise than one meter, due to the nature of current Bluetooth radio technology. Optional. When not set or zero, the attachment should be delivered at the beacon&#39;s outer limit of detection. |  [optional] |
|**namespacedType** | **String** | Specifies what kind of attachment this is. Tells a client how to interpret the &#x60;data&#x60; field. Format is namespace/type, for example scrupulous-wombat-12345/welcome-message |  [optional] |



