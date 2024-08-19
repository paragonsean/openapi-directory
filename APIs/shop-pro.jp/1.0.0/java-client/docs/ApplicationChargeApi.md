# ApplicationChargeApi

All URIs are relative to *https://api.shop-pro.jp*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUsageCharge**](ApplicationChargeApi.md#createUsageCharge) | **POST** /appstore/v1/recurring_application_charges/{recurringApplicationChargeId}/usage_charges.json | 従量課金データの作成 |
| [**postApplicationCharge**](ApplicationChargeApi.md#postApplicationCharge) | **POST** /appstore/v1/application_charges.json | アプリ内課金データの作成 |


<a id="createUsageCharge"></a>
# **createUsageCharge**
> CreateUsageCharge201Response createUsageCharge(recurringApplicationChargeId, createUsageChargeRequest, xAppstoreUsageChargeToken)

従量課金データの作成

アプリ内で基本機能が利用された頻度に伴って毎月の請求が変動するようなアプリの場合は「従量課金」を使って利用者に変動分の請求を行うことができます。 ※無料お試し期間中のショップに対しては従量課金データを作成できません。 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationChargeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationChargeApi apiInstance = new ApplicationChargeApi(defaultClient);
    String recurringApplicationChargeId = "recurringApplicationChargeId_example"; // String | 課金契約ID
    CreateUsageChargeRequest createUsageChargeRequest = new CreateUsageChargeRequest(); // CreateUsageChargeRequest | 従量課金データ
    String xAppstoreUsageChargeToken = "xAppstoreUsageChargeToken_example"; // String | アンインストール後の従量課金の精算をする際に、 `Authorization` ヘッダへアクセストークンを指定する代わりにこのヘッダを指定することで、このAPIを実行することができます。 インストール中は指定不要で、アンインストール後のみ必須となります。 アンインストールフックで通知される `usage_charge.api_token` の値を指定してください。 このヘッダは、アンインストールフックで通知される `usage_charge.closing_on` まで有効です。この期間を過ぎると従量課金を精算できなくなりますのでご注意ください。詳しくは [アプリのアンインストール](#section/API/アプリのアンインストール) をご確認ください。
    try {
      CreateUsageCharge201Response result = apiInstance.createUsageCharge(recurringApplicationChargeId, createUsageChargeRequest, xAppstoreUsageChargeToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationChargeApi#createUsageCharge");
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
| **recurringApplicationChargeId** | **String**| 課金契約ID | |
| **createUsageChargeRequest** | [**CreateUsageChargeRequest**](CreateUsageChargeRequest.md)| 従量課金データ | |
| **xAppstoreUsageChargeToken** | **String**| アンインストール後の従量課金の精算をする際に、 &#x60;Authorization&#x60; ヘッダへアクセストークンを指定する代わりにこのヘッダを指定することで、このAPIを実行することができます。 インストール中は指定不要で、アンインストール後のみ必須となります。 アンインストールフックで通知される &#x60;usage_charge.api_token&#x60; の値を指定してください。 このヘッダは、アンインストールフックで通知される &#x60;usage_charge.closing_on&#x60; まで有効です。この期間を過ぎると従量課金を精算できなくなりますのでご注意ください。詳しくは [アプリのアンインストール](#section/API/アプリのアンインストール) をご確認ください。 | [optional] |

### Return type

[**CreateUsageCharge201Response**](CreateUsageCharge201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="postApplicationCharge"></a>
# **postApplicationCharge**
> PostApplicationCharge201Response postApplicationCharge(postApplicationChargeRequest)

アプリ内課金データの作成

「アプリ内課金」はすでにインストール済みのアプリ上において、利用者が追加の買い切りによる課金によって新たなアプリ内の機能を提供される場合などに、利用者へ買い切りの課金分の請求を行うための課金形式です。  この課金はプラン課金の情報に紐付かないため、リクエストされたタイミングで課金データが作成されます。また、同一のアプリ内課金IDで同じ利用者へ複数回請求を行うことも可能です。  ただし、アプリの基本機能として提供しているサービスを利用した量やその頻度などに伴って毎月異なった額の請求を行うような課金については、プラン課金の「従量による課金」の機能を使って請求を行う必要があります。 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationChargeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationChargeApi apiInstance = new ApplicationChargeApi(defaultClient);
    PostApplicationChargeRequest postApplicationChargeRequest = new PostApplicationChargeRequest(); // PostApplicationChargeRequest | 
    try {
      PostApplicationCharge201Response result = apiInstance.postApplicationCharge(postApplicationChargeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationChargeApi#postApplicationCharge");
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
| **postApplicationChargeRequest** | [**PostApplicationChargeRequest**](PostApplicationChargeRequest.md)|  | |

### Return type

[**PostApplicationCharge201Response**](PostApplicationCharge201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

