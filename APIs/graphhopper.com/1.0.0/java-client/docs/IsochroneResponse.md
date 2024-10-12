

# IsochroneResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copyrights** | **List&lt;String&gt;** |  |  [optional] |
|**polygons** | [**List&lt;IsochroneResponsePolygon&gt;**](IsochroneResponsePolygon.md) | The list of polygons in GeoJson format. It can be used e.g. in the Leaflet framework:  &#x60;&#x60;&#x60; L.geoJson(json.polygons).addTo(map) &#x60;&#x60;&#x60;  The number of polygon is identical to the specified buckets in the query. Every polygon contains the bucket number in the properties section of the GeoJson.  |  [optional] |



