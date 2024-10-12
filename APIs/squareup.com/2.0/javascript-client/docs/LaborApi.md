# SquareConnectApi.LaborApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBreakType**](LaborApi.md#createBreakType) | **POST** /v2/labor/break-types | CreateBreakType
[**createShift**](LaborApi.md#createShift) | **POST** /v2/labor/shifts | CreateShift
[**deleteBreakType**](LaborApi.md#deleteBreakType) | **DELETE** /v2/labor/break-types/{id} | DeleteBreakType
[**deleteShift**](LaborApi.md#deleteShift) | **DELETE** /v2/labor/shifts/{id} | DeleteShift
[**getBreakType**](LaborApi.md#getBreakType) | **GET** /v2/labor/break-types/{id} | GetBreakType
[**getEmployeeWage**](LaborApi.md#getEmployeeWage) | **GET** /v2/labor/employee-wages/{id} | GetEmployeeWage
[**getShift**](LaborApi.md#getShift) | **GET** /v2/labor/shifts/{id} | GetShift
[**getTeamMemberWage**](LaborApi.md#getTeamMemberWage) | **GET** /v2/labor/team-member-wages/{id} | GetTeamMemberWage
[**listBreakTypes**](LaborApi.md#listBreakTypes) | **GET** /v2/labor/break-types | ListBreakTypes
[**listEmployeeWages**](LaborApi.md#listEmployeeWages) | **GET** /v2/labor/employee-wages | ListEmployeeWages
[**listTeamMemberWages**](LaborApi.md#listTeamMemberWages) | **GET** /v2/labor/team-member-wages | ListTeamMemberWages
[**listWorkweekConfigs**](LaborApi.md#listWorkweekConfigs) | **GET** /v2/labor/workweek-configs | ListWorkweekConfigs
[**searchShifts**](LaborApi.md#searchShifts) | **POST** /v2/labor/shifts/search | SearchShifts
[**updateBreakType**](LaborApi.md#updateBreakType) | **PUT** /v2/labor/break-types/{id} | UpdateBreakType
[**updateShift**](LaborApi.md#updateShift) | **PUT** /v2/labor/shifts/{id} | UpdateShift
[**updateWorkweekConfig**](LaborApi.md#updateWorkweekConfig) | **PUT** /v2/labor/workweek-configs/{id} | UpdateWorkweekConfig



## createBreakType

> CreateBreakTypeResponse createBreakType(createBreakTypeRequest)

CreateBreakType

Creates a new &#x60;BreakType&#x60;.  A &#x60;BreakType&#x60; is a template for creating &#x60;Break&#x60; objects. You must provide the following values in your request to this endpoint:  - &#x60;location_id&#x60; - &#x60;break_name&#x60; - &#x60;expected_duration&#x60; - &#x60;is_paid&#x60;  You can only have three &#x60;BreakType&#x60; instances per location. If you attempt to add a fourth &#x60;BreakType&#x60; for a location, an &#x60;INVALID_REQUEST_ERROR&#x60; \&quot;Exceeded limit of 3 breaks per location.\&quot; is returned.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let createBreakTypeRequest = new SquareConnectApi.CreateBreakTypeRequest(); // CreateBreakTypeRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createBreakType(createBreakTypeRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createBreakTypeRequest** | [**CreateBreakTypeRequest**](CreateBreakTypeRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateBreakTypeResponse**](CreateBreakTypeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createShift

> CreateShiftResponse createShift(createShiftRequest)

CreateShift

Creates a new &#x60;Shift&#x60;.  A &#x60;Shift&#x60; represents a complete workday for a single employee. You must provide the following values in your request to this endpoint:  - &#x60;location_id&#x60; - &#x60;employee_id&#x60; - &#x60;start_at&#x60;  An attempt to create a new &#x60;Shift&#x60; can result in a &#x60;BAD_REQUEST&#x60; error when: - The &#x60;status&#x60; of the new &#x60;Shift&#x60; is &#x60;OPEN&#x60; and the employee has another shift with an &#x60;OPEN&#x60; status. - The &#x60;start_at&#x60; date is in the future. - The &#x60;start_at&#x60; or &#x60;end_at&#x60; date overlaps another shift for the same employee. - The &#x60;Break&#x60; instances are set in the request and a break &#x60;start_at&#x60; is before the &#x60;Shift.start_at&#x60;, a break &#x60;end_at&#x60; is after the &#x60;Shift.end_at&#x60;, or both.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let createShiftRequest = new SquareConnectApi.CreateShiftRequest(); // CreateShiftRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createShift(createShiftRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createShiftRequest** | [**CreateShiftRequest**](CreateShiftRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateShiftResponse**](CreateShiftResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBreakType

> DeleteBreakTypeResponse deleteBreakType(id)

DeleteBreakType

Deletes an existing &#x60;BreakType&#x60;.  A &#x60;BreakType&#x60; can be deleted even if it is referenced from a &#x60;Shift&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let id = "id_example"; // String | The UUID for the `BreakType` being deleted.
apiInstance.deleteBreakType(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The UUID for the &#x60;BreakType&#x60; being deleted. | 

### Return type

[**DeleteBreakTypeResponse**](DeleteBreakTypeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteShift

> DeleteShiftResponse deleteShift(id)

DeleteShift

Deletes a &#x60;Shift&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let id = "id_example"; // String | The UUID for the `Shift` being deleted.
apiInstance.deleteShift(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The UUID for the &#x60;Shift&#x60; being deleted. | 

### Return type

[**DeleteShiftResponse**](DeleteShiftResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBreakType

> GetBreakTypeResponse getBreakType(id)

GetBreakType

Returns a single &#x60;BreakType&#x60; specified by &#x60;id&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let id = "id_example"; // String | The UUID for the `BreakType` being retrieved.
apiInstance.getBreakType(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The UUID for the &#x60;BreakType&#x60; being retrieved. | 

### Return type

[**GetBreakTypeResponse**](GetBreakTypeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeWage

> GetEmployeeWageResponse getEmployeeWage(id)

GetEmployeeWage

Returns a single &#x60;EmployeeWage&#x60; specified by &#x60;id&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let id = "id_example"; // String | The UUID for the `EmployeeWage` being retrieved.
apiInstance.getEmployeeWage(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The UUID for the &#x60;EmployeeWage&#x60; being retrieved. | 

### Return type

[**GetEmployeeWageResponse**](GetEmployeeWageResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShift

> GetShiftResponse getShift(id)

GetShift

Returns a single &#x60;Shift&#x60; specified by &#x60;id&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let id = "id_example"; // String | The UUID for the `Shift` being retrieved.
apiInstance.getShift(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The UUID for the &#x60;Shift&#x60; being retrieved. | 

### Return type

[**GetShiftResponse**](GetShiftResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamMemberWage

> GetTeamMemberWageResponse getTeamMemberWage(id)

GetTeamMemberWage

Returns a single &#x60;TeamMemberWage&#x60; specified by &#x60;id &#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let id = "id_example"; // String | The UUID for the `TeamMemberWage` being retrieved.
apiInstance.getTeamMemberWage(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The UUID for the &#x60;TeamMemberWage&#x60; being retrieved. | 

### Return type

[**GetTeamMemberWageResponse**](GetTeamMemberWageResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBreakTypes

> ListBreakTypesResponse listBreakTypes(opts)

ListBreakTypes

Returns a paginated list of &#x60;BreakType&#x60; instances for a business.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let opts = {
  'locationId': "locationId_example", // String | Filter the returned `BreakType` results to only those that are associated with the specified location.
  'limit': 56, // Number | The maximum number of `BreakType` results to return per page. The number can range between 1 and 200. The default is 200.
  'cursor': "cursor_example" // String | A pointer to the next page of `BreakType` results to fetch.
};
apiInstance.listBreakTypes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locationId** | **String**| Filter the returned &#x60;BreakType&#x60; results to only those that are associated with the specified location. | [optional] 
 **limit** | **Number**| The maximum number of &#x60;BreakType&#x60; results to return per page. The number can range between 1 and 200. The default is 200. | [optional] 
 **cursor** | **String**| A pointer to the next page of &#x60;BreakType&#x60; results to fetch. | [optional] 

### Return type

[**ListBreakTypesResponse**](ListBreakTypesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEmployeeWages

> ListEmployeeWagesResponse listEmployeeWages(opts)

ListEmployeeWages

Returns a paginated list of &#x60;EmployeeWage&#x60; instances for a business.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let opts = {
  'employeeId': "employeeId_example", // String | Filter the returned wages to only those that are associated with the specified employee.
  'limit': 56, // Number | The maximum number of `EmployeeWage` results to return per page. The number can range between 1 and 200. The default is 200.
  'cursor': "cursor_example" // String | A pointer to the next page of `EmployeeWage` results to fetch.
};
apiInstance.listEmployeeWages(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employeeId** | **String**| Filter the returned wages to only those that are associated with the specified employee. | [optional] 
 **limit** | **Number**| The maximum number of &#x60;EmployeeWage&#x60; results to return per page. The number can range between 1 and 200. The default is 200. | [optional] 
 **cursor** | **String**| A pointer to the next page of &#x60;EmployeeWage&#x60; results to fetch. | [optional] 

### Return type

[**ListEmployeeWagesResponse**](ListEmployeeWagesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTeamMemberWages

> ListTeamMemberWagesResponse listTeamMemberWages(opts)

ListTeamMemberWages

Returns a paginated list of &#x60;TeamMemberWage&#x60; instances for a business.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let opts = {
  'teamMemberId': "teamMemberId_example", // String | Filter the returned wages to only those that are associated with the specified team member.
  'limit': 56, // Number | The maximum number of `TeamMemberWage` results to return per page. The number can range between 1 and 200. The default is 200.
  'cursor': "cursor_example" // String | A pointer to the next page of `EmployeeWage` results to fetch.
};
apiInstance.listTeamMemberWages(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamMemberId** | **String**| Filter the returned wages to only those that are associated with the specified team member. | [optional] 
 **limit** | **Number**| The maximum number of &#x60;TeamMemberWage&#x60; results to return per page. The number can range between 1 and 200. The default is 200. | [optional] 
 **cursor** | **String**| A pointer to the next page of &#x60;EmployeeWage&#x60; results to fetch. | [optional] 

### Return type

[**ListTeamMemberWagesResponse**](ListTeamMemberWagesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWorkweekConfigs

> ListWorkweekConfigsResponse listWorkweekConfigs(opts)

ListWorkweekConfigs

Returns a list of &#x60;WorkweekConfig&#x60; instances for a business.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let opts = {
  'limit': 56, // Number | The maximum number of `WorkweekConfigs` results to return per page.
  'cursor': "cursor_example" // String | A pointer to the next page of `WorkweekConfig` results to fetch.
};
apiInstance.listWorkweekConfigs(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **Number**| The maximum number of &#x60;WorkweekConfigs&#x60; results to return per page. | [optional] 
 **cursor** | **String**| A pointer to the next page of &#x60;WorkweekConfig&#x60; results to fetch. | [optional] 

### Return type

[**ListWorkweekConfigsResponse**](ListWorkweekConfigsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchShifts

> SearchShiftsResponse searchShifts(searchShiftsRequest)

SearchShifts

Returns a paginated list of &#x60;Shift&#x60; records for a business. The list to be returned can be filtered by: - Location IDs. - Employee IDs. - Shift status (&#x60;OPEN&#x60; and &#x60;CLOSED&#x60;). - Shift start. - Shift end. - Workday details.  The list can be sorted by: - &#x60;start_at&#x60;. - &#x60;end_at&#x60;. - &#x60;created_at&#x60;. - &#x60;updated_at&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let searchShiftsRequest = new SquareConnectApi.SearchShiftsRequest(); // SearchShiftsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchShifts(searchShiftsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchShiftsRequest** | [**SearchShiftsRequest**](SearchShiftsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchShiftsResponse**](SearchShiftsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBreakType

> UpdateBreakTypeResponse updateBreakType(id, updateBreakTypeRequest)

UpdateBreakType

Updates an existing &#x60;BreakType&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let id = "id_example"; // String |  The UUID for the `BreakType` being updated.
let updateBreakTypeRequest = new SquareConnectApi.UpdateBreakTypeRequest(); // UpdateBreakTypeRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updateBreakType(id, updateBreakTypeRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  The UUID for the &#x60;BreakType&#x60; being updated. | 
 **updateBreakTypeRequest** | [**UpdateBreakTypeRequest**](UpdateBreakTypeRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpdateBreakTypeResponse**](UpdateBreakTypeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateShift

> UpdateShiftResponse updateShift(id, updateShiftRequest)

UpdateShift

Updates an existing &#x60;Shift&#x60;.  When adding a &#x60;Break&#x60; to a &#x60;Shift&#x60;, any earlier &#x60;Break&#x60; instances in the &#x60;Shift&#x60; have the &#x60;end_at&#x60; property set to a valid RFC-3339 datetime string.  When closing a &#x60;Shift&#x60;, all &#x60;Break&#x60; instances in the &#x60;Shift&#x60; must be complete with &#x60;end_at&#x60; set on each &#x60;Break&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let id = "id_example"; // String | The ID of the object being updated.
let updateShiftRequest = new SquareConnectApi.UpdateShiftRequest(); // UpdateShiftRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updateShift(id, updateShiftRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the object being updated. | 
 **updateShiftRequest** | [**UpdateShiftRequest**](UpdateShiftRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpdateShiftResponse**](UpdateShiftResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWorkweekConfig

> UpdateWorkweekConfigResponse updateWorkweekConfig(id, updateWorkweekConfigRequest)

UpdateWorkweekConfig

Updates a &#x60;WorkweekConfig&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LaborApi();
let id = "id_example"; // String | The UUID for the `WorkweekConfig` object being updated.
let updateWorkweekConfigRequest = new SquareConnectApi.UpdateWorkweekConfigRequest(); // UpdateWorkweekConfigRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updateWorkweekConfig(id, updateWorkweekConfigRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The UUID for the &#x60;WorkweekConfig&#x60; object being updated. | 
 **updateWorkweekConfigRequest** | [**UpdateWorkweekConfigRequest**](UpdateWorkweekConfigRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpdateWorkweekConfigResponse**](UpdateWorkweekConfigResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

