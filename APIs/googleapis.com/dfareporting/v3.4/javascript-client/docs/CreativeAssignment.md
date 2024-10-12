# CampaignManager360Api.CreativeAssignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Whether this creative assignment is active. When true, the creative will be included in the ad&#39;s rotation. | [optional] 
**applyEventTags** | **Boolean** | Whether applicable event tags should fire when this creative assignment is rendered. If this value is unset when the ad is inserted or updated, it will default to true for all creative types EXCEPT for INTERNAL_REDIRECT, INTERSTITIAL_INTERNAL_REDIRECT, and INSTREAM_VIDEO. | [optional] 
**clickThroughUrl** | [**ClickThroughUrl**](ClickThroughUrl.md) |  | [optional] 
**companionCreativeOverrides** | [**[CompanionClickThroughOverride]**](CompanionClickThroughOverride.md) | Companion creative overrides for this creative assignment. Applicable to video ads. | [optional] 
**creativeGroupAssignments** | [**[CreativeGroupAssignment]**](CreativeGroupAssignment.md) | Creative group assignments for this creative assignment. Only one assignment per creative group number is allowed for a maximum of two assignments. | [optional] 
**creativeId** | **String** | ID of the creative to be assigned. This is a required field. | [optional] 
**creativeIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**endTime** | **Date** |  | [optional] 
**richMediaExitOverrides** | [**[RichMediaExitOverride]**](RichMediaExitOverride.md) | Rich media exit overrides for this creative assignment. Applicable when the creative type is any of the following: - DISPLAY - RICH_MEDIA_INPAGE - RICH_MEDIA_INPAGE_FLOATING - RICH_MEDIA_IM_EXPAND - RICH_MEDIA_EXPANDING - RICH_MEDIA_INTERSTITIAL_FLOAT - RICH_MEDIA_MOBILE_IN_APP - RICH_MEDIA_MULTI_FLOATING - RICH_MEDIA_PEEL_DOWN - VPAID_LINEAR - VPAID_NON_LINEAR  | [optional] 
**sequence** | **Number** | Sequence number of the creative assignment, applicable when the rotation type is CREATIVE_ROTATION_TYPE_SEQUENTIAL. Acceptable values are 1 to 65535, inclusive. | [optional] 
**sslCompliant** | **Boolean** | Whether the creative to be assigned is SSL-compliant. This is a read-only field that is auto-generated when the ad is inserted or updated. | [optional] 
**startTime** | **Date** |  | [optional] 
**weight** | **Number** | Weight of the creative assignment, applicable when the rotation type is CREATIVE_ROTATION_TYPE_RANDOM. Value must be greater than or equal to 1. | [optional] 


