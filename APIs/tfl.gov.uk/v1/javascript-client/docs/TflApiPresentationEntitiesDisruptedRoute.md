# TransportForLondonUnifiedApi.TflApiPresentationEntitiesDisruptedRoute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationName** | **String** | The name of the Destination StopPoint | [optional] 
**direction** | **String** | Inbound or Outbound | [optional] 
**id** | **String** | The Id of the route | [optional] 
**isEntireRouteSection** | **Boolean** | Whether this represents the entire route section | [optional] 
**lineId** | **String** | The Id of the Line | [optional] 
**lineString** | **String** | The co-ordinates of the route&#39;s path as a geoJSON lineString | [optional] 
**name** | **String** | Name such as \&quot;72\&quot; | [optional] 
**originationName** | **String** | The name of the Origin StopPoint | [optional] 
**routeCode** | **String** | The route code | [optional] 
**routeSectionNaptanEntrySequence** | [**[TflApiPresentationEntitiesRouteSectionNaptanEntrySequence]**](TflApiPresentationEntitiesRouteSectionNaptanEntrySequence.md) |  | [optional] 
**validFrom** | **Date** | The DateTime that the Service containing this Route is valid from. | [optional] 
**validTo** | **Date** | The DateTime that the Service containing this Route is valid until. | [optional] 
**via** | [**TflApiPresentationEntitiesRouteSectionNaptanEntrySequence**](TflApiPresentationEntitiesRouteSectionNaptanEntrySequence.md) |  | [optional] 


