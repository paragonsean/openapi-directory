# TurbineLabsApi.ChangeEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changeType** | **String** | Whether the value was added or removed to the object. | [optional] 
**objectKey** | **String** | An ID uniquely identifying the object being changed. | [optional] 
**objectType** | **String** | The name of the object being being altered. | [optional] 
**path** | **String** | A dot-separated / bracket-indexed path to the field changed on the object. | [optional] 
**value** | **String** | The value that has been added or removed to the object at the attribute path indicated in path.  | [optional] 
**zoneKey** | **String** | The zone this object is located in. | [optional] 



## Enum: ChangeTypeEnum


* `addition` (value: `"addition"`)

* `removal` (value: `"removal"`)





## Enum: ObjectTypeEnum


* `org` (value: `"org"`)

* `user` (value: `"user"`)

* `zone` (value: `"zone"`)

* `proxy` (value: `"proxy"`)

* `domain` (value: `"domain"`)

* `route` (value: `"route"`)

* `shared_rules` (value: `"shared_rules"`)

* `cluster` (value: `"cluster"`)




