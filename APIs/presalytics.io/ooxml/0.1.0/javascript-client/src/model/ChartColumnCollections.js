/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ChartColumnCollections model module.
 * @module model/ChartColumnCollections
 * @version 0.1.0
 */
class ChartColumnCollections {
    /**
     * Constructs a new <code>ChartColumnCollections</code>.
     * @alias module:model/ChartColumnCollections
     */
    constructor() { 
        
        ChartColumnCollections.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ChartColumnCollections</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ChartColumnCollections} obj Optional instance to populate.
     * @return {module:model/ChartColumnCollections} The populated <code>ChartColumnCollections</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ChartColumnCollections();

            if (data.hasOwnProperty('chartDataId')) {
                obj['chartDataId'] = ApiClient.convertToType(data['chartDataId'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ChartColumnCollections</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ChartColumnCollections</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['chartDataId'] && !(typeof data['chartDataId'] === 'string' || data['chartDataId'] instanceof String)) {
            throw new Error("Expected the field `chartDataId` to be a primitive type in the JSON string but got " + data['chartDataId']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}



/**
 * @member {String} chartDataId
 */
ChartColumnCollections.prototype['chartDataId'] = undefined;

/**
 * @member {String} id
 */
ChartColumnCollections.prototype['id'] = undefined;






export default ChartColumnCollections;

