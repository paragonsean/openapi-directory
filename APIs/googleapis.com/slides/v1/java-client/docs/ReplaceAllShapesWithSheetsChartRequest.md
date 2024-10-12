

# ReplaceAllShapesWithSheetsChartRequest

Replaces all shapes that match the given criteria with the provided Google Sheets chart. The chart will be scaled and centered to fit within the bounds of the original shape. NOTE: Replacing shapes with a chart requires at least one of the spreadsheets.readonly, spreadsheets, drive.readonly, or drive OAuth scopes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chartId** | **Integer** | The ID of the specific chart in the Google Sheets spreadsheet. |  [optional] |
|**containsText** | [**SubstringMatchCriteria**](SubstringMatchCriteria.md) |  |  [optional] |
|**linkingMode** | [**LinkingModeEnum**](#LinkingModeEnum) | The mode with which the chart is linked to the source spreadsheet. When not specified, the chart will be an image that is not linked. |  [optional] |
|**pageObjectIds** | **List&lt;String&gt;** | If non-empty, limits the matches to page elements only on the given pages. Returns a 400 bad request error if given the page object ID of a notes page or a notes master, or if a page with that object ID doesn&#39;t exist in the presentation. |  [optional] |
|**spreadsheetId** | **String** | The ID of the Google Sheets spreadsheet that contains the chart. |  [optional] |



## Enum: LinkingModeEnum

| Name | Value |
|---- | -----|
| NOT_LINKED_IMAGE | &quot;NOT_LINKED_IMAGE&quot; |
| LINKED | &quot;LINKED&quot; |



