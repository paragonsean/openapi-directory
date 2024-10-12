/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The BlacklistItemInsertVersion model module.
 * @module model/BlacklistItemInsertVersion
 * @version 4.0
 */
class BlacklistItemInsertVersion {
    /**
     * Constructs a new <code>BlacklistItemInsertVersion</code>.
     * @alias module:model/BlacklistItemInsertVersion
     * @param name {String} Blacklist item name
     */
    constructor(name) { 
        
        BlacklistItemInsertVersion.initialize(this, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name) { 
        obj['name'] = name;
    }

    /**
     * Constructs a <code>BlacklistItemInsertVersion</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BlacklistItemInsertVersion} obj Optional instance to populate.
     * @return {module:model/BlacklistItemInsertVersion} The populated <code>BlacklistItemInsertVersion</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BlacklistItemInsertVersion();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BlacklistItemInsertVersion</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BlacklistItemInsertVersion</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BlacklistItemInsertVersion.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}

BlacklistItemInsertVersion.RequiredProperties = ["name"];

/**
 * Blacklist item name
 * @member {String} name
 */
BlacklistItemInsertVersion.prototype['name'] = undefined;






export default BlacklistItemInsertVersion;

