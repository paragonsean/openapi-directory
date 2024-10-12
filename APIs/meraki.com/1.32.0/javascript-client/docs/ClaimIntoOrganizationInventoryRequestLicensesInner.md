# MerakiDashboardApi.ClaimIntoOrganizationInventoryRequestLicensesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | The key of the license | 
**mode** | **String** | Co-term licensing only: either &#39;renew&#39; or &#39;addDevices&#39;. &#39;addDevices&#39; will increase the license limit, while &#39;renew&#39; will extend the amount of time until expiration. Defaults to &#39;addDevices&#39;. All licenses must be claimed with the same mode, and at most one renewal can be claimed at a time. Does not apply to organizations using per-device licensing model. | [optional] 



## Enum: ModeEnum


* `addDevices` (value: `"addDevices"`)

* `renew` (value: `"renew"`)




