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

#include "OAIGetTaggedObjects_200_response_data_inner_data.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetTaggedObjects_200_response_data_inner_data::OAIGetTaggedObjects_200_response_data_inner_data(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetTaggedObjects_200_response_data_inner_data::OAIGetTaggedObjects_200_response_data_inner_data() {
    this->initializeModel();
}

OAIGetTaggedObjects_200_response_data_inner_data::~OAIGetTaggedObjects_200_response_data_inner_data() {}

void OAIGetTaggedObjects_200_response_data_inner_data::initializeModel() {

    m_alerts_isSet = false;
    m_alerts_isValid = false;

    m_backups_isSet = false;
    m_backups_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_group_isSet = false;
    m_group_isValid = false;

    m_host_uuid_isSet = false;
    m_host_uuid_isValid = false;

    m_hypervisor_isSet = false;
    m_hypervisor_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_ipv4_isSet = false;
    m_ipv4_isValid = false;

    m_ipv6_isSet = false;
    m_ipv6_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_specs_isSet = false;
    m_specs_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;

    m_watchdog_enabled_isSet = false;
    m_watchdog_enabled_isValid = false;

    m_axfr_ips_isSet = false;
    m_axfr_ips_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_domain_isSet = false;
    m_domain_isValid = false;

    m_expire_sec_isSet = false;
    m_expire_sec_isValid = false;

    m_master_ips_isSet = false;
    m_master_ips_isValid = false;

    m_refresh_sec_isSet = false;
    m_refresh_sec_isValid = false;

    m_retry_sec_isSet = false;
    m_retry_sec_isValid = false;

    m_soa_email_isSet = false;
    m_soa_email_isValid = false;

    m_ttl_sec_isSet = false;
    m_ttl_sec_isValid = false;

    m_filesystem_path_isSet = false;
    m_filesystem_path_isValid = false;

    m_hardware_type_isSet = false;
    m_hardware_type_isValid = false;

    m_linode_id_isSet = false;
    m_linode_id_isValid = false;

    m_linode_label_isSet = false;
    m_linode_label_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_client_conn_throttle_isSet = false;
    m_client_conn_throttle_isValid = false;

    m_hostname_isSet = false;
    m_hostname_isValid = false;

    m_transfer_isSet = false;
    m_transfer_isValid = false;
}

