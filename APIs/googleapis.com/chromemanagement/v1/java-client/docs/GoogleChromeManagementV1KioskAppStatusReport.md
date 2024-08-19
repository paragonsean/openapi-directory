

# GoogleChromeManagementV1KioskAppStatusReport

Kiosk app status report of a device. * Available for Kiosks * This field provides the app id and version number running on a kiosk device and the timestamp of when the report was last updated * Data for this field is controlled via policy: [ReportDeviceSessionStatus](https://chromeenterprise.google/policies/#ReportDeviceSessionStatus) * Data Collection Frequency: Only at Upload * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_APPS_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | App id of kiosk app for example \&quot;mdmkkicfmmkgmpkmkdikhlbggogpicma\&quot; |  [optional] |
|**appVersion** | **String** | App version number of kiosk app for example \&quot;1.10.118\&quot; |  [optional] |
|**reportTime** | **String** | Timestamp of when report was collected |  [optional] |



