

# EntityList

EntityList stores entities in a format that can be translated to a table in the Alert Center UI.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entities** | [**List&lt;Entity&gt;**](Entity.md) | List of entities affected by the alert. |  [optional] |
|**headers** | **List&lt;String&gt;** | Headers of the values in entities. If no value is defined in Entity, this field should be empty. |  [optional] |
|**name** | **String** | Name of the key detail used to display this entity list. |  [optional] |



