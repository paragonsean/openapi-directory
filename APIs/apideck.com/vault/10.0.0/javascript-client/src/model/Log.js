/**
 * Vault API
 * Welcome to the Vault API 👋  When you're looking to connect to an API, the first step is authentication.  Vault helps you handle OAuth flows, store API keys, and refresh access tokens from users (called consumers in Apideck).  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Get Started  To use the Apideck APIs, you need to sign up for free at [https://app.apideck.com/signup](). Follow the steps below to get started.  - [Create a free account.](https://app.apideck.com/signup) - Go to the [Dashboard](https://app.apideck.com/unify/unified-apis/dashboard). - Get your API key and the application ID. - Select and configure the integrations you want to make available to your users. Through the Unify dashboard, you can configure which connectors you want to support as integrations. - Retrieve the client_id and client_secret for the integration you want to activate (Only needed for OAuth integrations). - Soon, you can skip the previous step and use the Apideck sandbox credentials to get you started instead (upcoming) - Register the redirect URI for the example app (https://unify.apideck.com/vault/callback) in the list of redirect URIs under your app's settings - Use the [publishing guides](/app-listing-requirements) to get your integration listed across app marketplaces.  ### Hosted Vault  Hosted Vault (vault.apideck.com) is a no-code solution, so you don't need to build your own UI to handle the integration settings and authentication.  ![Hosted Vault - Integrations portal](https://github.com/apideck-samples/integration-settings/raw/master/public/img/vault.png)  Behind the scenes, Hosted Vault implements the Vault API endpoints and handles the following features for your customers:  - Add a connection - Handle the OAuth flow - Configure connection settings per integration - Manage connections - Discover and propose integration options - Search for integrations (upcoming) - Give integration suggestions based on provided metadata (email or website) when creating the session (upcoming)  To use Hosted Vault, you will need to first [**create a session**](https://developers.apideck.com/apis/vault/reference#operation/sessionsCreate). This can be achieved by making a POST request to the Vault API to create a valid session for a user, hereafter referred to as the consumer ID.  Example using curl:  ``` curl -X POST https://unify.apideck.com/vault/sessions     -H \"Content-Type: application/json\"     -H \"Authorization: Bearer <your-api-key>\"     -H \"X-APIDECK-CONSUMER-ID: <consumer-id>\"     -H \"X-APIDECK-APP-ID: <application-id>\"     -d '{\"consumer_metadata\": { \"account_name\" : \"Sample\", \"user_name\": \"Sand Box\", \"email\": \"sand@box.com\", \"image\": \"https://unavatar.now.sh/jake\" }, \"theme\": { \"vault_name\": \"Intercom\", \"primary_color\": \"#286efa\", \"sidepanel_background_color\": \"#286efa\",\"sidepanel_text_color\": \"#FFFFFF\", \"favicon\": \"https://res.cloudinary.com/apideck/icons/intercom\" }}' ```  ### Vault API  _Beware, this is strategy takes more time to implement in comparison to Hosted Vault._  If you are building your integration settings UI manually, you can call the Vault API directly.  The Vault API is for those who want to completely white label the in-app integrations overview and authentication experience. All the available endpoints are listed below.  Through the API, your customers authenticate directly in your app, where Vault will still take care of redirecting to the auth provider and back to your app.  If you're already storing access tokens, we will help you migrate through our Vault Migration API (upcoming).  ## Domain model  At its core, a domain model creates a web of interconnected entities.  Our domain model contains five main entity types: Consumer (user, account, team, machine), Application, Connector, Integration, and Connection.  ## Connection state  The connection state is computed based on the connection flow below.  ![](https://developers.apideck.com/api-references/vault/connection-flow.png)  More information about the connection state can be found in the [Connection state](https://developers.apideck.com/guides/connection-states) guide.  ## Unify and Proxy integration  The only thing you need to use the Unify APIs and Proxy is the consumer id; thereafter, Vault will do the look-up in the background to handle the token injection before performing the API call(s).  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-app-id      | String  | Yes      | The id of your Unify application. Available at https://app.apideck.com/api-keys. | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes. |  ## Guides  - [Get started with Apideck](https://developers.apideck.com/getting-started) - [Get started with Vault](https://developers.apideck.com/guides/vault) - [Authorize connection via Vault](https://developers.apideck.com/guides/authorize-connections) - [Vault connection status](https://developers.apideck.com/guides/connection-states) - [How to build an integrations UI with Vault](https://github.com/apideck-samples/integration-settings)   ## FAQ  **What purpose does Vault serve? Can I just handle the authentication and access token myself?** You can store everything yourself, but that defeats the purpose of using Apideck Unify. Handling tokens for multiple providers can quickly become very complex.  ### Is my data secure?  Vault employs data minimization, therefore only requesting the minimum amount of scopes needed to perform an API request.  ### How do I migrate existing data?  Using our migration API, you can migrate the access tokens and accounts to Apideck Vault.  ### Can I use Vault in combination with existing integrations?  Yes, you can. The flexibility of Unify allows you to quickly the use cases you need while keeping a gradual migration path based on your timeline and requirements.  ### How does Vault work for Apideck Ecosystem customers?  Once logged in, pick your ecosystem; on the left-hand side of the screen, you'll have the option to create an application underneath the Unify section.  ### How to integrate Apideck Vault  This section covers everything you need to know to authenticate your customers through Vault. Vault provides **three auth strategies** to use API tokens from your customers:  - Vault API - Hosted Vault - Vault Widget (JS, React, Vue)  You can also opt to bypass Vault and still take care of authentication flows yourself. Make sure to put the right safeguards in place to protect your customers' tokens and other sensitive data.  ### What auth types does Vault support?  We support all the common authentication types, including: API keys, OAuth, Basic auth, and more.  #### API keys  For Services supporting the API key strategy, you can use Hosted Vault will need to provide an in-app form where users can configure their API keys provided by the integration service.  #### OAuth 2.0  ##### Authorization Code Grant Type Flow  Vault handles the complete Authorization Code Grant Type Flow for you. This flow only supports browser-based (passive) authentication because most identity providers don't allow entering a username and password to be entered into applications that they don't own.  Certain connectors require an OAuth redirect authentication flow, where the end-user is redirected to the provider's website or mobile app to authenticate.  This is being handled by the `/authorize` endpoint.  #### Basic auth  Basic authentication is a simple authentication scheme built into the HTTP protocol. The required fields to complete basic auth are handled by Hosted Vault or by updating the connection through the Vault API below.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import LogOperation from './LogOperation';
import LogService from './LogService';

/**
 * The Log model module.
 * @module model/Log
 * @version 10.0.0
 */
