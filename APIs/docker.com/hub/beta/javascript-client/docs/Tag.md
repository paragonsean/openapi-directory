# DockerHubApi.Tag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | **Number** | ID of the user that pushed the tag | [optional] 
**fullSize** | **Number** | compressed size (sum of all layers) of the tagged image | [optional] 
**id** | **Number** | tag ID | [optional] 
**images** | [**Image**](.md) |  | [optional] 
**lastUpdated** | **String** | datetime of last update | [optional] 
**lastUpdater** | **Number** | ID of the last user that updated the tag | [optional] 
**lastUpdaterUsername** | **String** | Hub username of the user that updated the tag | [optional] 
**name** | **String** | name of the tag | [optional] 
**repository** | **Number** | repository ID | [optional] 
**status** | **String** | whether a tag has been pushed to or pulled in the past month | [optional] 
**tagLastPulled** | **String** | datetime of last pull | [optional] 
**tagLastPushed** | **String** | datetime of last push | [optional] 
**v2** | **String** | repository API version | [optional] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)




