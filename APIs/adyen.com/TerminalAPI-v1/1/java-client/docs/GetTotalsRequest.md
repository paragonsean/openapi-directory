

# GetTotalsRequest

It conveys information from the Sale System related to the scope and the format of the totals to be computed by the POI System. Content of the Get Totals Request message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**totalDetails** | [**List&lt;TotalDetailsEnum&gt;**](#List&lt;TotalDetailsEnum&gt;) |  |  [optional] |
|**totalFilter** | [**TotalFilter**](TotalFilter.md) |  |  [optional] |



## Enum: List&lt;TotalDetailsEnum&gt;

| Name | Value |
|---- | -----|
| OPERATOR_ID | &quot;OperatorID&quot; |
| POIID | &quot;POIID&quot; |
| SALE_ID | &quot;SaleID&quot; |
| SHIFT_NUMBER | &quot;ShiftNumber&quot; |
| TOTALS_GROUP_ID | &quot;TotalsGroupID&quot; |



