# ApiManagementClient.ConnectivityStatusContract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **String** | Error details of the connectivity to the resource. | [optional] 
**lastStatusChange** | **Date** | The date when the resource connectivity status last Changed from success to failure or vice-versa. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | 
**lastUpdated** | **Date** | The date when the resource connectivity status was last updated. This status should be updated every 15 minutes. If this status has not been updated, then it means that the service has lost network connectivity to the resource, from inside the Virtual Network.The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | 
**name** | **String** | The hostname of the resource which the service depends on. This can be the database, storage or any other azure resource on which the service depends upon. | 
**status** | **String** | Resource Connectivity Status Type identifier. | 



## Enum: StatusEnum


* `initializing` (value: `"initializing"`)

* `success` (value: `"success"`)

* `failure` (value: `"failure"`)




