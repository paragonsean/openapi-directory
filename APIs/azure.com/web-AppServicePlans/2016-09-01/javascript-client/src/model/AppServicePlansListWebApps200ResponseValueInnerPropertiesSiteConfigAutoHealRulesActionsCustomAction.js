/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction model module.
 * @module model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction
 * @version 2016-09-01
 */
class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction {
    /**
     * Constructs a new <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction</code>.
     * Custom action to be executed when an auto heal rule is triggered.
     * @alias module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction
     */
    constructor() { 
        
        AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction} The populated <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction();

            if (data.hasOwnProperty('exe')) {
                obj['exe'] = ApiClient.convertToType(data['exe'], 'String');
            }
            if (data.hasOwnProperty('parameters')) {
                obj['parameters'] = ApiClient.convertToType(data['parameters'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['exe'] && !(typeof data['exe'] === 'string' || data['exe'] instanceof String)) {
            throw new Error("Expected the field `exe` to be a primitive type in the JSON string but got " + data['exe']);
        }
        // ensure the json data is a string
        if (data['parameters'] && !(typeof data['parameters'] === 'string' || data['parameters'] instanceof String)) {
            throw new Error("Expected the field `parameters` to be a primitive type in the JSON string but got " + data['parameters']);
        }

        return true;
    }


}



/**
 * Executable to be run.
 * @member {String} exe
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction.prototype['exe'] = undefined;

/**
 * Parameters for the executable.
 * @member {String} parameters
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction.prototype['parameters'] = undefined;






export default AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction;

