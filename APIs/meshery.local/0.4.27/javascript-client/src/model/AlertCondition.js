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
import AlertEvaluator from './AlertEvaluator';
import AlertOperator from './AlertOperator';
import AlertQuery from './AlertQuery';
import AlertReducer from './AlertReducer';

/**
 * The AlertCondition model module.
 * @module model/AlertCondition
 * @version 0.4.27
 */
class AlertCondition {
    /**
     * Constructs a new <code>AlertCondition</code>.
     * @alias module:model/AlertCondition
     */
    constructor() { 
        
        AlertCondition.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AlertCondition</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AlertCondition} obj Optional instance to populate.
     * @return {module:model/AlertCondition} The populated <code>AlertCondition</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AlertCondition();

            if (data.hasOwnProperty('evaluator')) {
                obj['evaluator'] = AlertEvaluator.constructFromObject(data['evaluator']);
            }
            if (data.hasOwnProperty('operator')) {
                obj['operator'] = AlertOperator.constructFromObject(data['operator']);
            }
            if (data.hasOwnProperty('query')) {
                obj['query'] = AlertQuery.constructFromObject(data['query']);
            }
            if (data.hasOwnProperty('reducer')) {
                obj['reducer'] = AlertReducer.constructFromObject(data['reducer']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AlertCondition</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AlertCondition</code>.
     */
    static validateJSON(data) {
        // validate the optional field `evaluator`
        if (data['evaluator']) { // data not null
          AlertEvaluator.validateJSON(data['evaluator']);
        }
        // validate the optional field `operator`
        if (data['operator']) { // data not null
          AlertOperator.validateJSON(data['operator']);
        }
        // validate the optional field `query`
        if (data['query']) { // data not null
          AlertQuery.validateJSON(data['query']);
        }
        // validate the optional field `reducer`
        if (data['reducer']) { // data not null
          AlertReducer.validateJSON(data['reducer']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {module:model/AlertEvaluator} evaluator
 */
AlertCondition.prototype['evaluator'] = undefined;

/**
 * @member {module:model/AlertOperator} operator
 */
AlertCondition.prototype['operator'] = undefined;

/**
 * @member {module:model/AlertQuery} query
 */
AlertCondition.prototype['query'] = undefined;

/**
 * @member {module:model/AlertReducer} reducer
 */
AlertCondition.prototype['reducer'] = undefined;

/**
 * @member {String} type
 */
AlertCondition.prototype['type'] = undefined;






export default AlertCondition;

