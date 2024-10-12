# GoogleWorkspaceAlertCenterApi.AccessApproval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**justificationReason** | **[String]** | Justification for data access based on justification enums. | [optional] 
**officeLocation** | **String** | Office location of Google staff requesting access such as \&quot;US\&quot;. | [optional] 
**products** | **[String]** | Products within scope of the Access Approvals request. | [optional] 
**requestId** | **String** | ID of the Access Approvals request. This is a helpful field when requesting support from Google. | [optional] 
**scope** | **String** | Scope of access, also known as a resource. This is further narrowed down by the product field. | [optional] 
**tickets** | [**[SupportTicket]**](SupportTicket.md) | Support tickets related to this Access Approvals request. Populated if there is an associated case number. | [optional] 



## Enum: [JustificationReasonEnum]


* `JUSTIFICATION_UNSPECIFIED` (value: `"JUSTIFICATION_UNSPECIFIED"`)

* `CUSTOMER_INITIATED_SUPPORT` (value: `"CUSTOMER_INITIATED_SUPPORT"`)

* `GOOGLE_INITIATED_REVIEW` (value: `"GOOGLE_INITIATED_REVIEW"`)

* `GOOGLE_INITIATED_SERVICE` (value: `"GOOGLE_INITIATED_SERVICE"`)

* `THIRD_PARTY_DATA_REQUEST` (value: `"THIRD_PARTY_DATA_REQUEST"`)

* `GOOGLE_RESPONSE_TO_PRODUCTION_ALERT` (value: `"GOOGLE_RESPONSE_TO_PRODUCTION_ALERT"`)




