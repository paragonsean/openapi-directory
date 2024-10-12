# Json2VideoApi.Movie

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache** | **Boolean** |  | [optional] [default to true]
**comment** | **String** | Used for adding your comments | [optional] 
**draft** | **Boolean** | Draft movies include a watermark. Check your plan how many draft and final movies you have | [optional] [default to true]
**elements** | [**[MovieElementsInner]**](MovieElementsInner.md) |  | [optional] 
**exports** | **[Object]** | You can define different types of exports for your movie. Check the &lt;a href&#x3D;\&quot;https://json2video.com/docs/tutorial/exports\&quot;&gt;documentation&lt;/a&gt; for more information | [optional] 
**fps** | **Number** | Frames per second | [optional] [default to 25]
**height** | **Number** |  | [optional] [default to 360]
**quality** | **String** |  | [optional] [default to &#39;high&#39;]
**resolution** | **String** |  | [optional] 
**scenes** | [**[Scene]**](Scene.md) |  | 
**settings** | **Object** | Movie advanced settings | [optional] 
**width** | **Number** |  | [optional] [default to 640]



## Enum: QualityEnum


* `low` (value: `"low"`)

* `medium` (value: `"medium"`)

* `high` (value: `"high"`)





## Enum: ResolutionEnum


* `sd` (value: `"sd"`)

* `hd` (value: `"hd"`)

* `full-hd` (value: `"full-hd"`)

* `squared` (value: `"squared"`)

* `instagram-story` (value: `"instagram-story"`)

* `instagram-feed` (value: `"instagram-feed"`)

* `twitter-landscape` (value: `"twitter-landscape"`)

* `twitter-portrait` (value: `"twitter-portrait"`)




