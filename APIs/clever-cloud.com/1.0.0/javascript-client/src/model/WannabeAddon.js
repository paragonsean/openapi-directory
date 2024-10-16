/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PaymentData from './PaymentData';

/**
 * The WannabeAddon model module.
 * @module model/WannabeAddon
 * @version 1.0.0
 */
class WannabeAddon {
    /**
     * Constructs a new <code>WannabeAddon</code>.
     * @alias module:model/WannabeAddon
     * @param name {String} 
     * @param payment {module:model/PaymentData} 
     * @param plan {String} 
     * @param providerId {String} 
     * @param region {String} 
     */
    constructor(name, payment, plan, providerId, region) { 
        
        WannabeAddon.initialize(this, name, payment, plan, providerId, region);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name, payment, plan, providerId, region) { 
        obj['name'] = name;
        obj['payment'] = payment;
        obj['plan'] = plan;
        obj['providerId'] = providerId;
        obj['region'] = region;
    }

    /**
     * Constructs a <code>WannabeAddon</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WannabeAddon} obj Optional instance to populate.
     * @return {module:model/WannabeAddon} The populated <code>WannabeAddon</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WannabeAddon();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('payment')) {
                obj['payment'] = PaymentData.constructFromObject(data['payment']);
            }
            if (data.hasOwnProperty('plan')) {
                obj['plan'] = ApiClient.convertToType(data['plan'], 'String');
            }
            if (data.hasOwnProperty('providerId')) {
                obj['providerId'] = ApiClient.convertToType(data['providerId'], 'String');
            }
            if (data.hasOwnProperty('region')) {
                obj['region'] = ApiClient.convertToType(data['region'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WannabeAddon</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WannabeAddon</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of WannabeAddon.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `payment`
        if (data['payment']) { // data not null
          PaymentData.validateJSON(data['payment']);
        }
        // ensure the json data is a string
        if (data['plan'] && !(typeof data['plan'] === 'string' || data['plan'] instanceof String)) {
            throw new Error("Expected the field `plan` to be a primitive type in the JSON string but got " + data['plan']);
        }
        // ensure the json data is a string
        if (data['providerId'] && !(typeof data['providerId'] === 'string' || data['providerId'] instanceof String)) {
            throw new Error("Expected the field `providerId` to be a primitive type in the JSON string but got " + data['providerId']);
        }
        // ensure the json data is a string
        if (data['region'] && !(typeof data['region'] === 'string' || data['region'] instanceof String)) {
            throw new Error("Expected the field `region` to be a primitive type in the JSON string but got " + data['region']);
        }

        return true;
    }


}

WannabeAddon.RequiredProperties = ["name", "payment", "plan", "providerId", "region"];

/**
 * @member {String} name
 */
WannabeAddon.prototype['name'] = undefined;

/**
 * @member {module:model/PaymentData} payment
 */
WannabeAddon.prototype['payment'] = undefined;

/**
 * @member {String} plan
 */
WannabeAddon.prototype['plan'] = undefined;

/**
 * 
 * @member {String} providerId
 */
WannabeAddon.prototype['providerId'] = undefined;

/**
 * @member {String} region
 */
WannabeAddon.prototype['region'] = undefined;






export default WannabeAddon;

