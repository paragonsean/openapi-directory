

# DestinyResponsesDestinyProfileUserInfoCard


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicableMembershipTypes** | **List&lt;Integer&gt;** | The list of Membership Types indicating the platforms on which this Membership can be used.   Not in Cross Save &#x3D; its original membership type. Cross Save Primary &#x3D; Any membership types it is overridding, and its original membership type Cross Save Overridden &#x3D; Empty list |  [optional] |
|**bungieGlobalDisplayName** | **String** | The bungie global display name, if set. |  [optional] |
|**bungieGlobalDisplayNameCode** | **Integer** | The bungie global display name code, if set. |  [optional] |
|**crossSaveOverride** | **Integer** | If there is a cross save override in effect, this value will tell you the type that is overridding this one. |  [optional] |
|**dateLastPlayed** | **OffsetDateTime** |  |  [optional] |
|**displayName** | **String** | Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API. |  [optional] |
|**iconPath** | **String** | URL the Icon if available. |  [optional] |
|**isCrossSavePrimary** | **Boolean** | If true, this account is hooked up as the \&quot;Primary\&quot; cross save account for one or more platforms. |  [optional] |
|**isOverridden** | **Boolean** | If this profile is being overridden/obscured by Cross Save, this will be set to true. We will still return the profile for display purposes where users need to know the info: it is up to any given area of the app/site to determine if this profile should still be shown. |  [optional] |
|**isPublic** | **Boolean** | If True, this is a public user membership. |  [optional] |
|**membershipId** | **Long** | Membership ID as they user is known in the Accounts service |  [optional] |
|**membershipType** | **Integer** | Type of the membership. Not necessarily the native type. |  [optional] |
|**platformSilver** | [**DestinyComponentsInventoryDestinyPlatformSilverComponent**](DestinyComponentsInventoryDestinyPlatformSilverComponent.md) | This is the silver available on this Profile across any platforms on which they have purchased silver.   This is only available if you are requesting yourself. |  [optional] |
|**supplementalDisplayName** | **String** | A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc. |  [optional] |
|**unpairedGameVersions** | [**UnpairedGameVersionsEnum**](#UnpairedGameVersionsEnum) | If this profile is not in a cross save pairing, this will return the game versions that we believe this profile has access to.   For the time being, we will not return this information for any membership that is in a cross save pairing. The gist is that, once the pairing occurs, we do not currently have a consistent way to get that information for the profile&#39;s original Platform, and thus gameVersions would be too inconsistent (based on the last platform they happened to play on) for the info to be useful.   If we ever can get this data, this field will be deprecated and replaced with data on the DestinyLinkedProfileResponse itself, with game versions per linked Platform. But since we can&#39;t get that, we have this as a stop-gap measure for getting the data in the only situation that we currently need it. |  [optional] |



## Enum: UnpairedGameVersionsEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_4 | 4 |
| NUMBER_8 | 8 |
| NUMBER_16 | 16 |
| NUMBER_32 | 32 |
| NUMBER_64 | 64 |
| NUMBER_128 | 128 |
| NUMBER_256 | 256 |
| NUMBER_512 | 512 |



