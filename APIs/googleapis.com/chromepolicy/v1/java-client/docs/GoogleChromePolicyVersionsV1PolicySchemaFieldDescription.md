

# GoogleChromePolicyVersionsV1PolicySchemaFieldDescription

Provides detailed information for a particular field that is part of a PolicySchema.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultValue** | **Object** | Output only. Client default if the policy is unset. |  [optional] [readonly] |
|**description** | **String** | Deprecated. Use name and field_description instead. The description for the field. |  [optional] |
|**field** | **String** | Output only. The name of the field for associated with this description. |  [optional] [readonly] |
|**fieldConstraints** | [**GoogleChromePolicyVersionsV1FieldConstraints**](GoogleChromePolicyVersionsV1FieldConstraints.md) |  |  [optional] |
|**fieldDependencies** | [**List&lt;GoogleChromePolicyVersionsV1PolicySchemaFieldDependencies&gt;**](GoogleChromePolicyVersionsV1PolicySchemaFieldDependencies.md) | Output only. Provides a list of fields and values. At least one of the fields must have the corresponding value in order for this field to be allowed to be set. |  [optional] [readonly] |
|**fieldDescription** | **String** | Output only. The description of the field. |  [optional] [readonly] |
|**inputConstraint** | **String** | Output only. Any input constraints associated on the values for the field. |  [optional] [readonly] |
|**knownValueDescriptions** | [**List&lt;GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescription&gt;**](GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescription.md) | Output only. If the field has a set of known values, this field will provide a description for these values. |  [optional] [readonly] |
|**name** | **String** | Output only. The name of the field. |  [optional] [readonly] |
|**nestedFieldDescriptions** | [**List&lt;GoogleChromePolicyVersionsV1PolicySchemaFieldDescription&gt;**](GoogleChromePolicyVersionsV1PolicySchemaFieldDescription.md) | Output only. Provides the description of the fields nested in this field, if the field is a message type that defines multiple fields. Fields are suggested to be displayed by the ordering in this list, not by field number. |  [optional] [readonly] |
|**requiredItems** | [**List&lt;GoogleChromePolicyVersionsV1PolicySchemaRequiredItems&gt;**](GoogleChromePolicyVersionsV1PolicySchemaRequiredItems.md) | Output only. Provides a list of fields that are required to be set if this field has a certain value. |  [optional] [readonly] |



