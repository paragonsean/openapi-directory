/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import LocalizedString from './LocalizedString';

/**
 * The EventSeat model module.
 * @module model/EventSeat
 * @version v1
 */
class EventSeat {
    /**
     * Constructs a new <code>EventSeat</code>.
     * @alias module:model/EventSeat
     */
    constructor() { 
        
        EventSeat.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EventSeat</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EventSeat} obj Optional instance to populate.
     * @return {module:model/EventSeat} The populated <code>EventSeat</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EventSeat();

            if (data.hasOwnProperty('gate')) {
                obj['gate'] = LocalizedString.constructFromObject(data['gate']);
            }
            if (data.hasOwnProperty('kind')) {
                obj['kind'] = ApiClient.convertToType(data['kind'], 'String');
            }
            if (data.hasOwnProperty('row')) {
                obj['row'] = LocalizedString.constructFromObject(data['row']);
            }
            if (data.hasOwnProperty('seat')) {
                obj['seat'] = LocalizedString.constructFromObject(data['seat']);
            }
            if (data.hasOwnProperty('section')) {
                obj['section'] = LocalizedString.constructFromObject(data['section']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EventSeat</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EventSeat</code>.
     */
    static validateJSON(data) {
        // validate the optional field `gate`
        if (data['gate']) { // data not null
          LocalizedString.validateJSON(data['gate']);
        }
        // ensure the json data is a string
        if (data['kind'] && !(typeof data['kind'] === 'string' || data['kind'] instanceof String)) {
            throw new Error("Expected the field `kind` to be a primitive type in the JSON string but got " + data['kind']);
        }
        // validate the optional field `row`
        if (data['row']) { // data not null
          LocalizedString.validateJSON(data['row']);
        }
        // validate the optional field `seat`
        if (data['seat']) { // data not null
          LocalizedString.validateJSON(data['seat']);
        }
        // validate the optional field `section`
        if (data['section']) { // data not null
          LocalizedString.validateJSON(data['section']);
        }

        return true;
    }


}



/**
 * @member {module:model/LocalizedString} gate
 */
EventSeat.prototype['gate'] = undefined;

/**
 * Identifies what kind of resource this is. Value: the fixed string `\"walletobjects#eventSeat\"`.
 * @member {String} kind
 */
EventSeat.prototype['kind'] = undefined;

/**
 * @member {module:model/LocalizedString} row
 */
EventSeat.prototype['row'] = undefined;

/**
 * @member {module:model/LocalizedString} seat
 */
EventSeat.prototype['seat'] = undefined;

/**
 * @member {module:model/LocalizedString} section
 */
EventSeat.prototype['section'] = undefined;






export default EventSeat;

