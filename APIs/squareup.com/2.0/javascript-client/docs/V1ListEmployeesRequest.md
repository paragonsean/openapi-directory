# SquareConnectApi.V1ListEmployeesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchToken** | **String** | A pagination cursor to retrieve the next set of results for your original query to the endpoint. | [optional] 
**beginCreatedAt** | **String** | If filtering results by their created_at field, the beginning of the requested reporting period, in ISO 8601 format. | [optional] 
**beginUpdatedAt** | **String** | If filtering results by their updated_at field, the beginning of the requested reporting period, in ISO 8601 format | [optional] 
**endCreatedAt** | **String** | If filtering results by their created_at field, the end of the requested reporting period, in ISO 8601 format. | [optional] 
**endUpdatedAt** | **String** | If filtering results by there updated_at field, the end of the requested reporting period, in ISO 8601 format. | [optional] 
**externalId** | **String** | If provided, the endpoint returns only employee entities with the specified external_id. | [optional] 
**limit** | **Number** | The maximum integer number of employee entities to return in a single response. Default 100, maximum 200. | [optional] 
**order** | **String** | The order in which employees are listed in the response, based on their created_at field.      Default value: ASC | [optional] 
**status** | **String** | If provided, the endpoint returns only employee entities with the specified status (ACTIVE or INACTIVE). | [optional] 


