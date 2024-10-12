

# CanonicalProfileDefinitionPropertiesInner

The definition of a canonical profile property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileName** | **String** | Profile name. |  [optional] |
|**profilePropertyName** | **String** | Property name of profile. |  [optional] |
|**rank** | **Integer** | The rank. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of canonical property value. |  [optional] |
|**value** | **String** | Value of the canonical property. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NUMERIC | &quot;Numeric&quot; |
| CATEGORICAL | &quot;Categorical&quot; |
| DERIVED_CATEGORICAL | &quot;DerivedCategorical&quot; |
| DERIVED_NUMERIC | &quot;DerivedNumeric&quot; |



