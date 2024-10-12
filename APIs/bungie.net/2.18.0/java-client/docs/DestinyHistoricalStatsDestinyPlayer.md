

# DestinyHistoricalStatsDestinyPlayer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bungieNetUserInfo** | [**UserUserInfoCard**](UserUserInfoCard.md) | Details about the player as they are known on BungieNet. This will be undefined if the player has marked their credential private, or does not have a BungieNet account. |  [optional] |
|**characterClass** | **String** | Class of the character if applicable and available. |  [optional] |
|**characterLevel** | **Integer** | Level of the character if available. Zero if it is not available. |  [optional] |
|**clanName** | **String** | Current clan name for the player. This value may be null or an empty string if the user does not have a clan. |  [optional] |
|**clanTag** | **String** | Current clan tag for the player. This value may be null or an empty string if the user does not have a clan. |  [optional] |
|**classHash** | **Integer** |  |  [optional] |
|**destinyUserInfo** | [**UserUserInfoCard**](UserUserInfoCard.md) | Details about the player as they are known in game (platform display name, Destiny emblem) |  [optional] |
|**emblemHash** | **Integer** | If we know the emblem&#39;s hash, this can be used to look up the player&#39;s emblem at the time of a match when receiving PGCR data, or otherwise their currently equipped emblem (if we are able to obtain it). |  [optional] |
|**genderHash** | **Integer** |  |  [optional] |
|**lightLevel** | **Integer** | Light Level of the character if available. Zero if it is not available. |  [optional] |
|**raceHash** | **Integer** |  |  [optional] |



