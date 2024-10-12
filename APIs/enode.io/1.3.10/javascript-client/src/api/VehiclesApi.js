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


import ApiClient from "../ApiClient";
import GetVehicleChargestate200Response from '../model/GetVehicleChargestate200Response';
import GetVehiclesVehicleid200Response from '../model/GetVehiclesVehicleid200Response';
import GetVehiclesVehicleidInformation200Response from '../model/GetVehiclesVehicleidInformation200Response';
import GetVehiclesVehicleidLocation200Response from '../model/GetVehiclesVehicleidLocation200Response';
import GetVehiclesVehicleidOdometer200Response from '../model/GetVehiclesVehicleidOdometer200Response';
import PostVehiclesVehicleidWatchRequest from '../model/PostVehiclesVehicleidWatchRequest';
import PutVehiclesVehicleidSmartchargingpolicyRequest from '../model/PutVehiclesVehicleidSmartchargingpolicyRequest';

/**
* Vehicles service.
* @module api/VehiclesApi
* @version 1.3.10
*/
export default class VehiclesApi {

    /**
    * Constructs a new VehiclesApi. 
    * @alias module:api/VehiclesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getVehicleChargestate operation.
     * @callback module:api/VehiclesApi~getVehicleChargestateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetVehicleChargestate200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Vehicle Charge State
     * @param {module:api/VehiclesApi~getVehicleChargestateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetVehicleChargestate200Response}
     */
    getVehicleChargestate(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserAccessToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetVehicleChargestate200Response;
      return this.apiClient.callApi(
        '/vehicles/{vehicleId}/charge-state', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVehicles operation.
     * @callback module:api/VehiclesApi~getVehiclesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List Vehicles
     * @param {Object} opts Optional parameters
     * @param {Array.<Object>} [field] An optional array of Vehicle fields that should be included in the response, for example: `?field[]=information&field[]=location`   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request.
     * @param {module:api/VehiclesApi~getVehiclesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getVehicles(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'field[]': this.apiClient.buildCollectionParam(opts['field'], 'multi')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserAccessToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Object];
      return this.apiClient.callApi(
        '/vehicles', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVehiclesVehicleid operation.
     * @callback module:api/VehiclesApi~getVehiclesVehicleidCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetVehiclesVehicleid200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Vehicle
     * @param {String} vehicleId ID of the Vehicle
     * @param {Object} opts Optional parameters
     * @param {Array.<module:model/String>} [field] An optional array of Vehicle fields that should be included in the response, for example: `?field[]=information&field[]=location`   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request.
     * @param {module:api/VehiclesApi~getVehiclesVehicleidCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetVehiclesVehicleid200Response}
     */
    getVehiclesVehicleid(vehicleId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'vehicleId' is set
      if (vehicleId === undefined || vehicleId === null) {
        throw new Error("Missing the required parameter 'vehicleId' when calling getVehiclesVehicleid");
      }

      let pathParams = {
        'vehicleId': vehicleId
      };
      let queryParams = {
        'field[]': this.apiClient.buildCollectionParam(opts['field'], 'multi')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserAccessToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetVehiclesVehicleid200Response;
      return this.apiClient.callApi(
        '/vehicles/{vehicleId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVehiclesVehicleidInformation operation.
     * @callback module:api/VehiclesApi~getVehiclesVehicleidInformationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetVehiclesVehicleidInformation200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Vehicle Information
     * @param {module:api/VehiclesApi~getVehiclesVehicleidInformationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetVehiclesVehicleidInformation200Response}
     */
    getVehiclesVehicleidInformation(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserAccessToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetVehiclesVehicleidInformation200Response;
      return this.apiClient.callApi(
        '/vehicles/{vehicleId}/information', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVehiclesVehicleidLocation operation.
     * @callback module:api/VehiclesApi~getVehiclesVehicleidLocationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetVehiclesVehicleidLocation200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Vehicle Location
     * @param {module:api/VehiclesApi~getVehiclesVehicleidLocationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetVehiclesVehicleidLocation200Response}
     */
    getVehiclesVehicleidLocation(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserAccessToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetVehiclesVehicleidLocation200Response;
      return this.apiClient.callApi(
        '/vehicles/{vehicleId}/location', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVehiclesVehicleidOdometer operation.
     * @callback module:api/VehiclesApi~getVehiclesVehicleidOdometerCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetVehiclesVehicleidOdometer200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Vehicle Odometer
     * @param {module:api/VehiclesApi~getVehiclesVehicleidOdometerCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetVehiclesVehicleidOdometer200Response}
     */
    getVehiclesVehicleidOdometer(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserAccessToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetVehiclesVehicleidOdometer200Response;
      return this.apiClient.callApi(
        '/vehicles/{vehicleId}/odometer', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVehiclesVehicleidSmartchargingpolicy operation.
     * @callback module:api/VehiclesApi~getVehiclesVehicleidSmartchargingpolicyCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Vehicle Smart Charging Policy
     * @param {module:api/VehiclesApi~getVehiclesVehicleidSmartchargingpolicyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getVehiclesVehicleidSmartchargingpolicy(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserAccessToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/vehicles/{vehicleId}/smart-charging-policy', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postVehiclesVehicleidCharging operation.
     * @callback module:api/VehiclesApi~postVehiclesVehicleidChargingCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Start / Stop Charging
     * Instruct the vehicle to start or stop charging.   #### Precedence over smart charging If the vehicle is at a charging location where smart charging is activated: - a request to `start` charging will override smart charging and charging will stay on until fully charged.  - a request to `stop` charging will override smart charging and charging will be kept off for the duration of the current smart charging cycle.  The smart charging settings are not altered by these actions.
     * @param {module:api/VehiclesApi~postVehiclesVehicleidChargingCallback} callback The callback function, accepting three arguments: error, data, response
     */
    postVehiclesVehicleidCharging(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserAccessToken'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/vehicles/{vehicleId}/charging', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postVehiclesVehicleidWatch operation.
     * @callback module:api/VehiclesApi~postVehiclesVehicleidWatchCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Start Watching Vehicle
     * Temporarily triggers high-rate updates of the vehicle's properties, and this state expires automatically. This gives you a way to tell us that user may be interacting with your application and are expecting as-fast-as-possible updates on the status of their vehicle in your UI.  Any data changes resulting from this high-rate updating are reflected everywhere, whether you pull data from the `Vehicles` endpoint, or recieve it via the [Firehose Webhook](#tag/Webhooks)  The specifics of the expiration times, watch behaviors, and change thresholds are tuned by us to make sure that they work as expected, without causing undue interruption to the vehicle. For many vendors, it is not appropriate to let the high-rate monitoring last indefinitely, as it will keep systems within the car awake that should be allowed to fall into low-power/standby modes. 
     * @param {String} vehicleId ID of the Vehicle
     * @param {Object} opts Optional parameters
     * @param {module:model/PostVehiclesVehicleidWatchRequest} [postVehiclesVehicleidWatchRequest] 
     * @param {module:api/VehiclesApi~postVehiclesVehicleidWatchCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postVehiclesVehicleidWatch(vehicleId, opts, callback) {
      opts = opts || {};
      let postBody = opts['postVehiclesVehicleidWatchRequest'];
      // verify the required parameter 'vehicleId' is set
      if (vehicleId === undefined || vehicleId === null) {
        throw new Error("Missing the required parameter 'vehicleId' when calling postVehiclesVehicleidWatch");
      }

      let pathParams = {
        'vehicleId': vehicleId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserAccessToken'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/vehicles/{vehicleId}/watch', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putVehiclesVehicleidSmartchargingpolicy operation.
     * @callback module:api/VehiclesApi~putVehiclesVehicleidSmartchargingpolicyCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update Vehicle Smart Charging Policy
     * Updates the Smart Charging settings for a vehicle
     * @param {String} vehicleId ID of the Vehicle
     * @param {Object} opts Optional parameters
     * @param {module:model/PutVehiclesVehicleidSmartchargingpolicyRequest} [putVehiclesVehicleidSmartchargingpolicyRequest] 
     * @param {module:api/VehiclesApi~putVehiclesVehicleidSmartchargingpolicyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    putVehiclesVehicleidSmartchargingpolicy(vehicleId, opts, callback) {
      opts = opts || {};
      let postBody = opts['putVehiclesVehicleidSmartchargingpolicyRequest'];
      // verify the required parameter 'vehicleId' is set
      if (vehicleId === undefined || vehicleId === null) {
        throw new Error("Missing the required parameter 'vehicleId' when calling putVehiclesVehicleidSmartchargingpolicy");
      }

      let pathParams = {
        'vehicleId': vehicleId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserAccessToken'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/vehicles/{vehicleId}/smart-charging-policy', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
