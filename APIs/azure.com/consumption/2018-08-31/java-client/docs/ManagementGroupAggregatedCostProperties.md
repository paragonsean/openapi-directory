

# ManagementGroupAggregatedCostProperties

The properties of the Management Group Aggregated Cost.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureCharges** | **BigDecimal** | Azure Charges. |  [optional] [readonly] |
|**billingPeriodId** | **String** | The id of the billing period resource that the aggregated cost belongs to. |  [optional] [readonly] |
|**chargesBilledSeparately** | **BigDecimal** | Charges Billed Separately. |  [optional] [readonly] |
|**children** | [**List&lt;ManagementGroupAggregatedCostResult&gt;**](ManagementGroupAggregatedCostResult.md) | Children of a management group |  [optional] |
|**currency** | **String** | The ISO currency in which the meter is charged, for example, USD. |  [optional] [readonly] |
|**marketplaceCharges** | **BigDecimal** | Marketplace Charges. |  [optional] [readonly] |
|**usageEnd** | **OffsetDateTime** | The end of the date time range covered by the aggregated cost. |  [optional] [readonly] |
|**usageStart** | **OffsetDateTime** | The start of the date time range covered by aggregated cost. |  [optional] [readonly] |



