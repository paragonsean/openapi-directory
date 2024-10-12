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

#ifndef OAI_OAIDatabasesApi_H
#define OAI_OAIDatabasesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIDatabaseBackup.h"
#include "OAIDatabaseBackupSnapshot.h"
#include "OAIDatabaseCredentials.h"
#include "OAIDatabaseEngine.h"
#include "OAIDatabaseMongoDB.h"
#include "OAIDatabaseMySQL.h"
#include "OAIDatabaseMySQLRequest.h"
#include "OAIDatabasePostgreSQL.h"
#include "OAIDatabasePostgreSQLRequest.h"
#include "OAIDatabaseSSL.h"
#include "OAIDatabaseType.h"
#include "OAIGetAccount_default_response.h"
#include "OAIGetDatabasesEngines_200_response.h"
#include "OAIGetDatabasesInstances_200_response.h"
#include "OAIGetDatabasesMongoDBInstanceBackups_200_response.h"
#include "OAIGetDatabasesMongoDBInstances_200_response.h"
#include "OAIGetDatabasesMySQLInstances_200_response.h"
#include "OAIGetDatabasesPostgreSQLInstances_200_response.h"
#include "OAIGetDatabasesTypes_200_response.h"
#include "OAIObject.h"
#include "OAIPutDatabasesMongoDBInstance_request.h"
#include "OAIPutDatabasesMySQLInstance_request.h"
#include "OAIPutDatabasesPostgreSQLInstance_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDatabasesApi : public QObject {
    Q_OBJECT

