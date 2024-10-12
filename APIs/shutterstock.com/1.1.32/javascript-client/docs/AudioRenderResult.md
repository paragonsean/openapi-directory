# ShutterstockApiExplorer.AudioRenderResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdDate** | **Date** | The time the render was submitted to the API | [optional] 
**files** | [**[AudioRendersFilesList]**](AudioRendersFilesList.md) | The files associated with the render | [optional] 
**id** | **String** | The alphanumeric ID of the simple render | 
**preset** | **String** | The file format preset | [optional] 
**progressPercent** | **Number** | The current progress of the render as a percentage | [optional] 
**status** | **String** | A coarse progress indicator | 
**timeline** | [**AudioRenderTimeline**](AudioRenderTimeline.md) |  | 
**updatedDate** | **Date** | The time that the audio output was uploaded | [optional] 



## Enum: PresetEnum


* `MASTER_MP3` (value: `"MASTER_MP3"`)

* `MASTER_WAV` (value: `"MASTER_WAV"`)

* `STEMS_WAV` (value: `"STEMS_WAV"`)





## Enum: StatusEnum


* `WAITING_COMPOSE` (value: `"WAITING_COMPOSE"`)

* `RUNNING_COMPOSE` (value: `"RUNNING_COMPOSE"`)

* `WAITING_RENDER` (value: `"WAITING_RENDER"`)

* `RUNNING_RENDER` (value: `"RUNNING_RENDER"`)

* `CREATED` (value: `"CREATED"`)

* `FAILED_CREATE` (value: `"FAILED_CREATE"`)




