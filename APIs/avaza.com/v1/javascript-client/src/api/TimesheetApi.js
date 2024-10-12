/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import NewTimesheet from '../model/NewTimesheet';
import TimesheetDetails from '../model/TimesheetDetails';
import TimesheetList from '../model/TimesheetList';
import UpdateTimesheetModel from '../model/UpdateTimesheetModel';

/**
* Timesheet service.
* @module api/TimesheetApi
* @version v1
*/
export default class TimesheetApi {

    /**
    * Constructs a new TimesheetApi. 
    * @alias module:api/TimesheetApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the timesheetDelete operation.
     * @callback module:api/TimesheetApi~timesheetDeleteCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a Timesheet Entry
     * @param {Number} id The id of the timesheet entry to be deleted
     * @param {module:api/TimesheetApi~timesheetDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    timesheetDelete(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling timesheetDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/api/Timesheet/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the timesheetGet operation.
     * @callback module:api/TimesheetApi~timesheetGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TimesheetList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets list of Timsheets
     * @param {Object} opts Optional parameters
     * @param {Date} [updatedAfter] 
     * @param {Date} [entryDateFrom] 
     * @param {Date} [entryDateTo] 
     * @param {Number} [userID] The UserID of a timesheet user to filter timesheets for. Only api users with certain higher roles can see timesheets across multiple users.
     * @param {String} [userEmail] 
     * @param {String} [categoryName] 
     * @param {Number} [projectID] 
     * @param {Boolean} [isBillable] 
     * @param {Boolean} [isInvoiced] 
     * @param {Boolean} [isTimerRunning] 
     * @param {Number} [pageSize] Number of items per page (max 1000)
     * @param {Number} [pageNumber] Page to display. Starts from 1.
     * @param {Boolean} [includeInvoiceDetails] Defaults to false. When true, the InvoiceIDFK value will be included in the response.
     * @param {String} [sort] Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\",\"EntryDate\", \"EntryDate desc\", \"StartTimeLocal\",\"StartTimeLocal desc\", \"TimeSheetEntryID\", \"TimeSheetEntryID desc\"
     * @param {module:api/TimesheetApi~timesheetGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TimesheetList}
     */
    timesheetGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'UpdatedAfter': opts['updatedAfter'],
        'EntryDateFrom': opts['entryDateFrom'],
        'EntryDateTo': opts['entryDateTo'],
        'UserID': opts['userID'],
        'UserEmail': opts['userEmail'],
        'CategoryName': opts['categoryName'],
        'ProjectID': opts['projectID'],
        'isBillable': opts['isBillable'],
        'isInvoiced': opts['isInvoiced'],
        'isTimerRunning': opts['isTimerRunning'],
        'pageSize': opts['pageSize'],
        'pageNumber': opts['pageNumber'],
        'includeInvoiceDetails': opts['includeInvoiceDetails'],
        'Sort': opts['sort']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = TimesheetList;
      return this.apiClient.callApi(
        '/api/Timesheet', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the timesheetGetByID operation.
     * @callback module:api/TimesheetApi~timesheetGetByIDCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TimesheetDetails} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets a Timesheet Entry by Timesheet ID
     * @param {Number} id Timesheet ID number
     * @param {module:api/TimesheetApi~timesheetGetByIDCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TimesheetDetails}
     */
    timesheetGetByID(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling timesheetGetByID");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = TimesheetDetails;
      return this.apiClient.callApi(
        '/api/Timesheet/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the timesheetPost operation.
     * @callback module:api/TimesheetApi~timesheetPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TimesheetDetails} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new Timesheet Entry
     * @param {module:model/NewTimesheet} model 
     * @param {module:api/TimesheetApi~timesheetPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TimesheetDetails}
     */
    timesheetPost(model, callback) {
      let postBody = model;
      // verify the required parameter 'model' is set
      if (model === undefined || model === null) {
        throw new Error("Missing the required parameter 'model' when calling timesheetPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = TimesheetDetails;
      return this.apiClient.callApi(
        '/api/Timesheet', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the timesheetPut operation.
     * @callback module:api/TimesheetApi~timesheetPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TimesheetDetails} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a Timesheet
     * The FieldsToUpdate field expects a string array collection of the field names you would like updated. Valid fields to update inlcude \"ProjectIDFK\", \"TimeSheetCategoryIDFK\", \"TaskIDFK\", \"Duration\", \"EntryDate\", \"Notes\", \"hasStartEndTime\", \"CustomMetadata\". If you intend to provide start/end times on timesheets, this is achieved by including the start time in the EntryDate field (Iso date format), along with a Duration (decimal format).
     * @param {module:model/UpdateTimesheetModel} model 
     * @param {module:api/TimesheetApi~timesheetPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TimesheetDetails}
     */
    timesheetPut(model, callback) {
      let postBody = model;
      // verify the required parameter 'model' is set
      if (model === undefined || model === null) {
        throw new Error("Missing the required parameter 'model' when calling timesheetPut");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = TimesheetDetails;
      return this.apiClient.callApi(
        '/api/Timesheet', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
