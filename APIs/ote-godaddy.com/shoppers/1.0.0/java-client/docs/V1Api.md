# V1Api

All URIs are relative to *http://api.ote-godaddy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changePassword**](V1Api.md#changePassword) | **PUT** /v1/shoppers/{shopperId}/factors/password | Set subaccount&#39;s password |
| [**createSubaccount**](V1Api.md#createSubaccount) | **POST** /v1/shoppers/subaccount | Create a Subaccount owned by the authenticated Reseller |
| [**delete**](V1Api.md#delete) | **DELETE** /v1/shoppers/{shopperId} | Request the deletion of a shopper profile |
| [**get**](V1Api.md#get) | **GET** /v1/shoppers/{shopperId} | Get details for the specified Shopper |
| [**getStatus**](V1Api.md#getStatus) | **GET** /v1/shoppers/{shopperId}/status | Get details for the specified Shopper |
| [**update**](V1Api.md#update) | **POST** /v1/shoppers/{shopperId} | Update details for the specified Shopper |


<a id="changePassword"></a>
# **changePassword**
> ShopperId changePassword(shopperId, secret)

Set subaccount&#39;s password

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;Password set is only supported by API Resellers setting subaccount passwords.&lt;/li&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String shopperId = "shopperId_example"; // String | Shopper whose password will be set
    Secret secret = new Secret(); // Secret | The value to set the subaccount's password to
    try {
      ShopperId result = apiInstance.changePassword(shopperId, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#changePassword");
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
| **shopperId** | **String**| Shopper whose password will be set | |
| **secret** | [**Secret**](Secret.md)| The value to set the subaccount&#39;s password to | |

### Return type

[**ShopperId**](ShopperId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was not successful |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **500** | Internal server error |  -  |

<a id="createSubaccount"></a>
# **createSubaccount**
> ShopperId createSubaccount(subaccountCreate)

Create a Subaccount owned by the authenticated Reseller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    SubaccountCreate subaccountCreate = new SubaccountCreate(); // SubaccountCreate | The subaccount to create
    try {
      ShopperId result = apiInstance.createSubaccount(subaccountCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#createSubaccount");
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
| **subaccountCreate** | [**SubaccountCreate**](SubaccountCreate.md)| The subaccount to create | |

### Return type

[**ShopperId**](ShopperId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/xml
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **422** | &#x60;subaccount&#x60; does not fulfill the schema |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

<a id="delete"></a>
# **delete**
> delete(shopperId, auditClientIp)

Request the deletion of a shopper profile

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;Shopper deletion is not supported in OTE&lt;/li&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String shopperId = "shopperId_example"; // String | The ID of the shopper to delete. Must agree with the shopper id on the token or header, if present. *Note*: **shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)
    String auditClientIp = "auditClientIp_example"; // String | The client IP of the user who originated the request leading to this call.
    try {
      apiInstance.delete(shopperId, auditClientIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#delete");
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
| **shopperId** | **String**| The ID of the shopper to delete. Must agree with the shopper id on the token or header, if present. *Note*: **shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13) | |
| **auditClientIp** | **String**| The client IP of the user who originated the request leading to this call. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Resource not found |  -  |
| **409** | Active and locked shoppers cannot be deleted |  -  |
| **422** | Shopper ID is not supplied or invalid |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

<a id="get"></a>
# **get**
> Shopper get(shopperId, includes)

Get details for the specified Shopper

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String shopperId = "shopperId_example"; // String | Shopper whose details are to be retrieved
    List<String> includes = Arrays.asList(); // List<String> | Additional properties to be included in the response shopper object
    try {
      Shopper result = apiInstance.get(shopperId, includes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#get");
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
| **shopperId** | **String**| Shopper whose details are to be retrieved | |
| **includes** | [**List&lt;String&gt;**](String.md)| Additional properties to be included in the response shopper object | [optional] [enum: customerId] |

### Return type

[**Shopper**](Shopper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

<a id="getStatus"></a>
# **getStatus**
> ShopperStatus getStatus(shopperId, auditClientIp)

Get details for the specified Shopper

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**. **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String shopperId = "shopperId_example"; // String | The ID of the shopper to retrieve. Must agree with the shopper id on the token or header, if present
    String auditClientIp = "auditClientIp_example"; // String | The client IP of the user who originated the request leading to this call.
    try {
      ShopperStatus result = apiInstance.getStatus(shopperId, auditClientIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#getStatus");
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
| **shopperId** | **String**| The ID of the shopper to retrieve. Must agree with the shopper id on the token or header, if present | |
| **auditClientIp** | **String**| The client IP of the user who originated the request leading to this call. | |

### Return type

[**ShopperStatus**](ShopperStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Resource not found |  -  |
| **422** | Shopper ID is not supplied or invalid |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

<a id="update"></a>
# **update**
> ShopperId update(shopperId, shopperUpdate)

Update details for the specified Shopper

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String shopperId = "shopperId_example"; // String | The ID of the Shopper to update
    ShopperUpdate shopperUpdate = new ShopperUpdate(); // ShopperUpdate | The Shopper details to update
    try {
      ShopperId result = apiInstance.update(shopperId, shopperUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#update");
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
| **shopperId** | **String**| The ID of the Shopper to update | |
| **shopperUpdate** | [**ShopperUpdate**](ShopperUpdate.md)| The Shopper details to update | |

### Return type

[**ShopperId**](ShopperId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/xml
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Resource not found |  -  |
| **422** | &#x60;Shopper&#x60; does not fulfill the schema |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

