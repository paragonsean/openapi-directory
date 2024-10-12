# ContentBlocksApi

All URIs are relative to *https://rest.iad-01.braze.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listAvailableContentBlocks_0**](ContentBlocksApi.md#listAvailableContentBlocks_0) | **GET** /content_blocks/list | List Available Content Blocks |
| [**seeContentBlockInformation_0**](ContentBlocksApi.md#seeContentBlockInformation_0) | **GET** /content_blocks/info | See Content Block Information |


<a id="listAvailableContentBlocks_0"></a>
# **listAvailableContentBlocks_0**
> listAvailableContentBlocks_0(modifiedAfter, modifiedBefore, limit, offset)

List Available Content Blocks

This endpoint will list existing Content Block information.  ### Successful Response Properties &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR_REST_API_KEY {   \&quot;count\&quot;: \&quot;integer\&quot;,   \&quot;content_blocks\&quot;: [     {       \&quot;content_block_id\&quot;: \&quot;string\&quot;,       \&quot;name\&quot;: \&quot;string\&quot;,       \&quot;content_type\&quot;: \&quot;html or text\&quot;,       \&quot;liquid_tag\&quot;: \&quot;string\&quot;,       \&quot;inclusion_count\&quot; : \&quot;integer\&quot;,       \&quot;created_at\&quot;: \&quot;time-in-iso\&quot;,       \&quot;last_edited\&quot;: \&quot;time-in-iso\&quot;,       \&quot;tags\&quot; : \&quot;array of strings\&quot;     }   ] } &#x60;&#x60;&#x60;  ### Possible Errors - &#x60;Modified after time is invalid.&#x60; The date you have provided is not a valid or parsable date. Please reformat this value as a string in ISO 8601 format (&#x60;yyyy-mm-ddThh:mm:ss.ffffff&#x60;).  - &#x60;Modified before time is invalid.&#x60; The date you have provided is not a valid or parsable date. Please reformat this value as a string in ISO 8601 format (&#x60;yyyy-mm-ddThh:mm:ss.ffffff&#x60;).  - &#x60;Modified after time must be earlier than or the same as modified before time.&#x60;  - &#x60;Content Block number limit is invalid.&#x60; The &#x60;limit&#x60; parameter must be an integer (positive number) greater than 0.  - &#x60;Content Block number limit must be greater than 0.&#x60; The &#x60;limit&#x60; parameter must be an integer (positive number) greater than 0.  - &#x60;Content Block number limit exceeds maximum of 1000.&#x60; The &#x60;limit&#x60; parameter must be an integer (positive number) greater than 0.  - &#x60;Offset is invalid.&#x60; The &#x60;offset&#x60; parameter must be an integer (positive number) greater than 0.  - &#x60;Offset must be greater than 0.&#x60; The &#x60;offset&#x60; parameter must be an integer (positive number) greater than 0.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentBlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    ContentBlocksApi apiInstance = new ContentBlocksApi(defaultClient);
    String modifiedAfter = "2020-01-01T01:01:01.000000"; // String | (Optional) String in ISO 8601  Retrieve only content blocks updated at or after the given time.
    String modifiedBefore = "2020-02-01T01:01:01.000000"; // String | (Optional) String in ISO 8601  Retrieve only content blocks updated at or before the given time.
    String limit = "100"; // String | (Optional) Positive Number  Maximum number of content blocks to retrieve, default to 100 if not provided, maximum acceptable value is 1000.
    String offset = "1"; // String | (Optional) Positive Number  Number of content blocks to skip before returning rest of the templates that fit the search criteria.
    try {
      apiInstance.listAvailableContentBlocks_0(modifiedAfter, modifiedBefore, limit, offset);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentBlocksApi#listAvailableContentBlocks_0");
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
| **modifiedAfter** | **String**| (Optional) String in ISO 8601  Retrieve only content blocks updated at or after the given time. | [optional] |
| **modifiedBefore** | **String**| (Optional) String in ISO 8601  Retrieve only content blocks updated at or before the given time. | [optional] |
| **limit** | **String**| (Optional) Positive Number  Maximum number of content blocks to retrieve, default to 100 if not provided, maximum acceptable value is 1000. | [optional] |
| **offset** | **String**| (Optional) Positive Number  Number of content blocks to skip before returning rest of the templates that fit the search criteria. | [optional] |

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
| **200** |  |  -  |

<a id="seeContentBlockInformation_0"></a>
# **seeContentBlockInformation_0**
> seeContentBlockInformation_0(contentBlockId, includeInclusionData)

See Content Block Information

This endpoint will call information for an existing Content Block.  ### Successful Response Properties &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR_REST_API_KEY {   \&quot;content_block_id\&quot;: \&quot;string\&quot;,   \&quot;name\&quot;: \&quot;string\&quot;,   \&quot;content\&quot;: \&quot;string\&quot;,   \&quot;description\&quot;: \&quot;string\&quot;,   \&quot;content_type\&quot;: \&quot;html or text\&quot;,   \&quot;tags\&quot;:  \&quot;array of strings\&quot;,   \&quot;created_at\&quot;: \&quot;time-in-iso\&quot;,   \&quot;last_edited\&quot;: \&quot;time-in-iso\&quot;,   \&quot;inclusion_count\&quot; : \&quot;integer\&quot;,   \&quot;message\&quot;: \&quot;success\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - &#x60;Content Block ID cannot be blank.&#x60; - A Content Block has not been listed or is not encapsulated in quotes.  - &#x60;Content Block ID is invalid for this App Group.&#x60; - This Content Block does not exist or is in a different company account or app group.  - &#x60;Content Block has been deleted - content not available.&#x60; - This Content Block, though it may have existed earlier, has been deleted.  - &#x60;Include Inclusion Data - error&#x60; - One of true or false is not provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentBlocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    ContentBlocksApi apiInstance = new ContentBlocksApi(defaultClient);
    String contentBlockId = "{{content_block_id}}"; // String | (Required) String  The Content Block ID. This can be found by either listing Content Block information or going to the Developer Console, then API Settings, then scrolling to the bottom and searching for your Content Block API Identifier.
    String includeInclusionData = "false"; // String | (Optional) Boolean  When set to ‘true’, the API returns back the Message Variation API ID of Campaigns and Canvases where this content block is included, to be used in subsequent calls. The results exclude archived or deleted Campaigns or Canvases.
    try {
      apiInstance.seeContentBlockInformation_0(contentBlockId, includeInclusionData);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentBlocksApi#seeContentBlockInformation_0");
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
| **contentBlockId** | **String**| (Required) String  The Content Block ID. This can be found by either listing Content Block information or going to the Developer Console, then API Settings, then scrolling to the bottom and searching for your Content Block API Identifier. | [optional] |
| **includeInclusionData** | **String**| (Optional) Boolean  When set to ‘true’, the API returns back the Message Variation API ID of Campaigns and Canvases where this content block is included, to be used in subsequent calls. The results exclude archived or deleted Campaigns or Canvases. | [optional] |

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
| **200** |  |  -  |

