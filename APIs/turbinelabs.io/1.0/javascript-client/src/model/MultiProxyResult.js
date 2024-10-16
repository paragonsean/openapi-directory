/**
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Proxy from './Proxy';

/**
 * The MultiProxyResult model module.
 * @module model/MultiProxyResult
 * @version 1.0
 */
class MultiProxyResult {
    /**
     * Constructs a new <code>MultiProxyResult</code>.
     * @alias module:model/MultiProxyResult
     */
    constructor() { 
        
        MultiProxyResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>MultiProxyResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MultiProxyResult} obj Optional instance to populate.
     * @return {module:model/MultiProxyResult} The populated <code>MultiProxyResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MultiProxyResult();

            if (data.hasOwnProperty('result')) {
                obj['result'] = ApiClient.convertToType(data['result'], [Proxy]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MultiProxyResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MultiProxyResult</code>.
     */
    static validateJSON(data) {
        if (data['result']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['result'])) {
                throw new Error("Expected the field `result` to be an array in the JSON data but got " + data['result']);
            }
            // validate the optional field `result` (array)
            for (const item of data['result']) {
                Proxy.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Proxy>} result
 */
MultiProxyResult.prototype['result'] = undefined;






export default MultiProxyResult;

