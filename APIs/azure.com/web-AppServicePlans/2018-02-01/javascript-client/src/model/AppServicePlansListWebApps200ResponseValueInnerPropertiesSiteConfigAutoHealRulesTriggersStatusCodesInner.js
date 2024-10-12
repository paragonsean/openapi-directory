/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner model module.
 * @module model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner
 * @version 2018-02-01
 */
class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner {
    /**
     * Constructs a new <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner</code>.
     * Trigger based on status code.
     * @alias module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner
     */
    constructor() { 
        
        AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner} The populated <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner();

            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'Number');
            }
            if (data.hasOwnProperty('subStatus')) {
                obj['subStatus'] = ApiClient.convertToType(data['subStatus'], 'Number');
            }
            if (data.hasOwnProperty('timeInterval')) {
                obj['timeInterval'] = ApiClient.convertToType(data['timeInterval'], 'String');
            }
            if (data.hasOwnProperty('win32Status')) {
                obj['win32Status'] = ApiClient.convertToType(data['win32Status'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['timeInterval'] && !(typeof data['timeInterval'] === 'string' || data['timeInterval'] instanceof String)) {
            throw new Error("Expected the field `timeInterval` to be a primitive type in the JSON string but got " + data['timeInterval']);
        }

        return true;
    }


}



/**
 * Request Count.
 * @member {Number} count
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner.prototype['count'] = undefined;

/**
 * HTTP status code.
 * @member {Number} status
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner.prototype['status'] = undefined;

/**
 * Request Sub Status.
 * @member {Number} subStatus
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner.prototype['subStatus'] = undefined;

/**
 * Time interval.
 * @member {String} timeInterval
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner.prototype['timeInterval'] = undefined;

/**
 * Win32 error code.
 * @member {Number} win32Status
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner.prototype['win32Status'] = undefined;






export default AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner;

