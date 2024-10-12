/**
 * GalleryManagementClient
 * The Admin Gallery Management Client.
 *
 * The version of the OpenAPI document: 2015-04-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Artifact from './Artifact';
import DefinitionTemplates from './DefinitionTemplates';
import Filter from './Filter';
import GalleryItemPropertiesIconFileUris from './GalleryItemPropertiesIconFileUris';
import ImageGroup from './ImageGroup';
import LinkProperties from './LinkProperties';
import MarketingMaterial from './MarketingMaterial';
import OpenProperty from './OpenProperty';
import Product from './Product';

/**
 * The GalleryItemProperties model module.
 * @module model/GalleryItemProperties
 * @version 2015-04-01
 */
class GalleryItemProperties {
    /**
     * Constructs a new <code>GalleryItemProperties</code>.
     * Properties of a gallery item.
     * @alias module:model/GalleryItemProperties
     */
    constructor() { 
        
        GalleryItemProperties.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GalleryItemProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GalleryItemProperties} obj Optional instance to populate.
     * @return {module:model/GalleryItemProperties} The populated <code>GalleryItemProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GalleryItemProperties();

            if (data.hasOwnProperty('additionalProperties')) {
                obj['additionalProperties'] = ApiClient.convertToType(data['additionalProperties'], {'String': 'String'});
            }
            if (data.hasOwnProperty('artifacts')) {
                obj['artifacts'] = ApiClient.convertToType(data['artifacts'], [Artifact]);
            }
            if (data.hasOwnProperty('categoryIds')) {
                obj['categoryIds'] = ApiClient.convertToType(data['categoryIds'], ['String']);
            }
            if (data.hasOwnProperty('changedTime')) {
                obj['changedTime'] = ApiClient.convertToType(data['changedTime'], 'Date');
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('definitionTemplates')) {
                obj['definitionTemplates'] = DefinitionTemplates.constructFromObject(data['definitionTemplates']);
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('filters')) {
                obj['filters'] = ApiClient.convertToType(data['filters'], [Filter]);
            }
            if (data.hasOwnProperty('iconFileUris')) {
                obj['iconFileUris'] = GalleryItemPropertiesIconFileUris.constructFromObject(data['iconFileUris']);
            }
            if (data.hasOwnProperty('identity')) {
                obj['identity'] = ApiClient.convertToType(data['identity'], 'String');
            }
            if (data.hasOwnProperty('images')) {
                obj['images'] = ApiClient.convertToType(data['images'], [ImageGroup]);
            }
            if (data.hasOwnProperty('itemDisplayName')) {
                obj['itemDisplayName'] = ApiClient.convertToType(data['itemDisplayName'], 'String');
            }
            if (data.hasOwnProperty('itemName')) {
                obj['itemName'] = ApiClient.convertToType(data['itemName'], 'String');
            }
            if (data.hasOwnProperty('itemType')) {
                obj['itemType'] = ApiClient.convertToType(data['itemType'], 'String');
            }
            if (data.hasOwnProperty('links')) {
                obj['links'] = ApiClient.convertToType(data['links'], [LinkProperties]);
            }
            if (data.hasOwnProperty('longSummary')) {
                obj['longSummary'] = ApiClient.convertToType(data['longSummary'], 'String');
            }
            if (data.hasOwnProperty('marketingMaterial')) {
                obj['marketingMaterial'] = MarketingMaterial.constructFromObject(data['marketingMaterial']);
            }
            if (data.hasOwnProperty('metadata')) {
                obj['metadata'] = OpenProperty.constructFromObject(data['metadata']);
            }
            if (data.hasOwnProperty('products')) {
                obj['products'] = ApiClient.convertToType(data['products'], [Product]);
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ApiClient.convertToType(data['properties'], {'String': 'String'});
            }
            if (data.hasOwnProperty('publisher')) {
                obj['publisher'] = ApiClient.convertToType(data['publisher'], 'String');
            }
            if (data.hasOwnProperty('publisherDisplayName')) {
                obj['publisherDisplayName'] = ApiClient.convertToType(data['publisherDisplayName'], 'String');
            }
            if (data.hasOwnProperty('resourceGroupName')) {
                obj['resourceGroupName'] = ApiClient.convertToType(data['resourceGroupName'], 'String');
            }
            if (data.hasOwnProperty('screenshotUris')) {
                obj['screenshotUris'] = ApiClient.convertToType(data['screenshotUris'], ['String']);
            }
            if (data.hasOwnProperty('summary')) {
                obj['summary'] = ApiClient.convertToType(data['summary'], 'String');
            }
            if (data.hasOwnProperty('uiDefinitionUri')) {
                obj['uiDefinitionUri'] = ApiClient.convertToType(data['uiDefinitionUri'], 'String');
            }
            if (data.hasOwnProperty('version')) {
                obj['version'] = ApiClient.convertToType(data['version'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GalleryItemProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GalleryItemProperties</code>.
     */
    static validateJSON(data) {
        if (data['artifacts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['artifacts'])) {
                throw new Error("Expected the field `artifacts` to be an array in the JSON data but got " + data['artifacts']);
            }
            // validate the optional field `artifacts` (array)
            for (const item of data['artifacts']) {
                Artifact.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['categoryIds'])) {
            throw new Error("Expected the field `categoryIds` to be an array in the JSON data but got " + data['categoryIds']);
        }
        // validate the optional field `definitionTemplates`
        if (data['definitionTemplates']) { // data not null
          DefinitionTemplates.validateJSON(data['definitionTemplates']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        if (data['filters']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['filters'])) {
                throw new Error("Expected the field `filters` to be an array in the JSON data but got " + data['filters']);
            }
            // validate the optional field `filters` (array)
            for (const item of data['filters']) {
                Filter.validateJSON(item);
            };
        }
        // validate the optional field `iconFileUris`
        if (data['iconFileUris']) { // data not null
          GalleryItemPropertiesIconFileUris.validateJSON(data['iconFileUris']);
        }
        // ensure the json data is a string
        if (data['identity'] && !(typeof data['identity'] === 'string' || data['identity'] instanceof String)) {
            throw new Error("Expected the field `identity` to be a primitive type in the JSON string but got " + data['identity']);
        }
        if (data['images']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['images'])) {
                throw new Error("Expected the field `images` to be an array in the JSON data but got " + data['images']);
            }
            // validate the optional field `images` (array)
            for (const item of data['images']) {
                ImageGroup.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['itemDisplayName'] && !(typeof data['itemDisplayName'] === 'string' || data['itemDisplayName'] instanceof String)) {
            throw new Error("Expected the field `itemDisplayName` to be a primitive type in the JSON string but got " + data['itemDisplayName']);
        }
        // ensure the json data is a string
        if (data['itemName'] && !(typeof data['itemName'] === 'string' || data['itemName'] instanceof String)) {
            throw new Error("Expected the field `itemName` to be a primitive type in the JSON string but got " + data['itemName']);
        }
        // ensure the json data is a string
        if (data['itemType'] && !(typeof data['itemType'] === 'string' || data['itemType'] instanceof String)) {
            throw new Error("Expected the field `itemType` to be a primitive type in the JSON string but got " + data['itemType']);
        }
        if (data['links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['links'])) {
                throw new Error("Expected the field `links` to be an array in the JSON data but got " + data['links']);
            }
            // validate the optional field `links` (array)
            for (const item of data['links']) {
                LinkProperties.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['longSummary'] && !(typeof data['longSummary'] === 'string' || data['longSummary'] instanceof String)) {
            throw new Error("Expected the field `longSummary` to be a primitive type in the JSON string but got " + data['longSummary']);
        }
        // validate the optional field `marketingMaterial`
        if (data['marketingMaterial']) { // data not null
          MarketingMaterial.validateJSON(data['marketingMaterial']);
        }
        // validate the optional field `metadata`
        if (data['metadata']) { // data not null
          OpenProperty.validateJSON(data['metadata']);
        }
        if (data['products']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['products'])) {
                throw new Error("Expected the field `products` to be an array in the JSON data but got " + data['products']);
            }
            // validate the optional field `products` (array)
            for (const item of data['products']) {
                Product.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['publisher'] && !(typeof data['publisher'] === 'string' || data['publisher'] instanceof String)) {
            throw new Error("Expected the field `publisher` to be a primitive type in the JSON string but got " + data['publisher']);
        }
        // ensure the json data is a string
        if (data['publisherDisplayName'] && !(typeof data['publisherDisplayName'] === 'string' || data['publisherDisplayName'] instanceof String)) {
            throw new Error("Expected the field `publisherDisplayName` to be a primitive type in the JSON string but got " + data['publisherDisplayName']);
        }
        // ensure the json data is a string
        if (data['resourceGroupName'] && !(typeof data['resourceGroupName'] === 'string' || data['resourceGroupName'] instanceof String)) {
            throw new Error("Expected the field `resourceGroupName` to be a primitive type in the JSON string but got " + data['resourceGroupName']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['screenshotUris'])) {
            throw new Error("Expected the field `screenshotUris` to be an array in the JSON data but got " + data['screenshotUris']);
        }
        // ensure the json data is a string
        if (data['summary'] && !(typeof data['summary'] === 'string' || data['summary'] instanceof String)) {
            throw new Error("Expected the field `summary` to be a primitive type in the JSON string but got " + data['summary']);
        }
        // ensure the json data is a string
        if (data['uiDefinitionUri'] && !(typeof data['uiDefinitionUri'] === 'string' || data['uiDefinitionUri'] instanceof String)) {
            throw new Error("Expected the field `uiDefinitionUri` to be a primitive type in the JSON string but got " + data['uiDefinitionUri']);
        }
        // ensure the json data is a string
        if (data['version'] && !(typeof data['version'] === 'string' || data['version'] instanceof String)) {
            throw new Error("Expected the field `version` to be a primitive type in the JSON string but got " + data['version']);
        }

        return true;
    }


}



/**
 * List of additional properties provided for the item.
 * @member {Object.<String, String>} additionalProperties
 */
GalleryItemProperties.prototype['additionalProperties'] = undefined;

/**
 * List of artifacts for the gallery item.
 * @member {Array.<module:model/Artifact>} artifacts
 */
GalleryItemProperties.prototype['artifacts'] = undefined;

/**
 * List of category IDs the gallery item belongs to.
 * @member {Array.<String>} categoryIds
 */
GalleryItemProperties.prototype['categoryIds'] = undefined;

/**
 * Last update time of gallery item.
 * @member {Date} changedTime
 */
GalleryItemProperties.prototype['changedTime'] = undefined;

/**
 * The date and time that the gallery item was created.
 * @member {Date} createdTime
 */
GalleryItemProperties.prototype['createdTime'] = undefined;

/**
 * @member {module:model/DefinitionTemplates} definitionTemplates
 */
GalleryItemProperties.prototype['definitionTemplates'] = undefined;

/**
 * The description of the gallery item.
 * @member {String} description
 */
GalleryItemProperties.prototype['description'] = undefined;

/**
 * List of filters for the gallery item.
 * @member {Array.<module:model/Filter>} filters
 */
GalleryItemProperties.prototype['filters'] = undefined;

/**
 * @member {module:model/GalleryItemPropertiesIconFileUris} iconFileUris
 */
GalleryItemProperties.prototype['iconFileUris'] = undefined;

/**
 * Identity of the gallery item.
 * @member {String} identity
 */
GalleryItemProperties.prototype['identity'] = undefined;

/**
 * List of images.
 * @member {Array.<module:model/ImageGroup>} images
 */
GalleryItemProperties.prototype['images'] = undefined;

/**
 * Displayed name in the portal.
 * @member {String} itemDisplayName
 */
GalleryItemProperties.prototype['itemDisplayName'] = undefined;

/**
 * The display name for the gallery item, for the locale of the request.
 * @member {String} itemName
 */
GalleryItemProperties.prototype['itemName'] = undefined;

/**
 * Describes the type of the gallery item, either GalleryItem or ItemGroup.
 * @member {module:model/GalleryItemProperties.ItemTypeEnum} itemType
 */
GalleryItemProperties.prototype['itemType'] = undefined;

/**
 * Links provided for the item.
 * @member {Array.<module:model/LinkProperties>} links
 */
GalleryItemProperties.prototype['links'] = undefined;

/**
 * Long summary of the gallery item.
 * @member {String} longSummary
 */
GalleryItemProperties.prototype['longSummary'] = undefined;

/**
 * @member {module:model/MarketingMaterial} marketingMaterial
 */
GalleryItemProperties.prototype['marketingMaterial'] = undefined;

/**
 * @member {module:model/OpenProperty} metadata
 */
GalleryItemProperties.prototype['metadata'] = undefined;

/**
 * List of products.
 * @member {Array.<module:model/Product>} products
 */
GalleryItemProperties.prototype['products'] = undefined;

/**
 * List of properties provided for the gallery item.
 * @member {Object.<String, String>} properties
 */
GalleryItemProperties.prototype['properties'] = undefined;

/**
 * The publisher of the gallery item.
 * @member {String} publisher
 */
GalleryItemProperties.prototype['publisher'] = undefined;

/**
 * Display name of the publisher.
 * @member {String} publisherDisplayName
 */
GalleryItemProperties.prototype['publisherDisplayName'] = undefined;

/**
 * Resource group name the gallery item belongs too.
 * @member {String} resourceGroupName
 */
GalleryItemProperties.prototype['resourceGroupName'] = undefined;

/**
 * List of screenshot image URIs provided for the item.
 * @member {Array.<String>} screenshotUris
 */
GalleryItemProperties.prototype['screenshotUris'] = undefined;

/**
 * Short summary of the gallery item.
 * @member {String} summary
 */
GalleryItemProperties.prototype['summary'] = undefined;

/**
 * The URL of the view definition object that defines the UI information that is used when an instance of the gallery item resource definition is created.
 * @member {String} uiDefinitionUri
 */
GalleryItemProperties.prototype['uiDefinitionUri'] = undefined;

/**
 * The version identifier of the gallery item, in Major.Minor.Build format.
 * @member {String} version
 */
GalleryItemProperties.prototype['version'] = undefined;





/**
 * Allowed values for the <code>itemType</code> property.
 * @enum {String}
 * @readonly
 */
GalleryItemProperties['ItemTypeEnum'] = {

    /**
     * value: "GalleryItem"
     * @const
     */
    "GalleryItem": "GalleryItem",

    /**
     * value: "ItemGroup"
     * @const
     */
    "ItemGroup": "ItemGroup"
};



export default GalleryItemProperties;

