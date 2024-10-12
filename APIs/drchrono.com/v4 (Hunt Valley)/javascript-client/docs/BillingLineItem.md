# OpenapiJsClient.BillingLineItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment** | **Number** | Adjustment from total billed | [optional] [readonly] 
**allowed** | **Number** | Amount allowed by insurance | [optional] [readonly] 
**appointment** | **Number** | Appointment ID | 
**balanceIns** | **Number** | Insurance balance | [optional] 
**balancePt** | **Number** | Patient balance | [optional] [readonly] 
**balanceTotal** | **String** | Total balance | [optional] [readonly] 
**billed** | **Number** | Total billed | [optional] [readonly] 
**billingStatus** | **String** | One of &#x60;\&quot;\&quot;&#x60;, &#x60;\&quot;Incomplete Information\&quot;&#x60;, &#x60;\&quot;In Process Emdeon\&quot;&#x60;, &#x60;\&quot;In Process iHCFA\&quot;&#x60;, &#x60;\&quot;In Process Gateway\&quot;&#x60;, &#x60;\&quot;Rejected Emdeon\&quot;&#x60;, &#x60;\&quot;Rejected iHCFA\&quot;&#x60;, &#x60;\&quot;Rejected Gateway\&quot;&#x60;, &#x60;\&quot;In Process Payer\&quot;&#x60;, &#x60;\&quot;Payer Acknowledged\&quot;&#x60;, &#x60;\&quot;Rejected Payer\&quot;&#x60;, &#x60;\&quot;Paid in Full\&quot;&#x60;,  &#x60;\&quot;Partially Paid\&quot;&#x60;,  &#x60;\&quot;Coordination of Benefits\&quot;&#x60;,  &#x60;\&quot;ERA Received\&quot;&#x60;,  &#x60;\&quot;ERA Denied\&quot;&#x60; | [optional] [readonly] 
**code** | **String** |  | 
**deniedFlag** | **Boolean** |  | [optional] [readonly] 
**description** | **String** |  | [optional] [readonly] 
**diagnosisPointers** | **[String]** | List of 4 diagnosis pointers | 
**doctor** | **String** | Doctor ID | [optional] [readonly] 
**expectedReimbursement** | **Number** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**ins1Paid** | **Number** | Amount paid by patient&#39;s primary insurer | [optional] [readonly] 
**ins2Paid** | **Number** | Amount paid by patient&#39;s secondary insurer | [optional] [readonly] 
**ins3Paid** | **Number** | Amount paid by patinet&#39;s tertiary insurer | [optional] [readonly] 
**insTotal** | **String** | Total amount paid by patient&#39;s insurers | [optional] [readonly] 
**insuranceStatus** | **String** | This corresponds to the \&quot;Status/Adj Type\&quot; from billing detail screen | [optional] [readonly] 
**modifiers** | **[String]** | List of 4 code modifiers | [optional] 
**paidTotal** | **String** | Total amount paid | [optional] [readonly] 
**patient** | **String** | Patient ID | [optional] [readonly] 
**postedDate** | **String** |  | [optional] [readonly] 
**price** | **Number** | Price of procedure | [optional] 
**procedureType** | **String** | One of &#x60;\&quot;CPT(C)\&quot;&#x60;, &#x60;\&quot;HCPCS(H)\&quot;&#x60;, &#x60;\&quot;Custom(U)\&quot;&#x60;, use 1 character identifier when using &#x60;POST&#x60; | 
**ptPaid** | **Number** | Amount paid by patient | [optional] 
**quantity** | **Number** |  | [optional] 
**serviceDate** | **String** | Date on which the service was rendered | [optional] [readonly] 
**units** | **String** | Default to \&quot;UN\&quot; | [optional] 
**updatedAt** | **String** |  | [optional] [readonly] 



## Enum: BillingStatusEnum


* `empty` (value: `""`)

* `Incomplete Information` (value: `"Incomplete Information"`)

* `In Process Emdeon` (value: `"In Process Emdeon"`)

* `In Process iHCFA` (value: `"In Process iHCFA"`)

* `In Process Gateway` (value: `"In Process Gateway"`)

* `In Process Jopari` (value: `"In Process Jopari"`)

* `In Process Waystar` (value: `"In Process Waystar"`)

* `Rejected Emdeon` (value: `"Rejected Emdeon"`)

* `Rejected iHCFA` (value: `"Rejected iHCFA"`)

* `Rejected Gateway` (value: `"Rejected Gateway"`)

* `Rejected Jopari` (value: `"Rejected Jopari"`)

* `Rejected Waystar` (value: `"Rejected Waystar"`)

* `In Process Payer` (value: `"In Process Payer"`)

* `Payer Acknowledged` (value: `"Payer Acknowledged"`)

* `Rejected Payer` (value: `"Rejected Payer"`)

* `Paid in Full` (value: `"Paid in Full"`)

* `Partially Paid` (value: `"Partially Paid"`)

* `Coordination of Benefits` (value: `"Coordination of Benefits"`)

* `ERA Received` (value: `"ERA Received"`)

* `ERA Denied` (value: `"ERA Denied"`)





## Enum: ProcedureTypeEnum


* `C` (value: `"C"`)

* `H` (value: `"H"`)

* `U` (value: `"U"`)

* `S` (value: `"S"`)




