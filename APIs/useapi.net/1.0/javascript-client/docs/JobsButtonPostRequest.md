# MidjourneyRestApiByUseapiNet.JobsButtonPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button** | **String** | button from buttons array of job referenced via jobid | 
**discord** | **String** | Optional Discord token, if provided will override discord value of referenced jobid | [optional] 
**jobid** | **String** | jobid of successfully completed (status set to completed) jobs/imagine or jobs/button job | 
**maxJobs** | **Number** | Optional Maximum Concurrent Jobs for current Midjourney subscription | [optional] 
**replyRef** | **String** | Optional reference id which will be stored and returned along with this job response / result | [optional] 
**replyUrl** | **String** | Optional callback URL, API will call the provided replyUrl once generation completed | [optional] 



## Enum: ButtonEnum


* `U1` (value: `"U1"`)

* `U2` (value: `"U2"`)

* `U3` (value: `"U3"`)

* `U4` (value: `"U4"`)

* `V1` (value: `"V1"`)

* `V2` (value: `"V2"`)

* `V3` (value: `"V3"`)

* `V4` (value: `"V4"`)

* `⬅️` (value: `"⬅️"`)

* `➡️` (value: `"➡️"`)

* `⬆️` (value: `"⬆️"`)

* `⬇️` (value: `"⬇️"`)

* `🔄` (value: `"🔄"`)

* `Vary (Strong)` (value: `"Vary (Strong)"`)

* `Vary (Subtle)` (value: `"Vary (Subtle)"`)

* `Zoom Out 1.5x` (value: `"Zoom Out 1.5x"`)

* `Zoom Out 2x` (value: `"Zoom Out 2x"`)

* `Make Square` (value: `"Make Square"`)

* `Make Variations` (value: `"Make Variations"`)

* `Remaster` (value: `"Remaster"`)




