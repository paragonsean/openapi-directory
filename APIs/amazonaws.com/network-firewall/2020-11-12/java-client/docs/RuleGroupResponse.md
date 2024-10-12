

# RuleGroupResponse

The high-level properties of a rule group. This, along with the <a>RuleGroup</a>, define the rule group. You can retrieve all objects for a rule group by calling <a>DescribeRuleGroup</a>. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ruleGroupArn** | [**String**](String.md) |  |  |
|**ruleGroupName** | [**String**](String.md) |  |  |
|**ruleGroupId** | [**String**](String.md) |  |  |
|**description** | [**String**](String.md) |  |  [optional] |
|**type** | [**RuleGroupType**](RuleGroupType.md) |  |  [optional] |
|**capacity** | [**Integer**](Integer.md) |  |  [optional] |
|**ruleGroupStatus** | [**ResourceStatus**](ResourceStatus.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**consumedCapacity** | [**Integer**](Integer.md) |  |  [optional] |
|**numberOfAssociations** | [**Integer**](Integer.md) |  |  [optional] |
|**encryptionConfiguration** | [**RuleGroupResponseEncryptionConfiguration**](RuleGroupResponseEncryptionConfiguration.md) |  |  [optional] |
|**sourceMetadata** | [**RuleGroupResponseSourceMetadata**](RuleGroupResponseSourceMetadata.md) |  |  [optional] |
|**snsTopic** | [**String**](String.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



