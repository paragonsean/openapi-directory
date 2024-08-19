

# IEdmNavigationProperty


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containsTarget** | **Boolean** |  |  [optional] [readonly] |
|**declaringType** | [**IEdmStructuredType**](IEdmStructuredType.md) |  |  [optional] |
|**name** | **String** |  |  [optional] [readonly] |
|**onDelete** | [**OnDeleteEnum**](#OnDeleteEnum) |  |  [optional] [readonly] |
|**partner** | [**IEdmNavigationProperty**](IEdmNavigationProperty.md) |  |  [optional] |
|**propertyKind** | [**PropertyKindEnum**](#PropertyKindEnum) |  |  [optional] [readonly] |
|**referentialConstraint** | [**IEdmReferentialConstraint**](IEdmReferentialConstraint.md) |  |  [optional] |
|**type** | [**IEdmTypeReference**](IEdmTypeReference.md) |  |  [optional] |



## Enum: OnDeleteEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| CASCADE | &quot;Cascade&quot; |



## Enum: PropertyKindEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| STRUCTURAL | &quot;Structural&quot; |
| NAVIGATION | &quot;Navigation&quot; |



