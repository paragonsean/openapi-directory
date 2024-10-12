

# Drive

Representation of a shared drive. Some resource methods (such as `drives.update`) require a `driveId`. Use the `drives.list` method to retrieve the ID for a shared drive.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backgroundImageFile** | [**DriveBackgroundImageFile**](DriveBackgroundImageFile.md) |  |  [optional] |
|**backgroundImageLink** | **String** | Output only. A short-lived link to this shared drive&#39;s background image. |  [optional] |
|**capabilities** | [**DriveCapabilities**](DriveCapabilities.md) |  |  [optional] |
|**colorRgb** | **String** | The color of this shared drive as an RGB hex string. It can only be set on a &#x60;drive.drives.update&#x60; request that does not set &#x60;themeId&#x60;. |  [optional] |
|**createdDate** | **OffsetDateTime** | The time at which the shared drive was created (RFC 3339 date-time). |  [optional] |
|**hidden** | **Boolean** | Whether the shared drive is hidden from default view. |  [optional] |
|**id** | **String** | Output only. The ID of this shared drive which is also the ID of the top level folder of this shared drive. |  [optional] |
|**kind** | **String** | Output only. This is always &#x60;drive#drive&#x60; |  [optional] |
|**name** | **String** | The name of this shared drive. |  [optional] |
|**orgUnitId** | **String** | Output only. The organizational unit of this shared drive. This field is only populated on &#x60;drives.list&#x60; responses when the &#x60;useDomainAdminAccess&#x60; parameter is set to &#x60;true&#x60;. |  [optional] |
|**restrictions** | [**DriveRestrictions**](DriveRestrictions.md) |  |  [optional] |
|**themeId** | **String** | The ID of the theme from which the background image and color will be set. The set of possible &#x60;driveThemes&#x60; can be retrieved from a &#x60;drive.about.get&#x60; response. When not specified on a &#x60;drive.drives.insert&#x60; request, a random theme is chosen from which the background image and color are set. This is a write-only field; it can only be set on requests that don&#39;t set &#x60;colorRgb&#x60; or &#x60;backgroundImageFile&#x60;. |  [optional] |



