/**
 * agentOS Api V2, Customer Login Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-customer
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import LandlordAccountingModel from '../model/LandlordAccountingModel';
import LandlordCrmEntry from '../model/LandlordCrmEntry';
import LandlordMaintenanceModel from '../model/LandlordMaintenanceModel';
import LandlordProfitLossModel from '../model/LandlordProfitLossModel';
import LandlordRentArrearsModel from '../model/LandlordRentArrearsModel';
import LandlordSettingsModel from '../model/LandlordSettingsModel';
import LandlordSummaryModel from '../model/LandlordSummaryModel';
import LandlordTenancyModel from '../model/LandlordTenancyModel';

/**
* LandlordController service.
* @module api/LandlordControllerApi
* @version v2-customer
*/
export default class LandlordControllerApi {

    /**
    * Constructs a new LandlordControllerApi. 
    * @alias module:api/LandlordControllerApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the landlordControllerCreateMaintenancePreference operation.
     * @callback module:api/LandlordControllerApi~landlordControllerCreateMaintenancePreferenceCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Post tenancy maintenance preferences:-
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {String} tenancyID The Tenancy ID
     * @param {String} name Name of the maintenance preference to add
     * @param {String} notes Notes of the maintenance preference to add
     * @param {module:api/LandlordControllerApi~landlordControllerCreateMaintenancePreferenceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    landlordControllerCreateMaintenancePreference(shortName, token, tenancyID, name, notes, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerCreateMaintenancePreference");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerCreateMaintenancePreference");
      }
      // verify the required parameter 'tenancyID' is set
      if (tenancyID === undefined || tenancyID === null) {
        throw new Error("Missing the required parameter 'tenancyID' when calling landlordControllerCreateMaintenancePreference");
      }
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling landlordControllerCreateMaintenancePreference");
      }
      // verify the required parameter 'notes' is set
      if (notes === undefined || notes === null) {
        throw new Error("Missing the required parameter 'notes' when calling landlordControllerCreateMaintenancePreference");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token,
        'tenancyID': tenancyID,
        'name': name,
        'notes': notes
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/tenancy/maintenance/preference', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetAccounts operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetAccountsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LandlordAccountingModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the accounting details for the landlord.
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {module:api/LandlordControllerApi~landlordControllerGetAccountsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LandlordAccountingModel}
     */
    landlordControllerGetAccounts(shortName, token, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetAccounts");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetAccounts");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = LandlordAccountingModel;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/accounting', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetDocument operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetDocumentCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Download a Document
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {String} ID The Document ID
     * @param {module:api/LandlordControllerApi~landlordControllerGetDocumentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    landlordControllerGetDocument(shortName, token, ID, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetDocument");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetDocument");
      }
      // verify the required parameter 'ID' is set
      if (ID === undefined || ID === null) {
        throw new Error("Missing the required parameter 'ID' when calling landlordControllerGetDocument");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token,
        'ID': ID
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/document', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetInvetoryReport operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetInvetoryReportCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Generate a Inventory PDF for a tenancy
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {String} tenancyID The Tenancy ID
     * @param {module:api/LandlordControllerApi~landlordControllerGetInvetoryReportCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    landlordControllerGetInvetoryReport(shortName, token, tenancyID, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetInvetoryReport");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetInvetoryReport");
      }
      // verify the required parameter 'tenancyID' is set
      if (tenancyID === undefined || tenancyID === null) {
        throw new Error("Missing the required parameter 'tenancyID' when calling landlordControllerGetInvetoryReport");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token,
        'tenancyID': tenancyID
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/inventory', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetInvoice operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetInvoiceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get an invoice pdf belonging to the landlord.
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {String} invoiceID The invoice ID to load.
     * @param {module:api/LandlordControllerApi~landlordControllerGetInvoiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    landlordControllerGetInvoice(shortName, token, invoiceID, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetInvoice");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetInvoice");
      }
      // verify the required parameter 'invoiceID' is set
      if (invoiceID === undefined || invoiceID === null) {
        throw new Error("Missing the required parameter 'invoiceID' when calling landlordControllerGetInvoice");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token,
        'invoiceID': invoiceID
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/invoice', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetLandlordCrmEntries operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetLandlordCrmEntriesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/LandlordCrmEntry>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve landlord's CRM ID
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {module:api/LandlordControllerApi~landlordControllerGetLandlordCrmEntriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/LandlordCrmEntry>}
     */
    landlordControllerGetLandlordCrmEntries(shortName, token, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetLandlordCrmEntries");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetLandlordCrmEntries");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = [LandlordCrmEntry];
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/landlordcrmentries', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetMaintenanceJobs operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetMaintenanceJobsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LandlordMaintenanceModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Active maintenance jobs.
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {module:api/LandlordControllerApi~landlordControllerGetMaintenanceJobsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LandlordMaintenanceModel}
     */
    landlordControllerGetMaintenanceJobs(shortName, token, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetMaintenanceJobs");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetMaintenanceJobs");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = LandlordMaintenanceModel;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/maintenance', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetProfitLossReport operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetProfitLossReportCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LandlordProfitLossModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Generate a Profit and Loss Report
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {module:api/LandlordControllerApi~landlordControllerGetProfitLossReportCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LandlordProfitLossModel}
     */
    landlordControllerGetProfitLossReport(shortName, token, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetProfitLossReport");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetProfitLossReport");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = LandlordProfitLossModel;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/profitloss', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetRentArrears operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetRentArrearsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LandlordRentArrearsModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Rent Arrears
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {module:api/LandlordControllerApi~landlordControllerGetRentArrearsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LandlordRentArrearsModel}
     */
    landlordControllerGetRentArrears(shortName, token, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetRentArrears");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetRentArrears");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = LandlordRentArrearsModel;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/rentarrears', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetSASReport operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetSASReportCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Generate a Self Assessment Tax Report
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {Number} yearEnd The Tax Year End.
     * @param {module:api/LandlordControllerApi~landlordControllerGetSASReportCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    landlordControllerGetSASReport(shortName, token, yearEnd, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetSASReport");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetSASReport");
      }
      // verify the required parameter 'yearEnd' is set
      if (yearEnd === undefined || yearEnd === null) {
        throw new Error("Missing the required parameter 'yearEnd' when calling landlordControllerGetSASReport");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token,
        'yearEnd': yearEnd
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/sas', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetSettings operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetSettingsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LandlordSettingsModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get contact details of all linked landlords.
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {module:api/LandlordControllerApi~landlordControllerGetSettingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LandlordSettingsModel}
     */
    landlordControllerGetSettings(shortName, token, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetSettings");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetSettings");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = LandlordSettingsModel;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetSummaryDetails operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetSummaryDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LandlordSummaryModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the summary details for the landlord.
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {module:api/LandlordControllerApi~landlordControllerGetSummaryDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LandlordSummaryModel}
     */
    landlordControllerGetSummaryDetails(shortName, token, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetSummaryDetails");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetSummaryDetails");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = LandlordSummaryModel;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/summary', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetTenancy operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetTenancyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LandlordTenancyModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get tenancy details.
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {String} tenancyID The Tenancy ID
     * @param {module:api/LandlordControllerApi~landlordControllerGetTenancyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LandlordTenancyModel}
     */
    landlordControllerGetTenancy(shortName, token, tenancyID, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetTenancy");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetTenancy");
      }
      // verify the required parameter 'tenancyID' is set
      if (tenancyID === undefined || tenancyID === null) {
        throw new Error("Missing the required parameter 'tenancyID' when calling landlordControllerGetTenancy");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token,
        'tenancyID': tenancyID
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = LandlordTenancyModel;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/tenancy', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the landlordControllerGetTenancyAgreementReport operation.
     * @callback module:api/LandlordControllerApi~landlordControllerGetTenancyAgreementReportCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Generate a Tenancy Agreement Copy (PDF)
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {String} tenancyID The Tenancy ID
     * @param {module:api/LandlordControllerApi~landlordControllerGetTenancyAgreementReportCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    landlordControllerGetTenancyAgreementReport(shortName, token, tenancyID, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling landlordControllerGetTenancyAgreementReport");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling landlordControllerGetTenancyAgreementReport");
      }
      // verify the required parameter 'tenancyID' is set
      if (tenancyID === undefined || tenancyID === null) {
        throw new Error("Missing the required parameter 'tenancyID' when calling landlordControllerGetTenancyAgreementReport");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'token': token,
        'tenancyID': tenancyID
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/landlord/tenancyagreement', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
