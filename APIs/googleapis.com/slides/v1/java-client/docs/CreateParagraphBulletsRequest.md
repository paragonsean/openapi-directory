

# CreateParagraphBulletsRequest

Creates bullets for all of the paragraphs that overlap with the given text index range. The nesting level of each paragraph will be determined by counting leading tabs in front of each paragraph. To avoid excess space between the bullet and the corresponding paragraph, these leading tabs are removed by this request. This may change the indices of parts of the text. If the paragraph immediately before paragraphs being updated is in a list with a matching preset, the paragraphs being updated are added to that preceding list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bulletPreset** | [**BulletPresetEnum**](#BulletPresetEnum) | The kinds of bullet glyphs to be used. Defaults to the &#x60;BULLET_DISC_CIRCLE_SQUARE&#x60; preset. |  [optional] |
|**cellLocation** | [**TableCellLocation**](TableCellLocation.md) |  |  [optional] |
|**objectId** | **String** | The object ID of the shape or table containing the text to add bullets to. |  [optional] |
|**textRange** | [**Range**](Range.md) |  |  [optional] |



## Enum: BulletPresetEnum

| Name | Value |
|---- | -----|
| BULLET_DISC_CIRCLE_SQUARE | &quot;BULLET_DISC_CIRCLE_SQUARE&quot; |
| BULLET_DIAMONDX_ARROW3_D_SQUARE | &quot;BULLET_DIAMONDX_ARROW3D_SQUARE&quot; |
| BULLET_CHECKBOX | &quot;BULLET_CHECKBOX&quot; |
| BULLET_ARROW_DIAMOND_DISC | &quot;BULLET_ARROW_DIAMOND_DISC&quot; |
| BULLET_STAR_CIRCLE_SQUARE | &quot;BULLET_STAR_CIRCLE_SQUARE&quot; |
| BULLET_ARROW3_D_CIRCLE_SQUARE | &quot;BULLET_ARROW3D_CIRCLE_SQUARE&quot; |
| BULLET_LEFTTRIANGLE_DIAMOND_DISC | &quot;BULLET_LEFTTRIANGLE_DIAMOND_DISC&quot; |
| BULLET_DIAMONDX_HOLLOWDIAMOND_SQUARE | &quot;BULLET_DIAMONDX_HOLLOWDIAMOND_SQUARE&quot; |
| BULLET_DIAMOND_CIRCLE_SQUARE | &quot;BULLET_DIAMOND_CIRCLE_SQUARE&quot; |
| NUMBERED_DIGIT_ALPHA_ROMAN | &quot;NUMBERED_DIGIT_ALPHA_ROMAN&quot; |
| NUMBERED_DIGIT_ALPHA_ROMAN_PARENS | &quot;NUMBERED_DIGIT_ALPHA_ROMAN_PARENS&quot; |
| NUMBERED_DIGIT_NESTED | &quot;NUMBERED_DIGIT_NESTED&quot; |
| NUMBERED_UPPERALPHA_ALPHA_ROMAN | &quot;NUMBERED_UPPERALPHA_ALPHA_ROMAN&quot; |
| NUMBERED_UPPERROMAN_UPPERALPHA_DIGIT | &quot;NUMBERED_UPPERROMAN_UPPERALPHA_DIGIT&quot; |
| NUMBERED_ZERODIGIT_ALPHA_ROMAN | &quot;NUMBERED_ZERODIGIT_ALPHA_ROMAN&quot; |



