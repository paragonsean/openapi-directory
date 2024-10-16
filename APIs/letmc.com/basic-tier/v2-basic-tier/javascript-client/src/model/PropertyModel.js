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
 * The PropertyModel model module.
 * @module model/PropertyModel
 * @version v2-basic-tier
 */
class PropertyModel {
    /**
     * Constructs a new <code>PropertyModel</code>.
     * Stores the &#39;Sales&#39; type fields for property ownable as a stepping stone to a full on BO when we finally get the go ahead to write sales!!
     * @alias module:model/PropertyModel
     */
    constructor() { 
        
        PropertyModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PropertyModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PropertyModel} obj Optional instance to populate.
     * @return {module:model/PropertyModel} The populated <code>PropertyModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PropertyModel();

            if (data.hasOwnProperty('Area')) {
                obj['Area'] = ApiClient.convertToType(data['Area'], 'String');
            }
            if (data.hasOwnProperty('Branch')) {
                obj['Branch'] = ApiClient.convertToType(data['Branch'], 'String');
            }
            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('ETag')) {
                obj['ETag'] = ApiClient.convertToType(data['ETag'], 'String');
            }
            if (data.hasOwnProperty('FullAddress')) {
                obj['FullAddress'] = ApiClient.convertToType(data['FullAddress'], 'String');
            }
            if (data.hasOwnProperty('GlobalReference')) {
                obj['GlobalReference'] = ApiClient.convertToType(data['GlobalReference'], 'String');
            }
            if (data.hasOwnProperty('MainPhoto')) {
                obj['MainPhoto'] = ApiClient.convertToType(data['MainPhoto'], 'String');
            }
            if (data.hasOwnProperty('ManagedByStaff')) {
                obj['ManagedByStaff'] = ApiClient.convertToType(data['ManagedByStaff'], 'String');
            }
            if (data.hasOwnProperty('OID')) {
                obj['OID'] = ApiClient.convertToType(data['OID'], 'String');
            }
            if (data.hasOwnProperty('PropertySource')) {
                obj['PropertySource'] = ApiClient.convertToType(data['PropertySource'], 'String');
            }
            if (data.hasOwnProperty('PropertyType')) {
                obj['PropertyType'] = ApiClient.convertToType(data['PropertyType'], 'String');
            }
            if (data.hasOwnProperty('RoomName')) {
                obj['RoomName'] = ApiClient.convertToType(data['RoomName'], 'String');
            }
            if (data.hasOwnProperty('VideoURL')) {
                obj['VideoURL'] = ApiClient.convertToType(data['VideoURL'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PropertyModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PropertyModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Area'] && !(typeof data['Area'] === 'string' || data['Area'] instanceof String)) {
            throw new Error("Expected the field `Area` to be a primitive type in the JSON string but got " + data['Area']);
        }
        // ensure the json data is a string
        if (data['Branch'] && !(typeof data['Branch'] === 'string' || data['Branch'] instanceof String)) {
            throw new Error("Expected the field `Branch` to be a primitive type in the JSON string but got " + data['Branch']);
        }
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }
        // ensure the json data is a string
        if (data['ETag'] && !(typeof data['ETag'] === 'string' || data['ETag'] instanceof String)) {
            throw new Error("Expected the field `ETag` to be a primitive type in the JSON string but got " + data['ETag']);
        }
        // ensure the json data is a string
        if (data['FullAddress'] && !(typeof data['FullAddress'] === 'string' || data['FullAddress'] instanceof String)) {
            throw new Error("Expected the field `FullAddress` to be a primitive type in the JSON string but got " + data['FullAddress']);
        }
        // ensure the json data is a string
        if (data['GlobalReference'] && !(typeof data['GlobalReference'] === 'string' || data['GlobalReference'] instanceof String)) {
            throw new Error("Expected the field `GlobalReference` to be a primitive type in the JSON string but got " + data['GlobalReference']);
        }
        // ensure the json data is a string
        if (data['MainPhoto'] && !(typeof data['MainPhoto'] === 'string' || data['MainPhoto'] instanceof String)) {
            throw new Error("Expected the field `MainPhoto` to be a primitive type in the JSON string but got " + data['MainPhoto']);
        }
        // ensure the json data is a string
        if (data['ManagedByStaff'] && !(typeof data['ManagedByStaff'] === 'string' || data['ManagedByStaff'] instanceof String)) {
            throw new Error("Expected the field `ManagedByStaff` to be a primitive type in the JSON string but got " + data['ManagedByStaff']);
        }
        // ensure the json data is a string
        if (data['OID'] && !(typeof data['OID'] === 'string' || data['OID'] instanceof String)) {
            throw new Error("Expected the field `OID` to be a primitive type in the JSON string but got " + data['OID']);
        }
        // ensure the json data is a string
        if (data['PropertySource'] && !(typeof data['PropertySource'] === 'string' || data['PropertySource'] instanceof String)) {
            throw new Error("Expected the field `PropertySource` to be a primitive type in the JSON string but got " + data['PropertySource']);
        }
        // ensure the json data is a string
        if (data['PropertyType'] && !(typeof data['PropertyType'] === 'string' || data['PropertyType'] instanceof String)) {
            throw new Error("Expected the field `PropertyType` to be a primitive type in the JSON string but got " + data['PropertyType']);
        }
        // ensure the json data is a string
        if (data['RoomName'] && !(typeof data['RoomName'] === 'string' || data['RoomName'] instanceof String)) {
            throw new Error("Expected the field `RoomName` to be a primitive type in the JSON string but got " + data['RoomName']);
        }
        // ensure the json data is a string
        if (data['VideoURL'] && !(typeof data['VideoURL'] === 'string' || data['VideoURL'] instanceof String)) {
            throw new Error("Expected the field `VideoURL` to be a primitive type in the JSON string but got " + data['VideoURL']);
        }

        return true;
    }


}



