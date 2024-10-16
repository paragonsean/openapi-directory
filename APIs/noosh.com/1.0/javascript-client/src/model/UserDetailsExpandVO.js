/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import UserDetailsVO from './UserDetailsVO';

/**
 * The UserDetailsExpandVO model module.
 * @module model/UserDetailsExpandVO
 * @version 1.0
 */
class UserDetailsExpandVO {
    /**
     * Constructs a new <code>UserDetailsExpandVO</code>.
     * Java type: com.noosh.nooshapi.vo.UserDetailsExpandVO
     * @alias module:model/UserDetailsExpandVO
     */
    constructor() { 
        
        UserDetailsExpandVO.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UserDetailsExpandVO</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UserDetailsExpandVO} obj Optional instance to populate.
     * @return {module:model/UserDetailsExpandVO} The populated <code>UserDetailsExpandVO</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UserDetailsExpandVO();

            if (data.hasOwnProperty('result')) {
                obj['result'] = UserDetailsVO.constructFromObject(data['result']);
            }
            if (data.hasOwnProperty('status_code')) {
                obj['status_code'] = ApiClient.convertToType(data['status_code'], 'Number');
            }
            if (data.hasOwnProperty('status_reason')) {
                obj['status_reason'] = ApiClient.convertToType(data['status_reason'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UserDetailsExpandVO</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UserDetailsExpandVO</code>.
     */
    static validateJSON(data) {
        // validate the optional field `result`
        if (data['result']) { // data not null
          UserDetailsVO.validateJSON(data['result']);
        }
        // ensure the json data is a string
        if (data['status_reason'] && !(typeof data['status_reason'] === 'string' || data['status_reason'] instanceof String)) {
            throw new Error("Expected the field `status_reason` to be a primitive type in the JSON string but got " + data['status_reason']);
        }

        return true;
    }


}



/**
 * @member {module:model/UserDetailsVO} result
 */
UserDetailsExpandVO.prototype['result'] = undefined;

/**
 * 
 * @member {Number} status_code
 */
UserDetailsExpandVO.prototype['status_code'] = undefined;

/**
 * 
 * @member {String} status_reason
 */
UserDetailsExpandVO.prototype['status_reason'] = undefined;






export default UserDetailsExpandVO;

