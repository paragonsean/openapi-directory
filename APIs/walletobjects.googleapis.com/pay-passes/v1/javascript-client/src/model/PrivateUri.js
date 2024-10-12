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
 * The PrivateUri model module.
 * @module model/PrivateUri
 * @version v1
 */
class PrivateUri {
    /**
     * Constructs a new <code>PrivateUri</code>.
     * Private data for LinkModule. This data will be rendered as the LinkModule for a pass.
     * @alias module:model/PrivateUri
     */
    constructor() { 
        
        PrivateUri.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PrivateUri</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PrivateUri} obj Optional instance to populate.
     * @return {module:model/PrivateUri} The populated <code>PrivateUri</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PrivateUri();

            if (data.hasOwnProperty('description')) {
                obj['description'] = LocalizedString.constructFromObject(data['description']);
            }
            if (data.hasOwnProperty('uri')) {
                obj['uri'] = ApiClient.convertToType(data['uri'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PrivateUri</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PrivateUri</code>.
     */
    static validateJSON(data) {
        // validate the optional field `description`
        if (data['description']) { // data not null
          LocalizedString.validateJSON(data['description']);
        }
        // ensure the json data is a string
        if (data['uri'] && !(typeof data['uri'] === 'string' || data['uri'] instanceof String)) {
            throw new Error("Expected the field `uri` to be a primitive type in the JSON string but got " + data['uri']);
        }

        return true;
    }


}



/**
 * @member {module:model/LocalizedString} description
 */
PrivateUri.prototype['description'] = undefined;

/**
 * The location of a web page, image, or other resource. URIs in the `LinksModuleData` can have different prefixes indicating the type of URI (a link to a web page, a link to a map, a telephone number, or an email address).
 * @member {String} uri
 */
PrivateUri.prototype['uri'] = undefined;






export default PrivateUri;

