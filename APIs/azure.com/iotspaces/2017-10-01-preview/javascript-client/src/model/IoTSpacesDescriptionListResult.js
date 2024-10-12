/**
 * IoTSpacesClient
 * Use this API to manage the IoTSpaces service instances in your Azure subscription.
 *
 * The version of the OpenAPI document: 2017-10-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import IoTSpacesDescription from './IoTSpacesDescription';

/**
 * The IoTSpacesDescriptionListResult model module.
 * @module model/IoTSpacesDescriptionListResult
 * @version 2017-10-01-preview
 */
class IoTSpacesDescriptionListResult {
    /**
     * Constructs a new <code>IoTSpacesDescriptionListResult</code>.
     * A list of IoTSpaces description objects with a next link.
     * @alias module:model/IoTSpacesDescriptionListResult
     */
    constructor() { 
        
        IoTSpacesDescriptionListResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IoTSpacesDescriptionListResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IoTSpacesDescriptionListResult} obj Optional instance to populate.
     * @return {module:model/IoTSpacesDescriptionListResult} The populated <code>IoTSpacesDescriptionListResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IoTSpacesDescriptionListResult();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [IoTSpacesDescription]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IoTSpacesDescriptionListResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IoTSpacesDescriptionListResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['nextLink'] && !(typeof data['nextLink'] === 'string' || data['nextLink'] instanceof String)) {
            throw new Error("Expected the field `nextLink` to be a primitive type in the JSON string but got " + data['nextLink']);
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                IoTSpacesDescription.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * The link used to get the next page of IoTSpaces description objects.
 * @member {String} nextLink
 */
IoTSpacesDescriptionListResult.prototype['nextLink'] = undefined;

/**
 * A list of IoTSpaces description objects.
 * @member {Array.<module:model/IoTSpacesDescription>} value
 */
IoTSpacesDescriptionListResult.prototype['value'] = undefined;






export default IoTSpacesDescriptionListResult;