/**
 * The area the property is located in.
 * @member {String} Area
 */
PropertyModel.prototype['Area'] = undefined;

/**
 * The branch the block, property or room is assigned to
 * @member {String} Branch
 */
PropertyModel.prototype['Branch'] = undefined;

/**
 * The block, property or room description.
 * @member {String} Description
 */
PropertyModel.prototype['Description'] = undefined;

/**
 * A unique identifier defining the object and change revision.
 * @member {String} ETag
 */
PropertyModel.prototype['ETag'] = undefined;

/**
 * The full address of a block, property or room, formatted with line breaks such that it may be used on a letter directly.
 * @member {String} FullAddress
 */
PropertyModel.prototype['FullAddress'] = undefined;

/**
 * The global reference to this block, property or room
 * @member {String} GlobalReference
 */
PropertyModel.prototype['GlobalReference'] = undefined;

/**
 * Gets the main photo, if there is one.
 * @member {String} MainPhoto
 */
PropertyModel.prototype['MainPhoto'] = undefined;

/**
 * The staff memeber that manages the block, property or room
 * @member {String} ManagedByStaff
 */
PropertyModel.prototype['ManagedByStaff'] = undefined;

/**
 * The unique Object ID (OID).
 * @member {String} OID
 */
PropertyModel.prototype['OID'] = undefined;

/**
 * The block, property or room source type
 * @member {String} PropertySource
 */
PropertyModel.prototype['PropertySource'] = undefined;

/**
 * The block or property type.
 * @member {module:model/PropertyModel.PropertyTypeEnum} PropertyType
 */
PropertyModel.prototype['PropertyType'] = undefined;

/**
 * The room name (if applicable).
 * @member {String} RoomName
 */
PropertyModel.prototype['RoomName'] = undefined;

/**
 * URL of the video linked to the property
 * @member {String} VideoURL
 */
PropertyModel.prototype['VideoURL'] = undefined;





/**
 * Allowed values for the <code>PropertyType</code> property.
 * @enum {String}
 * @readonly
 */
PropertyModel['PropertyTypeEnum'] = {

    /**
     * value: "House"
     * @const
     */
    "House": "House",

    /**
     * value: "FlatApartment"
     * @const
     */
    "FlatApartment": "FlatApartment",

    /**
     * value: "Bungalow"
     * @const
     */
    "Bungalow": "Bungalow",

    /**
     * value: "Land"
     * @const
     */
    "Land": "Land",

    /**
     * value: "HouseFlatShare"
     * @const
     */
    "HouseFlatShare": "HouseFlatShare",

    /**
     * value: "GarageParking"
     * @const
     */
    "GarageParking": "GarageParking",

    /**
     * value: "CommercialProperty"
     * @const
     */
    "CommercialProperty": "CommercialProperty",

    /**
     * value: "Block"
     * @const
     */
    "Block": "Block",

    /**
     * value: "TerracedHouse"
     * @const
     */
    "TerracedHouse": "TerracedHouse",

    /**
     * value: "EndTerraceHouse"
     * @const
     */
    "EndTerraceHouse": "EndTerraceHouse",

    /**
     * value: "SemiDetachedHouse"
     * @const
     */
    "SemiDetachedHouse": "SemiDetachedHouse",

    /**
     * value: "DetachedHouse"
     * @const
     */
    "DetachedHouse": "DetachedHouse",

    /**
     * value: "SemiDetachedBungalow"
     * @const
     */
    "SemiDetachedBungalow": "SemiDetachedBungalow",

    /**
     * value: "TownHouse"
     * @const
     */
    "TownHouse": "TownHouse",

    /**
     * value: "Cottage"
     * @const
     */
    "Cottage": "Cottage",

    /**
     * value: "ServicedApartment"
     * @const
     */
    "ServicedApartment": "ServicedApartment",

    /**
     * value: "Studio"
     * @const
     */
    "Studio": "Studio",

    /**
     * value: "Apartment"
     * @const
     */
    "Apartment": "Apartment",

    /**
     * value: "Barn"
     * @const
     */
    "Barn": "Barn",

    /**
     * value: "FarmHouse"
     * @const
     */
    "FarmHouse": "FarmHouse",

    /**
     * value: "Penthouse"
     * @const
     */
    "Penthouse": "Penthouse",

    /**
     * value: "BuildingPlot"
     * @const
     */
    "BuildingPlot": "BuildingPlot",

    /**
     * value: "DetachedBungalow"
     * @const
     */
    "DetachedBungalow": "DetachedBungalow",

    /**
     * value: "LinkDetached"
     * @const
     */
    "LinkDetached": "LinkDetached",

    /**
     * value: "MidTerracedBungalow"
     * @const
     */
    "MidTerracedBungalow": "MidTerracedBungalow",

    /**
     * value: "LandResidential"
     * @const
     */
    "LandResidential": "LandResidential"
};



export default PropertyModel;

