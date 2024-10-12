# CloudSearchApi.EnterpriseTopazSidekickCardMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardCategory** | **String** | Declares a preference for how this card should be packed in MSCR. All cards in a response must correspond to a single category. As a result, cards may be dropped from the response if this field is set. Any card that does not match the category of the card with the highest priority in the response will be dropped. | [optional] 
**cardId** | **String** | An ID to identify the card and match actions to it. Be thoughtful of new card IDs since actions will be associated to that ID. E.g., if two card IDs collide, the system will think that the actions have been applied to the same card. Similarly, if EAS can return multiple cards of the same type (e.g., Meetings), ensure that the card_id identifies a given instance of the card so that, e.g., dismissals only affect the dismissed card as opposed to affecting all meeting cards. | [optional] 
**chronology** | **String** | Chronology. | [optional] 
**debugInfo** | **String** | Debug info (only reported if request&#39;s debug_level &gt; 0). | [optional] 
**nlpMetadata** | [**EnterpriseTopazSidekickNlpMetadata**](EnterpriseTopazSidekickNlpMetadata.md) |  | [optional] 
**rankingParams** | [**EnterpriseTopazSidekickRankingParams**](EnterpriseTopazSidekickRankingParams.md) |  | [optional] 
**renderMode** | **String** | Render mode. | [optional] 



## Enum: CardCategoryEnum


* `DEFAULT` (value: `"DEFAULT"`)

* `ANSWER` (value: `"ANSWER"`)

* `KNOWLEDGE` (value: `"KNOWLEDGE"`)

* `HOMEPAGE` (value: `"HOMEPAGE"`)





## Enum: ChronologyEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `PAST` (value: `"PAST"`)

* `RECENTLY_PAST` (value: `"RECENTLY_PAST"`)

* `PRESENT` (value: `"PRESENT"`)

* `NEAR_FUTURE` (value: `"NEAR_FUTURE"`)

* `FUTURE` (value: `"FUTURE"`)





## Enum: RenderModeEnum


* `UNKNOWN_RENDER` (value: `"UNKNOWN_RENDER"`)

* `COLLAPSED` (value: `"COLLAPSED"`)

* `EXPANDED` (value: `"EXPANDED"`)




