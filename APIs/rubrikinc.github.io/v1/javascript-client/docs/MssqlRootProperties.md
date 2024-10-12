# RubrikRestApi.MssqlRootProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rootId** | **String** | ID of the root of this object. | [optional] 
**rootName** | **String** | Name of the root of this object. | 
**rootRole** | **String** | Role of the root object for this object if the root object is a Host and part of a **_MssqlAvailabilityGroup_**. | [optional] 
**rootType** | **String** | Type of the root object for this object. The root object is the top-level object from which this object is derived. If this object is an availability database, the root object is **_MssqlAvailabilityGroup_**. Otherwise, if this object is part of a cluster, the root object is **_WindowsCluster_**. Otherwise, the root object is **_Host_**. | 



## Enum: RootTypeEnum


* `Host` (value: `"Host"`)

* `WindowsCluster` (value: `"WindowsCluster"`)

* `MssqlAvailabilityGroup` (value: `"MssqlAvailabilityGroup"`)




