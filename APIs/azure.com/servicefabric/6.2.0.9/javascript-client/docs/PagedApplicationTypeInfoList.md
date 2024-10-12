# ServiceFabricClientApis.PagedApplicationTypeInfoList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuationToken** | **String** | The continuation token parameter is used to obtain next set of results. The continuation token is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token is not included in the response. | [optional] 
**items** | [**[ApplicationTypeInfo]**](ApplicationTypeInfo.md) | List of application type information. | [optional] 


