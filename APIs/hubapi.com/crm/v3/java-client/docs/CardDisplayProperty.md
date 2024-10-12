

# CardDisplayProperty

Definition for a card display property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataType** | [**DataTypeEnum**](#DataTypeEnum) | Type of data represented by this property. |  |
|**label** | **String** | The label for this property as you&#39;d like it displayed to users. |  |
|**name** | **String** | An internal identifier for this property. This value must be unique TODO. |  |
|**options** | [**List&lt;DisplayOption&gt;**](DisplayOption.md) | An array of available options that can be displayed. Only used in when &#x60;dataType&#x60; is &#x60;STATUS&#x60;. |  |



## Enum: DataTypeEnum

| Name | Value |
|---- | -----|
| BOOLEAN | &quot;BOOLEAN&quot; |
| CURRENCY | &quot;CURRENCY&quot; |
| DATE | &quot;DATE&quot; |
| DATETIME | &quot;DATETIME&quot; |
| EMAIL | &quot;EMAIL&quot; |
| LINK | &quot;LINK&quot; |
| NUMERIC | &quot;NUMERIC&quot; |
| STRING | &quot;STRING&quot; |
| STATUS | &quot;STATUS&quot; |



