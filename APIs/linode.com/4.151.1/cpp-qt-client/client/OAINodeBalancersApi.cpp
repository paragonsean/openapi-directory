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

#include "OAINodeBalancersApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAINodeBalancersApi::OAINodeBalancersApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAINodeBalancersApi::~OAINodeBalancersApi() {
}

void OAINodeBalancersApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.linode.com/v4"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.linode.com/v4beta"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("createNodeBalancer", defaultConf);
    _serverIndices.insert("createNodeBalancer", 0);
    _serverConfigs.insert("createNodeBalancerConfig", defaultConf);
    _serverIndices.insert("createNodeBalancerConfig", 0);
    _serverConfigs.insert("createNodeBalancerNode", defaultConf);
    _serverIndices.insert("createNodeBalancerNode", 0);
    _serverConfigs.insert("deleteNodeBalancer", defaultConf);
    _serverIndices.insert("deleteNodeBalancer", 0);
    _serverConfigs.insert("deleteNodeBalancerConfig", defaultConf);
    _serverIndices.insert("deleteNodeBalancerConfig", 0);
    _serverConfigs.insert("deleteNodeBalancerConfigNode", defaultConf);
    _serverIndices.insert("deleteNodeBalancerConfigNode", 0);
    _serverConfigs.insert("getNodeBalancer", defaultConf);
    _serverIndices.insert("getNodeBalancer", 0);
    _serverConfigs.insert("getNodeBalancerConfig", defaultConf);
    _serverIndices.insert("getNodeBalancerConfig", 0);
    _serverConfigs.insert("getNodeBalancerConfigNodes", defaultConf);
    _serverIndices.insert("getNodeBalancerConfigNodes", 0);
    _serverConfigs.insert("getNodeBalancerConfigs", defaultConf);
    _serverIndices.insert("getNodeBalancerConfigs", 0);
    _serverConfigs.insert("getNodeBalancerNode", defaultConf);
    _serverIndices.insert("getNodeBalancerNode", 0);
    _serverConfigs.insert("getNodeBalancers", defaultConf);
    _serverIndices.insert("getNodeBalancers", 0);
    _serverConfigs.insert("nodebalancersNodeBalancerIdStatsGet", defaultConf);
    _serverIndices.insert("nodebalancersNodeBalancerIdStatsGet", 0);
    _serverConfigs.insert("rebuildNodeBalancerConfig", defaultConf);
    _serverIndices.insert("rebuildNodeBalancerConfig", 0);
    _serverConfigs.insert("updateNodeBalancer", defaultConf);
    _serverIndices.insert("updateNodeBalancer", 0);
    _serverConfigs.insert("updateNodeBalancerConfig", defaultConf);
    _serverIndices.insert("updateNodeBalancerConfig", 0);
    _serverConfigs.insert("updateNodeBalancerNode", defaultConf);
    _serverIndices.insert("updateNodeBalancerNode", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAINodeBalancersApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAINodeBalancersApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAINodeBalancersApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAINodeBalancersApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAINodeBalancersApi::setUsername(const QString &username) {
    _username = username;
}

void OAINodeBalancersApi::setPassword(const QString &password) {
    _password = password;
}


void OAINodeBalancersApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAINodeBalancersApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAINodeBalancersApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
    _manager = manager;
}

/**
    * Appends a new ServerConfiguration to the config map for a specific operation.
    * @param operation The id to the target operation.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    * returns the index of the new server config on success and -1 if the operation is not found
    */
int OAINodeBalancersApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    if (_serverConfigs.contains(operation)) {
        _serverConfigs[operation].append(OAIServerConfiguration(
                    url,
                    description,
                    variables));
        return _serverConfigs[operation].size()-1;
    } else {
        return -1;
    }
}

