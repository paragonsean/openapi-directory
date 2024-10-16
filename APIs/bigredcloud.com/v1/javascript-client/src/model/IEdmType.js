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

/**
 * The IEdmType model module.
 * @module model/IEdmType
 * @version v1
 */
class IEdmType {
    /**
     * Constructs a new <code>IEdmType</code>.
     * @alias module:model/IEdmType
     */
    constructor() { 
        
        IEdmType.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IEdmType</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IEdmType} obj Optional instance to populate.
     * @return {module:model/IEdmType} The populated <code>IEdmType</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IEdmType();

            if (data.hasOwnProperty('TypeKind')) {
                obj['TypeKind'] = ApiClient.convertToType(data['TypeKind'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IEdmType</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IEdmType</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {module:model/IEdmType.TypeKindEnum} TypeKind
 */
IEdmType.prototype['TypeKind'] = undefined;





/**
 * Allowed values for the <code>TypeKind</code> property.
 * @enum {Number}
 * @readonly
 */
IEdmType['TypeKindEnum'] = {

    /**
     * value: 0
     * @const
     */
    "0": 0,

    /**
     * value: 1
     * @const
     */
    "1": 1,

    /**
     * value: 2
     * @const
     */
    "2": 2,

    /**
     * value: 3
     * @const
     */
    "3": 3,

    /**
     * value: 4
     * @const
     */
    "4": 4,

    /**
     * value: 5
     * @const
     */
    "5": 5,

    /**
     * value: 6
     * @const
     */
    "6": 6,

    /**
     * value: 7
     * @const
     */
    "7": 7
};



export default IEdmType;

