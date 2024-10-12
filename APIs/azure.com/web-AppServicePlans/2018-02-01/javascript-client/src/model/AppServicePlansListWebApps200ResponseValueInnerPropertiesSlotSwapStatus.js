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
 * The AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus model module.
 * @module model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus
 * @version 2018-02-01
 */
class AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus {
    /**
     * Constructs a new <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus</code>.
     * The status of the last successful slot swap operation.
     * @alias module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus
     */
    constructor() { 
        
        AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus} The populated <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus();

            if (data.hasOwnProperty('destinationSlotName')) {
                obj['destinationSlotName'] = ApiClient.convertToType(data['destinationSlotName'], 'String');
            }
            if (data.hasOwnProperty('sourceSlotName')) {
                obj['sourceSlotName'] = ApiClient.convertToType(data['sourceSlotName'], 'String');
            }
            if (data.hasOwnProperty('timestampUtc')) {
                obj['timestampUtc'] = ApiClient.convertToType(data['timestampUtc'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['destinationSlotName'] && !(typeof data['destinationSlotName'] === 'string' || data['destinationSlotName'] instanceof String)) {
            throw new Error("Expected the field `destinationSlotName` to be a primitive type in the JSON string but got " + data['destinationSlotName']);
        }
        // ensure the json data is a string
        if (data['sourceSlotName'] && !(typeof data['sourceSlotName'] === 'string' || data['sourceSlotName'] instanceof String)) {
            throw new Error("Expected the field `sourceSlotName` to be a primitive type in the JSON string but got " + data['sourceSlotName']);
        }

        return true;
    }


}



/**
 * The destination slot of the last swap operation.
 * @member {String} destinationSlotName
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus.prototype['destinationSlotName'] = undefined;

/**
 * The source slot of the last swap operation.
 * @member {String} sourceSlotName
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus.prototype['sourceSlotName'] = undefined;

/**
 * The time the last successful slot swap completed.
 * @member {Date} timestampUtc
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus.prototype['timestampUtc'] = undefined;






export default AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus;

