# BehaviorApi

All URIs are relative to *https://api.truora.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportBehavior**](BehaviorApi.md#reportBehavior) | **POST** /v1/behavior | Report Behavior |


<a id="reportBehavior"></a>
# **reportBehavior**
> BehaviourOutput reportBehavior(birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason, phoneNumber)

Report Behavior

Creates a behavior item to report employee conducts that do not or might not be included in their background check. This report includes both possitive and negative behaviors and sorts them by severity.  ### Reasons to report a person  &lt;table&gt;   &lt;tr&gt;     &lt;td style&#x3D;\&quot;width: 100px\&quot;&gt;&lt;center&gt;&lt;b&gt;Very High&lt;/b&gt;&lt;br&gt;(Score: 1)&lt;/td&gt;     &lt;td&gt;Rape, Drug Dealing, Sexual Harassment&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;High&lt;/b&gt;&lt;br&gt;(Score: 0.8)&lt;/td&gt;     &lt;td&gt;Theft, Fights, Aggressive Behaviour, Identity Fraud, Drunk, Drug Possession&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Medium&lt;/b&gt;&lt;br&gt;(Score: 0.6)&lt;/td&gt;     &lt;td&gt;Absences&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Low&lt;/b&gt;&lt;br&gt;(Score: 0.4)&lt;/td&gt;     &lt;td&gt;Tardiness, Confidentiality Breach&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;None&lt;/b&gt;&lt;br&gt;(Score: 0)&lt;/td&gt;     &lt;td&gt;Good Reputation&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Unknown&lt;/b&gt;&lt;/td&gt;     &lt;td&gt;No information&lt;/td&gt;   &lt;/tr&gt; &lt;/table&gt;  **NOTE:** If the reason of your report is not here, please contact Truora support team. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BehaviorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    BehaviorApi apiInstance = new BehaviorApi(defaultClient);
    OffsetDateTime birthDate = OffsetDateTime.now(); // OffsetDateTime | Birth date of reported person
    String country = "co"; // String | Document country
    String documentId = "documentId_example"; // String | Person document ID
    String documentType = "national-id"; // String | Document type associated with the background check
    String email = "email_example"; // String | Reported person e-mail
    OffsetDateTime feedbackDate = OffsetDateTime.now(); // OffsetDateTime | Behavior report date
    String firstName = "firstName_example"; // String | Person first name
    String lastName = "lastName_example"; // String | Person last name
    String reason = "rape"; // String | Report reason
    String phoneNumber = "phoneNumber_example"; // String | Phone number of the reported person
    try {
      BehaviourOutput result = apiInstance.reportBehavior(birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason, phoneNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BehaviorApi#reportBehavior");
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
| **birthDate** | **OffsetDateTime**| Birth date of reported person | |
| **country** | **String**| Document country | [enum: co, ve, cl, mx, pe, do, sv, gt, bo, cr, ec, pa, br] |
| **documentId** | **String**| Person document ID | |
| **documentType** | **String**| Document type associated with the background check | [enum: national-id, passport, foreign-id, nit, diplomatic-id, civil-registration, identity-card, foreigner-card, professional-card, military-card, pep, nis, dni, rui, license-plate, query, name, rut, nuip, foreign-societies, escrow, individual-registration, general-registration, curp, dui, driver-license, ruc] |
| **email** | **String**| Reported person e-mail | |
| **feedbackDate** | **OffsetDateTime**| Behavior report date | |
| **firstName** | **String**| Person first name | |
| **lastName** | **String**| Person last name | |
| **reason** | **String**| Report reason | [enum: rape, drug-dealer, sexual-harassment, theft, fights, aggressive-behaviour, identity-fraud, drunk, drug-possession, absences, tardiness, confidentiality-breach, good-reputation] |
| **phoneNumber** | **String**| Phone number of the reported person | [optional] |

### Return type

[**BehaviourOutput**](BehaviourOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |
| **400** | Error uploading the items |  -  |

