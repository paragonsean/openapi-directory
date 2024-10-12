

# BatchUpdateSpreadsheetRequest

The request for updating any aspect of a spreadsheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includeSpreadsheetInResponse** | **Boolean** | Determines if the update response should include the spreadsheet resource. |  [optional] |
|**requests** | [**List&lt;Request&gt;**](Request.md) | A list of updates to apply to the spreadsheet. Requests will be applied in the order they are specified. If any request is not valid, no requests will be applied. |  [optional] |
|**responseIncludeGridData** | **Boolean** | True if grid data should be returned. Meaningful only if include_spreadsheet_in_response is &#39;true&#39;. This parameter is ignored if a field mask was set in the request. |  [optional] |
|**responseRanges** | **List&lt;String&gt;** | Limits the ranges included in the response spreadsheet. Meaningful only if include_spreadsheet_in_response is &#39;true&#39;. |  [optional] |



