

# PromotionsEntityCost

Cost of the promotion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currency** | **String** | Currency of the unit_cost (&lt;a href&#x3D;&#39;https://en.wikipedia.org/wiki/ISO_4217#Active_codes&#39;&gt;ISO 4212 alphabetic code&lt;/a&gt;). |  [optional] |
|**exchange** | **String** | What was offered in exchange of the promotion. |  [optional] |
|**quantity** | **Float** | Quantity of the promotion (see unit_cost). |  [optional] |
|**state** | [**PromotionsEntityCostState**](PromotionsEntityCostState.md) |  |  [optional] |
|**type** | [**PromotionsEntityCostType**](PromotionsEntityCostType.md) |  |  |
|**unitCost** | **Float** | Unit cost of the promotion. The total cost of the promotion can be calculated with: quantity × unit_cost. |  [optional] |
|**valorizedQuantity** | **Float** | Valorized quantity of the promotion (see valorized_unit_cost). *This field may be omitted according to the customer configuration.* |  [optional] |
|**valorizedUnitCost** | **Float** | Valorized unit cost of the promotion. The total valorized cost of the promotion can be calculated with: valorized_quantity × valorized_unit_cost. *This field may be omitted according to the customer configuration.* |  [optional] |



