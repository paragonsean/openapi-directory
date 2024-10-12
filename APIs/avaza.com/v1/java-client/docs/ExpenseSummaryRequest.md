

# ExpenseSummaryRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expenseDateFrom** | **OffsetDateTime** | (Required) Filter for expenses with expense dates greater or equal to the specified date. e.g. 2019-01-25. |  [optional] |
|**expenseDateTo** | **OffsetDateTime** | (Required) Filter for expenses with an expense date smaller or equal to the specified  date. e.g. 2019-01-25. |  [optional] |
|**groupBy** | **List&lt;String&gt;** | (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \&quot;Category\&quot;, \&quot;ChargeableStatus\&quot;, \&quot;Merchant\&quot;, \&quot;ApprovalStatus\&quot;, \&quot;ReimbursementStatus\&quot;, \&quot;Customer\&quot;, \&quot;Project\&quot;, \&quot;User\&quot;, \&quot;Task\&quot;, \&quot;Year\&quot;, \&quot;Month\&quot;, \&quot;Day\&quot;, \&quot;Week\&quot;. |  [optional] |
|**projectID** | **Integer** | (Optional) Filter by Project |  [optional] |
|**userID** | **List&lt;Integer&gt;** | (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose expenses should be retrieved. If the current user doesn&#39;t have impersonation rights, then they will only see their own data. |  [optional] |



