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
import BillingAggregatedInformationGetByAppDefaultResponseError from './BillingAggregatedInformationGetByAppDefaultResponseError';

/**
 * The BillingError model module.
 * @module model/BillingError
 * @version v0.1
 */
class BillingError {
    /**
     * Constructs a new <code>BillingError</code>.
     * Error
     * @alias module:model/BillingError
     */
    constructor() { 
        
        BillingError.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BillingError</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BillingError} obj Optional instance to populate.
     * @return {module:model/BillingError} The populated <code>BillingError</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BillingError();

            if (data.hasOwnProperty('error')) {
                obj['error'] = BillingAggregatedInformationGetByAppDefaultResponseError.constructFromObject(data['error']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BillingError</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BillingError</code>.
     */
    static validateJSON(data) {
        // validate the optional field `error`
        if (data['error']) { // data not null
          BillingAggregatedInformationGetByAppDefaultResponseError.validateJSON(data['error']);
        }

        return true;
    }


}



/**
 * @member {module:model/BillingAggregatedInformationGetByAppDefaultResponseError} error
 */
BillingError.prototype['error'] = undefined;






export default BillingError;

