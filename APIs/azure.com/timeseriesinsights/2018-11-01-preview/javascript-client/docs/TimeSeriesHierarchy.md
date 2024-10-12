# TimeSeriesInsightsClient.TimeSeriesHierarchy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique hierarchy identifier that is a immutable GUID. Can be null while creating hierarchy objects and then server generates the id, not null on get and delete operations. | [optional] 
**name** | **String** | User-given unique name for the type. It is mutable and not null. | 
**source** | [**TimeSeriesHierarchySource**](TimeSeriesHierarchySource.md) |  | 


