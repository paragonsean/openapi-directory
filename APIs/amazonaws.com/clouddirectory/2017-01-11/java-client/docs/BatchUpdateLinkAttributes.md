

# BatchUpdateLinkAttributes

Updates a given typed link’s attributes inside a <a>BatchRead</a> operation. Attributes to be updated must not contribute to the typed link’s identity, as defined by its <code>IdentityAttributeOrder</code>. For more information, see <a>UpdateLinkAttributes</a> and <a>BatchReadRequest$Operations</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**typedLinkSpecifier** | [**BatchGetLinkAttributesTypedLinkSpecifier**](BatchGetLinkAttributesTypedLinkSpecifier.md) |  |  |
|**attributeUpdates** | [**List**](List.md) |  |  |



