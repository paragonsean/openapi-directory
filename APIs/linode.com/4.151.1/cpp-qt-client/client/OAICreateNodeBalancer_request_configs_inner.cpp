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

#include "OAICreateNodeBalancer_request_configs_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateNodeBalancer_request_configs_inner::OAICreateNodeBalancer_request_configs_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateNodeBalancer_request_configs_inner::OAICreateNodeBalancer_request_configs_inner() {
    this->initializeModel();
}

OAICreateNodeBalancer_request_configs_inner::~OAICreateNodeBalancer_request_configs_inner() {}

void OAICreateNodeBalancer_request_configs_inner::initializeModel() {

    m_algorithm_isSet = false;
    m_algorithm_isValid = false;

    m_check_isSet = false;
    m_check_isValid = false;

    m_check_attempts_isSet = false;
    m_check_attempts_isValid = false;

    m_check_body_isSet = false;
    m_check_body_isValid = false;

    m_check_interval_isSet = false;
    m_check_interval_isValid = false;

    m_check_passive_isSet = false;
    m_check_passive_isValid = false;

    m_check_path_isSet = false;
    m_check_path_isValid = false;

    m_check_timeout_isSet = false;
    m_check_timeout_isValid = false;

    m_cipher_suite_isSet = false;
    m_cipher_suite_isValid = false;

    m_nodes_isSet = false;
    m_nodes_isValid = false;

    m_port_isSet = false;
    m_port_isValid = false;

    m_protocol_isSet = false;
    m_protocol_isValid = false;

    m_proxy_protocol_isSet = false;
    m_proxy_protocol_isValid = false;

    m_ssl_cert_isSet = false;
    m_ssl_cert_isValid = false;

    m_ssl_key_isSet = false;
    m_ssl_key_isValid = false;

    m_stickiness_isSet = false;
    m_stickiness_isValid = false;
}

void OAICreateNodeBalancer_request_configs_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateNodeBalancer_request_configs_inner::fromJsonObject(QJsonObject json) {

    m_algorithm_isValid = ::OpenAPI::fromJsonValue(m_algorithm, json[QString("algorithm")]);
    m_algorithm_isSet = !json[QString("algorithm")].isNull() && m_algorithm_isValid;

    m_check_isValid = ::OpenAPI::fromJsonValue(m_check, json[QString("check")]);
    m_check_isSet = !json[QString("check")].isNull() && m_check_isValid;

    m_check_attempts_isValid = ::OpenAPI::fromJsonValue(m_check_attempts, json[QString("check_attempts")]);
    m_check_attempts_isSet = !json[QString("check_attempts")].isNull() && m_check_attempts_isValid;

    m_check_body_isValid = ::OpenAPI::fromJsonValue(m_check_body, json[QString("check_body")]);
    m_check_body_isSet = !json[QString("check_body")].isNull() && m_check_body_isValid;

    m_check_interval_isValid = ::OpenAPI::fromJsonValue(m_check_interval, json[QString("check_interval")]);
    m_check_interval_isSet = !json[QString("check_interval")].isNull() && m_check_interval_isValid;

    m_check_passive_isValid = ::OpenAPI::fromJsonValue(m_check_passive, json[QString("check_passive")]);
    m_check_passive_isSet = !json[QString("check_passive")].isNull() && m_check_passive_isValid;

    m_check_path_isValid = ::OpenAPI::fromJsonValue(m_check_path, json[QString("check_path")]);
    m_check_path_isSet = !json[QString("check_path")].isNull() && m_check_path_isValid;

    m_check_timeout_isValid = ::OpenAPI::fromJsonValue(m_check_timeout, json[QString("check_timeout")]);
    m_check_timeout_isSet = !json[QString("check_timeout")].isNull() && m_check_timeout_isValid;

    m_cipher_suite_isValid = ::OpenAPI::fromJsonValue(m_cipher_suite, json[QString("cipher_suite")]);
    m_cipher_suite_isSet = !json[QString("cipher_suite")].isNull() && m_cipher_suite_isValid;

    m_nodes_isValid = ::OpenAPI::fromJsonValue(m_nodes, json[QString("nodes")]);
    m_nodes_isSet = !json[QString("nodes")].isNull() && m_nodes_isValid;

    m_port_isValid = ::OpenAPI::fromJsonValue(m_port, json[QString("port")]);
    m_port_isSet = !json[QString("port")].isNull() && m_port_isValid;

    m_protocol_isValid = ::OpenAPI::fromJsonValue(m_protocol, json[QString("protocol")]);
    m_protocol_isSet = !json[QString("protocol")].isNull() && m_protocol_isValid;

    m_proxy_protocol_isValid = ::OpenAPI::fromJsonValue(m_proxy_protocol, json[QString("proxy_protocol")]);
    m_proxy_protocol_isSet = !json[QString("proxy_protocol")].isNull() && m_proxy_protocol_isValid;

    m_ssl_cert_isValid = ::OpenAPI::fromJsonValue(m_ssl_cert, json[QString("ssl_cert")]);
    m_ssl_cert_isSet = !json[QString("ssl_cert")].isNull() && m_ssl_cert_isValid;

    m_ssl_key_isValid = ::OpenAPI::fromJsonValue(m_ssl_key, json[QString("ssl_key")]);
    m_ssl_key_isSet = !json[QString("ssl_key")].isNull() && m_ssl_key_isValid;

    m_stickiness_isValid = ::OpenAPI::fromJsonValue(m_stickiness, json[QString("stickiness")]);
    m_stickiness_isSet = !json[QString("stickiness")].isNull() && m_stickiness_isValid;
}

