/**
 * Background Removal API
 * Remove the background of any image
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
import AccountGet200ResponseDataAttributes from './AccountGet200ResponseDataAttributes';

/**
 * The AccountGet200ResponseData model module.
 * @module model/AccountGet200ResponseData
 * @version 1.0.0
 */
class AccountGet200ResponseData {
    /**
     * Constructs a new <code>AccountGet200ResponseData</code>.
     * @alias module:model/AccountGet200ResponseData
     */
    constructor() { 
        
        AccountGet200ResponseData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AccountGet200ResponseData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccountGet200ResponseData} obj Optional instance to populate.
     * @return {module:model/AccountGet200ResponseData} The populated <code>AccountGet200ResponseData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccountGet200ResponseData();

            if (data.hasOwnProperty('attributes')) {
                obj['attributes'] = AccountGet200ResponseDataAttributes.constructFromObject(data['attributes']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccountGet200ResponseData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccountGet200ResponseData</code>.
     */
    static validateJSON(data) {
        // validate the optional field `attributes`
        if (data['attributes']) { // data not null
          AccountGet200ResponseDataAttributes.validateJSON(data['attributes']);
        }

        return true;
    }


}



/**
 * @member {module:model/AccountGet200ResponseDataAttributes} attributes
 */
AccountGet200ResponseData.prototype['attributes'] = undefined;






export default AccountGet200ResponseData;

