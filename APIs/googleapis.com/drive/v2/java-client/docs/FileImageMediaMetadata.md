

# FileImageMediaMetadata

Output only. Metadata about image media. This will only be present for image types, and its contents will depend on what can be parsed from the image content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aperture** | **Float** | Output only. The aperture used to create the photo (f-number). |  [optional] |
|**cameraMake** | **String** | Output only. The make of the camera used to create the photo. |  [optional] |
|**cameraModel** | **String** | Output only. The model of the camera used to create the photo. |  [optional] |
|**colorSpace** | **String** | Output only. The color space of the photo. |  [optional] |
|**date** | **String** | Output only. The date and time the photo was taken (EXIF format timestamp). |  [optional] |
|**exposureBias** | **Float** | Output only. The exposure bias of the photo (APEX value). |  [optional] |
|**exposureMode** | **String** | Output only. The exposure mode used to create the photo. |  [optional] |
|**exposureTime** | **Float** | Output only. The length of the exposure, in seconds. |  [optional] |
|**flashUsed** | **Boolean** | Output only. Whether a flash was used to create the photo. |  [optional] |
|**focalLength** | **Float** | Output only. The focal length used to create the photo, in millimeters. |  [optional] |
|**height** | **Integer** | Output only. The height of the image in pixels. |  [optional] |
|**isoSpeed** | **Integer** | Output only. The ISO speed used to create the photo. |  [optional] |
|**lens** | **String** | Output only. The lens used to create the photo. |  [optional] |
|**location** | [**FileImageMediaMetadataLocation**](FileImageMediaMetadataLocation.md) |  |  [optional] |
|**maxApertureValue** | **Float** | Output only. The smallest f-number of the lens at the focal length used to create the photo (APEX value). |  [optional] |
|**meteringMode** | **String** | Output only. The metering mode used to create the photo. |  [optional] |
|**rotation** | **Integer** | Output only. The number of clockwise 90 degree rotations applied from the image&#39;s original orientation. |  [optional] |
|**sensor** | **String** | Output only. The type of sensor used to create the photo. |  [optional] |
|**subjectDistance** | **Integer** | Output only. The distance to the subject of the photo, in meters. |  [optional] |
|**whiteBalance** | **String** | Output only. The white balance mode used to create the photo. |  [optional] |
|**width** | **Integer** | Output only. The width of the image in pixels. |  [optional] |



