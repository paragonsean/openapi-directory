

# Macro

Represents a Google Tag Manager Macro.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**containerId** | **String** | GTM Container ID. |  [optional] |
|**disablingRuleId** | **List&lt;String&gt;** | For mobile containers only: A list of rule IDs for disabling conditional macros; the macro is enabled if one of the enabling rules is true while all the disabling rules are false. Treated as an unordered set. @mutable tagmanager.accounts.containers.macros.create @mutable tagmanager.accounts.containers.macros.update |  [optional] |
|**enablingRuleId** | **List&lt;String&gt;** | For mobile containers only: A list of rule IDs for enabling conditional macros; the macro is enabled if one of the enabling rules is true while all the disabling rules are false. Treated as an unordered set. @mutable tagmanager.accounts.containers.macros.create @mutable tagmanager.accounts.containers.macros.update |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Macro as computed at storage time. This value is recomputed whenever the macro is modified. |  [optional] |
|**macroId** | **String** | The Macro ID uniquely identifies the GTM Macro. |  [optional] |
|**name** | **String** | Macro display name. @mutable tagmanager.accounts.containers.macros.create @mutable tagmanager.accounts.containers.macros.update |  [optional] |
|**notes** | **String** | User notes on how to apply this macro in the container. @mutable tagmanager.accounts.containers.macros.create @mutable tagmanager.accounts.containers.macros.update |  [optional] |
|**parameter** | [**List&lt;Parameter&gt;**](Parameter.md) | The macro&#39;s parameters. @mutable tagmanager.accounts.containers.macros.create @mutable tagmanager.accounts.containers.macros.update |  [optional] |
|**parentFolderId** | **String** | Parent folder id. |  [optional] |
|**scheduleEndMs** | **String** | The end timestamp in milliseconds to schedule a macro. @mutable tagmanager.accounts.containers.macros.create @mutable tagmanager.accounts.containers.macros.update |  [optional] |
|**scheduleStartMs** | **String** | The start timestamp in milliseconds to schedule a macro. @mutable tagmanager.accounts.containers.macros.create @mutable tagmanager.accounts.containers.macros.update |  [optional] |
|**type** | **String** | GTM Macro Type. @mutable tagmanager.accounts.containers.macros.create @mutable tagmanager.accounts.containers.macros.update |  [optional] |



