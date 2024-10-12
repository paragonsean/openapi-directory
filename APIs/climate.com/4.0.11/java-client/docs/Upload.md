

# Upload

Client request to upload data for a user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) | Content type representing data being uploaded (e.g. image/vnd.climate.rgb.geotiff) |  |
|**length** | **Long** | Content size in bytes |  |
|**md5** | **String** | Base64 encoded md5 hash of the content |  |
|**metadata** | **Map&lt;String, Object&gt;** |  |  [optional] |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| IMAGE_VND_CLIMATE_THERMAL_GEOTIFF | &quot;image/vnd.climate.thermal.geotiff&quot; |
| IMAGE_VND_CLIMATE_NDVI_GEOTIFF | &quot;image/vnd.climate.ndvi.geotiff&quot; |
| IMAGE_VND_CLIMATE_RGB_GEOTIFF | &quot;image/vnd.climate.rgb.geotiff&quot; |
| IMAGE_VND_CLIMATE_RGB_NIR_GEOTIFF | &quot;image/vnd.climate.rgb-nir.geotiff&quot; |
| IMAGE_VND_CLIMATE_RGB_CIR_GEOTIFF | &quot;image/vnd.climate.rgb-cir.geotiff&quot; |
| IMAGE_VND_CLIMATE_WATERSTRESS_GEOTIFF | &quot;image/vnd.climate.waterstress.geotiff&quot; |
| IMAGE_VND_CLIMATE_ELEVATION_GEOTIFF | &quot;image/vnd.climate.elevation.geotiff&quot; |
| IMAGE_VND_CLIMATE_RAW_GEOTIFF | &quot;image/vnd.climate.raw.geotiff&quot; |
| APPLICATION_VND_CLIMATE_FIELD_GEOJSON | &quot;application/vnd.climate.field.geojson&quot; |
| APPLICATION_VND_CLIMATE_RX_PLANTING_SHP | &quot;application/vnd.climate.rx.planting.shp&quot; |
| APPLICATION_VND_CLIMATE_PRESCRIPTION_ZONES_SHP | &quot;application/vnd.climate.prescription.zones.shp&quot; |
| APPLICATION_VND_CLIMATE_MODUS_XML | &quot;application/vnd.climate.modus.xml&quot; |
| APPLICATION_VND_CLIMATE_STAND_COUNT_GEOJSON | &quot;application/vnd.climate.stand-count.geojson&quot; |
| APPLICATION_VND_CLIMATE_WEED_COUNT_GEOJSON | &quot;application/vnd.climate.weed-count.geojson&quot; |
| APPLICATION_VND_CLIMATE_AS_APPLIED_ZIP | &quot;application/vnd.climate.as-applied.zip&quot; |
| APPLICATION_VND_CLIMATE_AS_PLANTED_ZIP | &quot;application/vnd.climate.as-planted.zip&quot; |
| APPLICATION_VND_CLIMATE_AS_HARVESTED_ZIP | &quot;application/vnd.climate.as-harvested.zip&quot; |



