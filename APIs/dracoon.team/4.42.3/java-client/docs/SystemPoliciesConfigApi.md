# SystemPoliciesConfigApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changeClassificationPoliciesConfig**](SystemPoliciesConfigApi.md#changeClassificationPoliciesConfig) | **PUT** /v4/system/config/policies/classifications | Change classification policies |
| [**changeGuestUsersPoliciesConfig**](SystemPoliciesConfigApi.md#changeGuestUsersPoliciesConfig) | **PUT** /v4/system/config/policies/guest_users | Change guest user policies |
| [**changeMfaPoliciesConfig**](SystemPoliciesConfigApi.md#changeMfaPoliciesConfig) | **PUT** /v4/system/config/policies/mfa | Change MFA policies |
| [**changePasswordPoliciesConfig**](SystemPoliciesConfigApi.md#changePasswordPoliciesConfig) | **PUT** /v4/system/config/policies/passwords | Change password policies |
| [**enforceLoginPasswordChange**](SystemPoliciesConfigApi.md#enforceLoginPasswordChange) | **POST** /v4/system/config/policies/passwords/enforce_change | Enforce login password change for all users |
| [**requestClassificationPoliciesConfig**](SystemPoliciesConfigApi.md#requestClassificationPoliciesConfig) | **GET** /v4/system/config/policies/classifications | Request classification policies |
| [**requestGuestUsersPoliciesConfig**](SystemPoliciesConfigApi.md#requestGuestUsersPoliciesConfig) | **GET** /v4/system/config/policies/guest_users | Request guest user policies |
| [**requestMfaPoliciesConfig**](SystemPoliciesConfigApi.md#requestMfaPoliciesConfig) | **GET** /v4/system/config/policies/mfa | Request MFA policies |
| [**requestPasswordPoliciesConfig**](SystemPoliciesConfigApi.md#requestPasswordPoliciesConfig) | **GET** /v4/system/config/policies/passwords | Request password policies |
| [**requestPasswordPoliciesForPasswordType**](SystemPoliciesConfigApi.md#requestPasswordPoliciesForPasswordType) | **GET** /v4/system/config/policies/passwords/{password_type} | Request password policies for a certain password type |


<a id="changeClassificationPoliciesConfig"></a>
# **changeClassificationPoliciesConfig**
> ClassificationPoliciesConfig changeClassificationPoliciesConfig(updateClassificationPoliciesConfig, xSdsAuthToken)

Change classification policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.30.0&lt;/h3&gt;  ### Description: Change current classification policies: * &#x60;shareClassificationPolicies&#x60;  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Classification policies are changed.  ### Further Information: &#x60;classificationRequiresSharePassword&#x60;: When a node has this classification or higher, it cannot be shared without a password. If the node is an encrypted file this policy has no effect. &#x60;0&#x60; means no password will be enforced.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemPoliciesConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemPoliciesConfigApi apiInstance = new SystemPoliciesConfigApi(defaultClient);
    UpdateClassificationPoliciesConfig updateClassificationPoliciesConfig = new UpdateClassificationPoliciesConfig(); // UpdateClassificationPoliciesConfig | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      ClassificationPoliciesConfig result = apiInstance.changeClassificationPoliciesConfig(updateClassificationPoliciesConfig, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemPoliciesConfigApi#changeClassificationPoliciesConfig");
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
| **updateClassificationPoliciesConfig** | [**UpdateClassificationPoliciesConfig**](UpdateClassificationPoliciesConfig.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**ClassificationPoliciesConfig**](ClassificationPoliciesConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="changeGuestUsersPoliciesConfig"></a>
# **changeGuestUsersPoliciesConfig**
> GuestUsersPoliciesConfig changeGuestUsersPoliciesConfig(updateGuestUsersPoliciesConfig, xSdsAuthToken)

Change guest user policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.40.0&lt;/h3&gt;  ### Description: Change current guest user policies.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Guest user policies are changed.    ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemPoliciesConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemPoliciesConfigApi apiInstance = new SystemPoliciesConfigApi(defaultClient);
    UpdateGuestUsersPoliciesConfig updateGuestUsersPoliciesConfig = new UpdateGuestUsersPoliciesConfig(); // UpdateGuestUsersPoliciesConfig | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      GuestUsersPoliciesConfig result = apiInstance.changeGuestUsersPoliciesConfig(updateGuestUsersPoliciesConfig, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemPoliciesConfigApi#changeGuestUsersPoliciesConfig");
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
| **updateGuestUsersPoliciesConfig** | [**UpdateGuestUsersPoliciesConfig**](UpdateGuestUsersPoliciesConfig.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**GuestUsersPoliciesConfig**](GuestUsersPoliciesConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="changeMfaPoliciesConfig"></a>
# **changeMfaPoliciesConfig**
> MfaPoliciesConfig changeMfaPoliciesConfig(updateMfaPoliciesConfig, xSdsAuthToken)

Change MFA policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description: Change current multi-factor authentication policies.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Multi-factor authentication policies are changed.    ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemPoliciesConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemPoliciesConfigApi apiInstance = new SystemPoliciesConfigApi(defaultClient);
    UpdateMfaPoliciesConfig updateMfaPoliciesConfig = new UpdateMfaPoliciesConfig(); // UpdateMfaPoliciesConfig | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      MfaPoliciesConfig result = apiInstance.changeMfaPoliciesConfig(updateMfaPoliciesConfig, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemPoliciesConfigApi#changeMfaPoliciesConfig");
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
| **updateMfaPoliciesConfig** | [**UpdateMfaPoliciesConfig**](UpdateMfaPoliciesConfig.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**MfaPoliciesConfig**](MfaPoliciesConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="changePasswordPoliciesConfig"></a>
# **changePasswordPoliciesConfig**
> PasswordPoliciesConfig changePasswordPoliciesConfig(updatePasswordPoliciesConfig, xSdsAuthToken)

Change password policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.14.0&lt;/h3&gt;  ### Description:   Change current password policies for any password types:   * &#x60;login&#x60; * &#x60;shares&#x60; * &#x60;encryption&#x60;  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Password policies get changed.  ### Further Information: None.  ### Available password policies: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Value | Recommended Value | Password Type | | :--- | :--- | :--- | :--- | :--- | | &#x60;mustContainCharacters&#x60; | Characters which a password must contain:&lt;br&gt;&lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60; - at least one alphabetical character (&#x60;uppercase&#x60; **OR** &#x60;lowercase&#x60;)&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;br&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60; - at least one uppercase character&lt;pre&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60; - at least one lowercase character&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60; - at least one numeric character&lt;pre&gt;0 1 2 3 4 5 6 7 8 9&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60; - at least one special character (letters and digits excluded)&lt;pre&gt;! \&quot; # $ % ( ) * + , - . / : ; &#x3D; ? @ [ \\ ] ^ _ { &amp;#124; } ~&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60; - none of the above&lt;/li&gt;&lt;li&gt;&#x60;all&#x60; - combination of &#x60;uppercase&#x60;, &#x60;lowercase&#x60;, &#x60;numeric&#x60; and &#x60;special&#x60;&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60;&lt;/li&gt;&lt;li&gt;&#x60;all&#x60;&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;uppercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60;&lt;/li&gt;&lt;/ul&gt;  | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfCharacteristicsToEnforce&#x60; | Number of characteristics to enforce.&lt;br&gt;e.g. from &#x60;[\&quot;uppercase\&quot;, \&quot;lowercase\&quot;, \&quot;numeric\&quot;, \&quot;special\&quot;]&#x60;&lt;br&gt;all 4 character sets can be enforced; but also only 2 of them | &#x60;Integer between 0 and 4&#x60;&lt;br&gt;&lt;br&gt;default:&lt;ul&gt;&lt;li&gt;&#x60;none&#x60; - &#x60;0&#x60;&lt;/li&gt;&lt;li&gt;&#x60;all&#x60; - &#x60;4&#x60;&lt;/li&gt;&lt;li&gt;otherwise - amount of distinct values&lt;br&gt;cf. &#x60;mustContainCharacters&#x60; matrix&lt;/li&gt;&lt;/ul&gt; | &#x60;3&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;minLength&#x60; | Minimum number of characters a password must contain. | &#x60;Integer between 1 and 1024&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;: &#x60;12&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;: &#x60;12&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;: &#x60;14&#x60;&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectDictionaryWords&#x60; | Determines whether a password must **NOT** contain word(s) from a dictionary.&lt;br&gt;In &#x60;core-service.properties&#x60; a path to directory with dictionary files (&#x60;*.txt&#x60;) can be defined&lt;br&gt;cf. &#x60;policies.passwords.dictionary.directory&#x60;.&lt;br&gt;&lt;br&gt;If this rule gets enabled &#x60;policies.passwords.dictionary.directory&#x60; must be defined and contain dictionary files.&lt;br&gt;Otherwise, the rule will not have any effect on password validation process. | &#x60;true or false&#x60; | &#x60;true&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectUserInfo&#x60; | Determines whether a password must **NOT** contain user info.&lt;br&gt;Affects user&#39;s **first name**, **last name**, **email** and **user name**. | &#x60;true or false&#x60; | &#x60;true&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectKeyboardPatterns&#x60; | Determines whether a password must **NOT** contain keyboard patterns.&lt;br&gt;e.g. &#x60;qwertz&#x60;, &#x60;asdf&#x60; (min. 4 character pattern) | &#x60;true or false&#x60; | &#x60;true&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfArchivedPasswords&#x60; | Number of passwords to archive. | &#x60;Integer between 0 and 10&#x60;&lt;br&gt;Set &#x60;0&#x60; to disable password history. | &#x60;3&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;passwordExpiration.enabled&#x60; | Determines whether password expiration is enabled.&lt;br&gt;Password expiration policy can only be enabled in context with &#x60;enforceLoginPasswordChange&#x60;. | &#x60;true or false&#x60; | &#x60;false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxPasswordAge&#x60; | Maximum allowed password age (in **days**) | &#x60;positive Integer&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;userLockout.enabled&#x60; | Determines whether user lockout is enabled. | &#x60;true or false&#x60; | &#x60;true&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxNumberOfLoginFailures&#x60; | Maximum allowed number of failed login attempts. | &#x60;positive Integer&#x60; | &#x60;5&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;lockoutPeriod&#x60; | Amount of **minutes** a user has to wait to make another login attempt&lt;br&gt;after &#x60;maxNumberOfLoginFailures&#x60; has been exceeded. | &#x60;positive Integer&#x60; | &#x60;10&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;  ### Deprecated password policies: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Value | Recommended Value | Password Type | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;enforceLoginPasswordChange&#x60;&lt;/del&gt; | Determines whether a login password change should be enforced for all users.&lt;br&gt;Only takes effect, if login password policies get stricter.&lt;br&gt;Use &#x60;POST /system/config/policies/passwords/enforce_change&#x60; API to enforce a login password change. | &#x60;true or false&#x60;&lt;br&gt;default: &#x60;false&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;  ### &#x60;mustContainCharacters&#x60; matrix: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  |  | &#x60;alpha&#x60; | &#x60;uppercase&#x60; | &#x60;lowercase&#x60; | &#x60;numeric&#x60; | &#x60;special&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | | &#x60;alpha&#x60; | &#x60;alpha&#x60; | &#x60;uppercase&#x60; | &#x60;lowercase&#x60; | &#x60;alpha&#x60;&lt;br&gt;&#x60;numeric&#x60; | &#x60;alpha&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | &#x60;uppercase&#x60; | &#x60;uppercase&#x60; | &#x60;uppercase&#x60; | &#x60;uppercase&#x60;&lt;br&gt;&#x60;lowercase&#x60; | &#x60;uppercase&#x60;&lt;br&gt;&#x60;numeric&#x60; | &#x60;uppercase&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | &#x60;lowercase&#x60; | &#x60;lowercase&#x60; | &#x60;uppercase&#x60;&lt;br&gt;&#x60;lowercase&#x60; | &#x60;lowercase&#x60; | &#x60;lowercase&#x60;&lt;br&gt;&#x60;numeric&#x60; | &#x60;lowercase&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | &#x60;numeric&#x60; | &#x60;alpha&#x60;&lt;br&gt;&#x60;numeric&#x60; | &#x60;uppercase&#x60;&lt;br&gt;&#x60;numeric&#x60; | &#x60;lowercase&#x60;&lt;br&gt;&#x60;numeric&#x60; | &#x60;numeric&#x60; | &#x60;numeric&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | &#x60;special&#x60; | &#x60;alpha&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;uppercase&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;lowercase&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;numeric&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;special&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | &#x60;all&#x60; | &#x60;all&#x60; | &#x60;all&#x60; | &#x60;all&#x60; | &#x60;all&#x60; | &#x60;all&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | &#x60;none&#x60; | &#x60;none&#x60; | &#x60;none&#x60; |  &#x60;none&#x60; | &#x60;none&#x60; | &#x60;none&#x60; | &#x60;none&#x60; | &#x60;none&#x60; |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemPoliciesConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemPoliciesConfigApi apiInstance = new SystemPoliciesConfigApi(defaultClient);
    UpdatePasswordPoliciesConfig updatePasswordPoliciesConfig = new UpdatePasswordPoliciesConfig(); // UpdatePasswordPoliciesConfig | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      PasswordPoliciesConfig result = apiInstance.changePasswordPoliciesConfig(updatePasswordPoliciesConfig, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemPoliciesConfigApi#changePasswordPoliciesConfig");
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
| **updatePasswordPoliciesConfig** | [**UpdatePasswordPoliciesConfig**](UpdatePasswordPoliciesConfig.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**PasswordPoliciesConfig**](PasswordPoliciesConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="enforceLoginPasswordChange"></a>
# **enforceLoginPasswordChange**
> enforceLoginPasswordChange(xSdsAuthToken)

Enforce login password change for all users

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Enforce login password change for all users.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Login password change is enforced. Every user has to change their login password at next login.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemPoliciesConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemPoliciesConfigApi apiInstance = new SystemPoliciesConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      apiInstance.enforceLoginPasswordChange(xSdsAuthToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemPoliciesConfigApi#enforceLoginPasswordChange");
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

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestClassificationPoliciesConfig"></a>
# **requestClassificationPoliciesConfig**
> ClassificationPoliciesConfig requestClassificationPoliciesConfig(xSdsAuthToken)

Request classification policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.30.0&lt;/h3&gt;  ### Description:   Retrieve a list of classification policies: * &#x60;shareClassificationPolicies&#x60;  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of configured classification policies is returned.  ### Further Information: &#x60;classificationRequiresSharePassword&#x60;: When a node has this classification or higher, it cannot be shared without a password. If the node is an encrypted file this policy has no effect. &#x60;0&#x60; means no password will be enforced. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemPoliciesConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemPoliciesConfigApi apiInstance = new SystemPoliciesConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      ClassificationPoliciesConfig result = apiInstance.requestClassificationPoliciesConfig(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemPoliciesConfigApi#requestClassificationPoliciesConfig");
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
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestGuestUsersPoliciesConfig"></a>
# **requestGuestUsersPoliciesConfig**
> GuestUsersPoliciesConfig requestGuestUsersPoliciesConfig(xSdsAuthToken)

Request guest user policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.40.0&lt;/h3&gt;  ### Description:   Retrieve guest user policies.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Guest user policies are returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemPoliciesConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemPoliciesConfigApi apiInstance = new SystemPoliciesConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      GuestUsersPoliciesConfig result = apiInstance.requestGuestUsersPoliciesConfig(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemPoliciesConfigApi#requestGuestUsersPoliciesConfig");
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
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestMfaPoliciesConfig"></a>
# **requestMfaPoliciesConfig**
> MfaPoliciesConfig requestMfaPoliciesConfig(xSdsAuthToken)

Request MFA policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description:   Retrieve a list of multi-factor authentication policies.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of configured multi-factor authentication policies is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemPoliciesConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemPoliciesConfigApi apiInstance = new SystemPoliciesConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      MfaPoliciesConfig result = apiInstance.requestMfaPoliciesConfig(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemPoliciesConfigApi#requestMfaPoliciesConfig");
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

[**MfaPoliciesConfig**](MfaPoliciesConfig.md)

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
| **402** | Payment Required |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestPasswordPoliciesConfig"></a>
# **requestPasswordPoliciesConfig**
> PasswordPoliciesConfig requestPasswordPoliciesConfig(xSdsAuthToken)

Request password policies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.14.0&lt;/h3&gt;  ### Description:   Retrieve a list of configured password policies for all password types:   * &#x60;login&#x60; * &#x60;shares&#x60; * &#x60;encryption&#x60;  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of configured password policies is returned.  ### Further Information: None.  ### Available password policies: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Value | Password Type | | :--- | :--- | :--- | :--- | | &#x60;mustContainCharacters&#x60; | Characters which a password must contain:&lt;br&gt;&lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60; - at least one alphabetical character (&#x60;uppercase&#x60; **OR** &#x60;lowercase&#x60;)&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;br&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60; - at least one uppercase character&lt;pre&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60; - at least one lowercase character&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60; - at least one numeric character&lt;pre&gt;0 1 2 3 4 5 6 7 8 9&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60; - at least one special character (letters and digits excluded)&lt;pre&gt;! \&quot; # $ % ( ) * + , - . / : ; &#x3D; ? @ [ \\ ] ^ _ { &amp;#124; } ~&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60; - none of the above&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60;&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfCharacteristicsToEnforce&#x60; | Number of characteristics to enforce.&lt;br&gt;e.g. from &#x60;[\&quot;uppercase\&quot;, \&quot;lowercase\&quot;, \&quot;numeric\&quot;, \&quot;special\&quot;]&#x60;&lt;br&gt;all 4 character sets can be enforced; but also only 2 of them | &#x60;Integer between 0 and 4&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;minLength&#x60; | Minimum number of characters a password must contain. | &#x60;Integer between 1 and 1024&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectDictionaryWords&#x60; | Determines whether a password must **NOT** contain word(s) from a dictionary.&lt;br&gt;In &#x60;core-service.properties&#x60; a path to directory with dictionary files (&#x60;*.txt&#x60;) can be defined&lt;br&gt;cf. &#x60;policies.passwords.dictionary.directory&#x60;.&lt;br&gt;&lt;br&gt;If this rule gets enabled &#x60;policies.passwords.dictionary.directory&#x60; must be defined and contain dictionary files.&lt;br&gt;Otherwise, the rule will not have any effect on password validation process. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectUserInfo&#x60; | Determines whether a password must **NOT** contain user info.&lt;br&gt;Affects user&#39;s **first name**, **last name**, **email** and **user name**. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectKeyboardPatterns&#x60; | Determines whether a password must **NOT** contain keyboard patterns.&lt;br&gt;e.g. &#x60;qwertz&#x60;, &#x60;asdf&#x60; (min. 4 character pattern) | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfArchivedPasswords&#x60; | Number of passwords to archive.&lt;br&gt;Value &#x60;0&#x60; means that password history is disabled. | &#x60;Integer between 0 and 10&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;passwordExpiration.enabled&#x60; | Determines whether password expiration is enabled. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxPasswordAge&#x60; | Maximum allowed password age (in **days**) | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;userLockout.enabled&#x60; | Determines whether user lockout is enabled. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxNumberOfLoginFailures&#x60; | Maximum allowed number of failed login attempts. | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;lockoutPeriod&#x60; | Amount of **minutes** a user has to wait to make another login attempt&lt;br&gt;after &#x60;maxNumberOfLoginFailures&#x60; has been exceeded. | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemPoliciesConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemPoliciesConfigApi apiInstance = new SystemPoliciesConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      PasswordPoliciesConfig result = apiInstance.requestPasswordPoliciesConfig(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemPoliciesConfigApi#requestPasswordPoliciesConfig");
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
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestPasswordPoliciesForPasswordType"></a>
# **requestPasswordPoliciesForPasswordType**
> PasswordPoliciesConfig requestPasswordPoliciesForPasswordType(passwordType, xSdsAuthToken)

Request password policies for a certain password type

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.14.0&lt;/h3&gt;  ### Description:   Retrieve a list of configured password policies for a certain password type:   * &#x60;login&#x60; * &#x60;shares&#x60; * &#x60;encryption&#x60;  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of configured password policies is returned.  ### Further Information: None.  ### Available password policies: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Value | Password Type | | :--- | :--- | :--- | :--- | | &#x60;mustContainCharacters&#x60; | Characters which a password must contain:&lt;br&gt;&lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60; - at least one alphabetical character (&#x60;uppercase&#x60; **OR** &#x60;lowercase&#x60;)&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;br&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60; - at least one uppercase character&lt;pre&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60; - at least one lowercase character&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60; - at least one numeric character&lt;pre&gt;0 1 2 3 4 5 6 7 8 9&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60; - at least one special character (letters and digits excluded)&lt;pre&gt;! \&quot; # $ % ( ) * + , - . / : ; &#x3D; ? @ [ \\ ] ^ _ { &amp;#124; } ~&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60; - none of the above&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60;&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfCharacteristicsToEnforce&#x60; | Number of characteristics to enforce.&lt;br&gt;e.g. from &#x60;[\&quot;uppercase\&quot;, \&quot;lowercase\&quot;, \&quot;numeric\&quot;, \&quot;special\&quot;]&#x60;&lt;br&gt;all 4 character sets can be enforced; but also only 2 of them | &#x60;Integer between 0 and 4&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;minLength&#x60; | Minimum number of characters a password must contain. | &#x60;Integer between 1 and 1024&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectDictionaryWords&#x60; | Determines whether a password must **NOT** contain word(s) from a dictionary.&lt;br&gt;In &#x60;core-service.properties&#x60; a path to directory with dictionary files (&#x60;*.txt&#x60;) can be defined&lt;br&gt;cf. &#x60;policies.passwords.dictionary.directory&#x60;.&lt;br&gt;&lt;br&gt;If this rule gets enabled &#x60;policies.passwords.dictionary.directory&#x60; must be defined and contain dictionary files.&lt;br&gt;Otherwise, the rule will not have any effect on password validation process. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectUserInfo&#x60; | Determines whether a password must **NOT** contain user info.&lt;br&gt;Affects user&#39;s **first name**, **last name**, **email** and **user name**. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectKeyboardPatterns&#x60; | Determines whether a password must **NOT** contain keyboard patterns.&lt;br&gt;e.g. &#x60;qwertz&#x60;, &#x60;asdf&#x60; (min. 4 character pattern) | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfArchivedPasswords&#x60; | Number of passwords to archive.&lt;br&gt;Value &#x60;0&#x60; means that password history is disabled. | &#x60;Integer between 0 and 10&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;passwordExpiration.enabled&#x60; | Determines whether password expiration is enabled. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxPasswordAge&#x60; | Maximum allowed password age (in **days**) | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;userLockout.enabled&#x60; | Determines whether user lockout is enabled. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxNumberOfLoginFailures&#x60; | Maximum allowed number of failed login attempts. | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;lockoutPeriod&#x60; | Amount of **minutes** a user has to wait to make another login attempt&lt;br&gt;after &#x60;maxNumberOfLoginFailures&#x60; has been exceeded. | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemPoliciesConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemPoliciesConfigApi apiInstance = new SystemPoliciesConfigApi(defaultClient);
    String passwordType = "login"; // String | Password type
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      PasswordPoliciesConfig result = apiInstance.requestPasswordPoliciesForPasswordType(passwordType, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemPoliciesConfigApi#requestPasswordPoliciesForPasswordType");
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
| **passwordType** | **String**| Password type | [enum: login, encryption, shares] |
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
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

