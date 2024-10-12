/**
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PointPointAlerts model module.
 * @module model/PointPointAlerts
 * @version v1
 */
class PointPointAlerts {
    /**
     * Constructs a new <code>PointPointAlerts</code>.
     * @alias module:model/PointPointAlerts
     */
    constructor() { 
        
        PointPointAlerts.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PointPointAlerts</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PointPointAlerts} obj Optional instance to populate.
     * @return {module:model/PointPointAlerts} The populated <code>PointPointAlerts</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PointPointAlerts();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ApiClient.convertToType(data['data'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PointPointAlerts</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PointPointAlerts</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['data'] && !(typeof data['data'] === 'string' || data['data'] instanceof String)) {
            throw new Error("Expected the field `data` to be a primitive type in the JSON string but got " + data['data']);
        }

        return true;
    }


}



/**
 * @member {String} data
 */
PointPointAlerts.prototype['data'] = undefined;






export default PointPointAlerts;

