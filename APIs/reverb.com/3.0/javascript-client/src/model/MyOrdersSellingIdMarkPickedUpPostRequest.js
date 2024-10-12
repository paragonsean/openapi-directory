/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The MyOrdersSellingIdMarkPickedUpPostRequest model module.
 * @module model/MyOrdersSellingIdMarkPickedUpPostRequest
 * @version 3.0
 */
class MyOrdersSellingIdMarkPickedUpPostRequest {
    /**
     * Constructs a new <code>MyOrdersSellingIdMarkPickedUpPostRequest</code>.
     * @alias module:model/MyOrdersSellingIdMarkPickedUpPostRequest
     */
    constructor() { 
        
        MyOrdersSellingIdMarkPickedUpPostRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>MyOrdersSellingIdMarkPickedUpPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MyOrdersSellingIdMarkPickedUpPostRequest} obj Optional instance to populate.
     * @return {module:model/MyOrdersSellingIdMarkPickedUpPostRequest} The populated <code>MyOrdersSellingIdMarkPickedUpPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MyOrdersSellingIdMarkPickedUpPostRequest();

            if (data.hasOwnProperty('date')) {
                obj['date'] = ApiClient.convertToType(data['date'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MyOrdersSellingIdMarkPickedUpPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MyOrdersSellingIdMarkPickedUpPostRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['date'] && !(typeof data['date'] === 'string' || data['date'] instanceof String)) {
            throw new Error("Expected the field `date` to be a primitive type in the JSON string but got " + data['date']);
        }

        return true;
    }


}



/**
 * Date the item was picked up.
 * @member {String} date
 */
MyOrdersSellingIdMarkPickedUpPostRequest.prototype['date'] = undefined;






export default MyOrdersSellingIdMarkPickedUpPostRequest;

