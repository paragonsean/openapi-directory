

# GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues

A message that holds specific allowed and denied values. This message can define specific values and subtrees of the Resource Manager resource hierarchy (`Organizations`, `Folders`, `Projects`) that are allowed or denied. This is achieved by using the `under:` and optional `is:` prefixes. The `under:` prefix is used to denote resource subtree values. The `is:` prefix is used to denote specific values, and is required only if the value contains a \":\". Values prefixed with \"is:\" are treated the same as values with no prefix. Ancestry subtrees must be in one of the following formats: - `projects/` (for example, `projects/tokyo-rain-123`) - `folders/` (for example, `folders/1234`) - `organizations/` (for example, `organizations/1234`) The `supports_under` field of the associated `Constraint` defines whether ancestry prefixes can be used.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedValues** | **List&lt;String&gt;** | List of values allowed at this resource. |  [optional] |
|**deniedValues** | **List&lt;String&gt;** | List of values denied at this resource. |  [optional] |



