# ServiceBroker.GoogleCloudServicebrokerV1beta1ListServiceInstancesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Used to communicate description of the response. Usually for non-standard error codes. https://github.com/openservicebrokerapi/servicebroker/blob/master/spec.md#service-broker-errors | [optional] 
**instances** | [**[GoogleCloudServicebrokerV1beta1ServiceInstance]**](GoogleCloudServicebrokerV1beta1ServiceInstance.md) | The list of instances in the broker. | [optional] 
**nextPageToken** | **String** | This token allows you to get the next page of results for list requests. If the number of results is larger than &#x60;pageSize&#x60;, use the &#x60;nextPageToken&#x60; as a value for the query parameter &#x60;pageToken&#x60; in the next list request. Subsequent list requests will have their own &#x60;nextPageToken&#x60; to continue paging through the results | [optional] 


