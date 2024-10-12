# ClassApi

All URIs are relative to *https://api.flat.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateClass**](ClassApi.md#activateClass) | **POST** /classes/{class}/activate | Activate the class |
| [**addClassUser**](ClassApi.md#addClassUser) | **PUT** /classes/{class}/users/{user} | Add a user to the class |
| [**archiveAssignment**](ClassApi.md#archiveAssignment) | **POST** /classes/{class}/assignments/{assignment}/archive | Archive the assignment |
| [**archiveClass**](ClassApi.md#archiveClass) | **POST** /classes/{class}/archive | Archive the class |
| [**copyAssignment**](ClassApi.md#copyAssignment) | **POST** /classes/{class}/assignments/{assignment}/copy | Copy an assignment |
| [**createAssignment**](ClassApi.md#createAssignment) | **POST** /classes/{class}/assignments | Assignment creation |
| [**createClass**](ClassApi.md#createClass) | **POST** /classes | Create a new class |
| [**createSubmission**](ClassApi.md#createSubmission) | **PUT** /classes/{class}/assignments/{assignment}/submissions | Create or edit a submission |
| [**deleteClassUser**](ClassApi.md#deleteClassUser) | **DELETE** /classes/{class}/users/{user} | Remove a user from the class |
| [**deleteSubmission**](ClassApi.md#deleteSubmission) | **DELETE** /classes/{class}/assignments/{assignment}/submissions/{submission} | Delete a submission |
| [**deleteSubmissionComment**](ClassApi.md#deleteSubmissionComment) | **DELETE** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments/{comment} | Delete a feedback comment to a submission |
| [**editSubmission**](ClassApi.md#editSubmission) | **PUT** /classes/{class}/assignments/{assignment}/submissions/{submission} | Edit a submission |
| [**enrollClass**](ClassApi.md#enrollClass) | **POST** /classes/enroll/{enrollmentCode} | Join a class |
| [**exportSubmissionsReviewsAsCsv**](ClassApi.md#exportSubmissionsReviewsAsCsv) | **GET** /classes/{class}/assignments/{assignment}/submissions/csv | CSV Grades exports |
| [**exportSubmissionsReviewsAsExcel**](ClassApi.md#exportSubmissionsReviewsAsExcel) | **GET** /classes/{class}/assignments/{assignment}/submissions/excel | Excel Grades exports |
| [**forkScore_0**](ClassApi.md#forkScore_0) | **POST** /scores/{score}/fork | Fork a score |
| [**getClass**](ClassApi.md#getClass) | **GET** /classes/{class} | Get the details of a single class |
| [**getScoreSubmissions_0**](ClassApi.md#getScoreSubmissions_0) | **GET** /scores/{score}/submissions | List submissions related to the score |
| [**getSubmission**](ClassApi.md#getSubmission) | **GET** /classes/{class}/assignments/{assignment}/submissions/{submission} | Get a student submission |
| [**getSubmissionComments**](ClassApi.md#getSubmissionComments) | **GET** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments | List the feedback comments of a submission |
| [**getSubmissionHistory**](ClassApi.md#getSubmissionHistory) | **GET** /classes/{class}/assignments/{assignment}/submissions/{submission}/history | Get the history of the submission |
| [**getSubmissions**](ClassApi.md#getSubmissions) | **GET** /classes/{class}/assignments/{assignment}/submissions | List the students&#39; submissions |
| [**listAssignments**](ClassApi.md#listAssignments) | **GET** /classes/{class}/assignments | Assignments listing |
| [**listClassStudentSubmissions**](ClassApi.md#listClassStudentSubmissions) | **GET** /classes/{class}/students/{user}/submissions | List the submissions for a student |
| [**listClasses**](ClassApi.md#listClasses) | **GET** /classes | List the classes available for the current user |
| [**postSubmissionComment**](ClassApi.md#postSubmissionComment) | **POST** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments | Add a feedback comment to a submission |
| [**unarchiveAssignment**](ClassApi.md#unarchiveAssignment) | **DELETE** /classes/{class}/assignments/{assignment}/archive | Unarchive the assignment. |
| [**unarchiveClass**](ClassApi.md#unarchiveClass) | **DELETE** /classes/{class}/archive | Unarchive the class |
| [**updateClass**](ClassApi.md#updateClass) | **PUT** /classes/{class} | Update the class |
| [**updateSubmissionComment**](ClassApi.md#updateSubmissionComment) | **PUT** /classes/{class}/assignments/{assignment}/submissions/{submission}/comments/{comment} | Update a feedback comment to a submission |


<a id="activateClass"></a>
# **activateClass**
> ClassDetails activateClass(propertyClass)

Activate the class

Mark the class as &#x60;active&#x60;. This is mainly used for classes synchronized from Clever that are initially with an &#x60;inactive&#x60; state and hidden in the UI. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    try {
      ClassDetails result = apiInstance.activateClass(propertyClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#activateClass");
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
| **propertyClass** | **String**| Unique identifier of the class | |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The class details |  -  |
| **0** | Error |  -  |

<a id="addClassUser"></a>
# **addClassUser**
> addClassUser(propertyClass, user)

Add a user to the class

This method can be used by a teacher of the class to enroll another Flat user into the class.  Only users that are part of your Organization can be enrolled in a class of this same Organization.  When enrolling a user in the class, Flat will automatically add this user to the corresponding Class group, based on this role in the Organization. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String user = "user_example"; // String | Unique identifier of the user
    try {
      apiInstance.addClassUser(propertyClass, user);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#addClassUser");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **user** | **String**| Unique identifier of the user | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The user has been added to the class |  -  |
| **0** | Error |  -  |

<a id="archiveAssignment"></a>
# **archiveAssignment**
> Assignment archiveAssignment(propertyClass, assignment)

Archive the assignment

Archive the assignment 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    try {
      Assignment result = apiInstance.archiveAssignment(propertyClass, assignment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#archiveAssignment");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |

### Return type

[**Assignment**](Assignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The assignment details |  -  |
| **0** | Error |  -  |

<a id="archiveClass"></a>
# **archiveClass**
> ClassDetails archiveClass(propertyClass)

Archive the class

Mark the class as &#x60;archived&#x60;. When this course is synchronized with another app, like Google Classroom, this state will be automatically be updated. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    try {
      ClassDetails result = apiInstance.archiveClass(propertyClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#archiveClass");
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
| **propertyClass** | **String**| Unique identifier of the class | |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The class details |  -  |
| **0** | Error |  -  |

<a id="copyAssignment"></a>
# **copyAssignment**
> Assignment copyAssignment(propertyClass, assignment, body)

Copy an assignment

Copy an assignment to a specified class.  If the original assignment has a due date in the past, this new assingment will be created without a due date.  If the new class is synchronized with an external app (e.g. Google Classroom), the copied assignment will also be posted on the external app. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    AssignmentCopy body = new AssignmentCopy(); // AssignmentCopy | 
    try {
      Assignment result = apiInstance.copyAssignment(propertyClass, assignment, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#copyAssignment");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |
| **body** | [**AssignmentCopy**](AssignmentCopy.md)|  | |

### Return type

[**Assignment**](Assignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The new created assingment |  -  |
| **0** | Error |  -  |

<a id="createAssignment"></a>
# **createAssignment**
> Assignment createAssignment(propertyClass, body)

Assignment creation

Use this method as a teacher to create and post a new assignment to a class.  If the class is synchronized with Google Classroom, the assignment will be automatically posted to your Classroom course. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    AssignmentCreation body = new AssignmentCreation(); // AssignmentCreation | 
    try {
      Assignment result = apiInstance.createAssignment(propertyClass, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#createAssignment");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **body** | [**AssignmentCreation**](AssignmentCreation.md)|  | [optional] |

### Return type

[**Assignment**](Assignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The assignment has been created |  -  |
| **0** | Error |  -  |

<a id="createClass"></a>
# **createClass**
> ClassDetails createClass(body)

Create a new class

Classrooms on Flat allow you to create activities with assignments and post content to a specific group.  When creating a class, Flat automatically creates two groups: one for the teachers of the course, one for the students. The creator of this class is automatically added to the teachers group.  If the classsroom is synchronized with another application like Google Classroom, some of the meta information will automatically be updated.  You can add users to this class using &#x60;PUT /classes/{class}/users/{user}&#x60;, they will automatically added to the group based on their role on Flat. Users can also enroll themselves to this class using &#x60;POST /classes/enroll/{enrollmentCode}&#x60; and the &#x60;enrollmentCode&#x60; returned in the &#x60;ClassDetails&#x60; response. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    ClassCreation body = new ClassCreation(); // ClassCreation | 
    try {
      ClassDetails result = apiInstance.createClass(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#createClass");
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
| **body** | [**ClassCreation**](ClassCreation.md)|  | |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The new class details |  -  |
| **402** | Account overquota |  -  |
| **0** | Error |  -  |

<a id="createSubmission"></a>
# **createSubmission**
> AssignmentSubmission createSubmission(propertyClass, assignment, body)

Create or edit a submission

Use this method as a student to create, update and submit a submission related to an assignment. Students can only set &#x60;attachments&#x60; and &#x60;submit&#x60;. Teachers can use &#x60;PUT /classes/{class}/assignments/{assignment}/submissions/{submission}&#x60; to update a submission by id. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    AssignmentSubmissionUpdate body = new AssignmentSubmissionUpdate(); // AssignmentSubmissionUpdate | 
    try {
      AssignmentSubmission result = apiInstance.createSubmission(propertyClass, assignment, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#createSubmission");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |
| **body** | [**AssignmentSubmissionUpdate**](AssignmentSubmissionUpdate.md)|  | |

### Return type

[**AssignmentSubmission**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The submission |  -  |
| **0** | Error |  -  |

<a id="deleteClassUser"></a>
# **deleteClassUser**
> deleteClassUser(propertyClass, user)

Remove a user from the class

This method can be used by a teacher to remove a user from the class, or by a student to leave the classroom.  Warning: Removing a user from the class will remove the associated resources, including the submissions and feedback related to these submissions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String user = "user_example"; // String | Unique identifier of the user
    try {
      apiInstance.deleteClassUser(propertyClass, user);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#deleteClassUser");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **user** | **String**| Unique identifier of the user | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The user has been removed from the class |  -  |
| **0** | Error |  -  |

<a id="deleteSubmission"></a>
# **deleteSubmission**
> deleteSubmission(propertyClass, assignment, submission)

Delete a submission

Use this method as a teacher to delete a submission and allow student to start over the assignment 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    String submission = "submission_example"; // String | Unique identifier of the submission
    try {
      apiInstance.deleteSubmission(propertyClass, assignment, submission);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#deleteSubmission");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |
| **submission** | **String**| Unique identifier of the submission | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The submission has been deleted |  -  |
| **0** | Error |  -  |

<a id="deleteSubmissionComment"></a>
# **deleteSubmissionComment**
> deleteSubmissionComment(propertyClass, assignment, submission, comment)

Delete a feedback comment to a submission

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    String submission = "submission_example"; // String | Unique identifier of the submission
    String comment = "comment_example"; // String | Unique identifier of the comment
    try {
      apiInstance.deleteSubmissionComment(propertyClass, assignment, submission, comment);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#deleteSubmissionComment");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |
| **submission** | **String**| Unique identifier of the submission | |
| **comment** | **String**| Unique identifier of the comment | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The comment has been deleted |  -  |
| **0** | Error |  -  |

<a id="editSubmission"></a>
# **editSubmission**
> AssignmentSubmission editSubmission(propertyClass, assignment, submission, body)

Edit a submission

Use this method as a teacher to update the different submission and give feedback. Teachers can only set &#x60;return&#x60;, &#x60;draftGrade&#x60; and &#x60;grade&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    String submission = "submission_example"; // String | Unique identifier of the submission
    AssignmentSubmissionUpdate body = new AssignmentSubmissionUpdate(); // AssignmentSubmissionUpdate | 
    try {
      AssignmentSubmission result = apiInstance.editSubmission(propertyClass, assignment, submission, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#editSubmission");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |
| **submission** | **String**| Unique identifier of the submission | |
| **body** | [**AssignmentSubmissionUpdate**](AssignmentSubmissionUpdate.md)|  | |

### Return type

[**AssignmentSubmission**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The submission |  -  |
| **0** | Error |  -  |

<a id="enrollClass"></a>
# **enrollClass**
> ClassDetails enrollClass(enrollmentCode)

Join a class

Use this method to join a class using an enrollment code given one of the teacher of this class. This code is also available in the &#x60;ClassDetails&#x60; returned to the teachers when creating the class or listing / fetching a specific class.  Flat will automatically add the user to the corresponding class group based on this role in the organization. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String enrollmentCode = "enrollmentCode_example"; // String | The enrollment code, available to the teacher in `ClassDetails` 
    try {
      ClassDetails result = apiInstance.enrollClass(enrollmentCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#enrollClass");
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
| **enrollmentCode** | **String**| The enrollment code, available to the teacher in &#x60;ClassDetails&#x60;  | |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The new class details |  -  |
| **0** | Error |  -  |

<a id="exportSubmissionsReviewsAsCsv"></a>
# **exportSubmissionsReviewsAsCsv**
> File exportSubmissionsReviewsAsCsv(propertyClass, assignment)

CSV Grades exports

Export list of submissions grades to a CSV file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    try {
      File result = apiInstance.exportSubmissionsReviewsAsCsv(propertyClass, assignment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#exportSubmissionsReviewsAsCsv");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of submissions |  -  |
| **0** | Error |  -  |

<a id="exportSubmissionsReviewsAsExcel"></a>
# **exportSubmissionsReviewsAsExcel**
> File exportSubmissionsReviewsAsExcel(propertyClass, assignment)

Excel Grades exports

Export list of submissions grades to an Excel file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    try {
      File result = apiInstance.exportSubmissionsReviewsAsExcel(propertyClass, assignment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#exportSubmissionsReviewsAsExcel");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of submissions |  -  |
| **0** | Error |  -  |

<a id="forkScore_0"></a>
# **forkScore_0**
> ScoreDetails forkScore_0(score, body, sharingKey)

Fork a score

This API call will make a copy of the last revision of the specified score and create a new score. The copy of the score will have a privacy set to &#x60;private&#x60;.  When using a [Flat for Education](https://flat.io/edu) account, the inline and contextualized comments will be accessible in the child document. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    ScoreFork body = new ScoreFork(); // ScoreFork | 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      ScoreDetails result = apiInstance.forkScore_0(score, body, sharingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#forkScore_0");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **body** | [**ScoreFork**](ScoreFork.md)|  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

[**ScoreDetails**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Score details |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="getClass"></a>
# **getClass**
> ClassDetails getClass(propertyClass)

Get the details of a single class

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    try {
      ClassDetails result = apiInstance.getClass(propertyClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#getClass");
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
| **propertyClass** | **String**| Unique identifier of the class | |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The new class details |  -  |
| **0** | Error |  -  |

<a id="getScoreSubmissions_0"></a>
# **getScoreSubmissions_0**
> List&lt;AssignmentSubmission&gt; getScoreSubmissions_0(score)

List submissions related to the score

This API call will list the different assignments submissions where the score is attached. This method can be used by anyone that are part of the organization and have at least read access to the document. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    try {
      List<AssignmentSubmission> result = apiInstance.getScoreSubmissions_0(score);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#getScoreSubmissions_0");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |

### Return type

[**List&lt;AssignmentSubmission&gt;**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of submissions |  -  |
| **0** | Error |  -  |

<a id="getSubmission"></a>
# **getSubmission**
> AssignmentSubmission getSubmission(propertyClass, assignment, submission)

Get a student submission

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    String submission = "submission_example"; // String | Unique identifier of the submission
    try {
      AssignmentSubmission result = apiInstance.getSubmission(propertyClass, assignment, submission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#getSubmission");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |
| **submission** | **String**| Unique identifier of the submission | |

### Return type

[**AssignmentSubmission**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A submission |  -  |
| **0** | Error |  -  |

<a id="getSubmissionComments"></a>
# **getSubmissionComments**
> List&lt;AssignmentSubmissionComment&gt; getSubmissionComments(propertyClass, assignment, submission)

List the feedback comments of a submission

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    String submission = "submission_example"; // String | Unique identifier of the submission
    try {
      List<AssignmentSubmissionComment> result = apiInstance.getSubmissionComments(propertyClass, assignment, submission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#getSubmissionComments");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |
| **submission** | **String**| Unique identifier of the submission | |

### Return type

[**List&lt;AssignmentSubmissionComment&gt;**](AssignmentSubmissionComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The comments of the score |  -  |
| **403** | Not granted to access to this submission |  -  |
| **404** | Submission not found |  -  |
| **0** | Error |  -  |

<a id="getSubmissionHistory"></a>
# **getSubmissionHistory**
> List&lt;AssignmentSubmissionHistory&gt; getSubmissionHistory(propertyClass, assignment, submission)

Get the history of the submission

For teachers only. Returns a detailed history of the submission. This currently includes state and grade histories. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    String submission = "submission_example"; // String | Unique identifier of the submission
    try {
      List<AssignmentSubmissionHistory> result = apiInstance.getSubmissionHistory(propertyClass, assignment, submission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#getSubmissionHistory");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |
| **submission** | **String**| Unique identifier of the submission | |

### Return type

[**List&lt;AssignmentSubmissionHistory&gt;**](AssignmentSubmissionHistory.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The history of the submission |  -  |
| **403** | Not granted to access to this submission |  -  |
| **404** | Submission not found |  -  |
| **0** | Error |  -  |

<a id="getSubmissions"></a>
# **getSubmissions**
> List&lt;AssignmentSubmission&gt; getSubmissions(propertyClass, assignment)

List the students&#39; submissions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    try {
      List<AssignmentSubmission> result = apiInstance.getSubmissions(propertyClass, assignment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#getSubmissions");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |

### Return type

[**List&lt;AssignmentSubmission&gt;**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The submissions |  -  |
| **0** | Error |  -  |

<a id="listAssignments"></a>
# **listAssignments**
> List&lt;Assignment&gt; listAssignments(propertyClass)

Assignments listing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    try {
      List<Assignment> result = apiInstance.listAssignments(propertyClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#listAssignments");
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
| **propertyClass** | **String**| Unique identifier of the class | |

### Return type

[**List&lt;Assignment&gt;**](Assignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of assignments for the class |  -  |
| **0** | Error |  -  |

<a id="listClassStudentSubmissions"></a>
# **listClassStudentSubmissions**
> List&lt;AssignmentSubmission&gt; listClassStudentSubmissions(propertyClass, user)

List the submissions for a student

Use this method as a teacher to list all the assignment submissions sent by a student of the class 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String user = "user_example"; // String | Unique identifier of the user
    try {
      List<AssignmentSubmission> result = apiInstance.listClassStudentSubmissions(propertyClass, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#listClassStudentSubmissions");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **user** | **String**| Unique identifier of the user | |

### Return type

[**List&lt;AssignmentSubmission&gt;**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of submissions |  -  |
| **0** | Error |  -  |

<a id="listClasses"></a>
# **listClasses**
> List&lt;ClassDetails&gt; listClasses(state)

List the classes available for the current user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String state = "active"; // String | Filter the classes by state
    try {
      List<ClassDetails> result = apiInstance.listClasses(state);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#listClasses");
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
| **state** | **String**| Filter the classes by state | [optional] [default to active] [enum: active, inactive, archived] |

### Return type

[**List&lt;ClassDetails&gt;**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of classes |  -  |
| **0** | Error |  -  |

<a id="postSubmissionComment"></a>
# **postSubmissionComment**
> AssignmentSubmissionComment postSubmissionComment(propertyClass, assignment, submission, assignmentSubmissionCommentCreation)

Add a feedback comment to a submission

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    String submission = "submission_example"; // String | Unique identifier of the submission
    AssignmentSubmissionCommentCreation assignmentSubmissionCommentCreation = new AssignmentSubmissionCommentCreation(); // AssignmentSubmissionCommentCreation | 
    try {
      AssignmentSubmissionComment result = apiInstance.postSubmissionComment(propertyClass, assignment, submission, assignmentSubmissionCommentCreation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#postSubmissionComment");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |
| **submission** | **String**| Unique identifier of the submission | |
| **assignmentSubmissionCommentCreation** | [**AssignmentSubmissionCommentCreation**](AssignmentSubmissionCommentCreation.md)|  | |

### Return type

[**AssignmentSubmissionComment**](AssignmentSubmissionComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The comment |  -  |
| **403** | Not granted to access to this submission |  -  |
| **404** | Submission not found |  -  |
| **0** | Error |  -  |

<a id="unarchiveAssignment"></a>
# **unarchiveAssignment**
> Assignment unarchiveAssignment(propertyClass, assignment)

Unarchive the assignment.

Mark the assignment as &#x60;active&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    try {
      Assignment result = apiInstance.unarchiveAssignment(propertyClass, assignment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#unarchiveAssignment");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |

### Return type

[**Assignment**](Assignment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The assignment details |  -  |
| **0** | Error |  -  |

<a id="unarchiveClass"></a>
# **unarchiveClass**
> ClassDetails unarchiveClass(propertyClass)

Unarchive the class

Mark the class as &#x60;active&#x60;. When this course is synchronized with another app, like Google Classroom, this state will be automatically be updated. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    try {
      ClassDetails result = apiInstance.unarchiveClass(propertyClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#unarchiveClass");
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
| **propertyClass** | **String**| Unique identifier of the class | |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The class details |  -  |
| **0** | Error |  -  |

<a id="updateClass"></a>
# **updateClass**
> ClassDetails updateClass(propertyClass, body)

Update the class

Update the meta information of the class 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    ClassUpdate body = new ClassUpdate(); // ClassUpdate | Details of the Class
    try {
      ClassDetails result = apiInstance.updateClass(propertyClass, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#updateClass");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **body** | [**ClassUpdate**](ClassUpdate.md)| Details of the Class | [optional] |

### Return type

[**ClassDetails**](ClassDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The new class details |  -  |
| **0** | Error |  -  |

<a id="updateSubmissionComment"></a>
# **updateSubmissionComment**
> AssignmentSubmissionComment updateSubmissionComment(propertyClass, assignment, submission, comment, assignmentSubmissionCommentCreation)

Update a feedback comment to a submission

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ClassApi apiInstance = new ClassApi(defaultClient);
    String propertyClass = "propertyClass_example"; // String | Unique identifier of the class
    String assignment = "assignment_example"; // String | Unique identifier of the assignment
    String submission = "submission_example"; // String | Unique identifier of the submission
    String comment = "comment_example"; // String | Unique identifier of the comment
    AssignmentSubmissionCommentCreation assignmentSubmissionCommentCreation = new AssignmentSubmissionCommentCreation(); // AssignmentSubmissionCommentCreation | 
    try {
      AssignmentSubmissionComment result = apiInstance.updateSubmissionComment(propertyClass, assignment, submission, comment, assignmentSubmissionCommentCreation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassApi#updateSubmissionComment");
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
| **propertyClass** | **String**| Unique identifier of the class | |
| **assignment** | **String**| Unique identifier of the assignment | |
| **submission** | **String**| Unique identifier of the submission | |
| **comment** | **String**| Unique identifier of the comment | |
| **assignmentSubmissionCommentCreation** | [**AssignmentSubmissionCommentCreation**](AssignmentSubmissionCommentCreation.md)|  | |

### Return type

[**AssignmentSubmissionComment**](AssignmentSubmissionComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The comment |  -  |
| **403** | Not granted to access to this submission |  -  |
| **404** | Submission not found |  -  |
| **0** | Error |  -  |

