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
 * The Gauge model module.
 * @module model/Gauge
 * @version 0.4.27
 */
class Gauge {
    /**
     * Constructs a new <code>Gauge</code>.
     * for a stat
     * @alias module:model/Gauge
     */
    constructor() { 
        
        Gauge.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Gauge</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Gauge} obj Optional instance to populate.
     * @return {module:model/Gauge} The populated <code>Gauge</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Gauge();

            if (data.hasOwnProperty('maxValue')) {
                obj['maxValue'] = ApiClient.convertToType(data['maxValue'], 'Number');
            }
            if (data.hasOwnProperty('minValue')) {
                obj['minValue'] = ApiClient.convertToType(data['minValue'], 'Number');
            }
            if (data.hasOwnProperty('show')) {
                obj['show'] = ApiClient.convertToType(data['show'], 'Boolean');
            }
            if (data.hasOwnProperty('thresholdLabels')) {
                obj['thresholdLabels'] = ApiClient.convertToType(data['thresholdLabels'], 'Boolean');
            }
            if (data.hasOwnProperty('thresholdMarkers')) {
                obj['thresholdMarkers'] = ApiClient.convertToType(data['thresholdMarkers'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Gauge</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Gauge</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Number} maxValue
 */
Gauge.prototype['maxValue'] = undefined;

/**
 * @member {Number} minValue
 */
Gauge.prototype['minValue'] = undefined;

/**
 * @member {Boolean} show
 */
Gauge.prototype['show'] = undefined;

/**
 * @member {Boolean} thresholdLabels
 */
Gauge.prototype['thresholdLabels'] = undefined;

/**
 * @member {Boolean} thresholdMarkers
 */
Gauge.prototype['thresholdMarkers'] = undefined;






export default Gauge;

