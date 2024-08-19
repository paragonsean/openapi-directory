

# CapacitySize

<p>Specifies the type and size of the endpoint capacity to activate for a blue/green deployment, a rolling deployment, or a rollback strategy. You can specify your batches as either instance count or the overall percentage or your fleet.</p> <p>For a rollback strategy, if you don't specify the fields in this object, or if you set the <code>Value</code> to 100%, then SageMaker uses a blue/green rollback strategy and rolls all traffic back to the blue fleet.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**CapacitySizeType**](CapacitySizeType.md) |  |  |
|**value** | [**Integer**](Integer.md) |  |  |



