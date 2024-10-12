

# CreateParagraphBulletsRequest

Creates bullets for all of the paragraphs that overlap with the given range. The nesting level of each paragraph will be determined by counting leading tabs in front of each paragraph. To avoid excess space between the bullet and the corresponding paragraph, these leading tabs are removed by this request. This may change the indices of parts of the text. If the paragraph immediately before paragraphs being updated is in a list with a matching preset, the paragraphs being updated are added to that preceding list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bulletPreset** | [**BulletPresetEnum**](#BulletPresetEnum) | The kinds of bullet glyphs to be used. |  [optional] |
|**range** | [**Range**](Range.md) |  |  [optional] |



## Enum: BulletPresetEnum

| Name | Value |
|---- | -----|
| BULLET_GLYPH_PRESET_UNSPECIFIED | &quot;BULLET_GLYPH_PRESET_UNSPECIFIED&quot; |
| BULLET_DISC_CIRCLE_SQUARE | &quot;BULLET_DISC_CIRCLE_SQUARE&quot; |
| BULLET_DIAMONDX_ARROW3_D_SQUARE | &quot;BULLET_DIAMONDX_ARROW3D_SQUARE&quot; |
| BULLET_CHECKBOX | &quot;BULLET_CHECKBOX&quot; |
| BULLET_ARROW_DIAMOND_DISC | &quot;BULLET_ARROW_DIAMOND_DISC&quot; |
| BULLET_STAR_CIRCLE_SQUARE | &quot;BULLET_STAR_CIRCLE_SQUARE&quot; |
| BULLET_ARROW3_D_CIRCLE_SQUARE | &quot;BULLET_ARROW3D_CIRCLE_SQUARE&quot; |
| BULLET_LEFTTRIANGLE_DIAMOND_DISC | &quot;BULLET_LEFTTRIANGLE_DIAMOND_DISC&quot; |
| BULLET_DIAMONDX_HOLLOWDIAMOND_SQUARE | &quot;BULLET_DIAMONDX_HOLLOWDIAMOND_SQUARE&quot; |
| BULLET_DIAMOND_CIRCLE_SQUARE | &quot;BULLET_DIAMOND_CIRCLE_SQUARE&quot; |
| NUMBERED_DECIMAL_ALPHA_ROMAN | &quot;NUMBERED_DECIMAL_ALPHA_ROMAN&quot; |
| NUMBERED_DECIMAL_ALPHA_ROMAN_PARENS | &quot;NUMBERED_DECIMAL_ALPHA_ROMAN_PARENS&quot; |
| NUMBERED_DECIMAL_NESTED | &quot;NUMBERED_DECIMAL_NESTED&quot; |
| NUMBERED_UPPERALPHA_ALPHA_ROMAN | &quot;NUMBERED_UPPERALPHA_ALPHA_ROMAN&quot; |
| NUMBERED_UPPERROMAN_UPPERALPHA_DECIMAL | &quot;NUMBERED_UPPERROMAN_UPPERALPHA_DECIMAL&quot; |
| NUMBERED_ZERODECIMAL_ALPHA_ROMAN | &quot;NUMBERED_ZERODECIMAL_ALPHA_ROMAN&quot; |



