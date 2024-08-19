# Api.UninstallationApi

All URIs are relative to *https://api.shop-pro.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteInstallation**](UninstallationApi.md#deleteInstallation) | **DELETE** /appstore/v1/installation.json | アプリストアアプリのアンインストール



## deleteInstallation

> DeleteInstallation200Response deleteInstallation()

アプリストアアプリのアンインストール

このAPIは OAuth のアクセストークンに紐付くアプリケーションをショップから削除します。 このAPIを利用した場合、ショップオーナーがアンインストールした場合と異なり、アンインストールフックは実行されません。 代わりにアンインストールフックで通知される情報は、このAPIのレスポンスに含まれています。  アンインストール時の注意点については、[アプリのアンインストール](https://app.shop-pro.jp/open_api#section/API/アプリのインストール)を参照して下さい。 

### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.UninstallationApi();
apiInstance.deleteInstallation((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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

