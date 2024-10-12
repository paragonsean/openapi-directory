# Pims.PromotionsEntityAppliedToInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventId** | **Number** | ID of the event the promotion applies to. This property is exclusive with &#39;series_id&#39;: if defined, then &#39;series_id&#39; will not be displayed. | [optional] 
**quantity** | **Number** | Quantity share of the promotion devoted to this event/series. | [optional] 
**seriesId** | **Number** | ID of the series the promotion applies to. This property is exclusive with &#39;event_id&#39;: if defined, then &#39;event_id&#39; will not be displayed. | [optional] 
**unitCost** | **Number** | Unit cost share of the promotion devoted to this event/series. The total cost of the share can be calculated with: quantity × unit_cost. *This field may be omitted according to the customer configuration.* | [optional] 
**valorizedQuantity** | **Number** | Valorized quantity share of the promotion devoted to this event/series. *This field may be omitted according to the customer configuration.* | [optional] 
**valorizedUnitCost** | **Number** | Valorized unit cost share of the promotion devoted to this event/series. The total valorized cost of the share can be calculated with: valorized_quantity × valorized_unit_cost. | [optional] 


