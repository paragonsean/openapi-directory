

# EventsV1Subscription


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The unique SID identifier of the Account. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date that this Subscription was created, given in ISO 8601 format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date that this Subscription was updated, given in ISO 8601 format. |  [optional] |
|**description** | **String** | A human readable description for the Subscription |  [optional] |
|**links** | **Object** | Contains a dictionary of URL links to nested resources of this Subscription. |  [optional] |
|**sid** | **String** | A 34 character string that uniquely identifies this Subscription. |  [optional] |
|**sinkSid** | **String** | The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created. |  [optional] |
|**url** | **URI** | The URL of this resource. |  [optional] |



