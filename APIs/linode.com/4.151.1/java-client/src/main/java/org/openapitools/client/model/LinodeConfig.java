/*
 * Linode API
 * ## Introduction The Linode API provides the ability to programmatically manage the full range of Linode products and services.  This reference is designed to assist application developers and system administrators.  Each endpoint includes descriptions, request syntax, and examples using standard HTTP requests. Response data is returned in JSON format.   This document was generated from our OpenAPI Specification.  See the <a target=\"_top\" href=\"https://www.openapis.org\">OpenAPI website</a> for more information.  <a target=\"_top\" href=\"/docs/api/openapi.yaml\">Download the Linode OpenAPI Specification</a>.   ## Changelog  <a target=\"_top\" href=\"/docs/products/tools/api/release-notes/\">View our Changelog</a> to see release notes on all changes made to our API.  ## Access and Authentication  Some endpoints are publicly accessible without requiring authentication. All endpoints affecting your Account, however, require either a Personal Access Token or OAuth authentication (when using third-party applications).  ### Personal Access Token  The easiest way to access the API is with a Personal Access Token (PAT) generated from the <a target=\"_top\" href=\"https://cloud.linode.com/profile/tokens\">Linode Cloud Manager</a> or the [Create Personal Access Token](/docs/api/profile/#personal-access-token-create) endpoint.  All scopes for the OAuth security model ([defined below](/docs/api/#oauth)) apply to this security model as well.  ### Authentication  | Security Scheme Type: | HTTP | |-----------------------|------| | **HTTP Authorization Scheme** | bearer |  ## OAuth  If you only need to access the Linode API for personal use, we recommend that you create a [personal access token](/docs/api/#personal-access-token). If you're designing an application that can authenticate with an arbitrary Linode user, then you should use the OAuth 2.0 workflows presented in this section.  For a more detailed example of an OAuth 2.0 implementation, see our guide on [How to Create an OAuth App with the Linode Python API Library](/docs/products/tools/api/guides/create-an-oauth-app-with-the-python-api-library/#oauth-2-authentication-exchange).  Before you implement OAuth in your application, you first need to create an OAuth client. You can do this [with the Linode API](/docs/api/account/#oauth-client-create) or [via the Cloud Manager](https://cloud.linode.com/profile/clients):    - When creating the client, you'll supply a `label` and a `redirect_uri` (referred to as the Callback URL in the Cloud Manager).   - The response from this endpoint will give you a `client_id` and a `secret`.   - Clients can be public or private, and are private by default. You can choose to make the client public when it is created.     - A private client is used with applications which can securely store the client secret (that is, the secret returned to you when you first created the client). For example, an application running on a secured server that only the developer has access to would use a private OAuth client. This is also called a confidential client in some OAuth documentation.     - A public client is used with applications where the client secret is not guaranteed to be secure. For example, a native app running on a user's computer may not be able to keep the client secret safe, as a user could potentially inspect the source of the application. So, native apps or apps that run in a user's browser should use a public client.     - Public and private clients follow different workflows, as described below.  ### OAuth Workflow  The OAuth workflow is a series of exchanges between your third-party app and Linode. The workflow is used to authenticate a user before an application can start making API calls on the user's behalf.  Notes:  - With respect to the diagram in [section 1.2 of RFC 6749](https://tools.ietf.org/html/rfc6749#section-1.2), login.linode.com (referred to in this section as the *login server*) is the Resource Owner and the Authorization Server; api.linode.com (referred to here as the *api server*) is the Resource Server. - The OAuth spec refers to the private and public workflows listed below as the [authorization code flow](https://tools.ietf.org/html/rfc6749#section-1.3.1) and [implicit flow](https://tools.ietf.org/html/rfc6749#section-1.3.2).  | PRIVATE WORKFLOW | PUBLIC WORKFLOW | |------------------|------------------| | 1.  The user visits the application's website and is directed to login with Linode. | 1.  The user visits the application's website and is directed to login with Linode. | | 2.  Your application then redirects the user to Linode's [login server](https://login.linode.com) with the client application's `client_id` and requested OAuth `scope`, which should appear in the URL of the login page. | 2.  Your application then redirects the user to Linode's [login server](https://login.linode.com) with the client application's `client_id` and requested OAuth `scope`, which should appear in the URL of the login page. | | 3.  The user logs into the login server with their username and password. | 3.  The user logs into the login server with their username and password. | | 4.  The login server redirects the user to the specificed redirect URL with a temporary authorization `code` (exchange code) in the URL. | 4.  The login server redirects the user back to your application with an OAuth `access_token` embedded in the redirect URL's hash. This is temporary and expires in two hours. No `refresh_token` is issued. Therefore, once the `access_token` expires, a new one will need to be issued by having the user log in again. | | 5.  The application issues a POST request (*see additional details below*) to the login server with the exchange code, `client_id`, and the client application's `client_secret`. | | | 6.  The login server responds to the client application with a new OAuth `access_token` and `refresh_token`. The `access_token` is set to expire in two hours. | | | 7.  The `refresh_token` can be used by contacting the login server with the `client_id`, `client_secret`, `grant_type`, and `refresh_token` to get a new OAuth `access_token` and `refresh_token`. The new `access_token` is good for another two hours, and the new `refresh_token` can be used to extend the session again by this same method (*see additional details below*). | |  #### OAuth Private Workflow - Additional Details  The following information expands on steps 5 through 7 of the private workflow:  Once the user has logged into Linode and you have received an exchange code, you will need to trade that exchange code for an `access_token` and `refresh_token`. You do this by making an HTTP POST request to the following address:  ``` https://login.linode.com/oauth/token ```  Make this request as `application/x-www-form-urlencoded` or as `multipart/form-data` and include the following parameters in the POST body:  | PARAMETER | DESCRIPTION | |-----------|-------------| | client_id | Your app's client ID. | | client_secret | Your app's client secret. | | code | The code you just received from the redirect. |  You'll get a response like this:  ```json {   \"scope\": \"linodes:read_write\",   \"access_token\": \"03d084436a6c91fbafd5c4b20c82e5056a2e9ce1635920c30dc8d81dc7a6665c\",   \"refresh_token\": \"f2ec9712e616fdb5a2a21aa0e88cfadea7502ebc62cf5bd758dbcd65e1803bad\",   \"token_type\": \"bearer\",   \"expires_in\": 7200 } ```  Included in the response is an `access_token`. With this token, you can proceed to make authenticated HTTP requests to the API by adding this header to each request:  ``` Authorization: Bearer 03d084436a6c91fbafd5c4b20c82e5056a2e9ce1635920c30dc8d81dc7a6665c ```  This `access_token` is set to expire in two hours. To refresh access prior to expiration, make another request to the same URL with the following parameters in the POST body:  | PARAMETER | DESCRIPTION | |-----------|-------------| | grant_type | The grant type you're using. Use \"refresh_token\" when refreshing access. | | client_id | Your app's client ID. | | client_secret | Your app's client secret. | | refresh_token | The `refresh_token` received from the previous response. |  You'll get another response with an updated `access_token` and `refresh_token`, which can then be used to refresh access again.  ### OAuth Reference  | Security Scheme Type | OAuth 2.0 | |-----------------------|--------| | **Authorization URL** | `https://login.linode.com/oauth/authorize` | | **Token URL** | `https://login.linode.com/oauth/token` | | **Scopes** | <ul><li>`account:read_only` - Allows access to GET information about your Account.</li><li>`account:read_write` - Allows access to all endpoints related to your Account.</li><li>`databases:read_only` - Allows access to GET Managed Databases on your Account.</li><li>`databases:read_write` - Allows access to all endpoints related to your Managed Databases.</li><li>`domains:read_only` - Allows access to GET Domains on your Account.</li><li>`domains:read_write` - Allows access to all Domain endpoints.</li><li>`events:read_only` - Allows access to GET your Events.</li><li>`events:read_write` - Allows access to all endpoints related to your Events.</li><li>`firewall:read_only` - Allows access to GET information about your Firewalls.</li><li>`firewall:read_write` - Allows access to all Firewall endpoints.</li><li>`images:read_only` - Allows access to GET your Images.</li><li>`images:read_write` - Allows access to all endpoints related to your Images.</li><li>`ips:read_only` - Allows access to GET your ips.</li><li>`ips:read_write` - Allows access to all endpoints related to your ips.</li><li>`linodes:read_only` - Allows access to GET Linodes on your Account.</li><li>`linodes:read_write` - Allow access to all endpoints related to your Linodes.</li><li>`lke:read_only` - Allows access to GET LKE Clusters on your Account.</li><li>`lke:read_write` - Allows access to all endpoints related to LKE Clusters on your Account.</li><li>`longview:read_only` - Allows access to GET your Longview Clients.</li><li>`longview:read_write` - Allows access to all endpoints related to your Longview Clients.</li><li>`nodebalancers:read_only` - Allows access to GET NodeBalancers on your Account.</li><li>`nodebalancers:read_write` - Allows access to all NodeBalancer endpoints.</li><li>`object_storage:read_only` - Allows access to GET information related to your Object Storage.</li><li>`object_storage:read_write` - Allows access to all Object Storage endpoints.</li><li>`stackscripts:read_only` - Allows access to GET your StackScripts.</li><li>`stackscripts:read_write` - Allows access to all endpoints related to your StackScripts.</li><li>`volumes:read_only` - Allows access to GET your Volumes.</li><li>`volumes:read_write` - Allows access to all endpoints related to your Volumes.</li></ul><br/>|  ## Requests  Requests must be made over HTTPS to ensure transactions are encrypted. Data included in requests must be supplied in json format unless otherwise specified in the command description.  The following request methods are supported:  | METHOD  | USAGE | |---------|-------| | GET     | Retrieves data about collections and individual resources. | | POST    | For collections, creates a new resource of that type. Also used to perform actions on action endpoints. | | PUT     | Updates an existing resource. | | DELETE  | Deletes a resource. This is a destructive action. | | HEAD    | Returns only the response header information of a GET request | | OPTIONS | Provides permitted communication options for a command |  ## Responses  ### Response Status Codes  Actions will return one of the following HTTP response status codes:  | STATUS  | DESCRIPTION | |---------|-------------| | 200 OK  | The request was successful. | | 202 Accepted | The request was successful, but processing has not been completed. The response body includes a \"warnings\" array containing the details of incomplete processes. | | 204 No Content | The server successfully fulfilled the request and there is no additional content to send. | | 299 Deprecated | The request was successful, but involved a deprecated endpoint. The response body includes a \"warnings\" array containing warning messages. | | 400 Bad Request | You submitted an invalid request (missing parameters, etc.). | | 401 Unauthorized | You failed to authenticate for this resource. | | 403 Forbidden | You are authenticated, but don't have permission to do this. | | 404 Not Found | The resource you're requesting does not exist. | | 429 Too Many Requests | You've hit a rate limit. | | 500 Internal Server Error | Please [open a Support Ticket](/docs/api/support/#support-ticket-open). |  ### Response Headers  There are many ways to access response header information for individual command URLs, depending on how you are accessing the Linode API. For example, to view HTTP response headers for the `/regions` endpoint when making requests with `curl`, use the `-I` or `--head` option as follows:  ```Shell curl -I https://api.linode.com/v4/regions ```  Responses may include the following headers:  | HEADER | DESCRIPTION | EXAMPLE | |--------|-------------|---------| | Access-Control-Allow-Credentials | Responses to credentialed requests are exposed to frontend JavaScript code. | true | | Access-Control-Allow-Headers | All permissible request headers for this endpoint. | Authorization, Origin, X-Requested-With, Content-Type, Accept, X-Filter | | Access-Control-Allow-Methods | Permissible HTTP methods for this endpoint | HEAD, GET, OPTIONS, POST, PUT, DELETE | | Access-Control-Allow-Origin | Indicates origin access permissions. The wildcard character `*` means any origin can access the resource. | * | | Access-Control-Expose-Headers | Available headers to include in response to cross-origin requests. | X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Status | | Cache-Control | Controls caching in browsers and shared caches such as CDNs. | private, max-age=60, s-maxage=60 | | Content-Security-Policy | Controls which resources are allowed to load. By default, resources do not load. | default-src 'none' | | Content-Type | All responses are in json format. | application/json | | Content-Warning | A message containing instructions for successful requests that were not able to be completed. | Please contact support for assistance. | | Retry-After | The remaining time in seconds until the current [rate limit](#rate-limiting) window resets. | 60 | | Strict-Transport-Security | Enforces HTTPS-only access until the returned time in seconds. | max-age=31536000 | | Vary | Optional request headers that affected the response content. | Authorization, X-Filter | | X-Accepted-OAuth-Scopes | Required [scopes](#oauth-reference) for accessing the requested command. | linodes:read_only | | X-Customer-UUID | A unique identifier for the account owning the the [personal access token](#personal-access-token) that was used for the request. | ABCDEF01-3456-789A-BCDEF0123456789A | | X-OAuth-Scopes | Allowed [scopes](#oauth-reference) associated with the [personal access token](#personal-access-token) that was used for the request. A value of `*` indicates read/write access for all scope categories. | images:read_write linodes:read_only | | X-RateLimit-Limit | The maximum number of permitted requests during the [rate limit](#rate-limiting) window for this endpoint. | 800 | | X-RateLimit-Remaining | The remaining number of permitted requests in the current [rate limit](#rate-limiting) window. | 798 | | X-RateLimit-Reset | The time when the current [rate limit](#rate-limiting) window rests in UTC epoch seconds. | 1674747739 | | X-Spec-Version | The current API version that handled the request. | 4.150.0 |  ## Errors  Success is indicated via <a href=\"https://en.wikipedia.org/wiki/List_of_HTTP_status_codes\" target=\"_top\">Standard HTTP status codes</a>. `2xx` codes indicate success, `4xx` codes indicate a request error, and `5xx` errors indicate a server error. A request error might be an invalid input, a required parameter being omitted, or a malformed request. A server error means something went wrong processing your request. If this occurs, please [open a Support Ticket](/docs/api/support/#support-ticket-open) and let us know. Though errors are logged and we work quickly to resolve issues, opening a ticket and providing us with reproducable steps and data is always helpful.  The `errors` field is an array of the things that went wrong with your request. We will try to include as many of the problems in the response as possible, but it's conceivable that fixing these errors and resubmitting may result in new errors coming back once we are able to get further along in the process of handling your request.  Within each error object, the `field` parameter will be included if the error pertains to a specific field in the JSON you've submitted. This will be omitted if there is no relevant field. The `reason` is a human-readable explanation of the error, and will always be included.  ## Pagination  Resource lists are always paginated. The response will look similar to this:  ```json {     \"data\": [ ... ],     \"page\": 1,     \"pages\": 3,     \"results\": 300 } ```  * Pages start at 1. You may retrieve a specific page of results by adding `?page=x` to your URL (for example, `?page=4`). If the value of `page` exceeds `2^64/page_size`, the last possible page will be returned.   * Page sizes default to 100, and can be set to return between 25 and 500. Page size can be set using `?page_size=x`.  ## Filtering and Sorting  Collections are searchable by fields they include, marked in the spec as `x-linode-filterable: true`. Filters are passed in the `X-Filter` header and are formatted as JSON objects. Here is a request call for Linode Types in our \"standard\" class:  ```Shell curl \"https://api.linode.com/v4/linode/types\" \\   -H 'X-Filter: { \"class\": \"standard\" }' ```  The filter object's keys are the keys of the object you're filtering, and the values are accepted values. You can add multiple filters by including more than one key. For example, filtering for \"standard\" Linode Types that offer one vcpu:  ```Shell  curl \"https://api.linode.com/v4/linode/types\" \\   -H 'X-Filter: { \"class\": \"standard\", \"vcpus\": 1 }' ```  In the above example, both filters are combined with an \"and\" operation. However, if you wanted either Types with one vcpu or Types in our \"standard\" class, you can add an operator:   ```Shell curl \"https://api.linode.com/v4/linode/types\" \\   -H 'X-Filter: { \"+or\": [ { \"vcpus\": 1 }, { \"class\": \"standard\" } ] }' ```  Each filter in the `+or` array is its own filter object, and all conditions in it are combined with an \"and\" operation as they were in the previous example.  Other operators are also available. Operators are keys of a Filter JSON object. Their value must be of the appropriate type, and they are evaluated as described below:  | OPERATOR | TYPE   | DESCRIPTION                       | |----------|--------|-----------------------------------| | +and     | array  | All conditions must be true.       | | +or      | array  | One condition must be true.        | | +gt      | number | Value must be greater than number. | | +gte     | number | Value must be greater than or equal to number. | | +lt      | number | Value must be less than number. | | +lte     | number | Value must be less than or equal to number. | | +contains | string | Given string must be in the value. | | +neq      | string | Does not equal the value.          | | +order_by | string | Attribute to order the results by - must be filterable. | | +order    | string | Either \"asc\" or \"desc\". Defaults to \"asc\". Requires `+order_by`. |  For example, filtering for [Linode Types](/docs/api/linode-types/) that offer memory equal to or higher than 61440:  ```Shell curl \"https://api.linode.com/v4/linode/types\" \\   -H '     X-Filter: {       \"memory\": {         \"+gte\": 61440       }     }' ```  You can combine and nest operators to construct arbitrarily-complex queries. For example, give me all [Linode Types](/docs/api/linode-types/) which are either `standard` or `highmem` class, or have between 12 and 20 vcpus:  ```Shell curl \"https://api.linode.com/v4/linode/types\" \\   -H '     X-Filter: {       \"+or\": [         {           \"+or\": [             {               \"class\": \"standard\"             },             {               \"class\": \"highmem\"             }           ]         },         {           \"+and\": [             {               \"vcpus\": {                 \"+gte\": 12               }             },             {               \"vcpus\": {                 \"+lte\": 20               }             }           ]         }       ]     }' ``` ## Time Values  All times returned by the API are in UTC, regardless of the timezone configured within your user's profile (see `timezone` property within [Profile View](/docs/api/profile/#profile-view__responses)).  ## Rate Limiting  Rate limits on API requests help maintain the health and stability of the Linode API. Accordingly, every endpoint of the Linode API applies a rate limit on a per user basis as determined by OAuth token for authenticated requests or IP address for public endpoints.  Each rate limit consists of a total number of requests and a time window. For example, if an endpoint has a rate limit of 800 requests per minute, then up to 800 requests over a one minute window are permitted. Subsequent requests to an endpoint after hitting a rate limit return a 429 error. You can successfully remake requests to that endpoint after the rate limit window resets.  ### Linode APIv4 Rate Limits  With the Linode API, you can generally make up to 1,600 general API requests every two minutes. Additionally, all endpoints have a rate limit of 800 requests per minute unless otherwise specified below.  **Note:** There may be rate limiting applied at other levels outside of the API, for example, at the load balancer.  Creating Linodes has a dedicated rate limit of 10 requests per 30 seconds. That endpoint is:  * [Linode Create](/docs/api/linode-instances/#linode-create)  `/stats` endpoints have their own dedicated rate limits of 100 requests per minute. These endpoints are:  * [View Linode Statistics](/docs/api/linode-instances/#linode-statistics-view) * [View Linode Statistics (year/month)](/docs/api/linode-instances/#statistics-yearmonth-view) * [View NodeBalancer Statistics](/docs/api/nodebalancers/#nodebalancer-statistics-view) * [List Managed Stats](/docs/api/managed/#managed-stats-list)  Object Storage endpoints have a dedicated rate limit of 750 requests per second. The Object Storage endpoints are:  * [Object Storage Endpoints](/docs/api/object-storage/)  Opening Support Tickets has a dedicated rate limit of 2 requests per minute. That endpoint is:  * [Open Support Ticket](/docs/api/support/#support-ticket-open)  Accepting Service Transfers has a dedicated rate limit of 2 requests per minute. That endpoint is:  * [Service Transfer Accept](/docs/api/account/#service-transfer-accept)  ### Rate Limit HTTP Response Headers  The Linode API includes the following HTTP response headers which are designed to help you avoid hitting rate limits which might disrupt your applications:  * **X-RateLimit-Limit**: The maximum number of permitted requests during the rate limit window for this endpoint. * **X-RateLimit-Remaining**: The remaining number of permitted requests in the current rate limit window. * **X-RateLimit-Reset**: The time when the current rate limit window rests in UTC epoch seconds. * **Retry-After**: The remaining time in seconds until the current rate limit window resets.  ## CLI (Command Line Interface)  The <a href=\"https://github.com/linode/linode-cli\" target=\"_top\">Linode CLI</a> allows you to easily work with the API using intuitive and simple syntax. It requires a [Personal Access Token](/docs/api/#personal-access-token) for authentication, and gives you access to all of the features and functionality of the Linode API that are documented here with CLI examples.  Endpoints that do not have CLI examples are currently unavailable through the CLI, but can be accessed via other methods such as Shell commands and other third-party applications. 
 *
 * The version of the OpenAPI document: 4.151.1
 * Contact: support@linode.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Devices;
import org.openapitools.client.model.LinodeConfigHelpers;
import org.openapitools.client.model.LinodeConfigInterface;
import org.openapitools.jackson.nullable.JsonNullable;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * LinodeConfig
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:42.346741-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LinodeConfig {
  public static final String SERIALIZED_NAME_COMMENTS = "comments";
  @SerializedName(SERIALIZED_NAME_COMMENTS)
  private String comments;

  public static final String SERIALIZED_NAME_DEVICES = "devices";
  @SerializedName(SERIALIZED_NAME_DEVICES)
  private Devices devices;

  public static final String SERIALIZED_NAME_HELPERS = "helpers";
  @SerializedName(SERIALIZED_NAME_HELPERS)
  private LinodeConfigHelpers helpers;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_INTERFACES = "interfaces";
  @SerializedName(SERIALIZED_NAME_INTERFACES)
  private List<LinodeConfigInterface> interfaces = new ArrayList<>();

  public static final String SERIALIZED_NAME_KERNEL = "kernel";
  @SerializedName(SERIALIZED_NAME_KERNEL)
  private String kernel;

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public static final String SERIALIZED_NAME_MEMORY_LIMIT = "memory_limit";
  @SerializedName(SERIALIZED_NAME_MEMORY_LIMIT)
  private Integer memoryLimit;

  public static final String SERIALIZED_NAME_ROOT_DEVICE = "root_device";
  @SerializedName(SERIALIZED_NAME_ROOT_DEVICE)
  private String rootDevice;

  /**
   * Defines the state of your Linode after booting. Defaults to &#x60;default&#x60;. 
   */
  @JsonAdapter(RunLevelEnum.Adapter.class)
  public enum RunLevelEnum {
    DEFAULT("default"),
    
    SINGLE("single"),
    
    BINBASH("binbash");

    private String value;

    RunLevelEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RunLevelEnum fromValue(String value) {
      for (RunLevelEnum b : RunLevelEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RunLevelEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RunLevelEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RunLevelEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RunLevelEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RunLevelEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RUN_LEVEL = "run_level";
  @SerializedName(SERIALIZED_NAME_RUN_LEVEL)
  private RunLevelEnum runLevel;

  /**
   * Controls the virtualization mode. Defaults to &#x60;paravirt&#x60;. * &#x60;paravirt&#x60; is suitable for most cases. Linodes running in paravirt mode   share some qualities with the host, ultimately making it run faster since   there is less transition between it and the host. * &#x60;fullvirt&#x60; affords more customization, but is slower because 100% of the VM   is virtualized. 
   */
  @JsonAdapter(VirtModeEnum.Adapter.class)
  public enum VirtModeEnum {
    PARAVIRT("paravirt"),
    
    FULLVIRT("fullvirt");

    private String value;

    VirtModeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static VirtModeEnum fromValue(String value) {
      for (VirtModeEnum b : VirtModeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<VirtModeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final VirtModeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public VirtModeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return VirtModeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      VirtModeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_VIRT_MODE = "virt_mode";
  @SerializedName(SERIALIZED_NAME_VIRT_MODE)
  private VirtModeEnum virtMode;

  public LinodeConfig() {
  }

  public LinodeConfig(
     Integer id
  ) {
    this();
    this.id = id;
  }

  public LinodeConfig comments(String comments) {
    this.comments = comments;
    return this;
  }

  /**
   * Optional field for arbitrary User comments on this Config.
   * @return comments
   */
  @javax.annotation.Nullable
  public String getComments() {
    return comments;
  }

  public void setComments(String comments) {
    this.comments = comments;
  }


  public LinodeConfig devices(Devices devices) {
    this.devices = devices;
    return this;
  }

  /**
   * Get devices
   * @return devices
   */
  @javax.annotation.Nullable
  public Devices getDevices() {
    return devices;
  }

  public void setDevices(Devices devices) {
    this.devices = devices;
  }


  public LinodeConfig helpers(LinodeConfigHelpers helpers) {
    this.helpers = helpers;
    return this;
  }

  /**
   * Get helpers
   * @return helpers
   */
  @javax.annotation.Nullable
  public LinodeConfigHelpers getHelpers() {
    return helpers;
  }

  public void setHelpers(LinodeConfigHelpers helpers) {
    this.helpers = helpers;
  }


  /**
   * The ID of this Config.
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public LinodeConfig interfaces(List<LinodeConfigInterface> interfaces) {
    this.interfaces = interfaces;
    return this;
  }

  public LinodeConfig addInterfacesItem(LinodeConfigInterface interfacesItem) {
    if (this.interfaces == null) {
      this.interfaces = new ArrayList<>();
    }
    this.interfaces.add(interfacesItem);
    return this;
  }

  /**
   * An array of Network Interfaces to add to this Linode&#39;s Configuration Profile.  Up to three interface objects can be entered in this array. The position in the array determines the interface to which the settings apply:  - First/0:  eth0 - Second/1: eth1 - Third/2:  eth2  When updating a Linode&#39;s interfaces, *each interface must be redefined*. An empty interfaces array results in a default public interface configuration only.  If no public interface is configured, public IP addresses are still assigned to the Linode but will not be usable without manual configuration.  **Note:** Changes to Linode interface configurations can be enabled by rebooting the Linode.  **Note:** Only Next Generation Network (NGN) data centers support VLANs. Use the Regions ([/regions](/docs/api/regions/)) endpoint to view the capabilities of data center regions. If a VLAN is attached to your Linode and you attempt to migrate or clone it to a non-NGN data center, the migration or cloning will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support.  **Note:** See the [VLANs Overview](/docs/products/networking/vlans/#technical-specifications) guide to view additional specifications and limitations. 
   * @return interfaces
   */
  @javax.annotation.Nullable
  public List<LinodeConfigInterface> getInterfaces() {
    return interfaces;
  }

  public void setInterfaces(List<LinodeConfigInterface> interfaces) {
    this.interfaces = interfaces;
  }


  public LinodeConfig kernel(String kernel) {
    this.kernel = kernel;
    return this;
  }

  /**
   * A Kernel ID to boot a Linode with. Defaults to \&quot;linode/latest-64bit\&quot;.
   * @return kernel
   */
  @javax.annotation.Nullable
  public String getKernel() {
    return kernel;
  }

  public void setKernel(String kernel) {
    this.kernel = kernel;
  }


  public LinodeConfig label(String label) {
    this.label = label;
    return this;
  }

  /**
   * The Config&#39;s label is for display purposes only. 
   * @return label
   */
  @javax.annotation.Nullable
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }


  public LinodeConfig memoryLimit(Integer memoryLimit) {
    this.memoryLimit = memoryLimit;
    return this;
  }

  /**
   * Defaults to the total RAM of the Linode. 
   * @return memoryLimit
   */
  @javax.annotation.Nullable
  public Integer getMemoryLimit() {
    return memoryLimit;
  }

  public void setMemoryLimit(Integer memoryLimit) {
    this.memoryLimit = memoryLimit;
  }


  public LinodeConfig rootDevice(String rootDevice) {
    this.rootDevice = rootDevice;
    return this;
  }

  /**
   * The root device to boot. * If no value or an invalid value is provided, root device will default to &#x60;/dev/sda&#x60;. * If the device specified at the root device location is not mounted, the Linode will not boot until a device is mounted. 
   * @return rootDevice
   */
  @javax.annotation.Nullable
  public String getRootDevice() {
    return rootDevice;
  }

  public void setRootDevice(String rootDevice) {
    this.rootDevice = rootDevice;
  }


  public LinodeConfig runLevel(RunLevelEnum runLevel) {
    this.runLevel = runLevel;
    return this;
  }

  /**
   * Defines the state of your Linode after booting. Defaults to &#x60;default&#x60;. 
   * @return runLevel
   */
  @javax.annotation.Nullable
  public RunLevelEnum getRunLevel() {
    return runLevel;
  }

  public void setRunLevel(RunLevelEnum runLevel) {
    this.runLevel = runLevel;
  }


  public LinodeConfig virtMode(VirtModeEnum virtMode) {
    this.virtMode = virtMode;
    return this;
  }

  /**
   * Controls the virtualization mode. Defaults to &#x60;paravirt&#x60;. * &#x60;paravirt&#x60; is suitable for most cases. Linodes running in paravirt mode   share some qualities with the host, ultimately making it run faster since   there is less transition between it and the host. * &#x60;fullvirt&#x60; affords more customization, but is slower because 100% of the VM   is virtualized. 
   * @return virtMode
   */
  @javax.annotation.Nullable
  public VirtModeEnum getVirtMode() {
    return virtMode;
  }

  public void setVirtMode(VirtModeEnum virtMode) {
    this.virtMode = virtMode;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LinodeConfig linodeConfig = (LinodeConfig) o;
    return Objects.equals(this.comments, linodeConfig.comments) &&
        Objects.equals(this.devices, linodeConfig.devices) &&
        Objects.equals(this.helpers, linodeConfig.helpers) &&
        Objects.equals(this.id, linodeConfig.id) &&
        Objects.equals(this.interfaces, linodeConfig.interfaces) &&
        Objects.equals(this.kernel, linodeConfig.kernel) &&
        Objects.equals(this.label, linodeConfig.label) &&
        Objects.equals(this.memoryLimit, linodeConfig.memoryLimit) &&
        Objects.equals(this.rootDevice, linodeConfig.rootDevice) &&
        Objects.equals(this.runLevel, linodeConfig.runLevel) &&
        Objects.equals(this.virtMode, linodeConfig.virtMode);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(comments, devices, helpers, id, interfaces, kernel, label, memoryLimit, rootDevice, runLevel, virtMode);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LinodeConfig {\n");
    sb.append("    comments: ").append(toIndentedString(comments)).append("\n");
    sb.append("    devices: ").append(toIndentedString(devices)).append("\n");
    sb.append("    helpers: ").append(toIndentedString(helpers)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    interfaces: ").append(toIndentedString(interfaces)).append("\n");
    sb.append("    kernel: ").append(toIndentedString(kernel)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
    sb.append("    memoryLimit: ").append(toIndentedString(memoryLimit)).append("\n");
    sb.append("    rootDevice: ").append(toIndentedString(rootDevice)).append("\n");
    sb.append("    runLevel: ").append(toIndentedString(runLevel)).append("\n");
    sb.append("    virtMode: ").append(toIndentedString(virtMode)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("comments");
    openapiFields.add("devices");
    openapiFields.add("helpers");
    openapiFields.add("id");
    openapiFields.add("interfaces");
    openapiFields.add("kernel");
    openapiFields.add("label");
    openapiFields.add("memory_limit");
    openapiFields.add("root_device");
    openapiFields.add("run_level");
    openapiFields.add("virt_mode");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LinodeConfig
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LinodeConfig.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LinodeConfig is not found in the empty JSON string", LinodeConfig.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LinodeConfig.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LinodeConfig` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("comments") != null && !jsonObj.get("comments").isJsonNull()) && !jsonObj.get("comments").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comments` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comments").toString()));
      }
      // validate the optional field `devices`
      if (jsonObj.get("devices") != null && !jsonObj.get("devices").isJsonNull()) {
        Devices.validateJsonElement(jsonObj.get("devices"));
      }
      // validate the optional field `helpers`
      if (jsonObj.get("helpers") != null && !jsonObj.get("helpers").isJsonNull()) {
        LinodeConfigHelpers.validateJsonElement(jsonObj.get("helpers"));
      }
      if (jsonObj.get("interfaces") != null && !jsonObj.get("interfaces").isJsonNull()) {
        JsonArray jsonArrayinterfaces = jsonObj.getAsJsonArray("interfaces");
        if (jsonArrayinterfaces != null) {
          // ensure the json data is an array
          if (!jsonObj.get("interfaces").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `interfaces` to be an array in the JSON string but got `%s`", jsonObj.get("interfaces").toString()));
          }

          // validate the optional field `interfaces` (array)
          for (int i = 0; i < jsonArrayinterfaces.size(); i++) {
            LinodeConfigInterface.validateJsonElement(jsonArrayinterfaces.get(i));
          };
        }
      }
      if ((jsonObj.get("kernel") != null && !jsonObj.get("kernel").isJsonNull()) && !jsonObj.get("kernel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `kernel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("kernel").toString()));
      }
      if ((jsonObj.get("label") != null && !jsonObj.get("label").isJsonNull()) && !jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
      if ((jsonObj.get("root_device") != null && !jsonObj.get("root_device").isJsonNull()) && !jsonObj.get("root_device").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `root_device` to be a primitive type in the JSON string but got `%s`", jsonObj.get("root_device").toString()));
      }
      if ((jsonObj.get("run_level") != null && !jsonObj.get("run_level").isJsonNull()) && !jsonObj.get("run_level").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `run_level` to be a primitive type in the JSON string but got `%s`", jsonObj.get("run_level").toString()));
      }
      // validate the optional field `run_level`
      if (jsonObj.get("run_level") != null && !jsonObj.get("run_level").isJsonNull()) {
        RunLevelEnum.validateJsonElement(jsonObj.get("run_level"));
      }
      if ((jsonObj.get("virt_mode") != null && !jsonObj.get("virt_mode").isJsonNull()) && !jsonObj.get("virt_mode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `virt_mode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("virt_mode").toString()));
      }
      // validate the optional field `virt_mode`
      if (jsonObj.get("virt_mode") != null && !jsonObj.get("virt_mode").isJsonNull()) {
        VirtModeEnum.validateJsonElement(jsonObj.get("virt_mode"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LinodeConfig.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LinodeConfig' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LinodeConfig> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LinodeConfig.class));

       return (TypeAdapter<T>) new TypeAdapter<LinodeConfig>() {
           @Override
           public void write(JsonWriter out, LinodeConfig value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LinodeConfig read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LinodeConfig given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LinodeConfig
   * @throws IOException if the JSON string is invalid with respect to LinodeConfig
   */
  public static LinodeConfig fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LinodeConfig.class);
  }

  /**
   * Convert an instance of LinodeConfig to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

