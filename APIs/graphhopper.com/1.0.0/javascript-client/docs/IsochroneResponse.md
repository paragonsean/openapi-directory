# GraphHopperDirectionsApi.IsochroneResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyrights** | **[String]** |  | [optional] 
**polygons** | [**[IsochroneResponsePolygon]**](IsochroneResponsePolygon.md) | The list of polygons in GeoJson format. It can be used e.g. in the Leaflet framework:  &#x60;&#x60;&#x60; L.geoJson(json.polygons).addTo(map) &#x60;&#x60;&#x60;  The number of polygon is identical to the specified buckets in the query. Every polygon contains the bucket number in the properties section of the GeoJson.  | [optional] 


