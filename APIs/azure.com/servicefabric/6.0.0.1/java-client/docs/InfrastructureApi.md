# InfrastructureApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**invokeInfrastructureCommand**](InfrastructureApi.md#invokeInfrastructureCommand) | **POST** /$/InvokeInfrastructureCommand | Invokes an administrative command on the given Infrastructure Service instance. |
| [**invokeInfrastructureQuery**](InfrastructureApi.md#invokeInfrastructureQuery) | **GET** /$/InvokeInfrastructureQuery | Invokes a read-only query on the given infrastructure service instance. |


<a id="invokeInfrastructureCommand"></a>
# **invokeInfrastructureCommand**
> File invokeInfrastructureCommand(apiVersion, command, serviceId, timeout)

Invokes an administrative command on the given Infrastructure Service instance.

For clusters that have one or more instances of the Infrastructure Service configured, this API provides a way to send infrastructure-specific commands to a particular instance of the Infrastructure Service.  Available commands and their corresponding response formats vary depending upon the infrastructure on which the cluster is running.  This API supports the Service Fabric platform; it is not meant to be used directly from your code. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfrastructureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    InfrastructureApi apiInstance = new InfrastructureApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String command = "command_example"; // String | The text of the command to be invoked. The content of the command is infrastructure-specific.
    String serviceId = "serviceId_example"; // String | The identity of the infrastructure service. This is  the full name of the infrastructure service without the 'fabric:' URI scheme. This parameter required only for the cluster that have more than one instance of infrastructure service running.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      File result = apiInstance.invokeInfrastructureCommand(apiVersion, command, serviceId, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfrastructureApi#invokeInfrastructureCommand");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **command** | **String**| The text of the command to be invoked. The content of the command is infrastructure-specific. | |
| **serviceId** | **String**| The identity of the infrastructure service. This is  the full name of the infrastructure service without the &#39;fabric:&#39; URI scheme. This parameter required only for the cluster that have more than one instance of infrastructure service running. | [optional] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response from the infrastructure service. The response format is a JSON stream. The contents of the response depend on which command was issued.  |  -  |
| **0** | The detailed error response. |  -  |

<a id="invokeInfrastructureQuery"></a>
# **invokeInfrastructureQuery**
> File invokeInfrastructureQuery(apiVersion, command, serviceId, timeout)

Invokes a read-only query on the given infrastructure service instance.

For clusters that have one or more instances of the Infrastructure Service configured, this API provides a way to send infrastructure-specific queries to a particular instance of the Infrastructure Service.  Available commands and their corresponding response formats vary depending upon the infrastructure on which the cluster is running.  This API supports the Service Fabric platform; it is not meant to be used directly from your code. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfrastructureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    InfrastructureApi apiInstance = new InfrastructureApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String command = "command_example"; // String | The text of the command to be invoked. The content of the command is infrastructure-specific.
    String serviceId = "serviceId_example"; // String | The identity of the infrastructure service. This is  the full name of the infrastructure service without the 'fabric:' URI scheme. This parameter required only for the cluster that have more than one instance of infrastructure service running.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      File result = apiInstance.invokeInfrastructureQuery(apiVersion, command, serviceId, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfrastructureApi#invokeInfrastructureQuery");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **command** | **String**| The text of the command to be invoked. The content of the command is infrastructure-specific. | |
| **serviceId** | **String**| The identity of the infrastructure service. This is  the full name of the infrastructure service without the &#39;fabric:&#39; URI scheme. This parameter required only for the cluster that have more than one instance of infrastructure service running. | [optional] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response from the infrastructure service. The response format is a JSON stream. The contents of the response depend on which command was issued.  |  -  |
| **0** | The detailed error response. |  -  |

