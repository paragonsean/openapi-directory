# DefaultApi

All URIs are relative to *https://mandrillapp.com/api/1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exportsActivityJsonPost**](DefaultApi.md#exportsActivityJsonPost) | **POST** /exports/activity.json |  |
| [**exportsInfoJsonPost**](DefaultApi.md#exportsInfoJsonPost) | **POST** /exports/info.json |  |
| [**exportsListJsonPost**](DefaultApi.md#exportsListJsonPost) | **POST** /exports/list.json |  |
| [**exportsRejectsJsonPost**](DefaultApi.md#exportsRejectsJsonPost) | **POST** /exports/rejects.json |  |
| [**exportsWhitelistJsonPost**](DefaultApi.md#exportsWhitelistJsonPost) | **POST** /exports/whitelist.json |  |
| [**inboundAddDomainJsonPost**](DefaultApi.md#inboundAddDomainJsonPost) | **POST** /inbound/add-domain.json |  |
| [**inboundAddRouteJsonPost**](DefaultApi.md#inboundAddRouteJsonPost) | **POST** /inbound/add-route.json |  |
| [**inboundCheckDomainJsonPost**](DefaultApi.md#inboundCheckDomainJsonPost) | **POST** /inbound/check-domain.json |  |
| [**inboundDeleteDomainJsonPost**](DefaultApi.md#inboundDeleteDomainJsonPost) | **POST** /inbound/delete-domain.json |  |
| [**inboundDeleteRouteJsonPost**](DefaultApi.md#inboundDeleteRouteJsonPost) | **POST** /inbound/delete-route.json |  |
| [**inboundDomainsJsonPost**](DefaultApi.md#inboundDomainsJsonPost) | **POST** /inbound/domains.json |  |
| [**inboundRoutesJsonPost**](DefaultApi.md#inboundRoutesJsonPost) | **POST** /inbound/routes.json |  |
| [**inboundSendRawJsonPost**](DefaultApi.md#inboundSendRawJsonPost) | **POST** /inbound/send-raw.json |  |
| [**inboundUpdateRouteJsonPost**](DefaultApi.md#inboundUpdateRouteJsonPost) | **POST** /inbound/update-route.json |  |
| [**ipsCancelWarmupJsonPost**](DefaultApi.md#ipsCancelWarmupJsonPost) | **POST** /ips/cancel-warmup.json |  |
| [**ipsCheckCustomDnsJsonPost**](DefaultApi.md#ipsCheckCustomDnsJsonPost) | **POST** /ips/check-custom-dns.json |  |
| [**ipsCreatePoolJsonPost**](DefaultApi.md#ipsCreatePoolJsonPost) | **POST** /ips/create-pool.json |  |
| [**ipsDeleteJsonPost**](DefaultApi.md#ipsDeleteJsonPost) | **POST** /ips/delete.json |  |
| [**ipsDeletePoolJsonPost**](DefaultApi.md#ipsDeletePoolJsonPost) | **POST** /ips/delete-pool.json |  |
| [**ipsInfoJsonPost**](DefaultApi.md#ipsInfoJsonPost) | **POST** /ips/info.json |  |
| [**ipsListJsonPost**](DefaultApi.md#ipsListJsonPost) | **POST** /ips/list.json |  |
| [**ipsListPoolsJsonPost**](DefaultApi.md#ipsListPoolsJsonPost) | **POST** /ips/list-pools.json |  |
| [**ipsPoolInfoJsonPost**](DefaultApi.md#ipsPoolInfoJsonPost) | **POST** /ips/pool-info.json |  |
| [**ipsProvisionJsonPost**](DefaultApi.md#ipsProvisionJsonPost) | **POST** /ips/provision.json |  |
| [**ipsSetCustomDnsJsonPost**](DefaultApi.md#ipsSetCustomDnsJsonPost) | **POST** /ips/set-custom-dns.json |  |
| [**ipsSetPoolJsonPost**](DefaultApi.md#ipsSetPoolJsonPost) | **POST** /ips/set-pool.json |  |
| [**ipsStartWarmupJsonPost**](DefaultApi.md#ipsStartWarmupJsonPost) | **POST** /ips/start-warmup.json |  |
| [**messagesCancelScheduledJsonPost**](DefaultApi.md#messagesCancelScheduledJsonPost) | **POST** /messages/cancel-scheduled.json |  |
| [**messagesContentJsonPost**](DefaultApi.md#messagesContentJsonPost) | **POST** /messages/content.json |  |
| [**messagesInfoJsonPost**](DefaultApi.md#messagesInfoJsonPost) | **POST** /messages/info.json |  |
| [**messagesListScheduledJsonPost**](DefaultApi.md#messagesListScheduledJsonPost) | **POST** /messages/list-scheduled.json |  |
| [**messagesParseJsonPost**](DefaultApi.md#messagesParseJsonPost) | **POST** /messages/parse.json |  |
| [**messagesRescheduleJsonPost**](DefaultApi.md#messagesRescheduleJsonPost) | **POST** /messages/reschedule.json |  |
| [**messagesSearchJsonPost**](DefaultApi.md#messagesSearchJsonPost) | **POST** /messages/search.json |  |
| [**messagesSearchTimeSeriesJsonPost**](DefaultApi.md#messagesSearchTimeSeriesJsonPost) | **POST** /messages/search-time-series.json |  |
| [**messagesSendJsonPost**](DefaultApi.md#messagesSendJsonPost) | **POST** /messages/send.json |  |
| [**messagesSendRawJsonPost**](DefaultApi.md#messagesSendRawJsonPost) | **POST** /messages/send-raw.json |  |
| [**messagesSendTemplateJsonPost**](DefaultApi.md#messagesSendTemplateJsonPost) | **POST** /messages/send-template.json |  |
| [**metadataAddJsonPost**](DefaultApi.md#metadataAddJsonPost) | **POST** /metadata/add.json |  |
| [**metadataDeleteJsonPost**](DefaultApi.md#metadataDeleteJsonPost) | **POST** /metadata/delete.json |  |
| [**metadataListJsonPost**](DefaultApi.md#metadataListJsonPost) | **POST** /metadata/list.json |  |
| [**metadataUpdateJsonPost**](DefaultApi.md#metadataUpdateJsonPost) | **POST** /metadata/update.json |  |
| [**rejectsAddJsonPost**](DefaultApi.md#rejectsAddJsonPost) | **POST** /rejects/add.json |  |
| [**rejectsDeleteJsonPost**](DefaultApi.md#rejectsDeleteJsonPost) | **POST** /rejects/delete.json |  |
| [**rejectsListJsonPost**](DefaultApi.md#rejectsListJsonPost) | **POST** /rejects/list.json |  |
| [**sendersAddDomainJsonPost**](DefaultApi.md#sendersAddDomainJsonPost) | **POST** /senders/add-domain.json |  |
| [**sendersCheckDomainJsonPost**](DefaultApi.md#sendersCheckDomainJsonPost) | **POST** /senders/check-domain.json |  |
| [**sendersDomainsJsonPost**](DefaultApi.md#sendersDomainsJsonPost) | **POST** /senders/domains.json |  |
| [**sendersInfoJsonPost**](DefaultApi.md#sendersInfoJsonPost) | **POST** /senders/info.json |  |
| [**sendersListJsonPost**](DefaultApi.md#sendersListJsonPost) | **POST** /senders/list.json |  |
| [**sendersTimeSeriesJsonPost**](DefaultApi.md#sendersTimeSeriesJsonPost) | **POST** /senders/time-series.json |  |
| [**sendersVerifyDomainJsonPost**](DefaultApi.md#sendersVerifyDomainJsonPost) | **POST** /senders/verify-domain.json |  |
| [**subaccountsAddJsonPost**](DefaultApi.md#subaccountsAddJsonPost) | **POST** /subaccounts/add.json |  |
| [**subaccountsDeleteJsonPost**](DefaultApi.md#subaccountsDeleteJsonPost) | **POST** /subaccounts/delete.json |  |
| [**subaccountsInfoJsonPost**](DefaultApi.md#subaccountsInfoJsonPost) | **POST** /subaccounts/info.json |  |
| [**subaccountsListJsonPost**](DefaultApi.md#subaccountsListJsonPost) | **POST** /subaccounts/list.json |  |
| [**subaccountsPauseJsonPost**](DefaultApi.md#subaccountsPauseJsonPost) | **POST** /subaccounts/pause.json |  |
| [**subaccountsResumeJsonPost**](DefaultApi.md#subaccountsResumeJsonPost) | **POST** /subaccounts/resume.json |  |
| [**subaccountsUpdateJsonPost**](DefaultApi.md#subaccountsUpdateJsonPost) | **POST** /subaccounts/update.json |  |
| [**tagsAllTimeSeriesJsonPost**](DefaultApi.md#tagsAllTimeSeriesJsonPost) | **POST** /tags/all-time-series.json |  |
| [**tagsDeleteJsonPost**](DefaultApi.md#tagsDeleteJsonPost) | **POST** /tags/delete.json |  |
| [**tagsInfoJsonPost**](DefaultApi.md#tagsInfoJsonPost) | **POST** /tags/info.json |  |
| [**tagsListJsonPost**](DefaultApi.md#tagsListJsonPost) | **POST** /tags/list.json |  |
| [**tagsTimeSeriesJsonPost**](DefaultApi.md#tagsTimeSeriesJsonPost) | **POST** /tags/time-series.json |  |
| [**templatesAddJsonPost**](DefaultApi.md#templatesAddJsonPost) | **POST** /templates/add.json |  |
| [**templatesDeleteJsonPost**](DefaultApi.md#templatesDeleteJsonPost) | **POST** /templates/delete.json |  |
| [**templatesInfoJsonPost**](DefaultApi.md#templatesInfoJsonPost) | **POST** /templates/info.json |  |
| [**templatesListJsonPost**](DefaultApi.md#templatesListJsonPost) | **POST** /templates/list.json |  |
| [**templatesPublishJsonPost**](DefaultApi.md#templatesPublishJsonPost) | **POST** /templates/publish.json |  |
| [**templatesRenderJsonPost**](DefaultApi.md#templatesRenderJsonPost) | **POST** /templates/render.json |  |
| [**templatesTimeSeriesJsonPost**](DefaultApi.md#templatesTimeSeriesJsonPost) | **POST** /templates/time-series.json |  |
| [**templatesUpdateJsonPost**](DefaultApi.md#templatesUpdateJsonPost) | **POST** /templates/update.json |  |
| [**urlsAddTrackingDomainJsonPost**](DefaultApi.md#urlsAddTrackingDomainJsonPost) | **POST** /urls/add-tracking-domain.json |  |
| [**urlsCheckTrackingDomainJsonPost**](DefaultApi.md#urlsCheckTrackingDomainJsonPost) | **POST** /urls/check-tracking-domain.json |  |
| [**urlsListJsonPost**](DefaultApi.md#urlsListJsonPost) | **POST** /urls/list.json |  |
| [**urlsSearchJsonPost**](DefaultApi.md#urlsSearchJsonPost) | **POST** /urls/search.json |  |
| [**urlsTimeSeriesJsonPost**](DefaultApi.md#urlsTimeSeriesJsonPost) | **POST** /urls/time-series.json |  |
| [**urlsTrackingDomainsJsonPost**](DefaultApi.md#urlsTrackingDomainsJsonPost) | **POST** /urls/tracking-domains.json |  |
| [**usersInfoJsonPost**](DefaultApi.md#usersInfoJsonPost) | **POST** /users/info.json |  |
| [**usersPing2JsonPost**](DefaultApi.md#usersPing2JsonPost) | **POST** /users/ping2.json |  |
| [**usersPingJsonPost**](DefaultApi.md#usersPingJsonPost) | **POST** /users/ping.json |  |
| [**usersSendersJsonPost**](DefaultApi.md#usersSendersJsonPost) | **POST** /users/senders.json |  |
| [**webhooksAddJsonPost**](DefaultApi.md#webhooksAddJsonPost) | **POST** /webhooks/add.json |  |
| [**webhooksDeleteJsonPost**](DefaultApi.md#webhooksDeleteJsonPost) | **POST** /webhooks/delete.json |  |
| [**webhooksInfoJsonPost**](DefaultApi.md#webhooksInfoJsonPost) | **POST** /webhooks/info.json |  |
| [**webhooksListJsonPost**](DefaultApi.md#webhooksListJsonPost) | **POST** /webhooks/list.json |  |
| [**webhooksUpdateJsonPost**](DefaultApi.md#webhooksUpdateJsonPost) | **POST** /webhooks/update.json |  |
| [**whitelistsAddJsonPost**](DefaultApi.md#whitelistsAddJsonPost) | **POST** /whitelists/add.json |  |
| [**whitelistsDeleteJsonPost**](DefaultApi.md#whitelistsDeleteJsonPost) | **POST** /whitelists/delete.json |  |
| [**whitelistsListJsonPost**](DefaultApi.md#whitelistsListJsonPost) | **POST** /whitelists/list.json |  |


<a id="exportsActivityJsonPost"></a>
# **exportsActivityJsonPost**
> ExportsSatus exportsActivityJsonPost(body)



Begins an export of your activity history. The activity will be exported to a zip archive containing a single file named activity.csv in the same format as you would be able to export from your account&#39;s activity view. It includes the following fields: Date, Email Address, Sender, Subject, Status, Tags, Opens, Clicks, Bounce Detail. If you have configured any custom metadata fields, they will be included in the exported data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ExportsActivity body = new ExportsActivity(); // ExportsActivity | 
    try {
      ExportsSatus result = apiInstance.exportsActivityJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportsActivityJsonPost");
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
| **body** | [**ExportsActivity**](ExportsActivity.md)|  | |

### Return type

[**ExportsSatus**](ExportsSatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="exportsInfoJsonPost"></a>
# **exportsInfoJsonPost**
> ExportsInfoResponse exportsInfoJsonPost(body)



Returns information about an export job. If the export job&#39;s state is &#39;complete&#39;, the returned data will include a URL you can use to fetch the results. Every export job produces a zip archive, but the format of the archive is distinct for each job type. The api calls that initiate exports include more details about the output format for that job type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Id body = new Id(); // Id | 
    try {
      ExportsInfoResponse result = apiInstance.exportsInfoJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportsInfoJsonPost");
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
| **body** | [**Id**](Id.md)|  | |

### Return type

[**ExportsInfoResponse**](ExportsInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="exportsListJsonPost"></a>
# **exportsListJsonPost**
> List&lt;ExportsListResponseInner&gt; exportsListJsonPost(body)



Returns a list of your exports.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<ExportsListResponseInner> result = apiInstance.exportsListJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportsListJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;ExportsListResponseInner&gt;**](ExportsListResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="exportsRejectsJsonPost"></a>
# **exportsRejectsJsonPost**
> ExportsSatus exportsRejectsJsonPost(body)



Begins an export of your rejection blacklist. The blacklist will be exported to a zip archive containing a single file named rejects.csv that includes the following fields: email, reason, detail, created_at, expires_at, last_event_at, expires_at.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    NotifyEmail body = new NotifyEmail(); // NotifyEmail | 
    try {
      ExportsSatus result = apiInstance.exportsRejectsJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportsRejectsJsonPost");
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
| **body** | [**NotifyEmail**](NotifyEmail.md)|  | |

### Return type

[**ExportsSatus**](ExportsSatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="exportsWhitelistJsonPost"></a>
# **exportsWhitelistJsonPost**
> ExportsSatus exportsWhitelistJsonPost(body)



Begins an export of your rejection whitelist. The whitelist will be exported to a zip archive containing a single file named whitelist.csv that includes the following fields: email, detail, created_at.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    NotifyEmail body = new NotifyEmail(); // NotifyEmail | 
    try {
      ExportsSatus result = apiInstance.exportsWhitelistJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportsWhitelistJsonPost");
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
| **body** | [**NotifyEmail**](NotifyEmail.md)|  | |

### Return type

[**ExportsSatus**](ExportsSatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="inboundAddDomainJsonPost"></a>
# **inboundAddDomainJsonPost**
> InboundInfo inboundAddDomainJsonPost(body)



Add an inbound domain to your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Domain body = new Domain(); // Domain | 
    try {
      InboundInfo result = apiInstance.inboundAddDomainJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inboundAddDomainJsonPost");
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
| **body** | [**Domain**](Domain.md)|  | |

### Return type

[**InboundInfo**](InboundInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="inboundAddRouteJsonPost"></a>
# **inboundAddRouteJsonPost**
> Route inboundAddRouteJsonPost(body)



Add a new mailbox route to an inbound domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    InboundAddRoute body = new InboundAddRoute(); // InboundAddRoute | 
    try {
      Route result = apiInstance.inboundAddRouteJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inboundAddRouteJsonPost");
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
| **body** | [**InboundAddRoute**](InboundAddRoute.md)|  | |

### Return type

[**Route**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="inboundCheckDomainJsonPost"></a>
# **inboundCheckDomainJsonPost**
> InboundInfo inboundCheckDomainJsonPost(body)



Check the MX settings for an inbound domain. The domain must have already been added with the add-domain call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Domain body = new Domain(); // Domain | 
    try {
      InboundInfo result = apiInstance.inboundCheckDomainJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inboundCheckDomainJsonPost");
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
| **body** | [**Domain**](Domain.md)|  | |

### Return type

[**InboundInfo**](InboundInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="inboundDeleteDomainJsonPost"></a>
# **inboundDeleteDomainJsonPost**
> InboundInfo inboundDeleteDomainJsonPost(body)



Delete an inbound domain from the account. All mail will stop routing for this domain immediately.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Domain body = new Domain(); // Domain | 
    try {
      InboundInfo result = apiInstance.inboundDeleteDomainJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inboundDeleteDomainJsonPost");
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
| **body** | [**Domain**](Domain.md)|  | |

### Return type

[**InboundInfo**](InboundInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="inboundDeleteRouteJsonPost"></a>
# **inboundDeleteRouteJsonPost**
> Route inboundDeleteRouteJsonPost(body)



Delete an existing inbound mailbox route

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Id body = new Id(); // Id | 
    try {
      Route result = apiInstance.inboundDeleteRouteJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inboundDeleteRouteJsonPost");
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
| **body** | [**Id**](Id.md)|  | |

### Return type

[**Route**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="inboundDomainsJsonPost"></a>
# **inboundDomainsJsonPost**
> List&lt;InboundDomainsResponseInner&gt; inboundDomainsJsonPost(body)



List the domains that have been configured for inbound delivery

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<InboundDomainsResponseInner> result = apiInstance.inboundDomainsJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inboundDomainsJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;InboundDomainsResponseInner&gt;**](InboundDomainsResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="inboundRoutesJsonPost"></a>
# **inboundRoutesJsonPost**
> List&lt;InboundRoutesResponseInner&gt; inboundRoutesJsonPost(body)



List the mailbox routes defined for an inbound domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Domain body = new Domain(); // Domain | 
    try {
      List<InboundRoutesResponseInner> result = apiInstance.inboundRoutesJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inboundRoutesJsonPost");
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
| **body** | [**Domain**](Domain.md)|  | |

### Return type

[**List&lt;InboundRoutesResponseInner&gt;**](InboundRoutesResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="inboundSendRawJsonPost"></a>
# **inboundSendRawJsonPost**
> List&lt;InboundSendRawResponseInner&gt; inboundSendRawJsonPost(body)



Take a raw MIME document destined for a domain with inbound domains set up, and send it to the inbound hook exactly as if it had been sent over SMTP

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    InboundSendRaw body = new InboundSendRaw(); // InboundSendRaw | 
    try {
      List<InboundSendRawResponseInner> result = apiInstance.inboundSendRawJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inboundSendRawJsonPost");
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
| **body** | [**InboundSendRaw**](InboundSendRaw.md)|  | |

### Return type

[**List&lt;InboundSendRawResponseInner&gt;**](InboundSendRawResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="inboundUpdateRouteJsonPost"></a>
# **inboundUpdateRouteJsonPost**
> Route inboundUpdateRouteJsonPost(body)



Update the pattern or webhook of an existing inbound mailbox route. If null is provided for any fields, the values will remain unchanged.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    InboundUpdateRoute body = new InboundUpdateRoute(); // InboundUpdateRoute | 
    try {
      Route result = apiInstance.inboundUpdateRouteJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inboundUpdateRouteJsonPost");
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
| **body** | [**InboundUpdateRoute**](InboundUpdateRoute.md)|  | |

### Return type

[**Route**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsCancelWarmupJsonPost"></a>
# **ipsCancelWarmupJsonPost**
> IpInfo ipsCancelWarmupJsonPost(body)



Cancels the warmup process for a dedicated IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Ip body = new Ip(); // Ip | 
    try {
      IpInfo result = apiInstance.ipsCancelWarmupJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsCancelWarmupJsonPost");
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
| **body** | [**Ip**](Ip.md)|  | |

### Return type

[**IpInfo**](IpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsCheckCustomDnsJsonPost"></a>
# **ipsCheckCustomDnsJsonPost**
> IpsCheckCustomDnsResponse ipsCheckCustomDnsJsonPost(body)



Tests whether a domain name is valid for use as the custom reverse DNS for a dedicated IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    IpDomain body = new IpDomain(); // IpDomain | 
    try {
      IpsCheckCustomDnsResponse result = apiInstance.ipsCheckCustomDnsJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsCheckCustomDnsJsonPost");
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
| **body** | [**IpDomain**](IpDomain.md)|  | |

### Return type

[**IpsCheckCustomDnsResponse**](IpsCheckCustomDnsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsCreatePoolJsonPost"></a>
# **ipsCreatePoolJsonPost**
> IpsPool ipsCreatePoolJsonPost(body)



Creates a pool and returns it. If a pool already exists with this name, no action will be performed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    IpsPoolKey body = new IpsPoolKey(); // IpsPoolKey | 
    try {
      IpsPool result = apiInstance.ipsCreatePoolJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsCreatePoolJsonPost");
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
| **body** | [**IpsPoolKey**](IpsPoolKey.md)|  | |

### Return type

[**IpsPool**](IpsPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsDeleteJsonPost"></a>
# **ipsDeleteJsonPost**
> IpsDeleteResponse ipsDeleteJsonPost(body)



Deletes a dedicated IP. This is permanent and cannot be undone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Ip body = new Ip(); // Ip | 
    try {
      IpsDeleteResponse result = apiInstance.ipsDeleteJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsDeleteJsonPost");
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
| **body** | [**Ip**](Ip.md)|  | |

### Return type

[**IpsDeleteResponse**](IpsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsDeletePoolJsonPost"></a>
# **ipsDeletePoolJsonPost**
> IpsDeletePoolResponse ipsDeletePoolJsonPost(body)



Deletes a pool. A pool must be empty before you can delete it, and you cannot delete your default pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    IpsPoolKey body = new IpsPoolKey(); // IpsPoolKey | 
    try {
      IpsDeletePoolResponse result = apiInstance.ipsDeletePoolJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsDeletePoolJsonPost");
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
| **body** | [**IpsPoolKey**](IpsPoolKey.md)|  | |

### Return type

[**IpsDeletePoolResponse**](IpsDeletePoolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsInfoJsonPost"></a>
# **ipsInfoJsonPost**
> IpInfo ipsInfoJsonPost(body)



Retrieves information about a single dedicated ip.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Ip body = new Ip(); // Ip | 
    try {
      IpInfo result = apiInstance.ipsInfoJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsInfoJsonPost");
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
| **body** | [**Ip**](Ip.md)|  | |

### Return type

[**IpInfo**](IpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsListJsonPost"></a>
# **ipsListJsonPost**
> List&lt;IpsListPoolsResponseInnerIpsInner&gt; ipsListJsonPost(body)



Lists your dedicated IPs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<IpsListPoolsResponseInnerIpsInner> result = apiInstance.ipsListJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsListJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;IpsListPoolsResponseInnerIpsInner&gt;**](IpsListPoolsResponseInnerIpsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsListPoolsJsonPost"></a>
# **ipsListPoolsJsonPost**
> List&lt;IpsListPoolsResponseInner&gt; ipsListPoolsJsonPost(body)



Lists your dedicated IP pools.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<IpsListPoolsResponseInner> result = apiInstance.ipsListPoolsJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsListPoolsJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;IpsListPoolsResponseInner&gt;**](IpsListPoolsResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsPoolInfoJsonPost"></a>
# **ipsPoolInfoJsonPost**
> IpsPool ipsPoolInfoJsonPost(body)



Describes a single dedicated IP pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    IpsPoolKey body = new IpsPoolKey(); // IpsPoolKey | 
    try {
      IpsPool result = apiInstance.ipsPoolInfoJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsPoolInfoJsonPost");
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
| **body** | [**IpsPoolKey**](IpsPoolKey.md)|  | |

### Return type

[**IpsPool**](IpsPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsProvisionJsonPost"></a>
# **ipsProvisionJsonPost**
> IpsProvisionResponse ipsProvisionJsonPost(body)



Requests an additional dedicated IP for your account. Accounts may have one outstanding request at any time, and provisioning requests are processed within 24 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    IpsProvision body = new IpsProvision(); // IpsProvision | 
    try {
      IpsProvisionResponse result = apiInstance.ipsProvisionJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsProvisionJsonPost");
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
| **body** | [**IpsProvision**](IpsProvision.md)|  | |

### Return type

[**IpsProvisionResponse**](IpsProvisionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsSetCustomDnsJsonPost"></a>
# **ipsSetCustomDnsJsonPost**
> IpInfo ipsSetCustomDnsJsonPost(body)



Configures the custom DNS name for a dedicated IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    IpDomain body = new IpDomain(); // IpDomain | 
    try {
      IpInfo result = apiInstance.ipsSetCustomDnsJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsSetCustomDnsJsonPost");
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
| **body** | [**IpDomain**](IpDomain.md)|  | |

### Return type

[**IpInfo**](IpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsSetPoolJsonPost"></a>
# **ipsSetPoolJsonPost**
> IpInfo ipsSetPoolJsonPost(body)



Moves a dedicated IP to a different pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    IpsSetPool body = new IpsSetPool(); // IpsSetPool | 
    try {
      IpInfo result = apiInstance.ipsSetPoolJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsSetPoolJsonPost");
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
| **body** | [**IpsSetPool**](IpsSetPool.md)|  | |

### Return type

[**IpInfo**](IpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ipsStartWarmupJsonPost"></a>
# **ipsStartWarmupJsonPost**
> IpInfo ipsStartWarmupJsonPost(body)



Begins the warmup process for a dedicated IP. During the warmup process, Mandrill will gradually increase the percentage of your mail that is sent over the warming-up IP, over a period of roughly 30 days. The rest of your mail will be sent over shared IPs or other dedicated IPs in the same pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Ip body = new Ip(); // Ip | 
    try {
      IpInfo result = apiInstance.ipsStartWarmupJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipsStartWarmupJsonPost");
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
| **body** | [**Ip**](Ip.md)|  | |

### Return type

[**IpInfo**](IpInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="messagesCancelScheduledJsonPost"></a>
# **messagesCancelScheduledJsonPost**
> SchedulingchangeInfo messagesCancelScheduledJsonPost(body)



Cancels a scheduled email.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MessagesCancelScheduled body = new MessagesCancelScheduled(); // MessagesCancelScheduled | 
    try {
      SchedulingchangeInfo result = apiInstance.messagesCancelScheduledJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#messagesCancelScheduledJsonPost");
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
| **body** | [**MessagesCancelScheduled**](MessagesCancelScheduled.md)|  | |

### Return type

[**SchedulingchangeInfo**](SchedulingchangeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="messagesContentJsonPost"></a>
# **messagesContentJsonPost**
> MessagesContentResponse messagesContentJsonPost(body)



Get the full content of a recently sent message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Id body = new Id(); // Id | 
    try {
      MessagesContentResponse result = apiInstance.messagesContentJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#messagesContentJsonPost");
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
| **body** | [**Id**](Id.md)|  | |

### Return type

[**MessagesContentResponse**](MessagesContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="messagesInfoJsonPost"></a>
# **messagesInfoJsonPost**
> MessagesInfoResponse messagesInfoJsonPost(body)



Get the information for a single recently sent message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Id body = new Id(); // Id | 
    try {
      MessagesInfoResponse result = apiInstance.messagesInfoJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#messagesInfoJsonPost");
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
| **body** | [**Id**](Id.md)|  | |

### Return type

[**MessagesInfoResponse**](MessagesInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="messagesListScheduledJsonPost"></a>
# **messagesListScheduledJsonPost**
> List&lt;MessagesListScheduledResponseInner&gt; messagesListScheduledJsonPost(body)



Queries your scheduled emails by sender or recipient, or both.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MessagesListScheduled body = new MessagesListScheduled(); // MessagesListScheduled | 
    try {
      List<MessagesListScheduledResponseInner> result = apiInstance.messagesListScheduledJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#messagesListScheduledJsonPost");
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
| **body** | [**MessagesListScheduled**](MessagesListScheduled.md)|  | |

### Return type

[**List&lt;MessagesListScheduledResponseInner&gt;**](MessagesListScheduledResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="messagesParseJsonPost"></a>
# **messagesParseJsonPost**
> MessagesParseResponse messagesParseJsonPost(body)



Parse the full MIME document for an email message, returning the content of the message broken into its constituent pieces

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MessagesParse body = new MessagesParse(); // MessagesParse | 
    try {
      MessagesParseResponse result = apiInstance.messagesParseJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#messagesParseJsonPost");
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
| **body** | [**MessagesParse**](MessagesParse.md)|  | |

### Return type

[**MessagesParseResponse**](MessagesParseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="messagesRescheduleJsonPost"></a>
# **messagesRescheduleJsonPost**
> SchedulingchangeInfo messagesRescheduleJsonPost(body)



Reschedules a scheduled email.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MessagesReschedule body = new MessagesReschedule(); // MessagesReschedule | 
    try {
      SchedulingchangeInfo result = apiInstance.messagesRescheduleJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#messagesRescheduleJsonPost");
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
| **body** | [**MessagesReschedule**](MessagesReschedule.md)|  | |

### Return type

[**SchedulingchangeInfo**](SchedulingchangeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="messagesSearchJsonPost"></a>
# **messagesSearchJsonPost**
> List&lt;MessagesSearchResponseInner&gt; messagesSearchJsonPost(body)



Search the content of recently sent messages and optionally narrow by date range, tags and senders. This method may be called up to 20 times per minute. If you need the data more often, you can use /messages/info.json to get the information for a single message, or webhooks to push activity to your own application for querying.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MessagesSearch body = new MessagesSearch(); // MessagesSearch | 
    try {
      List<MessagesSearchResponseInner> result = apiInstance.messagesSearchJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#messagesSearchJsonPost");
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
| **body** | [**MessagesSearch**](MessagesSearch.md)|  | |

### Return type

[**List&lt;MessagesSearchResponseInner&gt;**](MessagesSearchResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="messagesSearchTimeSeriesJsonPost"></a>
# **messagesSearchTimeSeriesJsonPost**
> List&lt;TimeseriesInner&gt; messagesSearchTimeSeriesJsonPost(body)



Search the content of recently sent messages and return the aggregated hourly stats for matching messages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MessagesSearchTimeSeries body = new MessagesSearchTimeSeries(); // MessagesSearchTimeSeries | 
    try {
      List<TimeseriesInner> result = apiInstance.messagesSearchTimeSeriesJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#messagesSearchTimeSeriesJsonPost");
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
| **body** | [**MessagesSearchTimeSeries**](MessagesSearchTimeSeries.md)|  | |

### Return type

[**List&lt;TimeseriesInner&gt;**](TimeseriesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="messagesSendJsonPost"></a>
# **messagesSendJsonPost**
> List&lt;MessageSendStatusInner&gt; messagesSendJsonPost(body)



Send a new transactional message through Mandrill

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MessagesSend body = new MessagesSend(); // MessagesSend | 
    try {
      List<MessageSendStatusInner> result = apiInstance.messagesSendJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#messagesSendJsonPost");
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
| **body** | [**MessagesSend**](MessagesSend.md)|  | |

### Return type

[**List&lt;MessageSendStatusInner&gt;**](MessageSendStatusInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="messagesSendRawJsonPost"></a>
# **messagesSendRawJsonPost**
> List&lt;MessageSendStatusInner&gt; messagesSendRawJsonPost(body)



Take a raw MIME document for a message, and send it exactly as if it were sent through Mandrill&#39;s SMTP servers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MessagesSendRaw body = new MessagesSendRaw(); // MessagesSendRaw | 
    try {
      List<MessageSendStatusInner> result = apiInstance.messagesSendRawJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#messagesSendRawJsonPost");
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
| **body** | [**MessagesSendRaw**](MessagesSendRaw.md)|  | |

### Return type

[**List&lt;MessageSendStatusInner&gt;**](MessageSendStatusInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="messagesSendTemplateJsonPost"></a>
# **messagesSendTemplateJsonPost**
> List&lt;MessageSendStatusInner&gt; messagesSendTemplateJsonPost(body)



Send a new transactional message through Mandrill using a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MessagesSendTemplate body = new MessagesSendTemplate(); // MessagesSendTemplate | 
    try {
      List<MessageSendStatusInner> result = apiInstance.messagesSendTemplateJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#messagesSendTemplateJsonPost");
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
| **body** | [**MessagesSendTemplate**](MessagesSendTemplate.md)|  | |

### Return type

[**List&lt;MessageSendStatusInner&gt;**](MessageSendStatusInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="metadataAddJsonPost"></a>
# **metadataAddJsonPost**
> MetadataInfo metadataAddJsonPost(body)



Add a new custom metadata field to be indexed for the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MetadataTemplate body = new MetadataTemplate(); // MetadataTemplate | 
    try {
      MetadataInfo result = apiInstance.metadataAddJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#metadataAddJsonPost");
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
| **body** | [**MetadataTemplate**](MetadataTemplate.md)|  | |

### Return type

[**MetadataInfo**](MetadataInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="metadataDeleteJsonPost"></a>
# **metadataDeleteJsonPost**
> MetadataInfo metadataDeleteJsonPost(body)



Delete an existing custom metadata field. Deletion isn&#39;t instataneous, and /metadata/list will continue to return the field until the asynchronous deletion process is complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Name body = new Name(); // Name | 
    try {
      MetadataInfo result = apiInstance.metadataDeleteJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#metadataDeleteJsonPost");
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
| **body** | [**Name**](Name.md)|  | |

### Return type

[**MetadataInfo**](MetadataInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="metadataListJsonPost"></a>
# **metadataListJsonPost**
> List&lt;MetadataListResponseInner&gt; metadataListJsonPost(body)



Get the list of custom metadata fields indexed for the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<MetadataListResponseInner> result = apiInstance.metadataListJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#metadataListJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;MetadataListResponseInner&gt;**](MetadataListResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="metadataUpdateJsonPost"></a>
# **metadataUpdateJsonPost**
> MetadataInfo metadataUpdateJsonPost(body)



Update an existing custom metadata field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MetadataTemplate body = new MetadataTemplate(); // MetadataTemplate | 
    try {
      MetadataInfo result = apiInstance.metadataUpdateJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#metadataUpdateJsonPost");
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
| **body** | [**MetadataTemplate**](MetadataTemplate.md)|  | |

### Return type

[**MetadataInfo**](MetadataInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="rejectsAddJsonPost"></a>
# **rejectsAddJsonPost**
> RejectsAddResponse rejectsAddJsonPost(body)



Adds an email to your email rejection blacklist. Addresses that you add manually will never expire and there is no reputation penalty for removing them from your blacklist. Attempting to blacklist an address that has been whitelisted will have no effect.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    RejectsAdd body = new RejectsAdd(); // RejectsAdd | 
    try {
      RejectsAddResponse result = apiInstance.rejectsAddJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rejectsAddJsonPost");
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
| **body** | [**RejectsAdd**](RejectsAdd.md)|  | |

### Return type

[**RejectsAddResponse**](RejectsAddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="rejectsDeleteJsonPost"></a>
# **rejectsDeleteJsonPost**
> RejectsDeleteResponse rejectsDeleteJsonPost(body)



Deletes an email rejection. There is no limit to how many rejections you can remove from your blacklist, but keep in mind that each deletion has an affect on your reputation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    RejectsDelete body = new RejectsDelete(); // RejectsDelete | 
    try {
      RejectsDeleteResponse result = apiInstance.rejectsDeleteJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rejectsDeleteJsonPost");
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
| **body** | [**RejectsDelete**](RejectsDelete.md)|  | |

### Return type

[**RejectsDeleteResponse**](RejectsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="rejectsListJsonPost"></a>
# **rejectsListJsonPost**
> List&lt;RejectsListResponseInner&gt; rejectsListJsonPost(body)



Retrieves your email rejection blacklist. You can provide an email address to limit the results. Returns up to 1000 results. By default, entries that have expired are excluded from the results; set include_expired to true to include them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    RejectsList body = new RejectsList(); // RejectsList | 
    try {
      List<RejectsListResponseInner> result = apiInstance.rejectsListJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rejectsListJsonPost");
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
| **body** | [**RejectsList**](RejectsList.md)|  | |

### Return type

[**List&lt;RejectsListResponseInner&gt;**](RejectsListResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sendersAddDomainJsonPost"></a>
# **sendersAddDomainJsonPost**
> SenderDomainInfo sendersAddDomainJsonPost(body)



Adds a sender domain to your account. Sender domains are added automatically as you send, but you can use this call to add them ahead of time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Domain body = new Domain(); // Domain | 
    try {
      SenderDomainInfo result = apiInstance.sendersAddDomainJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendersAddDomainJsonPost");
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
| **body** | [**Domain**](Domain.md)|  | |

### Return type

[**SenderDomainInfo**](SenderDomainInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sendersCheckDomainJsonPost"></a>
# **sendersCheckDomainJsonPost**
> SenderDomainInfo sendersCheckDomainJsonPost(body)



Checks the SPF and DKIM settings for a domain. If you haven&#39;t already added this domain to your account, it will be added automatically.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Domain body = new Domain(); // Domain | 
    try {
      SenderDomainInfo result = apiInstance.sendersCheckDomainJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendersCheckDomainJsonPost");
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
| **body** | [**Domain**](Domain.md)|  | |

### Return type

[**SenderDomainInfo**](SenderDomainInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sendersDomainsJsonPost"></a>
# **sendersDomainsJsonPost**
> List&lt;SendersDomainsResponseInner&gt; sendersDomainsJsonPost(body)



Returns the sender domains that have been added to this account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<SendersDomainsResponseInner> result = apiInstance.sendersDomainsJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendersDomainsJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;SendersDomainsResponseInner&gt;**](SendersDomainsResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sendersInfoJsonPost"></a>
# **sendersInfoJsonPost**
> SendersInfoResponse sendersInfoJsonPost(body)



Return more detailed information about a single sender, including aggregates of recent stats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SenderAddress body = new SenderAddress(); // SenderAddress | 
    try {
      SendersInfoResponse result = apiInstance.sendersInfoJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendersInfoJsonPost");
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
| **body** | [**SenderAddress**](SenderAddress.md)|  | |

### Return type

[**SendersInfoResponse**](SendersInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sendersListJsonPost"></a>
# **sendersListJsonPost**
> List&lt;RejectsListResponseInnerSender&gt; sendersListJsonPost(body)



Return the senders that have tried to use this account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<RejectsListResponseInnerSender> result = apiInstance.sendersListJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendersListJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;RejectsListResponseInnerSender&gt;**](RejectsListResponseInnerSender.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sendersTimeSeriesJsonPost"></a>
# **sendersTimeSeriesJsonPost**
> List&lt;TimeSeriesInner&gt; sendersTimeSeriesJsonPost(body)



Return the recent history (hourly stats for the last 30 days) for a sender

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SenderAddress body = new SenderAddress(); // SenderAddress | 
    try {
      List<TimeSeriesInner> result = apiInstance.sendersTimeSeriesJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendersTimeSeriesJsonPost");
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
| **body** | [**SenderAddress**](SenderAddress.md)|  | |

### Return type

[**List&lt;TimeSeriesInner&gt;**](TimeSeriesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sendersVerifyDomainJsonPost"></a>
# **sendersVerifyDomainJsonPost**
> SendersVerifyDomainResponse sendersVerifyDomainJsonPost(body)



Sends a verification email in order to verify ownership of a domain. Domain verification is an optional step to confirm ownership of a domain. Once a domain has been verified in a Mandrill account, other accounts may not have their messages signed by that domain unless they also verify the domain. This prevents other Mandrill accounts from sending mail signed by your domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SendersVerifyDomain body = new SendersVerifyDomain(); // SendersVerifyDomain | 
    try {
      SendersVerifyDomainResponse result = apiInstance.sendersVerifyDomainJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendersVerifyDomainJsonPost");
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
| **body** | [**SendersVerifyDomain**](SendersVerifyDomain.md)|  | |

### Return type

[**SendersVerifyDomainResponse**](SendersVerifyDomainResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="subaccountsAddJsonPost"></a>
# **subaccountsAddJsonPost**
> SubaccountInfo2 subaccountsAddJsonPost(body)



Add a new subaccount

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SubaccountInfo body = new SubaccountInfo(); // SubaccountInfo | 
    try {
      SubaccountInfo2 result = apiInstance.subaccountsAddJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subaccountsAddJsonPost");
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
| **body** | [**SubaccountInfo**](SubaccountInfo.md)|  | |

### Return type

[**SubaccountInfo2**](SubaccountInfo2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="subaccountsDeleteJsonPost"></a>
# **subaccountsDeleteJsonPost**
> SubaccountInfo2 subaccountsDeleteJsonPost(body)



Delete an existing subaccount. Any email related to the subaccount will be saved, but stats will be removed and any future sending calls to this subaccount will fail.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Id body = new Id(); // Id | 
    try {
      SubaccountInfo2 result = apiInstance.subaccountsDeleteJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subaccountsDeleteJsonPost");
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
| **body** | [**Id**](Id.md)|  | |

### Return type

[**SubaccountInfo2**](SubaccountInfo2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="subaccountsInfoJsonPost"></a>
# **subaccountsInfoJsonPost**
> SubaccountsInfoResponse subaccountsInfoJsonPost(body)



Given the ID of an existing subaccount, return the data about it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Id body = new Id(); // Id | 
    try {
      SubaccountsInfoResponse result = apiInstance.subaccountsInfoJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subaccountsInfoJsonPost");
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
| **body** | [**Id**](Id.md)|  | |

### Return type

[**SubaccountsInfoResponse**](SubaccountsInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="subaccountsListJsonPost"></a>
# **subaccountsListJsonPost**
> List&lt;SubaccountsListResponseInner&gt; subaccountsListJsonPost(body)



Get the list of subaccounts defined for the account, optionally filtered by a prefix

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UrlKey body = new UrlKey(); // UrlKey | 
    try {
      List<SubaccountsListResponseInner> result = apiInstance.subaccountsListJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subaccountsListJsonPost");
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
| **body** | [**UrlKey**](UrlKey.md)|  | |

### Return type

[**List&lt;SubaccountsListResponseInner&gt;**](SubaccountsListResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="subaccountsPauseJsonPost"></a>
# **subaccountsPauseJsonPost**
> SubaccountInfo2 subaccountsPauseJsonPost(body)



Pause a subaccount&#39;s sending. Any future emails delivered to this subaccount will be queued for a maximum of 3 days until the subaccount is resumed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Id body = new Id(); // Id | 
    try {
      SubaccountInfo2 result = apiInstance.subaccountsPauseJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subaccountsPauseJsonPost");
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
| **body** | [**Id**](Id.md)|  | |

### Return type

[**SubaccountInfo2**](SubaccountInfo2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="subaccountsResumeJsonPost"></a>
# **subaccountsResumeJsonPost**
> SubaccountInfo2 subaccountsResumeJsonPost(body)



Resume a paused subaccount&#39;s sending

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Id body = new Id(); // Id | 
    try {
      SubaccountInfo2 result = apiInstance.subaccountsResumeJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subaccountsResumeJsonPost");
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
| **body** | [**Id**](Id.md)|  | |

### Return type

[**SubaccountInfo2**](SubaccountInfo2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="subaccountsUpdateJsonPost"></a>
# **subaccountsUpdateJsonPost**
> SubaccountInfo2 subaccountsUpdateJsonPost(body)



Update an existing subaccount

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SubaccountInfo body = new SubaccountInfo(); // SubaccountInfo | 
    try {
      SubaccountInfo2 result = apiInstance.subaccountsUpdateJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subaccountsUpdateJsonPost");
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
| **body** | [**SubaccountInfo**](SubaccountInfo.md)|  | |

### Return type

[**SubaccountInfo2**](SubaccountInfo2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tagsAllTimeSeriesJsonPost"></a>
# **tagsAllTimeSeriesJsonPost**
> List&lt;TimeseriesInner&gt; tagsAllTimeSeriesJsonPost(body)



Return the recent history (hourly stats for the last 30 days) for all tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<TimeseriesInner> result = apiInstance.tagsAllTimeSeriesJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagsAllTimeSeriesJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;TimeseriesInner&gt;**](TimeseriesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tagsDeleteJsonPost"></a>
# **tagsDeleteJsonPost**
> TagsDeleteResponse tagsDeleteJsonPost(body)



Deletes a tag permanently. Deleting a tag removes the tag from any messages that have been sent, and also deletes the tag&#39;s stats. There is no way to undo this operation, so use it carefully.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    TagKey body = new TagKey(); // TagKey | 
    try {
      TagsDeleteResponse result = apiInstance.tagsDeleteJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagsDeleteJsonPost");
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
| **body** | [**TagKey**](TagKey.md)|  | |

### Return type

[**TagsDeleteResponse**](TagsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tagsInfoJsonPost"></a>
# **tagsInfoJsonPost**
> TagsInfoResponse tagsInfoJsonPost(body)



Return more detailed information about a single tag, including aggregates of recent stats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    TagKey body = new TagKey(); // TagKey | 
    try {
      TagsInfoResponse result = apiInstance.tagsInfoJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagsInfoJsonPost");
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
| **body** | [**TagKey**](TagKey.md)|  | |

### Return type

[**TagsInfoResponse**](TagsInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tagsListJsonPost"></a>
# **tagsListJsonPost**
> List&lt;TagsListResponseInner&gt; tagsListJsonPost(body)



Return all of the user-defined tag information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<TagsListResponseInner> result = apiInstance.tagsListJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagsListJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;TagsListResponseInner&gt;**](TagsListResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="tagsTimeSeriesJsonPost"></a>
# **tagsTimeSeriesJsonPost**
> List&lt;TimeseriesInner&gt; tagsTimeSeriesJsonPost(body)



Return the recent history (hourly stats for the last 30 days) for a tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    TagKey body = new TagKey(); // TagKey | 
    try {
      List<TimeseriesInner> result = apiInstance.tagsTimeSeriesJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagsTimeSeriesJsonPost");
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
| **body** | [**TagKey**](TagKey.md)|  | |

### Return type

[**List&lt;TimeseriesInner&gt;**](TimeseriesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="templatesAddJsonPost"></a>
# **templatesAddJsonPost**
> TemplateDetailed templatesAddJsonPost(body)



Add a new template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Template body = new Template(); // Template | 
    try {
      TemplateDetailed result = apiInstance.templatesAddJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#templatesAddJsonPost");
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
| **body** | [**Template**](Template.md)|  | |

### Return type

[**TemplateDetailed**](TemplateDetailed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="templatesDeleteJsonPost"></a>
# **templatesDeleteJsonPost**
> TemplateDetailed templatesDeleteJsonPost(body)



Delete a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Name body = new Name(); // Name | 
    try {
      TemplateDetailed result = apiInstance.templatesDeleteJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#templatesDeleteJsonPost");
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
| **body** | [**Name**](Name.md)|  | |

### Return type

[**TemplateDetailed**](TemplateDetailed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="templatesInfoJsonPost"></a>
# **templatesInfoJsonPost**
> TemplateDetailed templatesInfoJsonPost(body)



Get the information for an existing template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Name body = new Name(); // Name | 
    try {
      TemplateDetailed result = apiInstance.templatesInfoJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#templatesInfoJsonPost");
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
| **body** | [**Name**](Name.md)|  | |

### Return type

[**TemplateDetailed**](TemplateDetailed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="templatesListJsonPost"></a>
# **templatesListJsonPost**
> List&lt;TemplatesListResponseInner&gt; templatesListJsonPost(body)



Return a list of all the templates available to this user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    TemplatesList body = new TemplatesList(); // TemplatesList | 
    try {
      List<TemplatesListResponseInner> result = apiInstance.templatesListJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#templatesListJsonPost");
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
| **body** | [**TemplatesList**](TemplatesList.md)|  | |

### Return type

[**List&lt;TemplatesListResponseInner&gt;**](TemplatesListResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="templatesPublishJsonPost"></a>
# **templatesPublishJsonPost**
> TemplateDetailed templatesPublishJsonPost(body)



Publish the content for the template. Any new messages sent using this template will start using the content that was previously in draft.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Name body = new Name(); // Name | 
    try {
      TemplateDetailed result = apiInstance.templatesPublishJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#templatesPublishJsonPost");
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
| **body** | [**Name**](Name.md)|  | |

### Return type

[**TemplateDetailed**](TemplateDetailed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="templatesRenderJsonPost"></a>
# **templatesRenderJsonPost**
> TemplatesRenderResponse templatesRenderJsonPost(body)



Inject content and optionally merge fields into a template, returning the HTML that results

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    TemplatesRender body = new TemplatesRender(); // TemplatesRender | 
    try {
      TemplatesRenderResponse result = apiInstance.templatesRenderJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#templatesRenderJsonPost");
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
| **body** | [**TemplatesRender**](TemplatesRender.md)|  | |

### Return type

[**TemplatesRenderResponse**](TemplatesRenderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="templatesTimeSeriesJsonPost"></a>
# **templatesTimeSeriesJsonPost**
> List&lt;TimeSeriesInner&gt; templatesTimeSeriesJsonPost(body)



Return the recent history (hourly stats for the last 30 days) for a template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Name body = new Name(); // Name | 
    try {
      List<TimeSeriesInner> result = apiInstance.templatesTimeSeriesJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#templatesTimeSeriesJsonPost");
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
| **body** | [**Name**](Name.md)|  | |

### Return type

[**List&lt;TimeSeriesInner&gt;**](TimeSeriesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="templatesUpdateJsonPost"></a>
# **templatesUpdateJsonPost**
> TemplateDetailed templatesUpdateJsonPost(body)



Update the code for an existing template. If null is provided for any fields, the values will remain unchanged.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Template body = new Template(); // Template | 
    try {
      TemplateDetailed result = apiInstance.templatesUpdateJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#templatesUpdateJsonPost");
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
| **body** | [**Template**](Template.md)|  | |

### Return type

[**TemplateDetailed**](TemplateDetailed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="urlsAddTrackingDomainJsonPost"></a>
# **urlsAddTrackingDomainJsonPost**
> TrackingDomainStatus urlsAddTrackingDomainJsonPost(body)



Add a tracking domain to your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Domain body = new Domain(); // Domain | 
    try {
      TrackingDomainStatus result = apiInstance.urlsAddTrackingDomainJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#urlsAddTrackingDomainJsonPost");
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
| **body** | [**Domain**](Domain.md)|  | |

### Return type

[**TrackingDomainStatus**](TrackingDomainStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="urlsCheckTrackingDomainJsonPost"></a>
# **urlsCheckTrackingDomainJsonPost**
> TrackingDomainStatus urlsCheckTrackingDomainJsonPost(body)



Checks the CNAME settings for a tracking domain. The domain must have been added already with the add-tracking-domain call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Domain body = new Domain(); // Domain | 
    try {
      TrackingDomainStatus result = apiInstance.urlsCheckTrackingDomainJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#urlsCheckTrackingDomainJsonPost");
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
| **body** | [**Domain**](Domain.md)|  | |

### Return type

[**TrackingDomainStatus**](TrackingDomainStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="urlsListJsonPost"></a>
# **urlsListJsonPost**
> List&lt;UrlInfosInner&gt; urlsListJsonPost(body)



Get the 100 most clicked URLs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<UrlInfosInner> result = apiInstance.urlsListJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#urlsListJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;UrlInfosInner&gt;**](UrlInfosInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="urlsSearchJsonPost"></a>
# **urlsSearchJsonPost**
> List&lt;UrlInfosInner&gt; urlsSearchJsonPost(body)



Return the 100 most clicked URLs that match the search query given

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UrlKey body = new UrlKey(); // UrlKey | 
    try {
      List<UrlInfosInner> result = apiInstance.urlsSearchJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#urlsSearchJsonPost");
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
| **body** | [**UrlKey**](UrlKey.md)|  | |

### Return type

[**List&lt;UrlInfosInner&gt;**](UrlInfosInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="urlsTimeSeriesJsonPost"></a>
# **urlsTimeSeriesJsonPost**
> List&lt;UrlsTimeSeriesResponseInner&gt; urlsTimeSeriesJsonPost(body)



Return the recent history (hourly stats for the last 30 days) for a url

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UrlsTimeSeries body = new UrlsTimeSeries(); // UrlsTimeSeries | 
    try {
      List<UrlsTimeSeriesResponseInner> result = apiInstance.urlsTimeSeriesJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#urlsTimeSeriesJsonPost");
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
| **body** | [**UrlsTimeSeries**](UrlsTimeSeries.md)|  | |

### Return type

[**List&lt;UrlsTimeSeriesResponseInner&gt;**](UrlsTimeSeriesResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="urlsTrackingDomainsJsonPost"></a>
# **urlsTrackingDomainsJsonPost**
> List&lt;UrlsTrackingDomainsResponseInner&gt; urlsTrackingDomainsJsonPost(body)



Get the list of tracking domains set up for this account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<UrlsTrackingDomainsResponseInner> result = apiInstance.urlsTrackingDomainsJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#urlsTrackingDomainsJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;UrlsTrackingDomainsResponseInner&gt;**](UrlsTrackingDomainsResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersInfoJsonPost"></a>
# **usersInfoJsonPost**
> UsersInfoResponse usersInfoJsonPost(body)



Return the information about the API-connected user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      UsersInfoResponse result = apiInstance.usersInfoJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#usersInfoJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**UsersInfoResponse**](UsersInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersPing2JsonPost"></a>
# **usersPing2JsonPost**
> UsersPing2Response usersPing2JsonPost(body)



Validate an API key and respond to a ping (anal JSON parser version)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      UsersPing2Response result = apiInstance.usersPing2JsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#usersPing2JsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**UsersPing2Response**](UsersPing2Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersPingJsonPost"></a>
# **usersPingJsonPost**
> usersPingJsonPost(body)



Validate an API key and respond to a ping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      apiInstance.usersPingJsonPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#usersPingJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersSendersJsonPost"></a>
# **usersSendersJsonPost**
> List&lt;RejectsListResponseInnerSender&gt; usersSendersJsonPost(body)



Return the senders that have tried to use this account, both verified and unverified

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<RejectsListResponseInnerSender> result = apiInstance.usersSendersJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#usersSendersJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;RejectsListResponseInnerSender&gt;**](RejectsListResponseInnerSender.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webhooksAddJsonPost"></a>
# **webhooksAddJsonPost**
> Webhook webhooksAddJsonPost(body)



Add a new webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    WebhooksAdd body = new WebhooksAdd(); // WebhooksAdd | 
    try {
      Webhook result = apiInstance.webhooksAddJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#webhooksAddJsonPost");
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
| **body** | [**WebhooksAdd**](WebhooksAdd.md)|  | |

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webhooksDeleteJsonPost"></a>
# **webhooksDeleteJsonPost**
> Webhook webhooksDeleteJsonPost(body)



Delete an existing webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    WebhookKey body = new WebhookKey(); // WebhookKey | 
    try {
      Webhook result = apiInstance.webhooksDeleteJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#webhooksDeleteJsonPost");
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
| **body** | [**WebhookKey**](WebhookKey.md)|  | |

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webhooksInfoJsonPost"></a>
# **webhooksInfoJsonPost**
> Webhook webhooksInfoJsonPost(body)



Given the ID of an existing webhook, return the data about it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    WebhookKey body = new WebhookKey(); // WebhookKey | 
    try {
      Webhook result = apiInstance.webhooksInfoJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#webhooksInfoJsonPost");
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
| **body** | [**WebhookKey**](WebhookKey.md)|  | |

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webhooksListJsonPost"></a>
# **webhooksListJsonPost**
> List&lt;WebhooksListResponseInner&gt; webhooksListJsonPost(body)



Get the list of all webhooks defined on the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiKey body = new ApiKey(); // ApiKey | 
    try {
      List<WebhooksListResponseInner> result = apiInstance.webhooksListJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#webhooksListJsonPost");
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
| **body** | [**ApiKey**](ApiKey.md)|  | |

### Return type

[**List&lt;WebhooksListResponseInner&gt;**](WebhooksListResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webhooksUpdateJsonPost"></a>
# **webhooksUpdateJsonPost**
> Webhook webhooksUpdateJsonPost(body)



Update an existing webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    WebhooksUpdate body = new WebhooksUpdate(); // WebhooksUpdate | 
    try {
      Webhook result = apiInstance.webhooksUpdateJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#webhooksUpdateJsonPost");
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
| **body** | [**WebhooksUpdate**](WebhooksUpdate.md)|  | |

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="whitelistsAddJsonPost"></a>
# **whitelistsAddJsonPost**
> WhitelistsAddResponse whitelistsAddJsonPost(body)



Adds an email to your email rejection whitelist. If the address is currently on your blacklist, that blacklist entry will be removed automatically.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Email body = new Email(); // Email | 
    try {
      WhitelistsAddResponse result = apiInstance.whitelistsAddJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#whitelistsAddJsonPost");
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
| **body** | [**Email**](Email.md)|  | |

### Return type

[**WhitelistsAddResponse**](WhitelistsAddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="whitelistsDeleteJsonPost"></a>
# **whitelistsDeleteJsonPost**
> WhitelistsDeleteResponse whitelistsDeleteJsonPost(body)



Removes an email address from the whitelist.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Email body = new Email(); // Email | 
    try {
      WhitelistsDeleteResponse result = apiInstance.whitelistsDeleteJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#whitelistsDeleteJsonPost");
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
| **body** | [**Email**](Email.md)|  | |

### Return type

[**WhitelistsDeleteResponse**](WhitelistsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="whitelistsListJsonPost"></a>
# **whitelistsListJsonPost**
> List&lt;WhitelistsListResponseInner&gt; whitelistsListJsonPost(body)



Retrieves your email rejection whitelist. You can provide an email address or search prefix to limit the results. Returns up to 1000 results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mandrillapp.com/api/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Email body = new Email(); // Email | 
    try {
      List<WhitelistsListResponseInner> result = apiInstance.whitelistsListJsonPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#whitelistsListJsonPost");
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
| **body** | [**Email**](Email.md)|  | |

### Return type

[**List&lt;WhitelistsListResponseInner&gt;**](WhitelistsListResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

