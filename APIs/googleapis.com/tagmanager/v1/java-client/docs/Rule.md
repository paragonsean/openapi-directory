

# Rule

Represents a Google Tag Manager Rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**condition** | [**List&lt;Condition&gt;**](Condition.md) | The list of conditions that make up this rule (implicit AND between them). @mutable tagmanager.accounts.containers.rules.create @mutable tagmanager.accounts.containers.rules.update |  [optional] |
|**containerId** | **String** | GTM Container ID. |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Rule as computed at storage time. This value is recomputed whenever the rule is modified. |  [optional] |
|**name** | **String** | Rule display name. @mutable tagmanager.accounts.containers.rules.create @mutable tagmanager.accounts.containers.rules.update |  [optional] |
|**notes** | **String** | User notes on how to apply this rule in the container. @mutable tagmanager.accounts.containers.rules.create @mutable tagmanager.accounts.containers.rules.update |  [optional] |
|**ruleId** | **String** | The Rule ID uniquely identifies the GTM Rule. |  [optional] |



