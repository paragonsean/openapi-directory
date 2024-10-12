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

#ifndef OAI_OAIAccountApi_H
#define OAI_OAIAccountApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAccount.h"
#include "OAIAccountSettings.h"
#include "OAICancelAccount_200_response.h"
#include "OAICancelAccount_409_response.h"
#include "OAICancelAccount_request.h"
#include "OAICreateEntityTransfer_request.h"
#include "OAICreatePayPalPayment_200_response.h"
#include "OAICreatePaymentMethod_request.h"
#include "OAICreatePayment_202_response.h"
#include "OAICreatePromoCredit_request.h"
#include "OAICreateServiceTransfer_request.h"
#include "OAICreditCard.h"
#include "OAIEntityTransfer.h"
#include "OAIEvent.h"
#include "OAIGetAccountLogins_200_response.h"
#include "OAIGetAccount_default_response.h"
#include "OAIGetClients_200_response.h"
#include "OAIGetEntityTransfers_200_response.h"
#include "OAIGetEvents_200_response.h"
#include "OAIGetInvoiceItems_200_response.h"
#include "OAIGetInvoices_200_response.h"
#include "OAIGetMaintenance_200_response.h"
#include "OAIGetNotifications_200_response.h"
#include "OAIGetPaymentMethods_200_response.h"
#include "OAIGetPayments_200_response.h"
#include "OAIGetServiceTransfers_200_response.h"
#include "OAIGetUsers_200_response.h"
#include "OAIGrantsResponse.h"
#include "OAIHttpFileElement.h"
#include "OAIInvoice.h"
#include "OAILogin.h"
#include "OAIOAuthClient.h"
#include "OAIObject.h"
#include "OAIPayPal.h"
#include "OAIPayPalExecute.h"
#include "OAIPayment.h"
#include "OAIPaymentMethod.h"
#include "OAIPaymentRequest.h"
#include "OAIPromotion.h"
#include "OAIServiceTransfer.h"
#include "OAITransfer.h"
#include "OAIUser.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIAccountApi : public QObject {
    Q_OBJECT

