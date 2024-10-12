# AvazaApiDocumentation.ExpenseSummaryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expenseDateFrom** | **Date** | (Required) Filter for expenses with expense dates greater or equal to the specified date. e.g. 2019-01-25. | [optional] 
**expenseDateTo** | **Date** | (Required) Filter for expenses with an expense date smaller or equal to the specified  date. e.g. 2019-01-25. | [optional] 
**groupBy** | **[String]** | (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \&quot;Category\&quot;, \&quot;ChargeableStatus\&quot;, \&quot;Merchant\&quot;, \&quot;ApprovalStatus\&quot;, \&quot;ReimbursementStatus\&quot;, \&quot;Customer\&quot;, \&quot;Project\&quot;, \&quot;User\&quot;, \&quot;Task\&quot;, \&quot;Year\&quot;, \&quot;Month\&quot;, \&quot;Day\&quot;, \&quot;Week\&quot;. | [optional] 
**projectID** | **Number** | (Optional) Filter by Project | [optional] 
**userID** | **[Number]** | (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose expenses should be retrieved. If the current user doesn&#39;t have impersonation rights, then they will only see their own data. | [optional] 


