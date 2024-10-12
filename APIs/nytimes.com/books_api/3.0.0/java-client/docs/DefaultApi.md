# DefaultApi

All URIs are relative to *https://api.nytimes.com/svc/books/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETListsBestSellersHistoryJson**](DefaultApi.md#gETListsBestSellersHistoryJson) | **GET** /lists/best-sellers/history.json | Best Seller History List |
| [**gETListsDateListJson**](DefaultApi.md#gETListsDateListJson) | **GET** /lists/{date}/{list}.json | Best Seller List by Date |
| [**gETListsFormat**](DefaultApi.md#gETListsFormat) | **GET** /lists.{format} | Best Seller List |
| [**gETListsNamesFormat**](DefaultApi.md#gETListsNamesFormat) | **GET** /lists/names.{format} | Best Seller List Names |
| [**gETListsOverviewFormat**](DefaultApi.md#gETListsOverviewFormat) | **GET** /lists/overview.{format} | Best Seller List Overview |
| [**gETReviewsFormat**](DefaultApi.md#gETReviewsFormat) | **GET** /reviews.{format} | Reviews |


<a id="gETListsBestSellersHistoryJson"></a>
# **gETListsBestSellersHistoryJson**
> GETListsBestSellersHistoryJson200Response gETListsBestSellersHistoryJson(ageGroup, author, contributor, isbn, price, publisher, title)

Best Seller History List



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nytimes.com/svc/books/v3");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ageGroup = "ageGroup_example"; // String | The target age group for the best seller.
    String author = "author_example"; // String | The author of the best seller. The author field does not include additional contributors (see Data Structure for more details about the author and contributor fields).  When searching the author field, you can specify any combination of first, middle and last names.  When sort-by is set to author, the results will be sorted by author's first name. 
    String contributor = "contributor_example"; // String | The author of the best seller, as well as other contributors such as the illustrator (to search or sort by author name only, use author instead).  When searching, you can specify any combination of first, middle and last names of any of the contributors.  When sort-by is set to contributor, the results will be sorted by the first name of the first contributor listed. 
    String isbn = "isbn_example"; // String | International Standard Book Number, 10 or 13 digits  A best seller may have both 10-digit and 13-digit ISBNs, and may have multiple ISBNs of each type. To search on multiple ISBNs, separate the ISBNs with semicolons (example: 9780446579933;0061374229).
    String price = "price_example"; // String | The publisher's list price of the best seller, including decimal point
    String publisher = "publisher_example"; // String | The standardized name of the publisher
    String title = "title_example"; // String | The title of the best seller  When searching, you can specify a portion of a title or a full title.
    try {
      GETListsBestSellersHistoryJson200Response result = apiInstance.gETListsBestSellersHistoryJson(ageGroup, author, contributor, isbn, price, publisher, title);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETListsBestSellersHistoryJson");
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
| **ageGroup** | **String**| The target age group for the best seller. | [optional] |
| **author** | **String**| The author of the best seller. The author field does not include additional contributors (see Data Structure for more details about the author and contributor fields).  When searching the author field, you can specify any combination of first, middle and last names.  When sort-by is set to author, the results will be sorted by author&#39;s first name.  | [optional] |
| **contributor** | **String**| The author of the best seller, as well as other contributors such as the illustrator (to search or sort by author name only, use author instead).  When searching, you can specify any combination of first, middle and last names of any of the contributors.  When sort-by is set to contributor, the results will be sorted by the first name of the first contributor listed.  | [optional] |
| **isbn** | **String**| International Standard Book Number, 10 or 13 digits  A best seller may have both 10-digit and 13-digit ISBNs, and may have multiple ISBNs of each type. To search on multiple ISBNs, separate the ISBNs with semicolons (example: 9780446579933;0061374229). | [optional] |
| **price** | **String**| The publisher&#39;s list price of the best seller, including decimal point | [optional] |
| **publisher** | **String**| The standardized name of the publisher | [optional] |
| **title** | **String**| The title of the best seller  When searching, you can specify a portion of a title or a full title. | [optional] |

### Return type

[**GETListsBestSellersHistoryJson200Response**](GETListsBestSellersHistoryJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="gETListsDateListJson"></a>
# **gETListsDateListJson**
> GETListsDateListJson200Response gETListsDateListJson(date, _list, isbn, listName, publishedDate, bestsellersDate, weeksOnList, rank, rankLastWeek, offset, sortOrder)

Best Seller List by Date



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nytimes.com/svc/books/v3");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String date = "date_example"; // String | 
    String _list = "_list_example"; // String | Name of the Best Sellers List. You can get the full list from /lists/names.json
    Integer isbn = 56; // Integer | International Standard Book Number, 10 or 13 digits
    String listName = "listName_example"; // String | The name of the Times best-seller list. To get valid values, use a list names request.  Be sure to replace spaces with hyphens (e.g., e-book-fiction or hardcover-fiction, not E-Book Fiction or Hardcover Fiction). (The parameter is not case sensitive.)
    OffsetDateTime publishedDate = OffsetDateTime.now(); // OffsetDateTime | YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date)
    String bestsellersDate = "bestsellersDate_example"; // String | YYYY-MM-DD  The week-ending date for the sales reflected on list-name. Times best-seller lists are compiled using available book sale data. The bestsellers-date may be significantly earlier than published-date. For additional information, see the explanation at the bottom of any best-seller list page on NYTimes.com (example: Hardcover Fiction, published Dec. 5 but reflecting sales to Nov. 29).
    Integer weeksOnList = 56; // Integer | The number of weeks that the best seller has been on list-name, as of bestsellers-date
    String rank = "rank_example"; // String | The rank of the best seller on list-name as of bestsellers-date
    Integer rankLastWeek = 56; // Integer | The rank of the best seller on list-name one week prior to bestsellers-date
    Integer offset = 56; // Integer | Sets the starting point of the result set
    String sortOrder = "ASC"; // String | The default is ASC (ascending). The sort-order parameter is used with the sort-by parameter — for details, see each request type.
    try {
      GETListsDateListJson200Response result = apiInstance.gETListsDateListJson(date, _list, isbn, listName, publishedDate, bestsellersDate, weeksOnList, rank, rankLastWeek, offset, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETListsDateListJson");
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
| **date** | **String**|  | |
| **_list** | **String**| Name of the Best Sellers List. You can get the full list from /lists/names.json | |
| **isbn** | **Integer**| International Standard Book Number, 10 or 13 digits | [optional] |
| **listName** | **String**| The name of the Times best-seller list. To get valid values, use a list names request.  Be sure to replace spaces with hyphens (e.g., e-book-fiction or hardcover-fiction, not E-Book Fiction or Hardcover Fiction). (The parameter is not case sensitive.) | [optional] |
| **publishedDate** | **OffsetDateTime**| YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date) | [optional] |
| **bestsellersDate** | **String**| YYYY-MM-DD  The week-ending date for the sales reflected on list-name. Times best-seller lists are compiled using available book sale data. The bestsellers-date may be significantly earlier than published-date. For additional information, see the explanation at the bottom of any best-seller list page on NYTimes.com (example: Hardcover Fiction, published Dec. 5 but reflecting sales to Nov. 29). | [optional] |
| **weeksOnList** | **Integer**| The number of weeks that the best seller has been on list-name, as of bestsellers-date | [optional] |
| **rank** | **String**| The rank of the best seller on list-name as of bestsellers-date | [optional] |
| **rankLastWeek** | **Integer**| The rank of the best seller on list-name one week prior to bestsellers-date | [optional] |
| **offset** | **Integer**| Sets the starting point of the result set | [optional] |
| **sortOrder** | **String**| The default is ASC (ascending). The sort-order parameter is used with the sort-by parameter — for details, see each request type. | [optional] [enum: ASC, DESC] |

### Return type

[**GETListsDateListJson200Response**](GETListsDateListJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="gETListsFormat"></a>
# **gETListsFormat**
> GETListsFormat200Response gETListsFormat(format, _list, weeksOnList, bestsellersDate, date, isbn, publishedDate, rank, rankLastWeek, offset, sortOrder)

Best Seller List



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nytimes.com/svc/books/v3");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "json"; // String | 
    String _list = "_list_example"; // String | The name of the Times best-seller list. To get valid values, use a list names request.  Be sure to replace spaces with hyphens (e.g., e-book-fiction or hardcover-fiction, not E-Book Fiction or Hardcover Fiction). (The parameter is not case sensitive.)
    Integer weeksOnList = 56; // Integer | The number of weeks that the best seller has been on list-name, as of bestsellers-date
    OffsetDateTime bestsellersDate = OffsetDateTime.now(); // OffsetDateTime | YYYY-MM-DD  The week-ending date for the sales reflected on list-name. Times best-seller lists are compiled using available book sale data. The bestsellers-date may be significantly earlier than published-date. For additional information, see the explanation at the bottom of any best-seller list page on NYTimes.com (example: Hardcover Fiction, published Dec. 5 but reflecting sales to Nov. 29).
    String date = "date_example"; // String | YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date)
    String isbn = "isbn_example"; // String | International Standard Book Number, 10 or 13 digits
    String publishedDate = "publishedDate_example"; // String | YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date)
    Integer rank = 56; // Integer | The rank of the best seller on list-name as of bestsellers-date
    Integer rankLastWeek = 56; // Integer | The rank of the best seller on list-name one week prior to bestsellers-date
    Integer offset = 56; // Integer | Sets the starting point of the result set
    String sortOrder = "ASC"; // String | Sets the sort order of the result set
    try {
      GETListsFormat200Response result = apiInstance.gETListsFormat(format, _list, weeksOnList, bestsellersDate, date, isbn, publishedDate, rank, rankLastWeek, offset, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETListsFormat");
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
| **format** | **String**|  | [enum: json, jsonp] |
| **_list** | **String**| The name of the Times best-seller list. To get valid values, use a list names request.  Be sure to replace spaces with hyphens (e.g., e-book-fiction or hardcover-fiction, not E-Book Fiction or Hardcover Fiction). (The parameter is not case sensitive.) | [optional] |
| **weeksOnList** | **Integer**| The number of weeks that the best seller has been on list-name, as of bestsellers-date | [optional] |
| **bestsellersDate** | **OffsetDateTime**| YYYY-MM-DD  The week-ending date for the sales reflected on list-name. Times best-seller lists are compiled using available book sale data. The bestsellers-date may be significantly earlier than published-date. For additional information, see the explanation at the bottom of any best-seller list page on NYTimes.com (example: Hardcover Fiction, published Dec. 5 but reflecting sales to Nov. 29). | [optional] |
| **date** | **String**| YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date) | [optional] |
| **isbn** | **String**| International Standard Book Number, 10 or 13 digits | [optional] |
| **publishedDate** | **String**| YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date) | [optional] |
| **rank** | **Integer**| The rank of the best seller on list-name as of bestsellers-date | [optional] |
| **rankLastWeek** | **Integer**| The rank of the best seller on list-name one week prior to bestsellers-date | [optional] |
| **offset** | **Integer**| Sets the starting point of the result set | [optional] |
| **sortOrder** | **String**| Sets the sort order of the result set | [optional] [enum: ASC, DESC] |

### Return type

[**GETListsFormat200Response**](GETListsFormat200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="gETListsNamesFormat"></a>
# **gETListsNamesFormat**
> GETListsNamesFormat200Response gETListsNamesFormat(format, apiKey)

Best Seller List Names



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nytimes.com/svc/books/v3");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "json"; // String | 
    String apiKey = "apiKey_example"; // String | 
    try {
      GETListsNamesFormat200Response result = apiInstance.gETListsNamesFormat(format, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETListsNamesFormat");
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
| **format** | **String**|  | [enum: json, jsonp] |
| **apiKey** | **String**|  | [optional] |

### Return type

[**GETListsNamesFormat200Response**](GETListsNamesFormat200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="gETListsOverviewFormat"></a>
# **gETListsOverviewFormat**
> GETListsOverviewFormat200Response gETListsOverviewFormat(format, publishedDate, apiKey)

Best Seller List Overview



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nytimes.com/svc/books/v3");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "json"; // String | 
    String publishedDate = "publishedDate_example"; // String | The best-seller list publication date. YYYY-MM-DD  You do not have to specify the exact date the list was published. The service will search forward (into the future) for the closest publication date to the date you specify. For example, a request for lists/overview/2013-05-22 will retrieve the list that was published on 05-26.  If you do not include a published_date, the current week's best-sellers lists will be returned.
    String apiKey = "apiKey_example"; // String | 
    try {
      GETListsOverviewFormat200Response result = apiInstance.gETListsOverviewFormat(format, publishedDate, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETListsOverviewFormat");
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
| **format** | **String**|  | [enum: json, jsonp] |
| **publishedDate** | **String**| The best-seller list publication date. YYYY-MM-DD  You do not have to specify the exact date the list was published. The service will search forward (into the future) for the closest publication date to the date you specify. For example, a request for lists/overview/2013-05-22 will retrieve the list that was published on 05-26.  If you do not include a published_date, the current week&#39;s best-sellers lists will be returned. | [optional] |
| **apiKey** | **String**|  | [optional] |

### Return type

[**GETListsOverviewFormat200Response**](GETListsOverviewFormat200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="gETReviewsFormat"></a>
# **gETReviewsFormat**
> GETReviewsFormat200Response gETReviewsFormat(format, isbn, title, author, apiKey)

Reviews



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nytimes.com/svc/books/v3");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "json"; // String | 
    Integer isbn = 56; // Integer | Searching by ISBN is the recommended method. You can enter 10- or 13-digit ISBNs.
    String title = "title_example"; // String | You’ll need to enter the full title of the book. Spaces in the title will be converted into the characters %20.
    String author = "author_example"; // String | You’ll need to enter the author’s first and last name, separated by a space. This space will be converted into the characters %20.
    String apiKey = "apiKey_example"; // String | 
    try {
      GETReviewsFormat200Response result = apiInstance.gETReviewsFormat(format, isbn, title, author, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETReviewsFormat");
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
| **format** | **String**|  | [enum: json, jsonp] |
| **isbn** | **Integer**| Searching by ISBN is the recommended method. You can enter 10- or 13-digit ISBNs. | [optional] |
| **title** | **String**| You’ll need to enter the full title of the book. Spaces in the title will be converted into the characters %20. | [optional] |
| **author** | **String**| You’ll need to enter the author’s first and last name, separated by a space. This space will be converted into the characters %20. | [optional] |
| **apiKey** | **String**|  | [optional] |

### Return type

[**GETReviewsFormat200Response**](GETReviewsFormat200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

