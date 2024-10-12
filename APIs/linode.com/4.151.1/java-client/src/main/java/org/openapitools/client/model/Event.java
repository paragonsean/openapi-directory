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
import java.math.BigDecimal;
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.EventEntity;
import org.openapitools.client.model.EventSecondaryEntity;
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
 * A collection of Event objects. An Event is an action taken against an entity related to your Account. For example, booting a Linode would create an Event. The Events returned depends on your grants. 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:42.346741-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Event {
  /**
   * The action that caused this Event. New actions may be added in the future. 
   */
  @JsonAdapter(ActionEnum.Adapter.class)
  public enum ActionEnum {
    ACCOUNT_UPDATE("account_update"),
    
    ACCOUNT_SETTINGS_UPDATE("account_settings_update"),
    
    BACKUPS_ENABLE("backups_enable"),
    
    BACKUPS_CANCEL("backups_cancel"),
    
    BACKUPS_RESTORE("backups_restore"),
    
    COMMUNITY_QUESTION_REPLY("community_question_reply"),
    
    COMMUNITY_LIKE("community_like"),
    
    CREDIT_CARD_UPDATED("credit_card_updated"),
    
    DISK_CREATE("disk_create"),
    
    DISK_DELETE("disk_delete"),
    
    DISK_UPDATE("disk_update"),
    
    DISK_DUPLICATE("disk_duplicate"),
    
    DISK_IMAGIZE("disk_imagize"),
    
    DISK_RESIZE("disk_resize"),
    
    DNS_RECORD_CREATE("dns_record_create"),
    
    DNS_RECORD_DELETE("dns_record_delete"),
    
    DNS_RECORD_UPDATE("dns_record_update"),
    
    DNS_ZONE_CREATE("dns_zone_create"),
    
    DNS_ZONE_DELETE("dns_zone_delete"),
    
    DNS_ZONE_IMPORT("dns_zone_import"),
    
    DNS_ZONE_UPDATE("dns_zone_update"),
    
    ENTITY_TRANSFER_ACCEPT("entity_transfer_accept"),
    
    ENTITY_TRANSFER_CANCEL("entity_transfer_cancel"),
    
    ENTITY_TRANSFER_CREATE("entity_transfer_create"),
    
    ENTITY_TRANSFER_FAIL("entity_transfer_fail"),
    
    ENTITY_TRANSFER_STALE("entity_transfer_stale"),
    
    FIREWALL_CREATE("firewall_create"),
    
    FIREWALL_DELETE("firewall_delete"),
    
    FIREWALL_DISABLE("firewall_disable"),
    
    FIREWALL_ENABLE("firewall_enable"),
    
    FIREWALL_UPDATE("firewall_update"),
    
    FIREWALL_DEVICE_ADD("firewall_device_add"),
    
    FIREWALL_DEVICE_REMOVE("firewall_device_remove"),
    
    HOST_REBOOT("host_reboot"),
    
    IMAGE_DELETE("image_delete"),
    
    IMAGE_UPDATE("image_update"),
    
    IMAGE_UPLOAD("image_upload"),
    
    IPADDRESS_UPDATE("ipaddress_update"),
    
    LASSIE_REBOOT("lassie_reboot"),
    
    LISH_BOOT("lish_boot"),
    
    LINODE_ADDIP("linode_addip"),
    
    LINODE_BOOT("linode_boot"),
    
    LINODE_CLONE("linode_clone"),
    
    LINODE_CREATE("linode_create"),
    
    LINODE_DELETE("linode_delete"),
    
    LINODE_UPDATE("linode_update"),
    
    LINODE_DELETEIP("linode_deleteip"),
    
    LINODE_MIGRATE("linode_migrate"),
    
    LINODE_MIGRATE_DATACENTER("linode_migrate_datacenter"),
    
    LINODE_MIGRATE_DATACENTER_CREATE("linode_migrate_datacenter_create"),
    
    LINODE_MUTATE("linode_mutate"),
    
    LINODE_MUTATE_CREATE("linode_mutate_create"),
    
    LINODE_REBOOT("linode_reboot"),
    
    LINODE_REBUILD("linode_rebuild"),
    
    LINODE_RESIZE("linode_resize"),
    
    LINODE_RESIZE_CREATE("linode_resize_create"),
    
    LINODE_SHUTDOWN("linode_shutdown"),
    
    LINODE_SNAPSHOT("linode_snapshot"),
    
    LINODE_CONFIG_CREATE("linode_config_create"),
    
    LINODE_CONFIG_DELETE("linode_config_delete"),
    
    LINODE_CONFIG_UPDATE("linode_config_update"),
    
    LKE_NODE_CREATE("lke_node_create"),
    
    LONGVIEWCLIENT_CREATE("longviewclient_create"),
    
    LONGVIEWCLIENT_DELETE("longviewclient_delete"),
    
    LONGVIEWCLIENT_UPDATE("longviewclient_update"),
    
    MANAGED_DISABLED("managed_disabled"),
    
    MANAGED_ENABLED("managed_enabled"),
    
    MANAGED_SERVICE_CREATE("managed_service_create"),
    
    MANAGED_SERVICE_DELETE("managed_service_delete"),
    
    NODEBALANCER_CREATE("nodebalancer_create"),
    
    NODEBALANCER_DELETE("nodebalancer_delete"),
    
    NODEBALANCER_UPDATE("nodebalancer_update"),
    
    NODEBALANCER_CONFIG_CREATE("nodebalancer_config_create"),
    
    NODEBALANCER_CONFIG_DELETE("nodebalancer_config_delete"),
    
    NODEBALANCER_CONFIG_UPDATE("nodebalancer_config_update"),
    
    NODEBALANCER_NODE_CREATE("nodebalancer_node_create"),
    
    NODEBALANCER_NODE_DELETE("nodebalancer_node_delete"),
    
    NODEBALANCER_NODE_UPDATE("nodebalancer_node_update"),
    
    OAUTH_CLIENT_CREATE("oauth_client_create"),
    
    OAUTH_CLIENT_DELETE("oauth_client_delete"),
    
    OAUTH_CLIENT_SECRET_RESET("oauth_client_secret_reset"),
    
    OAUTH_CLIENT_UPDATE("oauth_client_update"),
    
    PASSWORD_RESET("password_reset"),
    
    PAYMENT_METHOD_ADD("payment_method_add"),
    
    PAYMENT_SUBMITTED("payment_submitted"),
    
    PROFILE_UPDATE("profile_update"),
    
    STACKSCRIPT_CREATE("stackscript_create"),
    
    STACKSCRIPT_DELETE("stackscript_delete"),
    
    STACKSCRIPT_UPDATE("stackscript_update"),
    
    STACKSCRIPT_PUBLICIZE("stackscript_publicize"),
    
    STACKSCRIPT_REVISE("stackscript_revise"),
    
    TAG_CREATE("tag_create"),
    
    TAG_DELETE("tag_delete"),
    
    TFA_DISABLED("tfa_disabled"),
    
    TFA_ENABLED("tfa_enabled"),
    
    TICKET_ATTACHMENT_UPLOAD("ticket_attachment_upload"),
    
    TICKET_CREATE("ticket_create"),
    
    TICKET_UPDATE("ticket_update"),
    
    TOKEN_CREATE("token_create"),
    
    TOKEN_DELETE("token_delete"),
    
    TOKEN_UPDATE("token_update"),
    
    USER_CREATE("user_create"),
    
    USER_UPDATE("user_update"),
    
    USER_DELETE("user_delete"),
    
    USER_SSH_KEY_ADD("user_ssh_key_add"),
    
    USER_SSH_KEY_DELETE("user_ssh_key_delete"),
    
    USER_SSH_KEY_UPDATE("user_ssh_key_update"),
    
    VLAN_ATTACH("vlan_attach"),
    
    VLAN_DETACH("vlan_detach"),
    
    VOLUME_ATTACH("volume_attach"),
    
    VOLUME_CLONE("volume_clone"),
    
    VOLUME_CREATE("volume_create"),
    
    VOLUME_DELETE("volume_delete"),
    
    VOLUME_UPDATE("volume_update"),
    
    VOLUME_DETACH("volume_detach"),
    
    VOLUME_RESIZE("volume_resize");

    private String value;

    ActionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ActionEnum fromValue(String value) {
      for (ActionEnum b : ActionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ActionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ActionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ActionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ActionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ActionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ACTION = "action";
  @SerializedName(SERIALIZED_NAME_ACTION)
  private ActionEnum action;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private OffsetDateTime created;

  public static final String SERIALIZED_NAME_DURATION = "duration";
  @SerializedName(SERIALIZED_NAME_DURATION)
  private BigDecimal duration;

  public static final String SERIALIZED_NAME_ENTITY = "entity";
  @SerializedName(SERIALIZED_NAME_ENTITY)
  private EventEntity entity;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_PERCENT_COMPLETE = "percent_complete";
  @SerializedName(SERIALIZED_NAME_PERCENT_COMPLETE)
  private Integer percentComplete;

  public static final String SERIALIZED_NAME_RATE = "rate";
  @SerializedName(SERIALIZED_NAME_RATE)
  private String rate;

  public static final String SERIALIZED_NAME_READ = "read";
  @SerializedName(SERIALIZED_NAME_READ)
  private Boolean read;

  public static final String SERIALIZED_NAME_SECONDARY_ENTITY = "secondary_entity";
  @SerializedName(SERIALIZED_NAME_SECONDARY_ENTITY)
  private EventSecondaryEntity secondaryEntity;

  public static final String SERIALIZED_NAME_SEEN = "seen";
  @SerializedName(SERIALIZED_NAME_SEEN)
  private Boolean seen;

  /**
   * The current status of this Event.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    FAILED("failed"),
    
    FINISHED("finished"),
    
    NOTIFICATION("notification"),
    
    SCHEDULED("scheduled"),
    
    STARTED("started");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_TIME_REMAINING = "time_remaining";
  @SerializedName(SERIALIZED_NAME_TIME_REMAINING)
  private String timeRemaining;

  public static final String SERIALIZED_NAME_USERNAME = "username";
  @SerializedName(SERIALIZED_NAME_USERNAME)
  private String username;

  public Event() {
  }

  public Event(
     ActionEnum action, 
     OffsetDateTime created, 
     BigDecimal duration, 
     Integer id, 
     Integer percentComplete, 
     String rate, 
     Boolean read, 
     Boolean seen, 
     StatusEnum status, 
     String timeRemaining, 
     String username
  ) {
    this();
    this.action = action;
    this.created = created;
    this.duration = duration;
    this.id = id;
    this.percentComplete = percentComplete;
    this.rate = rate;
    this.read = read;
    this.seen = seen;
    this.status = status;
    this.timeRemaining = timeRemaining;
    this.username = username;
  }

  /**
   * The action that caused this Event. New actions may be added in the future. 
   * @return action
   */
  @javax.annotation.Nullable
  public ActionEnum getAction() {
    return action;
  }



  /**
   * When this Event was created.
   * @return created
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreated() {
    return created;
  }



  /**
   * The total duration in seconds that it takes for the Event to complete. 
   * @return duration
   */
  @javax.annotation.Nullable
  public BigDecimal getDuration() {
    return duration;
  }



  public Event entity(EventEntity entity) {
    this.entity = entity;
    return this;
  }

  /**
   * Get entity
   * @return entity
   */
  @javax.annotation.Nullable
  public EventEntity getEntity() {
    return entity;
  }

  public void setEntity(EventEntity entity) {
    this.entity = entity;
  }


  /**
   * The unique ID of this Event.
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public Event message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Provides additional information about the event. Additional information may include, but is not limited to, a more detailed representation of events which can help diagnose non-obvious failures. 
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  /**
   * A percentage estimating the amount of time remaining for an Event. Returns &#x60;null&#x60; for notification events. 
   * @return percentComplete
   */
  @javax.annotation.Nullable
  public Integer getPercentComplete() {
    return percentComplete;
  }



  /**
   * The rate of completion of the Event. Only some Events will return rate; for example, migration and resize Events. 
   * @return rate
   */
  @javax.annotation.Nullable
  public String getRate() {
    return rate;
  }



  /**
   * If this Event has been read.
   * @return read
   */
  @javax.annotation.Nullable
  public Boolean getRead() {
    return read;
  }



  public Event secondaryEntity(EventSecondaryEntity secondaryEntity) {
    this.secondaryEntity = secondaryEntity;
    return this;
  }

  /**
   * Get secondaryEntity
   * @return secondaryEntity
   */
  @javax.annotation.Nullable
  public EventSecondaryEntity getSecondaryEntity() {
    return secondaryEntity;
  }

  public void setSecondaryEntity(EventSecondaryEntity secondaryEntity) {
    this.secondaryEntity = secondaryEntity;
  }


  /**
   * If this Event has been seen.
   * @return seen
   */
  @javax.annotation.Nullable
  public Boolean getSeen() {
    return seen;
  }



  /**
   * The current status of this Event.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }



  /**
   * The estimated time remaining until the completion of this Event. This value is only returned for some in-progress migration events. For all other in-progress events, the &#x60;percent_complete&#x60; attribute will indicate about how much more work is to be done. 
   * @return timeRemaining
   */
  @javax.annotation.Nullable
  public String getTimeRemaining() {
    return timeRemaining;
  }



  /**
   * The username of the User who caused the Event. 
   * @return username
   */
  @javax.annotation.Nullable
  public String getUsername() {
    return username;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Event event = (Event) o;
    return Objects.equals(this.action, event.action) &&
        Objects.equals(this.created, event.created) &&
        Objects.equals(this.duration, event.duration) &&
        Objects.equals(this.entity, event.entity) &&
        Objects.equals(this.id, event.id) &&
        Objects.equals(this.message, event.message) &&
        Objects.equals(this.percentComplete, event.percentComplete) &&
        Objects.equals(this.rate, event.rate) &&
        Objects.equals(this.read, event.read) &&
        Objects.equals(this.secondaryEntity, event.secondaryEntity) &&
        Objects.equals(this.seen, event.seen) &&
        Objects.equals(this.status, event.status) &&
        Objects.equals(this.timeRemaining, event.timeRemaining) &&
        Objects.equals(this.username, event.username);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(action, created, duration, entity, id, message, percentComplete, rate, read, secondaryEntity, seen, status, timeRemaining, username);
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
    sb.append("class Event {\n");
    sb.append("    action: ").append(toIndentedString(action)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    entity: ").append(toIndentedString(entity)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    percentComplete: ").append(toIndentedString(percentComplete)).append("\n");
    sb.append("    rate: ").append(toIndentedString(rate)).append("\n");
    sb.append("    read: ").append(toIndentedString(read)).append("\n");
    sb.append("    secondaryEntity: ").append(toIndentedString(secondaryEntity)).append("\n");
    sb.append("    seen: ").append(toIndentedString(seen)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    timeRemaining: ").append(toIndentedString(timeRemaining)).append("\n");
    sb.append("    username: ").append(toIndentedString(username)).append("\n");
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
    openapiFields.add("action");
    openapiFields.add("created");
    openapiFields.add("duration");
    openapiFields.add("entity");
    openapiFields.add("id");
    openapiFields.add("message");
    openapiFields.add("percent_complete");
    openapiFields.add("rate");
    openapiFields.add("read");
    openapiFields.add("secondary_entity");
    openapiFields.add("seen");
    openapiFields.add("status");
    openapiFields.add("time_remaining");
    openapiFields.add("username");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Event
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Event.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Event is not found in the empty JSON string", Event.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Event.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Event` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("action") != null && !jsonObj.get("action").isJsonNull()) && !jsonObj.get("action").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `action` to be a primitive type in the JSON string but got `%s`", jsonObj.get("action").toString()));
      }
      // validate the optional field `action`
      if (jsonObj.get("action") != null && !jsonObj.get("action").isJsonNull()) {
        ActionEnum.validateJsonElement(jsonObj.get("action"));
      }
      // validate the optional field `entity`
      if (jsonObj.get("entity") != null && !jsonObj.get("entity").isJsonNull()) {
        EventEntity.validateJsonElement(jsonObj.get("entity"));
      }
      if ((jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) && !jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
      if ((jsonObj.get("rate") != null && !jsonObj.get("rate").isJsonNull()) && !jsonObj.get("rate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rate").toString()));
      }
      // validate the optional field `secondary_entity`
      if (jsonObj.get("secondary_entity") != null && !jsonObj.get("secondary_entity").isJsonNull()) {
        EventSecondaryEntity.validateJsonElement(jsonObj.get("secondary_entity"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("time_remaining") != null && !jsonObj.get("time_remaining").isJsonNull()) && !jsonObj.get("time_remaining").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `time_remaining` to be a primitive type in the JSON string but got `%s`", jsonObj.get("time_remaining").toString()));
      }
      if ((jsonObj.get("username") != null && !jsonObj.get("username").isJsonNull()) && !jsonObj.get("username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("username").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Event.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Event' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Event> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Event.class));

       return (TypeAdapter<T>) new TypeAdapter<Event>() {
           @Override
           public void write(JsonWriter out, Event value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Event read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Event given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Event
   * @throws IOException if the JSON string is invalid with respect to Event
   */
  public static Event fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Event.class);
  }

  /**
   * Convert an instance of Event to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

