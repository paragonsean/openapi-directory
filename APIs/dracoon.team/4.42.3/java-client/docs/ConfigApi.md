# ConfigApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**requestAlgorithms**](ConfigApi.md#requestAlgorithms) | **GET** /v4/config/info/policies/algorithms | Request algorithms |
| [**requestClassificationPoliciesConfigInfo**](ConfigApi.md#requestClassificationPoliciesConfigInfo) | **GET** /v4/config/info/policies/classifications | Request classification policies |
| [**requestCurrentProductPackages**](ConfigApi.md#requestCurrentProductPackages) | **GET** /v4/config/info/product_packages/current | Request list of currently enabled product packages |
| [**requestGeneralSettingsInfo**](ConfigApi.md#requestGeneralSettingsInfo) | **GET** /v4/config/info/general | Request general settings |
| [**requestGuestUsersPoliciesConfigInfo**](ConfigApi.md#requestGuestUsersPoliciesConfigInfo) | **GET** /v4/config/info/policies/guest_users | Request guest users policies |
| [**requestInfrastructurePropertiesInfo**](ConfigApi.md#requestInfrastructurePropertiesInfo) | **GET** /v4/config/info/infrastructure | Request infrastructure properties |
| [**requestNotificationChannelsInfo**](ConfigApi.md#requestNotificationChannelsInfo) | **GET** /v4/config/info/notifications/channels | Request list of notification channels |
| [**requestPasswordPoliciesConfigInfo**](ConfigApi.md#requestPasswordPoliciesConfigInfo) | **GET** /v4/config/info/policies/passwords | Request password policies |
| [**requestProductPackages**](ConfigApi.md#requestProductPackages) | **GET** /v4/config/info/product_packages | Request list of product packages |
| [**requestS3TagsInfo**](ConfigApi.md#requestS3TagsInfo) | **GET** /v4/config/info/s3_tags | Request list of configured S3 tags |
| [**requestSystemDefaultsInfo**](ConfigApi.md#requestSystemDefaultsInfo) | **GET** /v4/config/info/defaults | Request default values |
| [**requestSystemSettings**](ConfigApi.md#requestSystemSettings) | **GET** /v4/config/settings | Request system settings |
| [**updateSystemSettings**](ConfigApi.md#updateSystemSettings) | **PUT** /v4/config/settings | Update system settings |


<a id="requestAlgorithms"></a>
# **requestAlgorithms**
> AlgorithmVersionInfoList requestAlgorithms(xSdsAuthToken)

Request algorithms

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description: Retrieve a list of available algorithms used for encryption.  ### Precondition: Authenticated user.  ### Postcondition: List of available algorithms is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      AlgorithmVersionInfoList result = apiInstance.requestAlgorithms(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#requestAlgorithms");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**AlgorithmVersionInfoList**](AlgorithmVersionInfoList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestClassificationPoliciesConfigInfo"></a>
# **requestClassificationPoliciesConfigInfo**
> ClassificationPoliciesConfig requestClassificationPoliciesConfigInfo(xSdsAuthToken)

Request classification policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.30.0&lt;/h3&gt;  ### Description: Retrieve a list of classification policies: * &#x60;shareClassificationPolicies&#x60;  ### Precondition: Authenticated user.  ### Postcondition: List of configured classification policies is returned.  ### Further Information: &#x60;classificationRequiresSharePassword&#x60;: When a node has this classification or higher, it cannot be shared without a password. If the node is an encrypted file this policy has no effect. &#x60;0&#x60; means no password will be enforced. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      ClassificationPoliciesConfig result = apiInstance.requestClassificationPoliciesConfigInfo(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#requestClassificationPoliciesConfigInfo");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**ClassificationPoliciesConfig**](ClassificationPoliciesConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestCurrentProductPackages"></a>
# **requestCurrentProductPackages**
> ProductPackageResponseList requestCurrentProductPackages(xSdsAuthToken)

Request list of currently enabled product packages

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.38.0&lt;/h3&gt;  ### Description:   Returns a list of currently enabled product packages.  ### Precondition: Authenticated user  ### Postcondition: List of currently enabled Product Packages is returned.  ### Further Information: 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      ProductPackageResponseList result = apiInstance.requestCurrentProductPackages(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#requestCurrentProductPackages");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**ProductPackageResponseList**](ProductPackageResponseList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestGeneralSettingsInfo"></a>
# **requestGeneralSettingsInfo**
> GeneralSettingsInfo requestGeneralSettingsInfo(xSdsAuthToken)

Request general settings

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description: Returns a list of configurable general settings.  ### Precondition: Authenticated user.  ### Postcondition: List of configurable general settings is returned.  ### Further Information: None.  ### Configurable general settings: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;sharePasswordSmsEnabled&#x60; | Determines whether sending of share passwords via SMS is allowed. | &#x60;true or false&#x60; | | &#x60;cryptoEnabled&#x60; | Determines whether client-side encryption is enabled.&lt;br&gt;Can only be enabled once; disabling is **NOT** possible. | &#x60;true or false&#x60; | | &#x60;emailNotificationButtonEnabled&#x60; | Determines whether email notification button is enabled. | &#x60;true or false&#x60; | | &#x60;eulaEnabled&#x60; | Determines whether EULA is enabled.&lt;br&gt;Each user has to confirm the EULA at first login. | &#x60;true or false&#x60; | | &#x60;useS3Storage&#x60; | Defines if S3 is used as storage backend.&lt;br&gt;Can only be enabled once; disabling is **NOT** possible. | &#x60;true or false&#x60; | | &#x60;s3TagsEnabled&#x60; | Determines whether S3 tags are enabled | &#x60;true or false&#x60; | | &#x60;homeRoomsActive&#x60; | Determines whether each AD user has a personal home room | &#x60;true or false&#x60; | | &#x60;homeRoomParentId&#x60; | Defines a node under which all personal home rooms are located. **NULL** if &#x60;homeRoomsActive&#x60; is &#x60;false&#x60; | &#x60;Long&#x60; | | &#x60;subscriptionPlan&#x60; | Subscription Plan. &lt;br&gt; 0 &#x3D; Pro, 1 &#x3D; Premium, 2 &#x3D; Basic | &#x60;Integer&#x60; |  &lt;/details&gt;  ### Deprecated general settings: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &lt;del&gt;&#x60;mediaServerEnabled&#x60;&lt;/del&gt; | Determines whether media server is enabled.&lt;br&gt;Returns boolean value dependent on conjunction of &#x60;mediaServerConfigEnabled&#x60; AND &#x60;mediaServerEnabled&#x60; | &#x60;true or false&#x60; | | &lt;del&gt;&#x60;weakPasswordEnabled&#x60;&lt;/del&gt; | Determines whether weak password is allowed.&lt;br&gt;Use &#x60;GET /system/config/policies/passwords&#x60; API to get configured password policies. | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      GeneralSettingsInfo result = apiInstance.requestGeneralSettingsInfo(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#requestGeneralSettingsInfo");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**GeneralSettingsInfo**](GeneralSettingsInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestGuestUsersPoliciesConfigInfo"></a>
# **requestGuestUsersPoliciesConfigInfo**
> GuestUsersPoliciesConfig requestGuestUsersPoliciesConfigInfo(xSdsAuthToken)

Request guest users policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.40.0&lt;/h3&gt;  ### Description: Retrieve a list of guest users policies.  ### Precondition: Authenticated user.  ### Postcondition: List of configured guest users policies is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      GuestUsersPoliciesConfig result = apiInstance.requestGuestUsersPoliciesConfigInfo(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#requestGuestUsersPoliciesConfigInfo");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**GuestUsersPoliciesConfig**](GuestUsersPoliciesConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestInfrastructurePropertiesInfo"></a>
# **requestInfrastructurePropertiesInfo**
> InfrastructureProperties requestInfrastructurePropertiesInfo(xSdsAuthToken)

Request infrastructure properties

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   Returns a list of read-only infrastructure properties.    ### Precondition: Authenticated user.  ### Postcondition: List of infrastructure properties is returned.  ### Further Information: Source: &#x60;core-service.properties&#x60;  ### Read-only infrastructure properties: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;smsConfigEnabled&#x60; | Determines whether sending of share passwords via SMS is **system-wide** enabled. | &#x60;true or false&#x60; | | &#x60;mediaServerConfigEnabled&#x60; | Determines whether media server is **system-wide** enabled. | &#x60;true or false&#x60; | | &#x60;s3DefaultRegion&#x60; | Suggested S3 region | &#x60;Region name&#x60; | | &#x60;s3EnforceDirectUpload&#x60; | Enforce direct upload to S3 | &#x60;true or false&#x60; | | &#x60;isDracoonCloud&#x60; | Determines if the **DRACOON Core** is deployed in the cloud environment | &#x60;true or false&#x60; | | &#x60;tenantUuid&#x60; | Current tenant UUID | &#x60;UUID&#x60; |  &lt;/details&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      InfrastructureProperties result = apiInstance.requestInfrastructurePropertiesInfo(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#requestInfrastructurePropertiesInfo");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**InfrastructureProperties**](InfrastructureProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestNotificationChannelsInfo"></a>
# **requestNotificationChannelsInfo**
> NotificationChannelList requestNotificationChannelsInfo(xSdsAuthToken)

Request list of notification channels

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description: Retrieve a list of configured notification channels.  ### Precondition: Authenticated user.  ### Postcondition: List of notification channels is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      NotificationChannelList result = apiInstance.requestNotificationChannelsInfo(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#requestNotificationChannelsInfo");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**NotificationChannelList**](NotificationChannelList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestPasswordPoliciesConfigInfo"></a>
# **requestPasswordPoliciesConfigInfo**
> PasswordPoliciesConfig requestPasswordPoliciesConfigInfo(xSdsAuthToken)

Request password policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.14.0&lt;/h3&gt;  ### Description:   Retrieve a list of configured password policies for all password types:   * &#x60;login&#x60; * &#x60;shares&#x60; * &#x60;encryption&#x60;  ### Precondition: Authenticated user.  ### Postcondition: List of configured password policies is returned.  ### Further Information: None.  ### Available password policies: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Value | Password Type | | :--- | :--- | :--- | :--- | | &#x60;mustContainCharacters&#x60; | Characters which a password must contain:&lt;br&gt;&lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60; - at least one alphabetical character (&#x60;uppercase&#x60; **OR** &#x60;lowercase&#x60;)&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;br&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60; - at least one uppercase character&lt;pre&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60; - at least one lowercase character&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60; - at least one numeric character&lt;pre&gt;0 1 2 3 4 5 6 7 8 9&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60; - at least one special character (letters and digits excluded)&lt;pre&gt;! \&quot; # $ % ( ) * + , - . / : ; &#x3D; ? @ [ \\ ] ^ _ { &amp;#124; } ~&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60; - none of the above&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60;&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfCharacteristicsToEnforce&#x60; | Number of characteristics to enforce.&lt;br&gt;e.g. from &#x60;[\&quot;uppercase\&quot;, \&quot;lowercase\&quot;, \&quot;numeric\&quot;, \&quot;special\&quot;]&#x60;&lt;br&gt;all 4 character sets can be enforced; but also only 2 of them | &#x60;Integer between 0 and 4&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;minLength&#x60; | Minimum number of characters a password must contain. | &#x60;Integer between 1 and 1024&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectDictionaryWords&#x60; | Determines whether a password must **NOT** contain word(s) from a dictionary.&lt;br&gt;In &#x60;core-service.properties&#x60; a path to directory with dictionary files (&#x60;*.txt&#x60;) can be defined&lt;br&gt;cf. &#x60;policies.passwords.dictionary.directory&#x60;.&lt;br&gt;&lt;br&gt;If this rule gets enabled &#x60;policies.passwords.dictionary.directory&#x60; must be defined and contain dictionary files.&lt;br&gt;Otherwise, the rule will not have any effect on password validation process. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectUserInfo&#x60; | Determines whether a password must **NOT** contain user info.&lt;br&gt;Affects user&#39;s **first name**, **last name**, **email** and **user name**. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectKeyboardPatterns&#x60; | Determines whether a password must **NOT** contain keyboard patterns.&lt;br&gt;e.g. &#x60;qwertz&#x60;, &#x60;asdf&#x60; (min. 4 character pattern) | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfArchivedPasswords&#x60; | Number of passwords to archive.&lt;br&gt;Value &#x60;0&#x60; means that password history is disabled. | &#x60;Integer between 0 and 10&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;passwordExpiration.enabled&#x60; | Determines whether password expiration is enabled. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxPasswordAge&#x60; | Maximum allowed password age (in **days**) | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;userLockout.enabled&#x60; | Determines whether user lockout is enabled. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxNumberOfLoginFailures&#x60; | Maximum allowed number of failed login attempts. | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;lockoutPeriod&#x60; | Amount of **minutes** a user has to wait to make another login attempt&lt;br&gt;after &#x60;maxNumberOfLoginFailures&#x60; has been exceeded. | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      PasswordPoliciesConfig result = apiInstance.requestPasswordPoliciesConfigInfo(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#requestPasswordPoliciesConfigInfo");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**PasswordPoliciesConfig**](PasswordPoliciesConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestProductPackages"></a>
# **requestProductPackages**
> ProductPackageResponseList requestProductPackages(xSdsAuthToken)

Request list of product packages

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.38.0&lt;/h3&gt;  ### Description:   Returns a list of product packages.  ### Precondition: Authenticated user  ### Postcondition: List of Product Packages is returned.  ### Further Information: 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      ProductPackageResponseList result = apiInstance.requestProductPackages(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#requestProductPackages");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**ProductPackageResponseList**](ProductPackageResponseList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestS3TagsInfo"></a>
# **requestS3TagsInfo**
> S3TagList requestS3TagsInfo(xSdsAuthToken)

Request list of configured S3 tags

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description: Retrieve all configured S3 tags.  ### Precondition: Authenticated user.  ### Postcondition: List of configured S3 tags is returned.  ### Further Information: An empty list is returned if no S3 tags are found / configured.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      S3TagList result = apiInstance.requestS3TagsInfo(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#requestS3TagsInfo");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**S3TagList**](S3TagList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestSystemDefaultsInfo"></a>
# **requestSystemDefaultsInfo**
> SystemDefaults requestSystemDefaultsInfo(xSdsAuthToken)

Request default values

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.6.0&lt;/h3&gt;  ### Description:   Returns a list of configurable system default values.  ### Precondition: Authenticated user.  ### Postcondition: List of configurable default settings is returned.  ### Further Information: None.  ### Configurable default values: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;languageDefault&#x60; | Defines which language should be default. | &#x60;ISO 639-1 code&#x60; | | &#x60;downloadShareDefaultExpirationPeriod&#x60; | Default expiration period for Download Shares in _days_. | &#x60;Integer between 0 and 9999&#x60; | | &#x60;uploadShareDefaultExpirationPeriod&#x60; | Default expiration period for Upload Shares in _days_. | &#x60;Integer between 0 and 9999&#x60; | | &#x60;fileDefaultExpirationPeriod&#x60; | Default expiration period for all uploaded files in _days_. | &#x60;Integer between 0 and 9999&#x60; | | &#x60;nonmemberViewerDefault&#x60; | Defines if new users get the role _Non Member Viewer_ by default | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      SystemDefaults result = apiInstance.requestSystemDefaultsInfo(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#requestSystemDefaultsInfo");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**SystemDefaults**](SystemDefaults.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestSystemSettings"></a>
# **requestSystemSettings**
> ConfigOptionList requestSystemSettings(xSdsAuthToken)

Request system settings

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.6.0&lt;/h3&gt;  ### Description:   Returns a list of configurable system settings.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; required.  ### Postcondition: List of configurable settings is returned.  ### Further Information: Check for every settings key new corresponding API and key below.  If &#x60;eula_active&#x60; is true, but **NOT** accepted yet, or password **MUST** be changed, only the following two values are returned: * &#x60;allow_system_global_weak_password&#x60; * &#x60;eula_active&#x60;  ### Configurable settings &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;branding_server_branding_id&#x60; | The branding UUID, which corresponds to _BRANDING-QUALIFIER_ in the new branding server.&lt;br&gt;cf. &#x60;GET /system/config/settings/branding&#x60; &#x60;BrandingConfig.brandingQualifier&#x60; | &#x60;String&#x60; | | &#x60;branding_portal_url&#x60; | Access URL to to the Branding Portal&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;GET /system/config/settings/branding&#x60; &#x60;BrandingConfig.brandingProviderUrl&#x60; | &#x60;String&#x60; | | &#x60;dblog&#x60; | Write logs to local database.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;GET /system/config/settings/eventlog&#x60; &#x60;EventlogConfig.enabled&#x60; | &#x60;true or false&#x60; | | &#x60;default_downloadshare_expiration_period&#x60; | Default expiration period for Download Shares in days&lt;br&gt;cf. &#x60;GET /system/config/settings/defaults&#x60; &#x60;SystemDefaults.downloadShareDefaultExpirationPeriod&#x60; | &#x60;Integer between 0 and 9999&#x60; | | &#x60;default_file_upload_expiration_date&#x60; | Default expiration period for all uploaded files in days&lt;br&gt;cf. &#x60;GET /system/config/settings/defaults&#x60; &#x60;SystemDefaults.fileDefaultExpirationPeriod&#x60; | &#x60;Integer between 0 and 9999&#x60; | | &#x60;default_language&#x60; | Define which language should be default.&lt;br&gt;cf. &#x60;GET /system/config/settings/defaults&#x60; &#x60;SystemDefaults.languageDefault&#x60; | cf. &#x60;GET /public/system/info&#x60; - &#x60;SystemInfo.languageDefault&#x60; | | &#x60;default_uploadshare_expiration_period&#x60; | Default expiration period for Upload Shares in days&lt;br&gt;cf. &#x60;GET /system/config/settings/defaults&#x60; &#x60;SystemDefaults.uploadShareDefaultExpirationPeriod&#x60; | &#x60;Integer between 0 and 9999&#x60; | | &#x60;enable_client_side_crypto&#x60; | Activation status of client-side encryption&lt;br&gt;Can only be enabled once; disabling is **NOT** possible.&lt;br&gt;cf. &#x60;GET /system/config/settings/general&#x60; &#x60;GeneralSettings.cryptoEnabled&#x60; | &#x60;true or false&#x60;&lt;br&gt;default: &#x60;false&#x60; | | &#x60;eula_active&#x60; | Each user has to confirm the EULA at first login.&lt;br&gt;cf. &#x60;GET /system/config/settings/general&#x60; &#x60;GeneralSettings.eulaEnabled&#x60; | &#x60;true or false&#x60; | | &#x60;eventlog_retention_period&#x60; | Retention period (in days) of event log entries&lt;br&gt;After that period, all entries are deleted.&lt;br&gt;cf. &#x60;GET /system/config/settings/eventlog&#x60; &#x60;EventlogConfig.retentionPeriod&#x60; | &#x60;Integer between 0 and 9999&#x60;&lt;br&gt;If set to &#x60;0&#x60;: no logs are deleted&lt;br&gt;Recommended value: &#x60;7&#x60; | | &#x60;ip_address_logging&#x60; | Determines whether a user&#39;s IP address is logged.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;GET /system/config/settings/eventlog&#x60; &#x60;EventlogConfig.logIpEnabled&#x60;&lt;br&gt;cf. &#x60;GET /system/config/settings/syslog&#x60; &#x60;SyslogConfig.logIpEnabled&#x60; | &#x60;true or false&#x60; | | &#x60;mailserver&#x60; | Email server to send emails.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;GET /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.host&#x60; | &#x60;DNS name or IPv4 of an email server&#x60; | | &#x60;mailserver_authentication_necessary&#x60; | Set to &#x60;true&#x60; if the email server requires authentication.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;GET /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.authenticationEnabled&#x60; | &#x60;true or false&#x60; | | &#x60;mailserver_password&#x60; | **Password is no longer returned.**&lt;br&gt;Check &#x60;mailserver_password_set&#x60; to determine whether password is set. |  | | &#x60;mailserver_password_set&#x60; | Indicates if a password is set for the mailserver (because &#x60;mailserver_password&#x60; is always returned empty).&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;GET /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.passwordDefined&#x60; | &#x60;true or false&#x60; | | &#x60;mailserver_port&#x60; | Email server port&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;GET /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.port&#x60; | &#x60;Valid port number&#x60; | | &#x60;mailserver_username&#x60; | User ame for email server&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;GET /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.username&#x60; | &#x60;Username for authentication&#x60; | | &#x60;mailserver_use_ssl&#x60; | Email server requires SSL connection?&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;Requires &#x60;mailserver_use_starttls&#x60; to be &#x60;false&#x60;&lt;br&gt;cf. &#x60;GET /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.username&#x60; | &#x60;true or false&#x60; | | &#x60;mailserver_use_starttls&#x60; | Email server requires StartTLS connection?&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;Requires &#x60;mailserver_use_ssl&#x60; to be &#x60;false&#x60;&lt;br&gt;cf. &#x60;GET /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.starttlsEnabled&#x60; | &#x60;true or false&#x60; | | &#x60;syslog&#x60; | Write logs to a syslog interface.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;GET /system/config/settings/syslog&#x60; &#x60;SyslogConfig.enabled&#x60; | &#x60;true or false&#x60; | | &#x60;syslog_host&#x60; | Syslog server (IP or FQDN)&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;GET /system/config/settings/syslog&#x60; &#x60;SyslogConfig.host&#x60; | &#x60;DNS name or IPv4 of a syslog server&#x60; | | &#x60;syslog_port&#x60; | Syslog server port&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;GET /system/config/settings/syslog&#x60; &#x60;SyslogConfig.port&#x60; | &#x60;Valid port number&#x60; | | &#x60;syslog_protocol&#x60; | Protocol to connect to syslog server.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;GET /system/config/settings/syslog&#x60; &#x60;SyslogConfig.protocol&#x60; | &#x60;TCP or UDP&#x60; | | &#x60;enable_email_notification_button&#x60; | Enable mail notification button.&lt;br&gt;cf. &#x60;GET /system/config/settings/general&#x60; &#x60;GeneralSettings.emailNotificationButtonEnabled&#x60; | &#x60;true or false&#x60; | | &#x60;allow_share_password_sms&#x60; | Allow sending of share passwords via SMS.&lt;br&gt;cf. &#x60;GET /system/config/settings/general&#x60; &#x60;GeneralSettings.sharePasswordSmsEnabled&#x60; | &#x60;true or false&#x60; | | &#x60;globally_allow_share_password_sms&#x60; | Allow sending of share passwords via SMS **system-wide** (read-only).&lt;br&gt;cf. &#x60;GET /system/config/settings/infrastructure&#x60; &#x60;InfrastructureProperties.smsConfigEnabled&#x60; | &#x60;true or false&#x60; | | &#x60;use_s3_storage&#x60; | Defines if S3 is used as storage backend.&lt;br&gt;Can only be enabled once; disabling is **NOT** possible.&lt;br&gt;cf. &#x60;GET /system/config/settings/general&#x60; &#x60;GeneralSettings.useS3Storage&#x60; | &#x60;true or false&#x60; | | &#x60;s3_default_region&#x60; |Suggested S3 region (read-only)&lt;br&gt;cf. &#x60;GET /system/config/settings/infrastructure&#x60; &#x60;InfrastructureProperties.s3DefaultRegion&#x60; | &#x60;Region name&#x60; |  &lt;/details&gt;  ### Deprecated settings &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &lt;del&gt;&#x60;allow_system_global_weak_password&#x60;&lt;/del&gt; | Determines whether weak password (cf. _Password Policy_ below) is allowed.&lt;br&gt;cf. &#x60;GET /system/config/settings/general&#x60; &#x60;GeneralSettings.weakPasswordEnabled&#x60;&lt;br&gt;Use &#x60;GET /system/config/policies/passwords&#x60; API to get configured password policies. | &#x60;true or false&#x60; | | &lt;del&gt;&#x60;branding_server_customer&#x60;&lt;/del&gt; | The UUID of the branding server customer, which corresponds to customer key in the branding server. | &#x60;String&#x60; | | &lt;del&gt;&#x60;branding_server_url&#x60;&lt;/del&gt; | Access URL to to the Branding Server.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer. | &#x60;String&#x60; | | &lt;del&gt;&#x60;email_from&#x60;&lt;/del&gt; | Sender of system-generated emails&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;**Moved to branding** | &#x60;Valid email address&#x60; | | &lt;del&gt;&#x60;email_to_sales&#x60;&lt;/del&gt; | Contact email address for customers to request more user licenses or data volume.&lt;br&gt;**Moved to branding** | &#x60;Valid email address&#x60; | | &lt;del&gt;&#x60;email_to_support&#x60;&lt;/del&gt; | Support email address for users&lt;br&gt;**Moved to branding** | &#x60;Valid email address&#x60; | | &lt;del&gt;&#x60;file_size_js&#x60;&lt;/del&gt; | Maximum file size (in bytes) for downloads of encrypted files with JavaScript.&lt;br&gt;Bigger files will require a JavaApplet. | &#x60;Integer&#x60;&lt;br&gt;Recommended value: &#x60;10485760&#x60; (&#x3D;&#x60;10MB&#x60;) | | &lt;del&gt;&#x60;system_name&#x60;&lt;/del&gt; | System name&lt;br&gt;**Moved to branding** use &#x60;product.title&#x60; | &#x60;Display name of the DRACOON&#x60; |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      ConfigOptionList result = apiInstance.requestSystemSettings(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#requestSystemSettings");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**ConfigOptionList**](ConfigOptionList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="updateSystemSettings"></a>
# **updateSystemSettings**
> updateSystemSettings(configOptionList, xSdsAuthToken)

Update system settings

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.6.0&lt;/h3&gt;  ### Description: Update configurable settings.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: One or more global settings gets changed.  ### Further Information: This API is deprecated and will be removed in the future.   Check for every settings key new corresponding API and key below.  ### Configurable settings: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;branding_server_branding_id&#x60; | The branding UUID, which corresponds to _BRANDING-QUALIFIER_ in the new branding server.&lt;br&gt;cf. &#x60;PUT /system/config/settings/branding&#x60; &#x60;BrandingConfig.brandingQualifier&#x60; | &#x60;String&#x60; | | &#x60;branding_portal_url&#x60; | Access URL to to the Branding Portal&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;PUT /system/config/settings/branding&#x60; &#x60;BrandingConfig.brandingProviderUrl&#x60; | &#x60;String&#x60; | | &#x60;dblog&#x60; | Write logs to local database.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;PUT /system/config/settings/eventlog&#x60; &#x60;EventlogConfig.enabled&#x60; | &#x60;true or false&#x60; | | &#x60;default_downloadshare_expiration_period&#x60; | Default expiration period for Download Shares in days&lt;br&gt;cf. &#x60;PUT /system/config/settings/defaults&#x60; &#x60;SystemDefaults.downloadShareDefaultExpirationPeriod&#x60; | &#x60;Integer between 0 and 9999&#x60;&lt;br&gt;Set &#x60;0&#x60; to disable. | | &#x60;default_file_upload_expiration_date&#x60; | Default expiration period for all uploaded files in days&lt;br&gt;cf. &#x60;PUT /system/config/settings/defaults&#x60; &#x60;SystemDefaults.fileDefaultExpirationPeriod&#x60; | &#x60;Integer between 0 and 9999&#x60;&lt;br&gt;Set &#x60;0&#x60; to disable. | | &#x60;default_language&#x60; | Define which language should be default.&lt;br&gt;cf. &#x60;PUT /system/config/settings/defaults&#x60; &#x60;SystemDefaults.languageDefault&#x60; | cf. &#x60;GET /public/system/info&#x60; - &#x60;SystemInfo.languageDefault&#x60; | | &#x60;default_uploadshare_expiration_period&#x60; | Default expiration period for Upload Shares in days&lt;br&gt;cf. &#x60;PUT /system/config/settings/defaults&#x60; &#x60;SystemDefaults.uploadShareDefaultExpirationPeriod&#x60; | &#x60;Integer between 0 and 9999&#x60;&lt;br&gt;Set &#x60;0&#x60; to disable. | | &#x60;enable_client_side_crypto&#x60; | Activation status of client-side encryption&lt;br&gt;Can only be enabled once; disabling is **NOT** possible.&lt;br&gt;cf. &#x60;PUT /system/config/settings/general&#x60; &#x60;GeneralSettings.cryptoEnabled&#x60; | &#x60;true or false&#x60;&lt;br&gt;default: &#x60;false&#x60; | | &#x60;eula_active&#x60; | Each user has to confirm the EULA at first login.&lt;br&gt;cf. &#x60;PUT /system/config/settings/general&#x60; &#x60;GeneralSettings.eulaEnabled&#x60; | &#x60;true or false&#x60; | | &#x60;eventlog_retention_period&#x60; | Retention period (in days) of event log entries&lt;br&gt;After that period, all entries are deleted.&lt;br&gt;cf. &#x60;PUT /system/config/settings/eventlog&#x60; &#x60;EventlogConfig.retentionPeriod&#x60; | &#x60;Integer between 0 and 9999&#x60;&lt;br&gt;If set to &#x60;0&#x60;: no logs are deleted&lt;br&gt;Recommended value: &#x60;7&#x60; | | &#x60;ip_address_logging&#x60; | Determines whether a user&#39;s IP address is logged.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;PUT /system/config/settings/eventlog&#x60; &#x60;EventlogConfig.logIpEnabled&#x60;&lt;br&gt;cf. &#x60;PUT /system/config/settings/syslog&#x60; &#x60;SyslogConfig.logIpEnabled&#x60; | &#x60;true or false&#x60; | | &#x60;mailserver&#x60; | Email server to send emails.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;PUT /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.host&#x60; | &#x60;DNS name or IPv4 of an email server&#x60; | | &#x60;mailserver_authentication_necessary&#x60; | Set to &#x60;true&#x60; if the email server requires authentication.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;PUT /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.authenticationEnabled&#x60; | &#x60;true or false&#x60; | | &#x60;mailserver_password&#x60; | Password for email server&lt;br&gt;cf. &#x60;PUT /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.password&#x60; | &#x60;Password for authentication&#x60; | | &#x60;mailserver_port&#x60; | Email server port&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;PUT /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.port&#x60; | &#x60;Valid port number&#x60; | | &#x60;mailserver_username&#x60; | Username for email server&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;PUT /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.username&#x60; | &#x60;Username for authentication&#x60; | | &#x60;mailserver_use_ssl&#x60; | Email server requires SSL connection?&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;Requires &#x60;mailserver_use_starttls&#x60; to be &#x60;false&#x60;&lt;br&gt;cf. &#x60;PUT /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.username&#x60; | &#x60;true or false&#x60; | | &#x60;mailserver_use_starttls&#x60; | Email server requires StartTLS connection?&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;Requires &#x60;mailserver_use_ssl&#x60; to be &#x60;false&#x60;&lt;br&gt;cf. &#x60;PUT /system/config/settings/mail_server&#x60; &#x60;MailServerConfig.starttlsEnabled&#x60; | &#x60;true or false&#x60; | | &#x60;syslog&#x60; | Write logs to a syslog interface.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;PUT /system/config/settings/syslog&#x60; &#x60;SyslogConfig.enabled&#x60; | &#x60;true or false&#x60; | | &#x60;syslog_host&#x60; | Syslog server (IP or FQDN)&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;PUT /system/config/settings/syslog&#x60; &#x60;SyslogConfig.host&#x60; | &#x60;DNS name or IPv4 of a syslog server&#x60; | | &#x60;syslog_port&#x60; | Syslog server port&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;PUT /system/config/settings/syslog&#x60; &#x60;SyslogConfig.port&#x60; | &#x60;Valid port number&#x60; | | &#x60;syslog_protocol&#x60; | Protocol to connect to syslog server.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;cf. &#x60;PUT /system/config/settings/syslog&#x60; &#x60;SyslogConfig.protocol&#x60; | &#x60;TCP or UDP&#x60; | | &#x60;enable_email_notification_button&#x60; | Enable mail notification button.&lt;br&gt;cf. &#x60;PUT /system/config/settings/general&#x60; &#x60;GeneralSettings.emailNotificationButtonEnabled&#x60; | &#x60;true or false&#x60; | | &#x60;allow_share_password_sms&#x60; | Allow sending of share passwords via SMS.&lt;br&gt;cf. &#x60;PUT /system/config/settings/general&#x60; &#x60;GeneralSettings.sharePasswordSmsEnabled&#x60; | &#x60;true or false&#x60; |  &lt;/details&gt;  ### Deprecated settings: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &lt;del&gt;&#x60;allow_system_global_weak_password&#x60;&lt;/del&gt; | Determines whether weak password (cf. _Password Policy_ below) is allowed.&lt;br&gt;cf. &#x60;PUT /system/config/settings/general&#x60; &#x60;GeneralSettings.weakPasswordEnabled&#x60;&lt;br&gt;Use &#x60;PUT /system/config/policies/passwords&#x60; API to change configured password policies. | &#x60;true or false&#x60; | | &lt;del&gt;&#x60;branding_server_customer&#x60;&lt;/del&gt; | The UUID of the branding server customer, which corresponds to customer key in the branding server. | &#x60;String&#x60; | | &lt;del&gt;&#x60;branding_server_url&#x60;&lt;/del&gt; | Access URL to to the Branding Server.&lt;br&gt;Only visible for _Config Manager_ of Provider Customer. | &#x60;String&#x60; | | &lt;del&gt;&#x60;email_from&#x60;&lt;/del&gt; | Sender of system-generated emails&lt;br&gt;Only visible for _Config Manager_ of Provider Customer.&lt;br&gt;**Moved to branding** | &#x60;Valid email address&#x60; | | &lt;del&gt;&#x60;email_to_sales&#x60;&lt;/del&gt; | Contact email address for customers to request more user licenses or data volume.&lt;br&gt;**Moved to branding** | &#x60;Valid email address&#x60; | | &lt;del&gt;&#x60;email_to_support&#x60;&lt;/del&gt; | Support email address for users&lt;br&gt;**Moved to branding** | &#x60;Valid email address&#x60; | | &lt;del&gt;&#x60;file_size_js&#x60;&lt;/del&gt; | Maximum file size (in bytes) for downloads of encrypted files with JavaScript.&lt;br&gt;Bigger files will require a JavaApplet. | &#x60;Integer&#x60;&lt;br&gt;Recommended value: &#x60;10485760&#x60; (&#x3D;&#x60;10MB&#x60;) | | &lt;del&gt;&#x60;system_name&#x60;&lt;/del&gt; | System name&lt;br&gt;**Moved to branding** use &#x60;product.title&#x60; | &#x60;Display name of the DRACOON&#x60; |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    ConfigOptionList configOptionList = new ConfigOptionList(); // ConfigOptionList | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      apiInstance.updateSystemSettings(configOptionList, xSdsAuthToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#updateSystemSettings");
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
| **configOptionList** | [**ConfigOptionList**](ConfigOptionList.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

