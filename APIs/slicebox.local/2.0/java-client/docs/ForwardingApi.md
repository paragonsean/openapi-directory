# ForwardingApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**forwardingRuleIdDelete**](ForwardingApi.md#forwardingRuleIdDelete) | **DELETE** /forwarding/rule/{id} |  |
| [**forwardingRulesGet**](ForwardingApi.md#forwardingRulesGet) | **GET** /forwarding/rules |  |
| [**forwardingRulesPost**](ForwardingApi.md#forwardingRulesPost) | **POST** /forwarding/rules |  |


<a id="forwardingRuleIdDelete"></a>
# **forwardingRuleIdDelete**
> forwardingRuleIdDelete(id)



remove the forwarding rule corresponding to the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForwardingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ForwardingApi apiInstance = new ForwardingApi(defaultClient);
    Long id = 56L; // Long | id of forwarding rule to remove
    try {
      apiInstance.forwardingRuleIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForwardingApi#forwardingRuleIdDelete");
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
| **id** | **Long**| id of forwarding rule to remove | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | forwarding rule removed |  -  |

<a id="forwardingRulesGet"></a>
# **forwardingRulesGet**
> List&lt;Forwardingrule&gt; forwardingRulesGet(startindex, count)



get a list of all forwarding rules. A forwarding rule specifies the automatic forwarding of images from a source (SCP, BOX, etc.) to a destimation (BOX, SCU, etc.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForwardingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ForwardingApi apiInstance = new ForwardingApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of rules
    Long count = 20L; // Long | size of returned slice of rules
    try {
      List<Forwardingrule> result = apiInstance.forwardingRulesGet(startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForwardingApi#forwardingRulesGet");
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
| **startindex** | **Long**| start index of returned slice of rules | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of rules | [optional] [default to 20] |

### Return type

[**List&lt;Forwardingrule&gt;**](Forwardingrule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of forwarding rules |  -  |

<a id="forwardingRulesPost"></a>
# **forwardingRulesPost**
> Forwardingrule forwardingRulesPost(fowardingRule)



add a new forwarding rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForwardingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ForwardingApi apiInstance = new ForwardingApi(defaultClient);
    Forwardingrule fowardingRule = new Forwardingrule(); // Forwardingrule | The forwarding rule to add. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    try {
      Forwardingrule result = apiInstance.forwardingRulesPost(fowardingRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForwardingApi#forwardingRulesPost");
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
| **fowardingRule** | [**Forwardingrule**](Forwardingrule.md)| The forwarding rule to add. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] |

### Return type

[**Forwardingrule**](Forwardingrule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | the created forwarding rule |  -  |

