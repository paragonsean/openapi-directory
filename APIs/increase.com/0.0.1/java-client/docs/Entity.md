

# Entity

Entities are the legal entities that own accounts. They can be people, corporations, partnerships, or trusts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**corporation** | [**Corporation**](Corporation.md) |  |  |
|**description** | **String** | The entity&#39;s description for display purposes. |  |
|**id** | **String** | The entity&#39;s identifier. |  |
|**joint** | [**Joint**](Joint.md) |  |  |
|**naturalPerson** | [**Individual2**](Individual2.md) |  |  |
|**relationship** | [**RelationshipEnum**](#RelationshipEnum) | The relationship between your group and the entity. |  |
|**structure** | [**StructureEnum**](#StructureEnum) | The entity&#39;s legal structure. |  |
|**supplementalDocuments** | [**List&lt;SupplementalDocumentsElement&gt;**](SupplementalDocumentsElement.md) | Additional documentation associated with the entity. |  |
|**trust** | [**Trust**](Trust.md) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;entity&#x60;. |  |



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



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ENTITY | &quot;entity&quot; |