public:
    OAIDatabasesApi(const int timeOut = 0);
    ~OAIDatabasesApi();

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
    * @param[in]  instance_id qint32 [required]
    * @param[in]  backup_id qint32 [required]
    */
    virtual void deleteDatabaseMongoDBInstanceBackup(const qint32 &instance_id, const qint32 &backup_id);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  backup_id qint32 [required]
    */
    virtual void deleteDatabaseMySQLInstanceBackup(const qint32 &instance_id, const qint32 &backup_id);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  backup_id qint32 [required]
    */
    virtual void deleteDatabasePostgreSQLInstanceBackup(const qint32 &instance_id, const qint32 &backup_id);

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void deleteDatabasesMongoDBInstance(const qint32 &instance_id);

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void deleteDatabasesMySQLInstance(const qint32 &instance_id);

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void deleteDatabasesPostgreSQLInstance(const qint32 &instance_id);

    /**
    * @param[in]  engine_id QString [required]
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getDatabasesEngine(const QString &engine_id, const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getDatabasesEngines(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getDatabasesInstances(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void getDatabasesMongoDBInstance(const qint32 &instance_id);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  backup_id qint32 [required]
    */
    virtual void getDatabasesMongoDBInstanceBackup(const qint32 &instance_id, const qint32 &backup_id);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getDatabasesMongoDBInstanceBackups(const qint32 &instance_id, const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void getDatabasesMongoDBInstanceCredentials(const qint32 &instance_id);

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void getDatabasesMongoDBInstanceSSL(const qint32 &instance_id);

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getDatabasesMongoDBInstances(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void getDatabasesMySQLInstance(const qint32 &instance_id);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  backup_id qint32 [required]
    */
    virtual void getDatabasesMySQLInstanceBackup(const qint32 &instance_id, const qint32 &backup_id);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getDatabasesMySQLInstanceBackups(const qint32 &instance_id, const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void getDatabasesMySQLInstanceCredentials(const qint32 &instance_id);

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void getDatabasesMySQLInstanceSSL(const qint32 &instance_id);

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getDatabasesMySQLInstances(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void getDatabasesPostgreSQLInstance(const qint32 &instance_id);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  backup_id qint32 [required]
    */
    virtual void getDatabasesPostgreSQLInstanceBackup(const qint32 &instance_id, const qint32 &backup_id);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getDatabasesPostgreSQLInstanceBackups(const qint32 &instance_id, const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void getDatabasesPostgreSQLInstanceCredentials(const qint32 &instance_id);

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void getDatabasesPostgreSQLInstanceSSL(const qint32 &instance_id);

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getDatabasesPostgreSQLInstances(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  type_id QString [required]
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getDatabasesType(const QString &type_id, const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getDatabasesTypes(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  oai_database_backup_snapshot OAIDatabaseBackupSnapshot [optional]
    */
    virtual void postDatabasesMongoDBInstanceBackup(const qint32 &instance_id, const ::OpenAPI::OptionalParam<OAIDatabaseBackupSnapshot> &oai_database_backup_snapshot = ::OpenAPI::OptionalParam<OAIDatabaseBackupSnapshot>());

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  backup_id qint32 [required]
    */
    virtual void postDatabasesMongoDBInstanceBackupRestore(const qint32 &instance_id, const qint32 &backup_id);

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void postDatabasesMongoDBInstanceCredentialsReset(const qint32 &instance_id);

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void postDatabasesMongoDBInstancePatch(const qint32 &instance_id);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  oai_database_backup_snapshot OAIDatabaseBackupSnapshot [optional]
    */
    virtual void postDatabasesMySQLInstanceBackup(const qint32 &instance_id, const ::OpenAPI::OptionalParam<OAIDatabaseBackupSnapshot> &oai_database_backup_snapshot = ::OpenAPI::OptionalParam<OAIDatabaseBackupSnapshot>());

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  backup_id qint32 [required]
    */
    virtual void postDatabasesMySQLInstanceBackupRestore(const qint32 &instance_id, const qint32 &backup_id);

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void postDatabasesMySQLInstanceCredentialsReset(const qint32 &instance_id);

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void postDatabasesMySQLInstancePatch(const qint32 &instance_id);

    /**
    * @param[in]  oai_database_my_sql_request OAIDatabaseMySQLRequest [required]
    */
    virtual void postDatabasesMySQLInstances(const OAIDatabaseMySQLRequest &oai_database_my_sql_request);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  oai_database_backup_snapshot OAIDatabaseBackupSnapshot [optional]
    */
    virtual void postDatabasesPostgreSQLInstanceBackup(const qint32 &instance_id, const ::OpenAPI::OptionalParam<OAIDatabaseBackupSnapshot> &oai_database_backup_snapshot = ::OpenAPI::OptionalParam<OAIDatabaseBackupSnapshot>());

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  backup_id qint32 [required]
    */
    virtual void postDatabasesPostgreSQLInstanceBackupRestore(const qint32 &instance_id, const qint32 &backup_id);

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void postDatabasesPostgreSQLInstanceCredentialsReset(const qint32 &instance_id);

    /**
    * @param[in]  instance_id qint32 [required]
    */
    virtual void postDatabasesPostgreSQLInstancePatch(const qint32 &instance_id);

    /**
    * @param[in]  oai_database_postgre_sql_request OAIDatabasePostgreSQLRequest [required]
    */
    virtual void postDatabasesPostgreSQLInstances(const OAIDatabasePostgreSQLRequest &oai_database_postgre_sql_request);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  oai_put_databases_mongo_db_instance_request OAIPutDatabasesMongoDBInstance_request [required]
    */
    virtual void putDatabasesMongoDBInstance(const qint32 &instance_id, const OAIPutDatabasesMongoDBInstance_request &oai_put_databases_mongo_db_instance_request);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  oai_put_databases_my_sql_instance_request OAIPutDatabasesMySQLInstance_request [required]
    */
    virtual void putDatabasesMySQLInstance(const qint32 &instance_id, const OAIPutDatabasesMySQLInstance_request &oai_put_databases_my_sql_instance_request);

    /**
    * @param[in]  instance_id qint32 [required]
    * @param[in]  oai_put_databases_postgre_sql_instance_request OAIPutDatabasesPostgreSQLInstance_request [required]
    */
    virtual void putDatabasesPostgreSQLInstance(const qint32 &instance_id, const OAIPutDatabasesPostgreSQLInstance_request &oai_put_databases_postgre_sql_instance_request);


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

    void deleteDatabaseMongoDBInstanceBackupCallback(OAIHttpRequestWorker *worker);
    void deleteDatabaseMySQLInstanceBackupCallback(OAIHttpRequestWorker *worker);
    void deleteDatabasePostgreSQLInstanceBackupCallback(OAIHttpRequestWorker *worker);
    void deleteDatabasesMongoDBInstanceCallback(OAIHttpRequestWorker *worker);
    void deleteDatabasesMySQLInstanceCallback(OAIHttpRequestWorker *worker);
    void deleteDatabasesPostgreSQLInstanceCallback(OAIHttpRequestWorker *worker);
    void getDatabasesEngineCallback(OAIHttpRequestWorker *worker);
    void getDatabasesEnginesCallback(OAIHttpRequestWorker *worker);
    void getDatabasesInstancesCallback(OAIHttpRequestWorker *worker);
    void getDatabasesMongoDBInstanceCallback(OAIHttpRequestWorker *worker);
    void getDatabasesMongoDBInstanceBackupCallback(OAIHttpRequestWorker *worker);
    void getDatabasesMongoDBInstanceBackupsCallback(OAIHttpRequestWorker *worker);
    void getDatabasesMongoDBInstanceCredentialsCallback(OAIHttpRequestWorker *worker);
    void getDatabasesMongoDBInstanceSSLCallback(OAIHttpRequestWorker *worker);
    void getDatabasesMongoDBInstancesCallback(OAIHttpRequestWorker *worker);
    void getDatabasesMySQLInstanceCallback(OAIHttpRequestWorker *worker);
    void getDatabasesMySQLInstanceBackupCallback(OAIHttpRequestWorker *worker);
    void getDatabasesMySQLInstanceBackupsCallback(OAIHttpRequestWorker *worker);
    void getDatabasesMySQLInstanceCredentialsCallback(OAIHttpRequestWorker *worker);
    void getDatabasesMySQLInstanceSSLCallback(OAIHttpRequestWorker *worker);
    void getDatabasesMySQLInstancesCallback(OAIHttpRequestWorker *worker);
    void getDatabasesPostgreSQLInstanceCallback(OAIHttpRequestWorker *worker);
    void getDatabasesPostgreSQLInstanceBackupCallback(OAIHttpRequestWorker *worker);
    void getDatabasesPostgreSQLInstanceBackupsCallback(OAIHttpRequestWorker *worker);
    void getDatabasesPostgreSQLInstanceCredentialsCallback(OAIHttpRequestWorker *worker);
    void getDatabasesPostgreSQLInstanceSSLCallback(OAIHttpRequestWorker *worker);
    void getDatabasesPostgreSQLInstancesCallback(OAIHttpRequestWorker *worker);
    void getDatabasesTypeCallback(OAIHttpRequestWorker *worker);
    void getDatabasesTypesCallback(OAIHttpRequestWorker *worker);
    void postDatabasesMongoDBInstanceBackupCallback(OAIHttpRequestWorker *worker);
    void postDatabasesMongoDBInstanceBackupRestoreCallback(OAIHttpRequestWorker *worker);
    void postDatabasesMongoDBInstanceCredentialsResetCallback(OAIHttpRequestWorker *worker);
    void postDatabasesMongoDBInstancePatchCallback(OAIHttpRequestWorker *worker);
    void postDatabasesMySQLInstanceBackupCallback(OAIHttpRequestWorker *worker);
    void postDatabasesMySQLInstanceBackupRestoreCallback(OAIHttpRequestWorker *worker);
    void postDatabasesMySQLInstanceCredentialsResetCallback(OAIHttpRequestWorker *worker);
    void postDatabasesMySQLInstancePatchCallback(OAIHttpRequestWorker *worker);
    void postDatabasesMySQLInstancesCallback(OAIHttpRequestWorker *worker);
    void postDatabasesPostgreSQLInstanceBackupCallback(OAIHttpRequestWorker *worker);
    void postDatabasesPostgreSQLInstanceBackupRestoreCallback(OAIHttpRequestWorker *worker);
    void postDatabasesPostgreSQLInstanceCredentialsResetCallback(OAIHttpRequestWorker *worker);
    void postDatabasesPostgreSQLInstancePatchCallback(OAIHttpRequestWorker *worker);
    void postDatabasesPostgreSQLInstancesCallback(OAIHttpRequestWorker *worker);
    void putDatabasesMongoDBInstanceCallback(OAIHttpRequestWorker *worker);
    void putDatabasesMySQLInstanceCallback(OAIHttpRequestWorker *worker);
    void putDatabasesPostgreSQLInstanceCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void deleteDatabaseMongoDBInstanceBackupSignal(OAIObject summary);
    void deleteDatabaseMySQLInstanceBackupSignal(OAIObject summary);
    void deleteDatabasePostgreSQLInstanceBackupSignal(OAIObject summary);
    void deleteDatabasesMongoDBInstanceSignal(OAIObject summary);
    void deleteDatabasesMySQLInstanceSignal(OAIObject summary);
    void deleteDatabasesPostgreSQLInstanceSignal(OAIObject summary);
    void getDatabasesEngineSignal(OAIDatabaseEngine summary);
    void getDatabasesEnginesSignal(OAIGetDatabasesEngines_200_response summary);
    void getDatabasesInstancesSignal(OAIGetDatabasesInstances_200_response summary);
    void getDatabasesMongoDBInstanceSignal(OAIDatabaseMongoDB summary);
    void getDatabasesMongoDBInstanceBackupSignal(OAIDatabaseBackup summary);
    void getDatabasesMongoDBInstanceBackupsSignal(OAIGetDatabasesMongoDBInstanceBackups_200_response summary);
    void getDatabasesMongoDBInstanceCredentialsSignal(OAIDatabaseCredentials summary);
    void getDatabasesMongoDBInstanceSSLSignal(OAIDatabaseSSL summary);
    void getDatabasesMongoDBInstancesSignal(OAIGetDatabasesMongoDBInstances_200_response summary);
    void getDatabasesMySQLInstanceSignal(OAIDatabaseMySQL summary);
    void getDatabasesMySQLInstanceBackupSignal(OAIDatabaseBackup summary);
    void getDatabasesMySQLInstanceBackupsSignal(OAIGetDatabasesMongoDBInstanceBackups_200_response summary);
    void getDatabasesMySQLInstanceCredentialsSignal(OAIDatabaseCredentials summary);
    void getDatabasesMySQLInstanceSSLSignal(OAIDatabaseSSL summary);
    void getDatabasesMySQLInstancesSignal(OAIGetDatabasesMySQLInstances_200_response summary);
    void getDatabasesPostgreSQLInstanceSignal(OAIDatabasePostgreSQL summary);
    void getDatabasesPostgreSQLInstanceBackupSignal(OAIDatabaseBackup summary);
    void getDatabasesPostgreSQLInstanceBackupsSignal(OAIGetDatabasesMongoDBInstanceBackups_200_response summary);
    void getDatabasesPostgreSQLInstanceCredentialsSignal(OAIDatabaseCredentials summary);
    void getDatabasesPostgreSQLInstanceSSLSignal(OAIDatabaseSSL summary);
    void getDatabasesPostgreSQLInstancesSignal(OAIGetDatabasesPostgreSQLInstances_200_response summary);
    void getDatabasesTypeSignal(OAIDatabaseType summary);
    void getDatabasesTypesSignal(OAIGetDatabasesTypes_200_response summary);
    void postDatabasesMongoDBInstanceBackupSignal(OAIObject summary);
    void postDatabasesMongoDBInstanceBackupRestoreSignal(OAIObject summary);
    void postDatabasesMongoDBInstanceCredentialsResetSignal(OAIObject summary);
    void postDatabasesMongoDBInstancePatchSignal(OAIObject summary);
    void postDatabasesMySQLInstanceBackupSignal(OAIObject summary);
    void postDatabasesMySQLInstanceBackupRestoreSignal(OAIObject summary);
    void postDatabasesMySQLInstanceCredentialsResetSignal(OAIObject summary);
    void postDatabasesMySQLInstancePatchSignal(OAIObject summary);
    void postDatabasesMySQLInstancesSignal(OAIDatabaseMySQL summary);
    void postDatabasesPostgreSQLInstanceBackupSignal(OAIObject summary);
    void postDatabasesPostgreSQLInstanceBackupRestoreSignal(OAIObject summary);
    void postDatabasesPostgreSQLInstanceCredentialsResetSignal(OAIObject summary);
    void postDatabasesPostgreSQLInstancePatchSignal(OAIObject summary);
    void postDatabasesPostgreSQLInstancesSignal(OAIDatabasePostgreSQL summary);
    void putDatabasesMongoDBInstanceSignal(OAIDatabaseMongoDB summary);
    void putDatabasesMySQLInstanceSignal(OAIDatabaseMySQL summary);
    void putDatabasesPostgreSQLInstanceSignal(OAIDatabasePostgreSQL summary);


    void deleteDatabaseMongoDBInstanceBackupSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deleteDatabaseMySQLInstanceBackupSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deleteDatabasePostgreSQLInstanceBackupSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deleteDatabasesMongoDBInstanceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deleteDatabasesMySQLInstanceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deleteDatabasesPostgreSQLInstanceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void getDatabasesEngineSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseEngine summary);
    void getDatabasesEnginesSignalFull(OAIHttpRequestWorker *worker, OAIGetDatabasesEngines_200_response summary);
    void getDatabasesInstancesSignalFull(OAIHttpRequestWorker *worker, OAIGetDatabasesInstances_200_response summary);
    void getDatabasesMongoDBInstanceSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseMongoDB summary);
    void getDatabasesMongoDBInstanceBackupSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseBackup summary);
    void getDatabasesMongoDBInstanceBackupsSignalFull(OAIHttpRequestWorker *worker, OAIGetDatabasesMongoDBInstanceBackups_200_response summary);
    void getDatabasesMongoDBInstanceCredentialsSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseCredentials summary);
    void getDatabasesMongoDBInstanceSSLSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseSSL summary);
    void getDatabasesMongoDBInstancesSignalFull(OAIHttpRequestWorker *worker, OAIGetDatabasesMongoDBInstances_200_response summary);
    void getDatabasesMySQLInstanceSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseMySQL summary);
    void getDatabasesMySQLInstanceBackupSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseBackup summary);
    void getDatabasesMySQLInstanceBackupsSignalFull(OAIHttpRequestWorker *worker, OAIGetDatabasesMongoDBInstanceBackups_200_response summary);
    void getDatabasesMySQLInstanceCredentialsSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseCredentials summary);
    void getDatabasesMySQLInstanceSSLSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseSSL summary);
    void getDatabasesMySQLInstancesSignalFull(OAIHttpRequestWorker *worker, OAIGetDatabasesMySQLInstances_200_response summary);
    void getDatabasesPostgreSQLInstanceSignalFull(OAIHttpRequestWorker *worker, OAIDatabasePostgreSQL summary);
    void getDatabasesPostgreSQLInstanceBackupSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseBackup summary);
    void getDatabasesPostgreSQLInstanceBackupsSignalFull(OAIHttpRequestWorker *worker, OAIGetDatabasesMongoDBInstanceBackups_200_response summary);
    void getDatabasesPostgreSQLInstanceCredentialsSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseCredentials summary);
    void getDatabasesPostgreSQLInstanceSSLSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseSSL summary);
    void getDatabasesPostgreSQLInstancesSignalFull(OAIHttpRequestWorker *worker, OAIGetDatabasesPostgreSQLInstances_200_response summary);
    void getDatabasesTypeSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseType summary);
    void getDatabasesTypesSignalFull(OAIHttpRequestWorker *worker, OAIGetDatabasesTypes_200_response summary);
    void postDatabasesMongoDBInstanceBackupSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void postDatabasesMongoDBInstanceBackupRestoreSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void postDatabasesMongoDBInstanceCredentialsResetSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void postDatabasesMongoDBInstancePatchSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void postDatabasesMySQLInstanceBackupSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void postDatabasesMySQLInstanceBackupRestoreSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void postDatabasesMySQLInstanceCredentialsResetSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void postDatabasesMySQLInstancePatchSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void postDatabasesMySQLInstancesSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseMySQL summary);
    void postDatabasesPostgreSQLInstanceBackupSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void postDatabasesPostgreSQLInstanceBackupRestoreSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void postDatabasesPostgreSQLInstanceCredentialsResetSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void postDatabasesPostgreSQLInstancePatchSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void postDatabasesPostgreSQLInstancesSignalFull(OAIHttpRequestWorker *worker, OAIDatabasePostgreSQL summary);
    void putDatabasesMongoDBInstanceSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseMongoDB summary);
    void putDatabasesMySQLInstanceSignalFull(OAIHttpRequestWorker *worker, OAIDatabaseMySQL summary);
    void putDatabasesPostgreSQLInstanceSignalFull(OAIHttpRequestWorker *worker, OAIDatabasePostgreSQL summary);

    Q_DECL_DEPRECATED_X("Use deleteDatabaseMongoDBInstanceBackupSignalError() instead")
    void deleteDatabaseMongoDBInstanceBackupSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatabaseMongoDBInstanceBackupSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDatabaseMySQLInstanceBackupSignalError() instead")
    void deleteDatabaseMySQLInstanceBackupSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatabaseMySQLInstanceBackupSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDatabasePostgreSQLInstanceBackupSignalError() instead")
    void deleteDatabasePostgreSQLInstanceBackupSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatabasePostgreSQLInstanceBackupSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDatabasesMongoDBInstanceSignalError() instead")
    void deleteDatabasesMongoDBInstanceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatabasesMongoDBInstanceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDatabasesMySQLInstanceSignalError() instead")
    void deleteDatabasesMySQLInstanceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatabasesMySQLInstanceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDatabasesPostgreSQLInstanceSignalError() instead")
    void deleteDatabasesPostgreSQLInstanceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatabasesPostgreSQLInstanceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesEngineSignalError() instead")
    void getDatabasesEngineSignalE(OAIDatabaseEngine summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesEngineSignalError(OAIDatabaseEngine summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesEnginesSignalError() instead")
    void getDatabasesEnginesSignalE(OAIGetDatabasesEngines_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesEnginesSignalError(OAIGetDatabasesEngines_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesInstancesSignalError() instead")
    void getDatabasesInstancesSignalE(OAIGetDatabasesInstances_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesInstancesSignalError(OAIGetDatabasesInstances_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMongoDBInstanceSignalError() instead")
    void getDatabasesMongoDBInstanceSignalE(OAIDatabaseMongoDB summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMongoDBInstanceSignalError(OAIDatabaseMongoDB summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMongoDBInstanceBackupSignalError() instead")
    void getDatabasesMongoDBInstanceBackupSignalE(OAIDatabaseBackup summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMongoDBInstanceBackupSignalError(OAIDatabaseBackup summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMongoDBInstanceBackupsSignalError() instead")
    void getDatabasesMongoDBInstanceBackupsSignalE(OAIGetDatabasesMongoDBInstanceBackups_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMongoDBInstanceBackupsSignalError(OAIGetDatabasesMongoDBInstanceBackups_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMongoDBInstanceCredentialsSignalError() instead")
    void getDatabasesMongoDBInstanceCredentialsSignalE(OAIDatabaseCredentials summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMongoDBInstanceCredentialsSignalError(OAIDatabaseCredentials summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMongoDBInstanceSSLSignalError() instead")
    void getDatabasesMongoDBInstanceSSLSignalE(OAIDatabaseSSL summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMongoDBInstanceSSLSignalError(OAIDatabaseSSL summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMongoDBInstancesSignalError() instead")
    void getDatabasesMongoDBInstancesSignalE(OAIGetDatabasesMongoDBInstances_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMongoDBInstancesSignalError(OAIGetDatabasesMongoDBInstances_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMySQLInstanceSignalError() instead")
    void getDatabasesMySQLInstanceSignalE(OAIDatabaseMySQL summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMySQLInstanceSignalError(OAIDatabaseMySQL summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMySQLInstanceBackupSignalError() instead")
    void getDatabasesMySQLInstanceBackupSignalE(OAIDatabaseBackup summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMySQLInstanceBackupSignalError(OAIDatabaseBackup summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMySQLInstanceBackupsSignalError() instead")
    void getDatabasesMySQLInstanceBackupsSignalE(OAIGetDatabasesMongoDBInstanceBackups_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMySQLInstanceBackupsSignalError(OAIGetDatabasesMongoDBInstanceBackups_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMySQLInstanceCredentialsSignalError() instead")
    void getDatabasesMySQLInstanceCredentialsSignalE(OAIDatabaseCredentials summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMySQLInstanceCredentialsSignalError(OAIDatabaseCredentials summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMySQLInstanceSSLSignalError() instead")
    void getDatabasesMySQLInstanceSSLSignalE(OAIDatabaseSSL summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMySQLInstanceSSLSignalError(OAIDatabaseSSL summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMySQLInstancesSignalError() instead")
    void getDatabasesMySQLInstancesSignalE(OAIGetDatabasesMySQLInstances_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMySQLInstancesSignalError(OAIGetDatabasesMySQLInstances_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesPostgreSQLInstanceSignalError() instead")
    void getDatabasesPostgreSQLInstanceSignalE(OAIDatabasePostgreSQL summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesPostgreSQLInstanceSignalError(OAIDatabasePostgreSQL summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesPostgreSQLInstanceBackupSignalError() instead")
    void getDatabasesPostgreSQLInstanceBackupSignalE(OAIDatabaseBackup summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesPostgreSQLInstanceBackupSignalError(OAIDatabaseBackup summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesPostgreSQLInstanceBackupsSignalError() instead")
    void getDatabasesPostgreSQLInstanceBackupsSignalE(OAIGetDatabasesMongoDBInstanceBackups_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesPostgreSQLInstanceBackupsSignalError(OAIGetDatabasesMongoDBInstanceBackups_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesPostgreSQLInstanceCredentialsSignalError() instead")
    void getDatabasesPostgreSQLInstanceCredentialsSignalE(OAIDatabaseCredentials summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesPostgreSQLInstanceCredentialsSignalError(OAIDatabaseCredentials summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesPostgreSQLInstanceSSLSignalError() instead")
    void getDatabasesPostgreSQLInstanceSSLSignalE(OAIDatabaseSSL summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesPostgreSQLInstanceSSLSignalError(OAIDatabaseSSL summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesPostgreSQLInstancesSignalError() instead")
    void getDatabasesPostgreSQLInstancesSignalE(OAIGetDatabasesPostgreSQLInstances_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesPostgreSQLInstancesSignalError(OAIGetDatabasesPostgreSQLInstances_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesTypeSignalError() instead")
    void getDatabasesTypeSignalE(OAIDatabaseType summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesTypeSignalError(OAIDatabaseType summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesTypesSignalError() instead")
    void getDatabasesTypesSignalE(OAIGetDatabasesTypes_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesTypesSignalError(OAIGetDatabasesTypes_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMongoDBInstanceBackupSignalError() instead")
    void postDatabasesMongoDBInstanceBackupSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMongoDBInstanceBackupSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMongoDBInstanceBackupRestoreSignalError() instead")
    void postDatabasesMongoDBInstanceBackupRestoreSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMongoDBInstanceBackupRestoreSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMongoDBInstanceCredentialsResetSignalError() instead")
    void postDatabasesMongoDBInstanceCredentialsResetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMongoDBInstanceCredentialsResetSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMongoDBInstancePatchSignalError() instead")
    void postDatabasesMongoDBInstancePatchSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMongoDBInstancePatchSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMySQLInstanceBackupSignalError() instead")
    void postDatabasesMySQLInstanceBackupSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMySQLInstanceBackupSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMySQLInstanceBackupRestoreSignalError() instead")
    void postDatabasesMySQLInstanceBackupRestoreSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMySQLInstanceBackupRestoreSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMySQLInstanceCredentialsResetSignalError() instead")
    void postDatabasesMySQLInstanceCredentialsResetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMySQLInstanceCredentialsResetSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMySQLInstancePatchSignalError() instead")
    void postDatabasesMySQLInstancePatchSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMySQLInstancePatchSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMySQLInstancesSignalError() instead")
    void postDatabasesMySQLInstancesSignalE(OAIDatabaseMySQL summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMySQLInstancesSignalError(OAIDatabaseMySQL summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesPostgreSQLInstanceBackupSignalError() instead")
    void postDatabasesPostgreSQLInstanceBackupSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesPostgreSQLInstanceBackupSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesPostgreSQLInstanceBackupRestoreSignalError() instead")
    void postDatabasesPostgreSQLInstanceBackupRestoreSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesPostgreSQLInstanceBackupRestoreSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesPostgreSQLInstanceCredentialsResetSignalError() instead")
    void postDatabasesPostgreSQLInstanceCredentialsResetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesPostgreSQLInstanceCredentialsResetSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesPostgreSQLInstancePatchSignalError() instead")
    void postDatabasesPostgreSQLInstancePatchSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesPostgreSQLInstancePatchSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesPostgreSQLInstancesSignalError() instead")
    void postDatabasesPostgreSQLInstancesSignalE(OAIDatabasePostgreSQL summary, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesPostgreSQLInstancesSignalError(OAIDatabasePostgreSQL summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putDatabasesMongoDBInstanceSignalError() instead")
    void putDatabasesMongoDBInstanceSignalE(OAIDatabaseMongoDB summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putDatabasesMongoDBInstanceSignalError(OAIDatabaseMongoDB summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putDatabasesMySQLInstanceSignalError() instead")
    void putDatabasesMySQLInstanceSignalE(OAIDatabaseMySQL summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putDatabasesMySQLInstanceSignalError(OAIDatabaseMySQL summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putDatabasesPostgreSQLInstanceSignalError() instead")
    void putDatabasesPostgreSQLInstanceSignalE(OAIDatabasePostgreSQL summary, QNetworkReply::NetworkError error_type, QString error_str);
    void putDatabasesPostgreSQLInstanceSignalError(OAIDatabasePostgreSQL summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use deleteDatabaseMongoDBInstanceBackupSignalErrorFull() instead")
    void deleteDatabaseMongoDBInstanceBackupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatabaseMongoDBInstanceBackupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDatabaseMySQLInstanceBackupSignalErrorFull() instead")
    void deleteDatabaseMySQLInstanceBackupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatabaseMySQLInstanceBackupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDatabasePostgreSQLInstanceBackupSignalErrorFull() instead")
    void deleteDatabasePostgreSQLInstanceBackupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatabasePostgreSQLInstanceBackupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDatabasesMongoDBInstanceSignalErrorFull() instead")
    void deleteDatabasesMongoDBInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatabasesMongoDBInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDatabasesMySQLInstanceSignalErrorFull() instead")
    void deleteDatabasesMySQLInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatabasesMySQLInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDatabasesPostgreSQLInstanceSignalErrorFull() instead")
    void deleteDatabasesPostgreSQLInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDatabasesPostgreSQLInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesEngineSignalErrorFull() instead")
    void getDatabasesEngineSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesEngineSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesEnginesSignalErrorFull() instead")
    void getDatabasesEnginesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesEnginesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesInstancesSignalErrorFull() instead")
    void getDatabasesInstancesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesInstancesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMongoDBInstanceSignalErrorFull() instead")
    void getDatabasesMongoDBInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMongoDBInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMongoDBInstanceBackupSignalErrorFull() instead")
    void getDatabasesMongoDBInstanceBackupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMongoDBInstanceBackupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMongoDBInstanceBackupsSignalErrorFull() instead")
    void getDatabasesMongoDBInstanceBackupsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMongoDBInstanceBackupsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMongoDBInstanceCredentialsSignalErrorFull() instead")
    void getDatabasesMongoDBInstanceCredentialsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMongoDBInstanceCredentialsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMongoDBInstanceSSLSignalErrorFull() instead")
    void getDatabasesMongoDBInstanceSSLSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMongoDBInstanceSSLSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMongoDBInstancesSignalErrorFull() instead")
    void getDatabasesMongoDBInstancesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMongoDBInstancesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMySQLInstanceSignalErrorFull() instead")
    void getDatabasesMySQLInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMySQLInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMySQLInstanceBackupSignalErrorFull() instead")
    void getDatabasesMySQLInstanceBackupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMySQLInstanceBackupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMySQLInstanceBackupsSignalErrorFull() instead")
    void getDatabasesMySQLInstanceBackupsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMySQLInstanceBackupsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMySQLInstanceCredentialsSignalErrorFull() instead")
    void getDatabasesMySQLInstanceCredentialsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMySQLInstanceCredentialsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMySQLInstanceSSLSignalErrorFull() instead")
    void getDatabasesMySQLInstanceSSLSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMySQLInstanceSSLSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesMySQLInstancesSignalErrorFull() instead")
    void getDatabasesMySQLInstancesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesMySQLInstancesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesPostgreSQLInstanceSignalErrorFull() instead")
    void getDatabasesPostgreSQLInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesPostgreSQLInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesPostgreSQLInstanceBackupSignalErrorFull() instead")
    void getDatabasesPostgreSQLInstanceBackupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesPostgreSQLInstanceBackupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesPostgreSQLInstanceBackupsSignalErrorFull() instead")
    void getDatabasesPostgreSQLInstanceBackupsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesPostgreSQLInstanceBackupsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesPostgreSQLInstanceCredentialsSignalErrorFull() instead")
    void getDatabasesPostgreSQLInstanceCredentialsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesPostgreSQLInstanceCredentialsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesPostgreSQLInstanceSSLSignalErrorFull() instead")
    void getDatabasesPostgreSQLInstanceSSLSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesPostgreSQLInstanceSSLSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesPostgreSQLInstancesSignalErrorFull() instead")
    void getDatabasesPostgreSQLInstancesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesPostgreSQLInstancesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesTypeSignalErrorFull() instead")
    void getDatabasesTypeSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesTypeSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDatabasesTypesSignalErrorFull() instead")
    void getDatabasesTypesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDatabasesTypesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMongoDBInstanceBackupSignalErrorFull() instead")
    void postDatabasesMongoDBInstanceBackupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMongoDBInstanceBackupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMongoDBInstanceBackupRestoreSignalErrorFull() instead")
    void postDatabasesMongoDBInstanceBackupRestoreSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMongoDBInstanceBackupRestoreSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMongoDBInstanceCredentialsResetSignalErrorFull() instead")
    void postDatabasesMongoDBInstanceCredentialsResetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMongoDBInstanceCredentialsResetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMongoDBInstancePatchSignalErrorFull() instead")
    void postDatabasesMongoDBInstancePatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMongoDBInstancePatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMySQLInstanceBackupSignalErrorFull() instead")
    void postDatabasesMySQLInstanceBackupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMySQLInstanceBackupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMySQLInstanceBackupRestoreSignalErrorFull() instead")
    void postDatabasesMySQLInstanceBackupRestoreSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMySQLInstanceBackupRestoreSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMySQLInstanceCredentialsResetSignalErrorFull() instead")
    void postDatabasesMySQLInstanceCredentialsResetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMySQLInstanceCredentialsResetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMySQLInstancePatchSignalErrorFull() instead")
    void postDatabasesMySQLInstancePatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMySQLInstancePatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesMySQLInstancesSignalErrorFull() instead")
    void postDatabasesMySQLInstancesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesMySQLInstancesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesPostgreSQLInstanceBackupSignalErrorFull() instead")
    void postDatabasesPostgreSQLInstanceBackupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesPostgreSQLInstanceBackupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesPostgreSQLInstanceBackupRestoreSignalErrorFull() instead")
    void postDatabasesPostgreSQLInstanceBackupRestoreSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesPostgreSQLInstanceBackupRestoreSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesPostgreSQLInstanceCredentialsResetSignalErrorFull() instead")
    void postDatabasesPostgreSQLInstanceCredentialsResetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesPostgreSQLInstanceCredentialsResetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesPostgreSQLInstancePatchSignalErrorFull() instead")
    void postDatabasesPostgreSQLInstancePatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesPostgreSQLInstancePatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postDatabasesPostgreSQLInstancesSignalErrorFull() instead")
    void postDatabasesPostgreSQLInstancesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postDatabasesPostgreSQLInstancesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putDatabasesMongoDBInstanceSignalErrorFull() instead")
    void putDatabasesMongoDBInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putDatabasesMongoDBInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putDatabasesMySQLInstanceSignalErrorFull() instead")
    void putDatabasesMySQLInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putDatabasesMySQLInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putDatabasesPostgreSQLInstanceSignalErrorFull() instead")
    void putDatabasesPostgreSQLInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putDatabasesPostgreSQLInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
