# TagManagerApi.Parameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isWeakReference** | **Boolean** | Whether or not a reference type parameter is strongly or weakly referenced. Only used by Transformations. @mutable tagmanager.accounts.containers.workspaces.transformations.create @mutable tagmanager.accounts.containers.workspaces.transformations.update | [optional] 
**key** | **String** | The named key that uniquely identifies a parameter. Required for top-level parameters, as well as map values. Ignored for list values. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update | [optional] 
**list** | [**[Parameter]**](Parameter.md) | This list parameter&#39;s parameters (keys will be ignored). @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update | [optional] 
**map** | [**[Parameter]**](Parameter.md) | This map parameter&#39;s parameters (must have keys; keys must be unique). @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update | [optional] 
**type** | **String** | The parameter type. Valid values are: - boolean: The value represents a boolean, represented as &#39;true&#39; or &#39;false&#39; - integer: The value represents a 64-bit signed integer value, in base 10 - list: A list of parameters should be specified - map: A map of parameters should be specified - template: The value represents any text; this can include variable references (even variable references that might return non-string types) - trigger_reference: The value represents a trigger, represented as the trigger id - tag_reference: The value represents a tag, represented as the tag name @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update | [optional] 
**value** | **String** | A parameter&#39;s value (may contain variable references such as \&quot;{{myVariable}}\&quot;) as appropriate to the specified type. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update | [optional] 



## Enum: TypeEnum


* `typeUnspecified` (value: `"typeUnspecified"`)

* `template` (value: `"template"`)

* `integer` (value: `"integer"`)

* `boolean` (value: `"boolean"`)

* `list` (value: `"list"`)

* `map` (value: `"map"`)

* `triggerReference` (value: `"triggerReference"`)

* `tagReference` (value: `"tagReference"`)




