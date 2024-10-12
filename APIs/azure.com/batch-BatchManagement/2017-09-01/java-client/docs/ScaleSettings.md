

# ScaleSettings

Defines the desired size of the pool. This can either be 'fixedScale' where the requested targetDedicatedNodes is specified, or 'autoScale' which defines a formula which is periodically reevaluated. If this property is not specified, the pool will have a fixed scale with 0 targetDedicatedNodes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoScale** | [**AutoScaleSettings**](AutoScaleSettings.md) |  |  [optional] |
|**fixedScale** | [**FixedScaleSettings**](FixedScaleSettings.md) |  |  [optional] |



