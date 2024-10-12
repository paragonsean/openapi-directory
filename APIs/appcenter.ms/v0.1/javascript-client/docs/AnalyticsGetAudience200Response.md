# AppCenterClient.AnalyticsGetAudience200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customProperties** | **{String: String}** | Custom properties used in the definition. | [optional] 
**enabled** | **Boolean** |  | [optional] [default to true]
**estimatedTotalCount** | **Number** | Estimated total audience size. | [optional] 
**timestamp** | **Date** | Date the audience was last refreshed. | [optional] 
**definition** | **String** | Audience definition in OData format. | [optional] 
**description** | **String** | Audience description. | [optional] 
**estimatedCount** | **Number** | Estimated audience size. | [optional] 
**name** | **String** | Audience name. | [optional] 
**state** | **String** | Audience state. | [optional] 



## Enum: {String: String}


* `string` (value: `"string"`)

* `number` (value: `"number"`)

* `boolean` (value: `"boolean"`)

* `date_time` (value: `"date_time"`)





## Enum: StateEnum


* `Calculating` (value: `"Calculating"`)

* `Ready` (value: `"Ready"`)

* `Disabled` (value: `"Disabled"`)




