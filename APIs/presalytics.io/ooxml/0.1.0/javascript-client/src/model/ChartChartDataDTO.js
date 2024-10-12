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
 * The ChartChartDataDTO model module.
 * @module model/ChartChartDataDTO
 * @version 0.1.0
 */
class ChartChartDataDTO {
    /**
     * Constructs a new <code>ChartChartDataDTO</code>.
     * @alias module:model/ChartChartDataDTO
     */
    constructor() { 
        
        ChartChartDataDTO.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ChartChartDataDTO</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ChartChartDataDTO} obj Optional instance to populate.
     * @return {module:model/ChartChartDataDTO} The populated <code>ChartChartDataDTO</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ChartChartDataDTO();

            if (data.hasOwnProperty('categoryNames')) {
                obj['categoryNames'] = ApiClient.convertToType(data['categoryNames'], ['String']);
            }
            if (data.hasOwnProperty('chartId')) {
                obj['chartId'] = ApiClient.convertToType(data['chartId'], 'String');
            }
            if (data.hasOwnProperty('dataPoints')) {
                obj['dataPoints'] = ApiClient.convertToType(data['dataPoints'], [['Number']]);
            }
            if (data.hasOwnProperty('seriesNames')) {
                obj['seriesNames'] = ApiClient.convertToType(data['seriesNames'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ChartChartDataDTO</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ChartChartDataDTO</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['categoryNames'])) {
            throw new Error("Expected the field `categoryNames` to be an array in the JSON data but got " + data['categoryNames']);
        }
        // ensure the json data is a string
        if (data['chartId'] && !(typeof data['chartId'] === 'string' || data['chartId'] instanceof String)) {
            throw new Error("Expected the field `chartId` to be a primitive type in the JSON string but got " + data['chartId']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['dataPoints'])) {
            throw new Error("Expected the field `dataPoints` to be an array in the JSON data but got " + data['dataPoints']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['seriesNames'])) {
            throw new Error("Expected the field `seriesNames` to be an array in the JSON data but got " + data['seriesNames']);
        }

        return true;
    }


}



/**
 * @member {Array.<String>} categoryNames
 */
ChartChartDataDTO.prototype['categoryNames'] = undefined;

/**
 * @member {String} chartId
 */
ChartChartDataDTO.prototype['chartId'] = undefined;

/**
 * @member {Array.<Array.<Number>>} dataPoints
 */
ChartChartDataDTO.prototype['dataPoints'] = undefined;

/**
 * @member {Array.<String>} seriesNames
 */
ChartChartDataDTO.prototype['seriesNames'] = undefined;






export default ChartChartDataDTO;

