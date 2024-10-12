

# GoogleCloudDialogflowCxV3beta1EntityTypeEntity

An **entity entry** for an associated entity type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**synonyms** | **List&lt;String&gt;** | Required. A collection of value synonyms. For example, if the entity type is *vegetable*, and &#x60;value&#x60; is *scallions*, a synonym could be *green onions*. For &#x60;KIND_LIST&#x60; entity types: * This collection must contain exactly one synonym equal to &#x60;value&#x60;. |  [optional] |
|**value** | **String** | Required. The primary value associated with this entity entry. For example, if the entity type is *vegetable*, the value could be *scallions*. For &#x60;KIND_MAP&#x60; entity types: * A canonical value to be used in place of synonyms. For &#x60;KIND_LIST&#x60; entity types: * A string that can contain references to other entity types (with or without aliases). |  [optional] |



