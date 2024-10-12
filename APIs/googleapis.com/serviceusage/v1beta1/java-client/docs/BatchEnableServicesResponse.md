

# BatchEnableServicesResponse

Response message for the `BatchEnableServices` method. This response message is assigned to the `response` field of the returned Operation when that operation is done.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failures** | [**List&lt;EnableFailure&gt;**](EnableFailure.md) | If allow_partial_success is true, and one or more services could not be enabled, this field contains the details about each failure. |  [optional] |
|**services** | [**List&lt;GoogleApiServiceusageV1Service&gt;**](GoogleApiServiceusageV1Service.md) | The new state of the services after enabling. |  [optional] |



