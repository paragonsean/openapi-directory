

# SnowMonkeyConfig

Configuration for the faults that can be injected in requests. The name Snow Monkey is an hommage to Netflix's Chaos Monkey 😉

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chaosConfig** | [**ChaosConfig**](ChaosConfig.md) |  |  |
|**dryRun** | **Boolean** | Whether or not outages will actualy impact requests |  |
|**enabled** | **Boolean** | Whether or not this config is enabled |  |
|**includeUserFacingDescriptors** | **Boolean** | Whether or not user facing apps. will be impacted by Snow Monkey |  |
|**outageDurationFrom** | **Integer** | Start of outage duration range |  |
|**outageDurationTo** | **Integer** | End of outage duration range |  |
|**outageStrategy** | **OutageStrategy** |  |  |
|**startTime** | **String** | Start time of Snow Monkey each day |  |
|**stopTime** | **String** | Stop time of Snow Monkey each day |  |
|**targetGroups** | **List&lt;String&gt;** | Groups impacted by Snow Monkey. If empty, all groups will be impacted |  |
|**timesPerDay** | **Integer** | Number of time per day each service will be outage |  |



