

# DropNullFields

Specifies a transform that removes columns from the dataset if all values in the column are 'null'. By default, Glue Studio will recognize null objects, but some values such as empty strings, strings that are \"null\", -1 integers or other placeholders such as zeros, are not automatically recognized as nulls.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**inputs** | [**List**](List.md) |  |  |
|**nullCheckBoxList** | [**DropNullFieldsNullCheckBoxList**](DropNullFieldsNullCheckBoxList.md) |  |  [optional] |
|**nullTextList** | [**List**](List.md) |  |  [optional] |



