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

#ifndef OAI_OAILinodeInstancesApi_H
#define OAI_OAILinodeInstancesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAddLinodeIP_request.h"
#include "OAIBackup.h"
#include "OAIBootLinodeInstance_request.h"
#include "OAICloneLinodeInstance_request.h"
#include "OAICreateLinodeInstance_request.h"
#include "OAICreateSnapshot_request.h"
#include "OAIDisk.h"
#include "OAIDiskRequest.h"
#include "OAIGetAccount_default_response.h"
#include "OAIGetBackups_200_response.h"
#include "OAIGetKernels_200_response.h"
#include "OAIGetLinodeConfigs_200_response.h"
#include "OAIGetLinodeDisks_200_response.h"
#include "OAIGetLinodeFirewalls_200_response.h"
#include "OAIGetLinodeIPs_200_response.h"
#include "OAIGetLinodeInstances_200_response.h"
#include "OAIGetLinodeNodeBalancers_200_response.h"
#include "OAIGetLinodeTransferByYearMonth_200_response.h"
#include "OAIGetLinodeTransfer_200_response.h"
#include "OAIGetLinodeVolumes_200_response.h"
#include "OAIIPAddress.h"
#include "OAIKernel.h"
#include "OAILinode.h"
#include "OAILinodeConfig.h"
#include "OAILinodeRequest.h"
#include "OAILinodeStats.h"
#include "OAIMigrateLinodeInstance_request.h"
#include "OAIMutateLinodeInstance_request.h"
#include "OAIObject.h"
#include "OAIRebootLinodeInstance_request.h"
#include "OAIRescueLinodeInstance_request.h"
#include "OAIResetDiskPassword_request.h"
#include "OAIResetLinodePassword_request.h"
#include "OAIResizeDisk_request.h"
#include "OAIResizeLinodeInstance_request.h"
#include "OAIRestoreBackup_request.h"
#include "OAIUpdateLinodeIP_request.h"
#include "UNKNOWN_BASE_TYPE.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAILinodeInstancesApi : public QObject {
    Q_OBJECT

