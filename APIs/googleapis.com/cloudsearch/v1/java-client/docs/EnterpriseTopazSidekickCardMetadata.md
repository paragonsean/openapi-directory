

# EnterpriseTopazSidekickCardMetadata

Card metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardCategory** | [**CardCategoryEnum**](#CardCategoryEnum) | Declares a preference for how this card should be packed in MSCR. All cards in a response must correspond to a single category. As a result, cards may be dropped from the response if this field is set. Any card that does not match the category of the card with the highest priority in the response will be dropped. |  [optional] |
|**cardId** | **String** | An ID to identify the card and match actions to it. Be thoughtful of new card IDs since actions will be associated to that ID. E.g., if two card IDs collide, the system will think that the actions have been applied to the same card. Similarly, if EAS can return multiple cards of the same type (e.g., Meetings), ensure that the card_id identifies a given instance of the card so that, e.g., dismissals only affect the dismissed card as opposed to affecting all meeting cards. |  [optional] |
|**chronology** | [**ChronologyEnum**](#ChronologyEnum) | Chronology. |  [optional] |
|**debugInfo** | **String** | Debug info (only reported if request&#39;s debug_level &gt; 0). |  [optional] |
|**nlpMetadata** | [**EnterpriseTopazSidekickNlpMetadata**](EnterpriseTopazSidekickNlpMetadata.md) |  |  [optional] |
|**rankingParams** | [**EnterpriseTopazSidekickRankingParams**](EnterpriseTopazSidekickRankingParams.md) |  |  [optional] |
|**renderMode** | [**RenderModeEnum**](#RenderModeEnum) | Render mode. |  [optional] |



## Enum: CardCategoryEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| ANSWER | &quot;ANSWER&quot; |
| KNOWLEDGE | &quot;KNOWLEDGE&quot; |
| HOMEPAGE | &quot;HOMEPAGE&quot; |



## Enum: ChronologyEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| PAST | &quot;PAST&quot; |
| RECENTLY_PAST | &quot;RECENTLY_PAST&quot; |
| PRESENT | &quot;PRESENT&quot; |
| NEAR_FUTURE | &quot;NEAR_FUTURE&quot; |
| FUTURE | &quot;FUTURE&quot; |



## Enum: RenderModeEnum

| Name | Value |
|---- | -----|
| UNKNOWN_RENDER | &quot;UNKNOWN_RENDER&quot; |
| COLLAPSED | &quot;COLLAPSED&quot; |
| EXPANDED | &quot;EXPANDED&quot; |



