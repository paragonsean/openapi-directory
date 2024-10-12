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
import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions from './AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions';
import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers from './AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers';

/**
 * The AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules model module.
 * @module model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules
 * @version 2016-09-01
 */
class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules {
    /**
     * Constructs a new <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules</code>.
     * Rules that can be defined for auto-heal.
     * @alias module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules
     */
    constructor() { 
        
        AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules} The populated <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules();

            if (data.hasOwnProperty('actions')) {
                obj['actions'] = AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions.constructFromObject(data['actions']);
            }
            if (data.hasOwnProperty('triggers')) {
                obj['triggers'] = AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.constructFromObject(data['triggers']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules</code>.
     */
    static validateJSON(data) {
        // validate the optional field `actions`
        if (data['actions']) { // data not null
          AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions.validateJSON(data['actions']);
        }
        // validate the optional field `triggers`
        if (data['triggers']) { // data not null
          AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.validateJSON(data['triggers']);
        }

        return true;
    }


}



/**
 * @member {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions} actions
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules.prototype['actions'] = undefined;

/**
 * @member {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers} triggers
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules.prototype['triggers'] = undefined;






export default AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules;

