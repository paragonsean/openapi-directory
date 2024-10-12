/**
 * ApiManagementClient
 * Use this REST API to get all the issues across an Azure Api Management service.
 *
 * The version of the OpenAPI document: 2018-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import IssueListByServiceDefaultResponseError from './IssueListByServiceDefaultResponseError';

/**
 * The IssueListByServiceDefaultResponse model module.
 * @module model/IssueListByServiceDefaultResponse
 * @version 2018-01-01
 */
class IssueListByServiceDefaultResponse {
    /**
     * Constructs a new <code>IssueListByServiceDefaultResponse</code>.
     * Error Response.
     * @alias module:model/IssueListByServiceDefaultResponse
     */
    constructor() { 
        
        IssueListByServiceDefaultResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IssueListByServiceDefaultResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IssueListByServiceDefaultResponse} obj Optional instance to populate.
     * @return {module:model/IssueListByServiceDefaultResponse} The populated <code>IssueListByServiceDefaultResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IssueListByServiceDefaultResponse();

            if (data.hasOwnProperty('error')) {
                obj['error'] = IssueListByServiceDefaultResponseError.constructFromObject(data['error']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IssueListByServiceDefaultResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IssueListByServiceDefaultResponse</code>.
     */
    static validateJSON(data) {
        // validate the optional field `error`
        if (data['error']) { // data not null
          IssueListByServiceDefaultResponseError.validateJSON(data['error']);
        }

        return true;
    }


}



/**
 * @member {module:model/IssueListByServiceDefaultResponseError} error
 */
IssueListByServiceDefaultResponse.prototype['error'] = undefined;






export default IssueListByServiceDefaultResponse;

