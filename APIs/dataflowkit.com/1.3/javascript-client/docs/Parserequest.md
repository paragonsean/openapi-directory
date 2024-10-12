# DataflowKitWebScraper.Parserequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commonParent** | **String** | Specifies common ancestor block for a set of fields used to extract data from a web page. _(CSS Selector)_ | [optional] 
**fields** | [**[Field]**](Field.md) | Define a  set of fields used to extract data from a web page. A Field represents a given chunk of extracted data from every block on each page.  | 
**format** | **String** | Extracted data is returned either in CSV, MS Excel, JSON, JSON(Lines) or XML format. | 
**name** | **String** | Collection name. | 
**paginator** | [**Paginator**](Paginator.md) |  | [optional] 
**path** | **Boolean** | Path is a special parameter specifying navigation pages only. It collects information from detailed pages. No results from the current page return. Defaults to false. | [optional] [default to false]
**request** | [**Fetchrequest**](Fetchrequest.md) |  | [optional] 



## Enum: FormatEnum


* `csv` (value: `"csv"`)

* `json` (value: `"json"`)

* `jsonl` (value: `"jsonl"`)

* `excel` (value: `"excel"`)

* `xml` (value: `"xml"`)




