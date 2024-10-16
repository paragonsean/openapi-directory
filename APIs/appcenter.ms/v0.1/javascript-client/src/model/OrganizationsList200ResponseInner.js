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
 * The OrganizationsList200ResponseInner model module.
 * @module model/OrganizationsList200ResponseInner
 * @version v0.1
 */
class OrganizationsList200ResponseInner {
    /**
     * Constructs a new <code>OrganizationsList200ResponseInner</code>.
     * @alias module:model/OrganizationsList200ResponseInner
     * @param displayName {String} The display name of the organization
     * @param name {String} The slug name of the organization
     * @param origin {module:model/OrganizationsList200ResponseInner.OriginEnum} The creation origin of this organization
     */
    constructor(displayName, name, origin) { 
        
        OrganizationsList200ResponseInner.initialize(this, displayName, name, origin);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, displayName, name, origin) { 
        obj['display_name'] = displayName;
        obj['name'] = name;
        obj['origin'] = origin;
    }

    /**
     * Constructs a <code>OrganizationsList200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrganizationsList200ResponseInner} obj Optional instance to populate.
     * @return {module:model/OrganizationsList200ResponseInner} The populated <code>OrganizationsList200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrganizationsList200ResponseInner();

            if (data.hasOwnProperty('display_name')) {
                obj['display_name'] = ApiClient.convertToType(data['display_name'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('origin')) {
                obj['origin'] = ApiClient.convertToType(data['origin'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrganizationsList200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrganizationsList200ResponseInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OrganizationsList200ResponseInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['display_name'] && !(typeof data['display_name'] === 'string' || data['display_name'] instanceof String)) {
            throw new Error("Expected the field `display_name` to be a primitive type in the JSON string but got " + data['display_name']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['origin'] && !(typeof data['origin'] === 'string' || data['origin'] instanceof String)) {
            throw new Error("Expected the field `origin` to be a primitive type in the JSON string but got " + data['origin']);
        }

        return true;
    }


}

OrganizationsList200ResponseInner.RequiredProperties = ["display_name", "name", "origin"];

/**
 * The display name of the organization
 * @member {String} display_name
 */
OrganizationsList200ResponseInner.prototype['display_name'] = undefined;

/**
 * The slug name of the organization
 * @member {String} name
 */
OrganizationsList200ResponseInner.prototype['name'] = undefined;

/**
 * The creation origin of this organization
 * @member {module:model/OrganizationsList200ResponseInner.OriginEnum} origin
 */
OrganizationsList200ResponseInner.prototype['origin'] = undefined;





/**
 * Allowed values for the <code>origin</code> property.
 * @enum {String}
 * @readonly
 */
OrganizationsList200ResponseInner['OriginEnum'] = {

    /**
     * value: "appcenter"
     * @const
     */
    "appcenter": "appcenter",

    /**
     * value: "hockeyapp"
     * @const
     */
    "hockeyapp": "hockeyapp"
};



export default OrganizationsList200ResponseInner;

