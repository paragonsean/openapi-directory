/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DownloadableDataFileContentInterface model module.
 * @module model/DownloadableDataFileContentInterface
 * @version 2.2.10
 */
class DownloadableDataFileContentInterface {
    /**
     * Constructs a new <code>DownloadableDataFileContentInterface</code>.
     * 
     * @alias module:model/DownloadableDataFileContentInterface
     * @param fileData {String} Data (base64 encoded content)
     * @param name {String} File name
     */
    constructor(fileData, name) { 
        
        DownloadableDataFileContentInterface.initialize(this, fileData, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, fileData, name) { 
        obj['file_data'] = fileData;
        obj['name'] = name;
    }

    /**
     * Constructs a <code>DownloadableDataFileContentInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DownloadableDataFileContentInterface} obj Optional instance to populate.
     * @return {module:model/DownloadableDataFileContentInterface} The populated <code>DownloadableDataFileContentInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DownloadableDataFileContentInterface();

            if (data.hasOwnProperty('extension_attributes')) {
                obj['extension_attributes'] = ApiClient.convertToType(data['extension_attributes'], Object);
            }
            if (data.hasOwnProperty('file_data')) {
                obj['file_data'] = ApiClient.convertToType(data['file_data'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DownloadableDataFileContentInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DownloadableDataFileContentInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DownloadableDataFileContentInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['file_data'] && !(typeof data['file_data'] === 'string' || data['file_data'] instanceof String)) {
            throw new Error("Expected the field `file_data` to be a primitive type in the JSON string but got " + data['file_data']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}

DownloadableDataFileContentInterface.RequiredProperties = ["file_data", "name"];

/**
 * ExtensionInterface class for @see \\Magento\\Downloadable\\Api\\Data\\File\\ContentInterface
 * @member {Object} extension_attributes
 */
DownloadableDataFileContentInterface.prototype['extension_attributes'] = undefined;

/**
 * Data (base64 encoded content)
 * @member {String} file_data
 */
DownloadableDataFileContentInterface.prototype['file_data'] = undefined;

/**
 * File name
 * @member {String} name
 */
DownloadableDataFileContentInterface.prototype['name'] = undefined;






export default DownloadableDataFileContentInterface;

