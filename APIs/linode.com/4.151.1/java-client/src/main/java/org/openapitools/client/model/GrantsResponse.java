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
import org.openapitools.client.model.Grant;
import org.openapitools.client.model.GrantsResponseGlobal;

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
 * A structure representing all grants a restricted User has on the Account. Not available for unrestricted users, as they have access to everything without grants. If retrieved from the &#x60;/profile/grants&#x60; endpoint, entities to which a User has no access will be omitted. 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:42.346741-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GrantsResponse {
  public static final String SERIALIZED_NAME_DATABASE = "database";
  @SerializedName(SERIALIZED_NAME_DATABASE)
  private List<Grant> database = new ArrayList<>();

  public static final String SERIALIZED_NAME_DOMAIN = "domain";
  @SerializedName(SERIALIZED_NAME_DOMAIN)
  private List<Grant> domain = new ArrayList<>();

  public static final String SERIALIZED_NAME_GLOBAL = "global";
  @SerializedName(SERIALIZED_NAME_GLOBAL)
  private GrantsResponseGlobal global;

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private List<Grant> image = new ArrayList<>();

  public static final String SERIALIZED_NAME_LINODE = "linode";
  @SerializedName(SERIALIZED_NAME_LINODE)
  private List<Grant> linode = new ArrayList<>();

  public static final String SERIALIZED_NAME_LONGVIEW = "longview";
  @SerializedName(SERIALIZED_NAME_LONGVIEW)
  private List<Grant> longview = new ArrayList<>();

  public static final String SERIALIZED_NAME_NODEBALANCER = "nodebalancer";
  @SerializedName(SERIALIZED_NAME_NODEBALANCER)
  private List<Grant> nodebalancer = new ArrayList<>();

  public static final String SERIALIZED_NAME_STACKSCRIPT = "stackscript";
  @SerializedName(SERIALIZED_NAME_STACKSCRIPT)
  private List<Grant> stackscript = new ArrayList<>();

  public static final String SERIALIZED_NAME_VOLUME = "volume";
  @SerializedName(SERIALIZED_NAME_VOLUME)
  private List<Grant> volume = new ArrayList<>();

  public GrantsResponse() {
  }

  public GrantsResponse database(List<Grant> database) {
    this.database = database;
    return this;
  }

  public GrantsResponse addDatabaseItem(Grant databaseItem) {
    if (this.database == null) {
      this.database = new ArrayList<>();
    }
    this.database.add(databaseItem);
    return this;
  }

  /**
   * The grants this User has for each Database that is owned by this Account. 
   * @return database
   */
  @javax.annotation.Nullable
  public List<Grant> getDatabase() {
    return database;
  }

  public void setDatabase(List<Grant> database) {
    this.database = database;
  }


  public GrantsResponse domain(List<Grant> domain) {
    this.domain = domain;
    return this;
  }

  public GrantsResponse addDomainItem(Grant domainItem) {
    if (this.domain == null) {
      this.domain = new ArrayList<>();
    }
    this.domain.add(domainItem);
    return this;
  }

  /**
   * The grants this User has for each Domain that is owned by this Account. 
   * @return domain
   */
  @javax.annotation.Nullable
  public List<Grant> getDomain() {
    return domain;
  }

  public void setDomain(List<Grant> domain) {
    this.domain = domain;
  }


  public GrantsResponse global(GrantsResponseGlobal global) {
    this.global = global;
    return this;
  }

  /**
   * Get global
   * @return global
   */
  @javax.annotation.Nullable
  public GrantsResponseGlobal getGlobal() {
    return global;
  }

  public void setGlobal(GrantsResponseGlobal global) {
    this.global = global;
  }


  public GrantsResponse image(List<Grant> image) {
    this.image = image;
    return this;
  }

  public GrantsResponse addImageItem(Grant imageItem) {
    if (this.image == null) {
      this.image = new ArrayList<>();
    }
    this.image.add(imageItem);
    return this;
  }

  /**
   * The grants this User has for each Image that is owned by this Account. 
   * @return image
   */
  @javax.annotation.Nullable
  public List<Grant> getImage() {
    return image;
  }

  public void setImage(List<Grant> image) {
    this.image = image;
  }


  public GrantsResponse linode(List<Grant> linode) {
    this.linode = linode;
    return this;
  }

  public GrantsResponse addLinodeItem(Grant linodeItem) {
    if (this.linode == null) {
      this.linode = new ArrayList<>();
    }
    this.linode.add(linodeItem);
    return this;
  }

  /**
   * The grants this User has for each Linode that is owned by this Account. 
   * @return linode
   */
  @javax.annotation.Nullable
  public List<Grant> getLinode() {
    return linode;
  }

  public void setLinode(List<Grant> linode) {
    this.linode = linode;
  }


  public GrantsResponse longview(List<Grant> longview) {
    this.longview = longview;
    return this;
  }

  public GrantsResponse addLongviewItem(Grant longviewItem) {
    if (this.longview == null) {
      this.longview = new ArrayList<>();
    }
    this.longview.add(longviewItem);
    return this;
  }

  /**
   * The grants this User has for each Longview Client that is owned by this Account. 
   * @return longview
   */
  @javax.annotation.Nullable
  public List<Grant> getLongview() {
    return longview;
  }

  public void setLongview(List<Grant> longview) {
    this.longview = longview;
  }


  public GrantsResponse nodebalancer(List<Grant> nodebalancer) {
    this.nodebalancer = nodebalancer;
    return this;
  }

  public GrantsResponse addNodebalancerItem(Grant nodebalancerItem) {
    if (this.nodebalancer == null) {
      this.nodebalancer = new ArrayList<>();
    }
    this.nodebalancer.add(nodebalancerItem);
    return this;
  }

  /**
   * The grants this User has for each NodeBalancer that is owned by this Account. 
   * @return nodebalancer
   */
  @javax.annotation.Nullable
  public List<Grant> getNodebalancer() {
    return nodebalancer;
  }

  public void setNodebalancer(List<Grant> nodebalancer) {
    this.nodebalancer = nodebalancer;
  }


  public GrantsResponse stackscript(List<Grant> stackscript) {
    this.stackscript = stackscript;
    return this;
  }

  public GrantsResponse addStackscriptItem(Grant stackscriptItem) {
    if (this.stackscript == null) {
      this.stackscript = new ArrayList<>();
    }
    this.stackscript.add(stackscriptItem);
    return this;
  }

  /**
   * The grants this User has for each StackScript that is owned by this Account. 
   * @return stackscript
   */
  @javax.annotation.Nullable
  public List<Grant> getStackscript() {
    return stackscript;
  }

  public void setStackscript(List<Grant> stackscript) {
    this.stackscript = stackscript;
  }


  public GrantsResponse volume(List<Grant> volume) {
    this.volume = volume;
    return this;
  }

  public GrantsResponse addVolumeItem(Grant volumeItem) {
    if (this.volume == null) {
      this.volume = new ArrayList<>();
    }
    this.volume.add(volumeItem);
    return this;
  }

  /**
   * The grants this User has for each Block Storage Volume that is owned by this Account. 
   * @return volume
   */
  @javax.annotation.Nullable
  public List<Grant> getVolume() {
    return volume;
  }

  public void setVolume(List<Grant> volume) {
    this.volume = volume;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GrantsResponse grantsResponse = (GrantsResponse) o;
    return Objects.equals(this.database, grantsResponse.database) &&
        Objects.equals(this.domain, grantsResponse.domain) &&
        Objects.equals(this.global, grantsResponse.global) &&
        Objects.equals(this.image, grantsResponse.image) &&
        Objects.equals(this.linode, grantsResponse.linode) &&
        Objects.equals(this.longview, grantsResponse.longview) &&
        Objects.equals(this.nodebalancer, grantsResponse.nodebalancer) &&
        Objects.equals(this.stackscript, grantsResponse.stackscript) &&
        Objects.equals(this.volume, grantsResponse.volume);
  }

  @Override
  public int hashCode() {
    return Objects.hash(database, domain, global, image, linode, longview, nodebalancer, stackscript, volume);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GrantsResponse {\n");
    sb.append("    database: ").append(toIndentedString(database)).append("\n");
    sb.append("    domain: ").append(toIndentedString(domain)).append("\n");
    sb.append("    global: ").append(toIndentedString(global)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    linode: ").append(toIndentedString(linode)).append("\n");
    sb.append("    longview: ").append(toIndentedString(longview)).append("\n");
    sb.append("    nodebalancer: ").append(toIndentedString(nodebalancer)).append("\n");
    sb.append("    stackscript: ").append(toIndentedString(stackscript)).append("\n");
    sb.append("    volume: ").append(toIndentedString(volume)).append("\n");
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
    openapiFields.add("database");
    openapiFields.add("domain");
    openapiFields.add("global");
    openapiFields.add("image");
    openapiFields.add("linode");
    openapiFields.add("longview");
    openapiFields.add("nodebalancer");
    openapiFields.add("stackscript");
    openapiFields.add("volume");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GrantsResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GrantsResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GrantsResponse is not found in the empty JSON string", GrantsResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GrantsResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GrantsResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("database") != null && !jsonObj.get("database").isJsonNull()) {
        JsonArray jsonArraydatabase = jsonObj.getAsJsonArray("database");
        if (jsonArraydatabase != null) {
          // ensure the json data is an array
          if (!jsonObj.get("database").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `database` to be an array in the JSON string but got `%s`", jsonObj.get("database").toString()));
          }

          // validate the optional field `database` (array)
          for (int i = 0; i < jsonArraydatabase.size(); i++) {
            Grant.validateJsonElement(jsonArraydatabase.get(i));
          };
        }
      }
      if (jsonObj.get("domain") != null && !jsonObj.get("domain").isJsonNull()) {
        JsonArray jsonArraydomain = jsonObj.getAsJsonArray("domain");
        if (jsonArraydomain != null) {
          // ensure the json data is an array
          if (!jsonObj.get("domain").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `domain` to be an array in the JSON string but got `%s`", jsonObj.get("domain").toString()));
          }

          // validate the optional field `domain` (array)
          for (int i = 0; i < jsonArraydomain.size(); i++) {
            Grant.validateJsonElement(jsonArraydomain.get(i));
          };
        }
      }
      // validate the optional field `global`
      if (jsonObj.get("global") != null && !jsonObj.get("global").isJsonNull()) {
        GrantsResponseGlobal.validateJsonElement(jsonObj.get("global"));
      }
      if (jsonObj.get("image") != null && !jsonObj.get("image").isJsonNull()) {
        JsonArray jsonArrayimage = jsonObj.getAsJsonArray("image");
        if (jsonArrayimage != null) {
          // ensure the json data is an array
          if (!jsonObj.get("image").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `image` to be an array in the JSON string but got `%s`", jsonObj.get("image").toString()));
          }

          // validate the optional field `image` (array)
          for (int i = 0; i < jsonArrayimage.size(); i++) {
            Grant.validateJsonElement(jsonArrayimage.get(i));
          };
        }
      }
      if (jsonObj.get("linode") != null && !jsonObj.get("linode").isJsonNull()) {
        JsonArray jsonArraylinode = jsonObj.getAsJsonArray("linode");
        if (jsonArraylinode != null) {
          // ensure the json data is an array
          if (!jsonObj.get("linode").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `linode` to be an array in the JSON string but got `%s`", jsonObj.get("linode").toString()));
          }

          // validate the optional field `linode` (array)
          for (int i = 0; i < jsonArraylinode.size(); i++) {
            Grant.validateJsonElement(jsonArraylinode.get(i));
          };
        }
      }
      if (jsonObj.get("longview") != null && !jsonObj.get("longview").isJsonNull()) {
        JsonArray jsonArraylongview = jsonObj.getAsJsonArray("longview");
        if (jsonArraylongview != null) {
          // ensure the json data is an array
          if (!jsonObj.get("longview").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `longview` to be an array in the JSON string but got `%s`", jsonObj.get("longview").toString()));
          }

          // validate the optional field `longview` (array)
          for (int i = 0; i < jsonArraylongview.size(); i++) {
            Grant.validateJsonElement(jsonArraylongview.get(i));
          };
        }
      }
      if (jsonObj.get("nodebalancer") != null && !jsonObj.get("nodebalancer").isJsonNull()) {
        JsonArray jsonArraynodebalancer = jsonObj.getAsJsonArray("nodebalancer");
        if (jsonArraynodebalancer != null) {
          // ensure the json data is an array
          if (!jsonObj.get("nodebalancer").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `nodebalancer` to be an array in the JSON string but got `%s`", jsonObj.get("nodebalancer").toString()));
          }

          // validate the optional field `nodebalancer` (array)
          for (int i = 0; i < jsonArraynodebalancer.size(); i++) {
            Grant.validateJsonElement(jsonArraynodebalancer.get(i));
          };
        }
      }
      if (jsonObj.get("stackscript") != null && !jsonObj.get("stackscript").isJsonNull()) {
        JsonArray jsonArraystackscript = jsonObj.getAsJsonArray("stackscript");
        if (jsonArraystackscript != null) {
          // ensure the json data is an array
          if (!jsonObj.get("stackscript").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `stackscript` to be an array in the JSON string but got `%s`", jsonObj.get("stackscript").toString()));
          }

          // validate the optional field `stackscript` (array)
          for (int i = 0; i < jsonArraystackscript.size(); i++) {
            Grant.validateJsonElement(jsonArraystackscript.get(i));
          };
        }
      }
      if (jsonObj.get("volume") != null && !jsonObj.get("volume").isJsonNull()) {
        JsonArray jsonArrayvolume = jsonObj.getAsJsonArray("volume");
        if (jsonArrayvolume != null) {
          // ensure the json data is an array
          if (!jsonObj.get("volume").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `volume` to be an array in the JSON string but got `%s`", jsonObj.get("volume").toString()));
          }

          // validate the optional field `volume` (array)
          for (int i = 0; i < jsonArrayvolume.size(); i++) {
            Grant.validateJsonElement(jsonArrayvolume.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GrantsResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GrantsResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GrantsResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GrantsResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<GrantsResponse>() {
           @Override
           public void write(JsonWriter out, GrantsResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GrantsResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GrantsResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GrantsResponse
   * @throws IOException if the JSON string is invalid with respect to GrantsResponse
   */
  public static GrantsResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GrantsResponse.class);
  }

  /**
   * Convert an instance of GrantsResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

