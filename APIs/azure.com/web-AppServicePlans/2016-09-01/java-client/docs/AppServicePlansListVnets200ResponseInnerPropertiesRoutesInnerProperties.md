

# AppServicePlansListVnets200ResponseInnerPropertiesRoutesInnerProperties

VnetRoute resource specific properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endAddress** | **String** | The ending address for this route. If the start address is specified in CIDR notation, this must be omitted. |  [optional] |
|**name** | **String** | The name of this route. This is only returned by the server and does not need to be set by the client. |  [optional] |
|**routeType** | [**RouteTypeEnum**](#RouteTypeEnum) | The type of route this is: DEFAULT - By default, every app has routes to the local address ranges specified by RFC1918 INHERITED - Routes inherited from the real Virtual Network routes STATIC - Static route set on the app only  These values will be used for syncing an app&#39;s routes with those from a Virtual Network. |  [optional] |
|**startAddress** | **String** | The starting address for this route. This may also include a CIDR notation, in which case the end address must not be specified. |  [optional] |



## Enum: RouteTypeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| INHERITED | &quot;INHERITED&quot; |
| STATIC | &quot;STATIC&quot; |



