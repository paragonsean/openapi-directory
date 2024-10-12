# Pims.PromotionsEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliedTo** | [**[PromotionsEntityAppliedToInner]**](PromotionsEntityAppliedToInner.md) | List of events and/or series where the promotion is applied. A promotion can be applied on several events, and its costs can be split between those events. | 
**comments** | **String** | Comments on the promotion. | 
**cost** | [**PromotionsEntityCost**](PromotionsEntityCost.md) |  | 
**endDate** | **Date** | Date the promotion ends. (If null, has the same value as start_date.) | 
**file** | **String** | File associated to the promotion. | [optional] 
**id** | **Number** | Unique ID of the promotion. | 
**label** | **String** | Label of the promotion. | 
**startDate** | **Date** | Date the promotion begins. | 
**supplier** | [**PromotionsEntitySupplier**](PromotionsEntitySupplier.md) |  | 
**type** | [**PromotionsEntityType**](PromotionsEntityType.md) |  | 


