/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Description from './Description';

/**
 * The TermAndCondition model module.
 * @module model/TermAndCondition
 * @version 2.0.2
 */
class TermAndCondition {
    /**
     * Constructs a new <code>TermAndCondition</code>.
     * @alias module:model/TermAndCondition
     */
    constructor() { 
        
        TermAndCondition.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TermAndCondition</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TermAndCondition} obj Optional instance to populate.
     * @return {module:model/TermAndCondition} The populated <code>TermAndCondition</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TermAndCondition();

            if (data.hasOwnProperty('category')) {
                obj['category'] = ApiClient.convertToType(data['category'], 'String');
            }
            if (data.hasOwnProperty('circumstances')) {
                obj['circumstances'] = ApiClient.convertToType(data['circumstances'], 'String');
            }
            if (data.hasOwnProperty('descriptions')) {
                obj['descriptions'] = ApiClient.convertToType(data['descriptions'], [Description]);
            }
            if (data.hasOwnProperty('maxPenaltyAmount')) {
                obj['maxPenaltyAmount'] = ApiClient.convertToType(data['maxPenaltyAmount'], 'String');
            }
            if (data.hasOwnProperty('notApplicable')) {
                obj['notApplicable'] = ApiClient.convertToType(data['notApplicable'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TermAndCondition</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TermAndCondition</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['category'] && !(typeof data['category'] === 'string' || data['category'] instanceof String)) {
            throw new Error("Expected the field `category` to be a primitive type in the JSON string but got " + data['category']);
        }
        // ensure the json data is a string
        if (data['circumstances'] && !(typeof data['circumstances'] === 'string' || data['circumstances'] instanceof String)) {
            throw new Error("Expected the field `circumstances` to be a primitive type in the JSON string but got " + data['circumstances']);
        }
        if (data['descriptions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['descriptions'])) {
                throw new Error("Expected the field `descriptions` to be an array in the JSON data but got " + data['descriptions']);
            }
            // validate the optional field `descriptions` (array)
            for (const item of data['descriptions']) {
                Description.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['maxPenaltyAmount'] && !(typeof data['maxPenaltyAmount'] === 'string' || data['maxPenaltyAmount'] instanceof String)) {
            throw new Error("Expected the field `maxPenaltyAmount` to be a primitive type in the JSON string but got " + data['maxPenaltyAmount']);
        }

        return true;
    }


}



/**
 * This defines what type of modification is concerned in this rule.
 * @member {module:model/TermAndCondition.CategoryEnum} category
 */
TermAndCondition.prototype['category'] = undefined;

/**
 * @member {String} circumstances
 */
TermAndCondition.prototype['circumstances'] = undefined;

/**
 * @member {Array.<module:model/Description>} descriptions
 */
TermAndCondition.prototype['descriptions'] = undefined;

/**
 * @member {String} maxPenaltyAmount
 */
TermAndCondition.prototype['maxPenaltyAmount'] = undefined;

/**
 * @member {Boolean} notApplicable
 */
TermAndCondition.prototype['notApplicable'] = undefined;





/**
 * Allowed values for the <code>category</code> property.
 * @enum {String}
 * @readonly
 */
TermAndCondition['CategoryEnum'] = {

    /**
     * value: "REFUND"
     * @const
     */
    "REFUND": "REFUND",

    /**
     * value: "EXCHANGE"
     * @const
     */
    "EXCHANGE": "EXCHANGE",

    /**
     * value: "REVALIDATION"
     * @const
     */
    "REVALIDATION": "REVALIDATION",

    /**
     * value: "REISSUE"
     * @const
     */
    "REISSUE": "REISSUE",

    /**
     * value: "REBOOK"
     * @const
     */
    "REBOOK": "REBOOK",

    /**
     * value: "CANCELLATION"
     * @const
     */
    "CANCELLATION": "CANCELLATION"
};



export default TermAndCondition;

