/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AppServicePlansListVnets200ResponseInnerProperties from './AppServicePlansListVnets200ResponseInnerProperties';

/**
 * The AppServicePlansGetVnetFromServerFarm200Response model module.
 * @module model/AppServicePlansGetVnetFromServerFarm200Response
 * @version 2019-08-01
 */
class AppServicePlansGetVnetFromServerFarm200Response {
    /**
     * Constructs a new <code>AppServicePlansGetVnetFromServerFarm200Response</code>.
     * Virtual Network information contract.
     * @alias module:model/AppServicePlansGetVnetFromServerFarm200Response
     */
    constructor() { 
        
        AppServicePlansGetVnetFromServerFarm200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansGetVnetFromServerFarm200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansGetVnetFromServerFarm200Response} obj Optional instance to populate.
     * @return {module:model/AppServicePlansGetVnetFromServerFarm200Response} The populated <code>AppServicePlansGetVnetFromServerFarm200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansGetVnetFromServerFarm200Response();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = AppServicePlansListVnets200ResponseInnerProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('kind')) {
                obj['kind'] = ApiClient.convertToType(data['kind'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansGetVnetFromServerFarm200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansGetVnetFromServerFarm200Response</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          AppServicePlansListVnets200ResponseInnerProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['kind'] && !(typeof data['kind'] === 'string' || data['kind'] instanceof String)) {
            throw new Error("Expected the field `kind` to be a primitive type in the JSON string but got " + data['kind']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {module:model/AppServicePlansListVnets200ResponseInnerProperties} properties
 */
AppServicePlansGetVnetFromServerFarm200Response.prototype['properties'] = undefined;

/**
 * Resource Id.
 * @member {String} id
 */
AppServicePlansGetVnetFromServerFarm200Response.prototype['id'] = undefined;

/**
 * Kind of resource.
 * @member {String} kind
 */
AppServicePlansGetVnetFromServerFarm200Response.prototype['kind'] = undefined;

/**
 * Resource Name.
 * @member {String} name
 */
AppServicePlansGetVnetFromServerFarm200Response.prototype['name'] = undefined;

/**
 * Resource type.
 * @member {String} type
 */
AppServicePlansGetVnetFromServerFarm200Response.prototype['type'] = undefined;






export default AppServicePlansGetVnetFromServerFarm200Response;

