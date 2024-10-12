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
import AuthType from './AuthType';
import ConnectionConfigurationInner from './ConnectionConfigurationInner';
import ConnectionState from './ConnectionState';
import CustomMapping from './CustomMapping';
import FormField from './FormField';
import IntegrationState from './IntegrationState';
import OAuthGrantType from './OAuthGrantType';
import WebhookSubscription from './WebhookSubscription';

/**
 * The Connection model module.
 * @module model/Connection
 * @version 10.0.0
 */
class Connection {
    /**
     * Constructs a new <code>Connection</code>.
     * @alias module:model/Connection
     */
    constructor() { 
        
        Connection.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Connection</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Connection} obj Optional instance to populate.
     * @return {module:model/Connection} The populated <code>Connection</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Connection();

            if (data.hasOwnProperty('auth_type')) {
                obj['auth_type'] = AuthType.constructFromObject(data['auth_type']);
            }
            if (data.hasOwnProperty('authorize_url')) {
                obj['authorize_url'] = ApiClient.convertToType(data['authorize_url'], 'String');
            }
            if (data.hasOwnProperty('configurable_resources')) {
                obj['configurable_resources'] = ApiClient.convertToType(data['configurable_resources'], ['String']);
            }
            if (data.hasOwnProperty('configuration')) {
                obj['configuration'] = ApiClient.convertToType(data['configuration'], [ConnectionConfigurationInner]);
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'Number');
            }
            if (data.hasOwnProperty('custom_mappings')) {
                obj['custom_mappings'] = ApiClient.convertToType(data['custom_mappings'], [CustomMapping]);
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('form_fields')) {
                obj['form_fields'] = ApiClient.convertToType(data['form_fields'], [FormField]);
            }
            if (data.hasOwnProperty('has_guide')) {
                obj['has_guide'] = ApiClient.convertToType(data['has_guide'], 'Boolean');
            }
            if (data.hasOwnProperty('icon')) {
                obj['icon'] = ApiClient.convertToType(data['icon'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('integration_state')) {
                obj['integration_state'] = IntegrationState.constructFromObject(data['integration_state']);
            }
            if (data.hasOwnProperty('logo')) {
                obj['logo'] = ApiClient.convertToType(data['logo'], 'String');
            }
            if (data.hasOwnProperty('metadata')) {
                obj['metadata'] = ApiClient.convertToType(data['metadata'], {'String': Object});
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('oauth_grant_type')) {
                obj['oauth_grant_type'] = OAuthGrantType.constructFromObject(data['oauth_grant_type']);
            }
            if (data.hasOwnProperty('resource_schema_support')) {
                obj['resource_schema_support'] = ApiClient.convertToType(data['resource_schema_support'], ['String']);
            }
            if (data.hasOwnProperty('resource_settings_support')) {
                obj['resource_settings_support'] = ApiClient.convertToType(data['resource_settings_support'], ['String']);
            }
            if (data.hasOwnProperty('revoke_url')) {
                obj['revoke_url'] = ApiClient.convertToType(data['revoke_url'], 'String');
            }
            if (data.hasOwnProperty('schema_support')) {
                obj['schema_support'] = ApiClient.convertToType(data['schema_support'], 'Boolean');
            }
            if (data.hasOwnProperty('service_id')) {
                obj['service_id'] = ApiClient.convertToType(data['service_id'], 'String');
            }
            if (data.hasOwnProperty('settings')) {
                obj['settings'] = ApiClient.convertToType(data['settings'], {'String': Object});
            }
            if (data.hasOwnProperty('settings_required_for_authorization')) {
                obj['settings_required_for_authorization'] = ApiClient.convertToType(data['settings_required_for_authorization'], ['String']);
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ConnectionState.constructFromObject(data['state']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('subscriptions')) {
                obj['subscriptions'] = ApiClient.convertToType(data['subscriptions'], [WebhookSubscription]);
            }
            if (data.hasOwnProperty('tag_line')) {
                obj['tag_line'] = ApiClient.convertToType(data['tag_line'], 'String');
            }
            if (data.hasOwnProperty('unified_api')) {
                obj['unified_api'] = ApiClient.convertToType(data['unified_api'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'Number');
            }
            if (data.hasOwnProperty('validation_support')) {
                obj['validation_support'] = ApiClient.convertToType(data['validation_support'], 'Boolean');
            }
            if (data.hasOwnProperty('website')) {
                obj['website'] = ApiClient.convertToType(data['website'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Connection</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Connection</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['authorize_url'] && !(typeof data['authorize_url'] === 'string' || data['authorize_url'] instanceof String)) {
            throw new Error("Expected the field `authorize_url` to be a primitive type in the JSON string but got " + data['authorize_url']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['configurable_resources'])) {
            throw new Error("Expected the field `configurable_resources` to be an array in the JSON data but got " + data['configurable_resources']);
        }
        if (data['configuration']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['configuration'])) {
                throw new Error("Expected the field `configuration` to be an array in the JSON data but got " + data['configuration']);
            }
            // validate the optional field `configuration` (array)
            for (const item of data['configuration']) {
                ConnectionConfigurationInner.validateJSON(item);
            };
        }
        if (data['custom_mappings']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['custom_mappings'])) {
                throw new Error("Expected the field `custom_mappings` to be an array in the JSON data but got " + data['custom_mappings']);
            }
            // validate the optional field `custom_mappings` (array)
            for (const item of data['custom_mappings']) {
                CustomMapping.validateJSON(item);
            };
        }
        if (data['form_fields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['form_fields'])) {
                throw new Error("Expected the field `form_fields` to be an array in the JSON data but got " + data['form_fields']);
            }
            // validate the optional field `form_fields` (array)
            for (const item of data['form_fields']) {
                FormField.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['icon'] && !(typeof data['icon'] === 'string' || data['icon'] instanceof String)) {
            throw new Error("Expected the field `icon` to be a primitive type in the JSON string but got " + data['icon']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['logo'] && !(typeof data['logo'] === 'string' || data['logo'] instanceof String)) {
            throw new Error("Expected the field `logo` to be a primitive type in the JSON string but got " + data['logo']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['resource_schema_support'])) {
            throw new Error("Expected the field `resource_schema_support` to be an array in the JSON data but got " + data['resource_schema_support']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['resource_settings_support'])) {
            throw new Error("Expected the field `resource_settings_support` to be an array in the JSON data but got " + data['resource_settings_support']);
        }
        // ensure the json data is a string
        if (data['revoke_url'] && !(typeof data['revoke_url'] === 'string' || data['revoke_url'] instanceof String)) {
            throw new Error("Expected the field `revoke_url` to be a primitive type in the JSON string but got " + data['revoke_url']);
        }
        // ensure the json data is a string
        if (data['service_id'] && !(typeof data['service_id'] === 'string' || data['service_id'] instanceof String)) {
            throw new Error("Expected the field `service_id` to be a primitive type in the JSON string but got " + data['service_id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['settings_required_for_authorization'])) {
            throw new Error("Expected the field `settings_required_for_authorization` to be an array in the JSON data but got " + data['settings_required_for_authorization']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        if (data['subscriptions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['subscriptions'])) {
                throw new Error("Expected the field `subscriptions` to be an array in the JSON data but got " + data['subscriptions']);
            }
            // validate the optional field `subscriptions` (array)
            for (const item of data['subscriptions']) {
                WebhookSubscription.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['tag_line'] && !(typeof data['tag_line'] === 'string' || data['tag_line'] instanceof String)) {
            throw new Error("Expected the field `tag_line` to be a primitive type in the JSON string but got " + data['tag_line']);
        }
        // ensure the json data is a string
        if (data['unified_api'] && !(typeof data['unified_api'] === 'string' || data['unified_api'] instanceof String)) {
            throw new Error("Expected the field `unified_api` to be a primitive type in the JSON string but got " + data['unified_api']);
        }
        // ensure the json data is a string
        if (data['website'] && !(typeof data['website'] === 'string' || data['website'] instanceof String)) {
            throw new Error("Expected the field `website` to be a primitive type in the JSON string but got " + data['website']);
        }

        return true;
    }


}



/**
 * @member {module:model/AuthType} auth_type
 */
Connection.prototype['auth_type'] = undefined;

/**
 * The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter to the `authorize_url`. Be sure to URL encode the `redirect_uri` part. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.
 * @member {String} authorize_url
 */
Connection.prototype['authorize_url'] = undefined;

/**
 * @member {Array.<String>} configurable_resources
 */
Connection.prototype['configurable_resources'] = undefined;

/**
 * @member {Array.<module:model/ConnectionConfigurationInner>} configuration
 */
Connection.prototype['configuration'] = undefined;

/**
 * @member {Number} created_at
 */
Connection.prototype['created_at'] = undefined;

/**
 * List of custom mappings configured for this connection
 * @member {Array.<module:model/CustomMapping>} custom_mappings
 */
Connection.prototype['custom_mappings'] = undefined;

/**
 * Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API.
 * @member {Boolean} enabled
 */
Connection.prototype['enabled'] = undefined;

/**
 * The settings that are wanted to create a connection.
 * @member {Array.<module:model/FormField>} form_fields
 */
Connection.prototype['form_fields'] = undefined;

/**
 * Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection).
 * @member {Boolean} has_guide
 */
Connection.prototype['has_guide'] = undefined;

/**
 * A visual icon of the connection, that will be shown in the Vault
 * @member {String} icon
 */
Connection.prototype['icon'] = undefined;

/**
 * The unique identifier of the connection.
 * @member {String} id
 */
Connection.prototype['id'] = undefined;

/**
 * @member {module:model/IntegrationState} integration_state
 */
Connection.prototype['integration_state'] = undefined;

/**
 * The logo of the connection, that will be shown in the Vault
 * @member {String} logo
 */
Connection.prototype['logo'] = undefined;

/**
 * Attach your own consumer specific metadata
 * @member {Object.<String, Object>} metadata
 */
Connection.prototype['metadata'] = undefined;

/**
 * The name of the connection
 * @member {String} name
 */
Connection.prototype['name'] = undefined;

/**
 * @member {module:model/OAuthGrantType} oauth_grant_type
 */
Connection.prototype['oauth_grant_type'] = undefined;

/**
 * @member {Array.<String>} resource_schema_support
 */
Connection.prototype['resource_schema_support'] = undefined;

/**
 * @member {Array.<String>} resource_settings_support
 */
Connection.prototype['resource_settings_support'] = undefined;

/**
 * The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.
 * @member {String} revoke_url
 */
Connection.prototype['revoke_url'] = undefined;

/**
 * @member {Boolean} schema_support
 */
Connection.prototype['schema_support'] = undefined;

/**
 * The ID of the service this connection belongs to.
 * @member {String} service_id
 */
Connection.prototype['service_id'] = undefined;

/**
 * Connection settings. Values will persist to `form_fields` with corresponding id
 * @member {Object.<String, Object>} settings
 */
Connection.prototype['settings'] = undefined;

/**
 * List of settings that are required to be configured on integration before authorization can occur
 * @member {Array.<String>} settings_required_for_authorization
 */
Connection.prototype['settings_required_for_authorization'] = undefined;

/**
 * @member {module:model/ConnectionState} state
 */
Connection.prototype['state'] = undefined;

/**
 * Status of the connection.
 * @member {module:model/Connection.StatusEnum} status
 */
Connection.prototype['status'] = undefined;

/**
 * @member {Array.<module:model/WebhookSubscription>} subscriptions
 */
Connection.prototype['subscriptions'] = undefined;

/**
 * @member {String} tag_line
 */
Connection.prototype['tag_line'] = undefined;

/**
 * The unified API category where the connection belongs to.
 * @member {String} unified_api
 */
Connection.prototype['unified_api'] = undefined;

/**
 * @member {Number} updated_at
 */
Connection.prototype['updated_at'] = undefined;

/**
 * @member {Boolean} validation_support
 */
Connection.prototype['validation_support'] = undefined;

/**
 * The website URL of the connection
 * @member {String} website
 */
Connection.prototype['website'] = undefined;





/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
Connection['StatusEnum'] = {

    /**
     * value: "live"
     * @const
     */
    "live": "live",

    /**
     * value: "upcoming"
     * @const
     */
    "upcoming": "upcoming",

    /**
     * value: "requested"
     * @const
     */
    "requested": "requested"
};



export default Connection;

