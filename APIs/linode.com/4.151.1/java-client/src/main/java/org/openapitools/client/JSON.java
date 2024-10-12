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


package org.openapitools.client;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapter;
import com.google.gson.internal.bind.util.ISO8601Utils;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.google.gson.JsonElement;
import io.gsonfire.GsonFireBuilder;
import io.gsonfire.TypeSelector;

import okio.ByteString;

import java.io.IOException;
import java.io.StringReader;
import java.lang.reflect.Type;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.ParsePosition;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.Locale;
import java.util.Map;
import java.util.HashMap;

/*
 * A JSON utility class
 *
 * NOTE: in the future, this class may be converted to static, which may break
 *       backward-compatibility
 */
public class JSON {
    private static Gson gson;
    private static boolean isLenientOnJson = false;
    private static DateTypeAdapter dateTypeAdapter = new DateTypeAdapter();
    private static SqlDateTypeAdapter sqlDateTypeAdapter = new SqlDateTypeAdapter();
    private static OffsetDateTimeTypeAdapter offsetDateTimeTypeAdapter = new OffsetDateTimeTypeAdapter();
    private static LocalDateTypeAdapter localDateTypeAdapter = new LocalDateTypeAdapter();
    private static ByteArrayAdapter byteArrayAdapter = new ByteArrayAdapter();

