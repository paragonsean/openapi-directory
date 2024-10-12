# GoogleSlidesApi.ReplaceAllShapesWithSheetsChartRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chartId** | **Number** | The ID of the specific chart in the Google Sheets spreadsheet. | [optional] 
**containsText** | [**SubstringMatchCriteria**](SubstringMatchCriteria.md) |  | [optional] 
**linkingMode** | **String** | The mode with which the chart is linked to the source spreadsheet. When not specified, the chart will be an image that is not linked. | [optional] 
**pageObjectIds** | **[String]** | If non-empty, limits the matches to page elements only on the given pages. Returns a 400 bad request error if given the page object ID of a notes page or a notes master, or if a page with that object ID doesn&#39;t exist in the presentation. | [optional] 
**spreadsheetId** | **String** | The ID of the Google Sheets spreadsheet that contains the chart. | [optional] 



## Enum: LinkingModeEnum


* `NOT_LINKED_IMAGE` (value: `"NOT_LINKED_IMAGE"`)

* `LINKED` (value: `"LINKED"`)




