/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ReleasesListLatest200ResponseInnerDistributionStoresInner model module.
 * @module model/ReleasesListLatest200ResponseInnerDistributionStoresInner
 * @version v0.1
 */
class ReleasesListLatest200ResponseInnerDistributionStoresInner {
    /**
     * Constructs a new <code>ReleasesListLatest200ResponseInnerDistributionStoresInner</code>.
     * @alias module:model/ReleasesListLatest200ResponseInnerDistributionStoresInner
     * @param id {String} ID identifying a unique distribution store.
     */
    constructor(id) { 
        
        ReleasesListLatest200ResponseInnerDistributionStoresInner.initialize(this, id);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id) { 
        obj['id'] = id;
    }

    /**
     * Constructs a <code>ReleasesListLatest200ResponseInnerDistributionStoresInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ReleasesListLatest200ResponseInnerDistributionStoresInner} obj Optional instance to populate.
     * @return {module:model/ReleasesListLatest200ResponseInnerDistributionStoresInner} The populated <code>ReleasesListLatest200ResponseInnerDistributionStoresInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ReleasesListLatest200ResponseInnerDistributionStoresInner();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('publishing_status')) {
                obj['publishing_status'] = ApiClient.convertToType(data['publishing_status'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('is_latest')) {
                obj['is_latest'] = ApiClient.convertToType(data['is_latest'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ReleasesListLatest200ResponseInnerDistributionStoresInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ReleasesListLatest200ResponseInnerDistributionStoresInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ReleasesListLatest200ResponseInnerDistributionStoresInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['publishing_status'] && !(typeof data['publishing_status'] === 'string' || data['publishing_status'] instanceof String)) {
            throw new Error("Expected the field `publishing_status` to be a primitive type in the JSON string but got " + data['publishing_status']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

ReleasesListLatest200ResponseInnerDistributionStoresInner.RequiredProperties = ["id"];

/**
 * ID identifying a unique distribution store.
 * @member {String} id
 */
ReleasesListLatest200ResponseInnerDistributionStoresInner.prototype['id'] = undefined;

/**
 * A name identifying a unique distribution store.
 * @member {String} name
 */
ReleasesListLatest200ResponseInnerDistributionStoresInner.prototype['name'] = undefined;

/**
 * publishing status of the release in the store.
 * @member {String} publishing_status
 */
ReleasesListLatest200ResponseInnerDistributionStoresInner.prototype['publishing_status'] = undefined;

/**
 * type of the distribution store currently stores type can be intune, googleplay or windows.
 * @member {module:model/ReleasesListLatest200ResponseInnerDistributionStoresInner.TypeEnum} type
 */
ReleasesListLatest200ResponseInnerDistributionStoresInner.prototype['type'] = undefined;

/**
 * Is the containing release the latest one in this distribution store.
 * @member {Boolean} is_latest
 */
ReleasesListLatest200ResponseInnerDistributionStoresInner.prototype['is_latest'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
ReleasesListLatest200ResponseInnerDistributionStoresInner['TypeEnum'] = {

    /**
     * value: "intune"
     * @const
     */
    "intune": "intune",

    /**
     * value: "googleplay"
     * @const
     */
    "googleplay": "googleplay",

    /**
     * value: "apple"
     * @const
     */
    "apple": "apple",

    /**
     * value: "none"
     * @const
     */
    "none": "none"
};



export default ReleasesListLatest200ResponseInnerDistributionStoresInner;

