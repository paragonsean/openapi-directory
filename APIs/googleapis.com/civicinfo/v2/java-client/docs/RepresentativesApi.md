# RepresentativesApi

All URIs are relative to *https://civicinfo.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**civicinfoRepresentativesRepresentativeInfoByAddress**](RepresentativesApi.md#civicinfoRepresentativesRepresentativeInfoByAddress) | **GET** /civicinfo/v2/representatives |  |
| [**civicinfoRepresentativesRepresentativeInfoByDivision**](RepresentativesApi.md#civicinfoRepresentativesRepresentativeInfoByDivision) | **GET** /civicinfo/v2/representatives/{ocdId} |  |


<a id="civicinfoRepresentativesRepresentativeInfoByAddress"></a>
# **civicinfoRepresentativesRepresentativeInfoByAddress**
> RepresentativeInfoResponse civicinfoRepresentativesRepresentativeInfoByAddress($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, address, includeOffices, levels, roles)



Looks up political geography and representative information for a single address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepresentativesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://civicinfo.googleapis.com");

    RepresentativesApi apiInstance = new RepresentativesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String address = "address_example"; // String | The address to look up. May only be specified if the field ocdId is not given in the URL
    Boolean includeOffices = true; // Boolean | Whether to return information about offices and officials. If false, only the top-level district information will be returned.
    List<String> levels = Arrays.asList(); // List<String> | A list of office levels to filter by. Only offices that serve at least one of these levels will be returned. Divisions that don't contain a matching office will not be returned.
    List<String> roles = Arrays.asList(); // List<String> | A list of office roles to filter by. Only offices fulfilling one of these roles will be returned. Divisions that don't contain a matching office will not be returned.
    try {
      RepresentativeInfoResponse result = apiInstance.civicinfoRepresentativesRepresentativeInfoByAddress($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, address, includeOffices, levels, roles);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepresentativesApi#civicinfoRepresentativesRepresentativeInfoByAddress");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **address** | **String**| The address to look up. May only be specified if the field ocdId is not given in the URL | [optional] |
| **includeOffices** | **Boolean**| Whether to return information about offices and officials. If false, only the top-level district information will be returned. | [optional] |
| **levels** | [**List&lt;String&gt;**](String.md)| A list of office levels to filter by. Only offices that serve at least one of these levels will be returned. Divisions that don&#39;t contain a matching office will not be returned. | [optional] [enum: international, country, administrativeArea1, regional, administrativeArea2, locality, subLocality1, subLocality2, special] |
| **roles** | [**List&lt;String&gt;**](String.md)| A list of office roles to filter by. Only offices fulfilling one of these roles will be returned. Divisions that don&#39;t contain a matching office will not be returned. | [optional] [enum: headOfState, headOfGovernment, deputyHeadOfGovernment, governmentOfficer, executiveCouncil, legislatorUpperBody, legislatorLowerBody, highestCourtJudge, judge, schoolBoard, specialPurposeOfficer, otherRole] |

### Return type

[**RepresentativeInfoResponse**](RepresentativeInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="civicinfoRepresentativesRepresentativeInfoByDivision"></a>
# **civicinfoRepresentativesRepresentativeInfoByDivision**
> RepresentativeInfoData civicinfoRepresentativesRepresentativeInfoByDivision(ocdId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, levels, recursive, roles)



Looks up representative information for a single geographic division.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepresentativesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://civicinfo.googleapis.com");

    RepresentativesApi apiInstance = new RepresentativesApi(defaultClient);
    String ocdId = "ocdId_example"; // String | The Open Civic Data division identifier of the division to look up.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    List<String> levels = Arrays.asList(); // List<String> | A list of office levels to filter by. Only offices that serve at least one of these levels will be returned. Divisions that don't contain a matching office will not be returned.
    Boolean recursive = true; // Boolean | If true, information about all divisions contained in the division requested will be included as well. For example, if querying ocd-division/country:us/district:dc, this would also return all DC's wards and ANCs.
    List<String> roles = Arrays.asList(); // List<String> | A list of office roles to filter by. Only offices fulfilling one of these roles will be returned. Divisions that don't contain a matching office will not be returned.
    try {
      RepresentativeInfoData result = apiInstance.civicinfoRepresentativesRepresentativeInfoByDivision(ocdId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, levels, recursive, roles);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepresentativesApi#civicinfoRepresentativesRepresentativeInfoByDivision");
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
| **ocdId** | **String**| The Open Civic Data division identifier of the division to look up. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **levels** | [**List&lt;String&gt;**](String.md)| A list of office levels to filter by. Only offices that serve at least one of these levels will be returned. Divisions that don&#39;t contain a matching office will not be returned. | [optional] [enum: international, country, administrativeArea1, regional, administrativeArea2, locality, subLocality1, subLocality2, special] |
| **recursive** | **Boolean**| If true, information about all divisions contained in the division requested will be included as well. For example, if querying ocd-division/country:us/district:dc, this would also return all DC&#39;s wards and ANCs. | [optional] |
| **roles** | [**List&lt;String&gt;**](String.md)| A list of office roles to filter by. Only offices fulfilling one of these roles will be returned. Divisions that don&#39;t contain a matching office will not be returned. | [optional] [enum: headOfState, headOfGovernment, deputyHeadOfGovernment, governmentOfficer, executiveCouncil, legislatorUpperBody, legislatorLowerBody, highestCourtJudge, judge, schoolBoard, specialPurposeOfficer, otherRole] |

### Return type

[**RepresentativeInfoData**](RepresentativeInfoData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

