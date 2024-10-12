

# GeolocResultsDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**qtime** | **Long** | The execution time of the query in ms |  [optional] |
|**error** | **String** | A String only present if an error occured (e.g : empty Latitude or longitude) |  [optional] |
|**numFound** | **Integer** | The number of results display with this query (it takes the pagination into account) |  [optional] |
|**result** | [**List&lt;GisFeatureDistance&gt;**](GisFeatureDistance.md) |  |  [optional] |



