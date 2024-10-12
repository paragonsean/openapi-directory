

# EntryInfoProperty


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A human-readable description of the entry property |  |
|**sortable** | **Boolean** | Defines whether the entry property can be used for sorting with the \&quot;sort\&quot; parameter. If the entry listing endpoint supports sorting, this key MUST be present for sortable properties with value &#x60;true&#x60;. |  [optional] |
|**type** | **DataType** | The type of the property&#39;s value. This MUST be any of the types defined in the Data types section. For the purpose of compatibility with future versions of this specification, a client MUST accept values that are not &#x60;string&#x60; values specifying any of the OPTIMADE Data types, but MUST then also disregard the &#x60;type&#x60; field. Note, if the value is a nested type, only the outermost type should be reported. E.g., for the entry resource &#x60;structures&#x60;, the &#x60;species&#x60; property is defined as a list of dictionaries, hence its &#x60;type&#x60; value would be &#x60;list&#x60;. |  [optional] |
|**unit** | **String** | The physical unit of the entry property. This MUST be a valid representation of units according to version 2.1 of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html). It is RECOMMENDED that non-standard (non-SI) units are described in the description for the property. |  [optional] |



