/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ErrorResponse from '../model/ErrorResponse';
import SubscriptionPlanRequest from '../model/SubscriptionPlanRequest';
import SubscriptionPlanResponse from '../model/SubscriptionPlanResponse';

/**
* Internal service.
* @module api/InternalApi
* @version 4.42.3
*/
export default class InternalApi {

    /**
    * Constructs a new InternalApi. 
    * @alias module:api/InternalApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the internalRequestSubscriptionPlan operation.
     * @callback module:api/InternalApi~internalRequestSubscriptionPlanCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SubscriptionPlanResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request subscription plan
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.36.0</h3>  ### Description: Get the subscription plan id of the current tenant  ### Precondition: Valid `X-SDS-Service-Token` Header  ### Postcondition: Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 
     * @param {String} xSdsServiceToken Service Authentication token
     * @param {module:api/InternalApi~internalRequestSubscriptionPlanCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SubscriptionPlanResponse}
     */
    internalRequestSubscriptionPlan(xSdsServiceToken, callback) {
      let postBody = null;
      // verify the required parameter 'xSdsServiceToken' is set
      if (xSdsServiceToken === undefined || xSdsServiceToken === null) {
        throw new Error("Missing the required parameter 'xSdsServiceToken' when calling internalRequestSubscriptionPlan");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Service-Token': xSdsServiceToken
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SubscriptionPlanResponse;
      return this.apiClient.callApi(
        '/v4/internal/tenant/subscription_plan', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the internalSetSubscriptionPlan operation.
     * @callback module:api/InternalApi~internalSetSubscriptionPlanCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SubscriptionPlanResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set subscription plan
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.36.0</h3>  ### Description:  Change the subscription plan id of the current tenant  ### Precondition: Valid `X-SDS-Service-Token` Header  ### Postcondition: The subscription plan of the current tenant is set to the given value.   Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 
     * @param {String} xSdsServiceToken Service Authentication token
     * @param {module:model/SubscriptionPlanRequest} subscriptionPlanRequest 
     * @param {module:api/InternalApi~internalSetSubscriptionPlanCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SubscriptionPlanResponse}
     */
    internalSetSubscriptionPlan(xSdsServiceToken, subscriptionPlanRequest, callback) {
      let postBody = subscriptionPlanRequest;
      // verify the required parameter 'xSdsServiceToken' is set
      if (xSdsServiceToken === undefined || xSdsServiceToken === null) {
        throw new Error("Missing the required parameter 'xSdsServiceToken' when calling internalSetSubscriptionPlan");
      }
      // verify the required parameter 'subscriptionPlanRequest' is set
      if (subscriptionPlanRequest === undefined || subscriptionPlanRequest === null) {
        throw new Error("Missing the required parameter 'subscriptionPlanRequest' when calling internalSetSubscriptionPlan");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Service-Token': xSdsServiceToken
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = SubscriptionPlanResponse;
      return this.apiClient.callApi(
        '/v4/internal/tenant/subscription_plan', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
