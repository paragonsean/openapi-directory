/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ODataQueryContext from './ODataQueryContext';
import OrderByClause from './OrderByClause';
import OrderByNode from './OrderByNode';

/**
 * The OrderByQueryOption model module.
 * @module model/OrderByQueryOption
 * @version v1
 */
class OrderByQueryOption {
    /**
     * Constructs a new <code>OrderByQueryOption</code>.
     * @alias module:model/OrderByQueryOption
     */
    constructor() { 
        
        OrderByQueryOption.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OrderByQueryOption</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderByQueryOption} obj Optional instance to populate.
     * @return {module:model/OrderByQueryOption} The populated <code>OrderByQueryOption</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderByQueryOption();

            if (data.hasOwnProperty('Context')) {
                obj['Context'] = ODataQueryContext.constructFromObject(data['Context']);
            }
            if (data.hasOwnProperty('OrderByClause')) {
                obj['OrderByClause'] = OrderByClause.constructFromObject(data['OrderByClause']);
            }
            if (data.hasOwnProperty('OrderByNodes')) {
                obj['OrderByNodes'] = ApiClient.convertToType(data['OrderByNodes'], [OrderByNode]);
            }
            if (data.hasOwnProperty('RawValue')) {
                obj['RawValue'] = ApiClient.convertToType(data['RawValue'], 'String');
            }
            if (data.hasOwnProperty('Validator')) {
                obj['Validator'] = ApiClient.convertToType(data['Validator'], Object);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderByQueryOption</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderByQueryOption</code>.
     */
    static validateJSON(data) {
        // validate the optional field `Context`
        if (data['Context']) { // data not null
          ODataQueryContext.validateJSON(data['Context']);
        }
        // validate the optional field `OrderByClause`
        if (data['OrderByClause']) { // data not null
          OrderByClause.validateJSON(data['OrderByClause']);
        }
        if (data['OrderByNodes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['OrderByNodes'])) {
                throw new Error("Expected the field `OrderByNodes` to be an array in the JSON data but got " + data['OrderByNodes']);
            }
            // validate the optional field `OrderByNodes` (array)
            for (const item of data['OrderByNodes']) {
                OrderByNode.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['RawValue'] && !(typeof data['RawValue'] === 'string' || data['RawValue'] instanceof String)) {
            throw new Error("Expected the field `RawValue` to be a primitive type in the JSON string but got " + data['RawValue']);
        }

        return true;
    }


}



/**
 * @member {module:model/ODataQueryContext} Context
 */
OrderByQueryOption.prototype['Context'] = undefined;

/**
 * @member {module:model/OrderByClause} OrderByClause
 */
OrderByQueryOption.prototype['OrderByClause'] = undefined;

/**
 * @member {Array.<module:model/OrderByNode>} OrderByNodes
 */
OrderByQueryOption.prototype['OrderByNodes'] = undefined;

/**
 * @member {String} RawValue
 */
OrderByQueryOption.prototype['RawValue'] = undefined;

/**
 * @member {Object} Validator
 */
OrderByQueryOption.prototype['Validator'] = undefined;






export default OrderByQueryOption;