QString OAICreateNodeBalancer_request_configs_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateNodeBalancer_request_configs_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_algorithm_isSet) {
        obj.insert(QString("algorithm"), ::OpenAPI::toJsonValue(m_algorithm));
    }
    if (m_check_isSet) {
        obj.insert(QString("check"), ::OpenAPI::toJsonValue(m_check));
    }
    if (m_check_attempts_isSet) {
        obj.insert(QString("check_attempts"), ::OpenAPI::toJsonValue(m_check_attempts));
    }
    if (m_check_body_isSet) {
        obj.insert(QString("check_body"), ::OpenAPI::toJsonValue(m_check_body));
    }
    if (m_check_interval_isSet) {
        obj.insert(QString("check_interval"), ::OpenAPI::toJsonValue(m_check_interval));
    }
    if (m_check_passive_isSet) {
        obj.insert(QString("check_passive"), ::OpenAPI::toJsonValue(m_check_passive));
    }
    if (m_check_path_isSet) {
        obj.insert(QString("check_path"), ::OpenAPI::toJsonValue(m_check_path));
    }
    if (m_check_timeout_isSet) {
        obj.insert(QString("check_timeout"), ::OpenAPI::toJsonValue(m_check_timeout));
    }
    if (m_cipher_suite_isSet) {
        obj.insert(QString("cipher_suite"), ::OpenAPI::toJsonValue(m_cipher_suite));
    }
    if (m_nodes.size() > 0) {
        obj.insert(QString("nodes"), ::OpenAPI::toJsonValue(m_nodes));
    }
    if (m_port_isSet) {
        obj.insert(QString("port"), ::OpenAPI::toJsonValue(m_port));
    }
    if (m_protocol_isSet) {
        obj.insert(QString("protocol"), ::OpenAPI::toJsonValue(m_protocol));
    }
    if (m_proxy_protocol_isSet) {
        obj.insert(QString("proxy_protocol"), ::OpenAPI::toJsonValue(m_proxy_protocol));
    }
    if (m_ssl_cert_isSet) {
        obj.insert(QString("ssl_cert"), ::OpenAPI::toJsonValue(m_ssl_cert));
    }
    if (m_ssl_key_isSet) {
        obj.insert(QString("ssl_key"), ::OpenAPI::toJsonValue(m_ssl_key));
    }
    if (m_stickiness_isSet) {
        obj.insert(QString("stickiness"), ::OpenAPI::toJsonValue(m_stickiness));
    }
    return obj;
}

QString OAICreateNodeBalancer_request_configs_inner::getAlgorithm() const {
    return m_algorithm;
}
void OAICreateNodeBalancer_request_configs_inner::setAlgorithm(const QString &algorithm) {
    m_algorithm = algorithm;
    m_algorithm_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_algorithm_Set() const{
    return m_algorithm_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_algorithm_Valid() const{
    return m_algorithm_isValid;
}

QString OAICreateNodeBalancer_request_configs_inner::getCheck() const {
    return m_check;
}
void OAICreateNodeBalancer_request_configs_inner::setCheck(const QString &check) {
    m_check = check;
    m_check_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_Set() const{
    return m_check_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_Valid() const{
    return m_check_isValid;
}

qint32 OAICreateNodeBalancer_request_configs_inner::getCheckAttempts() const {
    return m_check_attempts;
}
void OAICreateNodeBalancer_request_configs_inner::setCheckAttempts(const qint32 &check_attempts) {
    m_check_attempts = check_attempts;
    m_check_attempts_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_attempts_Set() const{
    return m_check_attempts_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_attempts_Valid() const{
    return m_check_attempts_isValid;
}

QString OAICreateNodeBalancer_request_configs_inner::getCheckBody() const {
    return m_check_body;
}
void OAICreateNodeBalancer_request_configs_inner::setCheckBody(const QString &check_body) {
    m_check_body = check_body;
    m_check_body_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_body_Set() const{
    return m_check_body_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_body_Valid() const{
    return m_check_body_isValid;
}

qint32 OAICreateNodeBalancer_request_configs_inner::getCheckInterval() const {
    return m_check_interval;
}
void OAICreateNodeBalancer_request_configs_inner::setCheckInterval(const qint32 &check_interval) {
    m_check_interval = check_interval;
    m_check_interval_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_interval_Set() const{
    return m_check_interval_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_interval_Valid() const{
    return m_check_interval_isValid;
}

bool OAICreateNodeBalancer_request_configs_inner::isCheckPassive() const {
    return m_check_passive;
}
void OAICreateNodeBalancer_request_configs_inner::setCheckPassive(const bool &check_passive) {
    m_check_passive = check_passive;
    m_check_passive_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_passive_Set() const{
    return m_check_passive_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_passive_Valid() const{
    return m_check_passive_isValid;
}

QString OAICreateNodeBalancer_request_configs_inner::getCheckPath() const {
    return m_check_path;
}
void OAICreateNodeBalancer_request_configs_inner::setCheckPath(const QString &check_path) {
    m_check_path = check_path;
    m_check_path_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_path_Set() const{
    return m_check_path_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_path_Valid() const{
    return m_check_path_isValid;
}

qint32 OAICreateNodeBalancer_request_configs_inner::getCheckTimeout() const {
    return m_check_timeout;
}
void OAICreateNodeBalancer_request_configs_inner::setCheckTimeout(const qint32 &check_timeout) {
    m_check_timeout = check_timeout;
    m_check_timeout_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_timeout_Set() const{
    return m_check_timeout_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_check_timeout_Valid() const{
    return m_check_timeout_isValid;
}

QString OAICreateNodeBalancer_request_configs_inner::getCipherSuite() const {
    return m_cipher_suite;
}
void OAICreateNodeBalancer_request_configs_inner::setCipherSuite(const QString &cipher_suite) {
    m_cipher_suite = cipher_suite;
    m_cipher_suite_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_cipher_suite_Set() const{
    return m_cipher_suite_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_cipher_suite_Valid() const{
    return m_cipher_suite_isValid;
}

QList<OAINodeBalancerNode> OAICreateNodeBalancer_request_configs_inner::getNodes() const {
    return m_nodes;
}
void OAICreateNodeBalancer_request_configs_inner::setNodes(const QList<OAINodeBalancerNode> &nodes) {
    m_nodes = nodes;
    m_nodes_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_nodes_Set() const{
    return m_nodes_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_nodes_Valid() const{
    return m_nodes_isValid;
}

qint32 OAICreateNodeBalancer_request_configs_inner::getPort() const {
    return m_port;
}
void OAICreateNodeBalancer_request_configs_inner::setPort(const qint32 &port) {
    m_port = port;
    m_port_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_port_Set() const{
    return m_port_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_port_Valid() const{
    return m_port_isValid;
}

QString OAICreateNodeBalancer_request_configs_inner::getProtocol() const {
    return m_protocol;
}
void OAICreateNodeBalancer_request_configs_inner::setProtocol(const QString &protocol) {
    m_protocol = protocol;
    m_protocol_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_protocol_Set() const{
    return m_protocol_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_protocol_Valid() const{
    return m_protocol_isValid;
}

QString OAICreateNodeBalancer_request_configs_inner::getProxyProtocol() const {
    return m_proxy_protocol;
}
void OAICreateNodeBalancer_request_configs_inner::setProxyProtocol(const QString &proxy_protocol) {
    m_proxy_protocol = proxy_protocol;
    m_proxy_protocol_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_proxy_protocol_Set() const{
    return m_proxy_protocol_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_proxy_protocol_Valid() const{
    return m_proxy_protocol_isValid;
}

QString OAICreateNodeBalancer_request_configs_inner::getSslCert() const {
    return m_ssl_cert;
}
void OAICreateNodeBalancer_request_configs_inner::setSslCert(const QString &ssl_cert) {
    m_ssl_cert = ssl_cert;
    m_ssl_cert_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_ssl_cert_Set() const{
    return m_ssl_cert_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_ssl_cert_Valid() const{
    return m_ssl_cert_isValid;
}

QString OAICreateNodeBalancer_request_configs_inner::getSslKey() const {
    return m_ssl_key;
}
void OAICreateNodeBalancer_request_configs_inner::setSslKey(const QString &ssl_key) {
    m_ssl_key = ssl_key;
    m_ssl_key_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_ssl_key_Set() const{
    return m_ssl_key_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_ssl_key_Valid() const{
    return m_ssl_key_isValid;
}

QString OAICreateNodeBalancer_request_configs_inner::getStickiness() const {
    return m_stickiness;
}
void OAICreateNodeBalancer_request_configs_inner::setStickiness(const QString &stickiness) {
    m_stickiness = stickiness;
    m_stickiness_isSet = true;
}

bool OAICreateNodeBalancer_request_configs_inner::is_stickiness_Set() const{
    return m_stickiness_isSet;
}

bool OAICreateNodeBalancer_request_configs_inner::is_stickiness_Valid() const{
    return m_stickiness_isValid;
}

bool OAICreateNodeBalancer_request_configs_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_algorithm_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_check_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_check_attempts_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_check_body_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_check_interval_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_check_passive_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_check_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_check_timeout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cipher_suite_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nodes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_port_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_protocol_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_proxy_protocol_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ssl_cert_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ssl_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stickiness_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateNodeBalancer_request_configs_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
