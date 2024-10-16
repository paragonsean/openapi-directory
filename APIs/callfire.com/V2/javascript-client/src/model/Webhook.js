/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Webhook model module.
 * @module model/Webhook
 * @version V2
 */
class Webhook {
    /**
     * Constructs a new <code>Webhook</code>.
     * Webhook is a user-defined callback, which can be maintained via API. CallFire will send POST request to a client&#39;s endpoint defined in webhook once one of assigned events is triggered. See [webhooks guide](https://developers.callfire.com/webhooks-guide.html) for more information about CallFire Webhooks API.
     * @alias module:model/Webhook
     */
    constructor() { 
        
        Webhook.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Webhook</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Webhook} obj Optional instance to populate.
     * @return {module:model/Webhook} The populated <code>Webhook</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Webhook();

            if (data.hasOwnProperty('callback')) {
                obj['callback'] = ApiClient.convertToType(data['callback'], 'String');
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'Number');
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('events')) {
                obj['events'] = ApiClient.convertToType(data['events'], ['String']);
            }
            if (data.hasOwnProperty('expiresAt')) {
                obj['expiresAt'] = ApiClient.convertToType(data['expiresAt'], 'Number');
            }
            if (data.hasOwnProperty('fields')) {
                obj['fields'] = ApiClient.convertToType(data['fields'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('nonStrictSsl')) {
                obj['nonStrictSsl'] = ApiClient.convertToType(data['nonStrictSsl'], 'Boolean');
            }
            if (data.hasOwnProperty('resource')) {
                obj['resource'] = ApiClient.convertToType(data['resource'], 'String');
            }
            if (data.hasOwnProperty('secret')) {
                obj['secret'] = ApiClient.convertToType(data['secret'], 'String');
            }
            if (data.hasOwnProperty('singleUse')) {
                obj['singleUse'] = ApiClient.convertToType(data['singleUse'], 'Boolean');
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Webhook</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Webhook</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['callback'] && !(typeof data['callback'] === 'string' || data['callback'] instanceof String)) {
            throw new Error("Expected the field `callback` to be a primitive type in the JSON string but got " + data['callback']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['events'])) {
            throw new Error("Expected the field `events` to be an array in the JSON data but got " + data['events']);
        }
        // ensure the json data is a string
        if (data['fields'] && !(typeof data['fields'] === 'string' || data['fields'] instanceof String)) {
            throw new Error("Expected the field `fields` to be a primitive type in the JSON string but got " + data['fields']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['resource'] && !(typeof data['resource'] === 'string' || data['resource'] instanceof String)) {
            throw new Error("Expected the field `resource` to be a primitive type in the JSON string but got " + data['resource']);
        }
        // ensure the json data is a string
        if (data['secret'] && !(typeof data['secret'] === 'string' || data['secret'] instanceof String)) {
            throw new Error("Expected the field `secret` to be a primitive type in the JSON string but got " + data['secret']);
        }

        return true;
    }


}



/**
 * URL that webhook will send POST to on resource event trigger
 * @member {String} callback
 */
Webhook.prototype['callback'] = undefined;

/**
 * A time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000
 * @member {Number} createdAt
 */
Webhook.prototype['createdAt'] = undefined;

/**
 * A parameter which allows the webhook to send requests to unknown ssl endpoints (ssl certificate verification is disabled)
 * @member {Boolean} enabled
 */
Webhook.prototype['enabled'] = undefined;

/**
 * Comma separated list of events on resource that will trigger callbacks (ex: STARTED, STOPPED, FINISHED, etc...). 
 * @member {Array.<String>} events
 */
Webhook.prototype['events'] = undefined;

/**
 * ~
 * @member {Number} expiresAt
 */
Webhook.prototype['expiresAt'] = undefined;

/**
 * A limit callback response to a particular fields
 * @member {String} fields
 */
Webhook.prototype['fields'] = undefined;

/**
 * An id of a webhook
 * @member {Number} id
 */
Webhook.prototype['id'] = undefined;

/**
 * A name of a webhook
 * @member {String} name
 */
Webhook.prototype['name'] = undefined;

/**
 * A parameter which allows the webhook to send requests to unknown ssl endpoints (ssl certificate verification is disabled)
 * @member {Boolean} nonStrictSsl
 */
Webhook.prototype['nonStrictSsl'] = undefined;

/**
 * A resource name that webhook is watching events on. Use GET /webhooks/resources to determine resources and events available (ex: InboundCall, OutboundCall, InboundText, OutboundText, CallBroadcast, TextBroadcast, etc...)
 * @member {String} resource
 */
Webhook.prototype['resource'] = undefined;

/**
 * Webhook secret token which is used as a signing key to HmacSHA1 hash of json payload which is returned in 'X-CallFire-Signature' header. This header can be used to verify callback POST is coming from CallFire. See [security guide](https://developers.callfire.com/security-guide.html)
 * @member {String} secret
 */
Webhook.prototype['secret'] = undefined;

/**
 * If true is set then webhook triggers only once. Afterwards the webhook will be deleted
 * @member {Boolean} singleUse
 */
Webhook.prototype['singleUse'] = undefined;

/**
 * A time when the given resource was updated, formatted in unix time milliseconds (read only). Example: 1473781817000
 * @member {Number} updatedAt
 */
Webhook.prototype['updatedAt'] = undefined;






export default Webhook;