void OAIGetTaggedObjects_200_response_data_inner_data::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetTaggedObjects_200_response_data_inner_data::fromJsonObject(QJsonObject json) {

    m_alerts_isValid = ::OpenAPI::fromJsonValue(m_alerts, json[QString("alerts")]);
    m_alerts_isSet = !json[QString("alerts")].isNull() && m_alerts_isValid;

    m_backups_isValid = ::OpenAPI::fromJsonValue(m_backups, json[QString("backups")]);
    m_backups_isSet = !json[QString("backups")].isNull() && m_backups_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_group_isValid = ::OpenAPI::fromJsonValue(m_group, json[QString("group")]);
    m_group_isSet = !json[QString("group")].isNull() && m_group_isValid;

    m_host_uuid_isValid = ::OpenAPI::fromJsonValue(m_host_uuid, json[QString("host_uuid")]);
    m_host_uuid_isSet = !json[QString("host_uuid")].isNull() && m_host_uuid_isValid;

    m_hypervisor_isValid = ::OpenAPI::fromJsonValue(m_hypervisor, json[QString("hypervisor")]);
    m_hypervisor_isSet = !json[QString("hypervisor")].isNull() && m_hypervisor_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_ipv4_isValid = ::OpenAPI::fromJsonValue(m_ipv4, json[QString("ipv4")]);
    m_ipv4_isSet = !json[QString("ipv4")].isNull() && m_ipv4_isValid;

    m_ipv6_isValid = ::OpenAPI::fromJsonValue(m_ipv6, json[QString("ipv6")]);
    m_ipv6_isSet = !json[QString("ipv6")].isNull() && m_ipv6_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_specs_isValid = ::OpenAPI::fromJsonValue(m_specs, json[QString("specs")]);
    m_specs_isSet = !json[QString("specs")].isNull() && m_specs_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("updated")]);
    m_updated_isSet = !json[QString("updated")].isNull() && m_updated_isValid;

    m_watchdog_enabled_isValid = ::OpenAPI::fromJsonValue(m_watchdog_enabled, json[QString("watchdog_enabled")]);
    m_watchdog_enabled_isSet = !json[QString("watchdog_enabled")].isNull() && m_watchdog_enabled_isValid;

    m_axfr_ips_isValid = ::OpenAPI::fromJsonValue(m_axfr_ips, json[QString("axfr_ips")]);
    m_axfr_ips_isSet = !json[QString("axfr_ips")].isNull() && m_axfr_ips_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_domain_isValid = ::OpenAPI::fromJsonValue(m_domain, json[QString("domain")]);
    m_domain_isSet = !json[QString("domain")].isNull() && m_domain_isValid;

    m_expire_sec_isValid = ::OpenAPI::fromJsonValue(m_expire_sec, json[QString("expire_sec")]);
    m_expire_sec_isSet = !json[QString("expire_sec")].isNull() && m_expire_sec_isValid;

    m_master_ips_isValid = ::OpenAPI::fromJsonValue(m_master_ips, json[QString("master_ips")]);
    m_master_ips_isSet = !json[QString("master_ips")].isNull() && m_master_ips_isValid;

    m_refresh_sec_isValid = ::OpenAPI::fromJsonValue(m_refresh_sec, json[QString("refresh_sec")]);
    m_refresh_sec_isSet = !json[QString("refresh_sec")].isNull() && m_refresh_sec_isValid;

    m_retry_sec_isValid = ::OpenAPI::fromJsonValue(m_retry_sec, json[QString("retry_sec")]);
    m_retry_sec_isSet = !json[QString("retry_sec")].isNull() && m_retry_sec_isValid;

    m_soa_email_isValid = ::OpenAPI::fromJsonValue(m_soa_email, json[QString("soa_email")]);
    m_soa_email_isSet = !json[QString("soa_email")].isNull() && m_soa_email_isValid;

    m_ttl_sec_isValid = ::OpenAPI::fromJsonValue(m_ttl_sec, json[QString("ttl_sec")]);
    m_ttl_sec_isSet = !json[QString("ttl_sec")].isNull() && m_ttl_sec_isValid;

    m_filesystem_path_isValid = ::OpenAPI::fromJsonValue(m_filesystem_path, json[QString("filesystem_path")]);
    m_filesystem_path_isSet = !json[QString("filesystem_path")].isNull() && m_filesystem_path_isValid;

    m_hardware_type_isValid = ::OpenAPI::fromJsonValue(m_hardware_type, json[QString("hardware_type")]);
    m_hardware_type_isSet = !json[QString("hardware_type")].isNull() && m_hardware_type_isValid;

    m_linode_id_isValid = ::OpenAPI::fromJsonValue(m_linode_id, json[QString("linode_id")]);
    m_linode_id_isSet = !json[QString("linode_id")].isNull() && m_linode_id_isValid;

    m_linode_label_isValid = ::OpenAPI::fromJsonValue(m_linode_label, json[QString("linode_label")]);
    m_linode_label_isSet = !json[QString("linode_label")].isNull() && m_linode_label_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_client_conn_throttle_isValid = ::OpenAPI::fromJsonValue(m_client_conn_throttle, json[QString("client_conn_throttle")]);
    m_client_conn_throttle_isSet = !json[QString("client_conn_throttle")].isNull() && m_client_conn_throttle_isValid;

    m_hostname_isValid = ::OpenAPI::fromJsonValue(m_hostname, json[QString("hostname")]);
    m_hostname_isSet = !json[QString("hostname")].isNull() && m_hostname_isValid;

    m_transfer_isValid = ::OpenAPI::fromJsonValue(m_transfer, json[QString("transfer")]);
    m_transfer_isSet = !json[QString("transfer")].isNull() && m_transfer_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetTaggedObjects_200_response_data_inner_data::asJsonObject() const {
    QJsonObject obj;
    if (m_alerts.isSet()) {
        obj.insert(QString("alerts"), ::OpenAPI::toJsonValue(m_alerts));
    }
    if (m_backups.isSet()) {
        obj.insert(QString("backups"), ::OpenAPI::toJsonValue(m_backups));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_group_isSet) {
        obj.insert(QString("group"), ::OpenAPI::toJsonValue(m_group));
    }
    if (m_host_uuid_isSet) {
        obj.insert(QString("host_uuid"), ::OpenAPI::toJsonValue(m_host_uuid));
    }
    if (m_hypervisor_isSet) {
        obj.insert(QString("hypervisor"), ::OpenAPI::toJsonValue(m_hypervisor));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_ipv4_isSet) {
        obj.insert(QString("ipv4"), ::OpenAPI::toJsonValue(m_ipv4));
    }
    if (m_ipv6_isSet) {
        obj.insert(QString("ipv6"), ::OpenAPI::toJsonValue(m_ipv6));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_region_isSet) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_specs.isSet()) {
        obj.insert(QString("specs"), ::OpenAPI::toJsonValue(m_specs));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_updated_isSet) {
        obj.insert(QString("updated"), ::OpenAPI::toJsonValue(m_updated));
    }
    if (m_watchdog_enabled_isSet) {
        obj.insert(QString("watchdog_enabled"), ::OpenAPI::toJsonValue(m_watchdog_enabled));
    }
    if (m_axfr_ips.size() > 0) {
        obj.insert(QString("axfr_ips"), ::OpenAPI::toJsonValue(m_axfr_ips));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_domain_isSet) {
        obj.insert(QString("domain"), ::OpenAPI::toJsonValue(m_domain));
    }
    if (m_expire_sec_isSet) {
        obj.insert(QString("expire_sec"), ::OpenAPI::toJsonValue(m_expire_sec));
    }
    if (m_master_ips.size() > 0) {
        obj.insert(QString("master_ips"), ::OpenAPI::toJsonValue(m_master_ips));
    }
    if (m_refresh_sec_isSet) {
        obj.insert(QString("refresh_sec"), ::OpenAPI::toJsonValue(m_refresh_sec));
    }
    if (m_retry_sec_isSet) {
        obj.insert(QString("retry_sec"), ::OpenAPI::toJsonValue(m_retry_sec));
    }
    if (m_soa_email_isSet) {
        obj.insert(QString("soa_email"), ::OpenAPI::toJsonValue(m_soa_email));
    }
    if (m_ttl_sec_isSet) {
        obj.insert(QString("ttl_sec"), ::OpenAPI::toJsonValue(m_ttl_sec));
    }
    if (m_filesystem_path_isSet) {
        obj.insert(QString("filesystem_path"), ::OpenAPI::toJsonValue(m_filesystem_path));
    }
    if (m_hardware_type_isSet) {
        obj.insert(QString("hardware_type"), ::OpenAPI::toJsonValue(m_hardware_type));
    }
    if (m_linode_id_isSet) {
        obj.insert(QString("linode_id"), ::OpenAPI::toJsonValue(m_linode_id));
    }
    if (m_linode_label_isSet) {
        obj.insert(QString("linode_label"), ::OpenAPI::toJsonValue(m_linode_label));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_client_conn_throttle_isSet) {
        obj.insert(QString("client_conn_throttle"), ::OpenAPI::toJsonValue(m_client_conn_throttle));
    }
    if (m_hostname_isSet) {
        obj.insert(QString("hostname"), ::OpenAPI::toJsonValue(m_hostname));
    }
    if (m_transfer.isSet()) {
        obj.insert(QString("transfer"), ::OpenAPI::toJsonValue(m_transfer));
    }
    return obj;
}

