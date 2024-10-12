# CloudDatastoreApi.EntityResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | The time at which the entity was created. This field is set for &#x60;FULL&#x60; entity results. If this entity is missing, this field will not be set. | [optional] 
**cursor** | **Blob** | A cursor that points to the position after the result entity. Set only when the &#x60;EntityResult&#x60; is part of a &#x60;QueryResultBatch&#x60; message. | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 
**updateTime** | **String** | The time at which the entity was last changed. This field is set for &#x60;FULL&#x60; entity results. If this entity is missing, this field will not be set. | [optional] 
**version** | **String** | The version of the entity, a strictly positive number that monotonically increases with changes to the entity. This field is set for &#x60;FULL&#x60; entity results. For missing entities in &#x60;LookupResponse&#x60;, this is the version of the snapshot that was used to look up the entity, and it is always set except for eventually consistent reads. | [optional] 


