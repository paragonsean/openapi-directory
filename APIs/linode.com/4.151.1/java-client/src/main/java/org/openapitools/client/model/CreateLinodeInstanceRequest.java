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
import org.openapitools.client.model.LinodeConfigInterface;

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
 * CreateLinodeInstanceRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:42.346741-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateLinodeInstanceRequest {
  public static final String SERIALIZED_NAME_AUTHORIZED_KEYS = "authorized_keys";
  @SerializedName(SERIALIZED_NAME_AUTHORIZED_KEYS)
  private List<String> authorizedKeys = new ArrayList<>();

  public static final String SERIALIZED_NAME_AUTHORIZED_USERS = "authorized_users";
  @SerializedName(SERIALIZED_NAME_AUTHORIZED_USERS)
  private List<String> authorizedUsers = new ArrayList<>();

  public static final String SERIALIZED_NAME_BOOTED = "booted";
  @SerializedName(SERIALIZED_NAME_BOOTED)
  private Boolean booted = true;

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private String image;

  public static final String SERIALIZED_NAME_ROOT_PASS = "root_pass";
  @SerializedName(SERIALIZED_NAME_ROOT_PASS)
  private String rootPass;

  public static final String SERIALIZED_NAME_STACKSCRIPT_DATA = "stackscript_data";
  @SerializedName(SERIALIZED_NAME_STACKSCRIPT_DATA)
  private Object stackscriptData;

  public static final String SERIALIZED_NAME_STACKSCRIPT_ID = "stackscript_id";
  @SerializedName(SERIALIZED_NAME_STACKSCRIPT_ID)
  private Integer stackscriptId;

  public static final String SERIALIZED_NAME_BACKUP_ID = "backup_id";
  @SerializedName(SERIALIZED_NAME_BACKUP_ID)
  private Integer backupId;

  public static final String SERIALIZED_NAME_BACKUPS_ENABLED = "backups_enabled";
  @SerializedName(SERIALIZED_NAME_BACKUPS_ENABLED)
  private Boolean backupsEnabled;

  public static final String SERIALIZED_NAME_GROUP = "group";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_GROUP)
  private String group;

  public static final String SERIALIZED_NAME_INTERFACES = "interfaces";
  @SerializedName(SERIALIZED_NAME_INTERFACES)
  private List<LinodeConfigInterface> interfaces = new ArrayList<>();

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public static final String SERIALIZED_NAME_PRIVATE_IP = "private_ip";
  @SerializedName(SERIALIZED_NAME_PRIVATE_IP)
  private Boolean privateIp;

  public static final String SERIALIZED_NAME_REGION = "region";
  @SerializedName(SERIALIZED_NAME_REGION)
  private String region;

  public static final String SERIALIZED_NAME_SWAP_SIZE = "swap_size";
  @SerializedName(SERIALIZED_NAME_SWAP_SIZE)
  private Integer swapSize = 512;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<String> tags = new ArrayList<>();

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public CreateLinodeInstanceRequest() {
  }

  public CreateLinodeInstanceRequest authorizedKeys(List<String> authorizedKeys) {
    this.authorizedKeys = authorizedKeys;
    return this;
  }

  public CreateLinodeInstanceRequest addAuthorizedKeysItem(String authorizedKeysItem) {
    if (this.authorizedKeys == null) {
      this.authorizedKeys = new ArrayList<>();
    }
    this.authorizedKeys.add(authorizedKeysItem);
    return this;
  }

  /**
   * A list of public SSH keys that will be automatically appended to the root user&#39;s &#x60;~/.ssh/authorized_keys&#x60; file when deploying from an Image. 
   * @return authorizedKeys
   */
  @javax.annotation.Nullable
  public List<String> getAuthorizedKeys() {
    return authorizedKeys;
  }

  public void setAuthorizedKeys(List<String> authorizedKeys) {
    this.authorizedKeys = authorizedKeys;
  }


  public CreateLinodeInstanceRequest authorizedUsers(List<String> authorizedUsers) {
    this.authorizedUsers = authorizedUsers;
    return this;
  }

  public CreateLinodeInstanceRequest addAuthorizedUsersItem(String authorizedUsersItem) {
    if (this.authorizedUsers == null) {
      this.authorizedUsers = new ArrayList<>();
    }
    this.authorizedUsers.add(authorizedUsersItem);
    return this;
  }

  /**
   * A list of usernames. If the usernames have associated SSH keys, the keys will be appended to the root users &#x60;~/.ssh/authorized_keys&#x60; file automatically when deploying from an Image. 
   * @return authorizedUsers
   */
  @javax.annotation.Nullable
  public List<String> getAuthorizedUsers() {
    return authorizedUsers;
  }

  public void setAuthorizedUsers(List<String> authorizedUsers) {
    this.authorizedUsers = authorizedUsers;
  }


  public CreateLinodeInstanceRequest booted(Boolean booted) {
    this.booted = booted;
    return this;
  }

  /**
   * This field defaults to &#x60;true&#x60; if the Linode is created with an Image or from a Backup. If it is deployed from an Image or a Backup and you wish it to remain &#x60;offline&#x60; after deployment, set this to &#x60;false&#x60;. 
   * @return booted
   */
  @javax.annotation.Nullable
  public Boolean getBooted() {
    return booted;
  }

  public void setBooted(Boolean booted) {
    this.booted = booted;
  }


  public CreateLinodeInstanceRequest image(String image) {
    this.image = image;
    return this;
  }

  /**
   * An Image ID to deploy the Linode Disk from.  Access the Images List ([GET /images](/docs/api/images/#images-list)) endpoint with authentication to view all available Images. Official Linode Images start with &#x60;linode/&#x60;, while your Account&#39;s Images start with &#x60;private/&#x60;. Creating a disk from a Private Image requires &#x60;read_only&#x60; or &#x60;read_write&#x60; permissions for that Image. Access the User&#39;s Grant Update ([PUT /account/users/{username}/grants](/docs/api/account/#users-grants-update)) endpoint to adjust permissions for an Account Image. 
   * @return image
   */
  @javax.annotation.Nullable
  public String getImage() {
    return image;
  }

  public void setImage(String image) {
    this.image = image;
  }


  public CreateLinodeInstanceRequest rootPass(String rootPass) {
    this.rootPass = rootPass;
    return this;
  }

  /**
   * This sets the root user&#39;s password on a newly-created Linode Disk when deploying from an Image.  * **Required** when creating a Linode Disk from an Image, including when using a StackScript.  * Must meet a password strength score requirement that is calculated internally by the API. If the strength requirement is not met, you will receive a &#x60;Password does not meet strength requirement&#x60; error. 
   * @return rootPass
   */
  @javax.annotation.Nullable
  public String getRootPass() {
    return rootPass;
  }

  public void setRootPass(String rootPass) {
    this.rootPass = rootPass;
  }


  public CreateLinodeInstanceRequest stackscriptData(Object stackscriptData) {
    this.stackscriptData = stackscriptData;
    return this;
  }

  /**
   * This field is required only if the StackScript being deployed requires input data from the User for successful completion. See [User Defined Fields (UDFs)](/docs/guides/writing-scripts-for-use-with-linode-stackscripts-a-tutorial/#user-defined-fields-udfs) for more details.  This field is required to be valid JSON.  Total length cannot exceed 65,535 characters. 
   * @return stackscriptData
   */
  @javax.annotation.Nullable
  public Object getStackscriptData() {
    return stackscriptData;
  }

  public void setStackscriptData(Object stackscriptData) {
    this.stackscriptData = stackscriptData;
  }


  public CreateLinodeInstanceRequest stackscriptId(Integer stackscriptId) {
    this.stackscriptId = stackscriptId;
    return this;
  }

  /**
   * A StackScript ID that will cause the referenced StackScript to be run during deployment of this Linode. A compatible &#x60;image&#x60; is required to use a StackScript. To get a list of available StackScript and their permitted Images see [/stackscripts](/docs/api/stackscripts/#stackscripts-list). This field cannot be used when deploying from a Backup or a Private Image. 
   * @return stackscriptId
   */
  @javax.annotation.Nullable
  public Integer getStackscriptId() {
    return stackscriptId;
  }

  public void setStackscriptId(Integer stackscriptId) {
    this.stackscriptId = stackscriptId;
  }


  public CreateLinodeInstanceRequest backupId(Integer backupId) {
    this.backupId = backupId;
    return this;
  }

  /**
   * A Backup ID from another Linode&#39;s available backups. Your User must have &#x60;read_write&#x60; access to that Linode, the Backup must have a &#x60;status&#x60; of &#x60;successful&#x60;, and the Linode must be deployed to the same &#x60;region&#x60; as the Backup. See [GET /linode/instances/{linodeId}/backups](/docs/api/linode-instances/#backups-list) for a Linode&#39;s available backups.  This field and the &#x60;image&#x60; field are mutually exclusive. 
   * @return backupId
   */
  @javax.annotation.Nullable
  public Integer getBackupId() {
    return backupId;
  }

  public void setBackupId(Integer backupId) {
    this.backupId = backupId;
  }


  public CreateLinodeInstanceRequest backupsEnabled(Boolean backupsEnabled) {
    this.backupsEnabled = backupsEnabled;
    return this;
  }

  /**
   * If this field is set to &#x60;true&#x60;, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. The cost for the Backup service is dependent on the Type of Linode deployed.  This option is always treated as &#x60;true&#x60; if the account-wide &#x60;backups_enabled&#x60; setting is &#x60;true&#x60;.  See [account settings](/docs/api/account/#account-settings-view) for more information.  Backup pricing is included in the response from [/linodes/types](/docs/api/linode-types/#types-list) 
   * @return backupsEnabled
   */
  @javax.annotation.Nullable
  public Boolean getBackupsEnabled() {
    return backupsEnabled;
  }

  public void setBackupsEnabled(Boolean backupsEnabled) {
    this.backupsEnabled = backupsEnabled;
  }


  @Deprecated
  public CreateLinodeInstanceRequest group(String group) {
    this.group = group;
    return this;
  }

  /**
   * A deprecated property denoting a group label for this Linode. 
   * @return group
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getGroup() {
    return group;
  }

  @Deprecated
  public void setGroup(String group) {
    this.group = group;
  }


  public CreateLinodeInstanceRequest interfaces(List<LinodeConfigInterface> interfaces) {
    this.interfaces = interfaces;
    return this;
  }

  public CreateLinodeInstanceRequest addInterfacesItem(LinodeConfigInterface interfacesItem) {
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


  public CreateLinodeInstanceRequest label(String label) {
    this.label = label;
    return this;
  }

  /**
   * The Linode&#39;s label is for display purposes only. If no label is provided for a Linode, a default will be assigned.  Linode labels have the following constraints:    * Must begin and end with an alphanumeric character.   * May only consist of alphanumeric characters, dashes (&#x60;-&#x60;), underscores (&#x60;_&#x60;) or periods (&#x60;.&#x60;).   * Cannot have two dashes (&#x60;--&#x60;), underscores (&#x60;__&#x60;) or periods (&#x60;..&#x60;) in a row. 
   * @return label
   */
  @javax.annotation.Nullable
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }


  public CreateLinodeInstanceRequest privateIp(Boolean privateIp) {
    this.privateIp = privateIp;
    return this;
  }

  /**
   * If true, the created Linode will have private networking enabled and assigned a private IPv4 address. 
   * @return privateIp
   */
  @javax.annotation.Nullable
  public Boolean getPrivateIp() {
    return privateIp;
  }

  public void setPrivateIp(Boolean privateIp) {
    this.privateIp = privateIp;
  }


  public CreateLinodeInstanceRequest region(String region) {
    this.region = region;
    return this;
  }

  /**
   * The [Region](/docs/api/regions/#regions-list) where the Linode will be located. 
   * @return region
   */
  @javax.annotation.Nonnull
  public String getRegion() {
    return region;
  }

  public void setRegion(String region) {
    this.region = region;
  }


  public CreateLinodeInstanceRequest swapSize(Integer swapSize) {
    this.swapSize = swapSize;
    return this;
  }

  /**
   * When deploying from an Image, this field is optional, otherwise it is ignored. This is used to set the swap disk size for the newly-created Linode. 
   * @return swapSize
   */
  @javax.annotation.Nullable
  public Integer getSwapSize() {
    return swapSize;
  }

  public void setSwapSize(Integer swapSize) {
    this.swapSize = swapSize;
  }


  public CreateLinodeInstanceRequest tags(List<String> tags) {
    this.tags = tags;
    return this;
  }

  public CreateLinodeInstanceRequest addTagsItem(String tagsItem) {
    if (this.tags == null) {
      this.tags = new ArrayList<>();
    }
    this.tags.add(tagsItem);
    return this;
  }

  /**
   * An array of tags applied to this object.  Tags are for organizational purposes only. 
   * @return tags
   */
  @javax.annotation.Nullable
  public List<String> getTags() {
    return tags;
  }

  public void setTags(List<String> tags) {
    this.tags = tags;
  }


  public CreateLinodeInstanceRequest type(String type) {
    this.type = type;
    return this;
  }

  /**
   * The [Linode Type](/docs/api/linode-types/#types-list) of the Linode you are creating. 
   * @return type
   */
  @javax.annotation.Nonnull
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateLinodeInstanceRequest createLinodeInstanceRequest = (CreateLinodeInstanceRequest) o;
    return Objects.equals(this.authorizedKeys, createLinodeInstanceRequest.authorizedKeys) &&
        Objects.equals(this.authorizedUsers, createLinodeInstanceRequest.authorizedUsers) &&
        Objects.equals(this.booted, createLinodeInstanceRequest.booted) &&
        Objects.equals(this.image, createLinodeInstanceRequest.image) &&
        Objects.equals(this.rootPass, createLinodeInstanceRequest.rootPass) &&
        Objects.equals(this.stackscriptData, createLinodeInstanceRequest.stackscriptData) &&
        Objects.equals(this.stackscriptId, createLinodeInstanceRequest.stackscriptId) &&
        Objects.equals(this.backupId, createLinodeInstanceRequest.backupId) &&
        Objects.equals(this.backupsEnabled, createLinodeInstanceRequest.backupsEnabled) &&
        Objects.equals(this.group, createLinodeInstanceRequest.group) &&
        Objects.equals(this.interfaces, createLinodeInstanceRequest.interfaces) &&
        Objects.equals(this.label, createLinodeInstanceRequest.label) &&
        Objects.equals(this.privateIp, createLinodeInstanceRequest.privateIp) &&
        Objects.equals(this.region, createLinodeInstanceRequest.region) &&
        Objects.equals(this.swapSize, createLinodeInstanceRequest.swapSize) &&
        Objects.equals(this.tags, createLinodeInstanceRequest.tags) &&
        Objects.equals(this.type, createLinodeInstanceRequest.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(authorizedKeys, authorizedUsers, booted, image, rootPass, stackscriptData, stackscriptId, backupId, backupsEnabled, group, interfaces, label, privateIp, region, swapSize, tags, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateLinodeInstanceRequest {\n");
    sb.append("    authorizedKeys: ").append(toIndentedString(authorizedKeys)).append("\n");
    sb.append("    authorizedUsers: ").append(toIndentedString(authorizedUsers)).append("\n");
    sb.append("    booted: ").append(toIndentedString(booted)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    rootPass: ").append("*").append("\n");
    sb.append("    stackscriptData: ").append(toIndentedString(stackscriptData)).append("\n");
    sb.append("    stackscriptId: ").append(toIndentedString(stackscriptId)).append("\n");
    sb.append("    backupId: ").append(toIndentedString(backupId)).append("\n");
    sb.append("    backupsEnabled: ").append(toIndentedString(backupsEnabled)).append("\n");
    sb.append("    group: ").append(toIndentedString(group)).append("\n");
    sb.append("    interfaces: ").append(toIndentedString(interfaces)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
    sb.append("    privateIp: ").append(toIndentedString(privateIp)).append("\n");
    sb.append("    region: ").append(toIndentedString(region)).append("\n");
    sb.append("    swapSize: ").append(toIndentedString(swapSize)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("authorized_keys");
    openapiFields.add("authorized_users");
    openapiFields.add("booted");
    openapiFields.add("image");
    openapiFields.add("root_pass");
    openapiFields.add("stackscript_data");
    openapiFields.add("stackscript_id");
    openapiFields.add("backup_id");
    openapiFields.add("backups_enabled");
    openapiFields.add("group");
    openapiFields.add("interfaces");
    openapiFields.add("label");
    openapiFields.add("private_ip");
    openapiFields.add("region");
    openapiFields.add("swap_size");
    openapiFields.add("tags");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("region");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateLinodeInstanceRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateLinodeInstanceRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateLinodeInstanceRequest is not found in the empty JSON string", CreateLinodeInstanceRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateLinodeInstanceRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateLinodeInstanceRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateLinodeInstanceRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("authorized_keys") != null && !jsonObj.get("authorized_keys").isJsonNull() && !jsonObj.get("authorized_keys").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `authorized_keys` to be an array in the JSON string but got `%s`", jsonObj.get("authorized_keys").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("authorized_users") != null && !jsonObj.get("authorized_users").isJsonNull() && !jsonObj.get("authorized_users").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `authorized_users` to be an array in the JSON string but got `%s`", jsonObj.get("authorized_users").toString()));
      }
      if ((jsonObj.get("image") != null && !jsonObj.get("image").isJsonNull()) && !jsonObj.get("image").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `image` to be a primitive type in the JSON string but got `%s`", jsonObj.get("image").toString()));
      }
      if ((jsonObj.get("root_pass") != null && !jsonObj.get("root_pass").isJsonNull()) && !jsonObj.get("root_pass").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `root_pass` to be a primitive type in the JSON string but got `%s`", jsonObj.get("root_pass").toString()));
      }
      if ((jsonObj.get("group") != null && !jsonObj.get("group").isJsonNull()) && !jsonObj.get("group").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `group` to be a primitive type in the JSON string but got `%s`", jsonObj.get("group").toString()));
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
      if ((jsonObj.get("label") != null && !jsonObj.get("label").isJsonNull()) && !jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
      if (!jsonObj.get("region").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `region` to be a primitive type in the JSON string but got `%s`", jsonObj.get("region").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull() && !jsonObj.get("tags").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateLinodeInstanceRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateLinodeInstanceRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateLinodeInstanceRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateLinodeInstanceRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateLinodeInstanceRequest>() {
           @Override
           public void write(JsonWriter out, CreateLinodeInstanceRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateLinodeInstanceRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateLinodeInstanceRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateLinodeInstanceRequest
   * @throws IOException if the JSON string is invalid with respect to CreateLinodeInstanceRequest
   */
  public static CreateLinodeInstanceRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateLinodeInstanceRequest.class);
  }

  /**
   * Convert an instance of CreateLinodeInstanceRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

