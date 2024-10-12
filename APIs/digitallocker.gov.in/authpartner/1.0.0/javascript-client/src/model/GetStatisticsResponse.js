/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import GetStatisticsResponseMonthwiseRegistations from './GetStatisticsResponseMonthwiseRegistations';
import GetStatisticsResponseYearwiseAuthenticDocuments from './GetStatisticsResponseYearwiseAuthenticDocuments';

/**
 * The GetStatisticsResponse model module.
 * @module model/GetStatisticsResponse
 * @version 1.0.0
 */
class GetStatisticsResponse {
    /**
     * Constructs a new <code>GetStatisticsResponse</code>.
     * @alias module:model/GetStatisticsResponse
     * @param authenticDocuments {String} Count of authentic documents available through DigiLocker.
     * @param countAsOn {String} The date on which this statistics is generated.
     * @param issuers {String} Count of issuer organizations registered on DigiLocker.
     * @param monthwiseRegistations {module:model/GetStatisticsResponseMonthwiseRegistations} 
     * @param requestors {String} Count of requester organizations registered on DigiLocker.
     * @param users {String} Count of registered users on DigiLocker.
     * @param yearwiseAuthenticDocuments {module:model/GetStatisticsResponseYearwiseAuthenticDocuments} 
     */
    constructor(authenticDocuments, countAsOn, issuers, monthwiseRegistations, requestors, users, yearwiseAuthenticDocuments) { 
        
        GetStatisticsResponse.initialize(this, authenticDocuments, countAsOn, issuers, monthwiseRegistations, requestors, users, yearwiseAuthenticDocuments);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, authenticDocuments, countAsOn, issuers, monthwiseRegistations, requestors, users, yearwiseAuthenticDocuments) { 
        obj['authentic_documents'] = authenticDocuments;
        obj['count_as_on'] = countAsOn;
        obj['issuers'] = issuers;
        obj['monthwise_registations'] = monthwiseRegistations;
        obj['requestors'] = requestors;
        obj['users'] = users;
        obj['yearwise_authentic_documents'] = yearwiseAuthenticDocuments;
    }

    /**
     * Constructs a <code>GetStatisticsResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetStatisticsResponse} obj Optional instance to populate.
     * @return {module:model/GetStatisticsResponse} The populated <code>GetStatisticsResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetStatisticsResponse();

            if (data.hasOwnProperty('authentic_documents')) {
                obj['authentic_documents'] = ApiClient.convertToType(data['authentic_documents'], 'String');
            }
            if (data.hasOwnProperty('count_as_on')) {
                obj['count_as_on'] = ApiClient.convertToType(data['count_as_on'], 'String');
            }
            if (data.hasOwnProperty('issuers')) {
                obj['issuers'] = ApiClient.convertToType(data['issuers'], 'String');
            }
            if (data.hasOwnProperty('monthwise_registations')) {
                obj['monthwise_registations'] = GetStatisticsResponseMonthwiseRegistations.constructFromObject(data['monthwise_registations']);
            }
            if (data.hasOwnProperty('requestors')) {
                obj['requestors'] = ApiClient.convertToType(data['requestors'], 'String');
            }
            if (data.hasOwnProperty('users')) {
                obj['users'] = ApiClient.convertToType(data['users'], 'String');
            }
            if (data.hasOwnProperty('yearwise_authentic_documents')) {
                obj['yearwise_authentic_documents'] = GetStatisticsResponseYearwiseAuthenticDocuments.constructFromObject(data['yearwise_authentic_documents']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetStatisticsResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetStatisticsResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GetStatisticsResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['authentic_documents'] && !(typeof data['authentic_documents'] === 'string' || data['authentic_documents'] instanceof String)) {
            throw new Error("Expected the field `authentic_documents` to be a primitive type in the JSON string but got " + data['authentic_documents']);
        }
        // ensure the json data is a string
        if (data['count_as_on'] && !(typeof data['count_as_on'] === 'string' || data['count_as_on'] instanceof String)) {
            throw new Error("Expected the field `count_as_on` to be a primitive type in the JSON string but got " + data['count_as_on']);
        }
        // ensure the json data is a string
        if (data['issuers'] && !(typeof data['issuers'] === 'string' || data['issuers'] instanceof String)) {
            throw new Error("Expected the field `issuers` to be a primitive type in the JSON string but got " + data['issuers']);
        }
        // validate the optional field `monthwise_registations`
        if (data['monthwise_registations']) { // data not null
          GetStatisticsResponseMonthwiseRegistations.validateJSON(data['monthwise_registations']);
        }
        // ensure the json data is a string
        if (data['requestors'] && !(typeof data['requestors'] === 'string' || data['requestors'] instanceof String)) {
            throw new Error("Expected the field `requestors` to be a primitive type in the JSON string but got " + data['requestors']);
        }
        // ensure the json data is a string
        if (data['users'] && !(typeof data['users'] === 'string' || data['users'] instanceof String)) {
            throw new Error("Expected the field `users` to be a primitive type in the JSON string but got " + data['users']);
        }
        // validate the optional field `yearwise_authentic_documents`
        if (data['yearwise_authentic_documents']) { // data not null
          GetStatisticsResponseYearwiseAuthenticDocuments.validateJSON(data['yearwise_authentic_documents']);
        }

        return true;
    }


}

GetStatisticsResponse.RequiredProperties = ["authentic_documents", "count_as_on", "issuers", "monthwise_registations", "requestors", "users", "yearwise_authentic_documents"];

/**
 * Count of authentic documents available through DigiLocker.
 * @member {String} authentic_documents
 */
GetStatisticsResponse.prototype['authentic_documents'] = undefined;

/**
 * The date on which this statistics is generated.
 * @member {String} count_as_on
 */
GetStatisticsResponse.prototype['count_as_on'] = undefined;

/**
 * Count of issuer organizations registered on DigiLocker.
 * @member {String} issuers
 */
GetStatisticsResponse.prototype['issuers'] = undefined;

/**
 * @member {module:model/GetStatisticsResponseMonthwiseRegistations} monthwise_registations
 */
GetStatisticsResponse.prototype['monthwise_registations'] = undefined;

/**
 * Count of requester organizations registered on DigiLocker.
 * @member {String} requestors
 */
GetStatisticsResponse.prototype['requestors'] = undefined;

/**
 * Count of registered users on DigiLocker.
 * @member {String} users
 */
GetStatisticsResponse.prototype['users'] = undefined;

/**
 * @member {module:model/GetStatisticsResponseYearwiseAuthenticDocuments} yearwise_authentic_documents
 */
GetStatisticsResponse.prototype['yearwise_authentic_documents'] = undefined;






export default GetStatisticsResponse;

