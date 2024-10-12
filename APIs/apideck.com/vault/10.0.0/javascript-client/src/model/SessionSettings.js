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
import UnifiedApiId from './UnifiedApiId';

/**
 * The SessionSettings model module.
 * @module model/SessionSettings
 * @version 10.0.0
 */
class SessionSettings {
    /**
     * Constructs a new <code>SessionSettings</code>.
     * Settings to change the way the Vault is displayed.
     * @alias module:model/SessionSettings
     */
    constructor() { 
        
        SessionSettings.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['auto_redirect'] = false;
        obj['hide_guides'] = false;
        obj['hide_resource_settings'] = false;
        obj['isolation_mode'] = false;
        obj['sandbox_mode'] = false;
        obj['session_length'] = '1h';
        obj['show_logs'] = true;
        obj['show_sidebar'] = true;
        obj['show_suggestions'] = false;
    }

    /**
     * Constructs a <code>SessionSettings</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SessionSettings} obj Optional instance to populate.
     * @return {module:model/SessionSettings} The populated <code>SessionSettings</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SessionSettings();

            if (data.hasOwnProperty('allow_actions')) {
                obj['allow_actions'] = ApiClient.convertToType(data['allow_actions'], ['String']);
            }
            if (data.hasOwnProperty('auto_redirect')) {
                obj['auto_redirect'] = ApiClient.convertToType(data['auto_redirect'], 'Boolean');
            }
            if (data.hasOwnProperty('hide_guides')) {
                obj['hide_guides'] = ApiClient.convertToType(data['hide_guides'], 'Boolean');
            }
            if (data.hasOwnProperty('hide_resource_settings')) {
                obj['hide_resource_settings'] = ApiClient.convertToType(data['hide_resource_settings'], 'Boolean');
            }
            if (data.hasOwnProperty('isolation_mode')) {
                obj['isolation_mode'] = ApiClient.convertToType(data['isolation_mode'], 'Boolean');
            }
            if (data.hasOwnProperty('sandbox_mode')) {
                obj['sandbox_mode'] = ApiClient.convertToType(data['sandbox_mode'], 'Boolean');
            }
            if (data.hasOwnProperty('session_length')) {
                obj['session_length'] = ApiClient.convertToType(data['session_length'], 'String');
            }
            if (data.hasOwnProperty('show_logs')) {
                obj['show_logs'] = ApiClient.convertToType(data['show_logs'], 'Boolean');
            }
            if (data.hasOwnProperty('show_sidebar')) {
                obj['show_sidebar'] = ApiClient.convertToType(data['show_sidebar'], 'Boolean');
            }
            if (data.hasOwnProperty('show_suggestions')) {
                obj['show_suggestions'] = ApiClient.convertToType(data['show_suggestions'], 'Boolean');
            }
            if (data.hasOwnProperty('unified_apis')) {
                obj['unified_apis'] = ApiClient.convertToType(data['unified_apis'], [UnifiedApiId]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SessionSettings</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SessionSettings</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['allow_actions'])) {
            throw new Error("Expected the field `allow_actions` to be an array in the JSON data but got " + data['allow_actions']);
        }
        // ensure the json data is a string
        if (data['session_length'] && !(typeof data['session_length'] === 'string' || data['session_length'] instanceof String)) {
            throw new Error("Expected the field `session_length` to be a primitive type in the JSON string but got " + data['session_length']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['unified_apis'])) {
            throw new Error("Expected the field `unified_apis` to be an array in the JSON data but got " + data['unified_apis']);
        }

        return true;
    }


}



/**
 * Hide actions from your users in [Vault](/apis/vault/reference#section/Get-Started). Actions in `allow_actions` will be shown on a connection in Vault. Available actions are: `delete`, `disconnect`, `reauthorize` and `disable`. Empty array will hide all actions. By default all actions are visible.
 * @member {Array.<module:model/SessionSettings.AllowActionsEnum>} allow_actions
 */
SessionSettings.prototype['allow_actions'] = undefined;

/**
 * Automatically redirect to redirect uri after the connection has been configured as callable. Defaults to `false`.
 * @member {Boolean} auto_redirect
 * @default false
 */
SessionSettings.prototype['auto_redirect'] = false;

/**
 * Hide Apideck connection guides in [Vault](/apis/vault/reference#section/Get-Started). Defaults to `false`.
 * @member {Boolean} hide_guides
 * @default false
 */
SessionSettings.prototype['hide_guides'] = false;

/**
 * A boolean that controls the display of the configurable resources for an integration. When set to true, the resource configuration options will be hidden and not shown to the user. When set to false, the resource configuration options will be displayed to the user.
 * @member {Boolean} hide_resource_settings
 * @default false
 */
SessionSettings.prototype['hide_resource_settings'] = false;

/**
 * Configure [Vault](/apis/vault/reference#section/Get-Started) to run in isolation mode, meaning it only shows the connection settings and hides the navigation items.
 * @member {Boolean} isolation_mode
 * @default false
 */
SessionSettings.prototype['isolation_mode'] = false;

/**
 * Configure [Vault](/apis/vault/reference#section/Get-Started) to show a banner informing the logged in user is in a test environment.
 * @member {Boolean} sandbox_mode
 * @default false
 */
SessionSettings.prototype['sandbox_mode'] = false;

/**
 * The duration of time the session is valid for (maximum 1 week).
 * @member {String} session_length
 * @default '1h'
 */
SessionSettings.prototype['session_length'] = '1h';

/**
 * Configure [Vault](/apis/vault/reference#section/Get-Started) to show the logs page. Defaults to `true`.
 * @member {Boolean} show_logs
 * @default true
 */
SessionSettings.prototype['show_logs'] = true;

/**
 * Configure [Vault](/apis/vault/reference#section/Get-Started) to show the sidebar. Defaults to `true`.
 * @member {Boolean} show_sidebar
 * @default true
 */
SessionSettings.prototype['show_sidebar'] = true;

/**
 * Configure [Vault](/apis/vault/reference#section/Get-Started) to show the suggestions page. Defaults to `false`.
 * @member {Boolean} show_suggestions
 * @default false
 */
SessionSettings.prototype['show_suggestions'] = false;

/**
 * Provide the IDs of the Unified APIs you want to be visible. Leaving it empty or omitting this field will show all Unified APIs.
 * @member {Array.<module:model/UnifiedApiId>} unified_apis
 */
SessionSettings.prototype['unified_apis'] = undefined;





/**
 * Allowed values for the <code>allowActions</code> property.
 * @enum {String}
 * @readonly
 */
SessionSettings['AllowActionsEnum'] = {

    /**
     * value: "delete"
     * @const
     */
    "delete": "delete",

    /**
     * value: "disconnect"
     * @const
     */
    "disconnect": "disconnect",

    /**
     * value: "reauthorize"
     * @const
     */
    "reauthorize": "reauthorize",

    /**
     * value: "disable"
     * @const
     */
    "disable": "disable"
};



export default SessionSettings;

