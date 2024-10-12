/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
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
import LocalizedString from './LocalizedString';

/**
 * The FrequentFlyerInfo model module.
 * @module model/FrequentFlyerInfo
 * @version v1
 */
class FrequentFlyerInfo {
    /**
     * Constructs a new <code>FrequentFlyerInfo</code>.
     * @alias module:model/FrequentFlyerInfo
     */
    constructor() { 
        
        FrequentFlyerInfo.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FrequentFlyerInfo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FrequentFlyerInfo} obj Optional instance to populate.
     * @return {module:model/FrequentFlyerInfo} The populated <code>FrequentFlyerInfo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FrequentFlyerInfo();

            if (data.hasOwnProperty('frequentFlyerNumber')) {
                obj['frequentFlyerNumber'] = ApiClient.convertToType(data['frequentFlyerNumber'], 'String');
            }
            if (data.hasOwnProperty('frequentFlyerProgramName')) {
                obj['frequentFlyerProgramName'] = LocalizedString.constructFromObject(data['frequentFlyerProgramName']);
            }
            if (data.hasOwnProperty('kind')) {
                obj['kind'] = ApiClient.convertToType(data['kind'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FrequentFlyerInfo</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FrequentFlyerInfo</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['frequentFlyerNumber'] && !(typeof data['frequentFlyerNumber'] === 'string' || data['frequentFlyerNumber'] instanceof String)) {
            throw new Error("Expected the field `frequentFlyerNumber` to be a primitive type in the JSON string but got " + data['frequentFlyerNumber']);
        }
        // validate the optional field `frequentFlyerProgramName`
        if (data['frequentFlyerProgramName']) { // data not null
          LocalizedString.validateJSON(data['frequentFlyerProgramName']);
        }
        // ensure the json data is a string
        if (data['kind'] && !(typeof data['kind'] === 'string' || data['kind'] instanceof String)) {
            throw new Error("Expected the field `kind` to be a primitive type in the JSON string but got " + data['kind']);
        }

        return true;
    }


}



/**
 * Frequent flyer number. Required for each nested object of kind `walletobjects#frequentFlyerInfo`.
 * @member {String} frequentFlyerNumber
 */
FrequentFlyerInfo.prototype['frequentFlyerNumber'] = undefined;

/**
 * @member {module:model/LocalizedString} frequentFlyerProgramName
 */
FrequentFlyerInfo.prototype['frequentFlyerProgramName'] = undefined;

/**
 * Identifies what kind of resource this is. Value: the fixed string `\"walletobjects#frequentFlyerInfo\"`.
 * @member {String} kind
 */
FrequentFlyerInfo.prototype['kind'] = undefined;






export default FrequentFlyerInfo;

