# FlightsApi

All URIs are relative to *https://travelimpactmodel.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**travelimpactmodelFlightsComputeFlightEmissions**](FlightsApi.md#travelimpactmodelFlightsComputeFlightEmissions) | **POST** /v1/flights:computeFlightEmissions |  |


<a id="travelimpactmodelFlightsComputeFlightEmissions"></a>
# **travelimpactmodelFlightsComputeFlightEmissions**
> ComputeFlightEmissionsResponse travelimpactmodelFlightsComputeFlightEmissions($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, computeFlightEmissionsRequest)



Stateless method to retrieve emission estimates. Details on how emission estimates are computed: https://github.com/google/travel-impact-model The response will contain all entries that match the input flight legs, in the same order. If there are no estimates available for a certain flight leg, the response will return the flight leg object with empty emission fields. The request will still be considered successful. Reasons for missing emission estimates include: - The flight is unknown to the server. - The input flight leg is missing one or more identifiers. - The flight date is in the past. - The aircraft type is not supported by the model. - Missing seat configuration. The request can contain up to 1000 flight legs. If the request has more than 1000 direct flights, if will fail with an INVALID_ARGUMENT error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlightsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelimpactmodel.googleapis.com");

    FlightsApi apiInstance = new FlightsApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    ComputeFlightEmissionsRequest computeFlightEmissionsRequest = new ComputeFlightEmissionsRequest(); // ComputeFlightEmissionsRequest | 
    try {
      ComputeFlightEmissionsResponse result = apiInstance.travelimpactmodelFlightsComputeFlightEmissions($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, computeFlightEmissionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlightsApi#travelimpactmodelFlightsComputeFlightEmissions");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **computeFlightEmissionsRequest** | [**ComputeFlightEmissionsRequest**](ComputeFlightEmissionsRequest.md)|  | [optional] |

### Return type

[**ComputeFlightEmissionsResponse**](ComputeFlightEmissionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

