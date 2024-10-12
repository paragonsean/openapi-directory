# TokensApi

All URIs are relative to *https://www.bungie.net/Platform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tokensApplyMissingPartnerOffersWithoutClaim**](TokensApi.md#tokensApplyMissingPartnerOffersWithoutClaim) | **POST** /Tokens/Partner/ApplyMissingOffers/{partnerApplicationId}/{targetBnetMembershipId}/ |  |
| [**tokensClaimPartnerOffer**](TokensApi.md#tokensClaimPartnerOffer) | **POST** /Tokens/Partner/ClaimOffer/ |  |
| [**tokensForceDropsRepair**](TokensApi.md#tokensForceDropsRepair) | **POST** /Tokens/Partner/ForceDropsRepair/ |  |
| [**tokensGetBungieRewardsForPlatformUser**](TokensApi.md#tokensGetBungieRewardsForPlatformUser) | **GET** /Tokens/Rewards/GetRewardsForPlatformUser/{membershipId}/{membershipType}/ |  |
| [**tokensGetBungieRewardsForUser**](TokensApi.md#tokensGetBungieRewardsForUser) | **GET** /Tokens/Rewards/GetRewardsForUser/{membershipId}/ |  |
| [**tokensGetBungieRewardsList**](TokensApi.md#tokensGetBungieRewardsList) | **GET** /Tokens/Rewards/BungieRewards/ |  |
| [**tokensGetPartnerOfferSkuHistory**](TokensApi.md#tokensGetPartnerOfferSkuHistory) | **GET** /Tokens/Partner/History/{partnerApplicationId}/{targetBnetMembershipId}/ |  |
| [**tokensGetPartnerRewardHistory**](TokensApi.md#tokensGetPartnerRewardHistory) | **GET** /Tokens/Partner/History/{targetBnetMembershipId}/Application/{partnerApplicationId}/ |  |


<a id="tokensApplyMissingPartnerOffersWithoutClaim"></a>
# **tokensApplyMissingPartnerOffersWithoutClaim**
> GroupV2GetUserClanInviteSetting200Response tokensApplyMissingPartnerOffersWithoutClaim(partnerApplicationId, targetBnetMembershipId)



Apply a partner offer to the targeted user. This endpoint does not claim a new offer, but any already claimed offers will be applied to the game if not already.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TokensApi apiInstance = new TokensApi(defaultClient);
    Integer partnerApplicationId = 56; // Integer | The partner application identifier.
    Long targetBnetMembershipId = 56L; // Long | The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
    try {
      GroupV2GetUserClanInviteSetting200Response result = apiInstance.tokensApplyMissingPartnerOffersWithoutClaim(partnerApplicationId, targetBnetMembershipId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokensApi#tokensApplyMissingPartnerOffersWithoutClaim");
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
| **partnerApplicationId** | **Integer**| The partner application identifier. | |
| **targetBnetMembershipId** | **Long**| The bungie.net user to apply missing offers to. If not self, elevated permissions are required. | |

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="tokensClaimPartnerOffer"></a>
# **tokensClaimPartnerOffer**
> GroupV2GetUserClanInviteSetting200Response tokensClaimPartnerOffer()



Claim a partner offer as the authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TokensApi apiInstance = new TokensApi(defaultClient);
    try {
      GroupV2GetUserClanInviteSetting200Response result = apiInstance.tokensClaimPartnerOffer();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokensApi#tokensClaimPartnerOffer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="tokensForceDropsRepair"></a>
# **tokensForceDropsRepair**
> GroupV2GetUserClanInviteSetting200Response tokensForceDropsRepair()



Twitch Drops self-repair function - scans twitch for drops not marked as fulfilled and resyncs them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TokensApi apiInstance = new TokensApi(defaultClient);
    try {
      GroupV2GetUserClanInviteSetting200Response result = apiInstance.tokensForceDropsRepair();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokensApi#tokensForceDropsRepair");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="tokensGetBungieRewardsForPlatformUser"></a>
# **tokensGetBungieRewardsForPlatformUser**
> TokensGetBungieRewardsList200Response tokensGetBungieRewardsForPlatformUser(membershipId, membershipType)



Returns the bungie rewards for the targeted user when a platform membership Id and Type are used.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TokensApi apiInstance = new TokensApi(defaultClient);
    Long membershipId = 56L; // Long | users platform membershipId for requested user rewards. If not self, elevated permissions are required.
    Integer membershipType = 56; // Integer | The target Destiny 2 membership type.
    try {
      TokensGetBungieRewardsList200Response result = apiInstance.tokensGetBungieRewardsForPlatformUser(membershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokensApi#tokensGetBungieRewardsForPlatformUser");
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
| **membershipId** | **Long**| users platform membershipId for requested user rewards. If not self, elevated permissions are required. | |
| **membershipType** | **Integer**| The target Destiny 2 membership type. | |

### Return type

[**TokensGetBungieRewardsList200Response**](TokensGetBungieRewardsList200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="tokensGetBungieRewardsForUser"></a>
# **tokensGetBungieRewardsForUser**
> TokensGetBungieRewardsList200Response tokensGetBungieRewardsForUser(membershipId)



Returns the bungie rewards for the targeted user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TokensApi apiInstance = new TokensApi(defaultClient);
    Long membershipId = 56L; // Long | bungie.net user membershipId for requested user rewards. If not self, elevated permissions are required.
    try {
      TokensGetBungieRewardsList200Response result = apiInstance.tokensGetBungieRewardsForUser(membershipId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokensApi#tokensGetBungieRewardsForUser");
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
| **membershipId** | **Long**| bungie.net user membershipId for requested user rewards. If not self, elevated permissions are required. | |

### Return type

[**TokensGetBungieRewardsList200Response**](TokensGetBungieRewardsList200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="tokensGetBungieRewardsList"></a>
# **tokensGetBungieRewardsList**
> TokensGetBungieRewardsList200Response tokensGetBungieRewardsList()



Returns a list of the current bungie rewards

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    TokensApi apiInstance = new TokensApi(defaultClient);
    try {
      TokensGetBungieRewardsList200Response result = apiInstance.tokensGetBungieRewardsList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokensApi#tokensGetBungieRewardsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokensGetBungieRewardsList200Response**](TokensGetBungieRewardsList200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="tokensGetPartnerOfferSkuHistory"></a>
# **tokensGetPartnerOfferSkuHistory**
> TokensGetPartnerOfferSkuHistory200Response tokensGetPartnerOfferSkuHistory(partnerApplicationId, targetBnetMembershipId)



Returns the partner sku and offer history of the targeted user. Elevated permissions are required to see users that are not yourself.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TokensApi apiInstance = new TokensApi(defaultClient);
    Integer partnerApplicationId = 56; // Integer | The partner application identifier.
    Long targetBnetMembershipId = 56L; // Long | The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
    try {
      TokensGetPartnerOfferSkuHistory200Response result = apiInstance.tokensGetPartnerOfferSkuHistory(partnerApplicationId, targetBnetMembershipId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokensApi#tokensGetPartnerOfferSkuHistory");
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
| **partnerApplicationId** | **Integer**| The partner application identifier. | |
| **targetBnetMembershipId** | **Long**| The bungie.net user to apply missing offers to. If not self, elevated permissions are required. | |

### Return type

[**TokensGetPartnerOfferSkuHistory200Response**](TokensGetPartnerOfferSkuHistory200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="tokensGetPartnerRewardHistory"></a>
# **tokensGetPartnerRewardHistory**
> TokensGetPartnerRewardHistory200Response tokensGetPartnerRewardHistory(partnerApplicationId, targetBnetMembershipId)



Returns the partner rewards history of the targeted user, both partner offers and Twitch drops.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TokensApi apiInstance = new TokensApi(defaultClient);
    Integer partnerApplicationId = 56; // Integer | The partner application identifier.
    Long targetBnetMembershipId = 56L; // Long | The bungie.net user to return reward history for.
    try {
      TokensGetPartnerRewardHistory200Response result = apiInstance.tokensGetPartnerRewardHistory(partnerApplicationId, targetBnetMembershipId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokensApi#tokensGetPartnerRewardHistory");
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
| **partnerApplicationId** | **Integer**| The partner application identifier. | |
| **targetBnetMembershipId** | **Long**| The bungie.net user to return reward history for. | |

### Return type

[**TokensGetPartnerRewardHistory200Response**](TokensGetPartnerRewardHistory200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

