/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BreakoutVO from './BreakoutVO';
import PropertyPaAndAttVO from './PropertyPaAndAttVO';

/**
 * The QuotePriceDetailVO model module.
 * @module model/QuotePriceDetailVO
 * @version 1.0
 */
class QuotePriceDetailVO {
    /**
     * Constructs a new <code>QuotePriceDetailVO</code>.
     * Java type: com.noosh.nooshapi.vo.QuotePriceDetailVO
     * @alias module:model/QuotePriceDetailVO
     */
    constructor() { 
        
        QuotePriceDetailVO.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>QuotePriceDetailVO</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/QuotePriceDetailVO} obj Optional instance to populate.
     * @return {module:model/QuotePriceDetailVO} The populated <code>QuotePriceDetailVO</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new QuotePriceDetailVO();

            if (data.hasOwnProperty('breakouts')) {
                obj['breakouts'] = ApiClient.convertToType(data['breakouts'], [BreakoutVO]);
            }
            if (data.hasOwnProperty('cost')) {
                obj['cost'] = ApiClient.convertToType(data['cost'], Object);
            }
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], [PropertyPaAndAttVO]);
            }
            if (data.hasOwnProperty('fixed')) {
                obj['fixed'] = ApiClient.convertToType(data['fixed'], Object);
            }
            if (data.hasOwnProperty('is_chosen')) {
                obj['is_chosen'] = ApiClient.convertToType(data['is_chosen'], 'Boolean');
            }
            if (data.hasOwnProperty('is_included')) {
                obj['is_included'] = ApiClient.convertToType(data['is_included'], 'Boolean');
            }
            if (data.hasOwnProperty('is_quoted')) {
                obj['is_quoted'] = ApiClient.convertToType(data['is_quoted'], 'Boolean');
            }
            if (data.hasOwnProperty('parent_price_id')) {
                obj['parent_price_id'] = ApiClient.convertToType(data['parent_price_id'], 'Number');
            }
            if (data.hasOwnProperty('price_id')) {
                obj['price_id'] = ApiClient.convertToType(data['price_id'], 'Number');
            }
            if (data.hasOwnProperty('quantity')) {
                obj['quantity'] = ApiClient.convertToType(data['quantity'], Object);
            }
            if (data.hasOwnProperty('sell_price')) {
                obj['sell_price'] = ApiClient.convertToType(data['sell_price'], Object);
            }
            if (data.hasOwnProperty('shipping')) {
                obj['shipping'] = ApiClient.convertToType(data['shipping'], Object);
            }
            if (data.hasOwnProperty('source')) {
                obj['source'] = ApiClient.convertToType(data['source'], Object);
            }
            if (data.hasOwnProperty('supplier')) {
                obj['supplier'] = ApiClient.convertToType(data['supplier'], 'String');
            }
            if (data.hasOwnProperty('tax')) {
                obj['tax'] = ApiClient.convertToType(data['tax'], Object);
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], Object);
            }
            if (data.hasOwnProperty('transactional_cost')) {
                obj['transactional_cost'] = ApiClient.convertToType(data['transactional_cost'], Object);
            }
            if (data.hasOwnProperty('transactional_fixed')) {
                obj['transactional_fixed'] = ApiClient.convertToType(data['transactional_fixed'], Object);
            }
            if (data.hasOwnProperty('transactional_sell_price')) {
                obj['transactional_sell_price'] = ApiClient.convertToType(data['transactional_sell_price'], Object);
            }
            if (data.hasOwnProperty('transactional_shipping')) {
                obj['transactional_shipping'] = ApiClient.convertToType(data['transactional_shipping'], Object);
            }
            if (data.hasOwnProperty('transactional_tax')) {
                obj['transactional_tax'] = ApiClient.convertToType(data['transactional_tax'], Object);
            }
            if (data.hasOwnProperty('transactional_total')) {
                obj['transactional_total'] = ApiClient.convertToType(data['transactional_total'], Object);
            }
            if (data.hasOwnProperty('transactional_variable')) {
                obj['transactional_variable'] = ApiClient.convertToType(data['transactional_variable'], Object);
            }
            if (data.hasOwnProperty('variable')) {
                obj['variable'] = ApiClient.convertToType(data['variable'], Object);
            }
            if (data.hasOwnProperty('variable_percent')) {
                obj['variable_percent'] = ApiClient.convertToType(data['variable_percent'], Object);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>QuotePriceDetailVO</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>QuotePriceDetailVO</code>.
     */
    static validateJSON(data) {
        if (data['breakouts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['breakouts'])) {
                throw new Error("Expected the field `breakouts` to be an array in the JSON data but got " + data['breakouts']);
            }
            // validate the optional field `breakouts` (array)
            for (const item of data['breakouts']) {
                BreakoutVO.validateJSON(item);
            };
        }
        if (data['custom_fields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['custom_fields'])) {
                throw new Error("Expected the field `custom_fields` to be an array in the JSON data but got " + data['custom_fields']);
            }
            // validate the optional field `custom_fields` (array)
            for (const item of data['custom_fields']) {
                PropertyPaAndAttVO.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['supplier'] && !(typeof data['supplier'] === 'string' || data['supplier'] instanceof String)) {
            throw new Error("Expected the field `supplier` to be a primitive type in the JSON string but got " + data['supplier']);
        }

        return true;
    }


}



/**
 * 
 * @member {Array.<module:model/BreakoutVO>} breakouts
 */
QuotePriceDetailVO.prototype['breakouts'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} cost
 */
QuotePriceDetailVO.prototype['cost'] = undefined;

/**
 * 
 * @member {Array.<module:model/PropertyPaAndAttVO>} custom_fields
 */
QuotePriceDetailVO.prototype['custom_fields'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} fixed
 */
QuotePriceDetailVO.prototype['fixed'] = undefined;

/**
 * 
 * @member {Boolean} is_chosen
 */
QuotePriceDetailVO.prototype['is_chosen'] = undefined;

/**
 * 
 * @member {Boolean} is_included
 */
QuotePriceDetailVO.prototype['is_included'] = undefined;

/**
 * 
 * @member {Boolean} is_quoted
 */
QuotePriceDetailVO.prototype['is_quoted'] = undefined;

/**
 * 
 * @member {Number} parent_price_id
 */
QuotePriceDetailVO.prototype['parent_price_id'] = undefined;

/**
 * 
 * @member {Number} price_id
 */
QuotePriceDetailVO.prototype['price_id'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} quantity
 */
QuotePriceDetailVO.prototype['quantity'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} sell_price
 */
QuotePriceDetailVO.prototype['sell_price'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} shipping
 */
QuotePriceDetailVO.prototype['shipping'] = undefined;

/**
 * Java type: com.noosh.nooshapi.vo.QuotePriceSourceVO
 * @member {Object} source
 */
QuotePriceDetailVO.prototype['source'] = undefined;

/**
 * 
 * @member {String} supplier
 */
QuotePriceDetailVO.prototype['supplier'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} tax
 */
QuotePriceDetailVO.prototype['tax'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} total
 */
QuotePriceDetailVO.prototype['total'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} transactional_cost
 */
QuotePriceDetailVO.prototype['transactional_cost'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} transactional_fixed
 */
QuotePriceDetailVO.prototype['transactional_fixed'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} transactional_sell_price
 */
QuotePriceDetailVO.prototype['transactional_sell_price'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} transactional_shipping
 */
QuotePriceDetailVO.prototype['transactional_shipping'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} transactional_tax
 */
QuotePriceDetailVO.prototype['transactional_tax'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} transactional_total
 */
QuotePriceDetailVO.prototype['transactional_total'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} transactional_variable
 */
QuotePriceDetailVO.prototype['transactional_variable'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} variable
 */
QuotePriceDetailVO.prototype['variable'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} variable_percent
 */
QuotePriceDetailVO.prototype['variable_percent'] = undefined;






export default QuotePriceDetailVO;

