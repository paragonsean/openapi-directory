# MicrosoftNetApp.ReplicationObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpointType** | **String** | Indicates whether the local volume is the source or destination for the Volume Replication | [optional] 
**remoteVolumeRegion** | **String** | The remote region for the other end of the Volume Replication. | [optional] 
**remoteVolumeResourceId** | **String** | The resource ID of the remote volume. | 
**replicationId** | **String** | Id | [optional] 
**replicationSchedule** | **String** | Schedule | 



## Enum: EndpointTypeEnum


* `src` (value: `"src"`)

* `dst` (value: `"dst"`)





## Enum: ReplicationScheduleEnum


* `_10minutely` (value: `"_10minutely"`)

* `hourly` (value: `"hourly"`)

* `daily` (value: `"daily"`)

* `weekly` (value: `"weekly"`)

* `monthly` (value: `"monthly"`)




