

# SchemaAttributeType

<p>A list of the user attributes and their properties in your user pool. The attribute schema contains standard attributes, custom attributes with a <code>custom:</code> prefix, and developer attributes with a <code>dev:</code> prefix. For more information, see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html\">User pool attributes</a>.</p> <p>Developer-only attributes are a legacy feature of user pools, are read-only to all app clients. You can create and update developer-only attributes only with IAM-authenticated API operations. Use app client read/write permissions instead.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**attributeDataType** | [**AttributeDataType**](AttributeDataType.md) |  |  [optional] |
|**developerOnlyAttribute** | [**Boolean**](Boolean.md) |  |  [optional] |
|**mutable** | [**Boolean**](Boolean.md) |  |  [optional] |
|**required** | [**Boolean**](Boolean.md) |  |  [optional] |
|**numberAttributeConstraints** | [**SchemaAttributeTypeNumberAttributeConstraints**](SchemaAttributeTypeNumberAttributeConstraints.md) |  |  [optional] |
|**stringAttributeConstraints** | [**SchemaAttributeTypeStringAttributeConstraints**](SchemaAttributeTypeStringAttributeConstraints.md) |  |  [optional] |



