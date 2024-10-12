

# ClaimIntoOrganizationRequestLicensesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The key of the license |  |
|**mode** | [**ModeEnum**](#ModeEnum) | Either &#39;renew&#39; or &#39;addDevices&#39;. &#39;addDevices&#39; will increase the license limit, while &#39;renew&#39; will extend the amount of time until expiration. Defaults to &#39;addDevices&#39;. All licenses must be claimed with the same mode, and at most one renewal can be claimed at a time. This parameter is legacy and does not apply to organizations with per-device licensing enabled. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| ADD_DEVICES | &quot;addDevices&quot; |
| RENEW | &quot;renew&quot; |



