# DisplayVideo360Api.CmHybridConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmAccountId** | **String** | Required. Immutable. Account ID of the CM360 Floodlight configuration linked with the DV360 advertiser. | [optional] 
**cmAdvertiserIds** | **[String]** | Output only. The set of CM360 Advertiser IDs sharing the CM360 Floodlight configuration. | [optional] [readonly] 
**cmFloodlightConfigId** | **String** | Required. Immutable. ID of the CM360 Floodlight configuration linked with the DV360 advertiser. | [optional] 
**cmFloodlightLinkingAuthorized** | **Boolean** | Required. Immutable. By setting this field to &#x60;true&#x60;, you, on behalf of your company, authorize the sharing of information from the given Floodlight configuration to this Display &amp; Video 360 advertiser. | [optional] 
**cmSyncableSiteIds** | **[String]** | A list of CM360 sites whose placements will be synced to DV360 as creatives. If absent or empty in CreateAdvertiser method, the system will automatically create a CM360 site. Removing sites from this list may cause DV360 creatives synced from CM360 to be deleted. At least one site must be specified. | [optional] 
**dv360ToCmCostReportingEnabled** | **Boolean** | Whether or not to report DV360 cost to CM360. | [optional] 
**dv360ToCmDataSharingEnabled** | **Boolean** | Whether or not to include DV360 data in CM360 data transfer reports. | [optional] 


