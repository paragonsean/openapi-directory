# CompileApiApi

All URIs are relative to *http://openpolicy.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postCompile**](CompileApiApi.md#postCompile) | **POST** /v1/compile | Compile |


<a id="postCompile"></a>
# **postCompile**
> PostCompile200Response postCompile(pretty, explain, metrics, instrument, requestBody)

Compile

This API endpoint allows you to partially evaluate Rego queries and obtain a simplified version of the policy. The example below assumes that OPA has been given the following policy (use &#x60;PUT /v1/policies/{path}&#x60;):  &#x60;&#x60;&#x60;yaml package example allow {   input.subject.clearance_level &gt;&#x3D; data.reports[_].clearance_level } &#x60;&#x60;&#x60; Compile API **request body** so that it contain the following fields:  | Field | Type | Required | Description | | --- | --- | --- | --- | | &#x60;query&#x60; | &#x60;string&#x60; | Yes | The query to partially evaluate and compile. | | &#x60;input&#x60; | &#x60;any&#x60; | No | The input document to use during partial evaluation (default: undefined). | | &#x60;unknowns&#x60; | &#x60;array[string]&#x60; | No | The terms to treat as unknown during partial evaluation (default: &#x60;[\&quot;input\&quot;]&#x60;]). |  For example:  &#x60;&#x60;&#x60;json {   \&quot;query\&quot;: \&quot;data.example.allow &#x3D;&#x3D; true\&quot;,   \&quot;input\&quot;: {     \&quot;subject\&quot;: {       \&quot;clearance_level\&quot;: 4     }   },   \&quot;unknowns\&quot;: [     \&quot;data.reports\&quot;     ] } &#x60;&#x60;&#x60; ### Partial evaluation In some cases, the result of partial valuation is a conclusive, unconditional answer. See [the guidance](https://www.openpolicyagent.org/docs/latest/rest-api/#unconditional-results-from-partial-evaluation) for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompileApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    CompileApiApi apiInstance = new CompileApiApi(defaultClient);
    Boolean pretty = true; // Boolean | If true, response will be in a human-readable format.
    String explain = "full"; // String | If set to *full*, response will include query explanations in addition to the result.
    Boolean metrics = false; // Boolean | If true, compiler performance metrics will be returned in the response.
    Boolean instrument = false; // Boolean | If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem.
    Map<String, Object> requestBody = null; // Map<String, Object> | The query (in JSON format)
    try {
      PostCompile200Response result = apiInstance.postCompile(pretty, explain, metrics, instrument, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompileApiApi#postCompile");
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
| **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] |
| **explain** | **String**| If set to *full*, response will include query explanations in addition to the result. | [optional] |
| **metrics** | **Boolean**| If true, compiler performance metrics will be returned in the response. | [optional] |
| **instrument** | **Boolean**| If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem. | [optional] |
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)| The query (in JSON format) | [optional] |

### Return type

[**PostCompile200Response**](PostCompile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **500** | Server error |  -  |

