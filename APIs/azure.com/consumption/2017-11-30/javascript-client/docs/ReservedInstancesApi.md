# ConsumptionManagementClient.ReservedInstancesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationsDetailsList**](ReservedInstancesApi.md#reservationsDetailsList) | **GET** /{scope}/providers/Microsoft.Consumption/reservationDetails | 
[**reservationsSummariesList**](ReservedInstancesApi.md#reservationsSummariesList) | **GET** /{scope}/providers/Microsoft.Consumption/reservationSummaries | 



## reservationsDetailsList

> ReservationDetailsListResult reservationsDetailsList(scope, filter, apiVersion)



Lists the reservations details for provided date range.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ReservedInstancesApi();
let scope = "scope_example"; // String | The scope of the reservation details. The scope can be 'providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}' or 'providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}/reservations/{ReservationId}'
let filter = "filter_example"; // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-11-30.
apiInstance.reservationsDetailsList(scope, filter, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the reservation details. The scope can be &#39;providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}&#39; or &#39;providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}/reservations/{ReservationId}&#39; | 
 **filter** | **String**| Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;  | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-11-30. | 

### Return type

[**ReservationDetailsListResult**](ReservationDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reservationsSummariesList

> ReservationSummariesListResult reservationsSummariesList(scope, grain, apiVersion, opts)



Lists the reservations summaries for daily or monthly grain.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ReservedInstancesApi();
let scope = "scope_example"; // String | The scope of the reservation summaries. The scope can be 'providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}' or 'providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}/reservations/{ReservationId}'
let grain = "grain_example"; // String | Can be daily or monthly
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-11-30.
let opts = {
  'filter': "filter_example" // String | Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge'
};
apiInstance.reservationsSummariesList(scope, grain, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| The scope of the reservation summaries. The scope can be &#39;providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}&#39; or &#39;providers/Microsoft.Capacity/reservationorders/{ReservationOrderId}/reservations/{ReservationId}&#39; | 
 **grain** | **String**| Can be daily or monthly | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-11-30. | 
 **filter** | **String**| Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39; | [optional] 

### Return type

[**ReservationSummariesListResult**](ReservationSummariesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

