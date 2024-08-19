# UninstallationApi

All URIs are relative to *https://api.shop-pro.jp*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteInstallation**](UninstallationApi.md#deleteInstallation) | **DELETE** /appstore/v1/installation.json | アプリストアアプリのアンインストール |


<a id="deleteInstallation"></a>
# **deleteInstallation**
> DeleteInstallation200Response deleteInstallation()

アプリストアアプリのアンインストール

このAPIは OAuth のアクセストークンに紐付くアプリケーションをショップから削除します。 このAPIを利用した場合、ショップオーナーがアンインストールした場合と異なり、アンインストールフックは実行されません。 代わりにアンインストールフックで通知される情報は、このAPIのレスポンスに含まれています。  アンインストール時の注意点については、[アプリのアンインストール](https://app.shop-pro.jp/open_api#section/API/アプリのインストール)を参照して下さい。 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UninstallationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shop-pro.jp");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UninstallationApi apiInstance = new UninstallationApi(defaultClient);
    try {
      DeleteInstallation200Response result = apiInstance.deleteInstallation();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UninstallationApi#deleteInstallation");
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

[**DeleteInstallation200Response**](DeleteInstallation200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | アンインストール成功 |  -  |

