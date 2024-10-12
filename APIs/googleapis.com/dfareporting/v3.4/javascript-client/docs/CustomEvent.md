# CampaignManager360Api.CustomEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotateClickEvent** | [**CustomEventClickAnnotation**](CustomEventClickAnnotation.md) |  | [optional] 
**annotateImpressionEvent** | [**CustomEventImpressionAnnotation**](CustomEventImpressionAnnotation.md) |  | [optional] 
**customVariables** | [**[CustomVariable]**](CustomVariable.md) | Custom variables associated with the event. | [optional] 
**eventType** | **String** | The type of event. If INSERT, the fields in insertEvent need to be populated. If ANNOTATE, the fields in either annotateClickEvent or annotateImpressionEvent need to be populated. | [optional] 
**floodlightConfigurationId** | **String** | Floodlight configuration ID of the advertiser the event is linked to. This is a required field. | [optional] 
**insertEvent** | [**CustomEventInsert**](CustomEventInsert.md) |  | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#customEvent\&quot;. | [optional] 
**ordinal** | **String** | The ordinal of this custom event. This is a required field. | [optional] 
**timestampMicros** | **String** | The timestamp of this custom event, in Unix epoch micros. This is a required field. | [optional] 



## Enum: EventTypeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `INSERT` (value: `"INSERT"`)

* `ANNOTATE` (value: `"ANNOTATE"`)




