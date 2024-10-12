

# RequestRelationsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ids** | **List&lt;String&gt;** | Specifies an array of shipment and/or service ids that are in relation. If you deal with services then you need to use the id of your services in ids. To also consider sequences of the pickups and deliveries of your shipments, you need to use a special ID, i.e. use your shipment id plus the keyword &#x60;_pickup&#x60; or &#x60;_delivery&#x60;. If you want to place a service or shipment activity at the beginning of your route, use the special ID &#x60;start&#x60;. In turn, use &#x60;end&#x60; to place it at the end of the route. |  |
|**type** | **String** | Specifies the type of relation. It must be either of type &#x60;in_sequence&#x60; or &#x60;in_direct_sequence&#x60;.  |  |
|**vehicleId** | **String** | Id of pre-assigned vehicle, i.e. the vehicle id that is determined to conduct the services and shipments in this relation. |  [optional] |
|**groups** | **List&lt;String&gt;** | An array of groups that should be related |  |



