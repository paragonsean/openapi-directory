# PersonUpsertApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2PersonUpsertsJsonPost**](PersonUpsertApi.md#v2PersonUpsertsJsonPost) | **POST** /v2/person_upserts.json | Upsert a person |


<a id="v2PersonUpsertsJsonPost"></a>
# **v2PersonUpsertsJsonPost**
> PersonUpsert v2PersonUpsertsJsonPost(accountId, city, contactRestrictions, country, crmId, crmIdType, customFields, doNotContact, emailAddress, firstName, homePhone, id, importId, jobSeniority, lastName, linkedinUrl, locale, mobilePhone, ownerId, personCompanyIndustry, personCompanyName, personCompanyWebsite, personStageId, personalEmailAddress, personalWebsite, phone, phoneExtension, secondaryEmailAddress, state, tags, title, twitterHandle, upsertKey, workCity, workCountry, workState)

Upsert a person

Upserts a person record. The upsert_key dictates how the upsert will be performed. The create and update behavior is exactly the same as the individual create and update endpoints. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonUpsertApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    PersonUpsertApi apiInstance = new PersonUpsertApi(defaultClient);
    Integer accountId = 56; // Integer | ID of the Account to link this person to
    String city = "city_example"; // String | City
    List<String> contactRestrictions = Arrays.asList(); // List<String> | Specific methods of communication to prevent for this person. This will prevent individual execution of these communication types as well as automatically skip cadence steps of this communication type for this person in SalesLoft. Values currently accepted: call, email, message
    String country = "country_example"; // String | Country
    String crmId = "crmId_example"; // String | Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\"salesforce\\\" ID must be exactly 18 characters. A \\\"salesforce\\\" ID must be either a Lead (00Q) or Contact (003) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\"person:set_crm_id\\\" scope.  
    String crmIdType = "crmIdType_example"; // String | The CRM that the provided crm_id is for. Must be one of: salesforce
    Object customFields = null; // Object | Custom fields are defined by the user's team. Only fields with values are presented in the API.
    Boolean doNotContact = true; // Boolean | Whether or not this person has opted out of all communication. Setting this value to true prevents this person from being called, emailed, or added to a cadence in SalesLoft. If this person is currently in a cadence, they will be removed.
    String emailAddress = "emailAddress_example"; // String | Email address
    String firstName = "firstName_example"; // String | First name
    String homePhone = "homePhone_example"; // String | Home phone without formatting
    Integer id = 56; // Integer | ID of the person to update. Used if the upsert_key=id. When id and another upsert_key are provided, the request will fail if the upsert record id and id parameter don't match. 
    Integer importId = 56; // Integer | ID of the Import this person is a part of. A person can be part of multiple imports, but this ID will always be the most recent Import
    String jobSeniority = "jobSeniority_example"; // String | The Job Seniority of a Person, must be one of director, executive, individual_contributor, manager, vice_president, unknown
    String lastName = "lastName_example"; // String | Last name
    String linkedinUrl = "linkedinUrl_example"; // String | Linkedin URL
    String locale = "locale_example"; // String | Time locale of the person
    String mobilePhone = "mobilePhone_example"; // String | Mobile phone without formatting
    Integer ownerId = 56; // Integer | ID of the User that owns this person
    String personCompanyIndustry = "personCompanyIndustry_example"; // String | Company industry. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
    String personCompanyName = "personCompanyName_example"; // String | Company name. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
    String personCompanyWebsite = "personCompanyWebsite_example"; // String | Company website. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
    Integer personStageId = 56; // Integer | ID of the PersonStage of this person
    String personalEmailAddress = "personalEmailAddress_example"; // String | Personal email address
    String personalWebsite = "personalWebsite_example"; // String | The website of this person
    String phone = "phone_example"; // String | Phone without formatting
    String phoneExtension = "phoneExtension_example"; // String | Phone extension without formatting
    String secondaryEmailAddress = "secondaryEmailAddress_example"; // String | Alternate email address
    String state = "state_example"; // String | State
    List<String> tags = Arrays.asList(); // List<String> | All tags applied to this person
    String title = "title_example"; // String | Job title
    String twitterHandle = "twitterHandle_example"; // String | The twitter handle of this person
    String upsertKey = "upsertKey_example"; // String | Name of the parameter to upsert on. The field must be provided in the input parameters, or the request will fail. The request will also fail if there are multiple records matched by the upsert field. This can occur if intentional duplicates by email address is enabled.  If upsert_key is not provided, this endpoint will not update an existing record.  Valid options are: id, crm_id, email_address. If crm_id is provided, then a valid crm_id_type must be provided, as documented for the person create and update endpoints. 
    String workCity = "workCity_example"; // String | Work location - city
    String workCountry = "workCountry_example"; // String | Work location - country
    String workState = "workState_example"; // String | Work location - state
    try {
      PersonUpsert result = apiInstance.v2PersonUpsertsJsonPost(accountId, city, contactRestrictions, country, crmId, crmIdType, customFields, doNotContact, emailAddress, firstName, homePhone, id, importId, jobSeniority, lastName, linkedinUrl, locale, mobilePhone, ownerId, personCompanyIndustry, personCompanyName, personCompanyWebsite, personStageId, personalEmailAddress, personalWebsite, phone, phoneExtension, secondaryEmailAddress, state, tags, title, twitterHandle, upsertKey, workCity, workCountry, workState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonUpsertApi#v2PersonUpsertsJsonPost");
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
| **accountId** | **Integer**| ID of the Account to link this person to | [optional] |
| **city** | **String**| City | [optional] |
| **contactRestrictions** | [**List&lt;String&gt;**](String.md)| Specific methods of communication to prevent for this person. This will prevent individual execution of these communication types as well as automatically skip cadence steps of this communication type for this person in SalesLoft. Values currently accepted: call, email, message | [optional] |
| **country** | **String**| Country | [optional] |
| **crmId** | **String**| Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\&quot;salesforce\\\&quot; ID must be exactly 18 characters. A \\\&quot;salesforce\\\&quot; ID must be either a Lead (00Q) or Contact (003) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\&quot;person:set_crm_id\\\&quot; scope.   | [optional] |
| **crmIdType** | **String**| The CRM that the provided crm_id is for. Must be one of: salesforce | [optional] |
| **customFields** | [**Object**](Object.md)| Custom fields are defined by the user&#39;s team. Only fields with values are presented in the API. | [optional] |
| **doNotContact** | **Boolean**| Whether or not this person has opted out of all communication. Setting this value to true prevents this person from being called, emailed, or added to a cadence in SalesLoft. If this person is currently in a cadence, they will be removed. | [optional] |
| **emailAddress** | **String**| Email address | [optional] |
| **firstName** | **String**| First name | [optional] |
| **homePhone** | **String**| Home phone without formatting | [optional] |
| **id** | **Integer**| ID of the person to update. Used if the upsert_key&#x3D;id. When id and another upsert_key are provided, the request will fail if the upsert record id and id parameter don&#39;t match.  | [optional] |
| **importId** | **Integer**| ID of the Import this person is a part of. A person can be part of multiple imports, but this ID will always be the most recent Import | [optional] |
| **jobSeniority** | **String**| The Job Seniority of a Person, must be one of director, executive, individual_contributor, manager, vice_president, unknown | [optional] |
| **lastName** | **String**| Last name | [optional] |
| **linkedinUrl** | **String**| Linkedin URL | [optional] |
| **locale** | **String**| Time locale of the person | [optional] |
| **mobilePhone** | **String**| Mobile phone without formatting | [optional] |
| **ownerId** | **Integer**| ID of the User that owns this person | [optional] |
| **personCompanyIndustry** | **String**| Company industry. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended | [optional] |
| **personCompanyName** | **String**| Company name. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended | [optional] |
| **personCompanyWebsite** | **String**| Company website. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended | [optional] |
| **personStageId** | **Integer**| ID of the PersonStage of this person | [optional] |
| **personalEmailAddress** | **String**| Personal email address | [optional] |
| **personalWebsite** | **String**| The website of this person | [optional] |
| **phone** | **String**| Phone without formatting | [optional] |
| **phoneExtension** | **String**| Phone extension without formatting | [optional] |
| **secondaryEmailAddress** | **String**| Alternate email address | [optional] |
| **state** | **String**| State | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| All tags applied to this person | [optional] |
| **title** | **String**| Job title | [optional] |
| **twitterHandle** | **String**| The twitter handle of this person | [optional] |
| **upsertKey** | **String**| Name of the parameter to upsert on. The field must be provided in the input parameters, or the request will fail. The request will also fail if there are multiple records matched by the upsert field. This can occur if intentional duplicates by email address is enabled.  If upsert_key is not provided, this endpoint will not update an existing record.  Valid options are: id, crm_id, email_address. If crm_id is provided, then a valid crm_id_type must be provided, as documented for the person create and update endpoints.  | [optional] |
| **workCity** | **String**| Work location - city | [optional] |
| **workCountry** | **String**| Work location - country | [optional] |
| **workState** | **String**| Work location - state | [optional] |

### Return type

[**PersonUpsert**](PersonUpsert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

