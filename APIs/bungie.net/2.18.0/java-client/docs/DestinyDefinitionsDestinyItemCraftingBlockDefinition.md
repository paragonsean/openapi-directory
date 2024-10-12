

# DestinyDefinitionsDestinyItemCraftingBlockDefinition

If an item can have an action performed on it (like \"Dismantle\"), it will be defined here if you care.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseMaterialRequirements** | **Integer** | A reference to the base material requirements for crafting with this recipe. |  [optional] |
|**bonusPlugs** | [**List&lt;DestinyDefinitionsDestinyItemCraftingBlockBonusPlugDefinition&gt;**](DestinyDefinitionsDestinyItemCraftingBlockBonusPlugDefinition.md) | A list of &#39;bonus&#39; socket plugs that may be available if certain requirements are met. |  [optional] |
|**failedRequirementStrings** | **List&lt;String&gt;** |  |  [optional] |
|**outputItemHash** | **Integer** | A reference to the item definition that is created when crafting with this &#39;recipe&#39; item. |  [optional] |
|**requiredSocketTypeHashes** | **List&lt;Integer&gt;** | A list of socket type hashes that describes which sockets are required for crafting with this recipe. |  [optional] |



