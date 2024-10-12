/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
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
import AccountResource from './AccountResource';

/**
 * The GetAccountResponse model module.
 * @module model/GetAccountResponse
 * @version v1
 */
class GetAccountResponse {
    /**
     * Constructs a new <code>GetAccountResponse</code>.
     * Successful response to get a single account. 
     * @alias module:model/GetAccountResponse
     * @param data {module:model/AccountResource} The account returned in this response. 
     */
    constructor(data) { 
        
        GetAccountResponse.initialize(this, data);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, data) { 
        obj['data'] = data;
    }

    /**
     * Constructs a <code>GetAccountResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetAccountResponse} obj Optional instance to populate.
     * @return {module:model/GetAccountResponse} The populated <code>GetAccountResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetAccountResponse();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ApiClient.convertToType(data['data'], AccountResource);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetAccountResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetAccountResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GetAccountResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `data`
        if (data['data']) { // data not null
          AccountResource.validateJSON(data['data']);
        }

        return true;
    }


}

GetAccountResponse.RequiredProperties = ["data"];

/**
 * The account returned in this response. 
 * @member {module:model/AccountResource} data
 */
GetAccountResponse.prototype['data'] = undefined;






export default GetAccountResponse;

