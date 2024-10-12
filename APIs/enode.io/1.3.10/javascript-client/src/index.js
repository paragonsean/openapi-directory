/**
 * Enode API
 * Download [OpenAPI 3.0 Specification](/OpenAPI-Enode-v1.4.0.json)  Download [Postman Collection](/Postman-Enode-v1.4.0.json)  The Enode API is designed to make smart charging applications easy to develop. We provide an abstraction layer that reduces the complexity when extracting vehicle data and sending commands to vehicles from a variety of manufacturers.  The API has a RESTful architecture and utilizes OAuth2 authorization.  We are always available to handle any issues or just answer your questions. Feel free to reach out on post@enode.io   ## Registration for API access In order to use the API you will need a `client_id` and `client_secret`. Please contact us if you are interested in using our API in production, and we will provide these credentials.  # Authorization Vehicle / hardware access via the Enode API is granted to your application by the User in a standard OAuth `Authorization Code` flow.  > The authorization scheme documented here is the recommended approach for most situations. However, it is also possible to user other OAuth flows, non-confidential clients, and temporary users. Please feel free to contact us if you have any questions about your use-case or the integration of your existing infrastructure.  ### Preparation: Configure your OAuth client  Because Enode API implements the OAuth 2.0 spec completely and without modifications, you can avoid rolling your own OAuth client implementation and instead use a well-supported and battle-tested implementation. This is strongly recommended. Information on available OAuth clients for many languages is available [here](https://oauth.net/code/)  To configure your chosen OAuth client, you will need these details: - Your `client_id` - Your `client_secret` - Authorization URL: `https://link.test.enode.io/oauth2/auth` - Token URL: `https://link.test.enode.io/oauth2/token`  ```javascript // Node.js + openid-client example const enodeIssuer = await Issuer.discover('https://link.test.enode.io'); const client = new enodeIssuer.Client({   client_id: 'xyz',   client_secret: 'shhhhh',   redirect_uris: ['http://localhost:5000/callback'],   response_types: ['code'], }); ```   ### Preparation: Obtain a client access token via OAuth Client Credentials Grant Your OAuth client will have a method for using the `OAuth 2.0 Client Credentials Grant` to obtain an access token.  ```javascript // Node.js + openid-client example const clientAccessToken = await client.grant({grant_type: \"client_credentials\"}); ```  This access token belongs to your client and is used for administrative actions, such as the next step.  This token should be cached by your server and reused until it expires, at which point your server should request a new one.    ### Step 1. Generate an Enode Link session for your User and launch the OAuth flow  When your User indicates that they want to connect their hardware to your app, your server must call [Link User](#operation/postUsersUseridLink) to generate an Enode Link session for your User. The User ID can be any string that uniquely identifies the User, but it is recommended that you use the primary key by which you identify the User within your application.  Example Request: ``` POST /users/{userId}/link HTTP/1.1 Authorization: Bearer {access_token} {   \"forceLanguage\": \"nb-NO\",   \"vendor\": \"Tesla\", } ```  Example Response: ``` {     \"linkState\": \"ZjE2MzMxMGFiYmU4MzcxOTU1ZmRjMTU5NGU2ZmE4YTU3NjViMzIwY2YzNG\", } ```  The returned linkState must be stored by your server, attached to the session of the authenticated user for which it was generated.  Your OAuth client will provide a method to construct an authorization URL for your user. That method will require these details: - Redirect URI - The URI to which your user should be redirected when the Oauth flow completes - Scope - The OAuth scope(s) you wish to request access to (see list of valid values [here](#section/Authentication/AccessTokenBearer)) - State - The value of `linkState` from the request above  To launch the OAuth flow, send your user to the authorization URL constructed by your OAuth client. This can be done in an embedded webview within a native iOS/Android app, or in the system's default browser.  ```javascript // Node.js + openid-client + express example  // Construct an OAuth authorization URL const authorizationUrl = client.authorizationUrl({   scope: \"offline_access all\",   state: linkState });  // Redirect user to authorization URL res.redirect(authorizationUrl); ```   ### Step 2. User grants consent In the Link UI webapp the user will follow 3 steps:  1. Choose their hardware from a list of supported manufacturers (EVs and charging boxes). For certain EV makes it will be necessary to also select a charge box. 2. For each selection, the user will be presented with the login screen for that particular hardware. The user must successfully log in. 3. A summary of the requested scopes will be presented to the user. The user must choose whether to grant access to your application.   ### Step 3. OAuth flow concludes with a callback When the user has completed their interactions, they will be redirected to the `Redirect URI` you provided in Step 1, with various metadata appended as query parameters.  Your OAuth client will have a method to parse and validate that metadata, and fetch the granted access and refresh tokens.  Among that metadata will be a `state` value - you must verify that it is equal to the `linkState` value persisted in Step 1, as [a countermeasure against CSRF attacks](https://tools.ietf.org/html/rfc6819#section-4.4.1.8).  ```javascript // Node.js + openid-client + express example  // Fetch linkState from user session const linkState = get(req, 'session.linkState');  // Parse relevant parameters from request URL const params = client.callbackParams(req);  // Exchange authorization code for access and refresh tokens // In this example, openid-client does the linkState validation check for us const tokenSet = await client.oauthCallback('http://localhost:5000/callback', params, {state: linkState}) ```  With the access token in hand, you can now access resources on behalf of the user.   # Errors And Problems ## OAuth Authorization Request  When the User has completed the process of allowing/denying access in Enode Link, they will be redirected to your configured redirect URI. If something has gone wrong, query parameters `error` and `error_description` will be set as documented in [Section 4.1.2.1](https://tools.ietf.org/html/rfc6749#section-4.1.2.1) of the OAuth 2.0 spec:  |error                      |error_description| |---------------------------|-----------------| |invalid_request            |The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.| |unauthorized_client        |The client is not authorized to request an authorization code using this method.| |access_denied              |The resource owner or authorization server denied the request.| |unsupported_response_type  |The authorization server does not support obtaining an authorization code using this method.| |invalid_scope              |The requested scope is invalid, unknown, or malformed.| |server_error               |The authorization server encountered an unexpected condition that prevented it from fulfilling the request.| |temporarily_unavailable    |The authorization server is currently unable to handle the request due to a temporary overloading or maintenance of the server|  Example: ``` https://website.example/oauth_callback?state=e0a86fe5&error=access_denied&error_description=The+resource+owner+or+authorization+server+denied+the+request. ```   ## Errors when accessing a User's resources  When using an `access_token` to access a User's resources, the following HTTP Status Codes in the 4XX range may be encountered:  |HTTP Status Code           |Explanation      | |---------------------------|-----------------| |400 Bad Request            |The request payload has failed schema validation / parsing |401 Unauthorized           |Authentication details are missing or invalid |403 Forbidden              |Authentication succeeded, but the authenticated user doesn't have access to the resource |404 Not Found              |A non-existent resource is requested |429 Too Many Requests      |Rate limiting by the vendor has prevented us from completing the request   In all cases, an [RFC7807 Problem Details](https://tools.ietf.org/html/rfc7807) body is returned to aid in debugging.  Example: ``` HTTP/1.1 400 Bad Request Content-Type: application/problem+json {   \"type\": \"https://docs.enode.io/problems/payload-validation-error\",   \"title\": \"Payload validation failed\",   \"detail\": \"\\\"authorizationRequest.scope\\\" is required\", } ```  
 *
 * The version of the OpenAPI document: 1.3.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ControlChargerChargingRequest from './model/ControlChargerChargingRequest';
import GetCharger200Response from './model/GetCharger200Response';
import GetCharger200ResponseChargeState from './model/GetCharger200ResponseChargeState';
import GetCharger200ResponseInformation from './model/GetCharger200ResponseInformation';
import GetHealthVendors200ResponseInner from './model/GetHealthVendors200ResponseInner';
import GetMe200Response from './model/GetMe200Response';
import GetMe200ResponseLinkedVendorsInner from './model/GetMe200ResponseLinkedVendorsInner';
import GetStatisticsCharging200ResponseInner from './model/GetStatisticsCharging200ResponseInner';
import GetStatisticsCharging200ResponseInnerKw from './model/GetStatisticsCharging200ResponseInnerKw';
import GetStatisticsCharging200ResponseInnerPrice from './model/GetStatisticsCharging200ResponseInnerPrice';
import GetVehicleChargestate200Response from './model/GetVehicleChargestate200Response';
import GetVehiclesVehicleid200Response from './model/GetVehiclesVehicleid200Response';
import GetVehiclesVehicleidInformation200Response from './model/GetVehiclesVehicleidInformation200Response';
import GetVehiclesVehicleidLocation200Response from './model/GetVehiclesVehicleidLocation200Response';
import GetVehiclesVehicleidOdometer200Response from './model/GetVehiclesVehicleidOdometer200Response';
import PostCharginglocationsRequest from './model/PostCharginglocationsRequest';
import PostUsersUseridLink200Response from './model/PostUsersUseridLink200Response';
import PostUsersUseridLinkRequest from './model/PostUsersUseridLinkRequest';
import PostVehiclesVehicleidWatchRequest from './model/PostVehiclesVehicleidWatchRequest';
import PutVehiclesVehicleidSmartchargingpolicyRequest from './model/PutVehiclesVehicleidSmartchargingpolicyRequest';
import PutWebhooksFirehoseRequest from './model/PutWebhooksFirehoseRequest';
import ChargersApi from './api/ChargersApi';
import ChargingLocationsApi from './api/ChargingLocationsApi';
import MeApi from './api/MeApi';
import ServiceHealthApi from './api/ServiceHealthApi';
import StatisticsApi from './api/StatisticsApi';
import UserManagementApi from './api/UserManagementApi';
import VehiclesApi from './api/VehiclesApi';
import WebhooksApi from './api/WebhooksApi';


/**
* Download [OpenAPI 3.0 Specification](/OpenAPI-Enode-v1.4.0.json)  Download [Postman Collection](/Postman-Enode-v1.4.0.json)  The Enode API is designed to make smart charging applications easy to develop. We provide an abstraction layer that reduces the complexity when extracting vehicle data and sending commands to vehicles from a variety of manufacturers.  The API has a RESTful architecture and utilizes OAuth2 authorization.  We are always available to handle any issues or just answer your questions. Feel free to reach out on post@enode.io   ## Registration for API access In order to use the API you will need a &#x60;client_id&#x60; and &#x60;client_secret&#x60;. Please contact us if you are interested in using our API in production, and we will provide these credentials.  # Authorization Vehicle / hardware access via the Enode API is granted to your application by the User in a standard OAuth &#x60;Authorization Code&#x60; flow.  &gt; The authorization scheme documented here is the recommended approach for most situations. However, it is also possible to user other OAuth flows, non-confidential clients, and temporary users. Please feel free to contact us if you have any questions about your use-case or the integration of your existing infrastructure.  ### Preparation: Configure your OAuth client  Because Enode API implements the OAuth 2.0 spec completely and without modifications, you can avoid rolling your own OAuth client implementation and instead use a well-supported and battle-tested implementation. This is strongly recommended. Information on available OAuth clients for many languages is available [here](https://oauth.net/code/)  To configure your chosen OAuth client, you will need these details: - Your &#x60;client_id&#x60; - Your &#x60;client_secret&#x60; - Authorization URL: &#x60;https://link.test.enode.io/oauth2/auth&#x60; - Token URL: &#x60;https://link.test.enode.io/oauth2/token&#x60;  &#x60;&#x60;&#x60;javascript // Node.js + openid-client example const enodeIssuer &#x3D; await Issuer.discover(&#39;https://link.test.enode.io&#39;); const client &#x3D; new enodeIssuer.Client({   client_id: &#39;xyz&#39;,   client_secret: &#39;shhhhh&#39;,   redirect_uris: [&#39;http://localhost:5000/callback&#39;],   response_types: [&#39;code&#39;], }); &#x60;&#x60;&#x60;   ### Preparation: Obtain a client access token via OAuth Client Credentials Grant Your OAuth client will have a method for using the &#x60;OAuth 2.0 Client Credentials Grant&#x60; to obtain an access token.  &#x60;&#x60;&#x60;javascript // Node.js + openid-client example const clientAccessToken &#x3D; await client.grant({grant_type: \&quot;client_credentials\&quot;}); &#x60;&#x60;&#x60;  This access token belongs to your client and is used for administrative actions, such as the next step.  This token should be cached by your server and reused until it expires, at which point your server should request a new one.    ### Step 1. Generate an Enode Link session for your User and launch the OAuth flow  When your User indicates that they want to connect their hardware to your app, your server must call [Link User](#operation/postUsersUseridLink) to generate an Enode Link session for your User. The User ID can be any string that uniquely identifies the User, but it is recommended that you use the primary key by which you identify the User within your application.  Example Request: &#x60;&#x60;&#x60; POST /users/{userId}/link HTTP/1.1 Authorization: Bearer {access_token} {   \&quot;forceLanguage\&quot;: \&quot;nb-NO\&quot;,   \&quot;vendor\&quot;: \&quot;Tesla\&quot;, } &#x60;&#x60;&#x60;  Example Response: &#x60;&#x60;&#x60; {     \&quot;linkState\&quot;: \&quot;ZjE2MzMxMGFiYmU4MzcxOTU1ZmRjMTU5NGU2ZmE4YTU3NjViMzIwY2YzNG\&quot;, } &#x60;&#x60;&#x60;  The returned linkState must be stored by your server, attached to the session of the authenticated user for which it was generated.  Your OAuth client will provide a method to construct an authorization URL for your user. That method will require these details: - Redirect URI - The URI to which your user should be redirected when the Oauth flow completes - Scope - The OAuth scope(s) you wish to request access to (see list of valid values [here](#section/Authentication/AccessTokenBearer)) - State - The value of &#x60;linkState&#x60; from the request above  To launch the OAuth flow, send your user to the authorization URL constructed by your OAuth client. This can be done in an embedded webview within a native iOS/Android app, or in the system&#39;s default browser.  &#x60;&#x60;&#x60;javascript // Node.js + openid-client + express example  // Construct an OAuth authorization URL const authorizationUrl &#x3D; client.authorizationUrl({   scope: \&quot;offline_access all\&quot;,   state: linkState });  // Redirect user to authorization URL res.redirect(authorizationUrl); &#x60;&#x60;&#x60;   ### Step 2. User grants consent In the Link UI webapp the user will follow 3 steps:  1. Choose their hardware from a list of supported manufacturers (EVs and charging boxes). For certain EV makes it will be necessary to also select a charge box. 2. For each selection, the user will be presented with the login screen for that particular hardware. The user must successfully log in. 3. A summary of the requested scopes will be presented to the user. The user must choose whether to grant access to your application.   ### Step 3. OAuth flow concludes with a callback When the user has completed their interactions, they will be redirected to the &#x60;Redirect URI&#x60; you provided in Step 1, with various metadata appended as query parameters.  Your OAuth client will have a method to parse and validate that metadata, and fetch the granted access and refresh tokens.  Among that metadata will be a &#x60;state&#x60; value - you must verify that it is equal to the &#x60;linkState&#x60; value persisted in Step 1, as [a countermeasure against CSRF attacks](https://tools.ietf.org/html/rfc6819#section-4.4.1.8).  &#x60;&#x60;&#x60;javascript // Node.js + openid-client + express example  // Fetch linkState from user session const linkState &#x3D; get(req, &#39;session.linkState&#39;);  // Parse relevant parameters from request URL const params &#x3D; client.callbackParams(req);  // Exchange authorization code for access and refresh tokens // In this example, openid-client does the linkState validation check for us const tokenSet &#x3D; await client.oauthCallback(&#39;http://localhost:5000/callback&#39;, params, {state: linkState}) &#x60;&#x60;&#x60;  With the access token in hand, you can now access resources on behalf of the user.   # Errors And Problems ## OAuth Authorization Request  When the User has completed the process of allowing/denying access in Enode Link, they will be redirected to your configured redirect URI. If something has gone wrong, query parameters &#x60;error&#x60; and &#x60;error_description&#x60; will be set as documented in [Section 4.1.2.1](https://tools.ietf.org/html/rfc6749#section-4.1.2.1) of the OAuth 2.0 spec:  |error                      |error_description| |---------------------------|-----------------| |invalid_request            |The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.| |unauthorized_client        |The client is not authorized to request an authorization code using this method.| |access_denied              |The resource owner or authorization server denied the request.| |unsupported_response_type  |The authorization server does not support obtaining an authorization code using this method.| |invalid_scope              |The requested scope is invalid, unknown, or malformed.| |server_error               |The authorization server encountered an unexpected condition that prevented it from fulfilling the request.| |temporarily_unavailable    |The authorization server is currently unable to handle the request due to a temporary overloading or maintenance of the server|  Example: &#x60;&#x60;&#x60; https://website.example/oauth_callback?state&#x3D;e0a86fe5&amp;error&#x3D;access_denied&amp;error_description&#x3D;The+resource+owner+or+authorization+server+denied+the+request. &#x60;&#x60;&#x60;   ## Errors when accessing a User&#39;s resources  When using an &#x60;access_token&#x60; to access a User&#39;s resources, the following HTTP Status Codes in the 4XX range may be encountered:  |HTTP Status Code           |Explanation      | |---------------------------|-----------------| |400 Bad Request            |The request payload has failed schema validation / parsing |401 Unauthorized           |Authentication details are missing or invalid |403 Forbidden              |Authentication succeeded, but the authenticated user doesn&#39;t have access to the resource |404 Not Found              |A non-existent resource is requested |429 Too Many Requests      |Rate limiting by the vendor has prevented us from completing the request   In all cases, an [RFC7807 Problem Details](https://tools.ietf.org/html/rfc7807) body is returned to aid in debugging.  Example: &#x60;&#x60;&#x60; HTTP/1.1 400 Bad Request Content-Type: application/problem+json {   \&quot;type\&quot;: \&quot;https://docs.enode.io/problems/payload-validation-error\&quot;,   \&quot;title\&quot;: \&quot;Payload validation failed\&quot;,   \&quot;detail\&quot;: \&quot;\\\&quot;authorizationRequest.scope\\\&quot; is required\&quot;, } &#x60;&#x60;&#x60;  .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var EnodeApi = require('index'); // See note below*.
* var xxxSvc = new EnodeApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new EnodeApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new EnodeApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new EnodeApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.3.10
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ControlChargerChargingRequest model constructor.
     * @property {module:model/ControlChargerChargingRequest}
     */
    ControlChargerChargingRequest,

    /**
     * The GetCharger200Response model constructor.
     * @property {module:model/GetCharger200Response}
     */
    GetCharger200Response,

    /**
     * The GetCharger200ResponseChargeState model constructor.
     * @property {module:model/GetCharger200ResponseChargeState}
     */
    GetCharger200ResponseChargeState,

    /**
     * The GetCharger200ResponseInformation model constructor.
     * @property {module:model/GetCharger200ResponseInformation}
     */
    GetCharger200ResponseInformation,

    /**
     * The GetHealthVendors200ResponseInner model constructor.
     * @property {module:model/GetHealthVendors200ResponseInner}
     */
    GetHealthVendors200ResponseInner,

    /**
     * The GetMe200Response model constructor.
     * @property {module:model/GetMe200Response}
     */
    GetMe200Response,

    /**
     * The GetMe200ResponseLinkedVendorsInner model constructor.
     * @property {module:model/GetMe200ResponseLinkedVendorsInner}
     */
    GetMe200ResponseLinkedVendorsInner,

    /**
     * The GetStatisticsCharging200ResponseInner model constructor.
     * @property {module:model/GetStatisticsCharging200ResponseInner}
     */
    GetStatisticsCharging200ResponseInner,

    /**
     * The GetStatisticsCharging200ResponseInnerKw model constructor.
     * @property {module:model/GetStatisticsCharging200ResponseInnerKw}
     */
    GetStatisticsCharging200ResponseInnerKw,

    /**
     * The GetStatisticsCharging200ResponseInnerPrice model constructor.
     * @property {module:model/GetStatisticsCharging200ResponseInnerPrice}
     */
    GetStatisticsCharging200ResponseInnerPrice,

    /**
     * The GetVehicleChargestate200Response model constructor.
     * @property {module:model/GetVehicleChargestate200Response}
     */
    GetVehicleChargestate200Response,

    /**
     * The GetVehiclesVehicleid200Response model constructor.
     * @property {module:model/GetVehiclesVehicleid200Response}
     */
    GetVehiclesVehicleid200Response,

    /**
     * The GetVehiclesVehicleidInformation200Response model constructor.
     * @property {module:model/GetVehiclesVehicleidInformation200Response}
     */
    GetVehiclesVehicleidInformation200Response,

    /**
     * The GetVehiclesVehicleidLocation200Response model constructor.
     * @property {module:model/GetVehiclesVehicleidLocation200Response}
     */
    GetVehiclesVehicleidLocation200Response,

    /**
     * The GetVehiclesVehicleidOdometer200Response model constructor.
     * @property {module:model/GetVehiclesVehicleidOdometer200Response}
     */
    GetVehiclesVehicleidOdometer200Response,

    /**
     * The PostCharginglocationsRequest model constructor.
     * @property {module:model/PostCharginglocationsRequest}
     */
    PostCharginglocationsRequest,

    /**
     * The PostUsersUseridLink200Response model constructor.
     * @property {module:model/PostUsersUseridLink200Response}
     */
    PostUsersUseridLink200Response,

    /**
     * The PostUsersUseridLinkRequest model constructor.
     * @property {module:model/PostUsersUseridLinkRequest}
     */
    PostUsersUseridLinkRequest,

    /**
     * The PostVehiclesVehicleidWatchRequest model constructor.
     * @property {module:model/PostVehiclesVehicleidWatchRequest}
     */
    PostVehiclesVehicleidWatchRequest,

    /**
     * The PutVehiclesVehicleidSmartchargingpolicyRequest model constructor.
     * @property {module:model/PutVehiclesVehicleidSmartchargingpolicyRequest}
     */
    PutVehiclesVehicleidSmartchargingpolicyRequest,

    /**
     * The PutWebhooksFirehoseRequest model constructor.
     * @property {module:model/PutWebhooksFirehoseRequest}
     */
    PutWebhooksFirehoseRequest,

    /**
    * The ChargersApi service constructor.
    * @property {module:api/ChargersApi}
    */
    ChargersApi,

    /**
    * The ChargingLocationsApi service constructor.
    * @property {module:api/ChargingLocationsApi}
    */
    ChargingLocationsApi,

    /**
    * The MeApi service constructor.
    * @property {module:api/MeApi}
    */
    MeApi,

    /**
    * The ServiceHealthApi service constructor.
    * @property {module:api/ServiceHealthApi}
    */
    ServiceHealthApi,

    /**
    * The StatisticsApi service constructor.
    * @property {module:api/StatisticsApi}
    */
    StatisticsApi,

    /**
    * The UserManagementApi service constructor.
    * @property {module:api/UserManagementApi}
    */
    UserManagementApi,

    /**
    * The VehiclesApi service constructor.
    * @property {module:api/VehiclesApi}
    */
    VehiclesApi,

    /**
    * The WebhooksApi service constructor.
    * @property {module:api/WebhooksApi}
    */
    WebhooksApi
};
