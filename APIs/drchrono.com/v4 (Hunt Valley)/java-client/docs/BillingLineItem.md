

# BillingLineItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustment** | **BigDecimal** | Adjustment from total billed |  [optional] [readonly] |
|**allowed** | **BigDecimal** | Amount allowed by insurance |  [optional] [readonly] |
|**appointment** | **Integer** | Appointment ID |  |
|**balanceIns** | **BigDecimal** | Insurance balance |  [optional] |
|**balancePt** | **BigDecimal** | Patient balance |  [optional] [readonly] |
|**balanceTotal** | **String** | Total balance |  [optional] [readonly] |
|**billed** | **BigDecimal** | Total billed |  [optional] [readonly] |
|**billingStatus** | [**BillingStatusEnum**](#BillingStatusEnum) | One of &#x60;\&quot;\&quot;&#x60;, &#x60;\&quot;Incomplete Information\&quot;&#x60;, &#x60;\&quot;In Process Emdeon\&quot;&#x60;, &#x60;\&quot;In Process iHCFA\&quot;&#x60;, &#x60;\&quot;In Process Gateway\&quot;&#x60;, &#x60;\&quot;Rejected Emdeon\&quot;&#x60;, &#x60;\&quot;Rejected iHCFA\&quot;&#x60;, &#x60;\&quot;Rejected Gateway\&quot;&#x60;, &#x60;\&quot;In Process Payer\&quot;&#x60;, &#x60;\&quot;Payer Acknowledged\&quot;&#x60;, &#x60;\&quot;Rejected Payer\&quot;&#x60;, &#x60;\&quot;Paid in Full\&quot;&#x60;,  &#x60;\&quot;Partially Paid\&quot;&#x60;,  &#x60;\&quot;Coordination of Benefits\&quot;&#x60;,  &#x60;\&quot;ERA Received\&quot;&#x60;,  &#x60;\&quot;ERA Denied\&quot;&#x60; |  [optional] [readonly] |
|**code** | **String** |  |  |
|**deniedFlag** | **Boolean** |  |  [optional] [readonly] |
|**description** | **String** |  |  [optional] [readonly] |
|**diagnosisPointers** | **List&lt;String&gt;** | List of 4 diagnosis pointers |  |
|**doctor** | **String** | Doctor ID |  [optional] [readonly] |
|**expectedReimbursement** | **BigDecimal** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**ins1Paid** | **BigDecimal** | Amount paid by patient&#39;s primary insurer |  [optional] [readonly] |
|**ins2Paid** | **BigDecimal** | Amount paid by patient&#39;s secondary insurer |  [optional] [readonly] |
|**ins3Paid** | **BigDecimal** | Amount paid by patinet&#39;s tertiary insurer |  [optional] [readonly] |
|**insTotal** | **String** | Total amount paid by patient&#39;s insurers |  [optional] [readonly] |
|**insuranceStatus** | **String** | This corresponds to the \&quot;Status/Adj Type\&quot; from billing detail screen |  [optional] [readonly] |
|**modifiers** | **List&lt;String&gt;** | List of 4 code modifiers |  [optional] |
|**paidTotal** | **String** | Total amount paid |  [optional] [readonly] |
|**patient** | **String** | Patient ID |  [optional] [readonly] |
|**postedDate** | **String** |  |  [optional] [readonly] |
|**price** | **BigDecimal** | Price of procedure |  [optional] |
|**procedureType** | [**ProcedureTypeEnum**](#ProcedureTypeEnum) | One of &#x60;\&quot;CPT(C)\&quot;&#x60;, &#x60;\&quot;HCPCS(H)\&quot;&#x60;, &#x60;\&quot;Custom(U)\&quot;&#x60;, use 1 character identifier when using &#x60;POST&#x60; |  |
|**ptPaid** | **BigDecimal** | Amount paid by patient |  [optional] |
|**quantity** | **BigDecimal** |  |  [optional] |
|**serviceDate** | **String** | Date on which the service was rendered |  [optional] [readonly] |
|**units** | **String** | Default to \&quot;UN\&quot; |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |



## Enum: BillingStatusEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| INCOMPLETE_INFORMATION | &quot;Incomplete Information&quot; |
| IN_PROCESS_EMDEON | &quot;In Process Emdeon&quot; |
| IN_PROCESS_I_HCFA | &quot;In Process iHCFA&quot; |
| IN_PROCESS_GATEWAY | &quot;In Process Gateway&quot; |
| IN_PROCESS_JOPARI | &quot;In Process Jopari&quot; |
| IN_PROCESS_WAYSTAR | &quot;In Process Waystar&quot; |
| REJECTED_EMDEON | &quot;Rejected Emdeon&quot; |
| REJECTED_I_HCFA | &quot;Rejected iHCFA&quot; |
| REJECTED_GATEWAY | &quot;Rejected Gateway&quot; |
| REJECTED_JOPARI | &quot;Rejected Jopari&quot; |
| REJECTED_WAYSTAR | &quot;Rejected Waystar&quot; |
| IN_PROCESS_PAYER | &quot;In Process Payer&quot; |
| PAYER_ACKNOWLEDGED | &quot;Payer Acknowledged&quot; |
| REJECTED_PAYER | &quot;Rejected Payer&quot; |
| PAID_IN_FULL | &quot;Paid in Full&quot; |
| PARTIALLY_PAID | &quot;Partially Paid&quot; |
| COORDINATION_OF_BENEFITS | &quot;Coordination of Benefits&quot; |
| ERA_RECEIVED | &quot;ERA Received&quot; |
| ERA_DENIED | &quot;ERA Denied&quot; |



## Enum: ProcedureTypeEnum

| Name | Value |
|---- | -----|
| C | &quot;C&quot; |
| H | &quot;H&quot; |
| U | &quot;U&quot; |
| S | &quot;S&quot; |



