# GoogleSlidesApi.CreateShapeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elementProperties** | [**PageElementProperties**](PageElementProperties.md) |  | [optional] 
**objectId** | **String** | A user-supplied object ID. If you specify an ID, it must be unique among all pages and page elements in the presentation. The ID must start with an alphanumeric character or an underscore (matches regex &#x60;[a-zA-Z0-9_]&#x60;); remaining characters may include those as well as a hyphen or colon (matches regex &#x60;[a-zA-Z0-9_-:]&#x60;). The length of the ID must not be less than 5 or greater than 50. If empty, a unique identifier will be generated. | [optional] 
**shapeType** | **String** | The shape type. | [optional] 



## Enum: ShapeTypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `TEXT_BOX` (value: `"TEXT_BOX"`)

* `RECTANGLE` (value: `"RECTANGLE"`)

* `ROUND_RECTANGLE` (value: `"ROUND_RECTANGLE"`)

* `ELLIPSE` (value: `"ELLIPSE"`)

* `ARC` (value: `"ARC"`)

* `BENT_ARROW` (value: `"BENT_ARROW"`)

* `BENT_UP_ARROW` (value: `"BENT_UP_ARROW"`)

* `BEVEL` (value: `"BEVEL"`)

* `BLOCK_ARC` (value: `"BLOCK_ARC"`)

* `BRACE_PAIR` (value: `"BRACE_PAIR"`)

* `BRACKET_PAIR` (value: `"BRACKET_PAIR"`)

* `CAN` (value: `"CAN"`)

* `CHEVRON` (value: `"CHEVRON"`)

* `CHORD` (value: `"CHORD"`)

* `CLOUD` (value: `"CLOUD"`)

* `CORNER` (value: `"CORNER"`)

* `CUBE` (value: `"CUBE"`)

* `CURVED_DOWN_ARROW` (value: `"CURVED_DOWN_ARROW"`)

* `CURVED_LEFT_ARROW` (value: `"CURVED_LEFT_ARROW"`)

* `CURVED_RIGHT_ARROW` (value: `"CURVED_RIGHT_ARROW"`)

* `CURVED_UP_ARROW` (value: `"CURVED_UP_ARROW"`)

* `DECAGON` (value: `"DECAGON"`)

* `DIAGONAL_STRIPE` (value: `"DIAGONAL_STRIPE"`)

* `DIAMOND` (value: `"DIAMOND"`)

* `DODECAGON` (value: `"DODECAGON"`)

* `DONUT` (value: `"DONUT"`)

* `DOUBLE_WAVE` (value: `"DOUBLE_WAVE"`)

* `DOWN_ARROW` (value: `"DOWN_ARROW"`)

* `DOWN_ARROW_CALLOUT` (value: `"DOWN_ARROW_CALLOUT"`)

* `FOLDED_CORNER` (value: `"FOLDED_CORNER"`)

* `FRAME` (value: `"FRAME"`)

* `HALF_FRAME` (value: `"HALF_FRAME"`)

* `HEART` (value: `"HEART"`)

* `HEPTAGON` (value: `"HEPTAGON"`)

* `HEXAGON` (value: `"HEXAGON"`)

* `HOME_PLATE` (value: `"HOME_PLATE"`)

* `HORIZONTAL_SCROLL` (value: `"HORIZONTAL_SCROLL"`)

* `IRREGULAR_SEAL_1` (value: `"IRREGULAR_SEAL_1"`)

* `IRREGULAR_SEAL_2` (value: `"IRREGULAR_SEAL_2"`)

* `LEFT_ARROW` (value: `"LEFT_ARROW"`)

* `LEFT_ARROW_CALLOUT` (value: `"LEFT_ARROW_CALLOUT"`)

* `LEFT_BRACE` (value: `"LEFT_BRACE"`)

* `LEFT_BRACKET` (value: `"LEFT_BRACKET"`)

* `LEFT_RIGHT_ARROW` (value: `"LEFT_RIGHT_ARROW"`)

* `LEFT_RIGHT_ARROW_CALLOUT` (value: `"LEFT_RIGHT_ARROW_CALLOUT"`)

* `LEFT_RIGHT_UP_ARROW` (value: `"LEFT_RIGHT_UP_ARROW"`)

* `LEFT_UP_ARROW` (value: `"LEFT_UP_ARROW"`)

* `LIGHTNING_BOLT` (value: `"LIGHTNING_BOLT"`)

* `MATH_DIVIDE` (value: `"MATH_DIVIDE"`)

* `MATH_EQUAL` (value: `"MATH_EQUAL"`)

* `MATH_MINUS` (value: `"MATH_MINUS"`)

* `MATH_MULTIPLY` (value: `"MATH_MULTIPLY"`)

* `MATH_NOT_EQUAL` (value: `"MATH_NOT_EQUAL"`)

* `MATH_PLUS` (value: `"MATH_PLUS"`)

* `MOON` (value: `"MOON"`)

* `NO_SMOKING` (value: `"NO_SMOKING"`)

* `NOTCHED_RIGHT_ARROW` (value: `"NOTCHED_RIGHT_ARROW"`)

* `OCTAGON` (value: `"OCTAGON"`)

* `PARALLELOGRAM` (value: `"PARALLELOGRAM"`)

* `PENTAGON` (value: `"PENTAGON"`)

* `PIE` (value: `"PIE"`)

* `PLAQUE` (value: `"PLAQUE"`)

* `PLUS` (value: `"PLUS"`)

* `QUAD_ARROW` (value: `"QUAD_ARROW"`)

* `QUAD_ARROW_CALLOUT` (value: `"QUAD_ARROW_CALLOUT"`)

* `RIBBON` (value: `"RIBBON"`)

* `RIBBON_2` (value: `"RIBBON_2"`)

* `RIGHT_ARROW` (value: `"RIGHT_ARROW"`)

* `RIGHT_ARROW_CALLOUT` (value: `"RIGHT_ARROW_CALLOUT"`)

* `RIGHT_BRACE` (value: `"RIGHT_BRACE"`)

* `RIGHT_BRACKET` (value: `"RIGHT_BRACKET"`)

* `ROUND_1_RECTANGLE` (value: `"ROUND_1_RECTANGLE"`)

* `ROUND_2_DIAGONAL_RECTANGLE` (value: `"ROUND_2_DIAGONAL_RECTANGLE"`)

* `ROUND_2_SAME_RECTANGLE` (value: `"ROUND_2_SAME_RECTANGLE"`)

* `RIGHT_TRIANGLE` (value: `"RIGHT_TRIANGLE"`)

* `SMILEY_FACE` (value: `"SMILEY_FACE"`)

* `SNIP_1_RECTANGLE` (value: `"SNIP_1_RECTANGLE"`)

* `SNIP_2_DIAGONAL_RECTANGLE` (value: `"SNIP_2_DIAGONAL_RECTANGLE"`)

* `SNIP_2_SAME_RECTANGLE` (value: `"SNIP_2_SAME_RECTANGLE"`)

* `SNIP_ROUND_RECTANGLE` (value: `"SNIP_ROUND_RECTANGLE"`)

* `STAR_10` (value: `"STAR_10"`)

* `STAR_12` (value: `"STAR_12"`)

* `STAR_16` (value: `"STAR_16"`)

* `STAR_24` (value: `"STAR_24"`)

* `STAR_32` (value: `"STAR_32"`)

* `STAR_4` (value: `"STAR_4"`)

* `STAR_5` (value: `"STAR_5"`)

* `STAR_6` (value: `"STAR_6"`)

* `STAR_7` (value: `"STAR_7"`)

* `STAR_8` (value: `"STAR_8"`)

* `STRIPED_RIGHT_ARROW` (value: `"STRIPED_RIGHT_ARROW"`)

* `SUN` (value: `"SUN"`)

* `TRAPEZOID` (value: `"TRAPEZOID"`)

* `TRIANGLE` (value: `"TRIANGLE"`)

* `UP_ARROW` (value: `"UP_ARROW"`)

* `UP_ARROW_CALLOUT` (value: `"UP_ARROW_CALLOUT"`)

* `UP_DOWN_ARROW` (value: `"UP_DOWN_ARROW"`)

* `UTURN_ARROW` (value: `"UTURN_ARROW"`)

* `VERTICAL_SCROLL` (value: `"VERTICAL_SCROLL"`)

* `WAVE` (value: `"WAVE"`)

* `WEDGE_ELLIPSE_CALLOUT` (value: `"WEDGE_ELLIPSE_CALLOUT"`)

* `WEDGE_RECTANGLE_CALLOUT` (value: `"WEDGE_RECTANGLE_CALLOUT"`)

* `WEDGE_ROUND_RECTANGLE_CALLOUT` (value: `"WEDGE_ROUND_RECTANGLE_CALLOUT"`)

* `FLOW_CHART_ALTERNATE_PROCESS` (value: `"FLOW_CHART_ALTERNATE_PROCESS"`)

* `FLOW_CHART_COLLATE` (value: `"FLOW_CHART_COLLATE"`)

* `FLOW_CHART_CONNECTOR` (value: `"FLOW_CHART_CONNECTOR"`)

* `FLOW_CHART_DECISION` (value: `"FLOW_CHART_DECISION"`)

* `FLOW_CHART_DELAY` (value: `"FLOW_CHART_DELAY"`)

* `FLOW_CHART_DISPLAY` (value: `"FLOW_CHART_DISPLAY"`)

* `FLOW_CHART_DOCUMENT` (value: `"FLOW_CHART_DOCUMENT"`)

* `FLOW_CHART_EXTRACT` (value: `"FLOW_CHART_EXTRACT"`)

* `FLOW_CHART_INPUT_OUTPUT` (value: `"FLOW_CHART_INPUT_OUTPUT"`)

* `FLOW_CHART_INTERNAL_STORAGE` (value: `"FLOW_CHART_INTERNAL_STORAGE"`)

* `FLOW_CHART_MAGNETIC_DISK` (value: `"FLOW_CHART_MAGNETIC_DISK"`)

* `FLOW_CHART_MAGNETIC_DRUM` (value: `"FLOW_CHART_MAGNETIC_DRUM"`)

* `FLOW_CHART_MAGNETIC_TAPE` (value: `"FLOW_CHART_MAGNETIC_TAPE"`)

* `FLOW_CHART_MANUAL_INPUT` (value: `"FLOW_CHART_MANUAL_INPUT"`)

* `FLOW_CHART_MANUAL_OPERATION` (value: `"FLOW_CHART_MANUAL_OPERATION"`)

* `FLOW_CHART_MERGE` (value: `"FLOW_CHART_MERGE"`)

* `FLOW_CHART_MULTIDOCUMENT` (value: `"FLOW_CHART_MULTIDOCUMENT"`)

* `FLOW_CHART_OFFLINE_STORAGE` (value: `"FLOW_CHART_OFFLINE_STORAGE"`)

* `FLOW_CHART_OFFPAGE_CONNECTOR` (value: `"FLOW_CHART_OFFPAGE_CONNECTOR"`)

* `FLOW_CHART_ONLINE_STORAGE` (value: `"FLOW_CHART_ONLINE_STORAGE"`)

* `FLOW_CHART_OR` (value: `"FLOW_CHART_OR"`)

* `FLOW_CHART_PREDEFINED_PROCESS` (value: `"FLOW_CHART_PREDEFINED_PROCESS"`)

* `FLOW_CHART_PREPARATION` (value: `"FLOW_CHART_PREPARATION"`)

* `FLOW_CHART_PROCESS` (value: `"FLOW_CHART_PROCESS"`)

* `FLOW_CHART_PUNCHED_CARD` (value: `"FLOW_CHART_PUNCHED_CARD"`)

* `FLOW_CHART_PUNCHED_TAPE` (value: `"FLOW_CHART_PUNCHED_TAPE"`)

* `FLOW_CHART_SORT` (value: `"FLOW_CHART_SORT"`)

* `FLOW_CHART_SUMMING_JUNCTION` (value: `"FLOW_CHART_SUMMING_JUNCTION"`)

* `FLOW_CHART_TERMINATOR` (value: `"FLOW_CHART_TERMINATOR"`)

* `ARROW_EAST` (value: `"ARROW_EAST"`)

* `ARROW_NORTH_EAST` (value: `"ARROW_NORTH_EAST"`)

* `ARROW_NORTH` (value: `"ARROW_NORTH"`)

* `SPEECH` (value: `"SPEECH"`)

* `STARBURST` (value: `"STARBURST"`)

* `TEARDROP` (value: `"TEARDROP"`)

* `ELLIPSE_RIBBON` (value: `"ELLIPSE_RIBBON"`)

* `ELLIPSE_RIBBON_2` (value: `"ELLIPSE_RIBBON_2"`)

* `CLOUD_CALLOUT` (value: `"CLOUD_CALLOUT"`)

* `CUSTOM` (value: `"CUSTOM"`)




