/**
 * agentOS API V3, Diary Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-diary
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The BaseHypermediaLink model module.
 * @module model/BaseHypermediaLink
 * @version v3-diary
 */
class BaseHypermediaLink {
    /**
     * Constructs a new <code>BaseHypermediaLink</code>.
     * Hypermedia Link Class
     * @alias module:model/BaseHypermediaLink
     */
    constructor() { 
        
        BaseHypermediaLink.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BaseHypermediaLink</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BaseHypermediaLink} obj Optional instance to populate.
     * @return {module:model/BaseHypermediaLink} The populated <code>BaseHypermediaLink</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BaseHypermediaLink();

            if (data.hasOwnProperty('Href')) {
                obj['Href'] = ApiClient.convertToType(data['Href'], 'String');
            }
            if (data.hasOwnProperty('Method')) {
                obj['Method'] = ApiClient.convertToType(data['Method'], 'String');
            }
            if (data.hasOwnProperty('Relationship')) {
                obj['Relationship'] = ApiClient.convertToType(data['Relationship'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BaseHypermediaLink</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BaseHypermediaLink</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Href'] && !(typeof data['Href'] === 'string' || data['Href'] instanceof String)) {
            throw new Error("Expected the field `Href` to be a primitive type in the JSON string but got " + data['Href']);
        }
        // ensure the json data is a string
        if (data['Method'] && !(typeof data['Method'] === 'string' || data['Method'] instanceof String)) {
            throw new Error("Expected the field `Method` to be a primitive type in the JSON string but got " + data['Method']);
        }
        // ensure the json data is a string
        if (data['Relationship'] && !(typeof data['Relationship'] === 'string' || data['Relationship'] instanceof String)) {
            throw new Error("Expected the field `Relationship` to be a primitive type in the JSON string but got " + data['Relationship']);
        }

        return true;
    }


}



/**
 * The hypermedia href
 * @member {String} Href
 */
BaseHypermediaLink.prototype['Href'] = undefined;

/**
 * The http method type
 * @member {String} Method
 */
BaseHypermediaLink.prototype['Method'] = undefined;

/**
 * The hypermedia link relationship to current result object.
 * @member {String} Relationship
 */
BaseHypermediaLink.prototype['Relationship'] = undefined;






export default BaseHypermediaLink;

