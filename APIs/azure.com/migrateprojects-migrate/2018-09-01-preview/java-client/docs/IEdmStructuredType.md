

# IEdmStructuredType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseType** | [**IEdmStructuredType**](IEdmStructuredType.md) |  |  [optional] |
|**declaredProperties** | [**List&lt;IEdmProperty&gt;**](IEdmProperty.md) |  |  [optional] [readonly] |
|**isAbstract** | **Boolean** |  |  [optional] [readonly] |
|**isOpen** | **Boolean** |  |  [optional] [readonly] |
|**typeKind** | [**TypeKindEnum**](#TypeKindEnum) |  |  [optional] [readonly] |



## Enum: TypeKindEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| PRIMITIVE | &quot;Primitive&quot; |
| ENTITY | &quot;Entity&quot; |
| COMPLEX | &quot;Complex&quot; |
| COLLECTION | &quot;Collection&quot; |
| ENTITY_REFERENCE | &quot;EntityReference&quot; |
| ENUM | &quot;Enum&quot; |
| TYPE_DEFINITION | &quot;TypeDefinition&quot; |
| UNTYPED | &quot;Untyped&quot; |
| PATH | &quot;Path&quot; |



