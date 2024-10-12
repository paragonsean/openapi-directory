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
import TimesheetSummaryResult from '../model/TimesheetSummaryResult';

/**
* TimesheetSummary service.
* @module api/TimesheetSummaryApi
* @version v1
*/
export default class TimesheetSummaryApi {

    /**
    * Constructs a new TimesheetSummaryApi. 
    * @alias module:api/TimesheetSummaryApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the timesheetSummaryGet operation.
     * @callback module:api/TimesheetSummaryApi~timesheetSummaryGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TimesheetSummaryResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets Basic Summary of Timesheet Statistics
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [modelGroupBy] (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \"Customer\", \"Project\", \"Category\", \"User\", \"Task\", \"Year\", \"Month\", \"Day\", \"Week\".
     * @param {Date} [modelEntryDateFrom] (Required) Filter for timesheets greater or equal to the specified date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00
     * @param {Date} [modelEntryDateTo] (Required) Filter for timesheets with an entry date smaller or equal to the specified  date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00
     * @param {Array.<Number>} [modelUserID] (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose timesheets should be retrieved. If the current user doesn't have impersonation rights, then they will only see their own data.
     * @param {Number} [modelProjectID] (Optional) Filter by Project
     * @param {Boolean} [modelIsBillable] (Optional) Filter by the billable status of Timesheets.
     * @param {Boolean} [modelIsInvoiced] (Optional) Filter for timesheets by whether they have been Invoiced or not.
     * @param {module:api/TimesheetSummaryApi~timesheetSummaryGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TimesheetSummaryResult}
     */
    timesheetSummaryGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'model.groupBy': this.apiClient.buildCollectionParam(opts['modelGroupBy'], 'multi'),
        'model.entryDateFrom': opts['modelEntryDateFrom'],
        'model.entryDateTo': opts['modelEntryDateTo'],
        'model.userID': this.apiClient.buildCollectionParam(opts['modelUserID'], 'multi'),
        'model.projectID': opts['modelProjectID'],
        'model.isBillable': opts['modelIsBillable'],
        'model.isInvoiced': opts['modelIsInvoiced']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = TimesheetSummaryResult;
      return this.apiClient.callApi(
        '/api/TimesheetSummary', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
