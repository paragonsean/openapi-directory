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
import java.util.Arrays;
import org.openapitools.client.model.NodeBalancerConfigNodesStatus;
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
 * A NodeBalancer config represents the configuration of this NodeBalancer on a single port.  For example, a NodeBalancer Config on port 80 would typically represent how this NodeBalancer response to HTTP requests.  NodeBalancer configs have a list of backends, called \&quot;nodes,\&quot; that they forward requests between based on their configuration. 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:42.346741-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NodeBalancerConfig {
  /**
   * What algorithm this NodeBalancer should use for routing traffic to backends. 
   */
  @JsonAdapter(AlgorithmEnum.Adapter.class)
  public enum AlgorithmEnum {
    ROUNDROBIN("roundrobin"),
    
    LEASTCONN("leastconn"),
    
    SOURCE("source");

    private String value;

    AlgorithmEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AlgorithmEnum fromValue(String value) {
      for (AlgorithmEnum b : AlgorithmEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AlgorithmEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AlgorithmEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AlgorithmEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AlgorithmEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AlgorithmEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ALGORITHM = "algorithm";
  @SerializedName(SERIALIZED_NAME_ALGORITHM)
  private AlgorithmEnum algorithm = AlgorithmEnum.ROUNDROBIN;

  /**
   * The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. * If &#x60;none&#x60; no check is performed. * &#x60;connection&#x60; requires only a connection to the backend to succeed. * &#x60;http&#x60; and &#x60;http_body&#x60; rely on the backend serving HTTP, and that   the response returned matches what is expected. 
   */
  @JsonAdapter(CheckEnum.Adapter.class)
  public enum CheckEnum {
    NONE("none"),
    
    CONNECTION("connection"),
    
    HTTP("http"),
    
    HTTP_BODY("http_body");

    private String value;

    CheckEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CheckEnum fromValue(String value) {
      for (CheckEnum b : CheckEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CheckEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CheckEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CheckEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CheckEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CheckEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CHECK = "check";
  @SerializedName(SERIALIZED_NAME_CHECK)
  private CheckEnum check = CheckEnum.NONE;

  public static final String SERIALIZED_NAME_CHECK_ATTEMPTS = "check_attempts";
  @SerializedName(SERIALIZED_NAME_CHECK_ATTEMPTS)
  private Integer checkAttempts = 3;

  public static final String SERIALIZED_NAME_CHECK_BODY = "check_body";
  @SerializedName(SERIALIZED_NAME_CHECK_BODY)
  private String checkBody;

  public static final String SERIALIZED_NAME_CHECK_INTERVAL = "check_interval";
  @SerializedName(SERIALIZED_NAME_CHECK_INTERVAL)
  private Integer checkInterval = 31;

  public static final String SERIALIZED_NAME_CHECK_PASSIVE = "check_passive";
  @SerializedName(SERIALIZED_NAME_CHECK_PASSIVE)
  private Boolean checkPassive = true;

  public static final String SERIALIZED_NAME_CHECK_PATH = "check_path";
  @SerializedName(SERIALIZED_NAME_CHECK_PATH)
  private String checkPath;

  public static final String SERIALIZED_NAME_CHECK_TIMEOUT = "check_timeout";
  @SerializedName(SERIALIZED_NAME_CHECK_TIMEOUT)
  private Integer checkTimeout = 30;

  /**
   * What ciphers to use for SSL connections served by this NodeBalancer.  * &#x60;legacy&#x60; is considered insecure and should only be used if necessary. 
   */
  @JsonAdapter(CipherSuiteEnum.Adapter.class)
  public enum CipherSuiteEnum {
    RECOMMENDED("recommended"),
    
    LEGACY("legacy");

    private String value;

    CipherSuiteEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CipherSuiteEnum fromValue(String value) {
      for (CipherSuiteEnum b : CipherSuiteEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CipherSuiteEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CipherSuiteEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CipherSuiteEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CipherSuiteEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CipherSuiteEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CIPHER_SUITE = "cipher_suite";
  @SerializedName(SERIALIZED_NAME_CIPHER_SUITE)
  private CipherSuiteEnum cipherSuite = CipherSuiteEnum.RECOMMENDED;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_NODEBALANCER_ID = "nodebalancer_id";
  @SerializedName(SERIALIZED_NAME_NODEBALANCER_ID)
  private Integer nodebalancerId;

  public static final String SERIALIZED_NAME_NODES_STATUS = "nodes_status";
  @SerializedName(SERIALIZED_NAME_NODES_STATUS)
  private NodeBalancerConfigNodesStatus nodesStatus;

  public static final String SERIALIZED_NAME_PORT = "port";
  @SerializedName(SERIALIZED_NAME_PORT)
  private Integer port = 80;

  /**
   * The protocol this port is configured to serve.  * The &#x60;http&#x60; and &#x60;tcp&#x60; protocols do not support &#x60;ssl_cert&#x60; and &#x60;ssl_key&#x60;.  * The &#x60;https&#x60; protocol is mutually required with &#x60;ssl_cert&#x60; and &#x60;ssl_key&#x60;.  Review our guide on [Available Protocols](/docs/products/networking/nodebalancers/guides/protocols/) for information on protocol features. 
   */
  @JsonAdapter(ProtocolEnum.Adapter.class)
  public enum ProtocolEnum {
    HTTP("http"),
    
    HTTPS("https"),
    
    TCP("tcp");

    private String value;

    ProtocolEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProtocolEnum fromValue(String value) {
      for (ProtocolEnum b : ProtocolEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProtocolEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProtocolEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProtocolEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProtocolEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProtocolEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROTOCOL = "protocol";
  @SerializedName(SERIALIZED_NAME_PROTOCOL)
  private ProtocolEnum protocol = ProtocolEnum.HTTP;

  /**
   * ProxyProtocol is a TCP extension that sends initial TCP connection information such as source/destination IPs and ports to backend devices. This information would be lost otherwise. Backend devices must be configured to work with ProxyProtocol if enabled.  * If ommited, or set to &#x60;none&#x60;, the NodeBalancer doesn&#39;t send any auxilary data over TCP connections. This is the default. * If set to &#x60;v1&#x60;, the human-readable header format (Version 1) is used. Requires &#x60;tcp&#x60; protocol. * If set to &#x60;v2&#x60;, the binary header format (Version 2) is used. Requires &#x60;tcp&#x60; protocol. 
   */
  @JsonAdapter(ProxyProtocolEnum.Adapter.class)
  public enum ProxyProtocolEnum {
    NONE("none"),
    
    V1("v1"),
    
    V2("v2");

    private String value;

    ProxyProtocolEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProxyProtocolEnum fromValue(String value) {
      for (ProxyProtocolEnum b : ProxyProtocolEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProxyProtocolEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProxyProtocolEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProxyProtocolEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProxyProtocolEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProxyProtocolEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROXY_PROTOCOL = "proxy_protocol";
  @SerializedName(SERIALIZED_NAME_PROXY_PROTOCOL)
  private ProxyProtocolEnum proxyProtocol = ProxyProtocolEnum.NONE;

  public static final String SERIALIZED_NAME_SSL_CERT = "ssl_cert";
  @SerializedName(SERIALIZED_NAME_SSL_CERT)
  private String sslCert;

  public static final String SERIALIZED_NAME_SSL_COMMONNAME = "ssl_commonname";
  @SerializedName(SERIALIZED_NAME_SSL_COMMONNAME)
  private String sslCommonname;

  public static final String SERIALIZED_NAME_SSL_FINGERPRINT = "ssl_fingerprint";
  @SerializedName(SERIALIZED_NAME_SSL_FINGERPRINT)
  private String sslFingerprint;

  public static final String SERIALIZED_NAME_SSL_KEY = "ssl_key";
  @SerializedName(SERIALIZED_NAME_SSL_KEY)
  private String sslKey;

  /**
   * Controls how session stickiness is handled on this port. * If set to &#x60;none&#x60; connections will always be assigned a backend based on the algorithm configured. * If set to &#x60;table&#x60; sessions from the same remote address will be routed to the same   backend.  * For HTTP or HTTPS clients, &#x60;http_cookie&#x60; allows sessions to be   routed to the same backend based on a cookie set by the NodeBalancer. 
   */
  @JsonAdapter(StickinessEnum.Adapter.class)
  public enum StickinessEnum {
    NONE("none"),
    
    TABLE("table"),
    
    HTTP_COOKIE("http_cookie");

    private String value;

    StickinessEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StickinessEnum fromValue(String value) {
      for (StickinessEnum b : StickinessEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StickinessEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StickinessEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StickinessEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StickinessEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StickinessEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STICKINESS = "stickiness";
  @SerializedName(SERIALIZED_NAME_STICKINESS)
  private StickinessEnum stickiness = StickinessEnum.NONE;

  public NodeBalancerConfig() {
  }

  public NodeBalancerConfig(
     Integer id, 
     Integer nodebalancerId, 
     String sslCommonname, 
     String sslFingerprint
  ) {
    this();
    this.id = id;
    this.nodebalancerId = nodebalancerId;
    this.sslCommonname = sslCommonname;
    this.sslFingerprint = sslFingerprint;
  }

  public NodeBalancerConfig algorithm(AlgorithmEnum algorithm) {
    this.algorithm = algorithm;
    return this;
  }

  /**
   * What algorithm this NodeBalancer should use for routing traffic to backends. 
   * @return algorithm
   */
  @javax.annotation.Nullable
  public AlgorithmEnum getAlgorithm() {
    return algorithm;
  }

  public void setAlgorithm(AlgorithmEnum algorithm) {
    this.algorithm = algorithm;
  }


  public NodeBalancerConfig check(CheckEnum check) {
    this.check = check;
    return this;
  }

  /**
   * The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. * If &#x60;none&#x60; no check is performed. * &#x60;connection&#x60; requires only a connection to the backend to succeed. * &#x60;http&#x60; and &#x60;http_body&#x60; rely on the backend serving HTTP, and that   the response returned matches what is expected. 
   * @return check
   */
  @javax.annotation.Nullable
  public CheckEnum getCheck() {
    return check;
  }

  public void setCheck(CheckEnum check) {
    this.check = check;
  }


  public NodeBalancerConfig checkAttempts(Integer checkAttempts) {
    this.checkAttempts = checkAttempts;
    return this;
  }

  /**
   * How many times to attempt a check before considering a backend to be down. 
   * minimum: 1
   * maximum: 30
   * @return checkAttempts
   */
  @javax.annotation.Nullable
  public Integer getCheckAttempts() {
    return checkAttempts;
  }

  public void setCheckAttempts(Integer checkAttempts) {
    this.checkAttempts = checkAttempts;
  }


  public NodeBalancerConfig checkBody(String checkBody) {
    this.checkBody = checkBody;
    return this;
  }

  /**
   * This value must be present in the response body of the check in order for it to pass. If this value is not present in the response body of a check request, the backend is considered to be down. 
   * @return checkBody
   */
  @javax.annotation.Nullable
  public String getCheckBody() {
    return checkBody;
  }

  public void setCheckBody(String checkBody) {
    this.checkBody = checkBody;
  }


  public NodeBalancerConfig checkInterval(Integer checkInterval) {
    this.checkInterval = checkInterval;
    return this;
  }

  /**
   * How often, in seconds, to check that backends are up and serving requests.  Must be greater than &#x60;check_timeout&#x60;. 
   * @return checkInterval
   */
  @javax.annotation.Nullable
  public Integer getCheckInterval() {
    return checkInterval;
  }

  public void setCheckInterval(Integer checkInterval) {
    this.checkInterval = checkInterval;
  }


  public NodeBalancerConfig checkPassive(Boolean checkPassive) {
    this.checkPassive = checkPassive;
    return this;
  }

  /**
   * If true, any response from this backend with a &#x60;5xx&#x60; status code will be enough for it to be considered unhealthy and taken out of rotation. 
   * @return checkPassive
   */
  @javax.annotation.Nullable
  public Boolean getCheckPassive() {
    return checkPassive;
  }

  public void setCheckPassive(Boolean checkPassive) {
    this.checkPassive = checkPassive;
  }


  public NodeBalancerConfig checkPath(String checkPath) {
    this.checkPath = checkPath;
    return this;
  }

  /**
   * The URL path to check on each backend. If the backend does not respond to this request it is considered to be down. 
   * @return checkPath
   */
  @javax.annotation.Nullable
  public String getCheckPath() {
    return checkPath;
  }

  public void setCheckPath(String checkPath) {
    this.checkPath = checkPath;
  }


  public NodeBalancerConfig checkTimeout(Integer checkTimeout) {
    this.checkTimeout = checkTimeout;
    return this;
  }

  /**
   * How long, in seconds, to wait for a check attempt before considering it failed.  Must be less than &#x60;check_interval&#x60;. 
   * minimum: 1
   * maximum: 30
   * @return checkTimeout
   */
  @javax.annotation.Nullable
  public Integer getCheckTimeout() {
    return checkTimeout;
  }

  public void setCheckTimeout(Integer checkTimeout) {
    this.checkTimeout = checkTimeout;
  }


  public NodeBalancerConfig cipherSuite(CipherSuiteEnum cipherSuite) {
    this.cipherSuite = cipherSuite;
    return this;
  }

  /**
   * What ciphers to use for SSL connections served by this NodeBalancer.  * &#x60;legacy&#x60; is considered insecure and should only be used if necessary. 
   * @return cipherSuite
   */
  @javax.annotation.Nullable
  public CipherSuiteEnum getCipherSuite() {
    return cipherSuite;
  }

  public void setCipherSuite(CipherSuiteEnum cipherSuite) {
    this.cipherSuite = cipherSuite;
  }


  /**
   * This config&#39;s unique ID
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  /**
   * The ID for the NodeBalancer this config belongs to. 
   * @return nodebalancerId
   */
  @javax.annotation.Nullable
  public Integer getNodebalancerId() {
    return nodebalancerId;
  }



  public NodeBalancerConfig nodesStatus(NodeBalancerConfigNodesStatus nodesStatus) {
    this.nodesStatus = nodesStatus;
    return this;
  }

  /**
   * Get nodesStatus
   * @return nodesStatus
   */
  @javax.annotation.Nullable
  public NodeBalancerConfigNodesStatus getNodesStatus() {
    return nodesStatus;
  }

  public void setNodesStatus(NodeBalancerConfigNodesStatus nodesStatus) {
    this.nodesStatus = nodesStatus;
  }


  public NodeBalancerConfig port(Integer port) {
    this.port = port;
    return this;
  }

  /**
   * The port this Config is for. These values must be unique across configs on a single NodeBalancer (you can&#39;t have two configs for port 80, for example).  While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443. 
   * minimum: 1
   * maximum: 65535
   * @return port
   */
  @javax.annotation.Nullable
  public Integer getPort() {
    return port;
  }

  public void setPort(Integer port) {
    this.port = port;
  }


  public NodeBalancerConfig protocol(ProtocolEnum protocol) {
    this.protocol = protocol;
    return this;
  }

  /**
   * The protocol this port is configured to serve.  * The &#x60;http&#x60; and &#x60;tcp&#x60; protocols do not support &#x60;ssl_cert&#x60; and &#x60;ssl_key&#x60;.  * The &#x60;https&#x60; protocol is mutually required with &#x60;ssl_cert&#x60; and &#x60;ssl_key&#x60;.  Review our guide on [Available Protocols](/docs/products/networking/nodebalancers/guides/protocols/) for information on protocol features. 
   * @return protocol
   */
  @javax.annotation.Nullable
  public ProtocolEnum getProtocol() {
    return protocol;
  }

  public void setProtocol(ProtocolEnum protocol) {
    this.protocol = protocol;
  }


  public NodeBalancerConfig proxyProtocol(ProxyProtocolEnum proxyProtocol) {
    this.proxyProtocol = proxyProtocol;
    return this;
  }

  /**
   * ProxyProtocol is a TCP extension that sends initial TCP connection information such as source/destination IPs and ports to backend devices. This information would be lost otherwise. Backend devices must be configured to work with ProxyProtocol if enabled.  * If ommited, or set to &#x60;none&#x60;, the NodeBalancer doesn&#39;t send any auxilary data over TCP connections. This is the default. * If set to &#x60;v1&#x60;, the human-readable header format (Version 1) is used. Requires &#x60;tcp&#x60; protocol. * If set to &#x60;v2&#x60;, the binary header format (Version 2) is used. Requires &#x60;tcp&#x60; protocol. 
   * @return proxyProtocol
   */
  @javax.annotation.Nullable
  public ProxyProtocolEnum getProxyProtocol() {
    return proxyProtocol;
  }

  public void setProxyProtocol(ProxyProtocolEnum proxyProtocol) {
    this.proxyProtocol = proxyProtocol;
  }


  public NodeBalancerConfig sslCert(String sslCert) {
    this.sslCert = sslCert;
    return this;
  }

  /**
   * The PEM-formatted public SSL certificate (or the combined PEM-formatted SSL certificate and Certificate Authority chain) that should be served on this NodeBalancerConfig&#39;s port.  Line breaks must be represented as \&quot;\\n\&quot; in the string for requests (but not when using the Linode CLI).  [Diffie-Hellman Parameters](/docs/products/networking/nodebalancers/guides/ssl-termination/#diffie-hellman-parameters) can be included in this value to enable forward secrecy.  The contents of this field will not be shown in any responses that display the NodeBalancerConfig. Instead, &#x60;&lt;REDACTED&gt;&#x60; will be printed where the field appears.  The read-only &#x60;ssl_commonname&#x60; and &#x60;ssl_fingerprint&#x60; fields in a NodeBalancerConfig response are automatically derived from your certificate. Please refer to these fields to verify that the appropriate certificate was assigned to your NodeBalancerConfig. 
   * @return sslCert
   */
  @javax.annotation.Nullable
  public String getSslCert() {
    return sslCert;
  }

  public void setSslCert(String sslCert) {
    this.sslCert = sslCert;
  }


  /**
   * The read-only common name automatically derived from the SSL certificate assigned to this NodeBalancerConfig. Please refer to this field to verify that the appropriate certificate is assigned to your NodeBalancerConfig. 
   * @return sslCommonname
   */
  @javax.annotation.Nullable
  public String getSslCommonname() {
    return sslCommonname;
  }



  /**
   * The read-only SHA1-encoded fingerprint automatically derived from the SSL certificate assigned to this NodeBalancerConfig. Please refer to this field to verify that the appropriate certificate is assigned to your NodeBalancerConfig. 
   * @return sslFingerprint
   */
  @javax.annotation.Nullable
  public String getSslFingerprint() {
    return sslFingerprint;
  }



  public NodeBalancerConfig sslKey(String sslKey) {
    this.sslKey = sslKey;
    return this;
  }

  /**
   * The PEM-formatted private key for the SSL certificate set in the &#x60;ssl_cert&#x60; field.  Line breaks must be represented as \&quot;\\n\&quot; in the string for requests (but not when using the Linode CLI).  The contents of this field will not be shown in any responses that display the NodeBalancerConfig. Instead, &#x60;&lt;REDACTED&gt;&#x60; will be printed where the field appears.  The read-only &#x60;ssl_commonname&#x60; and &#x60;ssl_fingerprint&#x60; fields in a NodeBalancerConfig response are automatically derived from your certificate. Please refer to these fields to verify that the appropriate certificate was assigned to your NodeBalancerConfig. 
   * @return sslKey
   */
  @javax.annotation.Nullable
  public String getSslKey() {
    return sslKey;
  }

  public void setSslKey(String sslKey) {
    this.sslKey = sslKey;
  }


  public NodeBalancerConfig stickiness(StickinessEnum stickiness) {
    this.stickiness = stickiness;
    return this;
  }

  /**
   * Controls how session stickiness is handled on this port. * If set to &#x60;none&#x60; connections will always be assigned a backend based on the algorithm configured. * If set to &#x60;table&#x60; sessions from the same remote address will be routed to the same   backend.  * For HTTP or HTTPS clients, &#x60;http_cookie&#x60; allows sessions to be   routed to the same backend based on a cookie set by the NodeBalancer. 
   * @return stickiness
   */
  @javax.annotation.Nullable
  public StickinessEnum getStickiness() {
    return stickiness;
  }

  public void setStickiness(StickinessEnum stickiness) {
    this.stickiness = stickiness;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NodeBalancerConfig nodeBalancerConfig = (NodeBalancerConfig) o;
    return Objects.equals(this.algorithm, nodeBalancerConfig.algorithm) &&
        Objects.equals(this.check, nodeBalancerConfig.check) &&
        Objects.equals(this.checkAttempts, nodeBalancerConfig.checkAttempts) &&
        Objects.equals(this.checkBody, nodeBalancerConfig.checkBody) &&
        Objects.equals(this.checkInterval, nodeBalancerConfig.checkInterval) &&
        Objects.equals(this.checkPassive, nodeBalancerConfig.checkPassive) &&
        Objects.equals(this.checkPath, nodeBalancerConfig.checkPath) &&
        Objects.equals(this.checkTimeout, nodeBalancerConfig.checkTimeout) &&
        Objects.equals(this.cipherSuite, nodeBalancerConfig.cipherSuite) &&
        Objects.equals(this.id, nodeBalancerConfig.id) &&
        Objects.equals(this.nodebalancerId, nodeBalancerConfig.nodebalancerId) &&
        Objects.equals(this.nodesStatus, nodeBalancerConfig.nodesStatus) &&
        Objects.equals(this.port, nodeBalancerConfig.port) &&
        Objects.equals(this.protocol, nodeBalancerConfig.protocol) &&
        Objects.equals(this.proxyProtocol, nodeBalancerConfig.proxyProtocol) &&
        Objects.equals(this.sslCert, nodeBalancerConfig.sslCert) &&
        Objects.equals(this.sslCommonname, nodeBalancerConfig.sslCommonname) &&
        Objects.equals(this.sslFingerprint, nodeBalancerConfig.sslFingerprint) &&
        Objects.equals(this.sslKey, nodeBalancerConfig.sslKey) &&
        Objects.equals(this.stickiness, nodeBalancerConfig.stickiness);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(algorithm, check, checkAttempts, checkBody, checkInterval, checkPassive, checkPath, checkTimeout, cipherSuite, id, nodebalancerId, nodesStatus, port, protocol, proxyProtocol, sslCert, sslCommonname, sslFingerprint, sslKey, stickiness);
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
    sb.append("class NodeBalancerConfig {\n");
    sb.append("    algorithm: ").append(toIndentedString(algorithm)).append("\n");
    sb.append("    check: ").append(toIndentedString(check)).append("\n");
    sb.append("    checkAttempts: ").append(toIndentedString(checkAttempts)).append("\n");
    sb.append("    checkBody: ").append(toIndentedString(checkBody)).append("\n");
    sb.append("    checkInterval: ").append(toIndentedString(checkInterval)).append("\n");
    sb.append("    checkPassive: ").append(toIndentedString(checkPassive)).append("\n");
    sb.append("    checkPath: ").append(toIndentedString(checkPath)).append("\n");
    sb.append("    checkTimeout: ").append(toIndentedString(checkTimeout)).append("\n");
    sb.append("    cipherSuite: ").append(toIndentedString(cipherSuite)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    nodebalancerId: ").append(toIndentedString(nodebalancerId)).append("\n");
    sb.append("    nodesStatus: ").append(toIndentedString(nodesStatus)).append("\n");
    sb.append("    port: ").append(toIndentedString(port)).append("\n");
    sb.append("    protocol: ").append(toIndentedString(protocol)).append("\n");
    sb.append("    proxyProtocol: ").append(toIndentedString(proxyProtocol)).append("\n");
    sb.append("    sslCert: ").append(toIndentedString(sslCert)).append("\n");
    sb.append("    sslCommonname: ").append(toIndentedString(sslCommonname)).append("\n");
    sb.append("    sslFingerprint: ").append(toIndentedString(sslFingerprint)).append("\n");
    sb.append("    sslKey: ").append(toIndentedString(sslKey)).append("\n");
    sb.append("    stickiness: ").append(toIndentedString(stickiness)).append("\n");
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
    openapiFields.add("algorithm");
    openapiFields.add("check");
    openapiFields.add("check_attempts");
    openapiFields.add("check_body");
    openapiFields.add("check_interval");
    openapiFields.add("check_passive");
    openapiFields.add("check_path");
    openapiFields.add("check_timeout");
    openapiFields.add("cipher_suite");
    openapiFields.add("id");
    openapiFields.add("nodebalancer_id");
    openapiFields.add("nodes_status");
    openapiFields.add("port");
    openapiFields.add("protocol");
    openapiFields.add("proxy_protocol");
    openapiFields.add("ssl_cert");
    openapiFields.add("ssl_commonname");
    openapiFields.add("ssl_fingerprint");
    openapiFields.add("ssl_key");
    openapiFields.add("stickiness");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NodeBalancerConfig
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NodeBalancerConfig.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NodeBalancerConfig is not found in the empty JSON string", NodeBalancerConfig.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NodeBalancerConfig.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NodeBalancerConfig` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("algorithm") != null && !jsonObj.get("algorithm").isJsonNull()) && !jsonObj.get("algorithm").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `algorithm` to be a primitive type in the JSON string but got `%s`", jsonObj.get("algorithm").toString()));
      }
      // validate the optional field `algorithm`
      if (jsonObj.get("algorithm") != null && !jsonObj.get("algorithm").isJsonNull()) {
        AlgorithmEnum.validateJsonElement(jsonObj.get("algorithm"));
      }
      if ((jsonObj.get("check") != null && !jsonObj.get("check").isJsonNull()) && !jsonObj.get("check").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `check` to be a primitive type in the JSON string but got `%s`", jsonObj.get("check").toString()));
      }
      // validate the optional field `check`
      if (jsonObj.get("check") != null && !jsonObj.get("check").isJsonNull()) {
        CheckEnum.validateJsonElement(jsonObj.get("check"));
      }
      if ((jsonObj.get("check_body") != null && !jsonObj.get("check_body").isJsonNull()) && !jsonObj.get("check_body").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `check_body` to be a primitive type in the JSON string but got `%s`", jsonObj.get("check_body").toString()));
      }
      if ((jsonObj.get("check_path") != null && !jsonObj.get("check_path").isJsonNull()) && !jsonObj.get("check_path").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `check_path` to be a primitive type in the JSON string but got `%s`", jsonObj.get("check_path").toString()));
      }
      if ((jsonObj.get("cipher_suite") != null && !jsonObj.get("cipher_suite").isJsonNull()) && !jsonObj.get("cipher_suite").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cipher_suite` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cipher_suite").toString()));
      }
      // validate the optional field `cipher_suite`
      if (jsonObj.get("cipher_suite") != null && !jsonObj.get("cipher_suite").isJsonNull()) {
        CipherSuiteEnum.validateJsonElement(jsonObj.get("cipher_suite"));
      }
      // validate the optional field `nodes_status`
      if (jsonObj.get("nodes_status") != null && !jsonObj.get("nodes_status").isJsonNull()) {
        NodeBalancerConfigNodesStatus.validateJsonElement(jsonObj.get("nodes_status"));
      }
      if ((jsonObj.get("protocol") != null && !jsonObj.get("protocol").isJsonNull()) && !jsonObj.get("protocol").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `protocol` to be a primitive type in the JSON string but got `%s`", jsonObj.get("protocol").toString()));
      }
      // validate the optional field `protocol`
      if (jsonObj.get("protocol") != null && !jsonObj.get("protocol").isJsonNull()) {
        ProtocolEnum.validateJsonElement(jsonObj.get("protocol"));
      }
      if ((jsonObj.get("proxy_protocol") != null && !jsonObj.get("proxy_protocol").isJsonNull()) && !jsonObj.get("proxy_protocol").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `proxy_protocol` to be a primitive type in the JSON string but got `%s`", jsonObj.get("proxy_protocol").toString()));
      }
      // validate the optional field `proxy_protocol`
      if (jsonObj.get("proxy_protocol") != null && !jsonObj.get("proxy_protocol").isJsonNull()) {
        ProxyProtocolEnum.validateJsonElement(jsonObj.get("proxy_protocol"));
      }
      if ((jsonObj.get("ssl_cert") != null && !jsonObj.get("ssl_cert").isJsonNull()) && !jsonObj.get("ssl_cert").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssl_cert` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssl_cert").toString()));
      }
      if ((jsonObj.get("ssl_commonname") != null && !jsonObj.get("ssl_commonname").isJsonNull()) && !jsonObj.get("ssl_commonname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssl_commonname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssl_commonname").toString()));
      }
      if ((jsonObj.get("ssl_fingerprint") != null && !jsonObj.get("ssl_fingerprint").isJsonNull()) && !jsonObj.get("ssl_fingerprint").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssl_fingerprint` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssl_fingerprint").toString()));
      }
      if ((jsonObj.get("ssl_key") != null && !jsonObj.get("ssl_key").isJsonNull()) && !jsonObj.get("ssl_key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssl_key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssl_key").toString()));
      }
      if ((jsonObj.get("stickiness") != null && !jsonObj.get("stickiness").isJsonNull()) && !jsonObj.get("stickiness").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `stickiness` to be a primitive type in the JSON string but got `%s`", jsonObj.get("stickiness").toString()));
      }
      // validate the optional field `stickiness`
      if (jsonObj.get("stickiness") != null && !jsonObj.get("stickiness").isJsonNull()) {
        StickinessEnum.validateJsonElement(jsonObj.get("stickiness"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NodeBalancerConfig.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NodeBalancerConfig' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NodeBalancerConfig> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NodeBalancerConfig.class));

       return (TypeAdapter<T>) new TypeAdapter<NodeBalancerConfig>() {
           @Override
           public void write(JsonWriter out, NodeBalancerConfig value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NodeBalancerConfig read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NodeBalancerConfig given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NodeBalancerConfig
   * @throws IOException if the JSON string is invalid with respect to NodeBalancerConfig
   */
  public static NodeBalancerConfig fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NodeBalancerConfig.class);
  }

  /**
   * Convert an instance of NodeBalancerConfig to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

