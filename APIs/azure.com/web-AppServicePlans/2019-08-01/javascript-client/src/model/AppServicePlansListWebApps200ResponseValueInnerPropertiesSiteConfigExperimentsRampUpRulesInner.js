/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner model module.
 * @module model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner
 * @version 2019-08-01
 */
class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner {
    /**
     * Constructs a new <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner</code>.
     * Routing rules for ramp up testing. This rule allows to redirect static traffic % to a slot or to gradually change routing % based on performance.
     * @alias module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner
     */
    constructor() { 
        
        AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner} The populated <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner();

            if (data.hasOwnProperty('actionHostName')) {
                obj['actionHostName'] = ApiClient.convertToType(data['actionHostName'], 'String');
            }
            if (data.hasOwnProperty('changeDecisionCallbackUrl')) {
                obj['changeDecisionCallbackUrl'] = ApiClient.convertToType(data['changeDecisionCallbackUrl'], 'String');
            }
            if (data.hasOwnProperty('changeIntervalInMinutes')) {
                obj['changeIntervalInMinutes'] = ApiClient.convertToType(data['changeIntervalInMinutes'], 'Number');
            }
            if (data.hasOwnProperty('changeStep')) {
                obj['changeStep'] = ApiClient.convertToType(data['changeStep'], 'Number');
            }
            if (data.hasOwnProperty('maxReroutePercentage')) {
                obj['maxReroutePercentage'] = ApiClient.convertToType(data['maxReroutePercentage'], 'Number');
            }
            if (data.hasOwnProperty('minReroutePercentage')) {
                obj['minReroutePercentage'] = ApiClient.convertToType(data['minReroutePercentage'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('reroutePercentage')) {
                obj['reroutePercentage'] = ApiClient.convertToType(data['reroutePercentage'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['actionHostName'] && !(typeof data['actionHostName'] === 'string' || data['actionHostName'] instanceof String)) {
            throw new Error("Expected the field `actionHostName` to be a primitive type in the JSON string but got " + data['actionHostName']);
        }
        // ensure the json data is a string
        if (data['changeDecisionCallbackUrl'] && !(typeof data['changeDecisionCallbackUrl'] === 'string' || data['changeDecisionCallbackUrl'] instanceof String)) {
            throw new Error("Expected the field `changeDecisionCallbackUrl` to be a primitive type in the JSON string but got " + data['changeDecisionCallbackUrl']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * Hostname of a slot to which the traffic will be redirected if decided to. E.g. myapp-stage.azurewebsites.net.
 * @member {String} actionHostName
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner.prototype['actionHostName'] = undefined;

/**
 * Custom decision algorithm can be provided in TiPCallback site extension which URL can be specified. See TiPCallback site extension for the scaffold and contracts. https://www.siteextensions.net/packages/TiPCallback/
 * @member {String} changeDecisionCallbackUrl
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner.prototype['changeDecisionCallbackUrl'] = undefined;

/**
 * Specifies interval in minutes to reevaluate ReroutePercentage.
 * @member {Number} changeIntervalInMinutes
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner.prototype['changeIntervalInMinutes'] = undefined;

/**
 * In auto ramp up scenario this is the step to add/remove from <code>ReroutePercentage</code> until it reaches \\n<code>MinReroutePercentage</code> or  <code>MaxReroutePercentage</code>. Site metrics are checked every N minutes specified in <code>ChangeIntervalInMinutes</code>.\\nCustom decision algorithm  can be provided in TiPCallback site extension which URL can be specified in <code>ChangeDecisionCallbackUrl</code>.
 * @member {Number} changeStep
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner.prototype['changeStep'] = undefined;

/**
 * Specifies upper boundary below which ReroutePercentage will stay.
 * @member {Number} maxReroutePercentage
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner.prototype['maxReroutePercentage'] = undefined;

/**
 * Specifies lower boundary above which ReroutePercentage will stay.
 * @member {Number} minReroutePercentage
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner.prototype['minReroutePercentage'] = undefined;

/**
 * Name of the routing rule. The recommended name would be to point to the slot which will receive the traffic in the experiment.
 * @member {String} name
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner.prototype['name'] = undefined;

/**
 * Percentage of the traffic which will be redirected to <code>ActionHostName</code>.
 * @member {Number} reroutePercentage
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner.prototype['reroutePercentage'] = undefined;






export default AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner;

