# CustomersApi

All URIs are relative to *https://app.billbee.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAddCustomerAddress**](CustomersApi.md#customerAddCustomerAddress) | **POST** /api/v1/customers/{id}/addresses | Adds a new address to a customer |
| [**customerCreate**](CustomersApi.md#customerCreate) | **POST** /api/v1/customers | Creates a new customer |
| [**customerGetAll**](CustomersApi.md#customerGetAll) | **GET** /api/v1/customers | Get a list of all customers |
| [**customerGetCustomerAddress**](CustomersApi.md#customerGetCustomerAddress) | **GET** /api/v1/customers/addresses/{id} | Queries a single address from a customer |
| [**customerGetCustomerAddresses**](CustomersApi.md#customerGetCustomerAddresses) | **GET** /api/v1/customers/{id}/addresses | Queries a list of addresses from a customer |
| [**customerGetCustomerOrders**](CustomersApi.md#customerGetCustomerOrders) | **GET** /api/v1/customers/{id}/orders | Queries a list of orders from a customer |
| [**customerGetOne**](CustomersApi.md#customerGetOne) | **GET** /api/v1/customers/{id} | Queries a single customer by id |
| [**customerPatchAddress**](CustomersApi.md#customerPatchAddress) | **PATCH** /api/v1/customers/addresses/{id} | Updates one or more fields of an address |
| [**customerUpdate**](CustomersApi.md#customerUpdate) | **PUT** /api/v1/customers/{id} | Updates a customer by id |
| [**customerUpdateAddress**](CustomersApi.md#customerUpdateAddress) | **PUT** /api/v1/customers/addresses/{id} | Updates all fields of an address |
| [**searchSearch_0**](CustomersApi.md#searchSearch_0) | **POST** /api/v1/search | Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax |


<a id="customerAddCustomerAddress"></a>
# **customerAddCustomerAddress**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerAddCustomerAddress(id, billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel)

Adds a new address to a customer

Id and  CustomerId will be ignored in model. If Id is set, the addition will be stopped.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long id = 56L; // Long | CustomerId to attach the new address to.
    BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel = new BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel(); // BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel | Model containing the address, that should be attached.
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel result = apiInstance.customerAddCustomerAddress(id, billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customerAddCustomerAddress");
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
| **id** | **Long**| CustomerId to attach the new address to. | |
| **billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel** | [**BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)| Model containing the address, that should be attached. | |

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

<a id="customerCreate"></a>
# **customerCreate**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel customerCreate(billbeeInterfacesBillbeeAPIModelCreateCustomerApiModel)

Creates a new customer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel billbeeInterfacesBillbeeAPIModelCreateCustomerApiModel = new BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel(); // BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel | 
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel result = apiInstance.customerCreate(billbeeInterfacesBillbeeAPIModelCreateCustomerApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customerCreate");
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
| **billbeeInterfacesBillbeeAPIModelCreateCustomerApiModel** | [**BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel**](BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel.md)|  | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customerGetAll"></a>
# **customerGetAll**
> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel customerGetAll(page, pageSize)

Get a list of all customers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Integer page = 56; // Integer | The current page to request starting with 1
    Integer pageSize = 56; // Integer | The pagesize for the result list. Values between 1 and 250 are allowed
    try {
      RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel result = apiInstance.customerGetAll(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customerGetAll");
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
| **page** | **Integer**| The current page to request starting with 1 | [optional] |
| **pageSize** | **Integer**| The pagesize for the result list. Values between 1 and 250 are allowed | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customerGetCustomerAddress"></a>
# **customerGetCustomerAddress**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerGetCustomerAddress(id)

Queries a single address from a customer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long id = 56L; // Long | The id of the address
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel result = apiInstance.customerGetCustomerAddress(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customerGetCustomerAddress");
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

<a id="customerGetCustomerAddresses"></a>
# **customerGetCustomerAddresses**
> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerGetCustomerAddresses(id, page, pageSize)

Queries a list of addresses from a customer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long id = 56L; // Long | The id of the customer
    Integer page = 56; // Integer | The current page to request starting with 1
    Integer pageSize = 56; // Integer | The pagesize for the result list. Values between 1 and 250 are allowed
    try {
      RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel result = apiInstance.customerGetCustomerAddresses(id, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customerGetCustomerAddresses");
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
| **id** | **Long**| The id of the customer | |
| **page** | **Integer**| The current page to request starting with 1 | [optional] |
| **pageSize** | **Integer**| The pagesize for the result list. Values between 1 and 250 are allowed | [optional] |

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

<a id="customerGetCustomerOrders"></a>
# **customerGetCustomerOrders**
> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder customerGetCustomerOrders(id, page, pageSize)

Queries a list of orders from a customer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long id = 56L; // Long | The id of the customer
    Integer page = 56; // Integer | The current page to request starting with 1
    Integer pageSize = 56; // Integer | The pagesize for the result list. Values between 1 and 250 are allowed
    try {
      RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder result = apiInstance.customerGetCustomerOrders(id, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customerGetCustomerOrders");
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
| **id** | **Long**| The id of the customer | |
| **page** | **Integer**| The current page to request starting with 1 | [optional] |
| **pageSize** | **Integer**| The pagesize for the result list. Values between 1 and 250 are allowed | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customerGetOne"></a>
# **customerGetOne**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel customerGetOne(id)

Queries a single customer by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long id = 56L; // Long | The id of the customer to query
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel result = apiInstance.customerGetOne(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customerGetOne");
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
| **id** | **Long**| The id of the customer to query | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customerPatchAddress"></a>
# **customerPatchAddress**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerPatchAddress(id, body)

Updates one or more fields of an address

Id and CustomerId cannot be changed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long id = 56L; // Long | The id of the address
    Object body = null; // Object | The address fields to be changed. Please query an address via (todo) to see all fields. Note that Id and CustomerId cannot be changed.
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel result = apiInstance.customerPatchAddress(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customerPatchAddress");
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
| **body** | **Object**| The address fields to be changed. Please query an address via (todo) to see all fields. Note that Id and CustomerId cannot be changed. | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customerUpdate"></a>
# **customerUpdate**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel customerUpdate(id, billbeeInterfacesBillbeeAPIModelCustomerApiModel)

Updates a customer by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long id = 56L; // Long | The id of the customer
    BillbeeInterfacesBillbeeAPIModelCustomerApiModel billbeeInterfacesBillbeeAPIModelCustomerApiModel = new BillbeeInterfacesBillbeeAPIModelCustomerApiModel(); // BillbeeInterfacesBillbeeAPIModelCustomerApiModel | 
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel result = apiInstance.customerUpdate(id, billbeeInterfacesBillbeeAPIModelCustomerApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customerUpdate");
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
| **id** | **Long**| The id of the customer | |
| **billbeeInterfacesBillbeeAPIModelCustomerApiModel** | [**BillbeeInterfacesBillbeeAPIModelCustomerApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerApiModel.md)|  | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customerUpdateAddress"></a>
# **customerUpdateAddress**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerUpdateAddress(id, billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel)

Updates all fields of an address

Id and CustomerId cannot be changed. Fields you do not send will become empty.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    Long id = 56L; // Long | The id of the address
    BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel = new BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel(); // BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel | The updated address. Please query an address via (todo) to see all fields. Note that Id and CustomerId cannot be changed.
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel result = apiInstance.customerUpdateAddress(id, billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customerUpdateAddress");
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
| **billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel** | [**BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)| The updated address. Please query an address via (todo) to see all fields. Note that Id and CustomerId cannot be changed. | |

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

<a id="searchSearch_0"></a>
# **searchSearch_0**
> RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel searchSearch_0(rechnungsdruckWebAppControllersApiSearchControllerSearchModel)

Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    RechnungsdruckWebAppControllersApiSearchControllerSearchModel rechnungsdruckWebAppControllersApiSearchControllerSearchModel = new RechnungsdruckWebAppControllersApiSearchControllerSearchModel(); // RechnungsdruckWebAppControllersApiSearchControllerSearchModel | 
    try {
      RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel result = apiInstance.searchSearch_0(rechnungsdruckWebAppControllersApiSearchControllerSearchModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#searchSearch_0");
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
| **rechnungsdruckWebAppControllersApiSearchControllerSearchModel** | [**RechnungsdruckWebAppControllersApiSearchControllerSearchModel**](RechnungsdruckWebAppControllersApiSearchControllerSearchModel.md)|  | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel**](RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

