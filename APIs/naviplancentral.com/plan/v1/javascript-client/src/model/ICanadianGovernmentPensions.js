/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
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
import Currency from './Currency';

/**
 * The ICanadianGovernmentPensions model module.
 * @module model/ICanadianGovernmentPensions
 * @version v1
 */
class ICanadianGovernmentPensions {
    /**
     * Constructs a new <code>ICanadianGovernmentPensions</code>.
     * @alias module:model/ICanadianGovernmentPensions
     */
    constructor() { 
        
        ICanadianGovernmentPensions.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ICanadianGovernmentPensions</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ICanadianGovernmentPensions} obj Optional instance to populate.
     * @return {module:model/ICanadianGovernmentPensions} The populated <code>ICanadianGovernmentPensions</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ICanadianGovernmentPensions();

            if (data.hasOwnProperty('canadianOrQuebecPensionPlan')) {
                obj['canadianOrQuebecPensionPlan'] = Currency.constructFromObject(data['canadianOrQuebecPensionPlan']);
            }
            if (data.hasOwnProperty('oldAgeSecurity')) {
                obj['oldAgeSecurity'] = Currency.constructFromObject(data['oldAgeSecurity']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ICanadianGovernmentPensions</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ICanadianGovernmentPensions</code>.
     */
    static validateJSON(data) {
        // validate the optional field `canadianOrQuebecPensionPlan`
        if (data['canadianOrQuebecPensionPlan']) { // data not null
          Currency.validateJSON(data['canadianOrQuebecPensionPlan']);
        }
        // validate the optional field `oldAgeSecurity`
        if (data['oldAgeSecurity']) { // data not null
          Currency.validateJSON(data['oldAgeSecurity']);
        }

        return true;
    }


}



/**
 * @member {module:model/Currency} canadianOrQuebecPensionPlan
 */
ICanadianGovernmentPensions.prototype['canadianOrQuebecPensionPlan'] = undefined;

/**
 * @member {module:model/Currency} oldAgeSecurity
 */
ICanadianGovernmentPensions.prototype['oldAgeSecurity'] = undefined;






export default ICanadianGovernmentPensions;

