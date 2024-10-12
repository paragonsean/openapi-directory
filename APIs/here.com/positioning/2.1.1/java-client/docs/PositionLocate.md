

# PositionLocate

Object containing information on a location where a measurement was taken.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accuracy** | **BigDecimal** | Uncertainty circle radius in meters (degree of confidence according to the &#x60;confidence&#x60; parameter). |  |
|**alt** | **BigDecimal** | Altitude in meters (referenced to the WGS-84 ellipsoid) negative or positive. |  [optional] |
|**altAccuracy** | **BigDecimal** | Uncertainty of the altitude estimate in meters (degree of confidence according to the &#x60;confidence&#x60; parameter). This field superceeds old &#x60;altaccuracy&#x60;.  |  [optional] |
|**lat** | **BigDecimal** | Latitude in WGS-84 format, decimal representation ranging from -90 to 90. |  |
|**lng** | **BigDecimal** | Longitude in WGS-84 format, decimal representation ranging from -180 to 180. |  |



