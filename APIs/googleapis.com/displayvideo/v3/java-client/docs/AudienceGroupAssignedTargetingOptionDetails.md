

# AudienceGroupAssignedTargetingOptionDetails

Assigned audience group targeting option details. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_AUDIENCE_GROUP`. The relation between each group is UNION, except for excluded_first_and_third_party_audience_group and excluded_google_audience_group, of which COMPLEMENT is used as an INTERSECTION with other groups.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**excludedFirstAndThirdPartyAudienceGroup** | [**FirstAndThirdPartyAudienceGroup**](FirstAndThirdPartyAudienceGroup.md) |  |  [optional] |
|**excludedGoogleAudienceGroup** | [**GoogleAudienceGroup**](GoogleAudienceGroup.md) |  |  [optional] |
|**includedCombinedAudienceGroup** | [**CombinedAudienceGroup**](CombinedAudienceGroup.md) |  |  [optional] |
|**includedCustomListGroup** | [**CustomListGroup**](CustomListGroup.md) |  |  [optional] |
|**includedFirstAndThirdPartyAudienceGroups** | [**List&lt;FirstAndThirdPartyAudienceGroup&gt;**](FirstAndThirdPartyAudienceGroup.md) | The first and third party audience ids and recencies of included first and third party audience groups. Each first and third party audience group contains first and third party audience ids only. The relation between each first and third party audience group is INTERSECTION, and the result is UNION&#39;ed with other audience groups. Repeated groups with same settings will be ignored. |  [optional] |
|**includedGoogleAudienceGroup** | [**GoogleAudienceGroup**](GoogleAudienceGroup.md) |  |  [optional] |



