# AddressRequestsApi

All URIs are relative to *https://eu.eth.chaingateway.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAddress**](AddressRequestsApi.md#deleteAddress) | **POST** /deleteAddress | deleteAddress |
| [**exportAddress**](AddressRequestsApi.md#exportAddress) | **POST** /exportAddress | exportAddress |
| [**importAddress**](AddressRequestsApi.md#importAddress) | **POST** /importAddress | importAddress |
| [**listAddresses**](AddressRequestsApi.md#listAddresses) | **POST** /listAddresses | listAddresses |
| [**newAddress**](AddressRequestsApi.md#newAddress) | **POST** /newAddress | newAddress |


<a id="deleteAddress"></a>
# **deleteAddress**
> DeleteAddress deleteAddress(authorization, deleteAddressRequest)

deleteAddress

Deletes an existing ethereum address. Be careful when using this function.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    AddressRequestsApi apiInstance = new AddressRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    DeleteAddressRequest deleteAddressRequest = new DeleteAddressRequest(); // DeleteAddressRequest | 
    try {
      DeleteAddress result = apiInstance.deleteAddress(authorization, deleteAddressRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressRequestsApi#deleteAddress");
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
| **authorization** | **String**| API Key | |
| **deleteAddressRequest** | [**DeleteAddressRequest**](DeleteAddressRequest.md)|  | |

### Return type

[**DeleteAddress**](DeleteAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="exportAddress"></a>
# **exportAddress**
> ExportAddress exportAddress(authorization, exportAddressRequest)

exportAddress

Returns all ethereum addresses created with an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    AddressRequestsApi apiInstance = new AddressRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    ExportAddressRequest exportAddressRequest = new ExportAddressRequest(); // ExportAddressRequest | 
    try {
      ExportAddress result = apiInstance.exportAddress(authorization, exportAddressRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressRequestsApi#exportAddress");
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
| **authorization** | **String**| API Key | |
| **exportAddressRequest** | [**ExportAddressRequest**](ExportAddressRequest.md)|  | |

### Return type

[**ExportAddress**](ExportAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="importAddress"></a>
# **importAddress**
> ImportAddress importAddress(authorization, importAddressRequest)

importAddress

Returns all ethereum addresses created with an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    AddressRequestsApi apiInstance = new AddressRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    ImportAddressRequest importAddressRequest = new ImportAddressRequest(); // ImportAddressRequest | 
    try {
      ImportAddress result = apiInstance.importAddress(authorization, importAddressRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressRequestsApi#importAddress");
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
| **authorization** | **String**| API Key | |
| **importAddressRequest** | [**ImportAddressRequest**](ImportAddressRequest.md)|  | |

### Return type

[**ImportAddress**](ImportAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="listAddresses"></a>
# **listAddresses**
> ListAddresses listAddresses(contentType, authorization)

listAddresses

Returns all ethereum addresses created with an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    AddressRequestsApi apiInstance = new AddressRequestsApi(defaultClient);
    String contentType = "application/json"; // String | 
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    try {
      ListAddresses result = apiInstance.listAddresses(contentType, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressRequestsApi#listAddresses");
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
| **contentType** | **String**|  | |
| **authorization** | **String**| API Key | |

### Return type

[**ListAddresses**](ListAddresses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="newAddress"></a>
# **newAddress**
> NewAddress newAddress(authorization, newAddressRequest)

newAddress

Generates a new ethereum addresses you can use to send or receive funds. Do not lose the password! We can&#39;t restore access to an address if you lose it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    AddressRequestsApi apiInstance = new AddressRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    NewAddressRequest newAddressRequest = new NewAddressRequest(); // NewAddressRequest | 
    try {
      NewAddress result = apiInstance.newAddress(authorization, newAddressRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressRequestsApi#newAddress");
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
| **authorization** | **String**| API Key | |
| **newAddressRequest** | [**NewAddressRequest**](NewAddressRequest.md)|  | |

### Return type

[**NewAddress**](NewAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

