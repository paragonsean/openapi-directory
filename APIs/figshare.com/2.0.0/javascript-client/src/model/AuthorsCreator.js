/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AuthorsCreator model module.
 * @module model/AuthorsCreator
 * @version 2.0.0
 */
class AuthorsCreator {
    /**
     * Constructs a new <code>AuthorsCreator</code>.
     * @alias module:model/AuthorsCreator
     * @param authors {Array.<Object>} List of authors to be associated with the article. The list can contain the following fields: id, name, first_name, last_name, email, orcid_id. If an id is supplied, it will take priority and everything else will be ignored. No more than 10 authors. For adding more authors use the specific authors endpoint.
     */
    constructor(authors) { 
        
        AuthorsCreator.initialize(this, authors);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, authors) { 
        obj['authors'] = authors;
    }

    /**
     * Constructs a <code>AuthorsCreator</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AuthorsCreator} obj Optional instance to populate.
     * @return {module:model/AuthorsCreator} The populated <code>AuthorsCreator</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AuthorsCreator();

            if (data.hasOwnProperty('authors')) {
                obj['authors'] = ApiClient.convertToType(data['authors'], [Object]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AuthorsCreator</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AuthorsCreator</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AuthorsCreator.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['authors'])) {
            throw new Error("Expected the field `authors` to be an array in the JSON data but got " + data['authors']);
        }

        return true;
    }


}

AuthorsCreator.RequiredProperties = ["authors"];

/**
 * List of authors to be associated with the article. The list can contain the following fields: id, name, first_name, last_name, email, orcid_id. If an id is supplied, it will take priority and everything else will be ignored. No more than 10 authors. For adding more authors use the specific authors endpoint.
 * @member {Array.<Object>} authors
 */
AuthorsCreator.prototype['authors'] = undefined;






export default AuthorsCreator;

