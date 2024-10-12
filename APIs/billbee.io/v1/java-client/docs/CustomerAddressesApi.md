# CustomerAddressesApi

All URIs are relative to *https://app.billbee.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAddressesCreate**](CustomerAddressesApi.md#customerAddressesCreate) | **POST** /api/v1/customer-addresses | Creates a new customer address |
| [**customerAddressesGetAll**](CustomerAddressesApi.md#customerAddressesGetAll) | **GET** /api/v1/customer-addresses | Get a list of all customer addresses |
| [**customerAddressesGetOne**](CustomerAddressesApi.md#customerAddressesGetOne) | **GET** /api/v1/customer-addresses/{id} | Queries a single customer address by id |
| [**customerAddressesUpdate**](CustomerAddressesApi.md#customerAddressesUpdate) | **PUT** /api/v1/customer-addresses/{id} | Updates a customer address by id |


<a id="customerAddressesCreate"></a>
# **customerAddressesCreate**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerAddressesCreate(billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel)

Creates a new customer address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomerAddressesApi apiInstance = new CustomerAddressesApi(defaultClient);
    BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel = new BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel(); // BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel | 
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel result = apiInstance.customerAddressesCreate(billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAddressesApi#customerAddressesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel** | [**BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)|  | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customerAddressesGetAll"></a>
# **customerAddressesGetAll**
> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerAddressesGetAll(page, pageSize)

Get a list of all customer addresses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomerAddressesApi apiInstance = new CustomerAddressesApi(defaultClient);
    Integer page = 56; // Integer | The current page to request starting with 1 (default is 1)
    Integer pageSize = 56; // Integer | The page size for the result list. Values between 1 and 250 are allowed. (default is 50)
    try {
      RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel result = apiInstance.customerAddressesGetAll(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAddressesApi#customerAddressesGetAll");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| The current page to request starting with 1 (default is 1) | [optional] |
| **pageSize** | **Integer**| The page size for the result list. Values between 1 and 250 are allowed. (default is 50) | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customerAddressesGetOne"></a>
# **customerAddressesGetOne**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerAddressesGetOne(id)

Queries a single customer address by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomerAddressesApi apiInstance = new CustomerAddressesApi(defaultClient);
    Long id = 56L; // Long | The id of the address to query
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel result = apiInstance.customerAddressesGetOne(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAddressesApi#customerAddressesGetOne");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| The id of the address to query | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customerAddressesUpdate"></a>
# **customerAddressesUpdate**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerAddressesUpdate(id, billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel)

Updates a customer address by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomerAddressesApi apiInstance = new CustomerAddressesApi(defaultClient);
    Long id = 56L; // Long | The id of the address
    BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel = new BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel(); // BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel | 
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel result = apiInstance.customerAddressesUpdate(id, billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAddressesApi#customerAddressesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| The id of the address | |
| **billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel** | [**BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)|  | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

