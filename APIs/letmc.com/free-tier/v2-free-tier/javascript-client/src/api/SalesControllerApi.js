/**
 * LetMC Api V2, Free (Tier 1)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-free-tier
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import PhotoModelResults from '../model/PhotoModelResults';
import PropertyRoomModelResults from '../model/PropertyRoomModelResults';
import SalesFeatureModelResults from '../model/SalesFeatureModelResults';
import SalesFeatureTypeModel from '../model/SalesFeatureTypeModel';
import SalesFeatureTypeModelResults from '../model/SalesFeatureTypeModelResults';
import SalesInstructionModel from '../model/SalesInstructionModel';
import SalesInstructionModelResults from '../model/SalesInstructionModelResults';

/**
* SalesController service.
* @module api/SalesControllerApi
* @version v2-free-tier
*/
export default class SalesControllerApi {

    /**
    * Constructs a new SalesControllerApi. 
    * @alias module:api/SalesControllerApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the salesControllerGetAdvertisedSales operation.
     * @callback module:api/SalesControllerApi~salesControllerGetAdvertisedSalesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SalesInstructionModelResults} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Search all sales properties available given a range of search criteria
     * @param {String} shortName The unique client short-name
     * @param {String} branchID The unique ID of the Branch
     * @param {Number} offset The index of the first item to return
     * @param {Number} count The maximum number of items to return (up to 1000 per request)
     * @param {Boolean} onlyDevelopement Show only development properties?
     * @param {Boolean} onlyInvestements Show only investment properties?
     * @param {Object} opts Optional parameters
     * @param {Number} [minimumPrice] The minimum price to search for
     * @param {Number} [maximumPrice] The maximum price to search for
     * @param {Number} [minimumBeds] The minimum beds to search for
     * @param {Number} [minimumBathrooms] The minimum bathrooms to search for
     * @param {Number} [minimumEnsuites] The minimum ensuite bathrooms to search for
     * @param {Number} [minimumToilets] The minimum toilets to search for
     * @param {Number} [minimumReception] The minimum reception rooms to search for
     * @param {module:api/SalesControllerApi~salesControllerGetAdvertisedSalesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SalesInstructionModelResults}
     */
    salesControllerGetAdvertisedSales(shortName, branchID, offset, count, onlyDevelopement, onlyInvestements, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling salesControllerGetAdvertisedSales");
      }
      // verify the required parameter 'branchID' is set
      if (branchID === undefined || branchID === null) {
        throw new Error("Missing the required parameter 'branchID' when calling salesControllerGetAdvertisedSales");
      }
      // verify the required parameter 'offset' is set
      if (offset === undefined || offset === null) {
        throw new Error("Missing the required parameter 'offset' when calling salesControllerGetAdvertisedSales");
      }
      // verify the required parameter 'count' is set
      if (count === undefined || count === null) {
        throw new Error("Missing the required parameter 'count' when calling salesControllerGetAdvertisedSales");
      }
      // verify the required parameter 'onlyDevelopement' is set
      if (onlyDevelopement === undefined || onlyDevelopement === null) {
        throw new Error("Missing the required parameter 'onlyDevelopement' when calling salesControllerGetAdvertisedSales");
      }
      // verify the required parameter 'onlyInvestements' is set
      if (onlyInvestements === undefined || onlyInvestements === null) {
        throw new Error("Missing the required parameter 'onlyInvestements' when calling salesControllerGetAdvertisedSales");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'branchID': branchID,
        'offset': offset,
        'count': count,
        'onlyDevelopement': onlyDevelopement,
        'onlyInvestements': onlyInvestements,
        'minimumPrice': opts['minimumPrice'],
        'maximumPrice': opts['maximumPrice'],
        'minimumBeds': opts['minimumBeds'],
        'minimumBathrooms': opts['minimumBathrooms'],
        'minimumEnsuites': opts['minimumEnsuites'],
        'minimumToilets': opts['minimumToilets'],
        'minimumReception': opts['minimumReception']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = SalesInstructionModelResults;
      return this.apiClient.callApi(
        '/v2/tier1/{shortName}/sales/advertisedsales', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the salesControllerGetEER operation.
     * @callback module:api/SalesControllerApi~salesControllerGetEERCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Downloads the energy efficiency report (EER) graph for a sales instruction
     * @param {String} shortName The unique client short-name
     * @param {String} salesInstructionID The unique ID of the SalesInstruction
     * @param {module:api/SalesControllerApi~salesControllerGetEERCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    salesControllerGetEER(shortName, salesInstructionID, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling salesControllerGetEER");
      }
      // verify the required parameter 'salesInstructionID' is set
      if (salesInstructionID === undefined || salesInstructionID === null) {
        throw new Error("Missing the required parameter 'salesInstructionID' when calling salesControllerGetEER");
      }

      let pathParams = {
        'shortName': shortName,
        'salesInstructionID': salesInstructionID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v2/tier1/{shortName}/sales/reports/eer/{salesInstructionID}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the salesControllerGetEIR operation.
     * @callback module:api/SalesControllerApi~salesControllerGetEIRCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Downloads the energy efficiency report (EIR) graph for a sales instruction
     * @param {String} shortName The unique client short-name
     * @param {String} salesInstructionID The unique ID of the SalesInstruction
     * @param {module:api/SalesControllerApi~salesControllerGetEIRCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    salesControllerGetEIR(shortName, salesInstructionID, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling salesControllerGetEIR");
      }
      // verify the required parameter 'salesInstructionID' is set
      if (salesInstructionID === undefined || salesInstructionID === null) {
        throw new Error("Missing the required parameter 'salesInstructionID' when calling salesControllerGetEIR");
      }

      let pathParams = {
        'shortName': shortName,
        'salesInstructionID': salesInstructionID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/v2/tier1/{shortName}/sales/reports/eir/{salesInstructionID}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the salesControllerGetSalesInstructionsFeatures operation.
     * @callback module:api/SalesControllerApi~salesControllerGetSalesInstructionsFeaturesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SalesFeatureModelResults} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * A collection of all features linked to a sales instruction
     * @param {String} shortName The unique client short-name
     * @param {String} salesInstructionID The unique ID of the SalesInstruction
     * @param {Number} offset The index of the first item to return
     * @param {Number} count The maximum number of items to return (up to 1000 per request)
     * @param {module:api/SalesControllerApi~salesControllerGetSalesInstructionsFeaturesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SalesFeatureModelResults}
     */
    salesControllerGetSalesInstructionsFeatures(shortName, salesInstructionID, offset, count, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling salesControllerGetSalesInstructionsFeatures");
      }
      // verify the required parameter 'salesInstructionID' is set
      if (salesInstructionID === undefined || salesInstructionID === null) {
        throw new Error("Missing the required parameter 'salesInstructionID' when calling salesControllerGetSalesInstructionsFeatures");
      }
      // verify the required parameter 'offset' is set
      if (offset === undefined || offset === null) {
        throw new Error("Missing the required parameter 'offset' when calling salesControllerGetSalesInstructionsFeatures");
      }
      // verify the required parameter 'count' is set
      if (count === undefined || count === null) {
        throw new Error("Missing the required parameter 'count' when calling salesControllerGetSalesInstructionsFeatures");
      }

      let pathParams = {
        'shortName': shortName,
        'salesInstructionID': salesInstructionID
      };
      let queryParams = {
        'offset': offset,
        'count': count
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = SalesFeatureModelResults;
      return this.apiClient.callApi(
        '/v2/tier1/{shortName}/sales/salesinstructions/{salesInstructionID}/features', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the salesControllerGetSalesInstructionsFloorPlans operation.
     * @callback module:api/SalesControllerApi~salesControllerGetSalesInstructionsFloorPlansCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PhotoModelResults} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * A collection of floor plans linked to an instruction
     * @param {String} shortName The unique client short-name
     * @param {String} salesInstructionID The unique ID of the SalesInstruction
     * @param {Number} offset The index of the first item to return
     * @param {Number} count The maximum number of items to return (up to 1000 per request)
     * @param {module:api/SalesControllerApi~salesControllerGetSalesInstructionsFloorPlansCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PhotoModelResults}
     */
    salesControllerGetSalesInstructionsFloorPlans(shortName, salesInstructionID, offset, count, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling salesControllerGetSalesInstructionsFloorPlans");
      }
      // verify the required parameter 'salesInstructionID' is set
      if (salesInstructionID === undefined || salesInstructionID === null) {
        throw new Error("Missing the required parameter 'salesInstructionID' when calling salesControllerGetSalesInstructionsFloorPlans");
      }
      // verify the required parameter 'offset' is set
      if (offset === undefined || offset === null) {
        throw new Error("Missing the required parameter 'offset' when calling salesControllerGetSalesInstructionsFloorPlans");
      }
      // verify the required parameter 'count' is set
      if (count === undefined || count === null) {
        throw new Error("Missing the required parameter 'count' when calling salesControllerGetSalesInstructionsFloorPlans");
      }

      let pathParams = {
        'shortName': shortName,
        'salesInstructionID': salesInstructionID
      };
      let queryParams = {
        'offset': offset,
        'count': count
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = PhotoModelResults;
      return this.apiClient.callApi(
        '/v2/tier1/{shortName}/sales/salesinstructions/{salesInstructionID}/floorplans', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the salesControllerGetSalesInstructionsPhotos operation.
     * @callback module:api/SalesControllerApi~salesControllerGetSalesInstructionsPhotosCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PhotoModelResults} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * A collection of photos linked to an instruction
     * @param {String} shortName The unique client short-name
     * @param {String} salesInstructionID The unique ID of the SalesInstruction
     * @param {Number} offset The index of the first item to return
     * @param {Number} count The maximum number of items to return (up to 1000 per request)
     * @param {module:api/SalesControllerApi~salesControllerGetSalesInstructionsPhotosCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PhotoModelResults}
     */
    salesControllerGetSalesInstructionsPhotos(shortName, salesInstructionID, offset, count, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling salesControllerGetSalesInstructionsPhotos");
      }
      // verify the required parameter 'salesInstructionID' is set
      if (salesInstructionID === undefined || salesInstructionID === null) {
        throw new Error("Missing the required parameter 'salesInstructionID' when calling salesControllerGetSalesInstructionsPhotos");
      }
      // verify the required parameter 'offset' is set
      if (offset === undefined || offset === null) {
        throw new Error("Missing the required parameter 'offset' when calling salesControllerGetSalesInstructionsPhotos");
      }
      // verify the required parameter 'count' is set
      if (count === undefined || count === null) {
        throw new Error("Missing the required parameter 'count' when calling salesControllerGetSalesInstructionsPhotos");
      }

      let pathParams = {
        'shortName': shortName,
        'salesInstructionID': salesInstructionID
      };
      let queryParams = {
        'offset': offset,
        'count': count
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = PhotoModelResults;
      return this.apiClient.callApi(
        '/v2/tier1/{shortName}/sales/salesinstructions/{salesInstructionID}/photos', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the salesControllerGetSalesInstructionsRooms operation.
     * @callback module:api/SalesControllerApi~salesControllerGetSalesInstructionsRoomsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PropertyRoomModelResults} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * A collection of rooms linked to an instruction
     * @param {String} shortName The unique client short-name
     * @param {String} salesInstructionID The unique ID of the SalesInstruction
     * @param {Number} offset The index of the first item to return
     * @param {Number} count The maximum number of items to return (up to 1000 per request)
     * @param {module:api/SalesControllerApi~salesControllerGetSalesInstructionsRoomsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PropertyRoomModelResults}
     */
    salesControllerGetSalesInstructionsRooms(shortName, salesInstructionID, offset, count, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling salesControllerGetSalesInstructionsRooms");
      }
      // verify the required parameter 'salesInstructionID' is set
      if (salesInstructionID === undefined || salesInstructionID === null) {
        throw new Error("Missing the required parameter 'salesInstructionID' when calling salesControllerGetSalesInstructionsRooms");
      }
      // verify the required parameter 'offset' is set
      if (offset === undefined || offset === null) {
        throw new Error("Missing the required parameter 'offset' when calling salesControllerGetSalesInstructionsRooms");
      }
      // verify the required parameter 'count' is set
      if (count === undefined || count === null) {
        throw new Error("Missing the required parameter 'count' when calling salesControllerGetSalesInstructionsRooms");
      }

      let pathParams = {
        'shortName': shortName,
        'salesInstructionID': salesInstructionID
      };
      let queryParams = {
        'offset': offset,
        'count': count
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = PropertyRoomModelResults;
      return this.apiClient.callApi(
        '/v2/tier1/{shortName}/sales/salesinstructions/{salesInstructionID}/rooms', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v2Tier1ShortNameSalesSalesfeaturetypesGet operation.
     * @callback module:api/SalesControllerApi~v2Tier1ShortNameSalesSalesfeaturetypesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SalesFeatureTypeModelResults} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * A collection of all sales feature types linked to a company
     * @param {String} shortName The unique client short-name
     * @param {Number} offset The index of the first item to return
     * @param {Number} count The maximum number of items to return (up to 1000 per request)
     * @param {module:api/SalesControllerApi~v2Tier1ShortNameSalesSalesfeaturetypesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SalesFeatureTypeModelResults}
     */
    v2Tier1ShortNameSalesSalesfeaturetypesGet(shortName, offset, count, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling v2Tier1ShortNameSalesSalesfeaturetypesGet");
      }
      // verify the required parameter 'offset' is set
      if (offset === undefined || offset === null) {
        throw new Error("Missing the required parameter 'offset' when calling v2Tier1ShortNameSalesSalesfeaturetypesGet");
      }
      // verify the required parameter 'count' is set
      if (count === undefined || count === null) {
        throw new Error("Missing the required parameter 'count' when calling v2Tier1ShortNameSalesSalesfeaturetypesGet");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'offset': offset,
        'count': count
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = SalesFeatureTypeModelResults;
      return this.apiClient.callApi(
        '/v2/tier1/{shortName}/sales/salesfeaturetypes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet operation.
     * @callback module:api/SalesControllerApi~v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SalesFeatureTypeModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a specific sales feature type given its unique Object ID (OID)
     * @param {String} shortName The unique client short-name
     * @param {String} salesFeatureTypeID The unique ID of the SalesFeatureType
     * @param {module:api/SalesControllerApi~v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SalesFeatureTypeModel}
     */
    v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet(shortName, salesFeatureTypeID, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet");
      }
      // verify the required parameter 'salesFeatureTypeID' is set
      if (salesFeatureTypeID === undefined || salesFeatureTypeID === null) {
        throw new Error("Missing the required parameter 'salesFeatureTypeID' when calling v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet");
      }

      let pathParams = {
        'shortName': shortName,
        'salesFeatureTypeID': salesFeatureTypeID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = SalesFeatureTypeModel;
      return this.apiClient.callApi(
        '/v2/tier1/{shortName}/sales/salesfeaturetypes/{salesFeatureTypeID}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v2Tier1ShortNameSalesSalesinstructionsGet operation.
     * @callback module:api/SalesControllerApi~v2Tier1ShortNameSalesSalesinstructionsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SalesInstructionModelResults} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * A collection of all sales instructions linked to a company
     * @param {String} shortName The unique client short-name
     * @param {Number} offset The index of the first item to return
     * @param {Number} count The maximum number of items to return (up to 1000 per request)
     * @param {module:api/SalesControllerApi~v2Tier1ShortNameSalesSalesinstructionsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SalesInstructionModelResults}
     */
    v2Tier1ShortNameSalesSalesinstructionsGet(shortName, offset, count, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling v2Tier1ShortNameSalesSalesinstructionsGet");
      }
      // verify the required parameter 'offset' is set
      if (offset === undefined || offset === null) {
        throw new Error("Missing the required parameter 'offset' when calling v2Tier1ShortNameSalesSalesinstructionsGet");
      }
      // verify the required parameter 'count' is set
      if (count === undefined || count === null) {
        throw new Error("Missing the required parameter 'count' when calling v2Tier1ShortNameSalesSalesinstructionsGet");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'offset': offset,
        'count': count
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = SalesInstructionModelResults;
      return this.apiClient.callApi(
        '/v2/tier1/{shortName}/sales/salesinstructions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGet operation.
     * @callback module:api/SalesControllerApi~v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SalesInstructionModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a specific sales instruction given its unique Object ID (OID)
     * @param {String} shortName The unique client short-name
     * @param {String} salesInstructionID The unique ID of the SalesInstruction
     * @param {module:api/SalesControllerApi~v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SalesInstructionModel}
     */
    v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGet(shortName, salesInstructionID, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGet");
      }
      // verify the required parameter 'salesInstructionID' is set
      if (salesInstructionID === undefined || salesInstructionID === null) {
        throw new Error("Missing the required parameter 'salesInstructionID' when calling v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGet");
      }

      let pathParams = {
        'shortName': shortName,
        'salesInstructionID': salesInstructionID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = SalesInstructionModel;
      return this.apiClient.callApi(
        '/v2/tier1/{shortName}/sales/salesinstructions/{salesInstructionID}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
