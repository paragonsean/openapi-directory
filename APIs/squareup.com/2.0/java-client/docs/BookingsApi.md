# BookingsApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelBooking**](BookingsApi.md#cancelBooking) | **POST** /v2/bookings/{booking_id}/cancel | CancelBooking |
| [**createBooking**](BookingsApi.md#createBooking) | **POST** /v2/bookings | CreateBooking |
| [**listTeamMemberBookingProfiles**](BookingsApi.md#listTeamMemberBookingProfiles) | **GET** /v2/bookings/team-member-booking-profiles | ListTeamMemberBookingProfiles |
| [**retrieveBooking**](BookingsApi.md#retrieveBooking) | **GET** /v2/bookings/{booking_id} | RetrieveBooking |
| [**retrieveBusinessBookingProfile**](BookingsApi.md#retrieveBusinessBookingProfile) | **GET** /v2/bookings/business-booking-profile | RetrieveBusinessBookingProfile |
| [**retrieveTeamMemberBookingProfile**](BookingsApi.md#retrieveTeamMemberBookingProfile) | **GET** /v2/bookings/team-member-booking-profiles/{team_member_id} | RetrieveTeamMemberBookingProfile |
| [**searchAvailability**](BookingsApi.md#searchAvailability) | **POST** /v2/bookings/availability/search | SearchAvailability |
| [**updateBooking**](BookingsApi.md#updateBooking) | **PUT** /v2/bookings/{booking_id} | UpdateBooking |


<a id="cancelBooking"></a>
# **cancelBooking**
> CancelBookingResponse cancelBooking(bookingId, cancelBookingRequest)

CancelBooking

Cancels an existing booking.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String bookingId = "bookingId_example"; // String | The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-cancelled booking.
    CancelBookingRequest cancelBookingRequest = new CancelBookingRequest(); // CancelBookingRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CancelBookingResponse result = apiInstance.cancelBooking(bookingId, cancelBookingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#cancelBooking");
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
| **bookingId** | **String**| The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-cancelled booking. | |
| **cancelBookingRequest** | [**CancelBookingRequest**](CancelBookingRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CancelBookingResponse**](CancelBookingResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="createBooking"></a>
# **createBooking**
> CreateBookingResponse createBooking(createBookingRequest)

CreateBooking

Creates a booking.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    CreateBookingRequest createBookingRequest = new CreateBookingRequest(); // CreateBookingRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateBookingResponse result = apiInstance.createBooking(createBookingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#createBooking");
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
| **createBookingRequest** | [**CreateBookingRequest**](CreateBookingRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateBookingResponse**](CreateBookingResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listTeamMemberBookingProfiles"></a>
# **listTeamMemberBookingProfiles**
> ListTeamMemberBookingProfilesResponse listTeamMemberBookingProfiles(bookableOnly, limit, cursor, locationId)

ListTeamMemberBookingProfiles

Lists booking profiles for team members.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    Boolean bookableOnly = true; // Boolean | Indicates whether to include only bookable team members in the returned result (`true`) or not (`false`).
    Integer limit = 56; // Integer | The maximum number of results to return.
    String cursor = "cursor_example"; // String | The cursor for paginating through the results.
    String locationId = "locationId_example"; // String | Indicates whether to include only team members enabled at the given location in the returned result.
    try {
      ListTeamMemberBookingProfilesResponse result = apiInstance.listTeamMemberBookingProfiles(bookableOnly, limit, cursor, locationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#listTeamMemberBookingProfiles");
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
| **bookableOnly** | **Boolean**| Indicates whether to include only bookable team members in the returned result (&#x60;true&#x60;) or not (&#x60;false&#x60;). | [optional] |
| **limit** | **Integer**| The maximum number of results to return. | [optional] |
| **cursor** | **String**| The cursor for paginating through the results. | [optional] |
| **locationId** | **String**| Indicates whether to include only team members enabled at the given location in the returned result. | [optional] |

### Return type

[**ListTeamMemberBookingProfilesResponse**](ListTeamMemberBookingProfilesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveBooking"></a>
# **retrieveBooking**
> RetrieveBookingResponse retrieveBooking(bookingId)

RetrieveBooking

Retrieves a booking.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String bookingId = "bookingId_example"; // String | The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-retrieved booking.
    try {
      RetrieveBookingResponse result = apiInstance.retrieveBooking(bookingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#retrieveBooking");
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
| **bookingId** | **String**| The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-retrieved booking. | |

### Return type

[**RetrieveBookingResponse**](RetrieveBookingResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveBusinessBookingProfile"></a>
# **retrieveBusinessBookingProfile**
> RetrieveBusinessBookingProfileResponse retrieveBusinessBookingProfile()

RetrieveBusinessBookingProfile

Retrieves a seller&#39;s booking profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    try {
      RetrieveBusinessBookingProfileResponse result = apiInstance.retrieveBusinessBookingProfile();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#retrieveBusinessBookingProfile");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RetrieveBusinessBookingProfileResponse**](RetrieveBusinessBookingProfileResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveTeamMemberBookingProfile"></a>
# **retrieveTeamMemberBookingProfile**
> RetrieveTeamMemberBookingProfileResponse retrieveTeamMemberBookingProfile(teamMemberId)

RetrieveTeamMemberBookingProfile

Retrieves a team member&#39;s booking profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String teamMemberId = "teamMemberId_example"; // String | The ID of the team member to retrieve.
    try {
      RetrieveTeamMemberBookingProfileResponse result = apiInstance.retrieveTeamMemberBookingProfile(teamMemberId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#retrieveTeamMemberBookingProfile");
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
| **teamMemberId** | **String**| The ID of the team member to retrieve. | |

### Return type

[**RetrieveTeamMemberBookingProfileResponse**](RetrieveTeamMemberBookingProfileResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="searchAvailability"></a>
# **searchAvailability**
> SearchAvailabilityResponse searchAvailability(searchAvailabilityRequest)

SearchAvailability

Searches for availabilities for booking.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    SearchAvailabilityRequest searchAvailabilityRequest = new SearchAvailabilityRequest(); // SearchAvailabilityRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      SearchAvailabilityResponse result = apiInstance.searchAvailability(searchAvailabilityRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#searchAvailability");
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
| **searchAvailabilityRequest** | [**SearchAvailabilityRequest**](SearchAvailabilityRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**SearchAvailabilityResponse**](SearchAvailabilityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateBooking"></a>
# **updateBooking**
> UpdateBookingResponse updateBooking(bookingId, updateBookingRequest)

UpdateBooking

Updates a booking.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String bookingId = "bookingId_example"; // String | The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-updated booking.
    UpdateBookingRequest updateBookingRequest = new UpdateBookingRequest(); // UpdateBookingRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      UpdateBookingResponse result = apiInstance.updateBooking(bookingId, updateBookingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#updateBooking");
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
| **bookingId** | **String**| The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-updated booking. | |
| **updateBookingRequest** | [**UpdateBookingRequest**](UpdateBookingRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**UpdateBookingResponse**](UpdateBookingResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

