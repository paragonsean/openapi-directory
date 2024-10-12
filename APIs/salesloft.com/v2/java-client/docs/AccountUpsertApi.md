# AccountUpsertApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2AccountUpsertsJsonPost**](AccountUpsertApi.md#v2AccountUpsertsJsonPost) | **POST** /v2/account_upserts.json | Upsert an account |


<a id="v2AccountUpsertsJsonPost"></a>
# **v2AccountUpsertsJsonPost**
> AccountUpsert v2AccountUpsertsJsonPost(domain, name, accountTierId, city, companyStageId, companyType, conversationalName, country, crmId, crmIdType, customFields, description, doNotContact, founded, id, industry, linkedinUrl, locale, ownerId, phone, postalCode, revenueRange, size, state, street, tags, twitterHandle, upsertKey, website)

Upsert an account

Upserts an account record. The upsert_key dictates how the upsert will be performed. The create and update behavior is exactly the same as the individual create and update endpoints. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountUpsertApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    AccountUpsertApi apiInstance = new AccountUpsertApi(defaultClient);
    String domain = "domain_example"; // String | Website domain, not a fully qualified URI
    String name = "name_example"; // String | Account Full Name
    Integer accountTierId = 56; // Integer | ID of the Account Tier for this Account
    String city = "city_example"; // String | City
    Integer companyStageId = 56; // Integer | ID of the CompanyStage assigned to this Account
    String companyType = "companyType_example"; // String | Type of the Account's company
    String conversationalName = "conversationalName_example"; // String | Conversational name of the Account
    String country = "country_example"; // String | Country
    String crmId = "crmId_example"; // String | Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\"salesforce\\\" ID must be exactly 18 characters. A \\\"salesforce\\\" ID must be either an Account (001) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\"account:set_crm_id\\\" scope.  
    String crmIdType = "crmIdType_example"; // String | The CRM that the provided crm_id is for. Must be one of: salesforce
    List<Object> customFields = null; // List<Object> | Custom fields are defined by the user's team. Only fields with values are presented in the API.
    String description = "description_example"; // String | Description
    Boolean doNotContact = true; // Boolean | Whether this company can not be contacted. Values are either true or false. Setting this to true will remove all associated people from all active communications
    String founded = "founded_example"; // String | Date or year of founding
    Integer id = 56; // Integer | ID of the account to update. Used if the upsert_key=id. When id and another upsert_key are provided, the request will fail if the upsert record id and id parameter don't match. 
    String industry = "industry_example"; // String | Industry
    String linkedinUrl = "linkedinUrl_example"; // String | Full LinkedIn url
    String locale = "locale_example"; // String | Time locale
    Integer ownerId = 56; // Integer | ID of the User that owns this Account
    String phone = "phone_example"; // String | Phone number without formatting
    String postalCode = "postalCode_example"; // String | Postal code
    String revenueRange = "revenueRange_example"; // String | Estimated revenue range
    String size = "size_example"; // String | Estimated number of people in employment
    String state = "state_example"; // String | State
    String street = "street_example"; // String | Street name and number
    List<String> tags = Arrays.asList(); // List<String> | All tags applied to this Account
    String twitterHandle = "twitterHandle_example"; // String | Twitter handle, with @
    String upsertKey = "upsertKey_example"; // String | Name of the parameter to upsert on. The field must be provided in the input parameters, or the request will fail. The request will also fail if there are multiple records matched by the upsert field.  If upsert_key is not provided, this endpoint will not update an existing record.  Valid options are: id, crm_id, domain. If crm_id is provided, then a valid crm_id_type must be provided, as documented for the account create and update endpoints. 
    String website = "website_example"; // String | Website
    try {
      AccountUpsert result = apiInstance.v2AccountUpsertsJsonPost(domain, name, accountTierId, city, companyStageId, companyType, conversationalName, country, crmId, crmIdType, customFields, description, doNotContact, founded, id, industry, linkedinUrl, locale, ownerId, phone, postalCode, revenueRange, size, state, street, tags, twitterHandle, upsertKey, website);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountUpsertApi#v2AccountUpsertsJsonPost");
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
| **domain** | **String**| Website domain, not a fully qualified URI | |
| **name** | **String**| Account Full Name | |
| **accountTierId** | **Integer**| ID of the Account Tier for this Account | [optional] |
| **city** | **String**| City | [optional] |
| **companyStageId** | **Integer**| ID of the CompanyStage assigned to this Account | [optional] |
| **companyType** | **String**| Type of the Account&#39;s company | [optional] |
| **conversationalName** | **String**| Conversational name of the Account | [optional] |
| **country** | **String**| Country | [optional] |
| **crmId** | **String**| Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\&quot;salesforce\\\&quot; ID must be exactly 18 characters. A \\\&quot;salesforce\\\&quot; ID must be either an Account (001) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\&quot;account:set_crm_id\\\&quot; scope.   | [optional] |
| **crmIdType** | **String**| The CRM that the provided crm_id is for. Must be one of: salesforce | [optional] |
| **customFields** | [**List&lt;Object&gt;**](Object.md)| Custom fields are defined by the user&#39;s team. Only fields with values are presented in the API. | [optional] |
| **description** | **String**| Description | [optional] |
| **doNotContact** | **Boolean**| Whether this company can not be contacted. Values are either true or false. Setting this to true will remove all associated people from all active communications | [optional] |
| **founded** | **String**| Date or year of founding | [optional] |
| **id** | **Integer**| ID of the account to update. Used if the upsert_key&#x3D;id. When id and another upsert_key are provided, the request will fail if the upsert record id and id parameter don&#39;t match.  | [optional] |
| **industry** | **String**| Industry | [optional] |
| **linkedinUrl** | **String**| Full LinkedIn url | [optional] |
| **locale** | **String**| Time locale | [optional] |
| **ownerId** | **Integer**| ID of the User that owns this Account | [optional] |
| **phone** | **String**| Phone number without formatting | [optional] |
| **postalCode** | **String**| Postal code | [optional] |
| **revenueRange** | **String**| Estimated revenue range | [optional] |
| **size** | **String**| Estimated number of people in employment | [optional] |
| **state** | **String**| State | [optional] |
| **street** | **String**| Street name and number | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| All tags applied to this Account | [optional] |
| **twitterHandle** | **String**| Twitter handle, with @ | [optional] |
| **upsertKey** | **String**| Name of the parameter to upsert on. The field must be provided in the input parameters, or the request will fail. The request will also fail if there are multiple records matched by the upsert field.  If upsert_key is not provided, this endpoint will not update an existing record.  Valid options are: id, crm_id, domain. If crm_id is provided, then a valid crm_id_type must be provided, as documented for the account create and update endpoints.  | [optional] |
| **website** | **String**| Website | [optional] |

### Return type

[**AccountUpsert**](AccountUpsert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

