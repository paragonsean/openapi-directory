

# FieldMetadata

Metadata about a field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**primary** | **Boolean** | Output only. True if the field is the primary field for all sources in the person. Each person will have at most one field with &#x60;primary&#x60; set to true. |  [optional] [readonly] |
|**source** | [**Source**](Source.md) |  |  [optional] |
|**sourcePrimary** | **Boolean** | True if the field is the primary field for the source. Each source must have at most one field with &#x60;source_primary&#x60; set to true. |  [optional] |
|**verified** | **Boolean** | Output only. True if the field is verified; false if the field is unverified. A verified field is typically a name, email address, phone number, or website that has been confirmed to be owned by the person. |  [optional] [readonly] |



