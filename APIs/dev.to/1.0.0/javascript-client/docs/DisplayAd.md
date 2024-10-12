# ForemApiV1.DisplayAd

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **Boolean** | Ad must be both published and approved to be in rotation | [optional] 
**articleExcludeIds** | **String** | Articles this ad should *not* appear on (blank means no articles are disallowed, and this ad can appear next to any/all articles). Comma-separated list of integer Article IDs | [optional] 
**bodyMarkdown** | **String** | The text (in markdown) of the ad (required) | 
**creatorId** | **Number** | Identifies the user who created the ad. | [optional] 
**displayTo** | **String** | Potentially limits visitors to whom the ad is visible | [optional] [default to &#39;all&#39;]
**id** | **Number** | The ID of the Display Ad | [optional] 
**name** | **String** | For internal use, helps distinguish ads from one another | 
**organizationId** | **Number** | Identifies the organization to which the ad belongs | [optional] 
**placementArea** | **String** | Identifies which area of site layout the ad can appear in | 
**published** | **Boolean** | Ad must be both published and approved to be in rotation | [optional] 
**tagList** | **String** | Tags on which this ad can be displayed (blank is all/any tags) | [optional] 
**typeOf** | **String** | Types of the billboards: in_house (created by admins), community (created by an entity, appears on entity&#39;s content), external ( created by an entity, or a non-entity, can appear everywhere)  | [optional] [default to &#39;in_house&#39;]



## Enum: DisplayToEnum


* `all` (value: `"all"`)

* `logged_in` (value: `"logged_in"`)

* `logged_out` (value: `"logged_out"`)





## Enum: PlacementAreaEnum


* `sidebar_left` (value: `"sidebar_left"`)

* `sidebar_left_2` (value: `"sidebar_left_2"`)

* `sidebar_right` (value: `"sidebar_right"`)

* `feed_first` (value: `"feed_first"`)

* `feed_second` (value: `"feed_second"`)

* `feed_third` (value: `"feed_third"`)

* `post_sidebar` (value: `"post_sidebar"`)

* `post_comments` (value: `"post_comments"`)





## Enum: TypeOfEnum


* `in_house` (value: `"in_house"`)

* `community` (value: `"community"`)

* `external` (value: `"external"`)




