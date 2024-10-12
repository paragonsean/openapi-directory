# PersonnelData.DefaultApi

All URIs are relative to *https://api.personio.de/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyAttendancesGet**](DefaultApi.md#companyAttendancesGet) | **GET** /company/attendances | 
[**companyAttendancesIdDelete**](DefaultApi.md#companyAttendancesIdDelete) | **DELETE** /company/attendances/{id} | 
[**companyAttendancesIdPatch**](DefaultApi.md#companyAttendancesIdPatch) | **PATCH** /company/attendances/{id} | 
[**companyAttendancesPost**](DefaultApi.md#companyAttendancesPost) | **POST** /company/attendances | 
[**companyEmployeesEmployeeIdGet**](DefaultApi.md#companyEmployeesEmployeeIdGet) | **GET** /company/employees/{employee_id} | 
[**companyEmployeesEmployeeIdProfilePictureWidthGet**](DefaultApi.md#companyEmployeesEmployeeIdProfilePictureWidthGet) | **GET** /company/employees/{employee_id}/profile-picture/{width} | 
[**companyEmployeesGet**](DefaultApi.md#companyEmployeesGet) | **GET** /company/employees | 
[**companyEmployeesPost**](DefaultApi.md#companyEmployeesPost) | **POST** /company/employees | Create an employee
[**companyTimeOffTypesGet**](DefaultApi.md#companyTimeOffTypesGet) | **GET** /company/time-off-types | 
[**companyTimeOffsGet**](DefaultApi.md#companyTimeOffsGet) | **GET** /company/time-offs | 
[**companyTimeOffsIdDelete**](DefaultApi.md#companyTimeOffsIdDelete) | **DELETE** /company/time-offs/{id} | 
[**companyTimeOffsIdGet**](DefaultApi.md#companyTimeOffsIdGet) | **GET** /company/time-offs/{id} | 
[**companyTimeOffsPost**](DefaultApi.md#companyTimeOffsPost) | **POST** /company/time-offs | 



## companyAttendancesGet

> AttendancePeriodsResponse companyAttendancesGet(startDate, endDate, opts)



This endpoint is responsible for fetching attendance data for the company employees. It is possible to paginate results, filter by period, the date and/or time it was updated, and/or specific employees. The result will contain a list of attendance periods, structured as defined here.

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
let startDate = new Date("2013-10-20"); // Date | First day of the period to be queried. It is inclusive, so the day specified as start_date will also be considered on the results
let endDate = new Date("2013-10-20"); // Date | Last day of the period to be queried. It is inclusive, so the day specified as end_date will also be considered on the results.
let opts = {
  'updatedFrom': "updatedFrom_example", // String | Datetime from when the queried periods have been updated. Same format as updated_at. It is inclusive, so the day specified as updated_from will also be considered on the results. Can be just the date, or the date and the time, with or without the timezone.
  'updatedTo': "updatedTo_example", // String | Datetime until when the queried periods have been updated. Same format as updated_at. It is inclusive, so the day specified as updated_to will also be considered on the results. Can be just the date, or the date and the time, with or without the timezone.
  'employees': [null], // [Number] | A list of Personio employee identifiers to filter the results. Only those employees specified here will be returned.
  'limit': 200, // Number | Pagination attribute to limit how many attendances will be returned per page
  'offset': 0 // Number | Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned.
};
apiInstance.companyAttendancesGet(startDate, endDate, opts, (error, data, response) => {
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
 **startDate** | **Date**| First day of the period to be queried. It is inclusive, so the day specified as start_date will also be considered on the results | 
 **endDate** | **Date**| Last day of the period to be queried. It is inclusive, so the day specified as end_date will also be considered on the results. | 
 **updatedFrom** | **String**| Datetime from when the queried periods have been updated. Same format as updated_at. It is inclusive, so the day specified as updated_from will also be considered on the results. Can be just the date, or the date and the time, with or without the timezone. | [optional] 
 **updatedTo** | **String**| Datetime until when the queried periods have been updated. Same format as updated_at. It is inclusive, so the day specified as updated_to will also be considered on the results. Can be just the date, or the date and the time, with or without the timezone. | [optional] 
 **employees** | [**[Number]**](Number.md)| A list of Personio employee identifiers to filter the results. Only those employees specified here will be returned. | [optional] 
 **limit** | **Number**| Pagination attribute to limit how many attendances will be returned per page | [optional] [default to 200]
 **offset** | **Number**| Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned. | [optional] [default to 0]

### Return type

[**AttendancePeriodsResponse**](AttendancePeriodsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyAttendancesIdDelete

> Response companyAttendancesIdDelete(id)



This endpoint is responsible for deleting attendance data for the company employees.

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
let id = 56; // Number | ID of the attendance period to delete
apiInstance.companyAttendancesIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of the attendance period to delete | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyAttendancesIdPatch

> Response companyAttendancesIdPatch(id, updateAttendancePeriodRequest)



This endpoint is responsible for updating attendance data for the company employees. Attributes are not required and if not specified, the current value will be used. It is not possible to change the employee id.

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
let id = 56; // Number | ID of the attendance period to update
let updateAttendancePeriodRequest = new PersonnelData.UpdateAttendancePeriodRequest(); // UpdateAttendancePeriodRequest | attendance period data to update
apiInstance.companyAttendancesIdPatch(id, updateAttendancePeriodRequest, (error, data, response) => {
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
 **id** | **Number**| ID of the attendance period to update | 
 **updateAttendancePeriodRequest** | [**UpdateAttendancePeriodRequest**](UpdateAttendancePeriodRequest.md)| attendance period data to update | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## companyAttendancesPost

> NewAttendancePeriodResponse companyAttendancesPost(newAttendancePeriodRequest)



This endpoint is responsible for adding attendance data for the company employees. It is possible to add attendances for one or many employees at the same time. The payload sent on the request should be a list of attendance periods, in the form of an array containing attendance period objects.

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
let newAttendancePeriodRequest = new PersonnelData.NewAttendancePeriodRequest(); // NewAttendancePeriodRequest | List of attendance periods to create
apiInstance.companyAttendancesPost(newAttendancePeriodRequest, (error, data, response) => {
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
 **newAttendancePeriodRequest** | [**NewAttendancePeriodRequest**](NewAttendancePeriodRequest.md)| List of attendance periods to create | 

### Return type

[**NewAttendancePeriodResponse**](NewAttendancePeriodResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## companyEmployeesEmployeeIdGet

> EmployeeResponse companyEmployeesEmployeeIdGet(employeeId)



Show employee by ID

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
let employeeId = 56; // Number | Numeric `id` of the employee
apiInstance.companyEmployeesEmployeeIdGet(employeeId, (error, data, response) => {
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
 **employeeId** | **Number**| Numeric &#x60;id&#x60; of the employee | 

### Return type

[**EmployeeResponse**](EmployeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyEmployeesEmployeeIdProfilePictureWidthGet

> File companyEmployeesEmployeeIdProfilePictureWidthGet(employeeId, width)



Show employee profile picture

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
let employeeId = 56; // Number | Numeric `id` of the employee
let width = 56; // Number | Width of the image. Default 75x75
apiInstance.companyEmployeesEmployeeIdProfilePictureWidthGet(employeeId, width, (error, data, response) => {
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
 **employeeId** | **Number**| Numeric &#x60;id&#x60; of the employee | 
 **width** | **Number**| Width of the image. Default 75x75 | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png


## companyEmployeesGet

> EmployeesResponse companyEmployeesGet()



List Employees

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
apiInstance.companyEmployeesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**EmployeesResponse**](EmployeesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyEmployeesPost

> Response companyEmployeesPost(employeeEmail, employeeFirstName, employeeLastName, opts)

Create an employee

Creates new employee. Status of the employee will be set to &#x60;active&#x60; if &#x60;hire_date&#x60; provided is in past. Otherwise status will be set to &#x60;onboarding&#x60;. This endpoint will respond with &#x60;id&#x60; of created employee in case of success. 

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
let employeeEmail = "employeeEmail_example"; // String | Employee email
let employeeFirstName = "employeeFirstName_example"; // String | Employee first name
let employeeLastName = "employeeLastName_example"; // String | Employee last name
let opts = {
  'employeeDepartment': "employeeDepartment_example", // String | Employee department
  'employeeGender': "employeeGender_example", // String | Employee gender
  'employeeHireDate': new Date("2013-10-20"), // Date | Employee hire date
  'employeePosition': "employeePosition_example", // String | Employee position
  'employeeWeeklyHours': 3.4 // Number | Employee weekly working hours
};
apiInstance.companyEmployeesPost(employeeEmail, employeeFirstName, employeeLastName, opts, (error, data, response) => {
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
 **employeeEmail** | **String**| Employee email | 
 **employeeFirstName** | **String**| Employee first name | 
 **employeeLastName** | **String**| Employee last name | 
 **employeeDepartment** | **String**| Employee department | [optional] 
 **employeeGender** | **String**| Employee gender | [optional] 
 **employeeHireDate** | **Date**| Employee hire date | [optional] 
 **employeePosition** | **String**| Employee position | [optional] 
 **employeeWeeklyHours** | **Number**| Employee weekly working hours | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## companyTimeOffTypesGet

> CompanyTimeOffTypesGet200Response companyTimeOffTypesGet(opts)



Provides a list of available time-off types, for example &#39;Paid vacation&#39;, &#39;Parental leave&#39; or &#39;Home office&#39;

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
let opts = {
  'limit': 200, // Number | Pagination attribute to limit how many records will be returned per page
  'offset': 0 // Number | Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned.
};
apiInstance.companyTimeOffTypesGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Pagination attribute to limit how many records will be returned per page | [optional] [default to 200]
 **offset** | **Number**| Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned. | [optional] [default to 0]

### Return type

[**CompanyTimeOffTypesGet200Response**](CompanyTimeOffTypesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyTimeOffsGet

> AbsencePeriodsResponse companyTimeOffsGet(opts)



This endpoint is responsible for fetching absence data for the company employees. It is possible to paginate results, filter by period and/or specific employees. The result will contain a list of absence periods, structured as defined here.

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
let opts = {
  'startDate': new Date("2013-10-20"), // Date | First day of the period to be queried. It is inclusive, so the day specified as start_date will also be considered on the results
  'endDate': new Date("2013-10-20"), // Date | Last day of the period to be queried. It is inclusive, so the day specified as end_date will also be considered on the results.
  'updatedFrom': "updatedFrom_example", // String | Datetime from when the queried periods have been updated. It is inclusive, so the day specified as updated_from will also be considered on the results.
  'updatedTo': "updatedTo_example", // String | Datetime until when the queried periods have been updated. It is inclusive, so the day specified as updated_to will also be considered on the results.
  'employees': [null], // [Number] | A list of Personio employee identifiers to filter the results. Only those employees specified here will be returned.
  'limit': 200, // Number | Pagination attribute to limit how many attendances will be returned per page
  'offset': 0 // Number | Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned.
};
apiInstance.companyTimeOffsGet(opts, (error, data, response) => {
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
 **startDate** | **Date**| First day of the period to be queried. It is inclusive, so the day specified as start_date will also be considered on the results | [optional] 
 **endDate** | **Date**| Last day of the period to be queried. It is inclusive, so the day specified as end_date will also be considered on the results. | [optional] 
 **updatedFrom** | **String**| Datetime from when the queried periods have been updated. It is inclusive, so the day specified as updated_from will also be considered on the results. | [optional] 
 **updatedTo** | **String**| Datetime until when the queried periods have been updated. It is inclusive, so the day specified as updated_to will also be considered on the results. | [optional] 
 **employees** | [**[Number]**](Number.md)| A list of Personio employee identifiers to filter the results. Only those employees specified here will be returned. | [optional] 
 **limit** | **Number**| Pagination attribute to limit how many attendances will be returned per page | [optional] [default to 200]
 **offset** | **Number**| Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned. | [optional] [default to 0]

### Return type

[**AbsencePeriodsResponse**](AbsencePeriodsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyTimeOffsIdDelete

> Response companyTimeOffsIdDelete(id)



This endpoint is responsible for deleting absence period data for the company employees.

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
let id = 56; // Number | ID of the absence period to delete
apiInstance.companyTimeOffsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of the absence period to delete | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyTimeOffsIdGet

> Object companyTimeOffsIdGet(id)



Absence Period

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
let id = 56; // Number | Numeric `id` of the absence period
apiInstance.companyTimeOffsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Numeric &#x60;id&#x60; of the absence period | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companyTimeOffsPost

> CompanyTimeOffsPost201Response companyTimeOffsPost(createTimeOffPeriodRequest)



This endpoint is responsible for adding absence data for the company employees.

### Example

```javascript
import PersonnelData from 'personnel_data';

let apiInstance = new PersonnelData.DefaultApi();
let createTimeOffPeriodRequest = new PersonnelData.CreateTimeOffPeriodRequest(); // CreateTimeOffPeriodRequest | Absence period to create
apiInstance.companyTimeOffsPost(createTimeOffPeriodRequest, (error, data, response) => {
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
 **createTimeOffPeriodRequest** | [**CreateTimeOffPeriodRequest**](CreateTimeOffPeriodRequest.md)| Absence period to create | 

### Return type

[**CompanyTimeOffsPost201Response**](CompanyTimeOffsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

