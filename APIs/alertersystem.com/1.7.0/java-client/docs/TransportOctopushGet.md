

# TransportOctopushGet

The TransportOctopush resource is a collection of transports that carry dispatched alerts to the external Octopush service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**octopushApiKey** | **String** | The API key for the Octopush service. Stored in encrypted format. |  |
|**octopushFrom** | **String** | The sender value for the Octopush service. |  |
|**octopushType** | **String** | The SMS type (&#39;XXX&#39; &#x3D; SMS LowCost; &#39;FR&#39; &#x3D; SMS Premium; &#39;WWW&#39; &#x3D; SMS World) for the Octopush service. |  |
|**octopushUserLogin** | **String** | The user login (email) for the Octopush service. |  |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |



