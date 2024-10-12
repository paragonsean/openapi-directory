/**
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

#include "OAICreateLinodeInstance_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateLinodeInstance_request::OAICreateLinodeInstance_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateLinodeInstance_request::OAICreateLinodeInstance_request() {
    this->initializeModel();
}

OAICreateLinodeInstance_request::~OAICreateLinodeInstance_request() {}

void OAICreateLinodeInstance_request::initializeModel() {

    m_authorized_keys_isSet = false;
    m_authorized_keys_isValid = false;

    m_authorized_users_isSet = false;
    m_authorized_users_isValid = false;

    m_booted_isSet = false;
    m_booted_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_root_pass_isSet = false;
    m_root_pass_isValid = false;

    m_stackscript_data_isSet = false;
    m_stackscript_data_isValid = false;

    m_stackscript_id_isSet = false;
    m_stackscript_id_isValid = false;

    m_backup_id_isSet = false;
    m_backup_id_isValid = false;

    m_backups_enabled_isSet = false;
    m_backups_enabled_isValid = false;

    m_group_isSet = false;
    m_group_isValid = false;

    m_interfaces_isSet = false;
    m_interfaces_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;

    m_private_ip_isSet = false;
    m_private_ip_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_swap_size_isSet = false;
    m_swap_size_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAICreateLinodeInstance_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateLinodeInstance_request::fromJsonObject(QJsonObject json) {

    m_authorized_keys_isValid = ::OpenAPI::fromJsonValue(m_authorized_keys, json[QString("authorized_keys")]);
    m_authorized_keys_isSet = !json[QString("authorized_keys")].isNull() && m_authorized_keys_isValid;

    m_authorized_users_isValid = ::OpenAPI::fromJsonValue(m_authorized_users, json[QString("authorized_users")]);
    m_authorized_users_isSet = !json[QString("authorized_users")].isNull() && m_authorized_users_isValid;

    m_booted_isValid = ::OpenAPI::fromJsonValue(m_booted, json[QString("booted")]);
    m_booted_isSet = !json[QString("booted")].isNull() && m_booted_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_root_pass_isValid = ::OpenAPI::fromJsonValue(m_root_pass, json[QString("root_pass")]);
    m_root_pass_isSet = !json[QString("root_pass")].isNull() && m_root_pass_isValid;

    m_stackscript_data_isValid = ::OpenAPI::fromJsonValue(m_stackscript_data, json[QString("stackscript_data")]);
    m_stackscript_data_isSet = !json[QString("stackscript_data")].isNull() && m_stackscript_data_isValid;

    m_stackscript_id_isValid = ::OpenAPI::fromJsonValue(m_stackscript_id, json[QString("stackscript_id")]);
    m_stackscript_id_isSet = !json[QString("stackscript_id")].isNull() && m_stackscript_id_isValid;

    m_backup_id_isValid = ::OpenAPI::fromJsonValue(m_backup_id, json[QString("backup_id")]);
    m_backup_id_isSet = !json[QString("backup_id")].isNull() && m_backup_id_isValid;

    m_backups_enabled_isValid = ::OpenAPI::fromJsonValue(m_backups_enabled, json[QString("backups_enabled")]);
    m_backups_enabled_isSet = !json[QString("backups_enabled")].isNull() && m_backups_enabled_isValid;

    m_group_isValid = ::OpenAPI::fromJsonValue(m_group, json[QString("group")]);
    m_group_isSet = !json[QString("group")].isNull() && m_group_isValid;

    m_interfaces_isValid = ::OpenAPI::fromJsonValue(m_interfaces, json[QString("interfaces")]);
    m_interfaces_isSet = !json[QString("interfaces")].isNull() && m_interfaces_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_private_ip_isValid = ::OpenAPI::fromJsonValue(m_private_ip, json[QString("private_ip")]);
    m_private_ip_isSet = !json[QString("private_ip")].isNull() && m_private_ip_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_swap_size_isValid = ::OpenAPI::fromJsonValue(m_swap_size, json[QString("swap_size")]);
    m_swap_size_isSet = !json[QString("swap_size")].isNull() && m_swap_size_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAICreateLinodeInstance_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateLinodeInstance_request::asJsonObject() const {
    QJsonObject obj;
    if (m_authorized_keys.size() > 0) {
        obj.insert(QString("authorized_keys"), ::OpenAPI::toJsonValue(m_authorized_keys));
    }
    if (m_authorized_users.size() > 0) {
        obj.insert(QString("authorized_users"), ::OpenAPI::toJsonValue(m_authorized_users));
    }
    if (m_booted_isSet) {
        obj.insert(QString("booted"), ::OpenAPI::toJsonValue(m_booted));
    }
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_root_pass_isSet) {
        obj.insert(QString("root_pass"), ::OpenAPI::toJsonValue(m_root_pass));
    }
    if (m_stackscript_data_isSet) {
        obj.insert(QString("stackscript_data"), ::OpenAPI::toJsonValue(m_stackscript_data));
    }
    if (m_stackscript_id_isSet) {
        obj.insert(QString("stackscript_id"), ::OpenAPI::toJsonValue(m_stackscript_id));
    }
    if (m_backup_id_isSet) {
        obj.insert(QString("backup_id"), ::OpenAPI::toJsonValue(m_backup_id));
    }
    if (m_backups_enabled_isSet) {
        obj.insert(QString("backups_enabled"), ::OpenAPI::toJsonValue(m_backups_enabled));
    }
    if (m_group_isSet) {
        obj.insert(QString("group"), ::OpenAPI::toJsonValue(m_group));
    }
    if (m_interfaces.size() > 0) {
        obj.insert(QString("interfaces"), ::OpenAPI::toJsonValue(m_interfaces));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_private_ip_isSet) {
        obj.insert(QString("private_ip"), ::OpenAPI::toJsonValue(m_private_ip));
    }
    if (m_region_isSet) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_swap_size_isSet) {
        obj.insert(QString("swap_size"), ::OpenAPI::toJsonValue(m_swap_size));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QList<QString> OAICreateLinodeInstance_request::getAuthorizedKeys() const {
    return m_authorized_keys;
}
void OAICreateLinodeInstance_request::setAuthorizedKeys(const QList<QString> &authorized_keys) {
    m_authorized_keys = authorized_keys;
    m_authorized_keys_isSet = true;
}

bool OAICreateLinodeInstance_request::is_authorized_keys_Set() const{
    return m_authorized_keys_isSet;
}

bool OAICreateLinodeInstance_request::is_authorized_keys_Valid() const{
    return m_authorized_keys_isValid;
}

QList<QString> OAICreateLinodeInstance_request::getAuthorizedUsers() const {
    return m_authorized_users;
}
void OAICreateLinodeInstance_request::setAuthorizedUsers(const QList<QString> &authorized_users) {
    m_authorized_users = authorized_users;
    m_authorized_users_isSet = true;
}

bool OAICreateLinodeInstance_request::is_authorized_users_Set() const{
    return m_authorized_users_isSet;
}

bool OAICreateLinodeInstance_request::is_authorized_users_Valid() const{
    return m_authorized_users_isValid;
}

bool OAICreateLinodeInstance_request::isBooted() const {
    return m_booted;
}
void OAICreateLinodeInstance_request::setBooted(const bool &booted) {
    m_booted = booted;
    m_booted_isSet = true;
}

bool OAICreateLinodeInstance_request::is_booted_Set() const{
    return m_booted_isSet;
}

bool OAICreateLinodeInstance_request::is_booted_Valid() const{
    return m_booted_isValid;
}

QString OAICreateLinodeInstance_request::getImage() const {
    return m_image;
}
void OAICreateLinodeInstance_request::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAICreateLinodeInstance_request::is_image_Set() const{
    return m_image_isSet;
}

bool OAICreateLinodeInstance_request::is_image_Valid() const{
    return m_image_isValid;
}

QString OAICreateLinodeInstance_request::getRootPass() const {
    return m_root_pass;
}
void OAICreateLinodeInstance_request::setRootPass(const QString &root_pass) {
    m_root_pass = root_pass;
    m_root_pass_isSet = true;
}

bool OAICreateLinodeInstance_request::is_root_pass_Set() const{
    return m_root_pass_isSet;
}

bool OAICreateLinodeInstance_request::is_root_pass_Valid() const{
    return m_root_pass_isValid;
}

OAIObject OAICreateLinodeInstance_request::getStackscriptData() const {
    return m_stackscript_data;
}
void OAICreateLinodeInstance_request::setStackscriptData(const OAIObject &stackscript_data) {
    m_stackscript_data = stackscript_data;
    m_stackscript_data_isSet = true;
}

bool OAICreateLinodeInstance_request::is_stackscript_data_Set() const{
    return m_stackscript_data_isSet;
}

bool OAICreateLinodeInstance_request::is_stackscript_data_Valid() const{
    return m_stackscript_data_isValid;
}

qint32 OAICreateLinodeInstance_request::getStackscriptId() const {
    return m_stackscript_id;
}
void OAICreateLinodeInstance_request::setStackscriptId(const qint32 &stackscript_id) {
    m_stackscript_id = stackscript_id;
    m_stackscript_id_isSet = true;
}

bool OAICreateLinodeInstance_request::is_stackscript_id_Set() const{
    return m_stackscript_id_isSet;
}

bool OAICreateLinodeInstance_request::is_stackscript_id_Valid() const{
    return m_stackscript_id_isValid;
}

qint32 OAICreateLinodeInstance_request::getBackupId() const {
    return m_backup_id;
}
void OAICreateLinodeInstance_request::setBackupId(const qint32 &backup_id) {
    m_backup_id = backup_id;
    m_backup_id_isSet = true;
}

bool OAICreateLinodeInstance_request::is_backup_id_Set() const{
    return m_backup_id_isSet;
}

bool OAICreateLinodeInstance_request::is_backup_id_Valid() const{
    return m_backup_id_isValid;
}

bool OAICreateLinodeInstance_request::isBackupsEnabled() const {
    return m_backups_enabled;
}
void OAICreateLinodeInstance_request::setBackupsEnabled(const bool &backups_enabled) {
    m_backups_enabled = backups_enabled;
    m_backups_enabled_isSet = true;
}

bool OAICreateLinodeInstance_request::is_backups_enabled_Set() const{
    return m_backups_enabled_isSet;
}

bool OAICreateLinodeInstance_request::is_backups_enabled_Valid() const{
    return m_backups_enabled_isValid;
}

QString OAICreateLinodeInstance_request::getGroup() const {
    return m_group;
}
void OAICreateLinodeInstance_request::setGroup(const QString &group) {
    m_group = group;
    m_group_isSet = true;
}

bool OAICreateLinodeInstance_request::is_group_Set() const{
    return m_group_isSet;
}

bool OAICreateLinodeInstance_request::is_group_Valid() const{
    return m_group_isValid;
}

QList<OAILinodeConfigInterface> OAICreateLinodeInstance_request::getInterfaces() const {
    return m_interfaces;
}
void OAICreateLinodeInstance_request::setInterfaces(const QList<OAILinodeConfigInterface> &interfaces) {
    m_interfaces = interfaces;
    m_interfaces_isSet = true;
}

bool OAICreateLinodeInstance_request::is_interfaces_Set() const{
    return m_interfaces_isSet;
}

bool OAICreateLinodeInstance_request::is_interfaces_Valid() const{
    return m_interfaces_isValid;
}

QString OAICreateLinodeInstance_request::getLabel() const {
    return m_label;
}
void OAICreateLinodeInstance_request::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAICreateLinodeInstance_request::is_label_Set() const{
    return m_label_isSet;
}

bool OAICreateLinodeInstance_request::is_label_Valid() const{
    return m_label_isValid;
}

bool OAICreateLinodeInstance_request::isPrivateIp() const {
    return m_private_ip;
}
void OAICreateLinodeInstance_request::setPrivateIp(const bool &private_ip) {
    m_private_ip = private_ip;
    m_private_ip_isSet = true;
}

bool OAICreateLinodeInstance_request::is_private_ip_Set() const{
    return m_private_ip_isSet;
}

bool OAICreateLinodeInstance_request::is_private_ip_Valid() const{
    return m_private_ip_isValid;
}

QString OAICreateLinodeInstance_request::getRegion() const {
    return m_region;
}
void OAICreateLinodeInstance_request::setRegion(const QString &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAICreateLinodeInstance_request::is_region_Set() const{
    return m_region_isSet;
}

bool OAICreateLinodeInstance_request::is_region_Valid() const{
    return m_region_isValid;
}

qint32 OAICreateLinodeInstance_request::getSwapSize() const {
    return m_swap_size;
}
void OAICreateLinodeInstance_request::setSwapSize(const qint32 &swap_size) {
    m_swap_size = swap_size;
    m_swap_size_isSet = true;
}

bool OAICreateLinodeInstance_request::is_swap_size_Set() const{
    return m_swap_size_isSet;
}

bool OAICreateLinodeInstance_request::is_swap_size_Valid() const{
    return m_swap_size_isValid;
}

QList<QString> OAICreateLinodeInstance_request::getTags() const {
    return m_tags;
}
void OAICreateLinodeInstance_request::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAICreateLinodeInstance_request::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAICreateLinodeInstance_request::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAICreateLinodeInstance_request::getType() const {
    return m_type;
}
void OAICreateLinodeInstance_request::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAICreateLinodeInstance_request::is_type_Set() const{
    return m_type_isSet;
}

bool OAICreateLinodeInstance_request::is_type_Valid() const{
    return m_type_isValid;
}

bool OAICreateLinodeInstance_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_authorized_keys.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_authorized_users.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_booted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_root_pass_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stackscript_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stackscript_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_backup_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_backups_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_interfaces.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_private_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_swap_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateLinodeInstance_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_region_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
