# IncreaseApi.CreateAnEntityParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporation** | [**CreateAnEntityParametersCorporation**](CreateAnEntityParametersCorporation.md) |  | [optional] 
**description** | **String** | The description you choose to give the entity. | [optional] 
**joint** | [**CreateAnEntityParametersJoint**](CreateAnEntityParametersJoint.md) |  | [optional] 
**naturalPerson** | [**CreateAnEntityParametersNaturalPerson**](CreateAnEntityParametersNaturalPerson.md) |  | [optional] 
**relationship** | **String** | The relationship between your group and the entity. | 
**structure** | **String** | The type of Entity to create. | 
**supplementalDocuments** | [**[CreateAnEntityParametersSupplementalDocumentsInner]**](CreateAnEntityParametersSupplementalDocumentsInner.md) | Additional documentation associated with the entity. | [optional] 
**trust** | [**CreateAnEntityParametersTrust**](CreateAnEntityParametersTrust.md) |  | [optional] 



## Enum: RelationshipEnum


* `affiliated` (value: `"affiliated"`)

* `informational` (value: `"informational"`)

* `unaffiliated` (value: `"unaffiliated"`)





## Enum: StructureEnum


* `corporation` (value: `"corporation"`)

* `natural_person` (value: `"natural_person"`)

* `joint` (value: `"joint"`)

* `trust` (value: `"trust"`)




