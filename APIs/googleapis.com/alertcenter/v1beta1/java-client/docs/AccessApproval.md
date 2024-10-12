

# AccessApproval

Alert that is triggered when Google support requests to access customer data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**justificationReason** | [**List&lt;JustificationReasonEnum&gt;**](#List&lt;JustificationReasonEnum&gt;) | Justification for data access based on justification enums. |  [optional] |
|**officeLocation** | **String** | Office location of Google staff requesting access such as \&quot;US\&quot;. |  [optional] |
|**products** | **List&lt;String&gt;** | Products within scope of the Access Approvals request. |  [optional] |
|**requestId** | **String** | ID of the Access Approvals request. This is a helpful field when requesting support from Google. |  [optional] |
|**scope** | **String** | Scope of access, also known as a resource. This is further narrowed down by the product field. |  [optional] |
|**tickets** | [**List&lt;SupportTicket&gt;**](SupportTicket.md) | Support tickets related to this Access Approvals request. Populated if there is an associated case number. |  [optional] |



## Enum: List&lt;JustificationReasonEnum&gt;

| Name | Value |
|---- | -----|
| JUSTIFICATION_UNSPECIFIED | &quot;JUSTIFICATION_UNSPECIFIED&quot; |
| CUSTOMER_INITIATED_SUPPORT | &quot;CUSTOMER_INITIATED_SUPPORT&quot; |
| GOOGLE_INITIATED_REVIEW | &quot;GOOGLE_INITIATED_REVIEW&quot; |
| GOOGLE_INITIATED_SERVICE | &quot;GOOGLE_INITIATED_SERVICE&quot; |
| THIRD_PARTY_DATA_REQUEST | &quot;THIRD_PARTY_DATA_REQUEST&quot; |
| GOOGLE_RESPONSE_TO_PRODUCTION_ALERT | &quot;GOOGLE_RESPONSE_TO_PRODUCTION_ALERT&quot; |



