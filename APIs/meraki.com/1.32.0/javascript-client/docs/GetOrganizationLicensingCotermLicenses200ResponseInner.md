# MerakiDashboardApi.GetOrganizationLicensingCotermLicenses200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claimedAt** | **Date** | When the license was claimed into the organization | [optional] 
**counts** | [**[GetOrganizationLicensingCotermLicenses200ResponseInnerCountsInner]**](GetOrganizationLicensingCotermLicenses200ResponseInnerCountsInner.md) | The counts of the license by model type | [optional] 
**duration** | **Number** | The duration (term length) of the license, measured in days | [optional] 
**editions** | [**[GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner]**](GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner.md) | The editions of the license for each relevant product type | [optional] 
**expired** | **Boolean** | Flag to indicate if the license is expired | [optional] 
**invalidated** | **Boolean** | Flag to indicated that the license is invalidated | [optional] 
**invalidatedAt** | **Date** | When the license was invalidated. Will be null for active licenses | [optional] 
**key** | **String** | The key of the license | [optional] 
**mode** | **String** | The operation mode of the license when it was claimed | [optional] 
**organizationId** | **String** | The ID of the organization that the license is claimed in | [optional] 
**startedAt** | **Date** | When the license&#39;s term began (approximately the date when the license was created) | [optional] 



## Enum: ModeEnum


* `addDevices` (value: `"addDevices"`)

* `renew` (value: `"renew"`)




