

# InsertionOrder

A single insertion order.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** | Output only. The unique ID of the advertiser the insertion order belongs to. |  [optional] [readonly] |
|**bidStrategy** | [**BiddingStrategy**](BiddingStrategy.md) |  |  [optional] |
|**billableOutcome** | [**BillableOutcomeEnum**](#BillableOutcomeEnum) | Immutable. The billable outcome of the insertion order. Outcome based buying is deprecated. &#x60;BILLABLE_OUTCOME_PAY_PER_IMPRESSION&#x60; is the only valid value. |  [optional] |
|**budget** | [**InsertionOrderBudget**](InsertionOrderBudget.md) |  |  [optional] |
|**campaignId** | **String** | Required. Immutable. The unique ID of the campaign that the insertion order belongs to. |  [optional] |
|**displayName** | **String** | Required. The display name of the insertion order. Must be UTF-8 encoded with a maximum size of 240 bytes. |  [optional] |
|**entityStatus** | [**EntityStatusEnum**](#EntityStatusEnum) | Required. Controls whether or not the insertion order can spend its budget and bid on inventory. * For CreateInsertionOrder method, only &#x60;ENTITY_STATUS_DRAFT&#x60; is allowed. To activate an insertion order, use UpdateInsertionOrder method and update the status to &#x60;ENTITY_STATUS_ACTIVE&#x60; after creation. * An insertion order cannot be changed back to &#x60;ENTITY_STATUS_DRAFT&#x60; status from any other status. * An insertion order cannot be set to &#x60;ENTITY_STATUS_ACTIVE&#x60; if its parent campaign is not active. |  [optional] |
|**frequencyCap** | [**FrequencyCap**](FrequencyCap.md) |  |  [optional] |
|**insertionOrderId** | **String** | Output only. The unique ID of the insertion order. Assigned by the system. |  [optional] [readonly] |
|**insertionOrderType** | [**InsertionOrderTypeEnum**](#InsertionOrderTypeEnum) | The type of insertion order. If this field is unspecified in creation, the value defaults to &#x60;RTB&#x60;. |  [optional] |
|**integrationDetails** | [**IntegrationDetails**](IntegrationDetails.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name of the insertion order. |  [optional] [readonly] |
|**pacing** | [**Pacing**](Pacing.md) |  |  [optional] |
|**partnerCosts** | [**List&lt;PartnerCost&gt;**](PartnerCost.md) | The partner costs associated with the insertion order. If absent or empty in CreateInsertionOrder method, the newly created insertion order will inherit partner costs from the partner settings. |  [optional] |
|**performanceGoal** | [**PerformanceGoal**](PerformanceGoal.md) |  |  [optional] |
|**reservationType** | [**ReservationTypeEnum**](#ReservationTypeEnum) | Output only. The reservation type of the insertion order. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp when the insertion order was last updated. Assigned by the system. |  [optional] [readonly] |



## Enum: BillableOutcomeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;BILLABLE_OUTCOME_UNSPECIFIED&quot; |
| PAY_PER_IMPRESSION | &quot;BILLABLE_OUTCOME_PAY_PER_IMPRESSION&quot; |
| PAY_PER_CLICK | &quot;BILLABLE_OUTCOME_PAY_PER_CLICK&quot; |
| PAY_PER_VIEWABLE_IMPRESSION | &quot;BILLABLE_OUTCOME_PAY_PER_VIEWABLE_IMPRESSION&quot; |



## Enum: EntityStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENTITY_STATUS_UNSPECIFIED&quot; |
| ACTIVE | &quot;ENTITY_STATUS_ACTIVE&quot; |
| ARCHIVED | &quot;ENTITY_STATUS_ARCHIVED&quot; |
| DRAFT | &quot;ENTITY_STATUS_DRAFT&quot; |
| PAUSED | &quot;ENTITY_STATUS_PAUSED&quot; |
| SCHEDULED_FOR_DELETION | &quot;ENTITY_STATUS_SCHEDULED_FOR_DELETION&quot; |



## Enum: InsertionOrderTypeEnum

| Name | Value |
|---- | -----|
| INSERTION_ORDER_TYPE_UNSPECIFIED | &quot;INSERTION_ORDER_TYPE_UNSPECIFIED&quot; |
| RTB | &quot;RTB&quot; |
| OVER_THE_TOP | &quot;OVER_THE_TOP&quot; |



## Enum: ReservationTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;RESERVATION_TYPE_UNSPECIFIED&quot; |
| NOT_GUARANTEED | &quot;RESERVATION_TYPE_NOT_GUARANTEED&quot; |
| PROGRAMMATIC_GUARANTEED | &quot;RESERVATION_TYPE_PROGRAMMATIC_GUARANTEED&quot; |
| TAG_GUARANTEED | &quot;RESERVATION_TYPE_TAG_GUARANTEED&quot; |
| PETRA_VIRAL | &quot;RESERVATION_TYPE_PETRA_VIRAL&quot; |
| INSTANT_RESERVE | &quot;RESERVATION_TYPE_INSTANT_RESERVE&quot; |