public:
    OAILinodeInstancesApi(const int timeOut = 0);
    ~OAILinodeInstancesApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_linode_config OAILinodeConfig [required]
    */
    virtual void addLinodeConfig(const qint32 &linode_id, const OAILinodeConfig &oai_linode_config);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_disk_request OAIDiskRequest [required]
    */
    virtual void addLinodeDisk(const qint32 &linode_id, const OAIDiskRequest &oai_disk_request);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_add_linode_ip_request OAIAddLinodeIP_request [required]
    */
    virtual void addLinodeIP(const qint32 &linode_id, const OAIAddLinodeIP_request &oai_add_linode_ip_request);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_boot_linode_instance_request OAIBootLinodeInstance_request [optional]
    */
    virtual void bootLinodeInstance(const qint32 &linode_id, const ::OpenAPI::OptionalParam<OAIBootLinodeInstance_request> &oai_boot_linode_instance_request = ::OpenAPI::OptionalParam<OAIBootLinodeInstance_request>());

    /**
    * @param[in]  linode_id qint32 [required]
    */
    virtual void cancelBackups(const qint32 &linode_id);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  disk_id qint32 [required]
    */
    virtual void cloneLinodeDisk(const qint32 &linode_id, const qint32 &disk_id);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_clone_linode_instance_request OAICloneLinodeInstance_request [required]
    */
    virtual void cloneLinodeInstance(const qint32 &linode_id, const OAICloneLinodeInstance_request &oai_clone_linode_instance_request);

    /**
    * @param[in]  oai_create_linode_instance_request OAICreateLinodeInstance_request [required]
    */
    virtual void createLinodeInstance(const OAICreateLinodeInstance_request &oai_create_linode_instance_request);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_create_snapshot_request OAICreateSnapshot_request [required]
    */
    virtual void createSnapshot(const qint32 &linode_id, const OAICreateSnapshot_request &oai_create_snapshot_request);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  disk_id qint32 [required]
    */
    virtual void deleteDisk(const qint32 &linode_id, const qint32 &disk_id);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  config_id qint32 [required]
    */
    virtual void deleteLinodeConfig(const qint32 &linode_id, const qint32 &config_id);

    /**
    * @param[in]  linode_id qint32 [required]
    */
    virtual void deleteLinodeInstance(const qint32 &linode_id);

    /**
    * @param[in]  linode_id qint32 [required]
    */
    virtual void enableBackups(const qint32 &linode_id);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  backup_id qint32 [required]
    */
    virtual void getBackup(const qint32 &linode_id, const qint32 &backup_id);

    /**
    * @param[in]  linode_id qint32 [required]
    */
    virtual void getBackups(const qint32 &linode_id);

    /**
    * @param[in]  kernel_id QString [required]
    */
    virtual void getKernel(const QString &kernel_id);

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getKernels(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  config_id qint32 [required]
    */
    virtual void getLinodeConfig(const qint32 &linode_id, const qint32 &config_id);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getLinodeConfigs(const qint32 &linode_id, const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  disk_id qint32 [required]
    */
    virtual void getLinodeDisk(const qint32 &linode_id, const qint32 &disk_id);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getLinodeDisks(const qint32 &linode_id, const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getLinodeFirewalls(const qint32 &linode_id, const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  address QString [required]
    */
    virtual void getLinodeIP(const qint32 &linode_id, const QString &address);

    /**
    * @param[in]  linode_id qint32 [required]
    */
    virtual void getLinodeIPs(const qint32 &linode_id);

    /**
    * @param[in]  linode_id qint32 [required]
    */
    virtual void getLinodeInstance(const qint32 &linode_id);

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getLinodeInstances(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  linode_id qint32 [required]
    */
    virtual void getLinodeNodeBalancers(const qint32 &linode_id);

    /**
    * @param[in]  linode_id qint32 [required]
    */
    virtual void getLinodeStats(const qint32 &linode_id);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  year qint32 [required]
    * @param[in]  month qint32 [required]
    */
    virtual void getLinodeStatsByYearMonth(const qint32 &linode_id, const qint32 &year, const qint32 &month);

    /**
    * @param[in]  linode_id qint32 [required]
    */
    virtual void getLinodeTransfer(const qint32 &linode_id);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  year qint32 [required]
    * @param[in]  month qint32 [required]
    */
    virtual void getLinodeTransferByYearMonth(const qint32 &linode_id, const qint32 &year, const qint32 &month);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getLinodeVolumes(const qint32 &linode_id, const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_migrate_linode_instance_request OAIMigrateLinodeInstance_request [optional]
    */
    virtual void migrateLinodeInstance(const qint32 &linode_id, const ::OpenAPI::OptionalParam<OAIMigrateLinodeInstance_request> &oai_migrate_linode_instance_request = ::OpenAPI::OptionalParam<OAIMigrateLinodeInstance_request>());

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_mutate_linode_instance_request OAIMutateLinodeInstance_request [optional]
    */
    virtual void mutateLinodeInstance(const qint32 &linode_id, const ::OpenAPI::OptionalParam<OAIMutateLinodeInstance_request> &oai_mutate_linode_instance_request = ::OpenAPI::OptionalParam<OAIMutateLinodeInstance_request>());

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_reboot_linode_instance_request OAIRebootLinodeInstance_request [optional]
    */
    virtual void rebootLinodeInstance(const qint32 &linode_id, const ::OpenAPI::OptionalParam<OAIRebootLinodeInstance_request> &oai_reboot_linode_instance_request = ::OpenAPI::OptionalParam<OAIRebootLinodeInstance_request>());

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  unknown_base_type UNKNOWN_BASE_TYPE [required]
    */
    virtual void rebuildLinodeInstance(const qint32 &linode_id, const UNKNOWN_BASE_TYPE &unknown_base_type);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  address QString [required]
    */
    virtual void removeLinodeIP(const qint32 &linode_id, const QString &address);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_rescue_linode_instance_request OAIRescueLinodeInstance_request [optional]
    */
    virtual void rescueLinodeInstance(const qint32 &linode_id, const ::OpenAPI::OptionalParam<OAIRescueLinodeInstance_request> &oai_rescue_linode_instance_request = ::OpenAPI::OptionalParam<OAIRescueLinodeInstance_request>());

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  disk_id qint32 [required]
    * @param[in]  oai_reset_disk_password_request OAIResetDiskPassword_request [required]
    */
    virtual void resetDiskPassword(const qint32 &linode_id, const qint32 &disk_id, const OAIResetDiskPassword_request &oai_reset_disk_password_request);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_reset_linode_password_request OAIResetLinodePassword_request [optional]
    */
    virtual void resetLinodePassword(const qint32 &linode_id, const ::OpenAPI::OptionalParam<OAIResetLinodePassword_request> &oai_reset_linode_password_request = ::OpenAPI::OptionalParam<OAIResetLinodePassword_request>());

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  disk_id qint32 [required]
    * @param[in]  oai_resize_disk_request OAIResizeDisk_request [required]
    */
    virtual void resizeDisk(const qint32 &linode_id, const qint32 &disk_id, const OAIResizeDisk_request &oai_resize_disk_request);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_resize_linode_instance_request OAIResizeLinodeInstance_request [required]
    */
    virtual void resizeLinodeInstance(const qint32 &linode_id, const OAIResizeLinodeInstance_request &oai_resize_linode_instance_request);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  backup_id qint32 [required]
    * @param[in]  oai_restore_backup_request OAIRestoreBackup_request [required]
    */
    virtual void restoreBackup(const qint32 &linode_id, const qint32 &backup_id, const OAIRestoreBackup_request &oai_restore_backup_request);

    /**
    * @param[in]  linode_id qint32 [required]
    */
    virtual void shutdownLinodeInstance(const qint32 &linode_id);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  disk_id qint32 [required]
    * @param[in]  oai_disk OAIDisk [required]
    */
    virtual void updateDisk(const qint32 &linode_id, const qint32 &disk_id, const OAIDisk &oai_disk);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  config_id qint32 [required]
    * @param[in]  oai_linode_config OAILinodeConfig [required]
    */
    virtual void updateLinodeConfig(const qint32 &linode_id, const qint32 &config_id, const OAILinodeConfig &oai_linode_config);

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  address QString [required]
    * @param[in]  oai_update_linode_ip_request OAIUpdateLinodeIP_request [optional]
    */
    virtual void updateLinodeIP(const qint32 &linode_id, const QString &address, const ::OpenAPI::OptionalParam<OAIUpdateLinodeIP_request> &oai_update_linode_ip_request = ::OpenAPI::OptionalParam<OAIUpdateLinodeIP_request>());

    /**
    * @param[in]  linode_id qint32 [required]
    * @param[in]  oai_linode OAILinode [required]
    */
    virtual void updateLinodeInstance(const qint32 &linode_id, const OAILinode &oai_linode);


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void addLinodeConfigCallback(OAIHttpRequestWorker *worker);
    void addLinodeDiskCallback(OAIHttpRequestWorker *worker);
    void addLinodeIPCallback(OAIHttpRequestWorker *worker);
    void bootLinodeInstanceCallback(OAIHttpRequestWorker *worker);
    void cancelBackupsCallback(OAIHttpRequestWorker *worker);
    void cloneLinodeDiskCallback(OAIHttpRequestWorker *worker);
    void cloneLinodeInstanceCallback(OAIHttpRequestWorker *worker);
    void createLinodeInstanceCallback(OAIHttpRequestWorker *worker);
    void createSnapshotCallback(OAIHttpRequestWorker *worker);
    void deleteDiskCallback(OAIHttpRequestWorker *worker);
    void deleteLinodeConfigCallback(OAIHttpRequestWorker *worker);
    void deleteLinodeInstanceCallback(OAIHttpRequestWorker *worker);
    void enableBackupsCallback(OAIHttpRequestWorker *worker);
    void getBackupCallback(OAIHttpRequestWorker *worker);
    void getBackupsCallback(OAIHttpRequestWorker *worker);
    void getKernelCallback(OAIHttpRequestWorker *worker);
    void getKernelsCallback(OAIHttpRequestWorker *worker);
    void getLinodeConfigCallback(OAIHttpRequestWorker *worker);
    void getLinodeConfigsCallback(OAIHttpRequestWorker *worker);
    void getLinodeDiskCallback(OAIHttpRequestWorker *worker);
    void getLinodeDisksCallback(OAIHttpRequestWorker *worker);
    void getLinodeFirewallsCallback(OAIHttpRequestWorker *worker);
    void getLinodeIPCallback(OAIHttpRequestWorker *worker);
    void getLinodeIPsCallback(OAIHttpRequestWorker *worker);
    void getLinodeInstanceCallback(OAIHttpRequestWorker *worker);
    void getLinodeInstancesCallback(OAIHttpRequestWorker *worker);
    void getLinodeNodeBalancersCallback(OAIHttpRequestWorker *worker);
    void getLinodeStatsCallback(OAIHttpRequestWorker *worker);
    void getLinodeStatsByYearMonthCallback(OAIHttpRequestWorker *worker);
    void getLinodeTransferCallback(OAIHttpRequestWorker *worker);
    void getLinodeTransferByYearMonthCallback(OAIHttpRequestWorker *worker);
    void getLinodeVolumesCallback(OAIHttpRequestWorker *worker);
    void migrateLinodeInstanceCallback(OAIHttpRequestWorker *worker);
    void mutateLinodeInstanceCallback(OAIHttpRequestWorker *worker);
    void rebootLinodeInstanceCallback(OAIHttpRequestWorker *worker);
    void rebuildLinodeInstanceCallback(OAIHttpRequestWorker *worker);
    void removeLinodeIPCallback(OAIHttpRequestWorker *worker);
    void rescueLinodeInstanceCallback(OAIHttpRequestWorker *worker);
    void resetDiskPasswordCallback(OAIHttpRequestWorker *worker);
    void resetLinodePasswordCallback(OAIHttpRequestWorker *worker);
    void resizeDiskCallback(OAIHttpRequestWorker *worker);
    void resizeLinodeInstanceCallback(OAIHttpRequestWorker *worker);
    void restoreBackupCallback(OAIHttpRequestWorker *worker);
    void shutdownLinodeInstanceCallback(OAIHttpRequestWorker *worker);
    void updateDiskCallback(OAIHttpRequestWorker *worker);
    void updateLinodeConfigCallback(OAIHttpRequestWorker *worker);
    void updateLinodeIPCallback(OAIHttpRequestWorker *worker);
    void updateLinodeInstanceCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addLinodeConfigSignal(OAILinodeConfig summary);
    void addLinodeDiskSignal(OAIDisk summary);
    void addLinodeIPSignal(OAIIPAddress summary);
    void bootLinodeInstanceSignal(OAIObject summary);
    void cancelBackupsSignal(OAIObject summary);
    void cloneLinodeDiskSignal(OAIDisk summary);
    void cloneLinodeInstanceSignal(OAILinode summary);
    void createLinodeInstanceSignal(OAILinode summary);
    void createSnapshotSignal(OAIBackup summary);
    void deleteDiskSignal(OAIObject summary);
    void deleteLinodeConfigSignal(OAIObject summary);
    void deleteLinodeInstanceSignal(OAIObject summary);
    void enableBackupsSignal(OAIObject summary);
    void getBackupSignal(OAIBackup summary);
    void getBackupsSignal(OAIGetBackups_200_response summary);
    void getKernelSignal(OAIKernel summary);
    void getKernelsSignal(OAIGetKernels_200_response summary);
    void getLinodeConfigSignal(OAILinodeConfig summary);
    void getLinodeConfigsSignal(OAIGetLinodeConfigs_200_response summary);
    void getLinodeDiskSignal(OAIDisk summary);
    void getLinodeDisksSignal(OAIGetLinodeDisks_200_response summary);
    void getLinodeFirewallsSignal(OAIGetLinodeFirewalls_200_response summary);
    void getLinodeIPSignal(OAIIPAddress summary);
    void getLinodeIPsSignal(OAIGetLinodeIPs_200_response summary);
    void getLinodeInstanceSignal(OAILinode summary);
    void getLinodeInstancesSignal(OAIGetLinodeInstances_200_response summary);
    void getLinodeNodeBalancersSignal(OAIGetLinodeNodeBalancers_200_response summary);
    void getLinodeStatsSignal(OAILinodeStats summary);
    void getLinodeStatsByYearMonthSignal(OAILinodeStats summary);
    void getLinodeTransferSignal(OAIGetLinodeTransfer_200_response summary);
    void getLinodeTransferByYearMonthSignal(OAIGetLinodeTransferByYearMonth_200_response summary);
    void getLinodeVolumesSignal(OAIGetLinodeVolumes_200_response summary);
    void migrateLinodeInstanceSignal(OAIObject summary);
    void mutateLinodeInstanceSignal(OAIObject summary);
    void rebootLinodeInstanceSignal(OAIObject summary);
    void rebuildLinodeInstanceSignal(OAILinode summary);
    void removeLinodeIPSignal(OAIObject summary);
    void rescueLinodeInstanceSignal(OAIObject summary);
    void resetDiskPasswordSignal(OAIObject summary);
    void resetLinodePasswordSignal(OAIObject summary);
    void resizeDiskSignal(OAIObject summary);
    void resizeLinodeInstanceSignal(OAIObject summary);
    void restoreBackupSignal(OAIObject summary);
    void shutdownLinodeInstanceSignal(OAIObject summary);
    void updateDiskSignal(OAIDisk summary);
    void updateLinodeConfigSignal(OAILinodeConfig summary);
    void updateLinodeIPSignal(OAIIPAddress summary);
    void updateLinodeInstanceSignal(OAILinode summary);


    void addLinodeConfigSignalFull(OAIHttpRequestWorker *worker, OAILinodeConfig summary);
    void addLinodeDiskSignalFull(OAIHttpRequestWorker *worker, OAIDisk summary);
    void addLinodeIPSignalFull(OAIHttpRequestWorker *worker, OAIIPAddress summary);
    void bootLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void cancelBackupsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void cloneLinodeDiskSignalFull(OAIHttpRequestWorker *worker, OAIDisk summary);
    void cloneLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAILinode summary);
    void createLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAILinode summary);
    void createSnapshotSignalFull(OAIHttpRequestWorker *worker, OAIBackup summary);
    void deleteDiskSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deleteLinodeConfigSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deleteLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void enableBackupsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void getBackupSignalFull(OAIHttpRequestWorker *worker, OAIBackup summary);
    void getBackupsSignalFull(OAIHttpRequestWorker *worker, OAIGetBackups_200_response summary);
    void getKernelSignalFull(OAIHttpRequestWorker *worker, OAIKernel summary);
    void getKernelsSignalFull(OAIHttpRequestWorker *worker, OAIGetKernels_200_response summary);
    void getLinodeConfigSignalFull(OAIHttpRequestWorker *worker, OAILinodeConfig summary);
    void getLinodeConfigsSignalFull(OAIHttpRequestWorker *worker, OAIGetLinodeConfigs_200_response summary);
    void getLinodeDiskSignalFull(OAIHttpRequestWorker *worker, OAIDisk summary);
    void getLinodeDisksSignalFull(OAIHttpRequestWorker *worker, OAIGetLinodeDisks_200_response summary);
    void getLinodeFirewallsSignalFull(OAIHttpRequestWorker *worker, OAIGetLinodeFirewalls_200_response summary);
    void getLinodeIPSignalFull(OAIHttpRequestWorker *worker, OAIIPAddress summary);
    void getLinodeIPsSignalFull(OAIHttpRequestWorker *worker, OAIGetLinodeIPs_200_response summary);
    void getLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAILinode summary);
    void getLinodeInstancesSignalFull(OAIHttpRequestWorker *worker, OAIGetLinodeInstances_200_response summary);
    void getLinodeNodeBalancersSignalFull(OAIHttpRequestWorker *worker, OAIGetLinodeNodeBalancers_200_response summary);
    void getLinodeStatsSignalFull(OAIHttpRequestWorker *worker, OAILinodeStats summary);
    void getLinodeStatsByYearMonthSignalFull(OAIHttpRequestWorker *worker, OAILinodeStats summary);
    void getLinodeTransferSignalFull(OAIHttpRequestWorker *worker, OAIGetLinodeTransfer_200_response summary);
    void getLinodeTransferByYearMonthSignalFull(OAIHttpRequestWorker *worker, OAIGetLinodeTransferByYearMonth_200_response summary);
    void getLinodeVolumesSignalFull(OAIHttpRequestWorker *worker, OAIGetLinodeVolumes_200_response summary);
    void migrateLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void mutateLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void rebootLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void rebuildLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAILinode summary);
    void removeLinodeIPSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void rescueLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void resetDiskPasswordSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void resetLinodePasswordSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void resizeDiskSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void resizeLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void restoreBackupSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void shutdownLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateDiskSignalFull(OAIHttpRequestWorker *worker, OAIDisk summary);
    void updateLinodeConfigSignalFull(OAIHttpRequestWorker *worker, OAILinodeConfig summary);
    void updateLinodeIPSignalFull(OAIHttpRequestWorker *worker, OAIIPAddress summary);
    void updateLinodeInstanceSignalFull(OAIHttpRequestWorker *worker, OAILinode summary);

    Q_DECL_DEPRECATED_X("Use addLinodeConfigSignalError() instead")
    void addLinodeConfigSignalE(OAILinodeConfig summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addLinodeConfigSignalError(OAILinodeConfig summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addLinodeDiskSignalError() instead")
    void addLinodeDiskSignalE(OAIDisk summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addLinodeDiskSignalError(OAIDisk summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addLinodeIPSignalError() instead")
    void addLinodeIPSignalE(OAIIPAddress summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addLinodeIPSignalError(OAIIPAddress summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use bootLinodeInstanceSignalError() instead")
    void bootLinodeInstanceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void bootLinodeInstanceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cancelBackupsSignalError() instead")
    void cancelBackupsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void cancelBackupsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cloneLinodeDiskSignalError() instead")
    void cloneLinodeDiskSignalE(OAIDisk summary, QNetworkReply::NetworkError error_type, QString error_str);
    void cloneLinodeDiskSignalError(OAIDisk summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cloneLinodeInstanceSignalError() instead")
    void cloneLinodeInstanceSignalE(OAILinode summary, QNetworkReply::NetworkError error_type, QString error_str);
    void cloneLinodeInstanceSignalError(OAILinode summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createLinodeInstanceSignalError() instead")
    void createLinodeInstanceSignalE(OAILinode summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createLinodeInstanceSignalError(OAILinode summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createSnapshotSignalError() instead")
    void createSnapshotSignalE(OAIBackup summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createSnapshotSignalError(OAIBackup summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDiskSignalError() instead")
    void deleteDiskSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDiskSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteLinodeConfigSignalError() instead")
    void deleteLinodeConfigSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteLinodeConfigSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteLinodeInstanceSignalError() instead")
    void deleteLinodeInstanceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteLinodeInstanceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use enableBackupsSignalError() instead")
    void enableBackupsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void enableBackupsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getBackupSignalError() instead")
    void getBackupSignalE(OAIBackup summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getBackupSignalError(OAIBackup summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getBackupsSignalError() instead")
    void getBackupsSignalE(OAIGetBackups_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getBackupsSignalError(OAIGetBackups_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getKernelSignalError() instead")
    void getKernelSignalE(OAIKernel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getKernelSignalError(OAIKernel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getKernelsSignalError() instead")
    void getKernelsSignalE(OAIGetKernels_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getKernelsSignalError(OAIGetKernels_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeConfigSignalError() instead")
    void getLinodeConfigSignalE(OAILinodeConfig summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeConfigSignalError(OAILinodeConfig summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeConfigsSignalError() instead")
    void getLinodeConfigsSignalE(OAIGetLinodeConfigs_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeConfigsSignalError(OAIGetLinodeConfigs_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeDiskSignalError() instead")
    void getLinodeDiskSignalE(OAIDisk summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeDiskSignalError(OAIDisk summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeDisksSignalError() instead")
    void getLinodeDisksSignalE(OAIGetLinodeDisks_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeDisksSignalError(OAIGetLinodeDisks_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeFirewallsSignalError() instead")
    void getLinodeFirewallsSignalE(OAIGetLinodeFirewalls_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeFirewallsSignalError(OAIGetLinodeFirewalls_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeIPSignalError() instead")
    void getLinodeIPSignalE(OAIIPAddress summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeIPSignalError(OAIIPAddress summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeIPsSignalError() instead")
    void getLinodeIPsSignalE(OAIGetLinodeIPs_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeIPsSignalError(OAIGetLinodeIPs_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeInstanceSignalError() instead")
    void getLinodeInstanceSignalE(OAILinode summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeInstanceSignalError(OAILinode summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeInstancesSignalError() instead")
    void getLinodeInstancesSignalE(OAIGetLinodeInstances_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeInstancesSignalError(OAIGetLinodeInstances_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeNodeBalancersSignalError() instead")
    void getLinodeNodeBalancersSignalE(OAIGetLinodeNodeBalancers_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeNodeBalancersSignalError(OAIGetLinodeNodeBalancers_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeStatsSignalError() instead")
    void getLinodeStatsSignalE(OAILinodeStats summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeStatsSignalError(OAILinodeStats summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeStatsByYearMonthSignalError() instead")
    void getLinodeStatsByYearMonthSignalE(OAILinodeStats summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeStatsByYearMonthSignalError(OAILinodeStats summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeTransferSignalError() instead")
    void getLinodeTransferSignalE(OAIGetLinodeTransfer_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeTransferSignalError(OAIGetLinodeTransfer_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeTransferByYearMonthSignalError() instead")
    void getLinodeTransferByYearMonthSignalE(OAIGetLinodeTransferByYearMonth_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeTransferByYearMonthSignalError(OAIGetLinodeTransferByYearMonth_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeVolumesSignalError() instead")
    void getLinodeVolumesSignalE(OAIGetLinodeVolumes_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeVolumesSignalError(OAIGetLinodeVolumes_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use migrateLinodeInstanceSignalError() instead")
    void migrateLinodeInstanceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void migrateLinodeInstanceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mutateLinodeInstanceSignalError() instead")
    void mutateLinodeInstanceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void mutateLinodeInstanceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rebootLinodeInstanceSignalError() instead")
    void rebootLinodeInstanceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void rebootLinodeInstanceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rebuildLinodeInstanceSignalError() instead")
    void rebuildLinodeInstanceSignalE(OAILinode summary, QNetworkReply::NetworkError error_type, QString error_str);
    void rebuildLinodeInstanceSignalError(OAILinode summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use removeLinodeIPSignalError() instead")
    void removeLinodeIPSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void removeLinodeIPSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rescueLinodeInstanceSignalError() instead")
    void rescueLinodeInstanceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void rescueLinodeInstanceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resetDiskPasswordSignalError() instead")
    void resetDiskPasswordSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void resetDiskPasswordSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resetLinodePasswordSignalError() instead")
    void resetLinodePasswordSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void resetLinodePasswordSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resizeDiskSignalError() instead")
    void resizeDiskSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void resizeDiskSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resizeLinodeInstanceSignalError() instead")
    void resizeLinodeInstanceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void resizeLinodeInstanceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use restoreBackupSignalError() instead")
    void restoreBackupSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void restoreBackupSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use shutdownLinodeInstanceSignalError() instead")
    void shutdownLinodeInstanceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void shutdownLinodeInstanceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDiskSignalError() instead")
    void updateDiskSignalE(OAIDisk summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDiskSignalError(OAIDisk summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateLinodeConfigSignalError() instead")
    void updateLinodeConfigSignalE(OAILinodeConfig summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateLinodeConfigSignalError(OAILinodeConfig summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateLinodeIPSignalError() instead")
    void updateLinodeIPSignalE(OAIIPAddress summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateLinodeIPSignalError(OAIIPAddress summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateLinodeInstanceSignalError() instead")
    void updateLinodeInstanceSignalE(OAILinode summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateLinodeInstanceSignalError(OAILinode summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addLinodeConfigSignalErrorFull() instead")
    void addLinodeConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addLinodeConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addLinodeDiskSignalErrorFull() instead")
    void addLinodeDiskSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addLinodeDiskSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addLinodeIPSignalErrorFull() instead")
    void addLinodeIPSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addLinodeIPSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use bootLinodeInstanceSignalErrorFull() instead")
    void bootLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void bootLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cancelBackupsSignalErrorFull() instead")
    void cancelBackupsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void cancelBackupsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cloneLinodeDiskSignalErrorFull() instead")
    void cloneLinodeDiskSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void cloneLinodeDiskSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cloneLinodeInstanceSignalErrorFull() instead")
    void cloneLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void cloneLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createLinodeInstanceSignalErrorFull() instead")
    void createLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createSnapshotSignalErrorFull() instead")
    void createSnapshotSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createSnapshotSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDiskSignalErrorFull() instead")
    void deleteDiskSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDiskSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteLinodeConfigSignalErrorFull() instead")
    void deleteLinodeConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteLinodeConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteLinodeInstanceSignalErrorFull() instead")
    void deleteLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use enableBackupsSignalErrorFull() instead")
    void enableBackupsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void enableBackupsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getBackupSignalErrorFull() instead")
    void getBackupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getBackupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getBackupsSignalErrorFull() instead")
    void getBackupsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getBackupsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getKernelSignalErrorFull() instead")
    void getKernelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getKernelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getKernelsSignalErrorFull() instead")
    void getKernelsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getKernelsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeConfigSignalErrorFull() instead")
    void getLinodeConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeConfigsSignalErrorFull() instead")
    void getLinodeConfigsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeConfigsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeDiskSignalErrorFull() instead")
    void getLinodeDiskSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeDiskSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeDisksSignalErrorFull() instead")
    void getLinodeDisksSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeDisksSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeFirewallsSignalErrorFull() instead")
    void getLinodeFirewallsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeFirewallsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeIPSignalErrorFull() instead")
    void getLinodeIPSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeIPSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeIPsSignalErrorFull() instead")
    void getLinodeIPsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeIPsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeInstanceSignalErrorFull() instead")
    void getLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeInstancesSignalErrorFull() instead")
    void getLinodeInstancesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeInstancesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeNodeBalancersSignalErrorFull() instead")
    void getLinodeNodeBalancersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeNodeBalancersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeStatsSignalErrorFull() instead")
    void getLinodeStatsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeStatsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeStatsByYearMonthSignalErrorFull() instead")
    void getLinodeStatsByYearMonthSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeStatsByYearMonthSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeTransferSignalErrorFull() instead")
    void getLinodeTransferSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeTransferSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeTransferByYearMonthSignalErrorFull() instead")
    void getLinodeTransferByYearMonthSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeTransferByYearMonthSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLinodeVolumesSignalErrorFull() instead")
    void getLinodeVolumesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLinodeVolumesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use migrateLinodeInstanceSignalErrorFull() instead")
    void migrateLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void migrateLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use mutateLinodeInstanceSignalErrorFull() instead")
    void mutateLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void mutateLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rebootLinodeInstanceSignalErrorFull() instead")
    void rebootLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rebootLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rebuildLinodeInstanceSignalErrorFull() instead")
    void rebuildLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rebuildLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use removeLinodeIPSignalErrorFull() instead")
    void removeLinodeIPSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void removeLinodeIPSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rescueLinodeInstanceSignalErrorFull() instead")
    void rescueLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rescueLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resetDiskPasswordSignalErrorFull() instead")
    void resetDiskPasswordSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void resetDiskPasswordSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resetLinodePasswordSignalErrorFull() instead")
    void resetLinodePasswordSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void resetLinodePasswordSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resizeDiskSignalErrorFull() instead")
    void resizeDiskSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void resizeDiskSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resizeLinodeInstanceSignalErrorFull() instead")
    void resizeLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void resizeLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use restoreBackupSignalErrorFull() instead")
    void restoreBackupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void restoreBackupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use shutdownLinodeInstanceSignalErrorFull() instead")
    void shutdownLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void shutdownLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDiskSignalErrorFull() instead")
    void updateDiskSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDiskSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateLinodeConfigSignalErrorFull() instead")
    void updateLinodeConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateLinodeConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateLinodeIPSignalErrorFull() instead")
    void updateLinodeIPSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateLinodeIPSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateLinodeInstanceSignalErrorFull() instead")
    void updateLinodeInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateLinodeInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
