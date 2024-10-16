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
import LandlordPhotoModelResults from '../model/LandlordPhotoModelResults';

/**
* PropertyController service.
* @module api/PropertyControllerApi
* @version v2-customer
*/
export default class PropertyControllerApi {

    /**
    * Constructs a new PropertyControllerApi. 
    * @alias module:api/PropertyControllerApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the propertyControllerGetPropertiesPhotos operation.
     * @callback module:api/PropertyControllerApi~propertyControllerGetPropertiesPhotosCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LandlordPhotoModelResults} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * A collection showing all the photos linked to a specific block, property or room
     * @param {String} shortName The unique client short-name
     * @param {String} token The login token returned from the /session POST call
     * @param {String} propertyID The unique ID of the Property
     * @param {Number} offset The index of the first item to return
     * @param {Number} count The maximum number of items to return (up to 1000 per request)
     * @param {module:api/PropertyControllerApi~propertyControllerGetPropertiesPhotosCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LandlordPhotoModelResults}
     */
    propertyControllerGetPropertiesPhotos(shortName, token, propertyID, offset, count, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling propertyControllerGetPropertiesPhotos");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling propertyControllerGetPropertiesPhotos");
      }
      // verify the required parameter 'propertyID' is set
      if (propertyID === undefined || propertyID === null) {
        throw new Error("Missing the required parameter 'propertyID' when calling propertyControllerGetPropertiesPhotos");
      }
      // verify the required parameter 'offset' is set
      if (offset === undefined || offset === null) {
        throw new Error("Missing the required parameter 'offset' when calling propertyControllerGetPropertiesPhotos");
      }
      // verify the required parameter 'count' is set
      if (count === undefined || count === null) {
        throw new Error("Missing the required parameter 'count' when calling propertyControllerGetPropertiesPhotos");
      }

      let pathParams = {
        'shortName': shortName,
        'propertyID': propertyID
      };
      let queryParams = {
        'token': token,
        'offset': offset,
        'count': count
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = LandlordPhotoModelResults;
      return this.apiClient.callApi(
        '/v2/customer/{shortName}/property/{propertyID}/photos', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
