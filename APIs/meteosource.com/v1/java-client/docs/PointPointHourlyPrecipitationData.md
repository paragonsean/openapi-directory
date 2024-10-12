

# PointPointHourlyPrecipitationData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**convective** | **BigDecimal** | Total precipitation amount accumulated since last hour. Units: metric &#x3D; mm/h, us &#x3D; inches per hour, uk &#x3D; mm/h, ca &#x3D; mm/h |  [optional] |
|**rainspot** | **File** | Precipitation in the surrounding of queried location. The data is 7x7 ASCII art string, queried location being in the center. Character &#x60;#&#x60; means there is precipitation, &#x60;.&#x60; means no precipitation. The distance between neighboring cells is 0.25°. Unit: rainspot |  [optional] |
|**total** | **BigDecimal** | Total precipitation amount accumulated since last hour. Units: metric &#x3D; mm/h, us &#x3D; inches per hour, uk &#x3D; mm/h, ca &#x3D; mm/h |  [optional] |
|**type** | **File** | Precipitation type, may be one of:  * &#x60;none&#x60;, it there is no precipitation * &#x60;rain&#x60; * &#x60;snow&#x60; * &#x60;rain_snow&#x60; * &#x60;ice pellets&#x60; * &#x60;frozen rain&#x60;  Unit: precipitation type |  [optional] |



