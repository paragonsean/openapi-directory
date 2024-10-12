

# FindReplaceRequest

Finds and replaces data in cells over a range, sheet, or all sheets.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allSheets** | **Boolean** | True to find/replace over all sheets. |  [optional] |
|**find** | **String** | The value to search. |  [optional] |
|**includeFormulas** | **Boolean** | True if the search should include cells with formulas. False to skip cells with formulas. |  [optional] |
|**matchCase** | **Boolean** | True if the search is case sensitive. |  [optional] |
|**matchEntireCell** | **Boolean** | True if the find value should match the entire cell. |  [optional] |
|**range** | [**GridRange**](GridRange.md) |  |  [optional] |
|**replacement** | **String** | The value to use as the replacement. |  [optional] |
|**searchByRegex** | **Boolean** | True if the find value is a regex. The regular expression and replacement should follow Java regex rules at https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html. The replacement string is allowed to refer to capturing groups. For example, if one cell has the contents &#x60;\&quot;Google Sheets\&quot;&#x60; and another has &#x60;\&quot;Google Docs\&quot;&#x60;, then searching for &#x60;\&quot;o.* (.*)\&quot;&#x60; with a replacement of &#x60;\&quot;$1 Rocks\&quot;&#x60; would change the contents of the cells to &#x60;\&quot;GSheets Rocks\&quot;&#x60; and &#x60;\&quot;GDocs Rocks\&quot;&#x60; respectively. |  [optional] |
|**sheetId** | **Integer** | The sheet to find/replace over. |  [optional] |



