

# Attraction

Attraction

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Indicate if the entity is active, inactive entity won&#39;t appear in Discovery API |  [optional] |
|**additionalInfos** | **Map&lt;String, String&gt;** | Additional informations of the entity - multi-lingual fields |  [optional] |
|**classifications** | [**List&lt;Classification&gt;**](Classification.md) | Attraction&#39;s classifications |  [optional] |
|**descriptions** | **Map&lt;String, String&gt;** | Descriptions of the entity - multi-lingual fields |  [optional] |
|**discoverable** | **Boolean** | True if the entity is dicoverable in discovery API |  [optional] |
|**images** | [**Set&lt;Image&gt;**](Image.md) | Images of the entity |  [optional] |
|**names** | **Map&lt;String, String&gt;** | Names of the entity - multi-lingual fields |  [optional] |
|**references** | **Map&lt;String, String&gt;** | References of this entity in an other system. Reference is the exact same entity |  [optional] |
|**relationships** | **List&lt;Object&gt;** | Relationships on the entity, like if the entity is a duplicate of another one |  [optional] |
|**source** | [**Source**](Source.md) |  |  [optional] |
|**test** | **Boolean** | Indicate if this is a test entity, by default test entities won&#39;t appear in discovery API |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the entity |  |
|**url** | **String** | URL of a web site detail page of the entity |  [optional] |
|**version** | **Long** | Version of the entity. Version is to avoid updated an entity with an older version |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EVENT | &quot;event&quot; |
| VENUE | &quot;venue&quot; |
| ATTRACTION | &quot;attraction&quot; |



