# ChromePolicyApi.GoogleChromePolicyVersionsV1PolicySchemaFieldDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultValue** | **Object** | Output only. Client default if the policy is unset. | [optional] [readonly] 
**description** | **String** | Deprecated. Use name and field_description instead. The description for the field. | [optional] 
**field** | **String** | Output only. The name of the field for associated with this description. | [optional] [readonly] 
**fieldConstraints** | [**GoogleChromePolicyVersionsV1FieldConstraints**](GoogleChromePolicyVersionsV1FieldConstraints.md) |  | [optional] 
**fieldDependencies** | [**[GoogleChromePolicyVersionsV1PolicySchemaFieldDependencies]**](GoogleChromePolicyVersionsV1PolicySchemaFieldDependencies.md) | Output only. Provides a list of fields and values. At least one of the fields must have the corresponding value in order for this field to be allowed to be set. | [optional] [readonly] 
**fieldDescription** | **String** | Output only. The description of the field. | [optional] [readonly] 
**inputConstraint** | **String** | Output only. Any input constraints associated on the values for the field. | [optional] [readonly] 
**knownValueDescriptions** | [**[GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescription]**](GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescription.md) | Output only. If the field has a set of known values, this field will provide a description for these values. | [optional] [readonly] 
**name** | **String** | Output only. The name of the field. | [optional] [readonly] 
**nestedFieldDescriptions** | [**[GoogleChromePolicyVersionsV1PolicySchemaFieldDescription]**](GoogleChromePolicyVersionsV1PolicySchemaFieldDescription.md) | Output only. Provides the description of the fields nested in this field, if the field is a message type that defines multiple fields. Fields are suggested to be displayed by the ordering in this list, not by field number. | [optional] [readonly] 
**requiredItems** | [**[GoogleChromePolicyVersionsV1PolicySchemaRequiredItems]**](GoogleChromePolicyVersionsV1PolicySchemaRequiredItems.md) | Output only. Provides a list of fields that are required to be set if this field has a certain value. | [optional] [readonly] 