/**
    * Appends a new ServerConfiguration to the config map for a all operations and sets the index to that server.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAINodeBalancersApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    for (auto keyIt = _serverIndices.keyBegin(); keyIt != _serverIndices.keyEnd(); keyIt++) {
        setServerIndex(*keyIt, addServerConfiguration(*keyIt, url, description, variables));
    }
}

/**
    * Appends a new ServerConfiguration to the config map for an operations and sets the index to that server.
    * @param URL A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAINodeBalancersApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAINodeBalancersApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAINodeBalancersApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAINodeBalancersApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAINodeBalancersApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAINodeBalancersApi::getParamStylePrefix(const QString &style) {
    if (style == "matrix") {
        return ";";
    } else if (style == "label") {
        return ".";
    } else if (style == "form") {
        return "&";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "&";
    } else if (style == "pipeDelimited") {
        return "&";
    } else {
        return "none";
    }
}

QString OAINodeBalancersApi::getParamStyleSuffix(const QString &style) {
    if (style == "matrix") {
        return "=";
    } else if (style == "label") {
        return "";
    } else if (style == "form") {
        return "=";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "=";
    } else if (style == "pipeDelimited") {
        return "=";
    } else {
        return "none";
    }
}

QString OAINodeBalancersApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

    if (style == "matrix") {
        return (isExplode) ? ";" + name + "=" : ",";

    } else if (style == "label") {
        return (isExplode) ? "." : ",";

    } else if (style == "form") {
        return (isExplode) ? "&" + name + "=" : ",";

    } else if (style == "simple") {
        return ",";
    } else if (style == "spaceDelimited") {
        return (isExplode) ? "&" + name + "=" : " ";

    } else if (style == "pipeDelimited") {
        return (isExplode) ? "&" + name + "=" : "|";

    } else if (style == "deepObject") {
        return (isExplode) ? "&" : "none";

    } else {
        return "none";
    }
}

void OAINodeBalancersApi::createNodeBalancer(const OAICreateNodeBalancer_request &oai_create_node_balancer_request) {
    QString fullPath = QString(_serverConfigs["createNodeBalancer"][_serverIndices.value("createNodeBalancer")].URL()+"/nodebalancers");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_node_balancer_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::createNodeBalancerCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_write");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::createNodeBalancerCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::createNodeBalancerCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAINodeBalancer output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createNodeBalancerSignal(output);
        Q_EMIT createNodeBalancerSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_write");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT createNodeBalancerSignalE(output, error_type, error_str);
        Q_EMIT createNodeBalancerSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createNodeBalancerSignalError(output, error_type, error_str);
        Q_EMIT createNodeBalancerSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::createNodeBalancerConfig(const qint32 &node_balancer_id, const ::OpenAPI::OptionalParam<OAINodeBalancerConfig> &oai_node_balancer_config) {
    QString fullPath = QString(_serverConfigs["createNodeBalancerConfig"][_serverIndices.value("createNodeBalancerConfig")].URL()+"/nodebalancers/{nodeBalancerId}/configs");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_node_balancer_config.hasValue()){

        
        QByteArray output = oai_node_balancer_config.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::createNodeBalancerConfigCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_write");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::createNodeBalancerConfigCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::createNodeBalancerConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAINodeBalancerConfig output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createNodeBalancerConfigSignal(output);
        Q_EMIT createNodeBalancerConfigSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_write");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT createNodeBalancerConfigSignalE(output, error_type, error_str);
        Q_EMIT createNodeBalancerConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createNodeBalancerConfigSignalError(output, error_type, error_str);
        Q_EMIT createNodeBalancerConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::createNodeBalancerNode(const qint32 &node_balancer_id, const qint32 &config_id, const OAINodeBalancerNode &oai_node_balancer_node) {
    QString fullPath = QString(_serverConfigs["createNodeBalancerNode"][_serverIndices.value("createNodeBalancerNode")].URL()+"/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    
    {
        QString config_idPathParam("{");
        config_idPathParam.append("configId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "configId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"configId"+pathSuffix : pathPrefix;
        fullPath.replace(config_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(config_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_node_balancer_node.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::createNodeBalancerNodeCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_write");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::createNodeBalancerNodeCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::createNodeBalancerNodeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAINodeBalancerNode output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createNodeBalancerNodeSignal(output);
        Q_EMIT createNodeBalancerNodeSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_write");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT createNodeBalancerNodeSignalE(output, error_type, error_str);
        Q_EMIT createNodeBalancerNodeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createNodeBalancerNodeSignalError(output, error_type, error_str);
        Q_EMIT createNodeBalancerNodeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::deleteNodeBalancer(const qint32 &node_balancer_id) {
    QString fullPath = QString(_serverConfigs["deleteNodeBalancer"][_serverIndices.value("deleteNodeBalancer")].URL()+"/nodebalancers/{nodeBalancerId}");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::deleteNodeBalancerCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_write");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::deleteNodeBalancerCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::deleteNodeBalancerCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteNodeBalancerSignal(output);
        Q_EMIT deleteNodeBalancerSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_write");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deleteNodeBalancerSignalE(output, error_type, error_str);
        Q_EMIT deleteNodeBalancerSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteNodeBalancerSignalError(output, error_type, error_str);
        Q_EMIT deleteNodeBalancerSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::deleteNodeBalancerConfig(const qint32 &node_balancer_id, const qint32 &config_id) {
    QString fullPath = QString(_serverConfigs["deleteNodeBalancerConfig"][_serverIndices.value("deleteNodeBalancerConfig")].URL()+"/nodebalancers/{nodeBalancerId}/configs/{configId}");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    
    {
        QString config_idPathParam("{");
        config_idPathParam.append("configId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "configId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"configId"+pathSuffix : pathPrefix;
        fullPath.replace(config_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(config_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::deleteNodeBalancerConfigCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_write");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::deleteNodeBalancerConfigCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::deleteNodeBalancerConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteNodeBalancerConfigSignal(output);
        Q_EMIT deleteNodeBalancerConfigSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_write");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deleteNodeBalancerConfigSignalE(output, error_type, error_str);
        Q_EMIT deleteNodeBalancerConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteNodeBalancerConfigSignalError(output, error_type, error_str);
        Q_EMIT deleteNodeBalancerConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::deleteNodeBalancerConfigNode(const qint32 &node_balancer_id, const qint32 &config_id, const qint32 &node_id) {
    QString fullPath = QString(_serverConfigs["deleteNodeBalancerConfigNode"][_serverIndices.value("deleteNodeBalancerConfigNode")].URL()+"/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId}");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    
    {
        QString config_idPathParam("{");
        config_idPathParam.append("configId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "configId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"configId"+pathSuffix : pathPrefix;
        fullPath.replace(config_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(config_id)));
    }
    
    {
        QString node_idPathParam("{");
        node_idPathParam.append("nodeId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeId"+pathSuffix : pathPrefix;
        fullPath.replace(node_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::deleteNodeBalancerConfigNodeCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_write");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::deleteNodeBalancerConfigNodeCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::deleteNodeBalancerConfigNodeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteNodeBalancerConfigNodeSignal(output);
        Q_EMIT deleteNodeBalancerConfigNodeSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_write");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deleteNodeBalancerConfigNodeSignalE(output, error_type, error_str);
        Q_EMIT deleteNodeBalancerConfigNodeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteNodeBalancerConfigNodeSignalError(output, error_type, error_str);
        Q_EMIT deleteNodeBalancerConfigNodeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::getNodeBalancer(const qint32 &node_balancer_id) {
    QString fullPath = QString(_serverConfigs["getNodeBalancer"][_serverIndices.value("getNodeBalancer")].URL()+"/nodebalancers/{nodeBalancerId}");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::getNodeBalancerCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_only");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::getNodeBalancerCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::getNodeBalancerCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAINodeBalancer output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getNodeBalancerSignal(output);
        Q_EMIT getNodeBalancerSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_only");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getNodeBalancerSignalE(output, error_type, error_str);
        Q_EMIT getNodeBalancerSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getNodeBalancerSignalError(output, error_type, error_str);
        Q_EMIT getNodeBalancerSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::getNodeBalancerConfig(const qint32 &node_balancer_id, const qint32 &config_id) {
    QString fullPath = QString(_serverConfigs["getNodeBalancerConfig"][_serverIndices.value("getNodeBalancerConfig")].URL()+"/nodebalancers/{nodeBalancerId}/configs/{configId}");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    
    {
        QString config_idPathParam("{");
        config_idPathParam.append("configId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "configId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"configId"+pathSuffix : pathPrefix;
        fullPath.replace(config_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(config_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::getNodeBalancerConfigCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_only");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::getNodeBalancerConfigCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::getNodeBalancerConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAINodeBalancerConfig output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getNodeBalancerConfigSignal(output);
        Q_EMIT getNodeBalancerConfigSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_only");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getNodeBalancerConfigSignalE(output, error_type, error_str);
        Q_EMIT getNodeBalancerConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getNodeBalancerConfigSignalError(output, error_type, error_str);
        Q_EMIT getNodeBalancerConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::getNodeBalancerConfigNodes(const qint32 &node_balancer_id, const qint32 &config_id, const ::OpenAPI::OptionalParam<qint32> &page, const ::OpenAPI::OptionalParam<qint32> &page_size) {
    QString fullPath = QString(_serverConfigs["getNodeBalancerConfigNodes"][_serverIndices.value("getNodeBalancerConfigNodes")].URL()+"/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    
    {
        QString config_idPathParam("{");
        config_idPathParam.append("configId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "configId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"configId"+pathSuffix : pathPrefix;
        fullPath.replace(config_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(config_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("page")).append(querySuffix).append(QUrl::toPercentEncoding(page.stringValue()));
    }
    if (page_size.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page_size", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("page_size")).append(querySuffix).append(QUrl::toPercentEncoding(page_size.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::getNodeBalancerConfigNodesCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_only");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::getNodeBalancerConfigNodesCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::getNodeBalancerConfigNodesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetNodeBalancerConfigNodes_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getNodeBalancerConfigNodesSignal(output);
        Q_EMIT getNodeBalancerConfigNodesSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_only");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getNodeBalancerConfigNodesSignalE(output, error_type, error_str);
        Q_EMIT getNodeBalancerConfigNodesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getNodeBalancerConfigNodesSignalError(output, error_type, error_str);
        Q_EMIT getNodeBalancerConfigNodesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::getNodeBalancerConfigs(const qint32 &node_balancer_id, const ::OpenAPI::OptionalParam<qint32> &page, const ::OpenAPI::OptionalParam<qint32> &page_size) {
    QString fullPath = QString(_serverConfigs["getNodeBalancerConfigs"][_serverIndices.value("getNodeBalancerConfigs")].URL()+"/nodebalancers/{nodeBalancerId}/configs");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("page")).append(querySuffix).append(QUrl::toPercentEncoding(page.stringValue()));
    }
    if (page_size.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page_size", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("page_size")).append(querySuffix).append(QUrl::toPercentEncoding(page_size.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::getNodeBalancerConfigsCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_only");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::getNodeBalancerConfigsCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::getNodeBalancerConfigsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetNodeBalancerConfigs_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getNodeBalancerConfigsSignal(output);
        Q_EMIT getNodeBalancerConfigsSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_only");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getNodeBalancerConfigsSignalE(output, error_type, error_str);
        Q_EMIT getNodeBalancerConfigsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getNodeBalancerConfigsSignalError(output, error_type, error_str);
        Q_EMIT getNodeBalancerConfigsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::getNodeBalancerNode(const qint32 &node_balancer_id, const qint32 &config_id, const qint32 &node_id) {
    QString fullPath = QString(_serverConfigs["getNodeBalancerNode"][_serverIndices.value("getNodeBalancerNode")].URL()+"/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId}");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    
    {
        QString config_idPathParam("{");
        config_idPathParam.append("configId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "configId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"configId"+pathSuffix : pathPrefix;
        fullPath.replace(config_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(config_id)));
    }
    
    {
        QString node_idPathParam("{");
        node_idPathParam.append("nodeId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeId"+pathSuffix : pathPrefix;
        fullPath.replace(node_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::getNodeBalancerNodeCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_write");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::getNodeBalancerNodeCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::getNodeBalancerNodeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAINodeBalancerNode output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getNodeBalancerNodeSignal(output);
        Q_EMIT getNodeBalancerNodeSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_write");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getNodeBalancerNodeSignalE(output, error_type, error_str);
        Q_EMIT getNodeBalancerNodeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getNodeBalancerNodeSignalError(output, error_type, error_str);
        Q_EMIT getNodeBalancerNodeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::getNodeBalancers(const ::OpenAPI::OptionalParam<qint32> &page, const ::OpenAPI::OptionalParam<qint32> &page_size) {
    QString fullPath = QString(_serverConfigs["getNodeBalancers"][_serverIndices.value("getNodeBalancers")].URL()+"/nodebalancers");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("page")).append(querySuffix).append(QUrl::toPercentEncoding(page.stringValue()));
    }
    if (page_size.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page_size", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("page_size")).append(querySuffix).append(QUrl::toPercentEncoding(page_size.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::getNodeBalancersCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_only");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::getNodeBalancersCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::getNodeBalancersCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetLinodeNodeBalancers_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getNodeBalancersSignal(output);
        Q_EMIT getNodeBalancersSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_only");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getNodeBalancersSignalE(output, error_type, error_str);
        Q_EMIT getNodeBalancersSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getNodeBalancersSignalError(output, error_type, error_str);
        Q_EMIT getNodeBalancersSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::nodebalancersNodeBalancerIdStatsGet(const qint32 &node_balancer_id) {
    QString fullPath = QString(_serverConfigs["nodebalancersNodeBalancerIdStatsGet"][_serverIndices.value("nodebalancersNodeBalancerIdStatsGet")].URL()+"/nodebalancers/{nodeBalancerId}/stats");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::nodebalancersNodeBalancerIdStatsGetCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_only");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::nodebalancersNodeBalancerIdStatsGetCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::nodebalancersNodeBalancerIdStatsGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAINodeBalancerStats output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT nodebalancersNodeBalancerIdStatsGetSignal(output);
        Q_EMIT nodebalancersNodeBalancerIdStatsGetSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_only");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT nodebalancersNodeBalancerIdStatsGetSignalE(output, error_type, error_str);
        Q_EMIT nodebalancersNodeBalancerIdStatsGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT nodebalancersNodeBalancerIdStatsGetSignalError(output, error_type, error_str);
        Q_EMIT nodebalancersNodeBalancerIdStatsGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::rebuildNodeBalancerConfig(const qint32 &node_balancer_id, const qint32 &config_id, const OAIRebuildNodeBalancerConfig_request &oai_rebuild_node_balancer_config_request) {
    QString fullPath = QString(_serverConfigs["rebuildNodeBalancerConfig"][_serverIndices.value("rebuildNodeBalancerConfig")].URL()+"/nodebalancers/{nodeBalancerId}/configs/{configId}/rebuild");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    
    {
        QString config_idPathParam("{");
        config_idPathParam.append("configId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "configId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"configId"+pathSuffix : pathPrefix;
        fullPath.replace(config_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(config_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_rebuild_node_balancer_config_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::rebuildNodeBalancerConfigCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_write");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::rebuildNodeBalancerConfigCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::rebuildNodeBalancerConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAINodeBalancerConfig output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT rebuildNodeBalancerConfigSignal(output);
        Q_EMIT rebuildNodeBalancerConfigSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_write");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT rebuildNodeBalancerConfigSignalE(output, error_type, error_str);
        Q_EMIT rebuildNodeBalancerConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT rebuildNodeBalancerConfigSignalError(output, error_type, error_str);
        Q_EMIT rebuildNodeBalancerConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::updateNodeBalancer(const qint32 &node_balancer_id, const OAINodeBalancer &oai_node_balancer) {
    QString fullPath = QString(_serverConfigs["updateNodeBalancer"][_serverIndices.value("updateNodeBalancer")].URL()+"/nodebalancers/{nodeBalancerId}");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    {

        
        QByteArray output = oai_node_balancer.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::updateNodeBalancerCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_write");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::updateNodeBalancerCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::updateNodeBalancerCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAINodeBalancer output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateNodeBalancerSignal(output);
        Q_EMIT updateNodeBalancerSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_write");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT updateNodeBalancerSignalE(output, error_type, error_str);
        Q_EMIT updateNodeBalancerSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateNodeBalancerSignalError(output, error_type, error_str);
        Q_EMIT updateNodeBalancerSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::updateNodeBalancerConfig(const qint32 &node_balancer_id, const qint32 &config_id, const OAINodeBalancerConfig &oai_node_balancer_config) {
    QString fullPath = QString(_serverConfigs["updateNodeBalancerConfig"][_serverIndices.value("updateNodeBalancerConfig")].URL()+"/nodebalancers/{nodeBalancerId}/configs/{configId}");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    
    {
        QString config_idPathParam("{");
        config_idPathParam.append("configId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "configId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"configId"+pathSuffix : pathPrefix;
        fullPath.replace(config_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(config_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    {

        
        QByteArray output = oai_node_balancer_config.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::updateNodeBalancerConfigCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_write");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::updateNodeBalancerConfigCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::updateNodeBalancerConfigCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAINodeBalancerConfig output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateNodeBalancerConfigSignal(output);
        Q_EMIT updateNodeBalancerConfigSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_write");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT updateNodeBalancerConfigSignalE(output, error_type, error_str);
        Q_EMIT updateNodeBalancerConfigSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateNodeBalancerConfigSignalError(output, error_type, error_str);
        Q_EMIT updateNodeBalancerConfigSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::updateNodeBalancerNode(const qint32 &node_balancer_id, const qint32 &config_id, const qint32 &node_id, const OAINodeBalancerNode &oai_node_balancer_node) {
    QString fullPath = QString(_serverConfigs["updateNodeBalancerNode"][_serverIndices.value("updateNodeBalancerNode")].URL()+"/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId}");
    
    if (!_bearerToken.isEmpty())
        addHeaders("Authorization", "Bearer " + _bearerToken);
    
    
    {
        QString node_balancer_idPathParam("{");
        node_balancer_idPathParam.append("nodeBalancerId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeBalancerId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeBalancerId"+pathSuffix : pathPrefix;
        fullPath.replace(node_balancer_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_balancer_id)));
    }
    
    {
        QString config_idPathParam("{");
        config_idPathParam.append("configId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "configId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"configId"+pathSuffix : pathPrefix;
        fullPath.replace(config_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(config_id)));
    }
    
    {
        QString node_idPathParam("{");
        node_idPathParam.append("nodeId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "nodeId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"nodeId"+pathSuffix : pathPrefix;
        fullPath.replace(node_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(node_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    {

        
        QByteArray output = oai_node_balancer_node.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::updateNodeBalancerNodeCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    scope.append("nodebalancers:read_write");
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAINodeBalancersApi::updateNodeBalancerNodeCallback);
    connect(this, &OAINodeBalancersApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAINodeBalancersApi::updateNodeBalancerNodeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAINodeBalancerNode output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateNodeBalancerNodeSignal(output);
        Q_EMIT updateNodeBalancerNodeSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("nodebalancers:read_write");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.linode.com/oauth/authorize");
        QString tokenUrl("https://login.linode.com/oauth/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT updateNodeBalancerNodeSignalE(output, error_type, error_str);
        Q_EMIT updateNodeBalancerNodeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateNodeBalancerNodeSignalError(output, error_type, error_str);
        Q_EMIT updateNodeBalancerNodeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAINodeBalancersApi::tokenAvailable(){

    oauthToken token;
    switch (_OauthMethod) {
    case 1: //implicit flow
        token = _implicitFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _implicitFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 2: //authorization flow
        token = _authFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _authFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 3: //client credentials flow
        token = _credentialFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 4: //resource owner password flow
        token = _passwordFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    default:
        qDebug() << "No Oauth method set!";
        break;
    }
}
} // namespace OpenAPI
