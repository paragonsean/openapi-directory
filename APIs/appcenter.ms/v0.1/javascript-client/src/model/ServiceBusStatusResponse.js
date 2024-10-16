/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ServiceBusStatusResponseSubscriptionsInner from './ServiceBusStatusResponseSubscriptionsInner';

/**
 * The ServiceBusStatusResponse model module.
 * @module model/ServiceBusStatusResponse
 * @version v0.1
 */
class ServiceBusStatusResponse {
    /**
     * Constructs a new <code>ServiceBusStatusResponse</code>.
     * @alias module:model/ServiceBusStatusResponse
     * @param status {String} 
     */
    constructor(status) { 
        
        ServiceBusStatusResponse.initialize(this, status);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, status) { 
        obj['status'] = status;
    }

    /**
     * Constructs a <code>ServiceBusStatusResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ServiceBusStatusResponse} obj Optional instance to populate.
     * @return {module:model/ServiceBusStatusResponse} The populated <code>ServiceBusStatusResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ServiceBusStatusResponse();

            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('subscriptions')) {
                obj['subscriptions'] = ApiClient.convertToType(data['subscriptions'], [ServiceBusStatusResponseSubscriptionsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ServiceBusStatusResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ServiceBusStatusResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ServiceBusStatusResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
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
                ServiceBusStatusResponseSubscriptionsInner.validateJSON(item);
            };
        }

        return true;
    }


}

ServiceBusStatusResponse.RequiredProperties = ["status"];

/**
 * @member {String} status
 */
ServiceBusStatusResponse.prototype['status'] = undefined;

/**
 * @member {Array.<module:model/ServiceBusStatusResponseSubscriptionsInner>} subscriptions
 */
ServiceBusStatusResponse.prototype['subscriptions'] = undefined;






export default ServiceBusStatusResponse;

