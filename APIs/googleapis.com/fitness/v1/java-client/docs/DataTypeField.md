

# DataTypeField

In case of multi-dimensional data (such as an accelerometer with x, y, and z axes) each field represents one dimension. Each data type field has a unique name which identifies it. The field also defines the format of the data (int, float, etc.). This message is only instantiated in code and not used for wire comms or stored in any way.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**format** | [**FormatEnum**](#FormatEnum) | The different supported formats for each field in a data type. |  [optional] |
|**name** | **String** | Defines the name and format of data. Unlike data type names, field names are not namespaced, and only need to be unique within the data type. |  [optional] |
|**optional** | **Boolean** |  |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| INTEGER | &quot;integer&quot; |
| FLOAT_POINT | &quot;floatPoint&quot; |
| STRING | &quot;string&quot; |
| MAP | &quot;map&quot; |
| INTEGER_LIST | &quot;integerList&quot; |
| FLOAT_LIST | &quot;floatList&quot; |
| BLOB | &quot;blob&quot; |



