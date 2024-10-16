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
import Call from './Call';
import Text from './Text';

/**
 * The ContactHistory model module.
 * @module model/ContactHistory
 * @version V2
 */
class ContactHistory {
    /**
     * Constructs a new <code>ContactHistory</code>.
     * Contains history of all calls and texts addressed to a given contact
     * @alias module:model/ContactHistory
     */
    constructor() { 
        
        ContactHistory.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ContactHistory</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ContactHistory} obj Optional instance to populate.
     * @return {module:model/ContactHistory} The populated <code>ContactHistory</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ContactHistory();

            if (data.hasOwnProperty('calls')) {
                obj['calls'] = ApiClient.convertToType(data['calls'], [Call]);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('texts')) {
                obj['texts'] = ApiClient.convertToType(data['texts'], [Text]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ContactHistory</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ContactHistory</code>.
     */
    static validateJSON(data) {
        if (data['calls']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['calls'])) {
                throw new Error("Expected the field `calls` to be an array in the JSON data but got " + data['calls']);
            }
            // validate the optional field `calls` (array)
            for (const item of data['calls']) {
                Call.validateJSON(item);
            };
        }
        if (data['texts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['texts'])) {
                throw new Error("Expected the field `texts` to be an array in the JSON data but got " + data['texts']);
            }
            // validate the optional field `texts` (array)
            for (const item of data['texts']) {
                Text.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * List of Call objects addressed to a given contact
 * @member {Array.<module:model/Call>} calls
 */
ContactHistory.prototype['calls'] = undefined;

/**
 * An id of a contact
 * @member {Number} id
 */
ContactHistory.prototype['id'] = undefined;

/**
 * List of Text objects addressed to a given contact
 * @member {Array.<module:model/Text>} texts
 */
ContactHistory.prototype['texts'] = undefined;






export default ContactHistory;

