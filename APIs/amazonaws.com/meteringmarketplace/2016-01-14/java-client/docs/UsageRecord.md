

# UsageRecord

<p>A <code>UsageRecord</code> indicates a quantity of usage for a given product, customer, dimension and time.</p> <p>Multiple requests with the same <code>UsageRecords</code> as input will be de-duplicated to prevent double charges.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**timestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**customerIdentifier** | [**String**](String.md) |  |  |
|**dimension** | [**String**](String.md) |  |  |
|**quantity** | [**Integer**](Integer.md) |  |  [optional] |
|**usageAllocations** | [**List**](List.md) |  |  [optional] |



