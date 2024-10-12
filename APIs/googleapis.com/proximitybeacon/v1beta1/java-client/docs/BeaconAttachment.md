

# BeaconAttachment

Project-specific data associated with a beacon.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachmentName** | **String** | Resource name of this attachment. Attachment names have the format: beacons/ beacon_id/attachments/attachment_id. Leave this empty on creation. |  [optional] |
|**creationTimeMs** | **String** | The UTC time when this attachment was created, in milliseconds since the UNIX epoch. |  [optional] |
|**data** | **byte[]** | An opaque data container for client-provided data. Must be [base64](http://tools.ietf.org/html/rfc4648#section-4) encoded in HTTP requests, and will be so encoded (with padding) in responses. Required. |  [optional] |
|**maxDistanceMeters** | **Double** | The distance away from the beacon at which this attachment should be delivered to a mobile app. Setting this to a value greater than zero indicates that the app should behave as if the beacon is \&quot;seen\&quot; when the mobile device is less than this distance away from the beacon. Different attachments on the same beacon can have different max distances. Note that even though this value is expressed with fractional meter precision, real-world behavior is likley to be much less precise than one meter, due to the nature of current Bluetooth radio technology. Optional. When not set or zero, the attachment should be delivered at the beacon&#39;s outer limit of detection. Negative values are invalid and return an error. |  [optional] |
|**namespacedType** | **String** | Specifies what kind of attachment this is. Tells a client how to interpret the &#x60;data&#x60; field. Format is namespace/type. Namespace provides type separation between clients. Type describes the type of &#x60;data&#x60;, for use by the client when parsing the &#x60;data&#x60; field. Required. |  [optional] |



