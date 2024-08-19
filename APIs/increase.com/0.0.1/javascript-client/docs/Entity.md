# IncreaseApi.Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporation** | [**Corporation**](Corporation.md) |  | 
**description** | **String** | The entity&#39;s description for display purposes. | 
**id** | **String** | The entity&#39;s identifier. | 
**joint** | [**Joint**](Joint.md) |  | 
**naturalPerson** | [**Individual2**](Individual2.md) |  | 
**relationship** | **String** | The relationship between your group and the entity. | 
**structure** | **String** | The entity&#39;s legal structure. | 
**supplementalDocuments** | [**[SupplementalDocumentsElement]**](SupplementalDocumentsElement.md) | Additional documentation associated with the entity. | 
**trust** | [**Trust**](Trust.md) |  | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;entity&#x60;. | 



## Enum: RelationshipEnum


* `affiliated` (value: `"affiliated"`)

* `informational` (value: `"informational"`)

* `unaffiliated` (value: `"unaffiliated"`)





## Enum: StructureEnum


* `corporation` (value: `"corporation"`)

* `natural_person` (value: `"natural_person"`)

* `joint` (value: `"joint"`)

* `trust` (value: `"trust"`)





## Enum: TypeEnum


* `entity` (value: `"entity"`)




