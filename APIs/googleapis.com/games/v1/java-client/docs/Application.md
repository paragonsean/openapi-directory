

# Application

The Application resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**achievementCount** | **Integer** | The number of achievements visible to the currently authenticated player. |  [optional] |
|**assets** | [**List&lt;ImageAsset&gt;**](ImageAsset.md) | The assets of the application. |  [optional] |
|**author** | **String** | The author of the application. |  [optional] |
|**category** | [**ApplicationCategory**](ApplicationCategory.md) |  |  [optional] |
|**description** | **String** | The description of the application. |  [optional] |
|**enabledFeatures** | [**List&lt;EnabledFeaturesEnum&gt;**](#List&lt;EnabledFeaturesEnum&gt;) | A list of features that have been enabled for the application. |  [optional] |
|**id** | **String** | The ID of the application. |  [optional] |
|**instances** | [**List&lt;Instance&gt;**](Instance.md) | The instances of the application. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#application&#x60;. |  [optional] |
|**lastUpdatedTimestamp** | **String** | The last updated timestamp of the application. |  [optional] |
|**leaderboardCount** | **Integer** | The number of leaderboards visible to the currently authenticated player. |  [optional] |
|**name** | **String** | The name of the application. |  [optional] |
|**themeColor** | **String** | A hint to the client UI for what color to use as an app-themed color. The color is given as an RGB triplet (e.g. \&quot;E0E0E0\&quot;). |  [optional] |



## Enum: List&lt;EnabledFeaturesEnum&gt;

| Name | Value |
|---- | -----|
| SNAPSHOTS | &quot;SNAPSHOTS&quot; |



