

# ReportingReceivershipLitigationModel

Helper Model - Litigation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closedLitigationDate** | **OffsetDateTime** | Closed Litigation Date |  [optional] |
|**closedLitigationReason** | [**ClosedLitigationReasonEnum**](#ClosedLitigationReasonEnum) | Closed Litigation Reason |  [optional] |
|**compiledBySolicitorID** | **String** | Compiled By Solicitor ID (SalesSolicitor) |  [optional] |
|**displayCompiledBySolicitor** | **String** | Display Compiled By Solicitor |  [optional] |
|**evictionDate** | **OffsetDateTime** | Eviction Date |  [optional] |
|**evictionOutcome** | [**EvictionOutcomeEnum**](#EvictionOutcomeEnum) | Eviction Outcome |  [optional] |
|**extraNotes** | **String** | Extra Notes |  [optional] |
|**hearingDate** | **OffsetDateTime** | Hearing Date |  [optional] |
|**hearingOutcome** | **String** | Hearing Outcome |  [optional] |
|**litigationType** | **String** | Litigation Type |  [optional] |
|**noticeExpiryDate** | **OffsetDateTime** | Notice Expiry Date |  [optional] |
|**noticeServedDate** | **OffsetDateTime** | Notice Served Date |  [optional] |
|**proceedingsIssuedDate** | **OffsetDateTime** | Proceedings Issued Date |  [optional] |



## Enum: ClosedLitigationReasonEnum

| Name | Value |
|---- | -----|
| POSSESSION_OBTAINED | &quot;PossessionObtained&quot; |
| TENANT_VACATED | &quot;TenantVacated&quot; |
| LITIGATION_CANCELLED | &quot;LitigationCancelled&quot; |
| OTHER | &quot;Other&quot; |



## Enum: EvictionOutcomeEnum

| Name | Value |
|---- | -----|
| EVICTION_COMPLETE | &quot;EvictionComplete&quot; |
| EVICTION_CANCELLED | &quot;EvictionCancelled&quot; |
| OTHER | &quot;Other&quot; |



