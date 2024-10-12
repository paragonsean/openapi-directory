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
 * The ConnectionWebhook model module.
 * @module model/ConnectionWebhook
 * @version 10.0.0
 */
class ConnectionWebhook {
    /**
     * Constructs a new <code>ConnectionWebhook</code>.
     * @alias module:model/ConnectionWebhook
     * @param deliveryUrl {String} The delivery url of the webhook endpoint.
     * @param events {Array.<module:model/ConnectionWebhook.EventsEnum>} The list of subscribed events for this webhook. [`*`] indicates that all events are enabled.
     * @param executeBaseUrl {String} The Unify Base URL events from connectors will be sent to after service id is appended.
     * @param status {module:model/ConnectionWebhook.StatusEnum} The status of the webhook.
     * @param unifiedApi {module:model/UnifiedApiId} 
     */
    constructor(deliveryUrl, events, executeBaseUrl, status, unifiedApi) { 
        
        ConnectionWebhook.initialize(this, deliveryUrl, events, executeBaseUrl, status, unifiedApi);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, deliveryUrl, events, executeBaseUrl, status, unifiedApi) { 
        obj['delivery_url'] = deliveryUrl;
        obj['events'] = events;
        obj['execute_base_url'] = executeBaseUrl;
        obj['status'] = status;
        obj['unified_api'] = unifiedApi;
    }