OAILinode_alerts OAIGetTaggedObjects_200_response_data_inner_data::getAlerts() const {
    return m_alerts;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setAlerts(const OAILinode_alerts &alerts) {
    m_alerts = alerts;
    m_alerts_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_alerts_Set() const{
    return m_alerts_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_alerts_Valid() const{
    return m_alerts_isValid;
}

OAILinode_backups OAIGetTaggedObjects_200_response_data_inner_data::getBackups() const {
    return m_backups;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setBackups(const OAILinode_backups &backups) {
    m_backups = backups;
    m_backups_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_backups_Set() const{
    return m_backups_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_backups_Valid() const{
    return m_backups_isValid;
}

QDateTime OAIGetTaggedObjects_200_response_data_inner_data::getCreated() const {
    return m_created;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setCreated(const QDateTime &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_created_Set() const{
    return m_created_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getGroup() const {
    return m_group;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setGroup(const QString &group) {
    m_group = group;
    m_group_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_group_Set() const{
    return m_group_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_group_Valid() const{
    return m_group_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getHostUuid() const {
    return m_host_uuid;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setHostUuid(const QString &host_uuid) {
    m_host_uuid = host_uuid;
    m_host_uuid_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_host_uuid_Set() const{
    return m_host_uuid_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_host_uuid_Valid() const{
    return m_host_uuid_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getHypervisor() const {
    return m_hypervisor;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setHypervisor(const QString &hypervisor) {
    m_hypervisor = hypervisor;
    m_hypervisor_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_hypervisor_Set() const{
    return m_hypervisor_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_hypervisor_Valid() const{
    return m_hypervisor_isValid;
}

qint32 OAIGetTaggedObjects_200_response_data_inner_data::getId() const {
    return m_id;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getImage() const {
    return m_image;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_image_Set() const{
    return m_image_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_image_Valid() const{
    return m_image_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getIpv4() const {
    return m_ipv4;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setIpv4(const QString &ipv4) {
    m_ipv4 = ipv4;
    m_ipv4_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_ipv4_Set() const{
    return m_ipv4_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_ipv4_Valid() const{
    return m_ipv4_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getIpv6() const {
    return m_ipv6;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setIpv6(const QString &ipv6) {
    m_ipv6 = ipv6;
    m_ipv6_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_ipv6_Set() const{
    return m_ipv6_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_ipv6_Valid() const{
    return m_ipv6_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getLabel() const {
    return m_label;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_label_Set() const{
    return m_label_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_label_Valid() const{
    return m_label_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getRegion() const {
    return m_region;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setRegion(const QString &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_region_Set() const{
    return m_region_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_region_Valid() const{
    return m_region_isValid;
}

OAILinode_specs OAIGetTaggedObjects_200_response_data_inner_data::getSpecs() const {
    return m_specs;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setSpecs(const OAILinode_specs &specs) {
    m_specs = specs;
    m_specs_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_specs_Set() const{
    return m_specs_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_specs_Valid() const{
    return m_specs_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getStatus() const {
    return m_status;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_status_Set() const{
    return m_status_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_status_Valid() const{
    return m_status_isValid;
}

QList<QString> OAIGetTaggedObjects_200_response_data_inner_data::getTags() const {
    return m_tags;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getType() const {
    return m_type;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_type_Set() const{
    return m_type_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_type_Valid() const{
    return m_type_isValid;
}

QDateTime OAIGetTaggedObjects_200_response_data_inner_data::getUpdated() const {
    return m_updated;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setUpdated(const QDateTime &updated) {
    m_updated = updated;
    m_updated_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_updated_Set() const{
    return m_updated_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_updated_Valid() const{
    return m_updated_isValid;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::isWatchdogEnabled() const {
    return m_watchdog_enabled;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setWatchdogEnabled(const bool &watchdog_enabled) {
    m_watchdog_enabled = watchdog_enabled;
    m_watchdog_enabled_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_watchdog_enabled_Set() const{
    return m_watchdog_enabled_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_watchdog_enabled_Valid() const{
    return m_watchdog_enabled_isValid;
}

QList<QString> OAIGetTaggedObjects_200_response_data_inner_data::getAxfrIps() const {
    return m_axfr_ips;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setAxfrIps(const QList<QString> &axfr_ips) {
    m_axfr_ips = axfr_ips;
    m_axfr_ips_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_axfr_ips_Set() const{
    return m_axfr_ips_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_axfr_ips_Valid() const{
    return m_axfr_ips_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getDescription() const {
    return m_description;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_description_Set() const{
    return m_description_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getDomain() const {
    return m_domain;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setDomain(const QString &domain) {
    m_domain = domain;
    m_domain_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_domain_Set() const{
    return m_domain_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_domain_Valid() const{
    return m_domain_isValid;
}

qint32 OAIGetTaggedObjects_200_response_data_inner_data::getExpireSec() const {
    return m_expire_sec;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setExpireSec(const qint32 &expire_sec) {
    m_expire_sec = expire_sec;
    m_expire_sec_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_expire_sec_Set() const{
    return m_expire_sec_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_expire_sec_Valid() const{
    return m_expire_sec_isValid;
}

QList<QString> OAIGetTaggedObjects_200_response_data_inner_data::getMasterIps() const {
    return m_master_ips;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setMasterIps(const QList<QString> &master_ips) {
    m_master_ips = master_ips;
    m_master_ips_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_master_ips_Set() const{
    return m_master_ips_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_master_ips_Valid() const{
    return m_master_ips_isValid;
}

qint32 OAIGetTaggedObjects_200_response_data_inner_data::getRefreshSec() const {
    return m_refresh_sec;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setRefreshSec(const qint32 &refresh_sec) {
    m_refresh_sec = refresh_sec;
    m_refresh_sec_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_refresh_sec_Set() const{
    return m_refresh_sec_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_refresh_sec_Valid() const{
    return m_refresh_sec_isValid;
}

qint32 OAIGetTaggedObjects_200_response_data_inner_data::getRetrySec() const {
    return m_retry_sec;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setRetrySec(const qint32 &retry_sec) {
    m_retry_sec = retry_sec;
    m_retry_sec_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_retry_sec_Set() const{
    return m_retry_sec_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_retry_sec_Valid() const{
    return m_retry_sec_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getSoaEmail() const {
    return m_soa_email;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setSoaEmail(const QString &soa_email) {
    m_soa_email = soa_email;
    m_soa_email_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_soa_email_Set() const{
    return m_soa_email_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_soa_email_Valid() const{
    return m_soa_email_isValid;
}

qint32 OAIGetTaggedObjects_200_response_data_inner_data::getTtlSec() const {
    return m_ttl_sec;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setTtlSec(const qint32 &ttl_sec) {
    m_ttl_sec = ttl_sec;
    m_ttl_sec_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_ttl_sec_Set() const{
    return m_ttl_sec_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_ttl_sec_Valid() const{
    return m_ttl_sec_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getFilesystemPath() const {
    return m_filesystem_path;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setFilesystemPath(const QString &filesystem_path) {
    m_filesystem_path = filesystem_path;
    m_filesystem_path_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_filesystem_path_Set() const{
    return m_filesystem_path_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_filesystem_path_Valid() const{
    return m_filesystem_path_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getHardwareType() const {
    return m_hardware_type;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setHardwareType(const QString &hardware_type) {
    m_hardware_type = hardware_type;
    m_hardware_type_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_hardware_type_Set() const{
    return m_hardware_type_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_hardware_type_Valid() const{
    return m_hardware_type_isValid;
}

qint32 OAIGetTaggedObjects_200_response_data_inner_data::getLinodeId() const {
    return m_linode_id;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setLinodeId(const qint32 &linode_id) {
    m_linode_id = linode_id;
    m_linode_id_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_linode_id_Set() const{
    return m_linode_id_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_linode_id_Valid() const{
    return m_linode_id_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getLinodeLabel() const {
    return m_linode_label;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setLinodeLabel(const QString &linode_label) {
    m_linode_label = linode_label;
    m_linode_label_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_linode_label_Set() const{
    return m_linode_label_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_linode_label_Valid() const{
    return m_linode_label_isValid;
}

qint32 OAIGetTaggedObjects_200_response_data_inner_data::getSize() const {
    return m_size;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setSize(const qint32 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_size_Set() const{
    return m_size_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_size_Valid() const{
    return m_size_isValid;
}

qint32 OAIGetTaggedObjects_200_response_data_inner_data::getClientConnThrottle() const {
    return m_client_conn_throttle;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setClientConnThrottle(const qint32 &client_conn_throttle) {
    m_client_conn_throttle = client_conn_throttle;
    m_client_conn_throttle_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_client_conn_throttle_Set() const{
    return m_client_conn_throttle_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_client_conn_throttle_Valid() const{
    return m_client_conn_throttle_isValid;
}

QString OAIGetTaggedObjects_200_response_data_inner_data::getHostname() const {
    return m_hostname;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setHostname(const QString &hostname) {
    m_hostname = hostname;
    m_hostname_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_hostname_Set() const{
    return m_hostname_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_hostname_Valid() const{
    return m_hostname_isValid;
}

OAINodeBalancer_transfer OAIGetTaggedObjects_200_response_data_inner_data::getTransfer() const {
    return m_transfer;
}
void OAIGetTaggedObjects_200_response_data_inner_data::setTransfer(const OAINodeBalancer_transfer &transfer) {
    m_transfer = transfer;
    m_transfer_isSet = true;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_transfer_Set() const{
    return m_transfer_isSet;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::is_transfer_Valid() const{
    return m_transfer_isValid;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_alerts.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_backups.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_host_uuid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hypervisor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ipv4_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ipv6_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_specs.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
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

        if (m_updated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_watchdog_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_axfr_ips.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_domain_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expire_sec_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_master_ips.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_refresh_sec_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_retry_sec_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_soa_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ttl_sec_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_filesystem_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hardware_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_linode_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_linode_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_conn_throttle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hostname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transfer.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetTaggedObjects_200_response_data_inner_data::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
