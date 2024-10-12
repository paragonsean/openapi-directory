# NprListeningService.ImageLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **String** | The link to be followed | 
**caption** | **String** | The caption of the image; can be used as alternate text for accessibility | [optional] 
**contentType** | **String** | The MIME type of the response of this link; note that the enumerated list of possible values is not exhaustive and other MIME types could occur. The list should be treated as examples, rather than absolutes. | [default to &#39;image/jpeg&#39;]
**image** | **String** | A unique identifier for the image | [optional] 
**producer** | **String** | The producer of the image; should be used for properly attributing the image when it exists | [optional] 
**provider** | **String** | The provider of the image; should be used for properly attributing the image when it exists | [optional] 
**rel** | **String** | The crop type or intended display style/size; note that the enumerated list of possible values is not exhaustive and other values could occur. The list should be treated as examples, rather than absolutes. | [optional] [default to &#39;logo_square&#39;]



## Enum: ContentTypeEnum


* `jpeg` (value: `"image/jpeg"`)

* `png` (value: `"image/png"`)

* `gif` (value: `"image/gif"`)





## Enum: RelEnum


* `logo_square` (value: `"logo_square"`)

* `icon` (value: `"icon"`)

* `wide` (value: `"wide"`)

* `standard` (value: `"standard"`)

* `square` (value: `"square"`)

* `enlargement` (value: `"enlargement"`)

* `custom` (value: `"custom"`)




