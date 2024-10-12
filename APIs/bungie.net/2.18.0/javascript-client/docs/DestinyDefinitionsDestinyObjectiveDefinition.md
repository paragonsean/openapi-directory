# BungieNetApi.DestinyDefinitionsDestinyObjectiveDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowNegativeValue** | **Boolean** | If true, the value is allowed to go negative. | [optional] 
**allowOvercompletion** | **Boolean** | If True, the progress will continue even beyond the point where the objective met its minimum completion requirements. Your UI will have to accommodate it. | [optional] 
**allowValueChangeWhenCompleted** | **Boolean** | If true, you can effectively \&quot;un-complete\&quot; this objective if you lose progress after crossing the completion threshold.   If False, once you complete the task it will remain completed forever by locking the value. | [optional] 
**completedValueStyle** | **Number** | The style to use when the objective is completed. | [optional] 
**completionValue** | **Number** | The value that the unlock value defined in unlockValueHash must reach in order for the objective to be considered Completed. Used in calculating progress and completion status. | [optional] 
**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) | Ideally, this should tell you what your task is. I&#39;m not going to lie to you though. Sometimes this doesn&#39;t have useful information at all. Which sucks, but there&#39;s nothing either of us can do about it. | [optional] 
**hash** | **Number** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**inProgressValueStyle** | **Number** | The style to use when the objective is still in progress. | [optional] 
**index** | **Number** | The index of the entity as it was found in the investment tables. | [optional] 
**isCountingDownward** | **Boolean** | If true, completion means having an unlock value less than or equal to the completionValue.  If False, completion means having an unlock value greater than or equal to the completionValue. | [optional] 
**locationHash** | **Number** | OPTIONAL: a hash identifier for the location at which this objective must be accomplished, if there is a location defined. Look up the DestinyLocationDefinition for this hash for that additional location info. | [optional] 
**minimumVisibilityThreshold** | **Number** | If nonzero, this is the minimum value at which the objective&#39;s progression should be shown. Otherwise, don&#39;t show it yet. | [optional] 
**perks** | [**DestinyDefinitionsDestinyObjectivePerkEntryDefinition**](DestinyDefinitionsDestinyObjectivePerkEntryDefinition.md) | If this objective enables Perks intrinsically, the conditions for that enabling are defined here. | [optional] 
**progressDescription** | **String** | Text to describe the progress bar. | [optional] 
**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | [optional] 
**scope** | **Number** | A shortcut for determining the most restrictive gating that this Objective is set to use. This includes both the dynamic determination of progress and of completion values. See the DestinyGatingScope enum&#39;s documentation for more details. | [optional] 
**showValueOnComplete** | **Boolean** | If True, you should continue showing the progression value in the UI after it&#39;s complete. I mean, we already do that in BNet anyways, but if you want to be better behaved than us you could honor this flag. | [optional] 
**stats** | [**DestinyDefinitionsDestinyObjectiveStatEntryDefinition**](DestinyDefinitionsDestinyObjectiveStatEntryDefinition.md) | If this objective enables modifications on a player&#39;s stats intrinsically, the conditions are defined here. | [optional] 
**uiLabel** | **String** | Objectives can have arbitrary UI-defined identifiers that define the style applied to objectives. For convenience, known UI labels will be defined in the uiStyle enum value. | [optional] 
**uiStyle** | **Number** | If the objective has a known UI label value, this property will represent it. | [optional] 
**valueStyle** | **Number** | The UI style applied to the objective. It&#39;s an enum, take a look at DestinyUnlockValueUIStyle for details of the possible styles. Use this info as you wish to customize your UI.  DEPRECATED: This is no longer populated by Destiny 2 game content. Please use inProgressValueStyle and completedValueStyle instead. | [optional] 


