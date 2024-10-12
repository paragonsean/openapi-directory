# HealthRepositoryProviderSpecificationsForHip.DataTransferApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05HealthInformationTransferPost**](DataTransferApi.md#v05HealthInformationTransferPost) | **POST** /v0.5/health-information/transfer | health information transfer API



## v05HealthInformationTransferPost

> v05HealthInformationTransferPost(authorization, dataNotification)

health information transfer API

**NOTE**: This API is actually the callback URL that is passed as **dataPushUrl** in the data request API - /v0.5/health-information/hip/request. This API is directly called by HIP Data Bridge and is not mediated via CM, and hence not routed through the Gateway.    1. This API should be implemented at HIU side. It maybe implemented by the Data Bridge representing the HIU.    2. Entry elements maybe ***content*** or ***link***, although for version 1, entry ***content*** is preferred.    3. Entry ***content*** (or even link reference content) must be encrypted by means of Elliptic-curve Diffie–Hellman Key Exchange, utilizing the HIU keymaterials that are passed through the data request API - /v0.5/health-information/hip/request.    4. Media contains the mimetype of content, and for v1, it is \&quot;application/fhir+json\&quot;   5. checksum is Md5 checksum of the data conent, before encryption   6. Please refer to the NDHM Sandbox Documentation for the format of FHIR bundle that is passed through content  

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.DataTransferApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let dataNotification = new HealthRepositoryProviderSpecificationsForHip.DataNotification(); // DataNotification | 
apiInstance.v05HealthInformationTransferPost(authorization, dataNotification, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **dataNotification** | [**DataNotification**](DataNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

