# OriginTokenManagementInThisRegionApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createANewOriginTokenV1OriginTokenNewPost**](OriginTokenManagementInThisRegionApi.md#createANewOriginTokenV1OriginTokenNewPost) | **POST** /v1/origin_token/new | Create an origin token of the user in the region. |
| [**deleteTokenV1OriginTokenDelete**](OriginTokenManagementInThisRegionApi.md#deleteTokenV1OriginTokenDelete) | **DELETE** /v1/origin_token | Delete an origin token of the user in the region. |
| [**disableOriginTokenV1OriginTokenDisablePut**](OriginTokenManagementInThisRegionApi.md#disableOriginTokenV1OriginTokenDisablePut) | **PUT** /v1/origin_token/disable | Disable a enabled origin token of the user in the region. |
| [**enableOriginTokenV1OriginTokenEnablePut**](OriginTokenManagementInThisRegionApi.md#enableOriginTokenV1OriginTokenEnablePut) | **PUT** /v1/origin_token/enable | Enable a disabled origin token of the user in the region. |
| [**queryAllOriginTokensInTheRegionV1OriginTokenAllGet**](OriginTokenManagementInThisRegionApi.md#queryAllOriginTokensInTheRegionV1OriginTokenAllGet) | **GET** /v1/origin_token/all | Get the information of the origin tokens of the user in the region. |
| [**queryOriginTokenInfoV1OriginTokenPost**](OriginTokenManagementInThisRegionApi.md#queryOriginTokenInfoV1OriginTokenPost) | **POST** /v1/origin_token | Get the information of an origin token of the user in the region. |


<a id="createANewOriginTokenV1OriginTokenNewPost"></a>
# **createANewOriginTokenV1OriginTokenNewPost**
> OriginTokenOutput createANewOriginTokenV1OriginTokenNewPost(originTokenInput)

Create an origin token of the user in the region.

### What Creates a new origin token for the user passing as argument the origin. The origin parameter is the protocol and the domain where the origin token is valid.  The origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters The origin with the protocol and domain is required in the body of the request in the parameter &#x60;&#x60;origin&#x60;&#x60;. The allowed protocols are &#x60;&#x60;https://&#x60;&#x60;, and &#x60;&#x60;http://&#x60;&#x60;.  ### Result The result is a JSON object with the new origin token and the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual origin token information. - &#x60;&#x60;region_id&#x60;&#x60;: the name of the region where the origin token is valid. - &#x60;&#x60;origin&#x60;&#x60;: the protocol and the domain where the origin token is valid. - &#x60;&#x60;status&#x60;&#x60;: the status of the origin token. The only allowed values are &#x60;&#x60;ENABLED&#x60;&#x60; and &#x60;&#x60;DISABLED&#x60;&#x60;. - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin token was created in UNIX timestamp in milliseconds. - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin token was last updated in UNIX timestamp in milliseconds.  ### Errors It will return the API Global errors described in the API description.  It will also return the following errors: - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format. - a &#x60;409 Conflict&#x60; error if the origin token already exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginTokenManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginTokenManagementInThisRegionApi apiInstance = new OriginTokenManagementInThisRegionApi(defaultClient);
    OriginTokenInput originTokenInput = new OriginTokenInput(); // OriginTokenInput | 
    try {
      OriginTokenOutput result = apiInstance.createANewOriginTokenV1OriginTokenNewPost(originTokenInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginTokenManagementInThisRegionApi#createANewOriginTokenV1OriginTokenNewPost");
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
| **originTokenInput** | [**OriginTokenInput**](OriginTokenInput.md)|  | |

### Return type

[**OriginTokenOutput**](OriginTokenOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="deleteTokenV1OriginTokenDelete"></a>
# **deleteTokenV1OriginTokenDelete**
> Object deleteTokenV1OriginTokenDelete(bodyDeleteTokenV1OriginTokenDelete)

Delete an origin token of the user in the region.

### What Deletes the origin token passed as argument of the user in the selected region. Once the token is deleted, it will no longer be valid and the protocol and domain of the origin will no longer be under protection.  To delete an origin token, the user must be the owner and the token must be &#x60;&#x60;DISABLED&#x60;&#x60; first.  ### Parameters The Origin Token is required in the body of the request in the parameter &#x60;origin_token_id&#x60;.  ### Result If successful, the result will be an empty response with a status code of &#x60;204 No Content&#x60;.  ### Errors It will return the API Global errors described in the API description.  It will also return the following errors: - a &#x60;404 Not Found&#x60; error if the origin token is not found. - a &#x60;409 Conflict&#x60; error if the origin token is not disabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginTokenManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginTokenManagementInThisRegionApi apiInstance = new OriginTokenManagementInThisRegionApi(defaultClient);
    BodyDeleteTokenV1OriginTokenDelete bodyDeleteTokenV1OriginTokenDelete = new BodyDeleteTokenV1OriginTokenDelete(); // BodyDeleteTokenV1OriginTokenDelete | 
    try {
      Object result = apiInstance.deleteTokenV1OriginTokenDelete(bodyDeleteTokenV1OriginTokenDelete);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginTokenManagementInThisRegionApi#deleteTokenV1OriginTokenDelete");
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
| **bodyDeleteTokenV1OriginTokenDelete** | [**BodyDeleteTokenV1OriginTokenDelete**](BodyDeleteTokenV1OriginTokenDelete.md)|  | |

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="disableOriginTokenV1OriginTokenDisablePut"></a>
# **disableOriginTokenV1OriginTokenDisablePut**
> Object disableOriginTokenV1OriginTokenDisablePut(bodyDisableOriginTokenV1OriginTokenDisablePut)

Disable a enabled origin token of the user in the region.

### What Disable an enabled origin token passed as argument of the user in the selected region. When a token is enabled, it will participate in the protection of the origin protocol and domain. If the token is disabled, it will not participate in the protection of the origin protocol and domain.  To disable an origin token, the user must be the owner. If the token is already disabled, the function will not perform any action. If the token is enabled, it will be disabled.  ### Parameters The Origin Token is required in the body of the request in the parameter &#x60;origin_token_id&#x60;.  ### Result If successful, the result will be an empty response with a status code of &#x60;204 No Content&#x60;.  ### Errors It will return the API Global errors described in the API description.  It will also return the following errors: - a &#x60;404 Not Found&#x60; error if the origin token is not found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginTokenManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginTokenManagementInThisRegionApi apiInstance = new OriginTokenManagementInThisRegionApi(defaultClient);
    BodyDisableOriginTokenV1OriginTokenDisablePut bodyDisableOriginTokenV1OriginTokenDisablePut = new BodyDisableOriginTokenV1OriginTokenDisablePut(); // BodyDisableOriginTokenV1OriginTokenDisablePut | 
    try {
      Object result = apiInstance.disableOriginTokenV1OriginTokenDisablePut(bodyDisableOriginTokenV1OriginTokenDisablePut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginTokenManagementInThisRegionApi#disableOriginTokenV1OriginTokenDisablePut");
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
| **bodyDisableOriginTokenV1OriginTokenDisablePut** | [**BodyDisableOriginTokenV1OriginTokenDisablePut**](BodyDisableOriginTokenV1OriginTokenDisablePut.md)|  | |

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="enableOriginTokenV1OriginTokenEnablePut"></a>
# **enableOriginTokenV1OriginTokenEnablePut**
> Object enableOriginTokenV1OriginTokenEnablePut(bodyEnableOriginTokenV1OriginTokenEnablePut)

Enable a disabled origin token of the user in the region.

### What Enable a disabled origin token passed as argument of the user in the selected region. When a token is enabled, it will participate in the protection of the origin protocol and domain. If the token is disabled, it will not participate in the protection of the origin protocol and domain.  To enable an origin token, the user must be the owner. If the token is already enabled, the function will not perform any action. If the token is disabled, it will be enabled.  ### Parameters The Origin Token is required in the body of the request in the parameter &#x60;origin_token_id&#x60;.  ### Result If successful, the result will be an empty response with a status code of &#x60;204 No Content&#x60;.  ### Errors It will return the API Global errors described in the API description.  It will also return the following errors: - a &#x60;404 Not Found&#x60; error if the origin token is not found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginTokenManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginTokenManagementInThisRegionApi apiInstance = new OriginTokenManagementInThisRegionApi(defaultClient);
    BodyEnableOriginTokenV1OriginTokenEnablePut bodyEnableOriginTokenV1OriginTokenEnablePut = new BodyEnableOriginTokenV1OriginTokenEnablePut(); // BodyEnableOriginTokenV1OriginTokenEnablePut | 
    try {
      Object result = apiInstance.enableOriginTokenV1OriginTokenEnablePut(bodyEnableOriginTokenV1OriginTokenEnablePut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginTokenManagementInThisRegionApi#enableOriginTokenV1OriginTokenEnablePut");
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
| **bodyEnableOriginTokenV1OriginTokenEnablePut** | [**BodyEnableOriginTokenV1OriginTokenEnablePut**](BodyEnableOriginTokenV1OriginTokenEnablePut.md)|  | |

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="queryAllOriginTokensInTheRegionV1OriginTokenAllGet"></a>
# **queryAllOriginTokensInTheRegionV1OriginTokenAllGet**
> OriginTokenCollectionOutput queryAllOriginTokensInTheRegionV1OriginTokenAllGet()

Get the information of the origin tokens of the user in the region.

### What Obtain the attributes of all the origin tokens of the user in the selected region. The purpose of this function is to show what protocol and domain is linked to all the tokens.  The origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters No parameters are required.  ### Result The result is a list of JSON objects with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual origin token information. - &#x60;&#x60;region_id&#x60;&#x60;: the name of the region where the origin token is valid. - &#x60;&#x60;origin&#x60;&#x60;: the protocol and the domain where the origin token is valid. - &#x60;&#x60;status&#x60;&#x60;: the status of the origin token. The only allowed values are &#x60;&#x60;ENABLED&#x60;&#x60; and &#x60;&#x60;DISABLED&#x60;&#x60;. - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin token was created in UNIX timestamp in milliseconds. - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin token was last updated in UNIX timestamp in milliseconds.  ### Errors It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginTokenManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginTokenManagementInThisRegionApi apiInstance = new OriginTokenManagementInThisRegionApi(defaultClient);
    try {
      OriginTokenCollectionOutput result = apiInstance.queryAllOriginTokensInTheRegionV1OriginTokenAllGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginTokenManagementInThisRegionApi#queryAllOriginTokensInTheRegionV1OriginTokenAllGet");
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

[**OriginTokenCollectionOutput**](OriginTokenCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="queryOriginTokenInfoV1OriginTokenPost"></a>
# **queryOriginTokenInfoV1OriginTokenPost**
> OriginTokenOutput queryOriginTokenInfoV1OriginTokenPost(bodyQueryOriginTokenInfoV1OriginTokenPost)

Get the information of an origin token of the user in the region.

### What Obtain the attributes of the given origin token of the user in the selected region. The purpose of this function is to show what protocol and domain is linked to the token.  The origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters The Origin Token is required in the body of the request in the parameter &#x60;origin_token_id&#x60;.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual origin token information. - &#x60;&#x60;region_id&#x60;&#x60;: the name of the region where the origin token is valid. - &#x60;&#x60;origin&#x60;&#x60;: the protocol and the domain where the origin token is valid. - &#x60;&#x60;status&#x60;&#x60;: the status of the origin token. The only allowed values are &#x60;&#x60;ENABLED&#x60;&#x60; and &#x60;&#x60;DISABLED&#x60;&#x60;. - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin token was created in UNIX timestamp in milliseconds. - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin token was last updated in UNIX timestamp in milliseconds.  ### Errors It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginTokenManagementInThisRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    OriginTokenManagementInThisRegionApi apiInstance = new OriginTokenManagementInThisRegionApi(defaultClient);
    BodyQueryOriginTokenInfoV1OriginTokenPost bodyQueryOriginTokenInfoV1OriginTokenPost = new BodyQueryOriginTokenInfoV1OriginTokenPost(); // BodyQueryOriginTokenInfoV1OriginTokenPost | 
    try {
      OriginTokenOutput result = apiInstance.queryOriginTokenInfoV1OriginTokenPost(bodyQueryOriginTokenInfoV1OriginTokenPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginTokenManagementInThisRegionApi#queryOriginTokenInfoV1OriginTokenPost");
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
| **bodyQueryOriginTokenInfoV1OriginTokenPost** | [**BodyQueryOriginTokenInfoV1OriginTokenPost**](BodyQueryOriginTokenInfoV1OriginTokenPost.md)|  | |

### Return type

[**OriginTokenOutput**](OriginTokenOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

