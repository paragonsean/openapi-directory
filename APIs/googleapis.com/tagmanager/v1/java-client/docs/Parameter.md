

# Parameter

Represents a Google Tag Manager Parameter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The named key that uniquely identifies a parameter. Required for top-level parameters, as well as map values. Ignored for list values. @mutable tagmanager.accounts.containers.variables.create @mutable tagmanager.accounts.containers.variables.update @mutable tagmanager.accounts.containers.triggers.create @mutable tagmanager.accounts.containers.triggers.update @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**_list** | [**List&lt;Parameter&gt;**](Parameter.md) | This list parameter&#39;s parameters (keys will be ignored). @mutable tagmanager.accounts.containers.variables.create @mutable tagmanager.accounts.containers.variables.update @mutable tagmanager.accounts.containers.triggers.create @mutable tagmanager.accounts.containers.triggers.update @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**map** | [**List&lt;Parameter&gt;**](Parameter.md) | This map parameter&#39;s parameters (must have keys; keys must be unique). @mutable tagmanager.accounts.containers.variables.create @mutable tagmanager.accounts.containers.variables.update @mutable tagmanager.accounts.containers.triggers.create @mutable tagmanager.accounts.containers.triggers.update @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The parameter type. Valid values are: - boolean: The value represents a boolean, represented as &#39;true&#39; or &#39;false&#39; - integer: The value represents a 64-bit signed integer value, in base 10 - list: A list of parameters should be specified - map: A map of parameters should be specified - template: The value represents any text; this can include variable references (even variable references that might return non-string types) - trigger_reference: The value represents a trigger, represented as the trigger id - tag_reference: The value represents a tag, represented as the tag name @mutable tagmanager.accounts.containers.variables.create @mutable tagmanager.accounts.containers.variables.update @mutable tagmanager.accounts.containers.triggers.create @mutable tagmanager.accounts.containers.triggers.update @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**value** | **String** | A parameter&#39;s value (may contain variable references such as \&quot;{{myVariable}}\&quot;) as appropriate to the specified type. @mutable tagmanager.accounts.containers.variables.create @mutable tagmanager.accounts.containers.variables.update @mutable tagmanager.accounts.containers.triggers.create @mutable tagmanager.accounts.containers.triggers.update @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TEMPLATE | &quot;template&quot; |
| INTEGER | &quot;integer&quot; |
| BOOLEAN | &quot;boolean&quot; |
| LIST | &quot;list&quot; |
| MAP | &quot;map&quot; |
| TRIGGER_REFERENCE | &quot;triggerReference&quot; |
| TAG_REFERENCE | &quot;tagReference&quot; |



