# ShutterstockApiExplorer.AudioRenderTimelineSpanRegionEndType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beat** | **Number** | The beat, relative to the start of the active region, at which the end_type begins; in other words, the ending starts on this beat of the region | 
**event** | **String** | The type of event | 
**type** | **String** | The specific action to perform; if the event type is \&quot;ending\&quot; then this must be \&quot;ringout\&quot; and if event type is \&quot;transition\&quot; this must be \&quot;cut\&quot; | 



## Enum: EventEnum


* `ending` (value: `"ending"`)

* `transition` (value: `"transition"`)





## Enum: TypeEnum


* `ringout` (value: `"ringout"`)

* `cut` (value: `"cut"`)




