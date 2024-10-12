# AzureReservation.AppliedReservationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAppliedReservationList**](AppliedReservationApi.md#getAppliedReservationList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Capacity/appliedReservations | Get list of applicable &#x60;Reservation&#x60;s.



## getAppliedReservationList

> AppliedReservations getAppliedReservationList(apiVersion, subscriptionId)

Get list of applicable &#x60;Reservation&#x60;s.

Get applicable &#x60;Reservation&#x60;s that are applied to this subscription or a resource group under this subscription.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.AppliedReservationApi();
let apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
let subscriptionId = "subscriptionId_example"; // String | Id of the subscription
apiInstance.getAppliedReservationList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Supported version for this document is 2019-04-01 | 
 **subscriptionId** | **String**| Id of the subscription | 

### Return type

[**AppliedReservations**](AppliedReservations.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

