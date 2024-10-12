# BackupAndDrServiceApi.ListManagementServersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managementServers** | [**[ManagementServer]**](ManagementServer.md) | The list of ManagementServer instances in the project for the specified location. If the &#x60;{location}&#x60; value in the request is \&quot;-\&quot;, the response contains a list of instances from all locations. In case any location is unreachable, the response will only return management servers in reachable locations and the &#39;unreachable&#39; field will be populated with a list of unreachable locations. | [optional] 
**nextPageToken** | **String** | A token identifying a page of results the server should return. | [optional] 
**unreachable** | **[String]** | Locations that could not be reached. | [optional] 


