

# SlsaCompleteness

Indicates that the builder claims certain fields in this message to be complete.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arguments** | **Boolean** | If true, the builder claims that recipe.arguments is complete, meaning that all external inputs are properly captured in the recipe. |  [optional] |
|**environment** | **Boolean** | If true, the builder claims that recipe.environment is claimed to be complete. |  [optional] |
|**materials** | **Boolean** | If true, the builder claims that materials are complete, usually through some controls to prevent network access. Sometimes called \&quot;hermetic\&quot;. |  [optional] |



