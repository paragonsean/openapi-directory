# TrafficDirectorApi.PerXdsConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterConfig** | [**ClustersConfigDump**](ClustersConfigDump.md) |  | [optional] 
**listenerConfig** | [**ListenersConfigDump**](ListenersConfigDump.md) |  | [optional] 
**routeConfig** | [**RoutesConfigDump**](RoutesConfigDump.md) |  | [optional] 
**scopedRouteConfig** | [**ScopedRoutesConfigDump**](ScopedRoutesConfigDump.md) |  | [optional] 
**status** | **String** |  | [optional] 



## Enum: StatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `SYNCED` (value: `"SYNCED"`)

* `NOT_SENT` (value: `"NOT_SENT"`)

* `STALE` (value: `"STALE"`)

* `ERROR` (value: `"ERROR"`)




