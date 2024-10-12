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
import AppLinkDataAppLinkInfo from './AppLinkDataAppLinkInfo';

/**
 * The AppLinkData model module.
 * @module model/AppLinkData
 * @version v1
 */
class AppLinkData {
    /**
     * Constructs a new <code>AppLinkData</code>.
     * @alias module:model/AppLinkData
     */
    constructor() { 
        
        AppLinkData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppLinkData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppLinkData} obj Optional instance to populate.
     * @return {module:model/AppLinkData} The populated <code>AppLinkData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppLinkData();

            if (data.hasOwnProperty('androidAppLinkInfo')) {
                obj['androidAppLinkInfo'] = AppLinkDataAppLinkInfo.constructFromObject(data['androidAppLinkInfo']);
            }
            if (data.hasOwnProperty('iosAppLinkInfo')) {
                obj['iosAppLinkInfo'] = AppLinkDataAppLinkInfo.constructFromObject(data['iosAppLinkInfo']);
            }
            if (data.hasOwnProperty('webAppLinkInfo')) {
                obj['webAppLinkInfo'] = AppLinkDataAppLinkInfo.constructFromObject(data['webAppLinkInfo']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppLinkData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppLinkData</code>.
     */
    static validateJSON(data) {
        // validate the optional field `androidAppLinkInfo`
        if (data['androidAppLinkInfo']) { // data not null
          AppLinkDataAppLinkInfo.validateJSON(data['androidAppLinkInfo']);
        }
        // validate the optional field `iosAppLinkInfo`
        if (data['iosAppLinkInfo']) { // data not null
          AppLinkDataAppLinkInfo.validateJSON(data['iosAppLinkInfo']);
        }
        // validate the optional field `webAppLinkInfo`
        if (data['webAppLinkInfo']) { // data not null
          AppLinkDataAppLinkInfo.validateJSON(data['webAppLinkInfo']);
        }

        return true;
    }


}



/**
 * @member {module:model/AppLinkDataAppLinkInfo} androidAppLinkInfo
 */
AppLinkData.prototype['androidAppLinkInfo'] = undefined;

/**
 * @member {module:model/AppLinkDataAppLinkInfo} iosAppLinkInfo
 */
AppLinkData.prototype['iosAppLinkInfo'] = undefined;

/**
 * @member {module:model/AppLinkDataAppLinkInfo} webAppLinkInfo
 */
AppLinkData.prototype['webAppLinkInfo'] = undefined;






export default AppLinkData;

