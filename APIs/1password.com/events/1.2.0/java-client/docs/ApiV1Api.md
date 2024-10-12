# ApiV1Api

All URIs are relative to *https://events.1password.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAuditEvents**](ApiV1Api.md#getAuditEvents) | **POST** /api/v1/auditevents | Retrieves audit events for actions performed by team members within a 1Password account |
| [**getItemUsages**](ApiV1Api.md#getItemUsages) | **POST** /api/v1/itemusages | Retrieves events for each usage of an item stored in a shared vault within a 1Password account |
| [**getSignInAttempts**](ApiV1Api.md#getSignInAttempts) | **POST** /api/v1/signinattempts | Retrieves events for both successful and failed attempts to sign into a 1Password account |


<a id="getAuditEvents"></a>
# **getAuditEvents**
> AuditEventItems getAuditEvents()

Retrieves audit events for actions performed by team members within a 1Password account

This endpoint requires your JSON Web Token to have the *auditevents* feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.1password.com");
    
    // Configure HTTP bearer authorization: jwtsa
    HttpBearerAuth jwtsa = (HttpBearerAuth) defaultClient.getAuthentication("jwtsa");
    jwtsa.setBearerToken("BEARER TOKEN");

    ApiV1Api apiInstance = new ApiV1Api(defaultClient);
    try {
      AuditEventItems result = apiInstance.getAuditEvents();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV1Api#getAuditEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditEventItems**](AuditEventItems.md)

### Authorization

[jwtsa](../README.md#jwtsa)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audit events response object |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |
| **0** | Generic error |  -  |

<a id="getItemUsages"></a>
# **getItemUsages**
> ItemUsageItems getItemUsages()

Retrieves events for each usage of an item stored in a shared vault within a 1Password account

This endpoint requires your JSON Web Token to have the *itemusages* feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.1password.com");
    
    // Configure HTTP bearer authorization: jwtsa
    HttpBearerAuth jwtsa = (HttpBearerAuth) defaultClient.getAuthentication("jwtsa");
    jwtsa.setBearerToken("BEARER TOKEN");

    ApiV1Api apiInstance = new ApiV1Api(defaultClient);
    try {
      ItemUsageItems result = apiInstance.getItemUsages();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV1Api#getItemUsages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ItemUsageItems**](ItemUsageItems.md)

### Authorization

[jwtsa](../README.md#jwtsa)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item usages response object |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |
| **0** | Generic error |  -  |

<a id="getSignInAttempts"></a>
# **getSignInAttempts**
> SignInAttemptItems getSignInAttempts()

Retrieves events for both successful and failed attempts to sign into a 1Password account

This endpoint requires your JSON Web Token to have the *signinattempts* feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiV1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.1password.com");
    
    // Configure HTTP bearer authorization: jwtsa
    HttpBearerAuth jwtsa = (HttpBearerAuth) defaultClient.getAuthentication("jwtsa");
    jwtsa.setBearerToken("BEARER TOKEN");

    ApiV1Api apiInstance = new ApiV1Api(defaultClient);
    try {
      SignInAttemptItems result = apiInstance.getSignInAttempts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiV1Api#getSignInAttempts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SignInAttemptItems**](SignInAttemptItems.md)

### Authorization

[jwtsa](../README.md#jwtsa)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sign-in attempts response object |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |
| **0** | Generic error |  -  |

