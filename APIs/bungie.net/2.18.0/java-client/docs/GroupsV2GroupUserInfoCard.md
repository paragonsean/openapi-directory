

# GroupsV2GroupUserInfoCard


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastSeenDisplayName** | **String** | This will be the display name the clan server last saw the user as. If the account is an active cross save override, this will be the display name to use. Otherwise, this will match the displayName property. |  [optional] |
|**lastSeenDisplayNameType** | **Integer** | The platform of the LastSeenDisplayName |  [optional] |
|**applicableMembershipTypes** | **List&lt;Integer&gt;** | The list of Membership Types indicating the platforms on which this Membership can be used.   Not in Cross Save &#x3D; its original membership type. Cross Save Primary &#x3D; Any membership types it is overridding, and its original membership type Cross Save Overridden &#x3D; Empty list |  [optional] |
|**bungieGlobalDisplayName** | **String** | The bungie global display name, if set. |  [optional] |
|**bungieGlobalDisplayNameCode** | **Integer** | The bungie global display name code, if set. |  [optional] |
|**crossSaveOverride** | **Integer** | If there is a cross save override in effect, this value will tell you the type that is overridding this one. |  [optional] |
|**displayName** | **String** | Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API. |  [optional] |
|**iconPath** | **String** | URL the Icon if available. |  [optional] |
|**isPublic** | **Boolean** | If True, this is a public user membership. |  [optional] |
|**membershipId** | **Long** | Membership ID as they user is known in the Accounts service |  [optional] |
|**membershipType** | **Integer** | Type of the membership. Not necessarily the native type. |  [optional] |
|**supplementalDisplayName** | **String** | A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc. |  [optional] |



