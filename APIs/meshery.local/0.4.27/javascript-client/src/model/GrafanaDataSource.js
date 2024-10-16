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
 * The GrafanaDataSource model module.
 * @module model/GrafanaDataSource
 * @version 0.4.27
 */
class GrafanaDataSource {
    /**
     * Constructs a new <code>GrafanaDataSource</code>.
     * GrafanaDataSource represents a Grafana datasource like Prometheus
     * @alias module:model/GrafanaDataSource
     */
    constructor() { 
        
        GrafanaDataSource.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GrafanaDataSource</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GrafanaDataSource} obj Optional instance to populate.
     * @return {module:model/GrafanaDataSource} The populated <code>GrafanaDataSource</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GrafanaDataSource();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GrafanaDataSource</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GrafanaDataSource</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * @member {Number} id
 */
GrafanaDataSource.prototype['id'] = undefined;

/**
 * @member {String} name
 */
GrafanaDataSource.prototype['name'] = undefined;






export default GrafanaDataSource;

