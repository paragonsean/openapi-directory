# MidjourneyRestApiByUseapiNet.JobsBlendPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blendDimensions** | **String** |  | [optional] 
**blendUrls** | **[String]** | Must contain at least 2 valid URL image links, up to 5 URL image links supported | 
**channel** | **String** | Discord channel id | 
**discord** | **String** | Discord token | 
**maxJobs** | **Number** | Optional Maximum Concurrent Jobs for current Midjourney subscription | [optional] 
**replyRef** | **String** | Optional reference id which will be stored and returned along with this job response / result | [optional] 
**replyUrl** | **String** | Optional callback URL, API will call the provided replyUrl once generation completed | [optional] 
**server** | **String** | Discord server id | 



## Enum: BlendDimensionsEnum


* `Portrait` (value: `"Portrait"`)

* `Square` (value: `"Square"`)

* `Landscape` (value: `"Landscape"`)




