

# CreateAnEntityParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**corporation** | [**CreateAnEntityParametersCorporation**](CreateAnEntityParametersCorporation.md) |  |  [optional] |
|**description** | **String** | The description you choose to give the entity. |  [optional] |
|**joint** | [**CreateAnEntityParametersJoint**](CreateAnEntityParametersJoint.md) |  |  [optional] |
|**naturalPerson** | [**CreateAnEntityParametersNaturalPerson**](CreateAnEntityParametersNaturalPerson.md) |  |  [optional] |
|**relationship** | [**RelationshipEnum**](#RelationshipEnum) | The relationship between your group and the entity. |  |
|**structure** | [**StructureEnum**](#StructureEnum) | The type of Entity to create. |  |
|**supplementalDocuments** | [**List&lt;CreateAnEntityParametersSupplementalDocumentsInner&gt;**](CreateAnEntityParametersSupplementalDocumentsInner.md) | Additional documentation associated with the entity. |  [optional] |
|**trust** | [**CreateAnEntityParametersTrust**](CreateAnEntityParametersTrust.md) |  |  [optional] |



## Enum: RelationshipEnum

| Name | Value |
|---- | -----|
| AFFILIATED | &quot;affiliated&quot; |
| INFORMATIONAL | &quot;informational&quot; |
| UNAFFILIATED | &quot;unaffiliated&quot; |



## Enum: StructureEnum

| Name | Value |
|---- | -----|
| CORPORATION | &quot;corporation&quot; |
| NATURAL_PERSON | &quot;natural_person&quot; |
| JOINT | &quot;joint&quot; |
| TRUST | &quot;trust&quot; |



