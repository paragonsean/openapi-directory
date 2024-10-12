

# VideoTargeting

Represents targeting information about video.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**excludedPositionTypes** | [**List&lt;ExcludedPositionTypesEnum&gt;**](#List&lt;ExcludedPositionTypesEnum&gt;) | A list of video positions to be excluded. Position types can either be included or excluded (XOR). |  [optional] |
|**targetedPositionTypes** | [**List&lt;TargetedPositionTypesEnum&gt;**](#List&lt;TargetedPositionTypesEnum&gt;) | A list of video positions to be included. When the included list is present, the excluded list must be empty. When the excluded list is present, the included list must be empty. |  [optional] |



## Enum: List&lt;ExcludedPositionTypesEnum&gt;

| Name | Value |
|---- | -----|
| POSITION_TYPE_UNSPECIFIED | &quot;POSITION_TYPE_UNSPECIFIED&quot; |
| PREROLL | &quot;PREROLL&quot; |
| MIDROLL | &quot;MIDROLL&quot; |
| POSTROLL | &quot;POSTROLL&quot; |



## Enum: List&lt;TargetedPositionTypesEnum&gt;

| Name | Value |
|---- | -----|
| POSITION_TYPE_UNSPECIFIED | &quot;POSITION_TYPE_UNSPECIFIED&quot; |
| PREROLL | &quot;PREROLL&quot; |
| MIDROLL | &quot;MIDROLL&quot; |
| POSTROLL | &quot;POSTROLL&quot; |



