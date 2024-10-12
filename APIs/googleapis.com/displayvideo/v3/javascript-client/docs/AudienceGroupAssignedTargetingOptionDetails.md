# DisplayVideo360Api.AudienceGroupAssignedTargetingOptionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excludedFirstAndThirdPartyAudienceGroup** | [**FirstAndThirdPartyAudienceGroup**](FirstAndThirdPartyAudienceGroup.md) |  | [optional] 
**excludedGoogleAudienceGroup** | [**GoogleAudienceGroup**](GoogleAudienceGroup.md) |  | [optional] 
**includedCombinedAudienceGroup** | [**CombinedAudienceGroup**](CombinedAudienceGroup.md) |  | [optional] 
**includedCustomListGroup** | [**CustomListGroup**](CustomListGroup.md) |  | [optional] 
**includedFirstAndThirdPartyAudienceGroups** | [**[FirstAndThirdPartyAudienceGroup]**](FirstAndThirdPartyAudienceGroup.md) | The first and third party audience ids and recencies of included first and third party audience groups. Each first and third party audience group contains first and third party audience ids only. The relation between each first and third party audience group is INTERSECTION, and the result is UNION&#39;ed with other audience groups. Repeated groups with same settings will be ignored. | [optional] 
**includedGoogleAudienceGroup** | [**GoogleAudienceGroup**](GoogleAudienceGroup.md) |  | [optional] 


