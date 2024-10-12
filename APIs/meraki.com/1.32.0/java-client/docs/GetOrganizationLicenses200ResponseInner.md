

# GetOrganizationLicenses200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationDate** | **String** | The date the license started burning |  [optional] |
|**claimDate** | **String** | The date the license was claimed into the organization |  [optional] |
|**deviceSerial** | **String** | Serial number of the device the license is assigned to |  [optional] |
|**durationInDays** | **Integer** | The duration of the individual license |  [optional] |
|**expirationDate** | **String** | The date the license will expire |  [optional] |
|**headLicenseId** | **String** | The id of the head license this license is queued behind. If there is no head license, it returns nil. |  [optional] |
|**id** | **String** | License ID |  [optional] |
|**licenseKey** | **String** | License key |  [optional] |
|**licenseType** | **String** | License type |  [optional] |
|**networkId** | **String** | ID of the network the license is assigned to |  [optional] |
|**orderNumber** | **String** | Order number |  [optional] |
|**permanentlyQueuedLicenses** | [**List&lt;GetOrganizationLicenses200ResponseInnerPermanentlyQueuedLicensesInner&gt;**](GetOrganizationLicenses200ResponseInnerPermanentlyQueuedLicensesInner.md) | DEPRECATED List of permanently queued licenses attached to the license. Instead, use /organizations/{organizationId}/licenses?deviceSerial&#x3D; to retrieved queued licenses for a given device. |  [optional] |
|**seatCount** | **Integer** | The number of seats of the license. Only applicable to SM licenses. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the license. All queued licenses have a status of &#x60;recentlyQueued&#x60;. |  [optional] |
|**totalDurationInDays** | **Integer** | The duration of the license plus all permanently queued licenses associated with it |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| EXPIRED | &quot;expired&quot; |
| EXPIRING | &quot;expiring&quot; |
| RECENTLY_QUEUED | &quot;recentlyQueued&quot; |
| UNUSED | &quot;unused&quot; |
| UNUSED_ACTIVE | &quot;unusedActive&quot; |



