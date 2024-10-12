# ClimateFieldViewPlatformApis.Upload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentType** | **String** | Content type representing data being uploaded (e.g. image/vnd.climate.rgb.geotiff) | 
**length** | **Number** | Content size in bytes | 
**md5** | **String** | Base64 encoded md5 hash of the content | 
**metadata** | **{String: Object}** |  | [optional] 



## Enum: ContentTypeEnum


* `image/vnd.climate.thermal.geotiff` (value: `"image/vnd.climate.thermal.geotiff"`)

* `image/vnd.climate.ndvi.geotiff` (value: `"image/vnd.climate.ndvi.geotiff"`)

* `image/vnd.climate.rgb.geotiff` (value: `"image/vnd.climate.rgb.geotiff"`)

* `image/vnd.climate.rgb-nir.geotiff` (value: `"image/vnd.climate.rgb-nir.geotiff"`)

* `image/vnd.climate.rgb-cir.geotiff` (value: `"image/vnd.climate.rgb-cir.geotiff"`)

* `image/vnd.climate.waterstress.geotiff` (value: `"image/vnd.climate.waterstress.geotiff"`)

* `image/vnd.climate.elevation.geotiff` (value: `"image/vnd.climate.elevation.geotiff"`)

* `image/vnd.climate.raw.geotiff` (value: `"image/vnd.climate.raw.geotiff"`)

* `application/vnd.climate.field.geojson` (value: `"application/vnd.climate.field.geojson"`)

* `application/vnd.climate.rx.planting.shp` (value: `"application/vnd.climate.rx.planting.shp"`)

* `application/vnd.climate.prescription.zones.shp` (value: `"application/vnd.climate.prescription.zones.shp"`)

* `application/vnd.climate.modus.xml` (value: `"application/vnd.climate.modus.xml"`)

* `application/vnd.climate.stand-count.geojson` (value: `"application/vnd.climate.stand-count.geojson"`)

* `application/vnd.climate.weed-count.geojson` (value: `"application/vnd.climate.weed-count.geojson"`)

* `application/vnd.climate.as-applied.zip` (value: `"application/vnd.climate.as-applied.zip"`)

* `application/vnd.climate.as-planted.zip` (value: `"application/vnd.climate.as-planted.zip"`)

* `application/vnd.climate.as-harvested.zip` (value: `"application/vnd.climate.as-harvested.zip"`)




