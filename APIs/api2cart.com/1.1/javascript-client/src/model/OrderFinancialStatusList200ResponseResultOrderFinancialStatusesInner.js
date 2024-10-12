/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner model module.
 * @module model/OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner
 * @version 1.1
 */
class OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner {
    /**
     * Constructs a new <code>OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner</code>.
     * @alias module:model/OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner
     */
    constructor() { 
        
        OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner} obj Optional instance to populate.
     * @return {module:model/OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner} The populated <code>OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * @member {String} id
 */
OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner.prototype['id'] = undefined;

/**
 * @member {String} name
 */
OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner.prototype['name'] = undefined;






export default OrderFinancialStatusList200ResponseResultOrderFinancialStatusesInner;

