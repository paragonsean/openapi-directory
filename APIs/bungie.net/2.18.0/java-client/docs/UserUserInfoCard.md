

# UserUserInfoCard

This contract supplies basic information commonly used to display a minimal amount of information about a user. Take care to not add more properties here unless the property applies in all (or at least the majority) of the situations where UserInfoCard is used. Avoid adding game specific or platform specific details here. In cases where UserInfoCard is a subset of the data needed in a contract, use UserInfoCard as a property of other contracts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
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



