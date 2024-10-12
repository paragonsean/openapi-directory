

# DerivedSource

Specification of one of the bundles produced as a result of splitting a Source (e.g. when executing a SourceSplitRequest, or when splitting an active task using WorkItemStatus.dynamic_source_split), relative to the source being split.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**derivationMode** | [**DerivationModeEnum**](#DerivationModeEnum) | What source to base the produced source on (if any). |  [optional] |
|**source** | [**Source**](Source.md) |  |  [optional] |



## Enum: DerivationModeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;SOURCE_DERIVATION_MODE_UNKNOWN&quot; |
| INDEPENDENT | &quot;SOURCE_DERIVATION_MODE_INDEPENDENT&quot; |
| CHILD_OF_CURRENT | &quot;SOURCE_DERIVATION_MODE_CHILD_OF_CURRENT&quot; |
| SIBLING_OF_CURRENT | &quot;SOURCE_DERIVATION_MODE_SIBLING_OF_CURRENT&quot; |



