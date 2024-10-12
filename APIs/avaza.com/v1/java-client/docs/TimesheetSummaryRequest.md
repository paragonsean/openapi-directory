

# TimesheetSummaryRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entryDateFrom** | **OffsetDateTime** | (Required) Filter for timesheets greater or equal to the specified date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00 |  [optional] |
|**entryDateTo** | **OffsetDateTime** | (Required) Filter for timesheets with an entry date smaller or equal to the specified  date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00 |  [optional] |
|**groupBy** | **List&lt;String&gt;** | (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \&quot;Customer\&quot;, \&quot;Project\&quot;, \&quot;Category\&quot;, \&quot;User\&quot;, \&quot;Task\&quot;, \&quot;Year\&quot;, \&quot;Month\&quot;, \&quot;Day\&quot;, \&quot;Week\&quot;. |  [optional] |
|**projectID** | **Integer** | (Optional) Filter by Project |  [optional] |
|**userID** | **List&lt;Integer&gt;** | (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose timesheets should be retrieved. If the current user doesn&#39;t have impersonation rights, then they will only see their own data. |  [optional] |
|**isBillable** | **Boolean** | (Optional) Filter by the billable status of Timesheets. |  [optional] |
|**isInvoiced** | **Boolean** | (Optional) Filter for timesheets by whether they have been Invoiced or not. |  [optional] |



