/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ErrorResponse from '../model/ErrorResponse';
import TaxDataTaxRuleInterface from '../model/TaxDataTaxRuleInterface';

/**
* TaxRulesRuleId service.
* @module api/TaxRulesRuleIdApi
* @version 2.2.10
*/
export default class TaxRulesRuleIdApi {

    /**
    * Constructs a new TaxRulesRuleIdApi. 
    * @alias module:api/TaxRulesRuleIdApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the taxTaxRuleRepositoryV1DeleteByIdDelete operation.
     * @callback module:api/TaxRulesRuleIdApi~taxTaxRuleRepositoryV1DeleteByIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {Boolean} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * taxRules/{ruleId}
     * Delete TaxRule
     * @param {Number} ruleId 
     * @param {module:api/TaxRulesRuleIdApi~taxTaxRuleRepositoryV1DeleteByIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Boolean}
     */
    taxTaxRuleRepositoryV1DeleteByIdDelete(ruleId, callback) {
      let postBody = null;
      // verify the required parameter 'ruleId' is set
      if (ruleId === undefined || ruleId === null) {
        throw new Error("Missing the required parameter 'ruleId' when calling taxTaxRuleRepositoryV1DeleteByIdDelete");
      }

      let pathParams = {
        'ruleId': ruleId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = 'Boolean';
      return this.apiClient.callApi(
        '/V1/taxRules/{ruleId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taxTaxRuleRepositoryV1GetGet operation.
     * @callback module:api/TaxRulesRuleIdApi~taxTaxRuleRepositoryV1GetGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaxDataTaxRuleInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * taxRules/{ruleId}
     * Get TaxRule
     * @param {Number} ruleId 
     * @param {module:api/TaxRulesRuleIdApi~taxTaxRuleRepositoryV1GetGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaxDataTaxRuleInterface}
     */
    taxTaxRuleRepositoryV1GetGet(ruleId, callback) {
      let postBody = null;
      // verify the required parameter 'ruleId' is set
      if (ruleId === undefined || ruleId === null) {
        throw new Error("Missing the required parameter 'ruleId' when calling taxTaxRuleRepositoryV1GetGet");
      }

      let pathParams = {
        'ruleId': ruleId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = TaxDataTaxRuleInterface;
      return this.apiClient.callApi(
        '/V1/taxRules/{ruleId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