class Log {
    /**
     * Constructs a new <code>Log</code>.
     * @alias module:model/Log
     * @param apiStyle {String} Indicates if the request was made via REST or Graphql endpoint.
     * @param baseUrl {String} The Apideck base URL the request was made to.
     * @param childRequest {Boolean} Indicates whether or not this is a child or parent request.
     * @param consumerId {String} The consumer Id associated with the request.
     * @param duration {Number} The entire execution time in milliseconds it took to call the Apideck service provider.
     * @param execution {Number} The entire execution time in milliseconds it took to make the request.
     * @param hasChildren {Boolean} When request is a parent request, this indicates if there are child requests associated.
     * @param httpMethod {String} HTTP Method of request.
     * @param id {String} UUID acting as Request Identifier.
     * @param latency {Number} Latency added by making this request via Unified Api.
     * @param operation {module:model/LogOperation} 
     * @param parentId {String} When request is a child request, this UUID indicates it's parent request.
     * @param path {String} The path component of the URI the request was made to.
     * @param sandbox {Boolean} Indicates whether the request was made using Apidecks sandbox credentials or not.
     * @param service {module:model/LogService} 
     * @param statusCode {Number} HTTP Status code that was returned.
     * @param success {Boolean} Whether or not the request was successful.
     * @param timestamp {String} ISO Date and time when the request was made.
     * @param unifiedApi {module:model/Log.UnifiedApiEnum} Which Unified Api request was made to.
     */
    constructor(apiStyle, baseUrl, childRequest, consumerId, duration, execution, hasChildren, httpMethod, id, latency, operation, parentId, path, sandbox, service, statusCode, success, timestamp, unifiedApi) { 
        
        Log.initialize(this, apiStyle, baseUrl, childRequest, consumerId, duration, execution, hasChildren, httpMethod, id, latency, operation, parentId, path, sandbox, service, statusCode, success, timestamp, unifiedApi);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, apiStyle, baseUrl, childRequest, consumerId, duration, execution, hasChildren, httpMethod, id, latency, operation, parentId, path, sandbox, service, statusCode, success, timestamp, unifiedApi) { 
        obj['api_style'] = apiStyle;
        obj['base_url'] = baseUrl;
        obj['child_request'] = childRequest;
        obj['consumer_id'] = consumerId;
        obj['duration'] = duration;
        obj['execution'] = execution;
        obj['has_children'] = hasChildren;
        obj['http_method'] = httpMethod;
        obj['id'] = id;
        obj['latency'] = latency;
        obj['operation'] = operation;
        obj['parent_id'] = parentId;
        obj['path'] = path;
        obj['sandbox'] = sandbox;
        obj['service'] = service;
        obj['status_code'] = statusCode;
        obj['success'] = success;
        obj['timestamp'] = timestamp;
        obj['unified_api'] = unifiedApi;
    }

