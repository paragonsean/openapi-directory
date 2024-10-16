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
 * The WebhookResource model module.
 * @module model/WebhookResource
 * @version V2
 */
class WebhookResource {
    /**
     * Constructs a new <code>WebhookResource</code>.
     * WebhookResource describes a resource and a list of supported events, once event is triggered CallFire performs an HTTP POST request to a client&#39;s endpoint
     * @alias module:model/WebhookResource
     */
    constructor() { 
        
        WebhookResource.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>WebhookResource</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WebhookResource} obj Optional instance to populate.
     * @return {module:model/WebhookResource} The populated <code>WebhookResource</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WebhookResource();

            if (data.hasOwnProperty('resource')) {
                obj['resource'] = ApiClient.convertToType(data['resource'], 'String');
            }
            if (data.hasOwnProperty('supportedEvents')) {
                obj['supportedEvents'] = ApiClient.convertToType(data['supportedEvents'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WebhookResource</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WebhookResource</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['resource'] && !(typeof data['resource'] === 'string' || data['resource'] instanceof String)) {
            throw new Error("Expected the field `resource` to be a primitive type in the JSON string but got " + data['resource']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['supportedEvents'])) {
            throw new Error("Expected the field `supportedEvents` to be an array in the JSON data but got " + data['supportedEvents']);
        }

        return true;
    }


}



/**
 * A name of a webhook resource (ex: InboundCall, OutboundCall, InboundText, OutboundText, CallBroadcast, TextBroadcast, etc...)
 * @member {String} resource
 */
WebhookResource.prototype['resource'] = undefined;

/**
 * A list of event names which are supported by webhook resource (ex: Started, Stopped, Finished, etc.)
 * @member {Array.<String>} supportedEvents
 */
WebhookResource.prototype['supportedEvents'] = undefined;






export default WebhookResource;

