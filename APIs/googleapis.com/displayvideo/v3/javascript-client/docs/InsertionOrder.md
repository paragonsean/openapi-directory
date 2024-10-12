# DisplayVideo360Api.InsertionOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiserId** | **String** | Output only. The unique ID of the advertiser the insertion order belongs to. | [optional] [readonly] 
**bidStrategy** | [**BiddingStrategy**](BiddingStrategy.md) |  | [optional] 
**budget** | [**InsertionOrderBudget**](InsertionOrderBudget.md) |  | [optional] 
**campaignId** | **String** | Required. Immutable. The unique ID of the campaign that the insertion order belongs to. | [optional] 
**displayName** | **String** | Required. The display name of the insertion order. Must be UTF-8 encoded with a maximum size of 240 bytes. | [optional] 
**entityStatus** | **String** | Required. Controls whether or not the insertion order can spend its budget and bid on inventory. * For CreateInsertionOrder method, only &#x60;ENTITY_STATUS_DRAFT&#x60; is allowed. To activate an insertion order, use UpdateInsertionOrder method and update the status to &#x60;ENTITY_STATUS_ACTIVE&#x60; after creation. * An insertion order cannot be changed back to &#x60;ENTITY_STATUS_DRAFT&#x60; status from any other status. * An insertion order cannot be set to &#x60;ENTITY_STATUS_ACTIVE&#x60; if its parent campaign is not active. | [optional] 
**frequencyCap** | [**FrequencyCap**](FrequencyCap.md) |  | [optional] 
**insertionOrderId** | **String** | Output only. The unique ID of the insertion order. Assigned by the system. | [optional] [readonly] 
**insertionOrderType** | **String** | The type of insertion order. If this field is unspecified in creation, the value defaults to &#x60;RTB&#x60;. | [optional] 
**integrationDetails** | [**IntegrationDetails**](IntegrationDetails.md) |  | [optional] 
**kpi** | [**Kpi**](Kpi.md) |  | [optional] 
**name** | **String** | Output only. The resource name of the insertion order. | [optional] [readonly] 
**pacing** | [**Pacing**](Pacing.md) |  | [optional] 
**partnerCosts** | [**[PartnerCost]**](PartnerCost.md) | The partner costs associated with the insertion order. If absent or empty in CreateInsertionOrder method, the newly created insertion order will inherit partner costs from the partner settings. | [optional] 
**reservationType** | **String** | Output only. The reservation type of the insertion order. | [optional] [readonly] 
**updateTime** | **String** | Output only. The timestamp when the insertion order was last updated. Assigned by the system. | [optional] [readonly] 



## Enum: EntityStatusEnum


* `UNSPECIFIED` (value: `"ENTITY_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ENTITY_STATUS_ACTIVE"`)

* `ARCHIVED` (value: `"ENTITY_STATUS_ARCHIVED"`)

* `DRAFT` (value: `"ENTITY_STATUS_DRAFT"`)

* `PAUSED` (value: `"ENTITY_STATUS_PAUSED"`)

* `SCHEDULED_FOR_DELETION` (value: `"ENTITY_STATUS_SCHEDULED_FOR_DELETION"`)





## Enum: InsertionOrderTypeEnum


* `INSERTION_ORDER_TYPE_UNSPECIFIED` (value: `"INSERTION_ORDER_TYPE_UNSPECIFIED"`)

* `RTB` (value: `"RTB"`)

* `OVER_THE_TOP` (value: `"OVER_THE_TOP"`)





## Enum: ReservationTypeEnum


* `UNSPECIFIED` (value: `"RESERVATION_TYPE_UNSPECIFIED"`)

* `NOT_GUARANTEED` (value: `"RESERVATION_TYPE_NOT_GUARANTEED"`)

* `PROGRAMMATIC_GUARANTEED` (value: `"RESERVATION_TYPE_PROGRAMMATIC_GUARANTEED"`)

* `TAG_GUARANTEED` (value: `"RESERVATION_TYPE_TAG_GUARANTEED"`)

* `PETRA_VIRAL` (value: `"RESERVATION_TYPE_PETRA_VIRAL"`)

* `INSTANT_RESERVE` (value: `"RESERVATION_TYPE_INSTANT_RESERVE"`)




