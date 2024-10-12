

# ReplaceAllShapesWithImageRequest

Replaces all shapes that match the given criteria with the provided image. The images replacing the shapes are rectangular after being inserted into the presentation and do not take on the forms of the shapes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containsText** | [**SubstringMatchCriteria**](SubstringMatchCriteria.md) |  |  [optional] |
|**imageReplaceMethod** | [**ImageReplaceMethodEnum**](#ImageReplaceMethodEnum) | The image replace method. If you specify both a &#x60;replace_method&#x60; and an &#x60;image_replace_method&#x60;, the &#x60;image_replace_method&#x60; takes precedence. If you do not specify a value for &#x60;image_replace_method&#x60;, but specify a value for &#x60;replace_method&#x60;, then the specified &#x60;replace_method&#x60; value is used. If you do not specify either, then CENTER_INSIDE is used. |  [optional] |
|**imageUrl** | **String** | The image URL. The image is fetched once at insertion time and a copy is stored for display inside the presentation. Images must be less than 50MB in size, cannot exceed 25 megapixels, and must be in one of PNG, JPEG, or GIF format. The provided URL can be at most 2 kB in length. The URL itself is saved with the image, and exposed via the Image.source_url field. |  [optional] |
|**pageObjectIds** | **List&lt;String&gt;** | If non-empty, limits the matches to page elements only on the given pages. Returns a 400 bad request error if given the page object ID of a notes page or a notes master, or if a page with that object ID doesn&#39;t exist in the presentation. |  [optional] |
|**replaceMethod** | [**ReplaceMethodEnum**](#ReplaceMethodEnum) | The replace method. *Deprecated*: use &#x60;image_replace_method&#x60; instead. If you specify both a &#x60;replace_method&#x60; and an &#x60;image_replace_method&#x60;, the &#x60;image_replace_method&#x60; takes precedence. |  [optional] |



## Enum: ImageReplaceMethodEnum

| Name | Value |
|---- | -----|
| IMAGE_REPLACE_METHOD_UNSPECIFIED | &quot;IMAGE_REPLACE_METHOD_UNSPECIFIED&quot; |
| CENTER_INSIDE | &quot;CENTER_INSIDE&quot; |
| CENTER_CROP | &quot;CENTER_CROP&quot; |



## Enum: ReplaceMethodEnum

| Name | Value |
|---- | -----|
| INSIDE | &quot;CENTER_INSIDE&quot; |
| CROP | &quot;CENTER_CROP&quot; |



