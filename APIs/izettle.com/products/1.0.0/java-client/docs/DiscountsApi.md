# DiscountsApi

All URIs are relative to *https://products.izettle.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDiscount**](DiscountsApi.md#createDiscount) | **POST** /organizations/{organizationUuid}/discounts | Create a discount |
| [**deleteDiscount**](DiscountsApi.md#deleteDiscount) | **DELETE** /organizations/{organizationUuid}/discounts/{discountUuid} | Delete a single discount  |
| [**getAllDiscounts**](DiscountsApi.md#getAllDiscounts) | **GET** /organizations/{organizationUuid}/discounts | Retrieve all discounts |
| [**getDiscount**](DiscountsApi.md#getDiscount) | **GET** /organizations/{organizationUuid}/discounts/{discountUuid} | Retrieve a single discount |
| [**updateDiscount**](DiscountsApi.md#updateDiscount) | **PUT** /organizations/{organizationUuid}/discounts/{discountUuid} | Update a single discount |


<a id="createDiscount"></a>
# **createDiscount**
> createDiscount(organizationUuid, discountRequest)

Create a discount

Creates a single discount entity. The location of the newly created discount will be available in the successful response as a HttpHeaders.LOCATION header

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    DiscountsApi apiInstance = new DiscountsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    DiscountRequest discountRequest = new DiscountRequest(); // DiscountRequest | 
    try {
      apiInstance.createDiscount(organizationUuid, discountRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscountsApi#createDiscount");
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
| **organizationUuid** | **UUID**|  | |
| **discountRequest** | [**DiscountRequest**](DiscountRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Discount created |  * ETag - ETag value <br>  * Location - Location of updated product <br>  |
| **400** | Invalid request body |  -  |

<a id="deleteDiscount"></a>
# **deleteDiscount**
> deleteDiscount(organizationUuid, discountUuid)

Delete a single discount 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    DiscountsApi apiInstance = new DiscountsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    UUID discountUuid = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.deleteDiscount(organizationUuid, discountUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscountsApi#deleteDiscount");
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
| **organizationUuid** | **UUID**|  | |
| **discountUuid** | **UUID**|  | |

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Discount deleted |  -  |
| **404** | Organization or Discount not found |  -  |

<a id="getAllDiscounts"></a>
# **getAllDiscounts**
> List&lt;DiscountResponse&gt; getAllDiscounts(organizationUuid)

Retrieve all discounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    DiscountsApi apiInstance = new DiscountsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    try {
      List<DiscountResponse> result = apiInstance.getAllDiscounts(organizationUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscountsApi#getAllDiscounts");
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
| **organizationUuid** | **UUID**|  | |

### Return type

[**List&lt;DiscountResponse&gt;**](DiscountResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all discounts |  -  |

<a id="getDiscount"></a>
# **getDiscount**
> DiscountResponse getDiscount(organizationUuid, discountUuid, ifNoneMatch)

Retrieve a single discount

Get the full discount with the provided UUID. The method supports conditional GET through providing a HttpHeaders.IF_NONE_MATCH header. If the conditional prerequisite is fullfilled, the full discount is returned: otherwise a 304 not modified will be returned with an empty body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    DiscountsApi apiInstance = new DiscountsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    UUID discountUuid = UUID.randomUUID(); // UUID | 
    String ifNoneMatch = "ifNoneMatch_example"; // String | 
    try {
      DiscountResponse result = apiInstance.getDiscount(organizationUuid, discountUuid, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscountsApi#getDiscount");
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
| **organizationUuid** | **UUID**|  | |
| **discountUuid** | **UUID**|  | |
| **ifNoneMatch** | **String**|  | [optional] |

### Return type

[**DiscountResponse**](DiscountResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discount |  * ETag - ETag value <br>  |
| **304** | Not modified |  -  |
| **404** | Organization or Discount not found |  -  |

<a id="updateDiscount"></a>
# **updateDiscount**
> updateDiscount(organizationUuid, discountUuid, discountRequest, ifMatch)

Update a single discount

Updates a discount entity using JSON merge patch (https://tools.ietf.org/html/rfc7386). This means that only included fields will be changed: null values removes the field on the target entity, and other values updates the field. Conditional updates are supported through the HttpHeaders.IF_MATCH header. If the conditional prerequisite is fullfilled, the discount is updated: otherwise a 412 precondition failed will be returned with an empty body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    DiscountsApi apiInstance = new DiscountsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    UUID discountUuid = UUID.randomUUID(); // UUID | 
    DiscountRequest discountRequest = new DiscountRequest(); // DiscountRequest | 
    String ifMatch = "ifMatch_example"; // String | 
    try {
      apiInstance.updateDiscount(organizationUuid, discountUuid, discountRequest, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscountsApi#updateDiscount");
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
| **organizationUuid** | **UUID**|  | |
| **discountUuid** | **UUID**|  | |
| **discountRequest** | [**DiscountRequest**](DiscountRequest.md)|  | |
| **ifMatch** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Discount updated |  * ETag - ETag value <br>  * Location - Location of updated product <br>  |
| **400** | Invalid request body |  -  |
| **412** | Precondition failed: ETag did not match the expected value |  -  |

