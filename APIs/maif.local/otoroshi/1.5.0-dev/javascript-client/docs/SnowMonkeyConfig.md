# OtoroshiAdminApi.SnowMonkeyConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chaosConfig** | [**ChaosConfig**](ChaosConfig.md) |  | 
**dryRun** | **Boolean** | Whether or not outages will actualy impact requests | 
**enabled** | **Boolean** | Whether or not this config is enabled | 
**includeUserFacingDescriptors** | **Boolean** | Whether or not user facing apps. will be impacted by Snow Monkey | 
**outageDurationFrom** | **Number** | Start of outage duration range | 
**outageDurationTo** | **Number** | End of outage duration range | 
**outageStrategy** | [**OutageStrategy**](OutageStrategy.md) |  | 
**startTime** | **String** | Start time of Snow Monkey each day | 
**stopTime** | **String** | Stop time of Snow Monkey each day | 
**targetGroups** | **[String]** | Groups impacted by Snow Monkey. If empty, all groups will be impacted | 
**timesPerDay** | **Number** | Number of time per day each service will be outage | 


