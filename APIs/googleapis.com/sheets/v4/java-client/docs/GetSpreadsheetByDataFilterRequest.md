

# GetSpreadsheetByDataFilterRequest

The request for retrieving a Spreadsheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataFilters** | [**List&lt;DataFilter&gt;**](DataFilter.md) | The DataFilters used to select which ranges to retrieve from the spreadsheet. |  [optional] |
|**includeGridData** | **Boolean** | True if grid data should be returned. This parameter is ignored if a field mask was set in the request. |  [optional] |



