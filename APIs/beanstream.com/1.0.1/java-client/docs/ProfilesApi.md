# ProfilesApi

All URIs are relative to *https://www.beanstream.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**profilesPost**](ProfilesApi.md#profilesPost) | **POST** /profiles | Create Profile |
| [**profilesProfileIdCardsCardIdDelete**](ProfilesApi.md#profilesProfileIdCardsCardIdDelete) | **DELETE** /profiles/{profileId}/cards/{cardId} | Delete card |
| [**profilesProfileIdCardsCardIdPut**](ProfilesApi.md#profilesProfileIdCardsCardIdPut) | **PUT** /profiles/{profileId}/cards/{cardId} | Update card |
| [**profilesProfileIdCardsGet**](ProfilesApi.md#profilesProfileIdCardsGet) | **GET** /profiles/{profileId}/cards | Get cards |
| [**profilesProfileIdCardsPost**](ProfilesApi.md#profilesProfileIdCardsPost) | **POST** /profiles/{profileId}/cards | Add card |
| [**profilesProfileIdDelete**](ProfilesApi.md#profilesProfileIdDelete) | **DELETE** /profiles/{profileId} | Delete profile |
| [**profilesProfileIdGet**](ProfilesApi.md#profilesProfileIdGet) | **GET** /profiles/{profileId} | Get profile |
| [**profilesProfileIdPut**](ProfilesApi.md#profilesProfileIdPut) | **PUT** /profiles/{profileId} | Update Profile |


<a id="profilesPost"></a>
# **profilesPost**
> ProfileResponse profilesPost(createProfileBody)

Create Profile

Create a new Payment Profile using either a card or a Legato token. You must supply one of them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    CreateProfileBody createProfileBody = new CreateProfileBody(); // CreateProfileBody | 
    try {
      ProfileResponse result = apiInstance.profilesPost(createProfileBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesPost");
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
| **createProfileBody** | [**CreateProfileBody**](CreateProfileBody.md)|  | |

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Profile. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

<a id="profilesProfileIdCardsCardIdDelete"></a>
# **profilesProfileIdCardsCardIdDelete**
> ProfileResponse profilesProfileIdCardsCardIdDelete(profileId, cardId)

Delete card

Delete a card on the profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
    BigDecimal cardId = new BigDecimal(78); // BigDecimal | The card id.
    try {
      ProfileResponse result = apiInstance.profilesProfileIdCardsCardIdDelete(profileId, cardId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesProfileIdCardsCardIdDelete");
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
| **profileId** | **String**| The profile id. (aka CustomerCode) | |
| **cardId** | **BigDecimal**| The card id. | |

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Profile. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

<a id="profilesProfileIdCardsCardIdPut"></a>
# **profilesProfileIdCardsCardIdPut**
> ProfileResponse profilesProfileIdCardsCardIdPut(profileId, cardId, card)

Update card

Update the details of a card on the profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
    BigDecimal cardId = new BigDecimal(78); // BigDecimal | The card id.
    ProfileCard card = new ProfileCard(); // ProfileCard | The card that will be updated on the profile.
    try {
      ProfileResponse result = apiInstance.profilesProfileIdCardsCardIdPut(profileId, cardId, card);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesProfileIdCardsCardIdPut");
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
| **profileId** | **String**| The profile id. (aka CustomerCode) | |
| **cardId** | **BigDecimal**| The card id. | |
| **card** | [**ProfileCard**](ProfileCard.md)| The card that will be updated on the profile. | |

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Profile. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

<a id="profilesProfileIdCardsGet"></a>
# **profilesProfileIdCardsGet**
> ProfileGetCards profilesProfileIdCardsGet(profileId)

Get cards

Get all of the cards on the profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
    try {
      ProfileGetCards result = apiInstance.profilesProfileIdCardsGet(profileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesProfileIdCardsGet");
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
| **profileId** | **String**| The profile id. (aka CustomerCode) | |

### Return type

[**ProfileGetCards**](ProfileGetCards.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Profile. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

<a id="profilesProfileIdCardsPost"></a>
# **profilesProfileIdCardsPost**
> ProfileResponse profilesProfileIdCardsPost(profileId, card)

Add card

Add a card to the profile. Note that there is a default limit of 1 card per profile. You can change this in your Profiles settings in the back office.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
    ProfileCard card = new ProfileCard(); // ProfileCard | The card that will be added to the profile.
    try {
      ProfileResponse result = apiInstance.profilesProfileIdCardsPost(profileId, card);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesProfileIdCardsPost");
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
| **profileId** | **String**| The profile id. (aka CustomerCode) | |
| **card** | [**ProfileCard**](ProfileCard.md)| The card that will be added to the profile. | |

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Profile. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

<a id="profilesProfileIdDelete"></a>
# **profilesProfileIdDelete**
> ProfileResponse profilesProfileIdDelete(profileId)

Delete profile

Delete a Payment Profile using the profile ID, also known as the Customer Code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
    try {
      ProfileResponse result = apiInstance.profilesProfileIdDelete(profileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesProfileIdDelete");
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
| **profileId** | **String**| The profile id. (aka CustomerCode) | |

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Profile. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

<a id="profilesProfileIdGet"></a>
# **profilesProfileIdGet**
> PaymentProfile profilesProfileIdGet(profileId)

Get profile

Get a Payment Profile using the profile ID, also known as the Customer Code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
    try {
      PaymentProfile result = apiInstance.profilesProfileIdGet(profileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesProfileIdGet");
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
| **profileId** | **String**| The profile id. (aka CustomerCode) | |

### Return type

[**PaymentProfile**](PaymentProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Profile. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

<a id="profilesProfileIdPut"></a>
# **profilesProfileIdPut**
> ProfileResponse profilesProfileIdPut(profileId, updateProfileBody)

Update Profile

Create a new Payment Profile using either a card or a Legato token. You must supply one of them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String profileId = "profileId_example"; // String | The profile id. (aka CustomerCode)
    UpdateProfileBody updateProfileBody = new UpdateProfileBody(); // UpdateProfileBody | 
    try {
      ProfileResponse result = apiInstance.profilesProfileIdPut(profileId, updateProfileBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesProfileIdPut");
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
| **profileId** | **String**| The profile id. (aka CustomerCode) | |
| **updateProfileBody** | [**UpdateProfileBody**](UpdateProfileBody.md)|  | |

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Profile. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |

