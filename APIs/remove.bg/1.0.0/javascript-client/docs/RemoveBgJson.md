# BackgroundRemovalApi.RemoveBgJson

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addShadow** | **Boolean** | Whether to add an artificial shadow to the result (default: false). NOTE: Adding shadows is currently only supported for car photos. Other subjects are returned without shadow, even if set to true (this might change in the future).  | [optional] [default to false]
**bgColor** | **String** | Adds a solid color background. Can be a hex color code (e.g. 81d4fa, fff) or a color name (e.g. green). For semi-transparency, 4-/8-digit hex codes are also supported (e.g. 81d4fa77). (If this parameter is present, the other bg_ parameters must be empty.)  | [optional] 
**bgImageUrl** | **String** | Adds a background image from a URL. The image is centered and resized to fill the canvas while preserving the aspect ratio, unless it already has the exact same dimensions as the foreground image. (If this parameter is present, the other bg_ parameters must be empty.) | [optional] 
**channels** | **String** | Request either the finalized image (\&quot;rgba\&quot;, default) or an alpha mask (\&quot;alpha\&quot;). Note: Since remove.bg also applies RGB color corrections on edges, using only the alpha mask often leads to a lower final image quality. Therefore \&quot;rgba\&quot; is recommended.  | [optional] [default to &#39;rgba&#39;]
**crop** | **Boolean** | Whether to crop off all empty regions (default: false). Note that cropping has no effect on the amount of charged credits.  | [optional] [default to false]
**cropMargin** | **String** | Adds a margin around the cropped subject (default: 0). Can be an absolute value (e.g. \&quot;30px\&quot;) or relative to the subject size (e.g. \&quot;10%\&quot;). Can be a single value (all sides), two values (top/bottom and left/right) or four values (top, right, bottom, left). This parameter only has an effect when \&quot;crop&#x3D;true\&quot;. The maximum margin that can be added on each side is 50% of the subject dimensions or 500 pixels.  | [optional] [default to &#39;0&#39;]
**format** | **String** | Result image format: \&quot;auto\&quot; &#x3D; Use PNG format if transparent regions exist, otherwise use JPG format (default), \&quot;png\&quot; &#x3D; PNG format with alpha transparency, \&quot;jpg\&quot; &#x3D; JPG format, no transparency, \&quot;zip\&quot; &#x3D; ZIP format, contains color image and alpha matte image, supports transparency (recommended).  | [optional] [default to &#39;auto&#39;]
**imageFileB64** | **String** | Source image file (base64-encoded string). (If this parameter is present, the other image source parameters must be empty.) | [optional] 
**imageUrl** | **String** | Source image URL. (If this parameter is present, the other image source parameters must be empty.) | [optional] 
**position** | **String** | Positions the subject within the image canvas. Can be \&quot;original\&quot; (default unless \&quot;scale\&quot; is given), \&quot;center\&quot; (default when \&quot;scale\&quot; is given) or a value from \&quot;0%\&quot; to \&quot;100%\&quot; (both horizontal and vertical) or two values (horizontal, vertical).  | [optional] [default to &#39;original&#39;]
**roi** | **String** | Region of interest: Only contents of this rectangular region can be detected as foreground. Everything outside is considered background and will be removed. The rectangle is defined as two x/y coordinates in the format \&quot;x1 y1 x2 y2\&quot;. The coordinates can be in absolute pixels (suffix &#39;px&#39;) or relative to the width/height of the image (suffix &#39;%&#39;). By default, the whole image is the region of interest (\&quot;0% 0% 100% 100%\&quot;).  | [optional] [default to &#39;0% 0% 100% 100%&#39;]
**scale** | **String** | Scales the subject relative to the total image size. Can be any value from \&quot;10%\&quot; to \&quot;100%\&quot;, or \&quot;original\&quot; (default). Scaling the subject implies \&quot;position&#x3D;center\&quot; (unless specified otherwise).  | [optional] [default to &#39;original&#39;]
**semitransparency** | **Boolean** | Whether to have semi-transparent regions in the result (default: true). NOTE: Semitransparency is currently only supported for car windows (this might change in the future). Other objects are returned without semitransparency, even if set to true.  | [optional] [default to true]
**size** | **String** | Maximum output image resolution: \&quot;preview\&quot; (default) &#x3D; Resize image to 0.25 megapixels (e.g. 625×400 pixels) – 0.25 credits per image, \&quot;full\&quot; &#x3D; Use original image resolution, up to 25 megapixels (e.g. 6250x4000) with formats ZIP or JPG, or up to 10 megapixels (e.g. 4000x2500) with PNG – 1 credit per image), \&quot;auto\&quot; &#x3D; Use highest available resolution (based on image size and available credits).  For backwards-compatibility this parameter also accepts the values \&quot;medium\&quot; (up to 1.5 megapixels) and \&quot;hd\&quot; (up to 4 megapixels) for 1 credit per image. The value \&quot;full\&quot; is also available under the name \&quot;4k\&quot; and the value \&quot;preview\&quot; is aliased as \&quot;small\&quot; and \&quot;regular\&quot;.  | [optional] [default to &#39;preview&#39;]
**type** | **String** | Foreground type: \&quot;auto\&quot; &#x3D; Automatically detect kind of foreground, \&quot;person\&quot; &#x3D; Use person(s) as foreground, \&quot;product\&quot; &#x3D; Use product(s) as foreground. \&quot;car\&quot; &#x3D; Use car as foreground,  | [optional] [default to &#39;auto&#39;]
**typeLevel** | **String** | Classification level of the detected foreground type: \&quot;none\&quot; &#x3D; No classification (X-Type Header won&#39;t bet set on the response) \&quot;1\&quot; &#x3D; Use coarse classification classes: [person, product, animal, car, other] \&quot;2\&quot; &#x3D; Use more specific classification classes: [person, product, animal, car, car_interior, car_part, transportation, graphics, other] \&quot;latest\&quot; &#x3D; Always use the latest classification classes available  | [optional] [default to &#39;1&#39;]



## Enum: ChannelsEnum


* `rgba` (value: `"rgba"`)

* `alpha` (value: `"alpha"`)





## Enum: FormatEnum


* `auto` (value: `"auto"`)

* `png` (value: `"png"`)

* `jpg` (value: `"jpg"`)

* `zip` (value: `"zip"`)





## Enum: SizeEnum


* `preview` (value: `"preview"`)

* `full` (value: `"full"`)

* `auto` (value: `"auto"`)





## Enum: TypeEnum


* `auto` (value: `"auto"`)

* `person` (value: `"person"`)

* `product` (value: `"product"`)

* `car` (value: `"car"`)





## Enum: TypeLevelEnum


* `none` (value: `"none"`)

* `1` (value: `"1"`)

* `2` (value: `"2"`)

* `latest` (value: `"latest"`)




