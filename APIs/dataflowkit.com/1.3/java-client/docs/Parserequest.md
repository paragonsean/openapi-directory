

# Parserequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonParent** | **String** | Specifies common ancestor block for a set of fields used to extract data from a web page. _(CSS Selector)_ |  [optional] |
|**fields** | [**List&lt;Field&gt;**](Field.md) | Define a  set of fields used to extract data from a web page. A Field represents a given chunk of extracted data from every block on each page.  |  |
|**format** | [**FormatEnum**](#FormatEnum) | Extracted data is returned either in CSV, MS Excel, JSON, JSON(Lines) or XML format. |  |
|**name** | **String** | Collection name. |  |
|**paginator** | [**Paginator**](Paginator.md) |  |  [optional] |
|**path** | **Boolean** | Path is a special parameter specifying navigation pages only. It collects information from detailed pages. No results from the current page return. Defaults to false. |  [optional] |
|**request** | [**Fetchrequest**](Fetchrequest.md) |  |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| CSV | &quot;csv&quot; |
| JSON | &quot;json&quot; |
| JSONL | &quot;jsonl&quot; |
| EXCEL | &quot;excel&quot; |
| XML | &quot;xml&quot; |



