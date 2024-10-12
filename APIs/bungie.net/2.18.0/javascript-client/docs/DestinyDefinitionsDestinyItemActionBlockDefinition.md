# BungieNetApi.DestinyDefinitionsDestinyItemActionBlockDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionTypeLabel** | **String** | The internal identifier for the action. | [optional] 
**consumeEntireStack** | **Boolean** | If true, the entire stack is deleted when the action completes. | [optional] 
**deleteOnAction** | **Boolean** | If true, the item is deleted when the action completes. | [optional] 
**isPositive** | **Boolean** | The content has this property, however it&#39;s not entirely clear how it is used. | [optional] 
**overlayIcon** | **String** | The icon associated with the overlay screen for the action, if any. | [optional] 
**overlayScreenName** | **String** | If the action has an overlay screen associated with it, this is the name of that screen. Unfortunately, we cannot return the screen&#39;s data itself. | [optional] 
**progressionRewards** | [**[DestinyDefinitionsDestinyProgressionRewardDefinition]**](DestinyDefinitionsDestinyProgressionRewardDefinition.md) | If performing this action earns you Progression, this is the list of progressions and values granted for those progressions by performing this action. | [optional] 
**requiredCooldownHash** | **Number** | The identifier hash for the Cooldown associated with this action. We have not pulled this data yet for you to have more data to use for cooldowns. | [optional] 
**requiredCooldownSeconds** | **Number** | The number of seconds to delay before allowing this action to be performed again. | [optional] 
**requiredItems** | [**[DestinyDefinitionsDestinyItemActionRequiredItemDefinition]**](DestinyDefinitionsDestinyItemActionRequiredItemDefinition.md) | If the action requires other items to exist or be destroyed, this is the list of those items and requirements. | [optional] 
**requiredLocation** | **String** | Theoretically, an item could have a localized string for a hint about the location in which the action should be performed. In practice, no items yet have this property. | [optional] 
**useOnAcquire** | **Boolean** | If true, this action will be performed as soon as you earn this item. Some rewards work this way, providing you a single item to pick up from a reward-granting vendor in-game and then immediately consuming itself to provide you multiple items. | [optional] 
**verbDescription** | **String** | Localized text describing the action being performed. | [optional] 
**verbName** | **String** | Localized text for the verb of the action being performed. | [optional] 


