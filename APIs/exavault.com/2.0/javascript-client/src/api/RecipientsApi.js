/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ResendInvitationsRequestBody from '../model/ResendInvitationsRequestBody';
import ShareRecipientsResponse from '../model/ShareRecipientsResponse';

/**
* Recipients service.
* @module api/RecipientsApi
* @version 2.0
*/
export default class RecipientsApi {

    /**
    * Constructs a new RecipientsApi. 
    * @alias module:api/RecipientsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the resendInvitationsForShare operation.
     * @callback module:api/RecipientsApi~resendInvitationsForShareCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ShareRecipientsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Resend invitations to share recipients
     * Resend invitations to one or all recipients attached to specified share. The most recent message that was sent for the share will be re-used for this email.  You can use [GET /shares/{id}](#operation/getShareById) to view the recipient list and message history for a share. Use [PATCH /shares/{id}](#operation/updateShareById) to add or remove recipients.
     * @param {String} evApiKey API Key required to make the API call.
     * @param {String} evAccessToken Access token required to make the API call.
     * @param {Number} shareId ID of the share to resend invites for.
     * @param {Object} opts Optional parameters
     * @param {module:model/ResendInvitationsRequestBody} [resendInvitationsRequestBody] 
     * @param {module:api/RecipientsApi~resendInvitationsForShareCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ShareRecipientsResponse}
     */
    resendInvitationsForShare(evApiKey, evAccessToken, shareId, opts, callback) {
      opts = opts || {};
      let postBody = opts['resendInvitationsRequestBody'];
      // verify the required parameter 'evApiKey' is set
      if (evApiKey === undefined || evApiKey === null) {
        throw new Error("Missing the required parameter 'evApiKey' when calling resendInvitationsForShare");
      }
      // verify the required parameter 'evAccessToken' is set
      if (evAccessToken === undefined || evAccessToken === null) {
        throw new Error("Missing the required parameter 'evAccessToken' when calling resendInvitationsForShare");
      }
      // verify the required parameter 'shareId' is set
      if (shareId === undefined || shareId === null) {
        throw new Error("Missing the required parameter 'shareId' when calling resendInvitationsForShare");
      }

      let pathParams = {
        'shareId': shareId
      };
      let queryParams = {
      };
      let headerParams = {
        'ev-api-key': evApiKey,
        'ev-access-token': evAccessToken
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ShareRecipientsResponse;
      return this.apiClient.callApi(
        '/recipients/shares/invites/{shareId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
