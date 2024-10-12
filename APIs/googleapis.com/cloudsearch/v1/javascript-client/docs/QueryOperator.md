# CloudSearchApi.QueryOperator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Display name of the operator | [optional] 
**enumValues** | **[String]** | Potential list of values for the opeatror field. This field is only filled when we can safely enumerate all the possible values of this operator. | [optional] 
**greaterThanOperatorName** | **String** | Indicates the operator name that can be used to isolate the property using the greater-than operator. | [optional] 
**isFacetable** | **Boolean** | Can this operator be used to get facets. | [optional] 
**isRepeatable** | **Boolean** | Indicates if multiple values can be set for this property. | [optional] 
**isReturnable** | **Boolean** | Will the property associated with this facet be returned as part of search results. | [optional] 
**isSortable** | **Boolean** | Can this operator be used to sort results. | [optional] 
**isSuggestable** | **Boolean** | Can get suggestions for this field. | [optional] 
**lessThanOperatorName** | **String** | Indicates the operator name that can be used to isolate the property using the less-than operator. | [optional] 
**objectType** | **String** | The name of the object corresponding to the operator. This field is only filled for schema-specific operators, and is unset for common operators. | [optional] 
**operatorName** | **String** | The name of the operator. | [optional] 
**type** | **String** | The type of the operator. | [optional] 



## Enum: TypeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `INTEGER` (value: `"INTEGER"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `TIMESTAMP` (value: `"TIMESTAMP"`)

* `BOOLEAN` (value: `"BOOLEAN"`)

* `ENUM` (value: `"ENUM"`)

* `DATE` (value: `"DATE"`)

* `TEXT` (value: `"TEXT"`)

* `HTML` (value: `"HTML"`)




