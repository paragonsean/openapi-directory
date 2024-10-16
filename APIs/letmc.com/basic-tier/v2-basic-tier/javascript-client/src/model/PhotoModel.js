/**
 * LetMC Api V2, Basic (Tier 2)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-basic-tier
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PhotoModel model module.
 * @module model/PhotoModel
 * @version v2-basic-tier
 */
class PhotoModel {
    /**
     * Constructs a new <code>PhotoModel</code>.
     * Stores a photo related to a property structure.
     * @alias module:model/PhotoModel
     */
    constructor() { 
        
        PhotoModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PhotoModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PhotoModel} obj Optional instance to populate.
     * @return {module:model/PhotoModel} The populated <code>PhotoModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PhotoModel();

            if (data.hasOwnProperty('ETag')) {
                obj['ETag'] = ApiClient.convertToType(data['ETag'], 'String');
            }
            if (data.hasOwnProperty('FileName')) {
                obj['FileName'] = ApiClient.convertToType(data['FileName'], 'String');
            }
            if (data.hasOwnProperty('InspectionItem')) {
                obj['InspectionItem'] = ApiClient.convertToType(data['InspectionItem'], 'String');
            }
            if (data.hasOwnProperty('InterimInspection')) {
                obj['InterimInspection'] = ApiClient.convertToType(data['InterimInspection'], 'String');
            }
            if (data.hasOwnProperty('InventoryItem')) {
                obj['InventoryItem'] = ApiClient.convertToType(data['InventoryItem'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('OID')) {
                obj['OID'] = ApiClient.convertToType(data['OID'], 'String');
            }
            if (data.hasOwnProperty('PhotoNumber')) {
                obj['PhotoNumber'] = ApiClient.convertToType(data['PhotoNumber'], 'Number');
            }
            if (data.hasOwnProperty('PhotoType')) {
                obj['PhotoType'] = ApiClient.convertToType(data['PhotoType'], 'String');
            }
            if (data.hasOwnProperty('Property')) {
                obj['Property'] = ApiClient.convertToType(data['Property'], 'String');
            }
            if (data.hasOwnProperty('Room')) {
                obj['Room'] = ApiClient.convertToType(data['Room'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PhotoModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PhotoModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['ETag'] && !(typeof data['ETag'] === 'string' || data['ETag'] instanceof String)) {
            throw new Error("Expected the field `ETag` to be a primitive type in the JSON string but got " + data['ETag']);
        }
        // ensure the json data is a string
        if (data['FileName'] && !(typeof data['FileName'] === 'string' || data['FileName'] instanceof String)) {
            throw new Error("Expected the field `FileName` to be a primitive type in the JSON string but got " + data['FileName']);
        }
        // ensure the json data is a string
        if (data['InspectionItem'] && !(typeof data['InspectionItem'] === 'string' || data['InspectionItem'] instanceof String)) {
            throw new Error("Expected the field `InspectionItem` to be a primitive type in the JSON string but got " + data['InspectionItem']);
        }
        // ensure the json data is a string
        if (data['InterimInspection'] && !(typeof data['InterimInspection'] === 'string' || data['InterimInspection'] instanceof String)) {
            throw new Error("Expected the field `InterimInspection` to be a primitive type in the JSON string but got " + data['InterimInspection']);
        }
        // ensure the json data is a string
        if (data['InventoryItem'] && !(typeof data['InventoryItem'] === 'string' || data['InventoryItem'] instanceof String)) {
            throw new Error("Expected the field `InventoryItem` to be a primitive type in the JSON string but got " + data['InventoryItem']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['OID'] && !(typeof data['OID'] === 'string' || data['OID'] instanceof String)) {
            throw new Error("Expected the field `OID` to be a primitive type in the JSON string but got " + data['OID']);
        }
        // ensure the json data is a string
        if (data['PhotoType'] && !(typeof data['PhotoType'] === 'string' || data['PhotoType'] instanceof String)) {
            throw new Error("Expected the field `PhotoType` to be a primitive type in the JSON string but got " + data['PhotoType']);
        }
        // ensure the json data is a string
        if (data['Property'] && !(typeof data['Property'] === 'string' || data['Property'] instanceof String)) {
            throw new Error("Expected the field `Property` to be a primitive type in the JSON string but got " + data['Property']);
        }
        // ensure the json data is a string
        if (data['Room'] && !(typeof data['Room'] === 'string' || data['Room'] instanceof String)) {
            throw new Error("Expected the field `Room` to be a primitive type in the JSON string but got " + data['Room']);
        }

        return true;
    }


}



/**
 * A unique identifier defining the object and change revision.
 * @member {String} ETag
 */
PhotoModel.prototype['ETag'] = undefined;

/**
 * The file name.
 * @member {String} FileName
 */
PhotoModel.prototype['FileName'] = undefined;

/**
 * The inspection item the photo is assigned to (if applicable).
 * @member {String} InspectionItem
 */
PhotoModel.prototype['InspectionItem'] = undefined;

/**
 * The inspection the photo is assigned to (if applicable).
 * @member {String} InterimInspection
 */
PhotoModel.prototype['InterimInspection'] = undefined;

/**
 * The inventory item the photo is assigned to (if applicable).
 * @member {String} InventoryItem
 */
PhotoModel.prototype['InventoryItem'] = undefined;

/**
 * The photo name.
 * @member {String} Name
 */
PhotoModel.prototype['Name'] = undefined;

/**
 * The unique Object ID (OID).
 * @member {String} OID
 */
PhotoModel.prototype['OID'] = undefined;

/**
 * The photo ordering number
 * @member {Number} PhotoNumber
 */
PhotoModel.prototype['PhotoNumber'] = undefined;

/**
 * The photo type.
 * @member {module:model/PhotoModel.PhotoTypeEnum} PhotoType
 */
PhotoModel.prototype['PhotoType'] = undefined;

/**
 * The property the photo is assigned to.
 * @member {String} Property
 */
PhotoModel.prototype['Property'] = undefined;

/**
 * The room the photo is assigned to. (If applicable)
 * @member {String} Room
 */
PhotoModel.prototype['Room'] = undefined;





/**
 * Allowed values for the <code>PhotoType</code> property.
 * @enum {String}
 * @readonly
 */
PhotoModel['PhotoTypeEnum'] = {

    /**
     * value: "Photo"
     * @const
     */
    "Photo": "Photo",

    /**
     * value: "Map"
     * @const
     */
    "Map": "Map",

    /**
     * value: "FloorPlan"
     * @const
     */
    "FloorPlan": "FloorPlan",

    /**
     * value: "SiteMap"
     * @const
     */
    "SiteMap": "SiteMap",

    /**
     * value: "AerialPhoto"
     * @const
     */
    "AerialPhoto": "AerialPhoto"
};



export default PhotoModel;

