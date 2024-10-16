/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UniversalDoNotContact model module.
 * @module model/UniversalDoNotContact
 * @version V2
 */
class UniversalDoNotContact {
    /**
     * Constructs a new <code>UniversalDoNotContact</code>.
     * Represents a Universal (platform-wide) Do-Not-Contact object for a given phone number. Shows whether inbound/outbound actions are allowed for a given number.
     * @alias module:model/UniversalDoNotContact
     */
    constructor() { 
        
        UniversalDoNotContact.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UniversalDoNotContact</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UniversalDoNotContact} obj Optional instance to populate.
     * @return {module:model/UniversalDoNotContact} The populated <code>UniversalDoNotContact</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UniversalDoNotContact();

            if (data.hasOwnProperty('fromNumber')) {
                obj['fromNumber'] = ApiClient.convertToType(data['fromNumber'], 'String');
            }
            if (data.hasOwnProperty('inboundCall')) {
                obj['inboundCall'] = ApiClient.convertToType(data['inboundCall'], 'Boolean');
            }
            if (data.hasOwnProperty('inboundText')) {
                obj['inboundText'] = ApiClient.convertToType(data['inboundText'], 'Boolean');
            }
            if (data.hasOwnProperty('outboundCall')) {
                obj['outboundCall'] = ApiClient.convertToType(data['outboundCall'], 'Boolean');
            }
            if (data.hasOwnProperty('outboundText')) {
                obj['outboundText'] = ApiClient.convertToType(data['outboundText'], 'Boolean');
            }
            if (data.hasOwnProperty('toNumber')) {
                obj['toNumber'] = ApiClient.convertToType(data['toNumber'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UniversalDoNotContact</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UniversalDoNotContact</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['fromNumber'] && !(typeof data['fromNumber'] === 'string' || data['fromNumber'] instanceof String)) {
            throw new Error("Expected the field `fromNumber` to be a primitive type in the JSON string but got " + data['fromNumber']);
        }
        // ensure the json data is a string
        if (data['toNumber'] && !(typeof data['toNumber'] === 'string' || data['toNumber'] instanceof String)) {
            throw new Error("Expected the field `toNumber` to be a primitive type in the JSON string but got " + data['toNumber']);
        }

        return true;
    }


}



/**
 * Optional source number in E.164 format (11-digit). Example: 12132000384
 * @member {String} fromNumber
 */
UniversalDoNotContact.prototype['fromNumber'] = undefined;

/**
 * If toNumber can receive calls or If toNumber can call fromNumber.
 * @member {Boolean} inboundCall
 */
UniversalDoNotContact.prototype['inboundCall'] = undefined;

/**
 * If toNumber can receive texts or If toNumber can text fromNumber.
 * @member {Boolean} inboundText
 */
UniversalDoNotContact.prototype['inboundText'] = undefined;

/**
 * If toNumber can send calls or If fromNumber can call toNumber.
 * @member {Boolean} outboundCall
 */
UniversalDoNotContact.prototype['outboundCall'] = undefined;

/**
 * If toNumber can send texts or If fromNumber can text toNumber.
 * @member {Boolean} outboundText
 */
UniversalDoNotContact.prototype['outboundText'] = undefined;

/**
 * destination DNC number in E.164 format (11-digit). Example: 12132000384
 * @member {String} toNumber
 */
UniversalDoNotContact.prototype['toNumber'] = undefined;






export default UniversalDoNotContact;