    @SuppressWarnings("unchecked")
    public static GsonBuilder createGson() {
        GsonFireBuilder fireBuilder = new GsonFireBuilder()
                .registerTypeSelector(org.openapitools.client.model.GetManagedStats200ResponseData.class, new TypeSelector<org.openapitools.client.model.GetManagedStats200ResponseData>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.GetManagedStats200ResponseData> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("StatsDataAvailable", org.openapitools.client.model.StatsDataAvailable.class);
                        classByDiscriminatorValue.put("StatsDataUnavailable", org.openapitools.client.model.StatsDataUnavailable.class);
                        classByDiscriminatorValue.put("getManagedStats_200_response_data", org.openapitools.client.model.GetManagedStats200ResponseData.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "x-linode-ref-name"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.GetTaggedObjects200ResponseDataInnerData.class, new TypeSelector<org.openapitools.client.model.GetTaggedObjects200ResponseDataInnerData>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.GetTaggedObjects200ResponseDataInnerData> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("Domain", org.openapitools.client.model.Domain.class);
                        classByDiscriminatorValue.put("Linode", org.openapitools.client.model.Linode.class);
                        classByDiscriminatorValue.put("NodeBalancer", org.openapitools.client.model.NodeBalancer.class);
                        classByDiscriminatorValue.put("Volume", org.openapitools.client.model.Volume.class);
                        classByDiscriminatorValue.put("getTaggedObjects_200_response_data_inner_data", org.openapitools.client.model.GetTaggedObjects200ResponseDataInnerData.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
                .registerTypeSelector(org.openapitools.client.model.PaymentMethodData.class, new TypeSelector<org.openapitools.client.model.PaymentMethodData>() {
                    @Override
                    public Class<? extends org.openapitools.client.model.PaymentMethodData> getClassForElement(JsonElement readElement) {
                        Map<String, Class> classByDiscriminatorValue = new HashMap<String, Class>();
                        classByDiscriminatorValue.put("CreditCardData", org.openapitools.client.model.CreditCardData.class);
                        classByDiscriminatorValue.put("GooglePayData", org.openapitools.client.model.GooglePayData.class);
                        classByDiscriminatorValue.put("PayPalData", org.openapitools.client.model.PayPalData.class);
                        classByDiscriminatorValue.put("PaymentMethod_data", org.openapitools.client.model.PaymentMethodData.class);
                        return getClassByDiscriminator(classByDiscriminatorValue,
                                getDiscriminatorValue(readElement, "type"));
                    }
          })
        ;
        GsonBuilder builder = fireBuilder.createGsonBuilder();
        return builder;
    }

    private static String getDiscriminatorValue(JsonElement readElement, String discriminatorField) {
        JsonElement element = readElement.getAsJsonObject().get(discriminatorField);
        if (null == element) {
            throw new IllegalArgumentException("missing discriminator field: <" + discriminatorField + ">");
        }
        return element.getAsString();
    }

    /**
     * Returns the Java class that implements the OpenAPI schema for the specified discriminator value.
     *
     * @param classByDiscriminatorValue The map of discriminator values to Java classes.
     * @param discriminatorValue The value of the OpenAPI discriminator in the input data.
     * @return The Java class that implements the OpenAPI schema
     */
    private static Class getClassByDiscriminator(Map classByDiscriminatorValue, String discriminatorValue) {
        Class clazz = (Class) classByDiscriminatorValue.get(discriminatorValue);
        if (null == clazz) {
            throw new IllegalArgumentException("cannot determine model class of name: <" + discriminatorValue + ">");
        }
        return clazz;
    }

    static {
        GsonBuilder gsonBuilder = createGson();
        gsonBuilder.registerTypeAdapter(Date.class, dateTypeAdapter);
        gsonBuilder.registerTypeAdapter(java.sql.Date.class, sqlDateTypeAdapter);
        gsonBuilder.registerTypeAdapter(OffsetDateTime.class, offsetDateTimeTypeAdapter);
        gsonBuilder.registerTypeAdapter(LocalDate.class, localDateTypeAdapter);
        gsonBuilder.registerTypeAdapter(byte[].class, byteArrayAdapter);
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Account.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AccountCreditCard.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AccountSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AddLinodeIPRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AllocateIPRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AttachVolumeRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.AuthorizedApp.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Backup.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BackupDisksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.BootLinodeInstanceRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CancelAccount200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CancelAccount409Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CancelAccount409ResponseErrorsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CancelAccountRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CloneDomainRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CloneLinodeInstanceRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CloneVolumeRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateEntityTransferRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateFirewallsRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateFirewallsRequestDevices.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateFirewallsRequestRules.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateImageRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateLKEClusterRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateLKEClusterRequestControlPlane.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateLinodeInstanceRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateManagedCredentialRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateNodeBalancerRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateNodeBalancerRequestConfigsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateObjectStorageBucketRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateObjectStorageObjectURL200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateObjectStorageObjectURLRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreatePayPalPayment200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreatePayment202Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreatePaymentMethodRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreatePersonalAccessTokenRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreatePromoCreditRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateServiceTransferRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateSnapshotRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateTagRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateTicketReplyRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreateVolumeRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreditCard.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.CreditCardData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Database.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseBackup.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseBackupSnapshot.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseCredentials.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseEngine.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseHosts.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseMongoDB.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseMongoDBHosts.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseMongoDBRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseMySQL.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseMySQLRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabasePostgreSQL.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabasePostgreSQLHosts.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabasePostgreSQLRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseSSL.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseType.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseTypeEngine.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseTypeEnginePrice.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseTypeEngines.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DatabaseUpdates.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Device.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Devices.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Disk.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DiskRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Domain.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DomainRecord.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EntityTransfer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EntityTransferEntities.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ErrorObject.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Event.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EventEntity.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.EventSecondaryEntity.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Firewall.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FirewallDevices.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FirewallDevicesEntity.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FirewallRuleConfig.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FirewallRuleConfigAddresses.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.FirewallRules.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetAccountDefaultResponse.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetAccountLogins200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetBackups200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetBackups200ResponseAutomaticInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetBackups200ResponseSnapshot.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetClients200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetDatabasesEngines200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetDatabasesInstances200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetDatabasesMongoDBInstanceBackups200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetDatabasesMongoDBInstances200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetDatabasesMySQLInstances200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetDatabasesPostgreSQLInstances200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetDatabasesTypes200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetDevices200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetDomainRecords200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetDomainZone200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetDomains200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetEntityTransfers200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetEvents200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetFirewallDevices200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetIPs200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetIPv6Pools200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetIPv6Ranges200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetImages200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetInvoiceItems200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetInvoices200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetKernels200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLKEClusterAPIEndpoints200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLKEClusterAPIEndpoints200ResponseDataInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLKEClusterDashboard200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLKEClusterKubeconfig200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLKEClusterNode200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLKEClusterPools200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLKEClusters200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLKEVersions200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLinodeConfigs200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLinodeDisks200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLinodeFirewalls200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLinodeIPs200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLinodeIPs200ResponseIpv4.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLinodeIPs200ResponseIpv6.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLinodeInstances200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLinodeNodeBalancers200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLinodeTransfer200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLinodeTransferByYearMonth200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLinodeTypes200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLinodeVolumes200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLongviewClients200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetLongviewSubscriptions200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetMaintenance200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetManagedContacts200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetManagedCredentials200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetManagedIssues200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetManagedLinodeSettings200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetManagedServices200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetManagedStats200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetManagedStats200ResponseData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetNodeBalancerConfigNodes200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetNodeBalancerConfigs200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetNotifications200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetObjectStorageBucketContent200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetObjectStorageBuckets200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetObjectStorageClusters200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetObjectStorageKeys200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetObjectStorageTransfer200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetPaymentMethods200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetPayments200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetPersonalAccessTokens200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetProfileApps200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetRegions200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetSSHKeys200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetServiceTransfers200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetStackScripts200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetTaggedObjects200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetTaggedObjects200ResponseDataInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetTaggedObjects200ResponseDataInnerData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetTags200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetTicketReplies200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetTickets200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetUsers200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetVLANs200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GooglePayData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Grant.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GrantsResponse.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GrantsResponseGlobal.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IPAddress.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IPAddressPrivate.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IPAddressV6LinkLocal.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IPAddressV6Slaac.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IPAddressesAssignRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IPAddressesAssignRequestAssignmentsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IPAddressesShareRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IPv6Pool.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IPv6Range.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.IPv6RangeBGP.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Image.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ImagesUploadPost200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ImagesUploadPostRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ImportDomainRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Invoice.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceItem.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.InvoiceTaxSummaryInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Kernel.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LKECluster.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LKEClusterControlPlane.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LKENodePool.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LKENodePoolAutoscaler.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LKENodePoolDisksInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LKENodePoolRequestBody.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LKENodePoolRequestBodyAutoscaler.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LKENodeStatus.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LKEVersion.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Linode.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeAlerts.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeBackups.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeBackupsSchedule.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeConfig.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeConfigHelpers.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeConfigInterface.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeSpecs.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeStats.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeStatsIo.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeStatsNetv4.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeStatsNetv6.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeType.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeTypeAddons.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeTypeAddonsBackups.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeTypeAddonsBackupsPrice.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LinodeTypePrice.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Login.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LongviewClient.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LongviewClientApps.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LongviewPlan.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LongviewSubscription.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.LongviewSubscriptionPrice.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Maintenance.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MaintenanceEntity.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ManagedContact.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ManagedContactPhone.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ManagedCredential.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ManagedIssue.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ManagedIssueEntity.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ManagedLinodeSettings.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ManagedLinodeSettingsSsh.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ManagedService.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MigrateLinodeInstanceRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.MutateLinodeInstanceRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NodeBalancer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NodeBalancerConfig.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NodeBalancerConfigNodesStatus.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NodeBalancerNode.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NodeBalancerStats.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NodeBalancerStatsData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NodeBalancerStatsDataTraffic.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NodeBalancerTransfer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Notification.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.NotificationEntity.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.OAuthClient.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ObjectStorageBucket.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ObjectStorageCluster.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ObjectStorageKey.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ObjectStorageKeyBucketAccessInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ObjectStorageObject.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ObjectStorageSSL.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ObjectStorageSSLResponse.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaginationEnvelope.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayPal.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayPalData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PayPalExecute.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Payment.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentMethod.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentMethodData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PaymentRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PersonalAccessToken.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostIPv6Range200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostIPv6RangeRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostLKEClusterRegenerateRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostProfilePhoneNumberRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostProfilePhoneNumberVerifyRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Profile.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ProfileReferrals.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Promotion.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutDatabasesMongoDBInstanceRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutDatabasesMySQLInstanceRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutDatabasesPostgreSQLInstanceRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutLKECluster200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutLKEClusterRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutLKEClusterRequestControlPlane.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutLKENodePoolRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RebootLinodeInstanceRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RebuildNodeBalancerConfigRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RebuildNodeBalancerConfigRequestAllOfNodesInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Region.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RegionResolvers.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RescueDevices.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RescueLinodeInstanceRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ResetDiskPasswordRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ResetLinodePasswordRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ResizeDiskRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ResizeLinodeInstanceRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ResizeVolumeRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.RestoreBackupRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SSHKey.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SecurityQuestion.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SecurityQuestionsGet.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SecurityQuestionsGetSecurityQuestionsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SecurityQuestionsPost.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SecurityQuestionsPostSecurityQuestionsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ServiceTransfer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ServiceTransferEntities.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.StackScript.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.StatsData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.StatsDataAvailable.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SupportTicket.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SupportTicketEntity.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SupportTicketReply.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.SupportTicketRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Tag.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TfaConfirm200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TfaConfirmRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TfaEnable200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Transfer.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.TrustedDevice.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UpdateDomainRecordRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UpdateFirewallRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UpdateIPRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UpdateLinodeIPRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UpdateManagedCredentialUsernamePasswordRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UpdateObjectStorageBucketACLRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UpdateObjectStorageBucketAccessRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UpdateObjectStorageKeyRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UpdateSSHKeyRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UpdateVolumeRequest.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.User.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.UserDefinedField.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ViewManagedSSHKey200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ViewObjectStorageBucketACL200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Vlans.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.Volume.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.WarningObject.CustomTypeAdapterFactory());
        gson = gsonBuilder.create();
    }

    /**
     * Get Gson.
     *
     * @return Gson
     */
    public static Gson getGson() {
        return gson;
    }

    /**
     * Set Gson.
     *
     * @param gson Gson
     */
    public static void setGson(Gson gson) {
        JSON.gson = gson;
    }

    public static void setLenientOnJson(boolean lenientOnJson) {
        isLenientOnJson = lenientOnJson;
    }

    /**
     * Serialize the given Java object into JSON string.
     *
     * @param obj Object
     * @return String representation of the JSON
     */
    public static String serialize(Object obj) {
        return gson.toJson(obj);
    }

    /**
     * Deserialize the given JSON string to Java object.
     *
     * @param <T>        Type
     * @param body       The JSON string
     * @param returnType The type to deserialize into
     * @return The deserialized Java object
     */
    @SuppressWarnings("unchecked")
    public static <T> T deserialize(String body, Type returnType) {
        try {
            if (isLenientOnJson) {
                JsonReader jsonReader = new JsonReader(new StringReader(body));
                // see https://google-gson.googlecode.com/svn/trunk/gson/docs/javadocs/com/google/gson/stream/JsonReader.html#setLenient(boolean)
                jsonReader.setLenient(true);
                return gson.fromJson(jsonReader, returnType);
            } else {
                return gson.fromJson(body, returnType);
            }
        } catch (JsonParseException e) {
            // Fallback processing when failed to parse JSON form response body:
            // return the response body string directly for the String return type;
            if (returnType.equals(String.class)) {
                return (T) body;
            } else {
                throw (e);
            }
        }
    }

    /**
     * Gson TypeAdapter for Byte Array type
     */
    public static class ByteArrayAdapter extends TypeAdapter<byte[]> {

        @Override
        public void write(JsonWriter out, byte[] value) throws IOException {
            if (value == null) {
                out.nullValue();
            } else {
                out.value(ByteString.of(value).base64());
            }
        }

        @Override
        public byte[] read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String bytesAsBase64 = in.nextString();
                    ByteString byteString = ByteString.decodeBase64(bytesAsBase64);
                    return byteString.toByteArray();
            }
        }
    }

