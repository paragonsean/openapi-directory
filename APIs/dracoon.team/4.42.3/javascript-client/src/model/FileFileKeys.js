/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import FileKeyContainer from './FileKeyContainer';

/**
 * The FileFileKeys model module.
 * @module model/FileFileKeys
 * @version 4.42.3
 */
class FileFileKeys {
    /**
     * Constructs a new <code>FileFileKeys</code>.
     * File key information
     * @alias module:model/FileFileKeys
     */
    constructor() { 
        
        FileFileKeys.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FileFileKeys</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FileFileKeys} obj Optional instance to populate.
     * @return {module:model/FileFileKeys} The populated <code>FileFileKeys</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FileFileKeys();

            if (data.hasOwnProperty('fileKeyContainer')) {
                obj['fileKeyContainer'] = FileKeyContainer.constructFromObject(data['fileKeyContainer']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FileFileKeys</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FileFileKeys</code>.
     */
    static validateJSON(data) {
        // validate the optional field `fileKeyContainer`
        if (data['fileKeyContainer']) { // data not null
          FileKeyContainer.validateJSON(data['fileKeyContainer']);
        }

        return true;
    }


}



/**
 * @member {module:model/FileKeyContainer} fileKeyContainer
 */
FileFileKeys.prototype['fileKeyContainer'] = undefined;

/**
 * File ID
 * @member {Number} id
 */
FileFileKeys.prototype['id'] = undefined;






export default FileFileKeys;

