

# TransportFirebaseJsonldPost

The TransportFirebase resource is a collection of transports that carry dispatched alerts to the external Firebase service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**firebasePassword** | **String** | The password for the Firebase service. Stored in encrypted format. |  |
|**firebaseUsername** | **String** | The username for the Firebase service. |  |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



