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
 * The ChartRowCol model module.
 * @module model/ChartRowCol
 * @version 0.1.0
 */
class ChartRowCol {
    /**
     * Constructs a new <code>ChartRowCol</code>.
     * @alias module:model/ChartRowCol
     */
    constructor() { 
        
        ChartRowCol.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ChartRowCol</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ChartRowCol} obj Optional instance to populate.
     * @return {module:model/ChartRowCol} The populated <code>ChartRowCol</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ChartRowCol();

            if (data.hasOwnProperty('colName')) {
                obj['colName'] = ApiClient.convertToType(data['colName'], 'String');
            }
            if (data.hasOwnProperty('colQualifiedAssy')) {
                obj['colQualifiedAssy'] = ApiClient.convertToType(data['colQualifiedAssy'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('rowName')) {
                obj['rowName'] = ApiClient.convertToType(data['rowName'], 'String');
            }
            if (data.hasOwnProperty('rowQualifedAssy')) {
                obj['rowQualifedAssy'] = ApiClient.convertToType(data['rowQualifedAssy'], 'String');
            }
            if (data.hasOwnProperty('typeId')) {
                obj['typeId'] = ApiClient.convertToType(data['typeId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ChartRowCol</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ChartRowCol</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['colName'] && !(typeof data['colName'] === 'string' || data['colName'] instanceof String)) {
            throw new Error("Expected the field `colName` to be a primitive type in the JSON string but got " + data['colName']);
        }
        // ensure the json data is a string
        if (data['colQualifiedAssy'] && !(typeof data['colQualifiedAssy'] === 'string' || data['colQualifiedAssy'] instanceof String)) {
            throw new Error("Expected the field `colQualifiedAssy` to be a primitive type in the JSON string but got " + data['colQualifiedAssy']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['rowName'] && !(typeof data['rowName'] === 'string' || data['rowName'] instanceof String)) {
            throw new Error("Expected the field `rowName` to be a primitive type in the JSON string but got " + data['rowName']);
        }
        // ensure the json data is a string
        if (data['rowQualifedAssy'] && !(typeof data['rowQualifedAssy'] === 'string' || data['rowQualifedAssy'] instanceof String)) {
            throw new Error("Expected the field `rowQualifedAssy` to be a primitive type in the JSON string but got " + data['rowQualifedAssy']);
        }

        return true;
    }


}



/**
 * @member {String} colName
 */
ChartRowCol.prototype['colName'] = undefined;

/**
 * @member {String} colQualifiedAssy
 */
ChartRowCol.prototype['colQualifiedAssy'] = undefined;

/**
 * @member {String} id
 */
ChartRowCol.prototype['id'] = undefined;

/**
 * @member {String} rowName
 */
ChartRowCol.prototype['rowName'] = undefined;

/**
 * @member {String} rowQualifedAssy
 */
ChartRowCol.prototype['rowQualifedAssy'] = undefined;

/**
 * @member {Number} typeId
 */
ChartRowCol.prototype['typeId'] = undefined;






export default ChartRowCol;

