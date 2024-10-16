/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GraphQLExtension model module.
 * @module model/GraphQLExtension
 * @version 0.4.27
 */
class GraphQLExtension {
    /**
     * Constructs a new <code>GraphQLExtension</code>.
     * GraphQLExtension describes the graphql server extension point in the backend
     * @alias module:model/GraphQLExtension
     */
    constructor() { 
        
        GraphQLExtension.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GraphQLExtension</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GraphQLExtension} obj Optional instance to populate.
     * @return {module:model/GraphQLExtension} The populated <code>GraphQLExtension</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GraphQLExtension();

            if (data.hasOwnProperty('component')) {
                obj['component'] = ApiClient.convertToType(data['component'], 'String');
            }
            if (data.hasOwnProperty('path')) {
                obj['path'] = ApiClient.convertToType(data['path'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GraphQLExtension</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GraphQLExtension</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['component'] && !(typeof data['component'] === 'string' || data['component'] instanceof String)) {
            throw new Error("Expected the field `component` to be a primitive type in the JSON string but got " + data['component']);
        }
        // ensure the json data is a string
        if (data['path'] && !(typeof data['path'] === 'string' || data['path'] instanceof String)) {
            throw new Error("Expected the field `path` to be a primitive type in the JSON string but got " + data['path']);
        }

        return true;
    }


}



/**
 * @member {String} component
 */
GraphQLExtension.prototype['component'] = undefined;

/**
 * @member {String} path
 */
GraphQLExtension.prototype['path'] = undefined;






export default GraphQLExtension;