    /**
     * Constructs a <code>Log</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Log} obj Optional instance to populate.
     * @return {module:model/Log} The populated <code>Log</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Log();

            if (data.hasOwnProperty('api_style')) {
                obj['api_style'] = ApiClient.convertToType(data['api_style'], 'String');
            }
            if (data.hasOwnProperty('base_url')) {
                obj['base_url'] = ApiClient.convertToType(data['base_url'], 'String');
            }
            if (data.hasOwnProperty('child_request')) {
                obj['child_request'] = ApiClient.convertToType(data['child_request'], 'Boolean');
            }
            if (data.hasOwnProperty('consumer_id')) {
                obj['consumer_id'] = ApiClient.convertToType(data['consumer_id'], 'String');
            }
            if (data.hasOwnProperty('duration')) {
                obj['duration'] = ApiClient.convertToType(data['duration'], 'Number');
            }
            if (data.hasOwnProperty('error_message')) {
                obj['error_message'] = ApiClient.convertToType(data['error_message'], 'String');
            }
            if (data.hasOwnProperty('execution')) {
                obj['execution'] = ApiClient.convertToType(data['execution'], 'Number');
            }
            if (data.hasOwnProperty('has_children')) {
                obj['has_children'] = ApiClient.convertToType(data['has_children'], 'Boolean');
            }
            if (data.hasOwnProperty('http_method')) {
                obj['http_method'] = ApiClient.convertToType(data['http_method'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('latency')) {
                obj['latency'] = ApiClient.convertToType(data['latency'], 'Number');
            }
            if (data.hasOwnProperty('operation')) {
                obj['operation'] = LogOperation.constructFromObject(data['operation']);
            }
            if (data.hasOwnProperty('parent_id')) {
                obj['parent_id'] = ApiClient.convertToType(data['parent_id'], 'String');
            }
            if (data.hasOwnProperty('path')) {
                obj['path'] = ApiClient.convertToType(data['path'], 'String');
            }
            if (data.hasOwnProperty('sandbox')) {
                obj['sandbox'] = ApiClient.convertToType(data['sandbox'], 'Boolean');
            }
            if (data.hasOwnProperty('service')) {
                obj['service'] = LogService.constructFromObject(data['service']);
            }
            if (data.hasOwnProperty('source_ip')) {
                obj['source_ip'] = ApiClient.convertToType(data['source_ip'], 'String');
            }
            if (data.hasOwnProperty('status_code')) {
                obj['status_code'] = ApiClient.convertToType(data['status_code'], 'Number');
            }
            if (data.hasOwnProperty('success')) {
                obj['success'] = ApiClient.convertToType(data['success'], 'Boolean');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'String');
            }
            if (data.hasOwnProperty('unified_api')) {
                obj['unified_api'] = ApiClient.convertToType(data['unified_api'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Log</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Log</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Log.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['api_style'] && !(typeof data['api_style'] === 'string' || data['api_style'] instanceof String)) {
            throw new Error("Expected the field `api_style` to be a primitive type in the JSON string but got " + data['api_style']);
        }
        // ensure the json data is a string
        if (data['base_url'] && !(typeof data['base_url'] === 'string' || data['base_url'] instanceof String)) {
            throw new Error("Expected the field `base_url` to be a primitive type in the JSON string but got " + data['base_url']);
        }
        // ensure the json data is a string
        if (data['consumer_id'] && !(typeof data['consumer_id'] === 'string' || data['consumer_id'] instanceof String)) {
            throw new Error("Expected the field `consumer_id` to be a primitive type in the JSON string but got " + data['consumer_id']);
        }
        // ensure the json data is a string
        if (data['error_message'] && !(typeof data['error_message'] === 'string' || data['error_message'] instanceof String)) {
            throw new Error("Expected the field `error_message` to be a primitive type in the JSON string but got " + data['error_message']);
        }
        // ensure the json data is a string
        if (data['http_method'] && !(typeof data['http_method'] === 'string' || data['http_method'] instanceof String)) {
            throw new Error("Expected the field `http_method` to be a primitive type in the JSON string but got " + data['http_method']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `operation`
        if (data['operation']) { // data not null
          LogOperation.validateJSON(data['operation']);
        }
        // ensure the json data is a string
        if (data['parent_id'] && !(typeof data['parent_id'] === 'string' || data['parent_id'] instanceof String)) {
            throw new Error("Expected the field `parent_id` to be a primitive type in the JSON string but got " + data['parent_id']);
        }
        // ensure the json data is a string
        if (data['path'] && !(typeof data['path'] === 'string' || data['path'] instanceof String)) {
            throw new Error("Expected the field `path` to be a primitive type in the JSON string but got " + data['path']);
        }
        // validate the optional field `service`
        if (data['service']) { // data not null
          LogService.validateJSON(data['service']);
        }
        // ensure the json data is a string
        if (data['source_ip'] && !(typeof data['source_ip'] === 'string' || data['source_ip'] instanceof String)) {
            throw new Error("Expected the field `source_ip` to be a primitive type in the JSON string but got " + data['source_ip']);
        }
        // ensure the json data is a string
        if (data['timestamp'] && !(typeof data['timestamp'] === 'string' || data['timestamp'] instanceof String)) {
            throw new Error("Expected the field `timestamp` to be a primitive type in the JSON string but got " + data['timestamp']);
        }
        // ensure the json data is a string
        if (data['unified_api'] && !(typeof data['unified_api'] === 'string' || data['unified_api'] instanceof String)) {
            throw new Error("Expected the field `unified_api` to be a primitive type in the JSON string but got " + data['unified_api']);
        }

        return true;
    }


}

Log.RequiredProperties = ["api_style", "base_url", "child_request", "consumer_id", "duration", "execution", "has_children", "http_method", "id", "latency", "operation", "parent_id", "path", "sandbox", "service", "status_code", "success", "timestamp", "unified_api"];

/**
 * Indicates if the request was made via REST or Graphql endpoint.
 * @member {String} api_style
 */
Log.prototype['api_style'] = undefined;

/**
 * The Apideck base URL the request was made to.
 * @member {String} base_url
 */
Log.prototype['base_url'] = undefined;

/**
 * Indicates whether or not this is a child or parent request.
 * @member {Boolean} child_request
 */
Log.prototype['child_request'] = undefined;

/**
 * The consumer Id associated with the request.
 * @member {String} consumer_id
 */
Log.prototype['consumer_id'] = undefined;

/**
 * The entire execution time in milliseconds it took to call the Apideck service provider.
 * @member {Number} duration
 */
Log.prototype['duration'] = undefined;

/**
 * If error occurred, this is brief explanation
 * @member {String} error_message
 */
Log.prototype['error_message'] = undefined;

/**
 * The entire execution time in milliseconds it took to make the request.
 * @member {Number} execution
 */
Log.prototype['execution'] = undefined;

/**
 * When request is a parent request, this indicates if there are child requests associated.
 * @member {Boolean} has_children
 */
Log.prototype['has_children'] = undefined;

/**
 * HTTP Method of request.
 * @member {String} http_method
 */
Log.prototype['http_method'] = undefined;

/**
 * UUID acting as Request Identifier.
 * @member {String} id
 */
Log.prototype['id'] = undefined;

/**
 * Latency added by making this request via Unified Api.
 * @member {Number} latency
 */
Log.prototype['latency'] = undefined;

/**
 * @member {module:model/LogOperation} operation
 */
Log.prototype['operation'] = undefined;

/**
 * When request is a child request, this UUID indicates it's parent request.
 * @member {String} parent_id
 */
Log.prototype['parent_id'] = undefined;

/**
 * The path component of the URI the request was made to.
 * @member {String} path
 */
Log.prototype['path'] = undefined;

/**
 * Indicates whether the request was made using Apidecks sandbox credentials or not.
 * @member {Boolean} sandbox
 */
Log.prototype['sandbox'] = undefined;

/**
 * @member {module:model/LogService} service
 */
Log.prototype['service'] = undefined;

/**
 * The IP address of the source of the request.
 * @member {String} source_ip
 */
Log.prototype['source_ip'] = undefined;

/**
 * HTTP Status code that was returned.
 * @member {Number} status_code
 */
Log.prototype['status_code'] = undefined;

/**
 * Whether or not the request was successful.
 * @member {Boolean} success
 */
Log.prototype['success'] = undefined;

/**
 * ISO Date and time when the request was made.
 * @member {String} timestamp
 */
Log.prototype['timestamp'] = undefined;

/**
 * Which Unified Api request was made to.
 * @member {module:model/Log.UnifiedApiEnum} unified_api
 */
Log.prototype['unified_api'] = undefined;





/**
 * Allowed values for the <code>unified_api</code> property.
 * @enum {String}
 * @readonly
 */
Log['UnifiedApiEnum'] = {

    /**
     * value: "crm"
     * @const
     */
    "crm": "crm",

    /**
     * value: "lead"
     * @const
     */
    "lead": "lead",

    /**
     * value: "proxy"
     * @const
     */
    "proxy": "proxy",

    /**
     * value: "vault"
     * @const
     */
    "vault": "vault",

    /**
     * value: "accounting"
     * @const
     */
    "accounting": "accounting",

    /**
     * value: "hris"
     * @const
     */
    "hris": "hris",

    /**
     * value: "ats"
     * @const
     */
    "ats": "ats",

    /**
     * value: "ecommerce"
     * @const
     */
    "ecommerce": "ecommerce",

    /**
     * value: "issue-tracking"
     * @const
     */
    "issue-tracking": "issue-tracking",

    /**
     * value: "pos"
     * @const
     */
    "pos": "pos",

    /**
     * value: "file-storage"
     * @const
     */
    "file-storage": "file-storage",

    /**
     * value: "sms"
     * @const
     */
    "sms": "sms"
};



export default Log;

