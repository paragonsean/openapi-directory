# FundManagementApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postACCOUNTFUNDSBELOWTHRESHOLD**](FundManagementApi.md#postACCOUNTFUNDSBELOWTHRESHOLD) | **POST** /ACCOUNT_FUNDS_BELOW_THRESHOLD | Liable account&#39;s funds are below configured threshold |
| [**postACCOUNTHOLDERPAYOUT**](FundManagementApi.md#postACCOUNTHOLDERPAYOUT) | **POST** /ACCOUNT_HOLDER_PAYOUT | Paid out to account holder |
| [**postBENEFICIARYSETUP**](FundManagementApi.md#postBENEFICIARYSETUP) | **POST** /BENEFICIARY_SETUP | Beneficiary defined |
| [**postCOMPENSATENEGATIVEBALANCE**](FundManagementApi.md#postCOMPENSATENEGATIVEBALANCE) | **POST** /COMPENSATE_NEGATIVE_BALANCE | Negative account balances compensated |
| [**postDIRECTDEBITINITIATED**](FundManagementApi.md#postDIRECTDEBITINITIATED) | **POST** /DIRECT_DEBIT_INITIATED | Automated direct debit initiated |
| [**postREFUNDFUNDSTRANSFER**](FundManagementApi.md#postREFUNDFUNDSTRANSFER) | **POST** /REFUND_FUNDS_TRANSFER | Funds transfer between accounts refunded |
| [**postSCHEDULEDREFUNDS**](FundManagementApi.md#postSCHEDULEDREFUNDS) | **POST** /SCHEDULED_REFUNDS | &#39;Refund Transfers Not Paid Out&#39; call processed and refunds scheduled |
| [**postTRANSFERFUNDS**](FundManagementApi.md#postTRANSFERFUNDS) | **POST** /TRANSFER_FUNDS | Funds transferred between accounts |


<a id="postACCOUNTFUNDSBELOWTHRESHOLD"></a>
# **postACCOUNTFUNDSBELOWTHRESHOLD**
> NotificationResponse postACCOUNTFUNDSBELOWTHRESHOLD(accountFundsBelowThresholdNotification)

Liable account&#39;s funds are below configured threshold

Adyen sends this notification when the current funds of your liable account are below the configured threshold.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    FundManagementApi apiInstance = new FundManagementApi(defaultClient);
    AccountFundsBelowThresholdNotification accountFundsBelowThresholdNotification = new AccountFundsBelowThresholdNotification(); // AccountFundsBelowThresholdNotification | 
    try {
      NotificationResponse result = apiInstance.postACCOUNTFUNDSBELOWTHRESHOLD(accountFundsBelowThresholdNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundManagementApi#postACCOUNTFUNDSBELOWTHRESHOLD");
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
| **accountFundsBelowThresholdNotification** | [**AccountFundsBelowThresholdNotification**](AccountFundsBelowThresholdNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postACCOUNTHOLDERPAYOUT"></a>
# **postACCOUNTHOLDERPAYOUT**
> NotificationResponse postACCOUNTHOLDERPAYOUT(accountHolderPayoutNotification)

Paid out to account holder

Adyen sends this notification when a [payout request](https://docs.adyen.com/api-explorer/#/Fund/latest/post/payoutAccountHolder) to an account holder is processed and the payout is scheduled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    FundManagementApi apiInstance = new FundManagementApi(defaultClient);
    AccountHolderPayoutNotification accountHolderPayoutNotification = new AccountHolderPayoutNotification(); // AccountHolderPayoutNotification | 
    try {
      NotificationResponse result = apiInstance.postACCOUNTHOLDERPAYOUT(accountHolderPayoutNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundManagementApi#postACCOUNTHOLDERPAYOUT");
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
| **accountHolderPayoutNotification** | [**AccountHolderPayoutNotification**](AccountHolderPayoutNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postBENEFICIARYSETUP"></a>
# **postBENEFICIARYSETUP**
> NotificationResponse postBENEFICIARYSETUP(beneficiarySetupNotification)

Beneficiary defined

Adyen sends this notification when a [benefactor/beneficiary relationship is created](https://docs.adyen.com/api-explorer/#/Fund/latest/post/transferFunds).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    FundManagementApi apiInstance = new FundManagementApi(defaultClient);
    BeneficiarySetupNotification beneficiarySetupNotification = new BeneficiarySetupNotification(); // BeneficiarySetupNotification | 
    try {
      NotificationResponse result = apiInstance.postBENEFICIARYSETUP(beneficiarySetupNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundManagementApi#postBENEFICIARYSETUP");
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
| **beneficiarySetupNotification** | [**BeneficiarySetupNotification**](BeneficiarySetupNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postCOMPENSATENEGATIVEBALANCE"></a>
# **postCOMPENSATENEGATIVEBALANCE**
> NotificationResponse postCOMPENSATENEGATIVEBALANCE(compensateNegativeBalanceNotification)

Negative account balances compensated

Adyen sends this notification when funds are transferred from your platform&#39;s liable account to an overdrawn account to compensate for the overdraft.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    FundManagementApi apiInstance = new FundManagementApi(defaultClient);
    CompensateNegativeBalanceNotification compensateNegativeBalanceNotification = new CompensateNegativeBalanceNotification(); // CompensateNegativeBalanceNotification | 
    try {
      NotificationResponse result = apiInstance.postCOMPENSATENEGATIVEBALANCE(compensateNegativeBalanceNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundManagementApi#postCOMPENSATENEGATIVEBALANCE");
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
| **compensateNegativeBalanceNotification** | [**CompensateNegativeBalanceNotification**](CompensateNegativeBalanceNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postDIRECTDEBITINITIATED"></a>
# **postDIRECTDEBITINITIATED**
> NotificationResponse postDIRECTDEBITINITIATED(directDebitInitiatedNotification)

Automated direct debit initiated

Adyen sends this notification when a [direct debit is initiated](https://docs.adyen.com/api-explorer/#/Fund/latest/post/debitAccountHolder).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    FundManagementApi apiInstance = new FundManagementApi(defaultClient);
    DirectDebitInitiatedNotification directDebitInitiatedNotification = new DirectDebitInitiatedNotification(); // DirectDebitInitiatedNotification | 
    try {
      NotificationResponse result = apiInstance.postDIRECTDEBITINITIATED(directDebitInitiatedNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundManagementApi#postDIRECTDEBITINITIATED");
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
| **directDebitInitiatedNotification** | [**DirectDebitInitiatedNotification**](DirectDebitInitiatedNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postREFUNDFUNDSTRANSFER"></a>
# **postREFUNDFUNDSTRANSFER**
> NotificationResponse postREFUNDFUNDSTRANSFER(refundFundsTransferNotification)

Funds transfer between accounts refunded

Adyen sends this notification when [funds transferred between accounts are refunded](https://docs.adyen.com/api-explorer/#/Fund/v6/latest/refundFundsTransfer).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    FundManagementApi apiInstance = new FundManagementApi(defaultClient);
    RefundFundsTransferNotification refundFundsTransferNotification = new RefundFundsTransferNotification(); // RefundFundsTransferNotification | 
    try {
      NotificationResponse result = apiInstance.postREFUNDFUNDSTRANSFER(refundFundsTransferNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundManagementApi#postREFUNDFUNDSTRANSFER");
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
| **refundFundsTransferNotification** | [**RefundFundsTransferNotification**](RefundFundsTransferNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postSCHEDULEDREFUNDS"></a>
# **postSCHEDULEDREFUNDS**
> NotificationResponse postSCHEDULEDREFUNDS(scheduledRefundsNotification)

&#39;Refund Transfers Not Paid Out&#39; call processed and refunds scheduled

Adyen sends this notification when a request to [refund transfers that are not yet paid out](https://docs.adyen.com/api-explorer/#/Fund/latest/refundNotPaidOutTransfers) is processed and the associated refunds are scheduled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    FundManagementApi apiInstance = new FundManagementApi(defaultClient);
    ScheduledRefundsNotification scheduledRefundsNotification = new ScheduledRefundsNotification(); // ScheduledRefundsNotification | 
    try {
      NotificationResponse result = apiInstance.postSCHEDULEDREFUNDS(scheduledRefundsNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundManagementApi#postSCHEDULEDREFUNDS");
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
| **scheduledRefundsNotification** | [**ScheduledRefundsNotification**](ScheduledRefundsNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postTRANSFERFUNDS"></a>
# **postTRANSFERFUNDS**
> NotificationResponse postTRANSFERFUNDS(transferFundsNotification)

Funds transferred between accounts

Adyen sends this notification when [funds are transferred between accounts](https://docs.adyen.com/api-explorer/#/Fund/latest/post/transferFunds).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    FundManagementApi apiInstance = new FundManagementApi(defaultClient);
    TransferFundsNotification transferFundsNotification = new TransferFundsNotification(); // TransferFundsNotification | 
    try {
      NotificationResponse result = apiInstance.postTRANSFERFUNDS(transferFundsNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundManagementApi#postTRANSFERFUNDS");
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
| **transferFundsNotification** | [**TransferFundsNotification**](TransferFundsNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