public:
    OAIAccountApi(const int timeOut = 0);
    ~OAIAccountApi();

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
    * @param[in]  token QString [required]
    */
    Q_DECL_DEPRECATED virtual void acceptEntityTransfer(const QString &token);

    /**
    * @param[in]  token QString [required]
    */
    virtual void acceptServiceTransfer(const QString &token);

    /**
    * @param[in]  oai_cancel_account_request OAICancelAccount_request [required]
    */
    virtual void cancelAccount(const OAICancelAccount_request &oai_cancel_account_request);

    /**
    * @param[in]  oaio_auth_client OAIOAuthClient [optional]
    */
    virtual void createClient(const ::OpenAPI::OptionalParam<OAIOAuthClient> &oaio_auth_client = ::OpenAPI::OptionalParam<OAIOAuthClient>());

    /**
    * @param[in]  oai_credit_card OAICreditCard [required]
    */
    Q_DECL_DEPRECATED virtual void createCreditCard(const OAICreditCard &oai_credit_card);

    /**
    * @param[in]  oai_create_entity_transfer_request OAICreateEntityTransfer_request [optional]
    */
    Q_DECL_DEPRECATED virtual void createEntityTransfer(const ::OpenAPI::OptionalParam<OAICreateEntityTransfer_request> &oai_create_entity_transfer_request = ::OpenAPI::OptionalParam<OAICreateEntityTransfer_request>());

    /**
    * @param[in]  oai_pay_pal OAIPayPal [required]
    */
    Q_DECL_DEPRECATED virtual void createPayPalPayment(const OAIPayPal &oai_pay_pal);

    /**
    * @param[in]  oai_payment_request OAIPaymentRequest [required]
    */
    virtual void createPayment(const OAIPaymentRequest &oai_payment_request);

    /**
    * @param[in]  oai_create_payment_method_request OAICreatePaymentMethod_request [required]
    */
    virtual void createPaymentMethod(const OAICreatePaymentMethod_request &oai_create_payment_method_request);

    /**
    * @param[in]  oai_create_promo_credit_request OAICreatePromoCredit_request [optional]
    */
    virtual void createPromoCredit(const ::OpenAPI::OptionalParam<OAICreatePromoCredit_request> &oai_create_promo_credit_request = ::OpenAPI::OptionalParam<OAICreatePromoCredit_request>());

    /**
    * @param[in]  oai_create_service_transfer_request OAICreateServiceTransfer_request [optional]
    */
    virtual void createServiceTransfer(const ::OpenAPI::OptionalParam<OAICreateServiceTransfer_request> &oai_create_service_transfer_request = ::OpenAPI::OptionalParam<OAICreateServiceTransfer_request>());

    /**
    * @param[in]  oai_user OAIUser [optional]
    */
    virtual void createUser(const ::OpenAPI::OptionalParam<OAIUser> &oai_user = ::OpenAPI::OptionalParam<OAIUser>());

    /**
    * @param[in]  client_id QString [required]
    */
    virtual void deleteClient(const QString &client_id);

    /**
    * @param[in]  token QString [required]
    */
    Q_DECL_DEPRECATED virtual void deleteEntityTransfer(const QString &token);

    /**
    * @param[in]  payment_method_id qint32 [required]
    */
    virtual void deletePaymentMethod(const qint32 &payment_method_id);

    /**
    * @param[in]  token QString [required]
    */
    virtual void deleteServiceTransfer(const QString &token);

    /**
    * @param[in]  username QString [required]
    */
    virtual void deleteUser(const QString &username);


    virtual void enableAccountManaged();

    /**
    * @param[in]  event_id qint32 [required]
    */
    virtual void eventRead(const qint32 &event_id);

    /**
    * @param[in]  event_id qint32 [required]
    */
    virtual void eventSeen(const qint32 &event_id);

    /**
    * @param[in]  oai_pay_pal_execute OAIPayPalExecute [required]
    */
    Q_DECL_DEPRECATED virtual void executePayPalPayment(const OAIPayPalExecute &oai_pay_pal_execute);


    virtual void getAccount();

    /**
    * @param[in]  login_id qint32 [required]
    */
    virtual void getAccountLogin(const qint32 &login_id);


    virtual void getAccountLogins();


    virtual void getAccountSettings();

    /**
    * @param[in]  client_id QString [required]
    */
    virtual void getClient(const QString &client_id);

    /**
    * @param[in]  client_id QString [required]
    */
    virtual void getClientThumbnail(const QString &client_id);

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getClients(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  token QString [required]
    */
    Q_DECL_DEPRECATED virtual void getEntityTransfer(const QString &token);

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    Q_DECL_DEPRECATED virtual void getEntityTransfers(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  event_id qint32 [required]
    */
    virtual void getEvent(const qint32 &event_id);

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getEvents(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  invoice_id qint32 [required]
    */
    virtual void getInvoice(const qint32 &invoice_id);

    /**
    * @param[in]  invoice_id qint32 [required]
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getInvoiceItems(const qint32 &invoice_id, const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getInvoices(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());


    virtual void getMaintenance();


    virtual void getNotifications();

    /**
    * @param[in]  payment_id qint32 [required]
    */
    virtual void getPayment(const qint32 &payment_id);

    /**
    * @param[in]  payment_method_id qint32 [required]
    */
    virtual void getPaymentMethod(const qint32 &payment_method_id);

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getPaymentMethods(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getPayments(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  token QString [required]
    */
    virtual void getServiceTransfer(const QString &token);

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getServiceTransfers(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());


    virtual void getTransfer();

    /**
    * @param[in]  username QString [required]
    */
    virtual void getUser(const QString &username);

    /**
    * @param[in]  username QString [required]
    */
    virtual void getUserGrants(const QString &username);

    /**
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getUsers(const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  payment_method_id qint32 [required]
    */
    virtual void makePaymentMethodDefault(const qint32 &payment_method_id);

    /**
    * @param[in]  client_id QString [required]
    */
    virtual void resetClientSecret(const QString &client_id);

    /**
    * @param[in]  client_id QString [required]
    * @param[in]  body OAIHttpFileElement [required]
    */
    virtual void setClientThumbnail(const QString &client_id, const OAIHttpFileElement &body);

    /**
    * @param[in]  oai_account OAIAccount [required]
    */
    virtual void updateAccount(const OAIAccount &oai_account);

    /**
    * @param[in]  oai_account_settings OAIAccountSettings [required]
    */
    virtual void updateAccountSettings(const OAIAccountSettings &oai_account_settings);

    /**
    * @param[in]  client_id QString [required]
    * @param[in]  oaio_auth_client OAIOAuthClient [optional]
    */
    virtual void updateClient(const QString &client_id, const ::OpenAPI::OptionalParam<OAIOAuthClient> &oaio_auth_client = ::OpenAPI::OptionalParam<OAIOAuthClient>());

    /**
    * @param[in]  username QString [required]
    * @param[in]  oai_user OAIUser [optional]
    */
    virtual void updateUser(const QString &username, const ::OpenAPI::OptionalParam<OAIUser> &oai_user = ::OpenAPI::OptionalParam<OAIUser>());

    /**
    * @param[in]  username QString [required]
    * @param[in]  oai_grants_response OAIGrantsResponse [required]
    */
    virtual void updateUserGrants(const QString &username, const OAIGrantsResponse &oai_grants_response);


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

    void acceptEntityTransferCallback(OAIHttpRequestWorker *worker);
    void acceptServiceTransferCallback(OAIHttpRequestWorker *worker);
    void cancelAccountCallback(OAIHttpRequestWorker *worker);
    void createClientCallback(OAIHttpRequestWorker *worker);
    void createCreditCardCallback(OAIHttpRequestWorker *worker);
    void createEntityTransferCallback(OAIHttpRequestWorker *worker);
    void createPayPalPaymentCallback(OAIHttpRequestWorker *worker);
    void createPaymentCallback(OAIHttpRequestWorker *worker);
    void createPaymentMethodCallback(OAIHttpRequestWorker *worker);
    void createPromoCreditCallback(OAIHttpRequestWorker *worker);
    void createServiceTransferCallback(OAIHttpRequestWorker *worker);
    void createUserCallback(OAIHttpRequestWorker *worker);
    void deleteClientCallback(OAIHttpRequestWorker *worker);
    void deleteEntityTransferCallback(OAIHttpRequestWorker *worker);
    void deletePaymentMethodCallback(OAIHttpRequestWorker *worker);
    void deleteServiceTransferCallback(OAIHttpRequestWorker *worker);
    void deleteUserCallback(OAIHttpRequestWorker *worker);
    void enableAccountManagedCallback(OAIHttpRequestWorker *worker);
    void eventReadCallback(OAIHttpRequestWorker *worker);
    void eventSeenCallback(OAIHttpRequestWorker *worker);
    void executePayPalPaymentCallback(OAIHttpRequestWorker *worker);
    void getAccountCallback(OAIHttpRequestWorker *worker);
    void getAccountLoginCallback(OAIHttpRequestWorker *worker);
    void getAccountLoginsCallback(OAIHttpRequestWorker *worker);
    void getAccountSettingsCallback(OAIHttpRequestWorker *worker);
    void getClientCallback(OAIHttpRequestWorker *worker);
    void getClientThumbnailCallback(OAIHttpRequestWorker *worker);
    void getClientsCallback(OAIHttpRequestWorker *worker);
    void getEntityTransferCallback(OAIHttpRequestWorker *worker);
    void getEntityTransfersCallback(OAIHttpRequestWorker *worker);
    void getEventCallback(OAIHttpRequestWorker *worker);
    void getEventsCallback(OAIHttpRequestWorker *worker);
    void getInvoiceCallback(OAIHttpRequestWorker *worker);
    void getInvoiceItemsCallback(OAIHttpRequestWorker *worker);
    void getInvoicesCallback(OAIHttpRequestWorker *worker);
    void getMaintenanceCallback(OAIHttpRequestWorker *worker);
    void getNotificationsCallback(OAIHttpRequestWorker *worker);
    void getPaymentCallback(OAIHttpRequestWorker *worker);
    void getPaymentMethodCallback(OAIHttpRequestWorker *worker);
    void getPaymentMethodsCallback(OAIHttpRequestWorker *worker);
    void getPaymentsCallback(OAIHttpRequestWorker *worker);
    void getServiceTransferCallback(OAIHttpRequestWorker *worker);
    void getServiceTransfersCallback(OAIHttpRequestWorker *worker);
    void getTransferCallback(OAIHttpRequestWorker *worker);
    void getUserCallback(OAIHttpRequestWorker *worker);
    void getUserGrantsCallback(OAIHttpRequestWorker *worker);
    void getUsersCallback(OAIHttpRequestWorker *worker);
    void makePaymentMethodDefaultCallback(OAIHttpRequestWorker *worker);
    void resetClientSecretCallback(OAIHttpRequestWorker *worker);
    void setClientThumbnailCallback(OAIHttpRequestWorker *worker);
    void updateAccountCallback(OAIHttpRequestWorker *worker);
    void updateAccountSettingsCallback(OAIHttpRequestWorker *worker);
    void updateClientCallback(OAIHttpRequestWorker *worker);
    void updateUserCallback(OAIHttpRequestWorker *worker);
    void updateUserGrantsCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void acceptEntityTransferSignal(OAIObject summary);
    void acceptServiceTransferSignal(OAIObject summary);
    void cancelAccountSignal(OAICancelAccount_200_response summary);
    void createClientSignal(OAIOAuthClient summary);
    void createCreditCardSignal(OAIObject summary);
    void createEntityTransferSignal(OAIEntityTransfer summary);
    void createPayPalPaymentSignal(OAICreatePayPalPayment_200_response summary);
    void createPaymentSignal(OAIPayment summary);
    void createPaymentMethodSignal(OAIObject summary);
    void createPromoCreditSignal(OAIPromotion summary);
    void createServiceTransferSignal(OAIServiceTransfer summary);
    void createUserSignal(OAIUser summary);
    void deleteClientSignal(OAIObject summary);
    void deleteEntityTransferSignal(OAIObject summary);
    void deletePaymentMethodSignal(OAIObject summary);
    void deleteServiceTransferSignal(OAIObject summary);
    void deleteUserSignal(OAIObject summary);
    void enableAccountManagedSignal(OAIObject summary);
    void eventReadSignal(OAIObject summary);
    void eventSeenSignal(OAIObject summary);
    void executePayPalPaymentSignal(OAIObject summary);
    void getAccountSignal(OAIAccount summary);
    void getAccountLoginSignal(OAILogin summary);
    void getAccountLoginsSignal(OAIGetAccountLogins_200_response summary);
    void getAccountSettingsSignal(OAIAccountSettings summary);
    void getClientSignal(OAIOAuthClient summary);
    void getClientThumbnailSignal(OAIHttpFileElement summary);
    void getClientsSignal(OAIGetClients_200_response summary);
    void getEntityTransferSignal(OAIEntityTransfer summary);
    void getEntityTransfersSignal(OAIGetEntityTransfers_200_response summary);
    void getEventSignal(OAIEvent summary);
    void getEventsSignal(OAIGetEvents_200_response summary);
    void getInvoiceSignal(OAIInvoice summary);
    void getInvoiceItemsSignal(OAIGetInvoiceItems_200_response summary);
    void getInvoicesSignal(OAIGetInvoices_200_response summary);
    void getMaintenanceSignal(OAIGetMaintenance_200_response summary);
    void getNotificationsSignal(OAIGetNotifications_200_response summary);
    void getPaymentSignal(OAIPayment summary);
    void getPaymentMethodSignal(OAIPaymentMethod summary);
    void getPaymentMethodsSignal(OAIGetPaymentMethods_200_response summary);
    void getPaymentsSignal(OAIGetPayments_200_response summary);
    void getServiceTransferSignal(OAIServiceTransfer summary);
    void getServiceTransfersSignal(OAIGetServiceTransfers_200_response summary);
    void getTransferSignal(OAITransfer summary);
    void getUserSignal(OAIUser summary);
    void getUserGrantsSignal(OAIGrantsResponse summary);
    void getUsersSignal(OAIGetUsers_200_response summary);
    void makePaymentMethodDefaultSignal(OAIObject summary);
    void resetClientSecretSignal(OAIOAuthClient summary);
    void setClientThumbnailSignal(OAIObject summary);
    void updateAccountSignal(OAIAccount summary);
    void updateAccountSettingsSignal(OAIAccountSettings summary);
    void updateClientSignal(OAIOAuthClient summary);
    void updateUserSignal(OAIUser summary);
    void updateUserGrantsSignal(OAIGrantsResponse summary);


    void acceptEntityTransferSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void acceptServiceTransferSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void cancelAccountSignalFull(OAIHttpRequestWorker *worker, OAICancelAccount_200_response summary);
    void createClientSignalFull(OAIHttpRequestWorker *worker, OAIOAuthClient summary);
    void createCreditCardSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void createEntityTransferSignalFull(OAIHttpRequestWorker *worker, OAIEntityTransfer summary);
    void createPayPalPaymentSignalFull(OAIHttpRequestWorker *worker, OAICreatePayPalPayment_200_response summary);
    void createPaymentSignalFull(OAIHttpRequestWorker *worker, OAIPayment summary);
    void createPaymentMethodSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void createPromoCreditSignalFull(OAIHttpRequestWorker *worker, OAIPromotion summary);
    void createServiceTransferSignalFull(OAIHttpRequestWorker *worker, OAIServiceTransfer summary);
    void createUserSignalFull(OAIHttpRequestWorker *worker, OAIUser summary);
    void deleteClientSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deleteEntityTransferSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deletePaymentMethodSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deleteServiceTransferSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deleteUserSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void enableAccountManagedSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void eventReadSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void eventSeenSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void executePayPalPaymentSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void getAccountSignalFull(OAIHttpRequestWorker *worker, OAIAccount summary);
    void getAccountLoginSignalFull(OAIHttpRequestWorker *worker, OAILogin summary);
    void getAccountLoginsSignalFull(OAIHttpRequestWorker *worker, OAIGetAccountLogins_200_response summary);
    void getAccountSettingsSignalFull(OAIHttpRequestWorker *worker, OAIAccountSettings summary);
    void getClientSignalFull(OAIHttpRequestWorker *worker, OAIOAuthClient summary);
    void getClientThumbnailSignalFull(OAIHttpRequestWorker *worker, OAIHttpFileElement summary);
    void getClientsSignalFull(OAIHttpRequestWorker *worker, OAIGetClients_200_response summary);
    void getEntityTransferSignalFull(OAIHttpRequestWorker *worker, OAIEntityTransfer summary);
    void getEntityTransfersSignalFull(OAIHttpRequestWorker *worker, OAIGetEntityTransfers_200_response summary);
    void getEventSignalFull(OAIHttpRequestWorker *worker, OAIEvent summary);
    void getEventsSignalFull(OAIHttpRequestWorker *worker, OAIGetEvents_200_response summary);
    void getInvoiceSignalFull(OAIHttpRequestWorker *worker, OAIInvoice summary);
    void getInvoiceItemsSignalFull(OAIHttpRequestWorker *worker, OAIGetInvoiceItems_200_response summary);
    void getInvoicesSignalFull(OAIHttpRequestWorker *worker, OAIGetInvoices_200_response summary);
    void getMaintenanceSignalFull(OAIHttpRequestWorker *worker, OAIGetMaintenance_200_response summary);
    void getNotificationsSignalFull(OAIHttpRequestWorker *worker, OAIGetNotifications_200_response summary);
    void getPaymentSignalFull(OAIHttpRequestWorker *worker, OAIPayment summary);
    void getPaymentMethodSignalFull(OAIHttpRequestWorker *worker, OAIPaymentMethod summary);
    void getPaymentMethodsSignalFull(OAIHttpRequestWorker *worker, OAIGetPaymentMethods_200_response summary);
    void getPaymentsSignalFull(OAIHttpRequestWorker *worker, OAIGetPayments_200_response summary);
    void getServiceTransferSignalFull(OAIHttpRequestWorker *worker, OAIServiceTransfer summary);
    void getServiceTransfersSignalFull(OAIHttpRequestWorker *worker, OAIGetServiceTransfers_200_response summary);
    void getTransferSignalFull(OAIHttpRequestWorker *worker, OAITransfer summary);
    void getUserSignalFull(OAIHttpRequestWorker *worker, OAIUser summary);
    void getUserGrantsSignalFull(OAIHttpRequestWorker *worker, OAIGrantsResponse summary);
    void getUsersSignalFull(OAIHttpRequestWorker *worker, OAIGetUsers_200_response summary);
    void makePaymentMethodDefaultSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void resetClientSecretSignalFull(OAIHttpRequestWorker *worker, OAIOAuthClient summary);
    void setClientThumbnailSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateAccountSignalFull(OAIHttpRequestWorker *worker, OAIAccount summary);
    void updateAccountSettingsSignalFull(OAIHttpRequestWorker *worker, OAIAccountSettings summary);
    void updateClientSignalFull(OAIHttpRequestWorker *worker, OAIOAuthClient summary);
    void updateUserSignalFull(OAIHttpRequestWorker *worker, OAIUser summary);
    void updateUserGrantsSignalFull(OAIHttpRequestWorker *worker, OAIGrantsResponse summary);

    Q_DECL_DEPRECATED_X("Use acceptEntityTransferSignalError() instead")
    void acceptEntityTransferSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void acceptEntityTransferSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use acceptServiceTransferSignalError() instead")
    void acceptServiceTransferSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void acceptServiceTransferSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cancelAccountSignalError() instead")
    void cancelAccountSignalE(OAICancelAccount_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void cancelAccountSignalError(OAICancelAccount_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createClientSignalError() instead")
    void createClientSignalE(OAIOAuthClient summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createClientSignalError(OAIOAuthClient summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createCreditCardSignalError() instead")
    void createCreditCardSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createCreditCardSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createEntityTransferSignalError() instead")
    void createEntityTransferSignalE(OAIEntityTransfer summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createEntityTransferSignalError(OAIEntityTransfer summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createPayPalPaymentSignalError() instead")
    void createPayPalPaymentSignalE(OAICreatePayPalPayment_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createPayPalPaymentSignalError(OAICreatePayPalPayment_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createPaymentSignalError() instead")
    void createPaymentSignalE(OAIPayment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createPaymentSignalError(OAIPayment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createPaymentMethodSignalError() instead")
    void createPaymentMethodSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createPaymentMethodSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createPromoCreditSignalError() instead")
    void createPromoCreditSignalE(OAIPromotion summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createPromoCreditSignalError(OAIPromotion summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createServiceTransferSignalError() instead")
    void createServiceTransferSignalE(OAIServiceTransfer summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createServiceTransferSignalError(OAIServiceTransfer summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createUserSignalError() instead")
    void createUserSignalE(OAIUser summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createUserSignalError(OAIUser summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteClientSignalError() instead")
    void deleteClientSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteClientSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteEntityTransferSignalError() instead")
    void deleteEntityTransferSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteEntityTransferSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deletePaymentMethodSignalError() instead")
    void deletePaymentMethodSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deletePaymentMethodSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteServiceTransferSignalError() instead")
    void deleteServiceTransferSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteServiceTransferSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteUserSignalError() instead")
    void deleteUserSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteUserSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use enableAccountManagedSignalError() instead")
    void enableAccountManagedSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void enableAccountManagedSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventReadSignalError() instead")
    void eventReadSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eventReadSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventSeenSignalError() instead")
    void eventSeenSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eventSeenSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use executePayPalPaymentSignalError() instead")
    void executePayPalPaymentSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void executePayPalPaymentSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAccountSignalError() instead")
    void getAccountSignalE(OAIAccount summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAccountSignalError(OAIAccount summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAccountLoginSignalError() instead")
    void getAccountLoginSignalE(OAILogin summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAccountLoginSignalError(OAILogin summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAccountLoginsSignalError() instead")
    void getAccountLoginsSignalE(OAIGetAccountLogins_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAccountLoginsSignalError(OAIGetAccountLogins_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAccountSettingsSignalError() instead")
    void getAccountSettingsSignalE(OAIAccountSettings summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAccountSettingsSignalError(OAIAccountSettings summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getClientSignalError() instead")
    void getClientSignalE(OAIOAuthClient summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getClientSignalError(OAIOAuthClient summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getClientThumbnailSignalError() instead")
    void getClientThumbnailSignalE(OAIHttpFileElement summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getClientThumbnailSignalError(OAIHttpFileElement summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getClientsSignalError() instead")
    void getClientsSignalE(OAIGetClients_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getClientsSignalError(OAIGetClients_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEntityTransferSignalError() instead")
    void getEntityTransferSignalE(OAIEntityTransfer summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getEntityTransferSignalError(OAIEntityTransfer summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEntityTransfersSignalError() instead")
    void getEntityTransfersSignalE(OAIGetEntityTransfers_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getEntityTransfersSignalError(OAIGetEntityTransfers_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEventSignalError() instead")
    void getEventSignalE(OAIEvent summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getEventSignalError(OAIEvent summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEventsSignalError() instead")
    void getEventsSignalE(OAIGetEvents_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getEventsSignalError(OAIGetEvents_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceSignalError() instead")
    void getInvoiceSignalE(OAIInvoice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceSignalError(OAIInvoice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceItemsSignalError() instead")
    void getInvoiceItemsSignalE(OAIGetInvoiceItems_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceItemsSignalError(OAIGetInvoiceItems_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoicesSignalError() instead")
    void getInvoicesSignalE(OAIGetInvoices_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoicesSignalError(OAIGetInvoices_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMaintenanceSignalError() instead")
    void getMaintenanceSignalE(OAIGetMaintenance_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMaintenanceSignalError(OAIGetMaintenance_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNotificationsSignalError() instead")
    void getNotificationsSignalE(OAIGetNotifications_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNotificationsSignalError(OAIGetNotifications_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPaymentSignalError() instead")
    void getPaymentSignalE(OAIPayment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPaymentSignalError(OAIPayment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPaymentMethodSignalError() instead")
    void getPaymentMethodSignalE(OAIPaymentMethod summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPaymentMethodSignalError(OAIPaymentMethod summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPaymentMethodsSignalError() instead")
    void getPaymentMethodsSignalE(OAIGetPaymentMethods_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPaymentMethodsSignalError(OAIGetPaymentMethods_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPaymentsSignalError() instead")
    void getPaymentsSignalE(OAIGetPayments_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPaymentsSignalError(OAIGetPayments_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceTransferSignalError() instead")
    void getServiceTransferSignalE(OAIServiceTransfer summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceTransferSignalError(OAIServiceTransfer summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceTransfersSignalError() instead")
    void getServiceTransfersSignalE(OAIGetServiceTransfers_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceTransfersSignalError(OAIGetServiceTransfers_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTransferSignalError() instead")
    void getTransferSignalE(OAITransfer summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTransferSignalError(OAITransfer summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUserSignalError() instead")
    void getUserSignalE(OAIUser summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getUserSignalError(OAIUser summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUserGrantsSignalError() instead")
    void getUserGrantsSignalE(OAIGrantsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getUserGrantsSignalError(OAIGrantsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUsersSignalError() instead")
    void getUsersSignalE(OAIGetUsers_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getUsersSignalError(OAIGetUsers_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use makePaymentMethodDefaultSignalError() instead")
    void makePaymentMethodDefaultSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void makePaymentMethodDefaultSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resetClientSecretSignalError() instead")
    void resetClientSecretSignalE(OAIOAuthClient summary, QNetworkReply::NetworkError error_type, QString error_str);
    void resetClientSecretSignalError(OAIOAuthClient summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setClientThumbnailSignalError() instead")
    void setClientThumbnailSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setClientThumbnailSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateAccountSignalError() instead")
    void updateAccountSignalE(OAIAccount summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateAccountSignalError(OAIAccount summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateAccountSettingsSignalError() instead")
    void updateAccountSettingsSignalE(OAIAccountSettings summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateAccountSettingsSignalError(OAIAccountSettings summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateClientSignalError() instead")
    void updateClientSignalE(OAIOAuthClient summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateClientSignalError(OAIOAuthClient summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateUserSignalError() instead")
    void updateUserSignalE(OAIUser summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateUserSignalError(OAIUser summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateUserGrantsSignalError() instead")
    void updateUserGrantsSignalE(OAIGrantsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateUserGrantsSignalError(OAIGrantsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use acceptEntityTransferSignalErrorFull() instead")
    void acceptEntityTransferSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void acceptEntityTransferSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use acceptServiceTransferSignalErrorFull() instead")
    void acceptServiceTransferSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void acceptServiceTransferSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cancelAccountSignalErrorFull() instead")
    void cancelAccountSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void cancelAccountSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createClientSignalErrorFull() instead")
    void createClientSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createClientSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createCreditCardSignalErrorFull() instead")
    void createCreditCardSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createCreditCardSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createEntityTransferSignalErrorFull() instead")
    void createEntityTransferSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createEntityTransferSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createPayPalPaymentSignalErrorFull() instead")
    void createPayPalPaymentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createPayPalPaymentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createPaymentSignalErrorFull() instead")
    void createPaymentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createPaymentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createPaymentMethodSignalErrorFull() instead")
    void createPaymentMethodSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createPaymentMethodSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createPromoCreditSignalErrorFull() instead")
    void createPromoCreditSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createPromoCreditSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createServiceTransferSignalErrorFull() instead")
    void createServiceTransferSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createServiceTransferSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createUserSignalErrorFull() instead")
    void createUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteClientSignalErrorFull() instead")
    void deleteClientSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteClientSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteEntityTransferSignalErrorFull() instead")
    void deleteEntityTransferSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteEntityTransferSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deletePaymentMethodSignalErrorFull() instead")
    void deletePaymentMethodSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deletePaymentMethodSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteServiceTransferSignalErrorFull() instead")
    void deleteServiceTransferSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteServiceTransferSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteUserSignalErrorFull() instead")
    void deleteUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use enableAccountManagedSignalErrorFull() instead")
    void enableAccountManagedSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void enableAccountManagedSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventReadSignalErrorFull() instead")
    void eventReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eventReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eventSeenSignalErrorFull() instead")
    void eventSeenSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eventSeenSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use executePayPalPaymentSignalErrorFull() instead")
    void executePayPalPaymentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void executePayPalPaymentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAccountSignalErrorFull() instead")
    void getAccountSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAccountSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAccountLoginSignalErrorFull() instead")
    void getAccountLoginSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAccountLoginSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAccountLoginsSignalErrorFull() instead")
    void getAccountLoginsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAccountLoginsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAccountSettingsSignalErrorFull() instead")
    void getAccountSettingsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAccountSettingsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getClientSignalErrorFull() instead")
    void getClientSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getClientSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getClientThumbnailSignalErrorFull() instead")
    void getClientThumbnailSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getClientThumbnailSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getClientsSignalErrorFull() instead")
    void getClientsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getClientsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEntityTransferSignalErrorFull() instead")
    void getEntityTransferSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEntityTransferSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEntityTransfersSignalErrorFull() instead")
    void getEntityTransfersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEntityTransfersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEventSignalErrorFull() instead")
    void getEventSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEventSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEventsSignalErrorFull() instead")
    void getEventsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEventsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceSignalErrorFull() instead")
    void getInvoiceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoiceItemsSignalErrorFull() instead")
    void getInvoiceItemsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoiceItemsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getInvoicesSignalErrorFull() instead")
    void getInvoicesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getInvoicesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMaintenanceSignalErrorFull() instead")
    void getMaintenanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMaintenanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNotificationsSignalErrorFull() instead")
    void getNotificationsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNotificationsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPaymentSignalErrorFull() instead")
    void getPaymentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPaymentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPaymentMethodSignalErrorFull() instead")
    void getPaymentMethodSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPaymentMethodSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPaymentMethodsSignalErrorFull() instead")
    void getPaymentMethodsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPaymentMethodsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPaymentsSignalErrorFull() instead")
    void getPaymentsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPaymentsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceTransferSignalErrorFull() instead")
    void getServiceTransferSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceTransferSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceTransfersSignalErrorFull() instead")
    void getServiceTransfersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceTransfersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTransferSignalErrorFull() instead")
    void getTransferSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTransferSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUserSignalErrorFull() instead")
    void getUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUserGrantsSignalErrorFull() instead")
    void getUserGrantsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getUserGrantsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUsersSignalErrorFull() instead")
    void getUsersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getUsersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use makePaymentMethodDefaultSignalErrorFull() instead")
    void makePaymentMethodDefaultSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void makePaymentMethodDefaultSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resetClientSecretSignalErrorFull() instead")
    void resetClientSecretSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void resetClientSecretSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setClientThumbnailSignalErrorFull() instead")
    void setClientThumbnailSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setClientThumbnailSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateAccountSignalErrorFull() instead")
    void updateAccountSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateAccountSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateAccountSettingsSignalErrorFull() instead")
    void updateAccountSettingsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateAccountSettingsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateClientSignalErrorFull() instead")
    void updateClientSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateClientSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateUserSignalErrorFull() instead")
    void updateUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateUserGrantsSignalErrorFull() instead")
    void updateUserGrantsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateUserGrantsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
