

# RemoveBgJson


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addShadow** | **Boolean** | Whether to add an artificial shadow to the result (default: false). NOTE: Adding shadows is currently only supported for car photos. Other subjects are returned without shadow, even if set to true (this might change in the future).  |  [optional] |
|**bgColor** | **String** | Adds a solid color background. Can be a hex color code (e.g. 81d4fa, fff) or a color name (e.g. green). For semi-transparency, 4-/8-digit hex codes are also supported (e.g. 81d4fa77). (If this parameter is present, the other bg_ parameters must be empty.)  |  [optional] |
|**bgImageUrl** | **String** | Adds a background image from a URL. The image is centered and resized to fill the canvas while preserving the aspect ratio, unless it already has the exact same dimensions as the foreground image. (If this parameter is present, the other bg_ parameters must be empty.) |  [optional] |
|**channels** | [**ChannelsEnum**](#ChannelsEnum) | Request either the finalized image (\&quot;rgba\&quot;, default) or an alpha mask (\&quot;alpha\&quot;). Note: Since remove.bg also applies RGB color corrections on edges, using only the alpha mask often leads to a lower final image quality. Therefore \&quot;rgba\&quot; is recommended.  |  [optional] |
|**crop** | **Boolean** | Whether to crop off all empty regions (default: false). Note that cropping has no effect on the amount of charged credits.  |  [optional] |
|**cropMargin** | **String** | Adds a margin around the cropped subject (default: 0). Can be an absolute value (e.g. \&quot;30px\&quot;) or relative to the subject size (e.g. \&quot;10%\&quot;). Can be a single value (all sides), two values (top/bottom and left/right) or four values (top, right, bottom, left). This parameter only has an effect when \&quot;crop&#x3D;true\&quot;. The maximum margin that can be added on each side is 50% of the subject dimensions or 500 pixels.  |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Result image format: \&quot;auto\&quot; &#x3D; Use PNG format if transparent regions exist, otherwise use JPG format (default), \&quot;png\&quot; &#x3D; PNG format with alpha transparency, \&quot;jpg\&quot; &#x3D; JPG format, no transparency, \&quot;zip\&quot; &#x3D; ZIP format, contains color image and alpha matte image, supports transparency (recommended).  |  [optional] |
|**imageFileB64** | **String** | Source image file (base64-encoded string). (If this parameter is present, the other image source parameters must be empty.) |  [optional] |
|**imageUrl** | **String** | Source image URL. (If this parameter is present, the other image source parameters must be empty.) |  [optional] |
|**position** | **String** | Positions the subject within the image canvas. Can be \&quot;original\&quot; (default unless \&quot;scale\&quot; is given), \&quot;center\&quot; (default when \&quot;scale\&quot; is given) or a value from \&quot;0%\&quot; to \&quot;100%\&quot; (both horizontal and vertical) or two values (horizontal, vertical).  |  [optional] |
|**roi** | **String** | Region of interest: Only contents of this rectangular region can be detected as foreground. Everything outside is considered background and will be removed. The rectangle is defined as two x/y coordinates in the format \&quot;x1 y1 x2 y2\&quot;. The coordinates can be in absolute pixels (suffix &#39;px&#39;) or relative to the width/height of the image (suffix &#39;%&#39;). By default, the whole image is the region of interest (\&quot;0% 0% 100% 100%\&quot;).  |  [optional] |
|**scale** | **String** | Scales the subject relative to the total image size. Can be any value from \&quot;10%\&quot; to \&quot;100%\&quot;, or \&quot;original\&quot; (default). Scaling the subject implies \&quot;position&#x3D;center\&quot; (unless specified otherwise).  |  [optional] |
|**semitransparency** | **Boolean** | Whether to have semi-transparent regions in the result (default: true). NOTE: Semitransparency is currently only supported for car windows (this might change in the future). Other objects are returned without semitransparency, even if set to true.  |  [optional] |
|**size** | [**SizeEnum**](#SizeEnum) | Maximum output image resolution: \&quot;preview\&quot; (default) &#x3D; Resize image to 0.25 megapixels (e.g. 625×400 pixels) – 0.25 credits per image, \&quot;full\&quot; &#x3D; Use original image resolution, up to 25 megapixels (e.g. 6250x4000) with formats ZIP or JPG, or up to 10 megapixels (e.g. 4000x2500) with PNG – 1 credit per image), \&quot;auto\&quot; &#x3D; Use highest available resolution (based on image size and available credits).  For backwards-compatibility this parameter also accepts the values \&quot;medium\&quot; (up to 1.5 megapixels) and \&quot;hd\&quot; (up to 4 megapixels) for 1 credit per image. The value \&quot;full\&quot; is also available under the name \&quot;4k\&quot; and the value \&quot;preview\&quot; is aliased as \&quot;small\&quot; and \&quot;regular\&quot;.  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Foreground type: \&quot;auto\&quot; &#x3D; Automatically detect kind of foreground, \&quot;person\&quot; &#x3D; Use person(s) as foreground, \&quot;product\&quot; &#x3D; Use product(s) as foreground. \&quot;car\&quot; &#x3D; Use car as foreground,  |  [optional] |
|**typeLevel** | [**TypeLevelEnum**](#TypeLevelEnum) | Classification level of the detected foreground type: \&quot;none\&quot; &#x3D; No classification (X-Type Header won&#39;t bet set on the response) \&quot;1\&quot; &#x3D; Use coarse classification classes: [person, product, animal, car, other] \&quot;2\&quot; &#x3D; Use more specific classification classes: [person, product, animal, car, car_interior, car_part, transportation, graphics, other] \&quot;latest\&quot; &#x3D; Always use the latest classification classes available  |  [optional] |



## Enum: ChannelsEnum

| Name | Value |
|---- | -----|
| RGBA | &quot;rgba&quot; |
| ALPHA | &quot;alpha&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| PNG | &quot;png&quot; |
| JPG | &quot;jpg&quot; |
| ZIP | &quot;zip&quot; |



## Enum: SizeEnum

| Name | Value |
|---- | -----|
| PREVIEW | &quot;preview&quot; |
| FULL | &quot;full&quot; |
| AUTO | &quot;auto&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| PERSON | &quot;person&quot; |
| PRODUCT | &quot;product&quot; |
| CAR | &quot;car&quot; |



## Enum: TypeLevelEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| _1 | &quot;1&quot; |
| _2 | &quot;2&quot; |
| LATEST | &quot;latest&quot; |



