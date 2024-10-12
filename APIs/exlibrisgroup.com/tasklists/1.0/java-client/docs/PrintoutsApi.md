# PrintoutsApi

All URIs are relative to *https://api-eu.hosted.exlibrisgroup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAlmawsV1TaskListsPrintouts**](PrintoutsApi.md#getAlmawsV1TaskListsPrintouts) | **GET** /almaws/v1/task-lists/printouts | Retrieve Printouts |
| [**getAlmawsV1TaskListsPrintoutsPrintoutId**](PrintoutsApi.md#getAlmawsV1TaskListsPrintoutsPrintoutId) | **GET** /almaws/v1/task-lists/printouts/{printout_id} | Retrieve a Printout |
| [**postAlmawsV1TaskListsPrintouts**](PrintoutsApi.md#postAlmawsV1TaskListsPrintouts) | **POST** /almaws/v1/task-lists/printouts | Act on Printouts |
| [**postAlmawsV1TaskListsPrintoutsPrintoutId**](PrintoutsApi.md#postAlmawsV1TaskListsPrintoutsPrintoutId) | **POST** /almaws/v1/task-lists/printouts/{printout_id} | Printout Service |


<a id="getAlmawsV1TaskListsPrintouts"></a>
# **getAlmawsV1TaskListsPrintouts**
> GetAlmawsV1TaskListsPrintouts200Response getAlmawsV1TaskListsPrintouts(letter, status, printerId, printoutId, limit, offset)

Retrieve Printouts

This API returns a list of Printouts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrintoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-eu.hosted.exlibrisgroup.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PrintoutsApi apiInstance = new PrintoutsApi(defaultClient);
    String letter = "ALL"; // String | Printout Name. Optional. 
    String status = "ALL"; // String | Printout status. Optional. Valid values are: Printed, Pending, Canceled.
    String printerId = "ALL"; // String | Printout Printer
    String printoutId = "ALL"; // String | A list of Printout IDs (for example: 123,456,778) from 1 to the limit of 100 Optional. Use of this option overrides all of the filtering parameters
    Integer limit = 56; // Integer | Limits the number of results. Optional. Valid values are 0-100. Default value: 10.
    Integer offset = 56; // Integer | Offset of the results returned. Optional. Default value: 0, which means that the first results will be returned.
    try {
      GetAlmawsV1TaskListsPrintouts200Response result = apiInstance.getAlmawsV1TaskListsPrintouts(letter, status, printerId, printoutId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrintoutsApi#getAlmawsV1TaskListsPrintouts");
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
| **letter** | **String**| Printout Name. Optional.  | [optional] [default to ALL] |
| **status** | **String**| Printout status. Optional. Valid values are: Printed, Pending, Canceled. | [optional] [default to ALL] |
| **printerId** | **String**| Printout Printer | [optional] [default to ALL] |
| **printoutId** | **String**| A list of Printout IDs (for example: 123,456,778) from 1 to the limit of 100 Optional. Use of this option overrides all of the filtering parameters | [optional] [default to ALL] |
| **limit** | **Integer**| Limits the number of results. Optional. Valid values are 0-100. Default value: 10. | [optional] |
| **offset** | **Integer**| Offset of the results returned. Optional. Default value: 0, which means that the first results will be returned. | [optional] |

### Return type

[**GetAlmawsV1TaskListsPrintouts200Response**](GetAlmawsV1TaskListsPrintouts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - This method returns an object based on rest_printouts.xsd. See [here](/alma/apis/docs/xsd/rest_printouts.xsd) |  * X-Exl-Api-Remaining -  <br>  |
| **400** | Bad Request  401666|40166410 - &#39;Invalid parameter.&#39; |  -  |
| **500** | Internal Server Error |  -  |

<a id="getAlmawsV1TaskListsPrintoutsPrintoutId"></a>
# **getAlmawsV1TaskListsPrintoutsPrintoutId**
> Object getAlmawsV1TaskListsPrintoutsPrintoutId(printoutId)

Retrieve a Printout

This Web service returns a Printout given a Printout ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrintoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-eu.hosted.exlibrisgroup.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PrintoutsApi apiInstance = new PrintoutsApi(defaultClient);
    String printoutId = "printoutId_example"; // String | The Printout ID
    try {
      Object result = apiInstance.getAlmawsV1TaskListsPrintoutsPrintoutId(printoutId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrintoutsApi#getAlmawsV1TaskListsPrintoutsPrintoutId");
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
| **printoutId** | **String**| The Printout ID | |

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - This method returns an object based on rest_printout.xsd. See [here](/alma/apis/docs/xsd/rest_printout.xsd) |  * X-Exl-Api-Remaining -  <br>  |
| **400** | Bad Request  402896 - &#39;Invalid printout ID.&#39; |  -  |
| **500** | Internal Server Error |  -  |

<a id="postAlmawsV1TaskListsPrintouts"></a>
# **postAlmawsV1TaskListsPrintouts**
> Object postAlmawsV1TaskListsPrintouts(op, letter, status, printerId, printoutId)

Act on Printouts

This API performs an action on printouts: mark as printed or canceled. 10,000 records can be handled in one requests. Only printouts which were updated will be returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrintoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-eu.hosted.exlibrisgroup.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PrintoutsApi apiInstance = new PrintoutsApi(defaultClient);
    String op = "op_example"; // String | The operation to perform on the printout. Currently, the options are: 'mark_as_printed','mark_as_canceled'
    String letter = "ALL"; // String | Printout Name. Optional. 
    String status = "ALL"; // String | Printout status. Optional. Valid values are: Printed, Pending, Canceled.
    String printerId = "ALL"; // String | Printout Printer
    String printoutId = "ALL"; // String | A list of Printout IDs (for example: 123,456,778) from 1 to the limit of 100 Optional. Use of this option overrides all of the filtering parameters
    try {
      Object result = apiInstance.postAlmawsV1TaskListsPrintouts(op, letter, status, printerId, printoutId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrintoutsApi#postAlmawsV1TaskListsPrintouts");
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
| **op** | **String**| The operation to perform on the printout. Currently, the options are: &#39;mark_as_printed&#39;,&#39;mark_as_canceled&#39; | |
| **letter** | **String**| Printout Name. Optional.  | [optional] [default to ALL] |
| **status** | **String**| Printout status. Optional. Valid values are: Printed, Pending, Canceled. | [optional] [default to ALL] |
| **printerId** | **String**| Printout Printer | [optional] [default to ALL] |
| **printoutId** | **String**| A list of Printout IDs (for example: 123,456,778) from 1 to the limit of 100 Optional. Use of this option overrides all of the filtering parameters | [optional] [default to ALL] |

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - This method returns an object based on rest_printouts.xsd. See [here](/alma/apis/docs/xsd/rest_printouts.xsd) |  * X-Exl-Api-Remaining -  <br>  |
| **400** | Bad Request  401666|40166410 - &#39;Invalid parameter.&#39; |  -  |
| **500** | Internal Server Error |  -  |

<a id="postAlmawsV1TaskListsPrintoutsPrintoutId"></a>
# **postAlmawsV1TaskListsPrintoutsPrintoutId**
> Object postAlmawsV1TaskListsPrintoutsPrintoutId(printoutId, op)

Printout Service

This API operates on an printout. given a Printout ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrintoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-eu.hosted.exlibrisgroup.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PrintoutsApi apiInstance = new PrintoutsApi(defaultClient);
    String printoutId = "printoutId_example"; // String | The Printout ID
    String op = "op_example"; // String | The operation to perform on the printout. Currently, the options are 'mark_as_printed','mark_as_canceled'
    try {
      Object result = apiInstance.postAlmawsV1TaskListsPrintoutsPrintoutId(printoutId, op);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrintoutsApi#postAlmawsV1TaskListsPrintoutsPrintoutId");
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
| **printoutId** | **String**| The Printout ID | |
| **op** | **String**| The operation to perform on the printout. Currently, the options are &#39;mark_as_printed&#39;,&#39;mark_as_canceled&#39; | |

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - This method returns an object based on rest_printout.xsd. See [here](/alma/apis/docs/xsd/rest_printout.xsd) |  * X-Exl-Api-Remaining -  <br>  |
| **400** | Bad Request  402896 - &#39;Invalid printout ID.&#39;  40166410 - &#39;Invalid parameter.&#39;  40166412 - &#39;Failed to perform action.&#39; |  -  |
| **500** | Internal Server Error |  -  |

