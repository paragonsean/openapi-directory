# AmazonAppConfig.CreateExtensionAssociationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extensionIdentifier** | **String** | The name, the ID, or the Amazon Resource Name (ARN) of the extension. | 
**extensionVersionNumber** | **Number** | The version number of the extension. If not specified, AppConfig uses the maximum version of the extension. | [optional] 
**resourceIdentifier** | **String** | The ARN of an application, configuration profile, or environment. | 
**parameters** | **{String: String}** | The parameter names and values defined in the extensions. Extension parameters marked &lt;code&gt;Required&lt;/code&gt; must be entered for this field. | [optional] 
**tags** | **{String: String}** | Adds one or more tags for the specified extension association. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.  | [optional] 


