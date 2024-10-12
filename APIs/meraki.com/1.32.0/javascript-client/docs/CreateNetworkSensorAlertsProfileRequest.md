# MerakiDashboardApi.CreateNetworkSensorAlertsProfileRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**[GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInner]**](GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInner.md) | List of conditions that will cause the profile to send an alert. | 
**name** | **String** | Name of the sensor alert profile. | 
**recipients** | [**GetNetworkSensorAlertsProfiles200ResponseInnerRecipients**](GetNetworkSensorAlertsProfiles200ResponseInnerRecipients.md) |  | [optional] 
**schedule** | [**CreateNetworkSensorAlertsProfileRequestSchedule**](CreateNetworkSensorAlertsProfileRequestSchedule.md) |  | [optional] 
**serials** | **[String]** | List of device serials assigned to this sensor alert profile. | [optional] 


