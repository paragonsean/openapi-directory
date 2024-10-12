# MerakiDashboardApi.UpdateNetworkWirelessSsidSchedulesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | If true, the SSID outage schedule is enabled. | [optional] 
**ranges** | [**[UpdateNetworkWirelessSsidSchedulesRequestRangesInner]**](UpdateNetworkWirelessSsidSchedulesRequestRangesInner.md) | List of outage ranges. Has a start date and time, and end date and time. If this parameter is passed in along with rangesInSeconds parameter, this will take precedence. | [optional] 
**rangesInSeconds** | [**[UpdateNetworkWirelessSsidSchedulesRequestRangesInSecondsInner]**](UpdateNetworkWirelessSsidSchedulesRequestRangesInSecondsInner.md) | List of outage ranges in seconds since Sunday at Midnight. Has a start and end. If this parameter is passed in along with the ranges parameter, ranges will take precedence. | [optional] 


