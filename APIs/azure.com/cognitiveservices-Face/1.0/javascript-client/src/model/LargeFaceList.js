/**
 * Face Client
 * An API for face detection, verification, and identification.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import MetaDataContract from './MetaDataContract';
import RecognitionModel from './RecognitionModel';

/**
 * The LargeFaceList model module.
 * @module model/LargeFaceList
 * @version 1.0
 */
class LargeFaceList {
    /**
     * Constructs a new <code>LargeFaceList</code>.
     * Large face list object.
     * @alias module:model/LargeFaceList
     * @implements module:model/MetaDataContract
     */
    constructor() { 
        MetaDataContract.initialize(this);
        LargeFaceList.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['largeFaceListId'] = largeFaceListId;
    }

    /**
     * Constructs a <code>LargeFaceList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LargeFaceList} obj Optional instance to populate.
     * @return {module:model/LargeFaceList} The populated <code>LargeFaceList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LargeFaceList();
            MetaDataContract.constructFromObject(data, obj);

            if (data.hasOwnProperty('largeFaceListId')) {
                obj['largeFaceListId'] = ApiClient.convertToType(data['largeFaceListId'], 'String');
            }
            if (data.hasOwnProperty('recognitionModel')) {
                obj['recognitionModel'] = RecognitionModel.constructFromObject(data['recognitionModel']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('userData')) {
                obj['userData'] = ApiClient.convertToType(data['userData'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LargeFaceList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LargeFaceList</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of LargeFaceList.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['largeFaceListId'] && !(typeof data['largeFaceListId'] === 'string' || data['largeFaceListId'] instanceof String)) {
            throw new Error("Expected the field `largeFaceListId` to be a primitive type in the JSON string but got " + data['largeFaceListId']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['userData'] && !(typeof data['userData'] === 'string' || data['userData'] instanceof String)) {
            throw new Error("Expected the field `userData` to be a primitive type in the JSON string but got " + data['userData']);
        }

        return true;
    }


}

LargeFaceList.RequiredProperties = ["largeFaceListId"];

/**
 * LargeFaceListId of the target large face list.
 * @member {String} largeFaceListId
 */
LargeFaceList.prototype['largeFaceListId'] = undefined;

/**
 * @member {module:model/RecognitionModel} recognitionModel
 */
LargeFaceList.prototype['recognitionModel'] = undefined;

/**
 * User defined name, maximum length is 128.
 * @member {String} name
 */
LargeFaceList.prototype['name'] = undefined;

/**
 * User specified data. Length should not exceed 16KB.
 * @member {String} userData
 */
LargeFaceList.prototype['userData'] = undefined;


// Implement MetaDataContract interface:
/**
 * User defined name, maximum length is 128.
 * @member {String} name
 */
MetaDataContract.prototype['name'] = undefined;
/**
 * User specified data. Length should not exceed 16KB.
 * @member {String} userData
 */
MetaDataContract.prototype['userData'] = undefined;




export default LargeFaceList;

