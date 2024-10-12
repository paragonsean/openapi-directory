# TypePropertySalesApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchPropertySales**](TypePropertySalesApi.md#searchPropertySales) | **GET** /repository/search/type/property_sales | Search API for &#39;Property Sales&#39; entry type |


<a id="searchPropertySales"></a>
# **searchPropertySales**
> searchPropertySales(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbPropertySalesPropertyAddress, searchDbPropertySalesCity, searchDbPropertySalesZipcode, searchDbPropertySalesSalePrice, searchDbPropertySalesSaleDate, searchDbPropertySalesSeller, searchDbPropertySalesBuyer, searchDbPropertySalesType, searchDbPropertySalesBuildingDescription, searchDbPropertySalesBuildingDesign, searchDbPropertySalesSubdivision, searchDbPropertySalesLocation)

Search API for &#39;Property Sales&#39; entry type

API to search for entries of type Property Sales

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypePropertySalesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypePropertySalesApi apiInstance = new TypePropertySalesApi(defaultClient);
    String text = "text_example"; // String | Search text
    String name = "name_example"; // String | Search name
    String description = "description_example"; // String | Search description
    OffsetDateTime fromdate = OffsetDateTime.now(); // OffsetDateTime | From date
    OffsetDateTime todate = OffsetDateTime.now(); // OffsetDateTime | To date
    OffsetDateTime createdateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive create date from
    OffsetDateTime createdateTo = OffsetDateTime.now(); // OffsetDateTime | Archive create date to
    OffsetDateTime changedateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive change date from
    OffsetDateTime changedateTo = OffsetDateTime.now(); // OffsetDateTime | Archive change date to
    String group = "group_example"; // String | Parent entry
    String filesuffix = "filesuffix_example"; // String | File suffix
    Float maxlatitude = 3.4F; // Float | Northern bounds of search
    Float minlongitude = 3.4F; // Float | Western bounds of search
    Float minlatitude = 3.4F; // Float | Southern bounds of search
    Float maxlongitude = 3.4F; // Float | Eastern bounds of search
    Integer max = 56; // Integer | Max number of results
    Integer skip = 56; // Integer | Number to skip
    String searchDbPropertySalesPropertyAddress = "searchDbPropertySalesPropertyAddress_example"; // String | Property Address
    String searchDbPropertySalesCity = "searchDbPropertySalesCity_example"; // String | City
    String searchDbPropertySalesZipcode = "searchDbPropertySalesZipcode_example"; // String | Zip Code
    Double searchDbPropertySalesSalePrice = 3.4D; // Double | Sale Price
    String searchDbPropertySalesSaleDate = "searchDbPropertySalesSaleDate_example"; // String | Sale Date
    String searchDbPropertySalesSeller = "searchDbPropertySalesSeller_example"; // String | Seller
    String searchDbPropertySalesBuyer = "searchDbPropertySalesBuyer_example"; // String | Buyer
    String searchDbPropertySalesType = "searchDbPropertySalesType_example"; // String | Property Type
    String searchDbPropertySalesBuildingDescription = "searchDbPropertySalesBuildingDescription_example"; // String | Building Description
    String searchDbPropertySalesBuildingDesign = "searchDbPropertySalesBuildingDesign_example"; // String | Building Design
    String searchDbPropertySalesSubdivision = "searchDbPropertySalesSubdivision_example"; // String | Subdivision
    String searchDbPropertySalesLocation = "searchDbPropertySalesLocation_example"; // String | Location
    try {
      apiInstance.searchPropertySales(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbPropertySalesPropertyAddress, searchDbPropertySalesCity, searchDbPropertySalesZipcode, searchDbPropertySalesSalePrice, searchDbPropertySalesSaleDate, searchDbPropertySalesSeller, searchDbPropertySalesBuyer, searchDbPropertySalesType, searchDbPropertySalesBuildingDescription, searchDbPropertySalesBuildingDesign, searchDbPropertySalesSubdivision, searchDbPropertySalesLocation);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypePropertySalesApi#searchPropertySales");
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
| **text** | **String**| Search text | [optional] |
| **name** | **String**| Search name | [optional] |
| **description** | **String**| Search description | [optional] |
| **fromdate** | **OffsetDateTime**| From date | [optional] |
| **todate** | **OffsetDateTime**| To date | [optional] |
| **createdateFrom** | **OffsetDateTime**| Archive create date from | [optional] |
| **createdateTo** | **OffsetDateTime**| Archive create date to | [optional] |
| **changedateFrom** | **OffsetDateTime**| Archive change date from | [optional] |
| **changedateTo** | **OffsetDateTime**| Archive change date to | [optional] |
| **group** | **String**| Parent entry | [optional] |
| **filesuffix** | **String**| File suffix | [optional] |
| **maxlatitude** | **Float**| Northern bounds of search | [optional] |
| **minlongitude** | **Float**| Western bounds of search | [optional] |
| **minlatitude** | **Float**| Southern bounds of search | [optional] |
| **maxlongitude** | **Float**| Eastern bounds of search | [optional] |
| **max** | **Integer**| Max number of results | [optional] |
| **skip** | **Integer**| Number to skip | [optional] |
| **searchDbPropertySalesPropertyAddress** | **String**| Property Address | [optional] |
| **searchDbPropertySalesCity** | **String**| City | [optional] |
| **searchDbPropertySalesZipcode** | **String**| Zip Code | [optional] |
| **searchDbPropertySalesSalePrice** | **Double**| Sale Price | [optional] |
| **searchDbPropertySalesSaleDate** | **String**| Sale Date | [optional] |
| **searchDbPropertySalesSeller** | **String**| Seller | [optional] |
| **searchDbPropertySalesBuyer** | **String**| Buyer | [optional] |
| **searchDbPropertySalesType** | **String**| Property Type | [optional] |
| **searchDbPropertySalesBuildingDescription** | **String**| Building Description | [optional] |
| **searchDbPropertySalesBuildingDesign** | **String**| Building Design | [optional] |
| **searchDbPropertySalesSubdivision** | **String**| Subdivision | [optional] |
| **searchDbPropertySalesLocation** | **String**| Location | [optional] |

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
| **200** | No response was specified |  -  |

