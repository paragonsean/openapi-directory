

# PointPointData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alerts** | [**PointPointAlerts**](PointPointAlerts.md) |  |  |
|**current** | [**PointPointCurrentData**](PointPointCurrentData.md) |  |  [optional] |
|**daily** | [**PointPointDaily**](PointPointDaily.md) |  |  [optional] |
|**elevation** | **Integer** | Elevation above sea level in metres (for units &#39;metric&#39;, &#39;uk&#39;, &#39;ca&#39;) or feet (for units &#39;us&#39;) |  |
|**hourly** | [**PointPointHourly**](PointPointHourly.md) |  |  [optional] |
|**lat** | **String** | Latitude of the point, always in the format &lt;float&gt;&lt;N/S&gt;, for example &#x60;&#x60;23.5S&#x60;&#x60; |  |
|**lon** | **String** | Longitude of the point, always in the format &lt;float&gt;&lt;E/W&gt;, for example &#x60;&#x60;23.5W&#x60;&#x60; |  |
|**minutely** | [**PointPointMinutely**](PointPointMinutely.md) |  |  [optional] |
|**timezone** | **String** | Name of the timezone in format like &#39;Europe/London&#39;. Available only when the place is specified through place ID. |  [optional] |
|**units** | **String** | Unit system (metric, uk, ca or us) |  |



