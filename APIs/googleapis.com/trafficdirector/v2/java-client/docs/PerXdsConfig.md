

# PerXdsConfig

Detailed config (per xDS) with status. [#next-free-field: 6]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterConfig** | [**ClustersConfigDump**](ClustersConfigDump.md) |  |  [optional] |
|**listenerConfig** | [**ListenersConfigDump**](ListenersConfigDump.md) |  |  [optional] |
|**routeConfig** | [**RoutesConfigDump**](RoutesConfigDump.md) |  |  [optional] |
|**scopedRouteConfig** | [**ScopedRoutesConfigDump**](ScopedRoutesConfigDump.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| SYNCED | &quot;SYNCED&quot; |
| NOT_SENT | &quot;NOT_SENT&quot; |
| STALE | &quot;STALE&quot; |
| ERROR | &quot;ERROR&quot; |



