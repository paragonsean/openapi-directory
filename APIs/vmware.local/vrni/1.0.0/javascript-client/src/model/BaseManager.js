/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BaseEntity from './BaseEntity';
import EntityType from './EntityType';

/**
 * The BaseManager model module.
 * @module model/BaseManager
 * @version 1.0.0
 */
class BaseManager {
    /**
     * Constructs a new <code>BaseManager</code>.
     * @alias module:model/BaseManager
     * @extends module:model/BaseEntity
     * @implements module:model/BaseEntity
     */
    constructor() { 
        BaseEntity.initialize(this);
        BaseManager.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BaseManager</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BaseManager} obj Optional instance to populate.
     * @return {module:model/BaseManager} The populated <code>BaseManager</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BaseManager();
            BaseEntity.constructFromObject(data, obj);
            BaseEntity.constructFromObject(data, obj);

        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BaseManager</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BaseManager</code>.
     */
    static validateJSON(data) {

        return true;
    }


}




// Implement BaseEntity interface:
/**
 * @member {String} entity_id
 */
BaseEntity.prototype['entity_id'] = undefined;
/**
 * @member {module:model/EntityType} entity_type
 */
BaseEntity.prototype['entity_type'] = undefined;
/**
 * @member {String} name
 */
BaseEntity.prototype['name'] = undefined;




export default BaseManager;

