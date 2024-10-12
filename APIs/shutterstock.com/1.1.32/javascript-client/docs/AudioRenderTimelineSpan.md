# ShutterstockApiExplorer.AudioRenderTimelineSpan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Number** | An identifier which must be unique within the parent span | [optional] 
**instrumentGroups** | [**[AudioRenderTimelineSpanInstrumentGroup]**](AudioRenderTimelineSpanInstrumentGroup.md) | An array of instrument_group objects that are used in this span | [optional] 
**regions** | [**[AudioRenderTimelineSpanRegion]**](AudioRenderTimelineSpanRegion.md) | An array of region objects within the span | [optional] 
**spanType** | **String** | Type of span; metered spans represent a pariod of time with music, and unmetered spans denote the end of the prior metered span | 
**tempo** | **Number** | The tempo, in beats per minute, at the start of the span; if not provided, the API selects a random tempo | [optional] 
**tempoChanges** | [**[AudioRenderTimelineSpanTempoChanges]**](AudioRenderTimelineSpanTempoChanges.md) | Two or more inflection points in a tempo curve; the API creates a smoothly changing tempo by using a linear interpolation of the time between each tempo change | [optional] 
**time** | **Number** | The absolute time, in seconds, at which the span starts | 



## Enum: SpanTypeEnum


* `metered` (value: `"metered"`)

* `unmetered` (value: `"unmetered"`)




