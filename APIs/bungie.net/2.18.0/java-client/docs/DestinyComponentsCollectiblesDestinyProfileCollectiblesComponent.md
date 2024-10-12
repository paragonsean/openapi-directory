

# DestinyComponentsCollectiblesDestinyProfileCollectiblesComponent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collectibles** | [**Map&lt;String, DestinyComponentsCollectiblesDestinyCollectibleComponent&gt;**](DestinyComponentsCollectiblesDestinyCollectibleComponent.md) |  |  [optional] |
|**collectionBadgesRootNodeHash** | **Integer** | The hash for the root presentation node definition of Collection Badges. |  [optional] |
|**collectionCategoriesRootNodeHash** | **Integer** | The hash for the root presentation node definition of Collection categories. |  [optional] |
|**newnessFlaggedCollectibleHashes** | **List&lt;Integer&gt;** | The list of collectibles determined by the game as having been \&quot;recently\&quot; acquired.  The game client itself actually controls this data, so I personally question whether anyone will get much use out of this: because we can&#39;t edit this value through the API. But in case anyone finds it useful, here it is. |  [optional] |
|**recentCollectibleHashes** | **List&lt;Integer&gt;** | The list of collectibles determined by the game as having been \&quot;recently\&quot; acquired. |  [optional] |



