/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import MeBusinessCardWebsite from './MeBusinessCardWebsite';

/**
 * The MeBusinessCard model module.
 * @module model/MeBusinessCard
 * @version 4
 */
class MeBusinessCard {
    /**
     * Constructs a new <code>MeBusinessCard</code>.
     * @alias module:model/MeBusinessCard
     */
    constructor() { 
        
        MeBusinessCard.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>MeBusinessCard</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MeBusinessCard} obj Optional instance to populate.
     * @return {module:model/MeBusinessCard} The populated <code>MeBusinessCard</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MeBusinessCard();

            if (data.hasOwnProperty('company_name')) {
                obj['company_name'] = ApiClient.convertToType(data['company_name'], 'String');
            }
            if (data.hasOwnProperty('company_size')) {
                obj['company_size'] = ApiClient.convertToType(data['company_size'], 'String');
            }
            if (data.hasOwnProperty('headline')) {
                obj['headline'] = ApiClient.convertToType(data['headline'], 'String');
            }
            if (data.hasOwnProperty('industry')) {
                obj['industry'] = ApiClient.convertToType(data['industry'], 'String');
            }
            if (data.hasOwnProperty('interest_tags')) {
                obj['interest_tags'] = ApiClient.convertToType(data['interest_tags'], ['String']);
            }
            if (data.hasOwnProperty('job_position')) {
                obj['job_position'] = ApiClient.convertToType(data['job_position'], 'String');
            }
            if (data.hasOwnProperty('summary')) {
                obj['summary'] = ApiClient.convertToType(data['summary'], 'String');
            }
            if (data.hasOwnProperty('website')) {
                obj['website'] = MeBusinessCardWebsite.constructFromObject(data['website']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MeBusinessCard</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MeBusinessCard</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['company_name'] && !(typeof data['company_name'] === 'string' || data['company_name'] instanceof String)) {
            throw new Error("Expected the field `company_name` to be a primitive type in the JSON string but got " + data['company_name']);
        }
        // ensure the json data is a string
        if (data['company_size'] && !(typeof data['company_size'] === 'string' || data['company_size'] instanceof String)) {
            throw new Error("Expected the field `company_size` to be a primitive type in the JSON string but got " + data['company_size']);
        }
        // ensure the json data is a string
        if (data['headline'] && !(typeof data['headline'] === 'string' || data['headline'] instanceof String)) {
            throw new Error("Expected the field `headline` to be a primitive type in the JSON string but got " + data['headline']);
        }
        // ensure the json data is a string
        if (data['industry'] && !(typeof data['industry'] === 'string' || data['industry'] instanceof String)) {
            throw new Error("Expected the field `industry` to be a primitive type in the JSON string but got " + data['industry']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['interest_tags'])) {
            throw new Error("Expected the field `interest_tags` to be an array in the JSON data but got " + data['interest_tags']);
        }
        // ensure the json data is a string
        if (data['job_position'] && !(typeof data['job_position'] === 'string' || data['job_position'] instanceof String)) {
            throw new Error("Expected the field `job_position` to be a primitive type in the JSON string but got " + data['job_position']);
        }
        // ensure the json data is a string
        if (data['summary'] && !(typeof data['summary'] === 'string' || data['summary'] instanceof String)) {
            throw new Error("Expected the field `summary` to be a primitive type in the JSON string but got " + data['summary']);
        }
        // validate the optional field `website`
        if (data['website']) { // data not null
          MeBusinessCardWebsite.validateJSON(data['website']);
        }

        return true;
    }


}



/**
 * @member {String} company_name
 */
MeBusinessCard.prototype['company_name'] = undefined;

/**
 * @member {String} company_size
 */
MeBusinessCard.prototype['company_size'] = undefined;

/**
 * @member {String} headline
 */
MeBusinessCard.prototype['headline'] = undefined;

/**
 * @member {String} industry
 */
MeBusinessCard.prototype['industry'] = undefined;

/**
 * @member {Array.<String>} interest_tags
 */
MeBusinessCard.prototype['interest_tags'] = undefined;

/**
 * @member {String} job_position
 */
MeBusinessCard.prototype['job_position'] = undefined;

/**
 * @member {String} summary
 */
MeBusinessCard.prototype['summary'] = undefined;

/**
 * @member {module:model/MeBusinessCardWebsite} website
 */
MeBusinessCard.prototype['website'] = undefined;






export default MeBusinessCard;

