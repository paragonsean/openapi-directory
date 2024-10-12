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
import CompanyCreditDataCreditLimitInterface from '../model/CompanyCreditDataCreditLimitInterface';
import ErrorResponse from '../model/ErrorResponse';

/**
* CompanyCreditsCompanyCompanyId service.
* @module api/CompanyCreditsCompanyCompanyIdApi
* @version 2.2.10
*/
export default class CompanyCreditsCompanyCompanyIdApi {

    /**
    * Constructs a new CompanyCreditsCompanyCompanyIdApi. 
    * @alias module:api/CompanyCreditsCompanyCompanyIdApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet operation.
     * @callback module:api/CompanyCreditsCompanyCompanyIdApi~companyCreditCreditLimitManagementV1GetCreditByCompanyIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompanyCreditDataCreditLimitInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * companyCredits/company/{companyId}
     * Returns data on the credit limit for a specified company.
     * @param {Number} companyId 
     * @param {module:api/CompanyCreditsCompanyCompanyIdApi~companyCreditCreditLimitManagementV1GetCreditByCompanyIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompanyCreditDataCreditLimitInterface}
     */
    companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet(companyId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet");
      }

      let pathParams = {
        'companyId': companyId
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
      let returnType = CompanyCreditDataCreditLimitInterface;
      return this.apiClient.callApi(
        '/V1/companyCredits/company/{companyId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
