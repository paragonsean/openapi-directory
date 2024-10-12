

# SymptomPublic


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **String** |  |  [optional] |
|**children** | **Object** | list of child symptoms |  [optional] |
|**commonName** | **String** |  |  [optional] |
|**extras** | **Map&lt;String, Object&gt;** | additional content, like custom properties or images |  [optional] |
|**id** | **String** |  |  |
|**imageSource** | **String** |  |  [optional] |
|**imageUrl** | **String** |  |  [optional] |
|**name** | **String** |  |  |
|**parentId** | **String** | id of parent symptom |  [optional] |
|**parentRelation** | [**ParentRelationEnum**](#ParentRelationEnum) | type of relation with parent symptom |  [optional] |
|**sexFilter** | [**SexFilterEnum**](#SexFilterEnum) |  |  |



## Enum: ParentRelationEnum

| Name | Value |
|---- | -----|
| BASE | &quot;base&quot; |
| DURATION | &quot;duration&quot; |
| SEVERITY | &quot;severity&quot; |
| CHARACTER | &quot;character&quot; |
| EXACERBATING_FACTOR | &quot;exacerbating_factor&quot; |
| DIMINISHING_FACTOR | &quot;diminishing_factor&quot; |
| LOCATION | &quot;location&quot; |
| RADIATION | &quot;radiation&quot; |



## Enum: SexFilterEnum

| Name | Value |
|---- | -----|
| BOTH | &quot;both&quot; |
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |



