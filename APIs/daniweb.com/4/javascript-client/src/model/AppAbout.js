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
import AppAboutWebsite from './AppAboutWebsite';

/**
 * The AppAbout model module.
 * @module model/AppAbout
 * @version 4
 */
class AppAbout {
    /**
     * Constructs a new <code>AppAbout</code>.
     * @alias module:model/AppAbout
     */
    constructor() { 
        
        AppAbout.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppAbout</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppAbout} obj Optional instance to populate.
     * @return {module:model/AppAbout} The populated <code>AppAbout</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppAbout();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('website')) {
                obj['website'] = AppAboutWebsite.constructFromObject(data['website']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppAbout</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppAbout</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `website`
        if (data['website']) { // data not null
          AppAboutWebsite.validateJSON(data['website']);
        }

        return true;
    }


}



/**
 * @member {String} description
 */
AppAbout.prototype['description'] = undefined;

/**
 * @member {String} name
 */
AppAbout.prototype['name'] = undefined;

/**
 * @member {module:model/AppAboutWebsite} website
 */
AppAbout.prototype['website'] = undefined;






export default AppAbout;

