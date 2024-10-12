

# V3BulkDeparturesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateUtc** | **OffsetDateTime** | Filter by the date and time of the request (ISO 8601 UTC format) (default &#x3D; current date and time) |  [optional] |
|**expand** | [**List&lt;ExpandEnum&gt;**](#List&lt;ExpandEnum&gt;) | List objects to be returned in full (i.e. expanded) - options include: all, stop, route, run, direction, disruption, none |  [optional] |
|**includeCancelled** | **Boolean** | Indicates if cancelled services (if they exist) are returned (default &#x3D; false) - metropolitan train only |  [optional] |
|**includeGeopath** | **Boolean** | Indicates if the route geopath should be returned |  [optional] |
|**lookBackwards** | **Boolean** | Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default &#x3D; false). Requires max_results &amp;gt; 0. |  [optional] |
|**requests** | [**List&lt;V3StopDepartureRequest&gt;**](V3StopDepartureRequest.md) | Collection of departure requests |  |



## Enum: List&lt;ExpandEnum&gt;

| Name | Value |
|---- | -----|
| ALL | &quot;All&quot; |
| STOP | &quot;Stop&quot; |
| ROUTE | &quot;Route&quot; |
| RUN | &quot;Run&quot; |
| DIRECTION | &quot;Direction&quot; |
| DISRUPTION | &quot;Disruption&quot; |
| VEHICLE_DESCRIPTOR | &quot;VehicleDescriptor&quot; |
| VEHICLE_POSITION | &quot;VehiclePosition&quot; |
| NONE | &quot;None&quot; |



