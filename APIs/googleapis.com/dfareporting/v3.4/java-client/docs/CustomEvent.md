

# CustomEvent

Experimental feature (no support provided) A custom event represents a third party impression, a third party click, an annotation on a first party impression, or an annotation on a first party click.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotateClickEvent** | [**CustomEventClickAnnotation**](CustomEventClickAnnotation.md) |  |  [optional] |
|**annotateImpressionEvent** | [**CustomEventImpressionAnnotation**](CustomEventImpressionAnnotation.md) |  |  [optional] |
|**customVariables** | [**List&lt;CustomVariable&gt;**](CustomVariable.md) | Custom variables associated with the event. |  [optional] |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | The type of event. If INSERT, the fields in insertEvent need to be populated. If ANNOTATE, the fields in either annotateClickEvent or annotateImpressionEvent need to be populated. |  [optional] |
|**floodlightConfigurationId** | **String** | Floodlight configuration ID of the advertiser the event is linked to. This is a required field. |  [optional] |
|**insertEvent** | [**CustomEventInsert**](CustomEventInsert.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#customEvent\&quot;. |  [optional] |
|**ordinal** | **String** | The ordinal of this custom event. This is a required field. |  [optional] |
|**timestampMicros** | **String** | The timestamp of this custom event, in Unix epoch micros. This is a required field. |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| INSERT | &quot;INSERT&quot; |
| ANNOTATE | &quot;ANNOTATE&quot; |



