# BooksApi.DefaultApi

All URIs are relative to *https://api.nytimes.com/svc/books/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETListsBestSellersHistoryJson**](DefaultApi.md#gETListsBestSellersHistoryJson) | **GET** /lists/best-sellers/history.json | Best Seller History List
[**gETListsDateListJson**](DefaultApi.md#gETListsDateListJson) | **GET** /lists/{date}/{list}.json | Best Seller List by Date
[**gETListsFormat**](DefaultApi.md#gETListsFormat) | **GET** /lists.{format} | Best Seller List
[**gETListsNamesFormat**](DefaultApi.md#gETListsNamesFormat) | **GET** /lists/names.{format} | Best Seller List Names
[**gETListsOverviewFormat**](DefaultApi.md#gETListsOverviewFormat) | **GET** /lists/overview.{format} | Best Seller List Overview
[**gETReviewsFormat**](DefaultApi.md#gETReviewsFormat) | **GET** /reviews.{format} | Reviews



## gETListsBestSellersHistoryJson

> GETListsBestSellersHistoryJson200Response gETListsBestSellersHistoryJson(opts)

Best Seller History List



### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new BooksApi.DefaultApi();
let opts = {
  'ageGroup': "ageGroup_example", // String | The target age group for the best seller.
  'author': "author_example", // String | The author of the best seller. The author field does not include additional contributors (see Data Structure for more details about the author and contributor fields).  When searching the author field, you can specify any combination of first, middle and last names.  When sort-by is set to author, the results will be sorted by author's first name. 
  'contributor': "contributor_example", // String | The author of the best seller, as well as other contributors such as the illustrator (to search or sort by author name only, use author instead).  When searching, you can specify any combination of first, middle and last names of any of the contributors.  When sort-by is set to contributor, the results will be sorted by the first name of the first contributor listed. 
  'isbn': "isbn_example", // String | International Standard Book Number, 10 or 13 digits  A best seller may have both 10-digit and 13-digit ISBNs, and may have multiple ISBNs of each type. To search on multiple ISBNs, separate the ISBNs with semicolons (example: 9780446579933;0061374229).
  'price': "price_example", // String | The publisher's list price of the best seller, including decimal point
  'publisher': "publisher_example", // String | The standardized name of the publisher
  'title': "title_example" // String | The title of the best seller  When searching, you can specify a portion of a title or a full title.
};
apiInstance.gETListsBestSellersHistoryJson(opts, (error, data, response) => {
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
 **ageGroup** | **String**| The target age group for the best seller. | [optional] 
 **author** | **String**| The author of the best seller. The author field does not include additional contributors (see Data Structure for more details about the author and contributor fields).  When searching the author field, you can specify any combination of first, middle and last names.  When sort-by is set to author, the results will be sorted by author&#39;s first name.  | [optional] 
 **contributor** | **String**| The author of the best seller, as well as other contributors such as the illustrator (to search or sort by author name only, use author instead).  When searching, you can specify any combination of first, middle and last names of any of the contributors.  When sort-by is set to contributor, the results will be sorted by the first name of the first contributor listed.  | [optional] 
 **isbn** | **String**| International Standard Book Number, 10 or 13 digits  A best seller may have both 10-digit and 13-digit ISBNs, and may have multiple ISBNs of each type. To search on multiple ISBNs, separate the ISBNs with semicolons (example: 9780446579933;0061374229). | [optional] 
 **price** | **String**| The publisher&#39;s list price of the best seller, including decimal point | [optional] 
 **publisher** | **String**| The standardized name of the publisher | [optional] 
 **title** | **String**| The title of the best seller  When searching, you can specify a portion of a title or a full title. | [optional] 

### Return type

[**GETListsBestSellersHistoryJson200Response**](GETListsBestSellersHistoryJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETListsDateListJson

> GETListsDateListJson200Response gETListsDateListJson(date, list, opts)

Best Seller List by Date



### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new BooksApi.DefaultApi();
let date = "date_example"; // String | 
let list = "list_example"; // String | Name of the Best Sellers List. You can get the full list from /lists/names.json
let opts = {
  'isbn': 56, // Number | International Standard Book Number, 10 or 13 digits
  'listName': "listName_example", // String | The name of the Times best-seller list. To get valid values, use a list names request.  Be sure to replace spaces with hyphens (e.g., e-book-fiction or hardcover-fiction, not E-Book Fiction or Hardcover Fiction). (The parameter is not case sensitive.)
  'publishedDate': new Date("2013-10-20T19:20:30+01:00"), // Date | YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date)
  'bestsellersDate': "bestsellersDate_example", // String | YYYY-MM-DD  The week-ending date for the sales reflected on list-name. Times best-seller lists are compiled using available book sale data. The bestsellers-date may be significantly earlier than published-date. For additional information, see the explanation at the bottom of any best-seller list page on NYTimes.com (example: Hardcover Fiction, published Dec. 5 but reflecting sales to Nov. 29).
  'weeksOnList': 56, // Number | The number of weeks that the best seller has been on list-name, as of bestsellers-date
  'rank': "rank_example", // String | The rank of the best seller on list-name as of bestsellers-date
  'rankLastWeek': 56, // Number | The rank of the best seller on list-name one week prior to bestsellers-date
  'offset': 56, // Number | Sets the starting point of the result set
  'sortOrder': "sortOrder_example" // String | The default is ASC (ascending). The sort-order parameter is used with the sort-by parameter — for details, see each request type.
};
apiInstance.gETListsDateListJson(date, list, opts, (error, data, response) => {
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
 **date** | **String**|  | 
 **list** | **String**| Name of the Best Sellers List. You can get the full list from /lists/names.json | 
 **isbn** | **Number**| International Standard Book Number, 10 or 13 digits | [optional] 
 **listName** | **String**| The name of the Times best-seller list. To get valid values, use a list names request.  Be sure to replace spaces with hyphens (e.g., e-book-fiction or hardcover-fiction, not E-Book Fiction or Hardcover Fiction). (The parameter is not case sensitive.) | [optional] 
 **publishedDate** | **Date**| YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date) | [optional] 
 **bestsellersDate** | **String**| YYYY-MM-DD  The week-ending date for the sales reflected on list-name. Times best-seller lists are compiled using available book sale data. The bestsellers-date may be significantly earlier than published-date. For additional information, see the explanation at the bottom of any best-seller list page on NYTimes.com (example: Hardcover Fiction, published Dec. 5 but reflecting sales to Nov. 29). | [optional] 
 **weeksOnList** | **Number**| The number of weeks that the best seller has been on list-name, as of bestsellers-date | [optional] 
 **rank** | **String**| The rank of the best seller on list-name as of bestsellers-date | [optional] 
 **rankLastWeek** | **Number**| The rank of the best seller on list-name one week prior to bestsellers-date | [optional] 
 **offset** | **Number**| Sets the starting point of the result set | [optional] 
 **sortOrder** | **String**| The default is ASC (ascending). The sort-order parameter is used with the sort-by parameter — for details, see each request type. | [optional] 

### Return type

[**GETListsDateListJson200Response**](GETListsDateListJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETListsFormat

> GETListsFormat200Response gETListsFormat(format, opts)

Best Seller List



### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new BooksApi.DefaultApi();
let format = "format_example"; // String | 
let opts = {
  'list': "list_example", // String | The name of the Times best-seller list. To get valid values, use a list names request.  Be sure to replace spaces with hyphens (e.g., e-book-fiction or hardcover-fiction, not E-Book Fiction or Hardcover Fiction). (The parameter is not case sensitive.)
  'weeksOnList': 56, // Number | The number of weeks that the best seller has been on list-name, as of bestsellers-date
  'bestsellersDate': new Date("2013-10-20T19:20:30+01:00"), // Date | YYYY-MM-DD  The week-ending date for the sales reflected on list-name. Times best-seller lists are compiled using available book sale data. The bestsellers-date may be significantly earlier than published-date. For additional information, see the explanation at the bottom of any best-seller list page on NYTimes.com (example: Hardcover Fiction, published Dec. 5 but reflecting sales to Nov. 29).
  'date': "date_example", // String | YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date)
  'isbn': "isbn_example", // String | International Standard Book Number, 10 or 13 digits
  'publishedDate': "publishedDate_example", // String | YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date)
  'rank': 56, // Number | The rank of the best seller on list-name as of bestsellers-date
  'rankLastWeek': 56, // Number | The rank of the best seller on list-name one week prior to bestsellers-date
  'offset': 56, // Number | Sets the starting point of the result set
  'sortOrder': "sortOrder_example" // String | Sets the sort order of the result set
};
apiInstance.gETListsFormat(format, opts, (error, data, response) => {
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
 **format** | **String**|  | 
 **list** | **String**| The name of the Times best-seller list. To get valid values, use a list names request.  Be sure to replace spaces with hyphens (e.g., e-book-fiction or hardcover-fiction, not E-Book Fiction or Hardcover Fiction). (The parameter is not case sensitive.) | [optional] 
 **weeksOnList** | **Number**| The number of weeks that the best seller has been on list-name, as of bestsellers-date | [optional] 
 **bestsellersDate** | **Date**| YYYY-MM-DD  The week-ending date for the sales reflected on list-name. Times best-seller lists are compiled using available book sale data. The bestsellers-date may be significantly earlier than published-date. For additional information, see the explanation at the bottom of any best-seller list page on NYTimes.com (example: Hardcover Fiction, published Dec. 5 but reflecting sales to Nov. 29). | [optional] 
 **date** | **String**| YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date) | [optional] 
 **isbn** | **String**| International Standard Book Number, 10 or 13 digits | [optional] 
 **publishedDate** | **String**| YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date) | [optional] 
 **rank** | **Number**| The rank of the best seller on list-name as of bestsellers-date | [optional] 
 **rankLastWeek** | **Number**| The rank of the best seller on list-name one week prior to bestsellers-date | [optional] 
 **offset** | **Number**| Sets the starting point of the result set | [optional] 
 **sortOrder** | **String**| Sets the sort order of the result set | [optional] 

### Return type

[**GETListsFormat200Response**](GETListsFormat200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETListsNamesFormat

> GETListsNamesFormat200Response gETListsNamesFormat(format, opts)

Best Seller List Names



### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new BooksApi.DefaultApi();
let format = "format_example"; // String | 
let opts = {
  'apiKey': "apiKey_example" // String | 
};
apiInstance.gETListsNamesFormat(format, opts, (error, data, response) => {
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
 **format** | **String**|  | 
 **apiKey** | **String**|  | [optional] 

### Return type

[**GETListsNamesFormat200Response**](GETListsNamesFormat200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETListsOverviewFormat

> GETListsOverviewFormat200Response gETListsOverviewFormat(format, opts)

Best Seller List Overview



### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new BooksApi.DefaultApi();
let format = "format_example"; // String | 
let opts = {
  'publishedDate': "publishedDate_example", // String | The best-seller list publication date. YYYY-MM-DD  You do not have to specify the exact date the list was published. The service will search forward (into the future) for the closest publication date to the date you specify. For example, a request for lists/overview/2013-05-22 will retrieve the list that was published on 05-26.  If you do not include a published_date, the current week's best-sellers lists will be returned.
  'apiKey': "apiKey_example" // String | 
};
apiInstance.gETListsOverviewFormat(format, opts, (error, data, response) => {
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
 **format** | **String**|  | 
 **publishedDate** | **String**| The best-seller list publication date. YYYY-MM-DD  You do not have to specify the exact date the list was published. The service will search forward (into the future) for the closest publication date to the date you specify. For example, a request for lists/overview/2013-05-22 will retrieve the list that was published on 05-26.  If you do not include a published_date, the current week&#39;s best-sellers lists will be returned. | [optional] 
 **apiKey** | **String**|  | [optional] 

### Return type

[**GETListsOverviewFormat200Response**](GETListsOverviewFormat200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETReviewsFormat

> GETReviewsFormat200Response gETReviewsFormat(format, opts)

Reviews



### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new BooksApi.DefaultApi();
let format = "format_example"; // String | 
let opts = {
  'isbn': 56, // Number | Searching by ISBN is the recommended method. You can enter 10- or 13-digit ISBNs.
  'title': "title_example", // String | You’ll need to enter the full title of the book. Spaces in the title will be converted into the characters %20.
  'author': "author_example", // String | You’ll need to enter the author’s first and last name, separated by a space. This space will be converted into the characters %20.
  'apiKey': "apiKey_example" // String | 
};
apiInstance.gETReviewsFormat(format, opts, (error, data, response) => {
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
 **format** | **String**|  | 
 **isbn** | **Number**| Searching by ISBN is the recommended method. You can enter 10- or 13-digit ISBNs. | [optional] 
 **title** | **String**| You’ll need to enter the full title of the book. Spaces in the title will be converted into the characters %20. | [optional] 
 **author** | **String**| You’ll need to enter the author’s first and last name, separated by a space. This space will be converted into the characters %20. | [optional] 
 **apiKey** | **String**|  | [optional] 

### Return type

[**GETReviewsFormat200Response**](GETReviewsFormat200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

