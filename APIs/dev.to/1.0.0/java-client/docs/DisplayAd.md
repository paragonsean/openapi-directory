

# DisplayAd

A Display Ad, aka Billboard, aka Widget

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approved** | **Boolean** | Ad must be both published and approved to be in rotation |  [optional] |
|**articleExcludeIds** | **String** | Articles this ad should *not* appear on (blank means no articles are disallowed, and this ad can appear next to any/all articles). Comma-separated list of integer Article IDs |  [optional] |
|**bodyMarkdown** | **String** | The text (in markdown) of the ad (required) |  |
|**creatorId** | **Integer** | Identifies the user who created the ad. |  [optional] |
|**displayTo** | [**DisplayToEnum**](#DisplayToEnum) | Potentially limits visitors to whom the ad is visible |  [optional] |
|**id** | **Integer** | The ID of the Display Ad |  [optional] |
|**name** | **String** | For internal use, helps distinguish ads from one another |  |
|**organizationId** | **Integer** | Identifies the organization to which the ad belongs |  [optional] |
|**placementArea** | [**PlacementAreaEnum**](#PlacementAreaEnum) | Identifies which area of site layout the ad can appear in |  |
|**published** | **Boolean** | Ad must be both published and approved to be in rotation |  [optional] |
|**tagList** | **String** | Tags on which this ad can be displayed (blank is all/any tags) |  [optional] |
|**typeOf** | [**TypeOfEnum**](#TypeOfEnum) | Types of the billboards: in_house (created by admins), community (created by an entity, appears on entity&#39;s content), external ( created by an entity, or a non-entity, can appear everywhere)  |  [optional] |



## Enum: DisplayToEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| LOGGED_IN | &quot;logged_in&quot; |
| LOGGED_OUT | &quot;logged_out&quot; |



## Enum: PlacementAreaEnum

| Name | Value |
|---- | -----|
| SIDEBAR_LEFT | &quot;sidebar_left&quot; |
| SIDEBAR_LEFT_2 | &quot;sidebar_left_2&quot; |
| SIDEBAR_RIGHT | &quot;sidebar_right&quot; |
| FEED_FIRST | &quot;feed_first&quot; |
| FEED_SECOND | &quot;feed_second&quot; |
| FEED_THIRD | &quot;feed_third&quot; |
| POST_SIDEBAR | &quot;post_sidebar&quot; |
| POST_COMMENTS | &quot;post_comments&quot; |



## Enum: TypeOfEnum

| Name | Value |
|---- | -----|
| IN_HOUSE | &quot;in_house&quot; |
| COMMUNITY | &quot;community&quot; |
| EXTERNAL | &quot;external&quot; |



