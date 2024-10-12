# MicrosoftSupport.ServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicesGet**](ServicesApi.md#servicesGet) | **GET** /providers/Microsoft.Support/services/{serviceName} | 
[**servicesList**](ServicesApi.md#servicesList) | **GET** /providers/Microsoft.Support/services | 



## servicesGet

> Service servicesGet(serviceName, apiVersion)



Gets a specific Azure service for support ticket creation.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.ServicesApi();
let serviceName = "serviceName_example"; // String | Name of Azure service
let apiVersion = "apiVersion_example"; // String | Api version
apiInstance.servicesGet(serviceName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceName** | **String**| Name of Azure service | 
 **apiVersion** | **String**| Api version | 

### Return type

[**Service**](Service.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesList

> ServicesListResult servicesList(apiVersion)



Lists all the Azure services available for support ticket creation. Here are the Service Ids for **Billing**, **Subscription Management**, and **Service and subscription limits (Quotas)** issues: &lt;br/&gt;&lt;table&gt;&lt;tr&gt;&lt;td&gt;&lt;u&gt;Issue type&lt;/u&gt;&lt;/td&gt;&lt;td&gt;&lt;u&gt;Service Id&lt;/u&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Billing&lt;/td&gt;&lt;td&gt;&#39;/providers/Microsoft.Support/services/517f2da6-78fd-0498-4e22-ad26996b1dfc&#39;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Subscription Management&lt;/td&gt;&lt;td&gt;&#39;/providers/Microsoft.Support/services/f3dc5421-79ef-1efa-41a5-42bf3cbb52c6&#39;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Quota&lt;/td&gt;&lt;td&gt;&#39;/providers/Microsoft.Support/services/06bfd9d3-516b-d5c6-5802-169c800dec89&#39;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt; &lt;br/&gt;&lt;br/&gt; For **Technical** issues, select the Service Id that maps to the Azure service/product as displayed in the **Services** drop-down list on the Azure portal&#39;s &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/overview&#39;&gt;New support request&lt;/a&gt; page. &lt;br/&gt;&lt;br/&gt; Always use the service and it&#39;s corresponding problem classification(s) obtained programmatically for support ticket creation. This practice ensures that you always have the most recent set of service and problem classification Ids.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.ServicesApi();
let apiVersion = "apiVersion_example"; // String | Api version
apiInstance.servicesList(apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| Api version | 

### Return type

[**ServicesListResult**](ServicesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

