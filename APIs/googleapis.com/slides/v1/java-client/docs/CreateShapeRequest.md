

# CreateShapeRequest

Creates a new shape.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**elementProperties** | [**PageElementProperties**](PageElementProperties.md) |  |  [optional] |
|**objectId** | **String** | A user-supplied object ID. If you specify an ID, it must be unique among all pages and page elements in the presentation. The ID must start with an alphanumeric character or an underscore (matches regex &#x60;[a-zA-Z0-9_]&#x60;); remaining characters may include those as well as a hyphen or colon (matches regex &#x60;[a-zA-Z0-9_-:]&#x60;). The length of the ID must not be less than 5 or greater than 50. If empty, a unique identifier will be generated. |  [optional] |
|**shapeType** | [**ShapeTypeEnum**](#ShapeTypeEnum) | The shape type. |  [optional] |



## Enum: ShapeTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| TEXT_BOX | &quot;TEXT_BOX&quot; |
| RECTANGLE | &quot;RECTANGLE&quot; |
| ROUND_RECTANGLE | &quot;ROUND_RECTANGLE&quot; |
| ELLIPSE | &quot;ELLIPSE&quot; |
| ARC | &quot;ARC&quot; |
| BENT_ARROW | &quot;BENT_ARROW&quot; |
| BENT_UP_ARROW | &quot;BENT_UP_ARROW&quot; |
| BEVEL | &quot;BEVEL&quot; |
| BLOCK_ARC | &quot;BLOCK_ARC&quot; |
| BRACE_PAIR | &quot;BRACE_PAIR&quot; |
| BRACKET_PAIR | &quot;BRACKET_PAIR&quot; |
| CAN | &quot;CAN&quot; |
| CHEVRON | &quot;CHEVRON&quot; |
| CHORD | &quot;CHORD&quot; |
| CLOUD | &quot;CLOUD&quot; |
| CORNER | &quot;CORNER&quot; |
| CUBE | &quot;CUBE&quot; |
| CURVED_DOWN_ARROW | &quot;CURVED_DOWN_ARROW&quot; |
| CURVED_LEFT_ARROW | &quot;CURVED_LEFT_ARROW&quot; |
| CURVED_RIGHT_ARROW | &quot;CURVED_RIGHT_ARROW&quot; |
| CURVED_UP_ARROW | &quot;CURVED_UP_ARROW&quot; |
| DECAGON | &quot;DECAGON&quot; |
| DIAGONAL_STRIPE | &quot;DIAGONAL_STRIPE&quot; |
| DIAMOND | &quot;DIAMOND&quot; |
| DODECAGON | &quot;DODECAGON&quot; |
| DONUT | &quot;DONUT&quot; |
| DOUBLE_WAVE | &quot;DOUBLE_WAVE&quot; |
| DOWN_ARROW | &quot;DOWN_ARROW&quot; |
| DOWN_ARROW_CALLOUT | &quot;DOWN_ARROW_CALLOUT&quot; |
| FOLDED_CORNER | &quot;FOLDED_CORNER&quot; |
| FRAME | &quot;FRAME&quot; |
| HALF_FRAME | &quot;HALF_FRAME&quot; |
| HEART | &quot;HEART&quot; |
| HEPTAGON | &quot;HEPTAGON&quot; |
| HEXAGON | &quot;HEXAGON&quot; |
| HOME_PLATE | &quot;HOME_PLATE&quot; |
| HORIZONTAL_SCROLL | &quot;HORIZONTAL_SCROLL&quot; |
| IRREGULAR_SEAL_1 | &quot;IRREGULAR_SEAL_1&quot; |
| IRREGULAR_SEAL_2 | &quot;IRREGULAR_SEAL_2&quot; |
| LEFT_ARROW | &quot;LEFT_ARROW&quot; |
| LEFT_ARROW_CALLOUT | &quot;LEFT_ARROW_CALLOUT&quot; |
| LEFT_BRACE | &quot;LEFT_BRACE&quot; |
| LEFT_BRACKET | &quot;LEFT_BRACKET&quot; |
| LEFT_RIGHT_ARROW | &quot;LEFT_RIGHT_ARROW&quot; |
| LEFT_RIGHT_ARROW_CALLOUT | &quot;LEFT_RIGHT_ARROW_CALLOUT&quot; |
| LEFT_RIGHT_UP_ARROW | &quot;LEFT_RIGHT_UP_ARROW&quot; |
| LEFT_UP_ARROW | &quot;LEFT_UP_ARROW&quot; |
| LIGHTNING_BOLT | &quot;LIGHTNING_BOLT&quot; |
| MATH_DIVIDE | &quot;MATH_DIVIDE&quot; |
| MATH_EQUAL | &quot;MATH_EQUAL&quot; |
| MATH_MINUS | &quot;MATH_MINUS&quot; |
| MATH_MULTIPLY | &quot;MATH_MULTIPLY&quot; |
| MATH_NOT_EQUAL | &quot;MATH_NOT_EQUAL&quot; |
| MATH_PLUS | &quot;MATH_PLUS&quot; |
| MOON | &quot;MOON&quot; |
| NO_SMOKING | &quot;NO_SMOKING&quot; |
| NOTCHED_RIGHT_ARROW | &quot;NOTCHED_RIGHT_ARROW&quot; |
| OCTAGON | &quot;OCTAGON&quot; |
| PARALLELOGRAM | &quot;PARALLELOGRAM&quot; |
| PENTAGON | &quot;PENTAGON&quot; |
| PIE | &quot;PIE&quot; |
| PLAQUE | &quot;PLAQUE&quot; |
| PLUS | &quot;PLUS&quot; |
| QUAD_ARROW | &quot;QUAD_ARROW&quot; |
| QUAD_ARROW_CALLOUT | &quot;QUAD_ARROW_CALLOUT&quot; |
| RIBBON | &quot;RIBBON&quot; |
| RIBBON_2 | &quot;RIBBON_2&quot; |
| RIGHT_ARROW | &quot;RIGHT_ARROW&quot; |
| RIGHT_ARROW_CALLOUT | &quot;RIGHT_ARROW_CALLOUT&quot; |
| RIGHT_BRACE | &quot;RIGHT_BRACE&quot; |
| RIGHT_BRACKET | &quot;RIGHT_BRACKET&quot; |
| ROUND_1_RECTANGLE | &quot;ROUND_1_RECTANGLE&quot; |
| ROUND_2_DIAGONAL_RECTANGLE | &quot;ROUND_2_DIAGONAL_RECTANGLE&quot; |
| ROUND_2_SAME_RECTANGLE | &quot;ROUND_2_SAME_RECTANGLE&quot; |
| RIGHT_TRIANGLE | &quot;RIGHT_TRIANGLE&quot; |
| SMILEY_FACE | &quot;SMILEY_FACE&quot; |
| SNIP_1_RECTANGLE | &quot;SNIP_1_RECTANGLE&quot; |
| SNIP_2_DIAGONAL_RECTANGLE | &quot;SNIP_2_DIAGONAL_RECTANGLE&quot; |
| SNIP_2_SAME_RECTANGLE | &quot;SNIP_2_SAME_RECTANGLE&quot; |
| SNIP_ROUND_RECTANGLE | &quot;SNIP_ROUND_RECTANGLE&quot; |
| STAR_10 | &quot;STAR_10&quot; |
| STAR_12 | &quot;STAR_12&quot; |
| STAR_16 | &quot;STAR_16&quot; |
| STAR_24 | &quot;STAR_24&quot; |
| STAR_32 | &quot;STAR_32&quot; |
| STAR_4 | &quot;STAR_4&quot; |
| STAR_5 | &quot;STAR_5&quot; |
| STAR_6 | &quot;STAR_6&quot; |
| STAR_7 | &quot;STAR_7&quot; |
| STAR_8 | &quot;STAR_8&quot; |
| STRIPED_RIGHT_ARROW | &quot;STRIPED_RIGHT_ARROW&quot; |
| SUN | &quot;SUN&quot; |
| TRAPEZOID | &quot;TRAPEZOID&quot; |
| TRIANGLE | &quot;TRIANGLE&quot; |
| UP_ARROW | &quot;UP_ARROW&quot; |
| UP_ARROW_CALLOUT | &quot;UP_ARROW_CALLOUT&quot; |
| UP_DOWN_ARROW | &quot;UP_DOWN_ARROW&quot; |
| UTURN_ARROW | &quot;UTURN_ARROW&quot; |
| VERTICAL_SCROLL | &quot;VERTICAL_SCROLL&quot; |
| WAVE | &quot;WAVE&quot; |
| WEDGE_ELLIPSE_CALLOUT | &quot;WEDGE_ELLIPSE_CALLOUT&quot; |
| WEDGE_RECTANGLE_CALLOUT | &quot;WEDGE_RECTANGLE_CALLOUT&quot; |
| WEDGE_ROUND_RECTANGLE_CALLOUT | &quot;WEDGE_ROUND_RECTANGLE_CALLOUT&quot; |
| FLOW_CHART_ALTERNATE_PROCESS | &quot;FLOW_CHART_ALTERNATE_PROCESS&quot; |
| FLOW_CHART_COLLATE | &quot;FLOW_CHART_COLLATE&quot; |
| FLOW_CHART_CONNECTOR | &quot;FLOW_CHART_CONNECTOR&quot; |
| FLOW_CHART_DECISION | &quot;FLOW_CHART_DECISION&quot; |
| FLOW_CHART_DELAY | &quot;FLOW_CHART_DELAY&quot; |
| FLOW_CHART_DISPLAY | &quot;FLOW_CHART_DISPLAY&quot; |
| FLOW_CHART_DOCUMENT | &quot;FLOW_CHART_DOCUMENT&quot; |
| FLOW_CHART_EXTRACT | &quot;FLOW_CHART_EXTRACT&quot; |
| FLOW_CHART_INPUT_OUTPUT | &quot;FLOW_CHART_INPUT_OUTPUT&quot; |
| FLOW_CHART_INTERNAL_STORAGE | &quot;FLOW_CHART_INTERNAL_STORAGE&quot; |
| FLOW_CHART_MAGNETIC_DISK | &quot;FLOW_CHART_MAGNETIC_DISK&quot; |
| FLOW_CHART_MAGNETIC_DRUM | &quot;FLOW_CHART_MAGNETIC_DRUM&quot; |
| FLOW_CHART_MAGNETIC_TAPE | &quot;FLOW_CHART_MAGNETIC_TAPE&quot; |
| FLOW_CHART_MANUAL_INPUT | &quot;FLOW_CHART_MANUAL_INPUT&quot; |
| FLOW_CHART_MANUAL_OPERATION | &quot;FLOW_CHART_MANUAL_OPERATION&quot; |
| FLOW_CHART_MERGE | &quot;FLOW_CHART_MERGE&quot; |
| FLOW_CHART_MULTIDOCUMENT | &quot;FLOW_CHART_MULTIDOCUMENT&quot; |
| FLOW_CHART_OFFLINE_STORAGE | &quot;FLOW_CHART_OFFLINE_STORAGE&quot; |
| FLOW_CHART_OFFPAGE_CONNECTOR | &quot;FLOW_CHART_OFFPAGE_CONNECTOR&quot; |
| FLOW_CHART_ONLINE_STORAGE | &quot;FLOW_CHART_ONLINE_STORAGE&quot; |
| FLOW_CHART_OR | &quot;FLOW_CHART_OR&quot; |
| FLOW_CHART_PREDEFINED_PROCESS | &quot;FLOW_CHART_PREDEFINED_PROCESS&quot; |
| FLOW_CHART_PREPARATION | &quot;FLOW_CHART_PREPARATION&quot; |
| FLOW_CHART_PROCESS | &quot;FLOW_CHART_PROCESS&quot; |
| FLOW_CHART_PUNCHED_CARD | &quot;FLOW_CHART_PUNCHED_CARD&quot; |
| FLOW_CHART_PUNCHED_TAPE | &quot;FLOW_CHART_PUNCHED_TAPE&quot; |
| FLOW_CHART_SORT | &quot;FLOW_CHART_SORT&quot; |
| FLOW_CHART_SUMMING_JUNCTION | &quot;FLOW_CHART_SUMMING_JUNCTION&quot; |
| FLOW_CHART_TERMINATOR | &quot;FLOW_CHART_TERMINATOR&quot; |
| ARROW_EAST | &quot;ARROW_EAST&quot; |
| ARROW_NORTH_EAST | &quot;ARROW_NORTH_EAST&quot; |
| ARROW_NORTH | &quot;ARROW_NORTH&quot; |
| SPEECH | &quot;SPEECH&quot; |
| STARBURST | &quot;STARBURST&quot; |
| TEARDROP | &quot;TEARDROP&quot; |
| ELLIPSE_RIBBON | &quot;ELLIPSE_RIBBON&quot; |
| ELLIPSE_RIBBON_2 | &quot;ELLIPSE_RIBBON_2&quot; |
| CLOUD_CALLOUT | &quot;CLOUD_CALLOUT&quot; |
| CUSTOM | &quot;CUSTOM&quot; |



