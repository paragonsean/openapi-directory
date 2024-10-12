

# ApplicationDefinitionProperties

The managed application definition properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifacts** | [**List&lt;ApplicationArtifact&gt;**](ApplicationArtifact.md) | The collection of managed application artifacts. The portal will use the files specified as artifacts to construct the user experience of creating a managed application from a managed application definition. |  [optional] |
|**authorizations** | [**List&lt;ApplicationProviderAuthorization&gt;**](ApplicationProviderAuthorization.md) | The managed application provider authorizations. |  |
|**createUiDefinition** | **Object** | The createUiDefinition json for the backing template with Microsoft.Solutions/applications resource. It can be a JObject or well-formed JSON string. |  [optional] |
|**description** | **String** | The managed application definition description. |  [optional] |
|**displayName** | **String** | The managed application definition display name. |  [optional] |
|**isEnabled** | **String** | A value indicating whether the package is enabled or not. |  [optional] |
|**lockLevel** | **ApplicationLockLevel** |  |  |
|**mainTemplate** | **Object** | The inline main template json which has resources to be provisioned. It can be a JObject or well-formed JSON string. |  [optional] |
|**packageFileUri** | **String** | The managed application definition package file Uri. Use this element |  [optional] |



