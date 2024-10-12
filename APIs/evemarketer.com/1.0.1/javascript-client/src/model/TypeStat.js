/**
 * EVEMarketer Marketstat API
 * EVEMarketer Marketstat API is almost compatible with EVE-Central's Marketstat API.
 *
 * The version of the OpenAPI document: 1.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ForQuery from './ForQuery';

/**
 * The TypeStat model module.
 * @module model/TypeStat
 * @version 1.0.1
 */
class TypeStat {
    /**
     * Constructs a new <code>TypeStat</code>.
     * @alias module:model/TypeStat
     */
    constructor() { 
        
        TypeStat.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TypeStat</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TypeStat} obj Optional instance to populate.
     * @return {module:model/TypeStat} The populated <code>TypeStat</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TypeStat();

            if (data.hasOwnProperty('avg')) {
                obj['avg'] = ApiClient.convertToType(data['avg'], 'Number');
            }
            if (data.hasOwnProperty('fivePercent')) {
                obj['fivePercent'] = ApiClient.convertToType(data['fivePercent'], 'Number');
            }
            if (data.hasOwnProperty('forQuery')) {
                obj['forQuery'] = ForQuery.constructFromObject(data['forQuery']);
            }
            if (data.hasOwnProperty('generated')) {
                obj['generated'] = ApiClient.convertToType(data['generated'], 'Number');
            }
            if (data.hasOwnProperty('highToLow')) {
                obj['highToLow'] = ApiClient.convertToType(data['highToLow'], 'Boolean');
            }
            if (data.hasOwnProperty('max')) {
                obj['max'] = ApiClient.convertToType(data['max'], 'Number');
            }
            if (data.hasOwnProperty('median')) {
                obj['median'] = ApiClient.convertToType(data['median'], 'Number');
            }
            if (data.hasOwnProperty('min')) {
                obj['min'] = ApiClient.convertToType(data['min'], 'Number');
            }
            if (data.hasOwnProperty('stdDev')) {
                obj['stdDev'] = ApiClient.convertToType(data['stdDev'], 'Number');
            }
            if (data.hasOwnProperty('variance')) {
                obj['variance'] = ApiClient.convertToType(data['variance'], 'Number');
            }
            if (data.hasOwnProperty('volume')) {
                obj['volume'] = ApiClient.convertToType(data['volume'], 'Number');
            }
            if (data.hasOwnProperty('wavg')) {
                obj['wavg'] = ApiClient.convertToType(data['wavg'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TypeStat</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TypeStat</code>.
     */
    static validateJSON(data) {
        // validate the optional field `forQuery`
        if (data['forQuery']) { // data not null
          ForQuery.validateJSON(data['forQuery']);
        }

        return true;
    }


}



/**
 * Average Price
 * @member {Number} avg
 */
TypeStat.prototype['avg'] = undefined;

/**
 * @member {Number} fivePercent
 */
TypeStat.prototype['fivePercent'] = undefined;

/**
 * @member {module:model/ForQuery} forQuery
 */
TypeStat.prototype['forQuery'] = undefined;

/**
 * Generated at (UNIX Timestamp msec)
 * @member {Number} generated
 */
TypeStat.prototype['generated'] = undefined;

/**
 * @member {Boolean} highToLow
 */
TypeStat.prototype['highToLow'] = undefined;

/**
 * @member {Number} max
 */
TypeStat.prototype['max'] = undefined;

/**
 * Median Price
 * @member {Number} median
 */
TypeStat.prototype['median'] = undefined;

/**
 * @member {Number} min
 */
TypeStat.prototype['min'] = undefined;

/**
 * Standard Deviation
 * @member {Number} stdDev
 */
TypeStat.prototype['stdDev'] = undefined;

/**
 * @member {Number} variance
 */
TypeStat.prototype['variance'] = undefined;

/**
 * Order Volume
 * @member {Number} volume
 */
TypeStat.prototype['volume'] = undefined;

/**
 * Weighted Average Price
 * @member {Number} wavg
 */
TypeStat.prototype['wavg'] = undefined;






export default TypeStat;

