

# USqlTablePreview

A Data Lake Analytics catalog table or partition preview rows item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rows** | **List&lt;List&lt;String&gt;&gt;** | the rows of the table or partition preview, where each row is an array of string representations the row&#39;s values. Note: Byte arrays will appear as base-64 encoded values, SqlMap and SqlArray objects will appear as escaped JSON objects, and DateTime objects will appear as ISO formatted UTC date-times. |  [optional] |
|**schema** | [**List&lt;USqlTableColumn&gt;**](USqlTableColumn.md) | the schema of the table or partition. |  [optional] |
|**totalColumnCount** | **Long** | the total number of columns in the table or partition. |  [optional] |
|**totalRowCount** | **Long** | the total number of rows in the table or partition. |  [optional] |
|**truncated** | **Boolean** | true if the amount of data in the response is less than expected due to the preview operation&#39;s size limitations. This can occur if the requested rows or row counts are too large. |  [optional] |



