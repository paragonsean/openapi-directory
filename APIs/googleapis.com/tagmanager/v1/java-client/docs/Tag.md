

# Tag

Represents a Google Tag Manager Tag.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**blockingRuleId** | **List&lt;String&gt;** | Blocking rule IDs. If any of the listed rules evaluate to true, the tag will not fire. @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**blockingTriggerId** | **List&lt;String&gt;** | Blocking trigger IDs. If any of the listed triggers evaluate to true, the tag will not fire. @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**containerId** | **String** | GTM Container ID. |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Tag as computed at storage time. This value is recomputed whenever the tag is modified. |  [optional] |
|**firingRuleId** | **List&lt;String&gt;** | Firing rule IDs. A tag will fire when any of the listed rules are true and all of its blockingRuleIds (if any specified) are false. @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**firingTriggerId** | **List&lt;String&gt;** | Firing trigger IDs. A tag will fire when any of the listed triggers are true and all of its blockingTriggerIds (if any specified) are false. @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**liveOnly** | **Boolean** | If set to true, this tag will only fire in the live environment (e.g. not in preview or debug mode). @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**name** | **String** | Tag display name. @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**notes** | **String** | User notes on how to apply this tag in the container. @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**parameter** | [**List&lt;Parameter&gt;**](Parameter.md) | The tag&#39;s parameters. @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**parentFolderId** | **String** | Parent folder id. |  [optional] |
|**paused** | **Boolean** | True if the tag is paused. @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**priority** | [**Parameter**](Parameter.md) |  |  [optional] |
|**scheduleEndMs** | **String** | The end timestamp in milliseconds to schedule a tag. @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**scheduleStartMs** | **String** | The start timestamp in milliseconds to schedule a tag. @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |
|**setupTag** | [**List&lt;SetupTag&gt;**](SetupTag.md) | The list of setup tags. Currently we only allow one. |  [optional] |
|**tagFiringOption** | [**TagFiringOptionEnum**](#TagFiringOptionEnum) | Option to fire this tag. |  [optional] |
|**tagId** | **String** | The Tag ID uniquely identifies the GTM Tag. |  [optional] |
|**teardownTag** | [**List&lt;TeardownTag&gt;**](TeardownTag.md) | The list of teardown tags. Currently we only allow one. |  [optional] |
|**type** | **String** | GTM Tag Type. @mutable tagmanager.accounts.containers.tags.create @mutable tagmanager.accounts.containers.tags.update |  [optional] |



## Enum: TagFiringOptionEnum

| Name | Value |
|---- | -----|
| UNLIMITED | &quot;unlimited&quot; |
| ONCE_PER_EVENT | &quot;oncePerEvent&quot; |
| ONCE_PER_LOAD | &quot;oncePerLoad&quot; |



