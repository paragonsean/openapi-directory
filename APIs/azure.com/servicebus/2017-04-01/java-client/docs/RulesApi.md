# RulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rulesCreateOrUpdate**](RulesApi.md#rulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/subscriptions/{subscriptionName}/rules/{ruleName} |  |
| [**rulesDelete**](RulesApi.md#rulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/subscriptions/{subscriptionName}/rules/{ruleName} |  |
| [**rulesListBySubscriptions**](RulesApi.md#rulesListBySubscriptions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/subscriptions/{subscriptionName}/rules |  |


<a id="rulesCreateOrUpdate"></a>
# **rulesCreateOrUpdate**
> Rule rulesCreateOrUpdate(resourceGroupName, namespaceName, topicName, subscriptionName, ruleName, apiVersion, subscriptionId, parameters)



Creates a new rule and updates an existing rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String topicName = "topicName_example"; // String | The topic name.
    String subscriptionName = "subscriptionName_example"; // String | The subscription name.
    String ruleName = "ruleName_example"; // String | The rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Rule parameters = new Rule(); // Rule | Parameters supplied to create a rule.
    try {
      Rule result = apiInstance.rulesCreateOrUpdate(resourceGroupName, namespaceName, topicName, subscriptionName, ruleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#rulesCreateOrUpdate");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **topicName** | **String**| The topic name. | |
| **subscriptionName** | **String**| The subscription name. | |
| **ruleName** | **String**| The rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**Rule**](Rule.md)| Parameters supplied to create a rule. | |

### Return type

[**Rule**](Rule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule created. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="rulesDelete"></a>
# **rulesDelete**
> rulesDelete(resourceGroupName, namespaceName, topicName, subscriptionName, ruleName, apiVersion, subscriptionId)



Deletes an existing rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String topicName = "topicName_example"; // String | The topic name.
    String subscriptionName = "subscriptionName_example"; // String | The subscription name.
    String ruleName = "ruleName_example"; // String | The rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.rulesDelete(resourceGroupName, namespaceName, topicName, subscriptionName, ruleName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#rulesDelete");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **topicName** | **String**| The topic name. | |
| **subscriptionName** | **String**| The subscription name. | |
| **ruleName** | **String**| The rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule deleted. |  -  |
| **204** | No Content |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="rulesListBySubscriptions"></a>
# **rulesListBySubscriptions**
> RuleListResult rulesListBySubscriptions(resourceGroupName, namespaceName, topicName, subscriptionName, apiVersion, subscriptionId, $skip, $top)



List all the rules within given topic-subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String topicName = "topicName_example"; // String | The topic name.
    String subscriptionName = "subscriptionName_example"; // String | The subscription name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $skip = 56; // Integer | Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N usageDetails.
    try {
      RuleListResult result = apiInstance.rulesListBySubscriptions(resourceGroupName, namespaceName, topicName, subscriptionName, apiVersion, subscriptionId, $skip, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#rulesListBySubscriptions");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **topicName** | **String**| The topic name. | |
| **subscriptionName** | **String**| The subscription name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$skip** | **Integer**| Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N usageDetails. | [optional] |

### Return type

[**RuleListResult**](RuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved list of Rules. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

