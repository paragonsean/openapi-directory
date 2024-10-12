# ServiceUsageApi.BatchEnableServicesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failures** | [**[EnableFailure]**](EnableFailure.md) | If allow_partial_success is true, and one or more services could not be enabled, this field contains the details about each failure. | [optional] 
**services** | [**[GoogleApiServiceusageV1Service]**](GoogleApiServiceusageV1Service.md) | The new state of the services after enabling. | [optional] 


