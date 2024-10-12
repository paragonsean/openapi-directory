# BungieNetApi.UserCrossSaveUserMembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicableMembershipTypes** | **[Number]** | The list of Membership Types indicating the platforms on which this Membership can be used.   Not in Cross Save &#x3D; its original membership type. Cross Save Primary &#x3D; Any membership types it is overridding, and its original membership type Cross Save Overridden &#x3D; Empty list | [optional] 
**bungieGlobalDisplayName** | **String** | The bungie global display name, if set. | [optional] 
**bungieGlobalDisplayNameCode** | **Number** | The bungie global display name code, if set. | [optional] 
**crossSaveOverride** | **Number** | If there is a cross save override in effect, this value will tell you the type that is overridding this one. | [optional] 
**displayName** | **String** | Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API. | [optional] 
**isPublic** | **Boolean** | If True, this is a public user membership. | [optional] 
**membershipId** | **Number** | Membership ID as they user is known in the Accounts service | [optional] 
**membershipType** | **Number** | Type of the membership. Not necessarily the native type. | [optional] 


