

# Movie

Object defining the movie to be rendered

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cache** | **Boolean** |  |  [optional] |
|**comment** | **String** | Used for adding your comments |  [optional] |
|**draft** | **Boolean** | Draft movies include a watermark. Check your plan how many draft and final movies you have |  [optional] |
|**elements** | [**List&lt;MovieElementsInner&gt;**](MovieElementsInner.md) |  |  [optional] |
|**exports** | **List&lt;Object&gt;** | You can define different types of exports for your movie. Check the &lt;a href&#x3D;\&quot;https://json2video.com/docs/tutorial/exports\&quot;&gt;documentation&lt;/a&gt; for more information |  [optional] |
|**fps** | **Integer** | Frames per second |  [optional] |
|**height** | **Integer** |  |  [optional] |
|**quality** | [**QualityEnum**](#QualityEnum) |  |  [optional] |
|**resolution** | [**ResolutionEnum**](#ResolutionEnum) |  |  [optional] |
|**scenes** | [**List&lt;Scene&gt;**](Scene.md) |  |  |
|**settings** | **Object** | Movie advanced settings |  [optional] |
|**width** | **Integer** |  |  [optional] |



## Enum: QualityEnum

| Name | Value |
|---- | -----|
| LOW | &quot;low&quot; |
| MEDIUM | &quot;medium&quot; |
| HIGH | &quot;high&quot; |



## Enum: ResolutionEnum

| Name | Value |
|---- | -----|
| SD | &quot;sd&quot; |
| HD | &quot;hd&quot; |
| FULL_HD | &quot;full-hd&quot; |
| SQUARED | &quot;squared&quot; |
| INSTAGRAM_STORY | &quot;instagram-story&quot; |
| INSTAGRAM_FEED | &quot;instagram-feed&quot; |
| TWITTER_LANDSCAPE | &quot;twitter-landscape&quot; |
| TWITTER_PORTRAIT | &quot;twitter-portrait&quot; |



