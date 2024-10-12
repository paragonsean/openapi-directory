# UsageDetailsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usageDetailsList**](UsageDetailsApi.md#usageDetailsList) | **GET** /{scope}/providers/Microsoft.Consumption/usageDetails |  |


<a id="usageDetailsList"></a>
# **usageDetailsList**
> UsageDetailsListResult usageDetailsList(scope, apiVersion, $expand, $filter, $skiptoken, $top, metric)



Lists the usage details for the defined scope. Usage details are available via this API only for May 1, 2014 or later.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsageDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UsageDetailsApi apiInstance = new UsageDetailsApi(defaultClient);
    String scope = "scope_example"; // String | The scope associated with usage details operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, '/providers/Microsoft.Billing/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope and '/providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope. For subscription, billing account, department, enrollment account and management group, you can also add billing period to the scope using '/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'. For e.g. to specify billing period at department scope use '/providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-05-01.
    String $expand = "$expand_example"; // String | May be used to expand the properties/additionalInfo or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details.
    String $filter = "$filter_example"; // String | May be used to filter usageDetails by properties/resourceGroup, properties/resourceName, properties/resourceId, properties/chargeType, properties/reservationId, properties/publisherType or tags. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:). PublisherType Filter accepts two values azure and marketplace and it is currently supported for Web Direct Offer Type
    String $skiptoken = "$skiptoken_example"; // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N usageDetails.
    String metric = "actualcost"; // String | Allows to select different type of cost/usage records.
    try {
      UsageDetailsListResult result = apiInstance.usageDetailsList(scope, apiVersion, $expand, $filter, $skiptoken, $top, metric);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageDetailsApi#usageDetailsList");
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
| **scope** | **String**| The scope associated with usage details operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;/providers/Microsoft.Billing/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope and &#39;/providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope. For subscription, billing account, department, enrollment account and management group, you can also add billing period to the scope using &#39;/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39;. For e.g. to specify billing period at department scope use &#39;/providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39; | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-05-01. | |
| **$expand** | **String**| May be used to expand the properties/additionalInfo or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details. | [optional] |
| **$filter** | **String**| May be used to filter usageDetails by properties/resourceGroup, properties/resourceName, properties/resourceId, properties/chargeType, properties/reservationId, properties/publisherType or tags. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). PublisherType Filter accepts two values azure and marketplace and it is currently supported for Web Direct Offer Type | [optional] |
| **$skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N usageDetails. | [optional] |
| **metric** | **String**| Allows to select different type of cost/usage records. | [optional] [enum: actualcost, amortizedcost, usage] |

### Return type

[**UsageDetailsListResult**](UsageDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

