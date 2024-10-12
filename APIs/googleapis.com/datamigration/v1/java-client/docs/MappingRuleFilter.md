

# MappingRuleFilter

A filter defining the entities that a mapping rule should be applied to. When more than one field is specified, the rule is applied only to entities which match all the fields.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entities** | **List&lt;String&gt;** | Optional. The rule should be applied to specific entities defined by their fully qualified names. |  [optional] |
|**entityNameContains** | **String** | Optional. The rule should be applied to entities whose non-qualified name contains the given string. |  [optional] |
|**entityNamePrefix** | **String** | Optional. The rule should be applied to entities whose non-qualified name starts with the given prefix. |  [optional] |
|**entityNameSuffix** | **String** | Optional. The rule should be applied to entities whose non-qualified name ends with the given suffix. |  [optional] |
|**parentEntity** | **String** | Optional. The rule should be applied to entities whose parent entity (fully qualified name) matches the given value. For example, if the rule applies to a table entity, the expected value should be a schema (schema). If the rule applies to a column or index entity, the expected value can be either a schema (schema) or a table (schema.table) |  [optional] |



