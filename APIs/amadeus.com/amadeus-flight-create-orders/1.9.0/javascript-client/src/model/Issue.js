/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import IssueSource from './IssueSource';

/**
 * The Issue model module.
 * @module model/Issue
 * @version 1.9.0
 */
class Issue {
    /**
     * Constructs a new <code>Issue</code>.
     * @alias module:model/Issue
     */
    constructor() { 
        
        Issue.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Issue</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Issue} obj Optional instance to populate.
     * @return {module:model/Issue} The populated <code>Issue</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Issue();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'Number');
            }
            if (data.hasOwnProperty('detail')) {
                obj['detail'] = ApiClient.convertToType(data['detail'], 'String');
            }
            if (data.hasOwnProperty('source')) {
                obj['source'] = IssueSource.constructFromObject(data['source']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'Number');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Issue</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Issue</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['detail'] && !(typeof data['detail'] === 'string' || data['detail'] instanceof String)) {
            throw new Error("Expected the field `detail` to be a primitive type in the JSON string but got " + data['detail']);
        }
        // validate the optional field `source`
        if (data['source']) { // data not null
          IssueSource.validateJSON(data['source']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }

        return true;
    }


}



/**
 * an application-specific error code
 * @member {Number} code
 */
Issue.prototype['code'] = undefined;

/**
 * explanation of the error
 * @member {String} detail
 */
Issue.prototype['detail'] = undefined;

/**
 * @member {module:model/IssueSource} source
 */
Issue.prototype['source'] = undefined;

/**
 * the HTTP status code applicable to this error
 * @member {Number} status
 */
Issue.prototype['status'] = undefined;

/**
 * a short summary of the error
 * @member {String} title
 */
Issue.prototype['title'] = undefined;






export default Issue;