    /**
     * Gson TypeAdapter for JSR310 OffsetDateTime type
     */
    public static class OffsetDateTimeTypeAdapter extends TypeAdapter<OffsetDateTime> {

        private DateTimeFormatter formatter;

        public OffsetDateTimeTypeAdapter() {
            this(DateTimeFormatter.ISO_OFFSET_DATE_TIME);
        }

        public OffsetDateTimeTypeAdapter(DateTimeFormatter formatter) {
            this.formatter = formatter;
        }

        public void setFormat(DateTimeFormatter dateFormat) {
            this.formatter = dateFormat;
        }

        @Override
        public void write(JsonWriter out, OffsetDateTime date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                out.value(formatter.format(date));
            }
        }

        @Override
        public OffsetDateTime read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String date = in.nextString();
                    if (date.endsWith("+0000")) {
                        date = date.substring(0, date.length()-5) + "Z";
                    }
                    return OffsetDateTime.parse(date, formatter);
            }
        }
    }

    /**
     * Gson TypeAdapter for JSR310 LocalDate type
     */
    public static class LocalDateTypeAdapter extends TypeAdapter<LocalDate> {

        private DateTimeFormatter formatter;

        public LocalDateTypeAdapter() {
            this(DateTimeFormatter.ISO_LOCAL_DATE);
        }

        public LocalDateTypeAdapter(DateTimeFormatter formatter) {
            this.formatter = formatter;
        }

        public void setFormat(DateTimeFormatter dateFormat) {
            this.formatter = dateFormat;
        }

        @Override
        public void write(JsonWriter out, LocalDate date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                out.value(formatter.format(date));
            }
        }

        @Override
        public LocalDate read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String date = in.nextString();
                    return LocalDate.parse(date, formatter);
            }
        }
    }

    public static void setOffsetDateTimeFormat(DateTimeFormatter dateFormat) {
        offsetDateTimeTypeAdapter.setFormat(dateFormat);
    }

    public static void setLocalDateFormat(DateTimeFormatter dateFormat) {
        localDateTypeAdapter.setFormat(dateFormat);
    }

    /**
     * Gson TypeAdapter for java.sql.Date type
     * If the dateFormat is null, a simple "yyyy-MM-dd" format will be used
     * (more efficient than SimpleDateFormat).
     */
    public static class SqlDateTypeAdapter extends TypeAdapter<java.sql.Date> {

        private DateFormat dateFormat;

        public SqlDateTypeAdapter() {}

        public SqlDateTypeAdapter(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        public void setFormat(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        @Override
        public void write(JsonWriter out, java.sql.Date date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                String value;
                if (dateFormat != null) {
                    value = dateFormat.format(date);
                } else {
                    value = date.toString();
                }
                out.value(value);
            }
        }

        @Override
        public java.sql.Date read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String date = in.nextString();
                    try {
                        if (dateFormat != null) {
                            return new java.sql.Date(dateFormat.parse(date).getTime());
                        }
                        return new java.sql.Date(ISO8601Utils.parse(date, new ParsePosition(0)).getTime());
                    } catch (ParseException e) {
                        throw new JsonParseException(e);
                    }
            }
        }
    }

    /**
     * Gson TypeAdapter for java.util.Date type
     * If the dateFormat is null, ISO8601Utils will be used.
     */
    public static class DateTypeAdapter extends TypeAdapter<Date> {

        private DateFormat dateFormat;

        public DateTypeAdapter() {}

        public DateTypeAdapter(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        public void setFormat(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        @Override
        public void write(JsonWriter out, Date date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                String value;
                if (dateFormat != null) {
                    value = dateFormat.format(date);
                } else {
                    value = ISO8601Utils.format(date, true);
                }
                out.value(value);
            }
        }

        @Override
        public Date read(JsonReader in) throws IOException {
            try {
                switch (in.peek()) {
                    case NULL:
                        in.nextNull();
                        return null;
                    default:
                        String date = in.nextString();
                        try {
                            if (dateFormat != null) {
                                return dateFormat.parse(date);
                            }
                            return ISO8601Utils.parse(date, new ParsePosition(0));
                        } catch (ParseException e) {
                            throw new JsonParseException(e);
                        }
                }
            } catch (IllegalArgumentException e) {
                throw new JsonParseException(e);
            }
        }
    }

    public static void setDateFormat(DateFormat dateFormat) {
        dateTypeAdapter.setFormat(dateFormat);
    }

    public static void setSqlDateFormat(DateFormat dateFormat) {
        sqlDateTypeAdapter.setFormat(dateFormat);
    }
}