    /**
     * Constructs a <code>ConnectionWebhook</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ConnectionWebhook} obj Optional instance to populate.
     * @return {module:model/ConnectionWebhook} The populated <code>ConnectionWebhook</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ConnectionWebhook();

            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'Date');
            }
            if (data.hasOwnProperty('delivery_url')) {
                obj['delivery_url'] = ApiClient.convertToType(data['delivery_url'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('disabled_reason')) {
                obj['disabled_reason'] = ApiClient.convertToType(data['disabled_reason'], 'String');
            }
            if (data.hasOwnProperty('events')) {
                obj['events'] = ApiClient.convertToType(data['events'], ['String']);
            }
            if (data.hasOwnProperty('execute_base_url')) {
                obj['execute_base_url'] = ApiClient.convertToType(data['execute_base_url'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('unified_api')) {
                obj['unified_api'] = UnifiedApiId.constructFromObject(data['unified_api']);
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ConnectionWebhook</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ConnectionWebhook</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ConnectionWebhook.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['delivery_url'] && !(typeof data['delivery_url'] === 'string' || data['delivery_url'] instanceof String)) {
            throw new Error("Expected the field `delivery_url` to be a primitive type in the JSON string but got " + data['delivery_url']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['disabled_reason'] && !(typeof data['disabled_reason'] === 'string' || data['disabled_reason'] instanceof String)) {
            throw new Error("Expected the field `disabled_reason` to be a primitive type in the JSON string but got " + data['disabled_reason']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['events'])) {
            throw new Error("Expected the field `events` to be an array in the JSON data but got " + data['events']);
        }
        // ensure the json data is a string
        if (data['execute_base_url'] && !(typeof data['execute_base_url'] === 'string' || data['execute_base_url'] instanceof String)) {
            throw new Error("Expected the field `execute_base_url` to be a primitive type in the JSON string but got " + data['execute_base_url']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}

ConnectionWebhook.RequiredProperties = ["delivery_url", "events", "execute_base_url", "status", "unified_api"];

/**
 * The date and time when the object was created.
 * @member {Date} created_at
 */
ConnectionWebhook.prototype['created_at'] = undefined;

/**
 * The delivery url of the webhook endpoint.
 * @member {String} delivery_url
 */
ConnectionWebhook.prototype['delivery_url'] = undefined;

/**
 * A description of the object.
 * @member {String} description
 */
ConnectionWebhook.prototype['description'] = undefined;

/**
 * Indicates if the webhook has has been disabled as it reached its retry limit or if account is over the usage allocated by it's plan.
 * @member {module:model/ConnectionWebhook.DisabledReasonEnum} disabled_reason
 */
ConnectionWebhook.prototype['disabled_reason'] = undefined;

/**
 * The list of subscribed events for this webhook. [`*`] indicates that all events are enabled.
 * @member {Array.<module:model/ConnectionWebhook.EventsEnum>} events
 */
ConnectionWebhook.prototype['events'] = undefined;

/**
 * The Unify Base URL events from connectors will be sent to after service id is appended.
 * @member {String} execute_base_url
 */
ConnectionWebhook.prototype['execute_base_url'] = undefined;

/**
 * @member {String} id
 */
ConnectionWebhook.prototype['id'] = undefined;

/**
 * The status of the webhook.
 * @member {module:model/ConnectionWebhook.StatusEnum} status
 */
ConnectionWebhook.prototype['status'] = undefined;

/**
 * @member {module:model/UnifiedApiId} unified_api
 */
ConnectionWebhook.prototype['unified_api'] = undefined;

/**
 * The date and time when the object was last updated.
 * @member {Date} updated_at
 */
ConnectionWebhook.prototype['updated_at'] = undefined;





/**
 * Allowed values for the <code>disabled_reason</code> property.
 * @enum {String}
 * @readonly
 */
ConnectionWebhook['DisabledReasonEnum'] = {

    /**
     * value: "none"
     * @const
     */
    "none": "none",

    /**
     * value: "retry_limit"
     * @const
     */
    "retry_limit": "retry_limit",

    /**
     * value: "usage_limit"
     * @const
     */
    "usage_limit": "usage_limit"
};


/**
 * Allowed values for the <code>events</code> property.
 * @enum {String}
 * @readonly
 */
ConnectionWebhook['EventsEnum'] = {

    /**
     * value: "*"
     * @const
     */
    "STAR": "*",

    /**
     * value: "crm.activity.created"
     * @const
     */
    "crm.activity.created": "crm.activity.created",

    /**
     * value: "crm.activity.updated"
     * @const
     */
    "crm.activity.updated": "crm.activity.updated",

    /**
     * value: "crm.activity.deleted"
     * @const
     */
    "crm.activity.deleted": "crm.activity.deleted",

    /**
     * value: "crm.company.created"
     * @const
     */
    "crm.company.created": "crm.company.created",

    /**
     * value: "crm.company.updated"
     * @const
     */
    "crm.company.updated": "crm.company.updated",

    /**
     * value: "crm.company.deleted"
     * @const
     */
    "crm.company.deleted": "crm.company.deleted",

    /**
     * value: "crm.contact.created"
     * @const
     */
    "crm.contact.created": "crm.contact.created",

    /**
     * value: "crm.contact.updated"
     * @const
     */
    "crm.contact.updated": "crm.contact.updated",

    /**
     * value: "crm.contact.deleted"
     * @const
     */
    "crm.contact.deleted": "crm.contact.deleted",

    /**
     * value: "crm.lead.created"
     * @const
     */
    "crm.lead.created": "crm.lead.created",

    /**
     * value: "crm.lead.updated"
     * @const
     */
    "crm.lead.updated": "crm.lead.updated",

    /**
     * value: "crm.lead.deleted"
     * @const
     */
    "crm.lead.deleted": "crm.lead.deleted",

    /**
     * value: "crm.note.created"
     * @const
     */
    "crm.note.created": "crm.note.created",

    /**
     * value: "crm.notes.updated"
     * @const
     */
    "crm.notes.updated": "crm.notes.updated",

    /**
     * value: "crm.notes.deleted"
     * @const
     */
    "crm.notes.deleted": "crm.notes.deleted",

    /**
     * value: "crm.opportunity.created"
     * @const
     */
    "crm.opportunity.created": "crm.opportunity.created",

    /**
     * value: "crm.opportunity.updated"
     * @const
     */
    "crm.opportunity.updated": "crm.opportunity.updated",

    /**
     * value: "crm.opportunity.deleted"
     * @const
     */
    "crm.opportunity.deleted": "crm.opportunity.deleted",

    /**
     * value: "lead.lead.created"
     * @const
     */
    "lead.lead.created": "lead.lead.created",

    /**
     * value: "lead.lead.updated"
     * @const
     */
    "lead.lead.updated": "lead.lead.updated",

    /**
     * value: "lead.lead.deleted"
     * @const
     */
    "lead.lead.deleted": "lead.lead.deleted",

    /**
     * value: "vault.connection.created"
     * @const
     */
    "vault.connection.created": "vault.connection.created",

    /**
     * value: "vault.connection.updated"
     * @const
     */
    "vault.connection.updated": "vault.connection.updated",

    /**
     * value: "vault.connection.disabled"
     * @const
     */
    "vault.connection.disabled": "vault.connection.disabled",

    /**
     * value: "vault.connection.deleted"
     * @const
     */
    "vault.connection.deleted": "vault.connection.deleted",

    /**
     * value: "vault.connection.callable"
     * @const
     */
    "vault.connection.callable": "vault.connection.callable",

    /**
     * value: "vault.connection.revoked"
     * @const
     */
    "vault.connection.revoked": "vault.connection.revoked",

    /**
     * value: "vault.connection.token_refresh.failed"
     * @const
     */
    "vault.connection.token_refresh.failed": "vault.connection.token_refresh.failed",

    /**
     * value: "ats.job.created"
     * @const
     */
    "ats.job.created": "ats.job.created",

    /**
     * value: "ats.job.updated"
     * @const
     */
    "ats.job.updated": "ats.job.updated",

    /**
     * value: "ats.job.deleted"
     * @const
     */
    "ats.job.deleted": "ats.job.deleted",

    /**
     * value: "ats.applicant.created"
     * @const
     */
    "ats.applicant.created": "ats.applicant.created",

    /**
     * value: "ats.applicant.updated"
     * @const
     */
    "ats.applicant.updated": "ats.applicant.updated",

    /**
     * value: "ats.applicant.deleted"
     * @const
     */
    "ats.applicant.deleted": "ats.applicant.deleted",

    /**
     * value: "accounting.customer.created"
     * @const
     */
    "accounting.customer.created": "accounting.customer.created",

    /**
     * value: "accounting.customer.updated"
     * @const
     */
    "accounting.customer.updated": "accounting.customer.updated",

    /**
     * value: "accounting.customer.deleted"
     * @const
     */
    "accounting.customer.deleted": "accounting.customer.deleted",

    /**
     * value: "accounting.invoice.created"
     * @const
     */
    "accounting.invoice.created": "accounting.invoice.created",

    /**
     * value: "accounting.invoice.updated"
     * @const
     */
    "accounting.invoice.updated": "accounting.invoice.updated",

    /**
     * value: "accounting.invoice.deleted"
     * @const
     */
    "accounting.invoice.deleted": "accounting.invoice.deleted",

    /**
     * value: "accounting.invoice_item.created"
     * @const
     */
    "accounting.invoice_item.created": "accounting.invoice_item.created",

    /**
     * value: "accounting.invoice_item.updated"
     * @const
     */
    "accounting.invoice_item.updated": "accounting.invoice_item.updated",

    /**
     * value: "accounting.invoice_item.deleted"
     * @const
     */
    "accounting.invoice_item.deleted": "accounting.invoice_item.deleted",

    /**
     * value: "accounting.ledger_account.created"
     * @const
     */
    "accounting.ledger_account.created": "accounting.ledger_account.created",

    /**
     * value: "accounting.ledger_account.updated"
     * @const
     */
    "accounting.ledger_account.updated": "accounting.ledger_account.updated",

    /**
     * value: "accounting.ledger_account.deleted"
     * @const
     */
    "accounting.ledger_account.deleted": "accounting.ledger_account.deleted",

    /**
     * value: "accounting.tax_rate.created"
     * @const
     */
    "accounting.tax_rate.created": "accounting.tax_rate.created",

    /**
     * value: "accounting.tax_rate.updated"
     * @const
     */
    "accounting.tax_rate.updated": "accounting.tax_rate.updated",

    /**
     * value: "accounting.tax_rate.deleted"
     * @const
     */
    "accounting.tax_rate.deleted": "accounting.tax_rate.deleted",

    /**
     * value: "accounting.bill.created"
     * @const
     */
    "accounting.bill.created": "accounting.bill.created",

    /**
     * value: "accounting.bill.updated"
     * @const
     */
    "accounting.bill.updated": "accounting.bill.updated",

    /**
     * value: "accounting.bill.deleted"
     * @const
     */
    "accounting.bill.deleted": "accounting.bill.deleted",

    /**
     * value: "accounting.payment.created"
     * @const
     */
    "accounting.payment.created": "accounting.payment.created",

    /**
     * value: "accounting.payment.updated"
     * @const
     */
    "accounting.payment.updated": "accounting.payment.updated",

    /**
     * value: "accounting.payment.deleted"
     * @const
     */
    "accounting.payment.deleted": "accounting.payment.deleted",

    /**
     * value: "accounting.supplier.created"
     * @const
     */
    "accounting.supplier.created": "accounting.supplier.created",

    /**
     * value: "accounting.supplier.updated"
     * @const
     */
    "accounting.supplier.updated": "accounting.supplier.updated",

    /**
     * value: "accounting.supplier.deleted"
     * @const
     */
    "accounting.supplier.deleted": "accounting.supplier.deleted",

    /**
     * value: "accounting.purchase-order.created"
     * @const
     */
    "accounting.purchase-order.created": "accounting.purchase-order.created",

    /**
     * value: "accounting.purchase-order.updated"
     * @const
     */
    "accounting.purchase-order.updated": "accounting.purchase-order.updated",

    /**
     * value: "accounting.purchase-order.deleted"
     * @const
     */
    "accounting.purchase-order.deleted": "accounting.purchase-order.deleted",

    /**
     * value: "pos.order.created"
     * @const
     */
    "pos.order.created": "pos.order.created",

    /**
     * value: "pos.order.updated"
     * @const
     */
    "pos.order.updated": "pos.order.updated",

    /**
     * value: "pos.order.deleted"
     * @const
     */
    "pos.order.deleted": "pos.order.deleted",

    /**
     * value: "pos.product.created"
     * @const
     */
    "pos.product.created": "pos.product.created",

    /**
     * value: "pos.product.updated"
     * @const
     */
    "pos.product.updated": "pos.product.updated",

    /**
     * value: "pos.product.deleted"
     * @const
     */
    "pos.product.deleted": "pos.product.deleted",

    /**
     * value: "pos.payment.created"
     * @const
     */
    "pos.payment.created": "pos.payment.created",

    /**
     * value: "pos.payment.updated"
     * @const
     */
    "pos.payment.updated": "pos.payment.updated",

    /**
     * value: "pos.payment.deleted"
     * @const
     */
    "pos.payment.deleted": "pos.payment.deleted",

    /**
     * value: "pos.merchant.created"
     * @const
     */
    "pos.merchant.created": "pos.merchant.created",

    /**
     * value: "pos.merchant.updated"
     * @const
     */
    "pos.merchant.updated": "pos.merchant.updated",

    /**
     * value: "pos.merchant.deleted"
     * @const
     */
    "pos.merchant.deleted": "pos.merchant.deleted",

    /**
     * value: "pos.location.created"
     * @const
     */
    "pos.location.created": "pos.location.created",

    /**
     * value: "pos.location.updated"
     * @const
     */
    "pos.location.updated": "pos.location.updated",

    /**
     * value: "pos.location.deleted"
     * @const
     */
    "pos.location.deleted": "pos.location.deleted",

    /**
     * value: "pos.item.created"
     * @const
     */
    "pos.item.created": "pos.item.created",

    /**
     * value: "pos.item.updated"
     * @const
     */
    "pos.item.updated": "pos.item.updated",

    /**
     * value: "pos.item.deleted"
     * @const
     */
    "pos.item.deleted": "pos.item.deleted",

    /**
     * value: "pos.modifier.created"
     * @const
     */
    "pos.modifier.created": "pos.modifier.created",

    /**
     * value: "pos.modifier.updated"
     * @const
     */
    "pos.modifier.updated": "pos.modifier.updated",

    /**
     * value: "pos.modifier.deleted"
     * @const
     */
    "pos.modifier.deleted": "pos.modifier.deleted",

    /**
     * value: "pos.modifier-group.created"
     * @const
     */
    "pos.modifier-group.created": "pos.modifier-group.created",

    /**
     * value: "pos.modifier-group.updated"
     * @const
     */
    "pos.modifier-group.updated": "pos.modifier-group.updated",

    /**
     * value: "pos.modifier-group.deleted"
     * @const
     */
    "pos.modifier-group.deleted": "pos.modifier-group.deleted",

    /**
     * value: "hris.employee.created"
     * @const
     */
    "hris.employee.created": "hris.employee.created",

    /**
     * value: "hris.employee.updated"
     * @const
     */
    "hris.employee.updated": "hris.employee.updated",

    /**
     * value: "hris.employee.deleted"
     * @const
     */
    "hris.employee.deleted": "hris.employee.deleted",

    /**
     * value: "hris.employee.terminated"
     * @const
     */
    "hris.employee.terminated": "hris.employee.terminated",

    /**
     * value: "hris.company.created"
     * @const
     */
    "hris.company.created": "hris.company.created",

    /**
     * value: "hris.company.updated"
     * @const
     */
    "hris.company.updated": "hris.company.updated",

    /**
     * value: "hris.company.deleted"
     * @const
     */
    "hris.company.deleted": "hris.company.deleted",

    /**
     * value: "file-storage.file.created"
     * @const
     */
    "file-storage.file.created": "file-storage.file.created",

    /**
     * value: "file-storage.file.updated"
     * @const
     */
    "file-storage.file.updated": "file-storage.file.updated",

    /**
     * value: "file-storage.file.deleted"
     * @const
     */
    "file-storage.file.deleted": "file-storage.file.deleted",

    /**
     * value: "issue-tracking.ticket.created"
     * @const
     */
    "issue-tracking.ticket.created": "issue-tracking.ticket.created",

    /**
     * value: "issue-tracking.ticket.updated"
     * @const
     */
    "issue-tracking.ticket.updated": "issue-tracking.ticket.updated",

    /**
     * value: "issue-tracking.ticket.deleted"
     * @const
     */
    "issue-tracking.ticket.deleted": "issue-tracking.ticket.deleted",

    /**
     * value: "ats.application.created"
     * @const
     */
    "ats.application.created": "ats.application.created",

    /**
     * value: "ats.application.updated"
     * @const
     */
    "ats.application.updated": "ats.application.updated",

    /**
     * value: "ats.application.deleted"
     * @const
     */
    "ats.application.deleted": "ats.application.deleted"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
ConnectionWebhook['StatusEnum'] = {

    /**
     * value: "enabled"
     * @const
     */
    "enabled": "enabled",

    /**
     * value: "disabled"
     * @const
     */
    "disabled": "disabled"
};



export default ConnectionWebhook;

