# Id4iApi.GuidCollection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdTimestamp** | **Number** | The UTC unix timestamp of when this collection has been created | [optional] [readonly] 
**holderOrganizationId** | **String** | Organization namespace of the holder of the collection | [optional] 
**id4n** | **String** | The ID | [optional] [readonly] 
**label** | **String** |  | [optional] 
**ownerOrganizationId** | **String** | Organization namespace of the collection owner | [optional] [readonly] 
**physicalState** | **String** | Physical attachment state of the collection | [optional] 
**type** | **String** |  | [optional] [readonly] 



## Enum: PhysicalStateEnum


* `UNATTACHED` (value: `"UNATTACHED"`)

* `ATTACHED` (value: `"ATTACHED"`)

* `DETACHED` (value: `"DETACHED"`)





## Enum: TypeEnum


* `ROUTING_COLLECTION` (value: `"ROUTING_COLLECTION"`)

* `LOGISTIC_COLLECTION` (value: `"LOGISTIC_COLLECTION"`)

* `LABELLED_COLLECTION` (value: `"LABELLED_COLLECTION"`)




