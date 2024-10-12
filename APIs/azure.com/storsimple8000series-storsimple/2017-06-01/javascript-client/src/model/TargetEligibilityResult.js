/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import TargetEligibilityErrorMessage from './TargetEligibilityErrorMessage';

/**
 * The TargetEligibilityResult model module.
 * @module model/TargetEligibilityResult
 * @version 2017-06-01
 */
class TargetEligibilityResult {
    /**
     * Constructs a new <code>TargetEligibilityResult</code>.
     * The eligibility result of device, as a failover target device.
     * @alias module:model/TargetEligibilityResult
     */
    constructor() { 
        
        TargetEligibilityResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TargetEligibilityResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TargetEligibilityResult} obj Optional instance to populate.
     * @return {module:model/TargetEligibilityResult} The populated <code>TargetEligibilityResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TargetEligibilityResult();

            if (data.hasOwnProperty('eligibilityStatus')) {
                obj['eligibilityStatus'] = ApiClient.convertToType(data['eligibilityStatus'], 'String');
            }
            if (data.hasOwnProperty('messages')) {
                obj['messages'] = ApiClient.convertToType(data['messages'], [TargetEligibilityErrorMessage]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TargetEligibilityResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TargetEligibilityResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['eligibilityStatus'] && !(typeof data['eligibilityStatus'] === 'string' || data['eligibilityStatus'] instanceof String)) {
            throw new Error("Expected the field `eligibilityStatus` to be a primitive type in the JSON string but got " + data['eligibilityStatus']);
        }
        if (data['messages']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['messages'])) {
                throw new Error("Expected the field `messages` to be an array in the JSON data but got " + data['messages']);
            }
            // validate the optional field `messages` (array)
            for (const item of data['messages']) {
                TargetEligibilityErrorMessage.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * The eligibility status of device, as a failover target device.
 * @member {module:model/TargetEligibilityResult.EligibilityStatusEnum} eligibilityStatus
 */
TargetEligibilityResult.prototype['eligibilityStatus'] = undefined;

/**
 * The list of error messages, if a device does not qualify as a failover target device.
 * @member {Array.<module:model/TargetEligibilityErrorMessage>} messages
 */
TargetEligibilityResult.prototype['messages'] = undefined;





/**
 * Allowed values for the <code>eligibilityStatus</code> property.
 * @enum {String}
 * @readonly
 */
TargetEligibilityResult['EligibilityStatusEnum'] = {

    /**
     * value: "NotEligible"
     * @const
     */
    "NotEligible": "NotEligible",

    /**
     * value: "Eligible"
     * @const
     */
    "Eligible": "Eligible"
};



export default TargetEligibilityResult;

