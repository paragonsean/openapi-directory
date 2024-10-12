/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ActivityEntryForApiContractPartialFindResult from '../model/ActivityEntryForApiContractPartialFindResult';
import ActivityEntryOptionalFields from '../model/ActivityEntryOptionalFields';
import ActivityEntrySortRule from '../model/ActivityEntrySortRule';
import ContentLanguagePreference from '../model/ContentLanguagePreference';
import EntryEditEvent from '../model/EntryEditEvent';
import EntryOptionalFields from '../model/EntryOptionalFields';
import EntryType from '../model/EntryType';

/**
* ActivityEntryApi service.
* @module api/ActivityEntryApiApi
* @version 1.0
*/
export default class ActivityEntryApiApi {

    /**
    * Constructs a new ActivityEntryApiApi. 
    * @alias module:api/ActivityEntryApiApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the apiActivityEntriesGet operation.
     * @callback module:api/ActivityEntryApiApi~apiActivityEntriesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActivityEntryForApiContractPartialFindResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {Date} [before] 
     * @param {Date} [since] 
     * @param {Number} [userId] 
     * @param {module:model/EntryEditEvent} [editEvent] 
     * @param {module:model/EntryType} [entryType] 
     * @param {Number} [maxResults = 50)] 
     * @param {Boolean} [getTotalCount = false)] 
     * @param {module:model/ActivityEntryOptionalFields} [fields] 
     * @param {module:model/EntryOptionalFields} [entryFields] 
     * @param {module:model/ContentLanguagePreference} [lang] 
     * @param {module:model/ActivityEntrySortRule} [sortRule] 
     * @param {module:api/ActivityEntryApiApi~apiActivityEntriesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActivityEntryForApiContractPartialFindResult}
     */
    apiActivityEntriesGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'before': opts['before'],
        'since': opts['since'],
        'userId': opts['userId'],
        'editEvent': opts['editEvent'],
        'entryType': opts['entryType'],
        'maxResults': opts['maxResults'],
        'getTotalCount': opts['getTotalCount'],
        'fields': opts['fields'],
        'entryFields': opts['entryFields'],
        'lang': opts['lang'],
        'sortRule': opts['sortRule']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'text/plain'];
      let returnType = ActivityEntryForApiContractPartialFindResult;
      return this.apiClient.callApi(
        '/api/activityEntries', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
