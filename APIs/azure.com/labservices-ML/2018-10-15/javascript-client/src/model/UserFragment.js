/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Resource from './Resource';
import UserPropertiesFragment from './UserPropertiesFragment';

/**
 * The UserFragment model module.
 * @module model/UserFragment
 * @version 2018-10-15
 */
class UserFragment {
    /**
     * Constructs a new <code>UserFragment</code>.
     * The User registered to a lab
     * @alias module:model/UserFragment
     * @implements module:model/Resource
     */
    constructor() { 
        Resource.initialize(this);
        UserFragment.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UserFragment</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UserFragment} obj Optional instance to populate.
     * @return {module:model/UserFragment} The populated <code>UserFragment</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UserFragment();
            Resource.constructFromObject(data, obj);

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = UserPropertiesFragment.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('location')) {
                obj['location'] = ApiClient.convertToType(data['location'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], {'String': 'String'});
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UserFragment</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UserFragment</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          UserPropertiesFragment.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['location'] && !(typeof data['location'] === 'string' || data['location'] instanceof String)) {
            throw new Error("Expected the field `location` to be a primitive type in the JSON string but got " + data['location']);
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
 * @member {module:model/UserPropertiesFragment} properties
 */
UserFragment.prototype['properties'] = undefined;

/**
 * The identifier of the resource.
 * @member {String} id
 */
UserFragment.prototype['id'] = undefined;

/**
 * The location of the resource.
 * @member {String} location
 */
UserFragment.prototype['location'] = undefined;

/**
 * The name of the resource.
 * @member {String} name
 */
UserFragment.prototype['name'] = undefined;

/**
 * The tags of the resource.
 * @member {Object.<String, String>} tags
 */
UserFragment.prototype['tags'] = undefined;

/**
 * The type of the resource.
 * @member {String} type
 */
UserFragment.prototype['type'] = undefined;


// Implement Resource interface:
/**
 * The identifier of the resource.
 * @member {String} id
 */
Resource.prototype['id'] = undefined;
/**
 * The location of the resource.
 * @member {String} location
 */
Resource.prototype['location'] = undefined;
/**
 * The name of the resource.
 * @member {String} name
 */
Resource.prototype['name'] = undefined;
/**
 * The tags of the resource.
 * @member {Object.<String, String>} tags
 */
Resource.prototype['tags'] = undefined;
/**
 * The type of the resource.
 * @member {String} type
 */
Resource.prototype['type'] = undefined;




export default UserFragment;

