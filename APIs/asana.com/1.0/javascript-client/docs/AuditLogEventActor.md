# Asana.AuditLogEventActor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actorType** | **String** | The type of actor. Can be one of &#x60;user&#x60;, &#x60;asana&#x60;, &#x60;asana_support&#x60;, &#x60;anonymous&#x60;, or &#x60;external_administrator&#x60;. | [optional] 
**email** | **String** | The email of the actor, if it is a user. | [optional] 
**gid** | **String** | Globally unique identifier of the actor, if it is a user. | [optional] 
**name** | **String** | The name of the actor, if it is a user. | [optional] 



## Enum: ActorTypeEnum


* `user` (value: `"user"`)

* `asana` (value: `"asana"`)

* `asana_support` (value: `"asana_support"`)

* `anonymous` (value: `"anonymous"`)

* `external_administrator` (value: `"external_administrator"`)




