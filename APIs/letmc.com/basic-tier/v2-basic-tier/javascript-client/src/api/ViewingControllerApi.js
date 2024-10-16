/**
 * LetMC Api V2, Basic (Tier 2)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-basic-tier
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ViewingBookingModel from '../model/ViewingBookingModel';

/**
* ViewingController service.
* @module api/ViewingControllerApi
* @version v2-basic-tier
*/
export default class ViewingControllerApi {

    /**
    * Constructs a new ViewingControllerApi. 
    * @alias module:api/ViewingControllerApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the viewingControllerGetBookings operation.
     * @callback module:api/ViewingControllerApi~viewingControllerGetBookingsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ViewingBookingModel>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets a list of available viewing slots for one or more properties
     * @param {String} shortName The unique client short-name
     * @param {Date} preferredDate The preferred date for a viewing
     * @param {Array.<String>} propertyIDsToView An array of unique IDs of properties to view
     * @param {module:api/ViewingControllerApi~viewingControllerGetBookingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ViewingBookingModel>}
     */
    viewingControllerGetBookings(shortName, preferredDate, propertyIDsToView, callback) {
      let postBody = null;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling viewingControllerGetBookings");
      }
      // verify the required parameter 'preferredDate' is set
      if (preferredDate === undefined || preferredDate === null) {
        throw new Error("Missing the required parameter 'preferredDate' when calling viewingControllerGetBookings");
      }
      // verify the required parameter 'propertyIDsToView' is set
      if (propertyIDsToView === undefined || propertyIDsToView === null) {
        throw new Error("Missing the required parameter 'propertyIDsToView' when calling viewingControllerGetBookings");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'preferredDate': preferredDate,
        'propertyIDsToView': this.apiClient.buildCollectionParam(propertyIDsToView, 'multi')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = [ViewingBookingModel];
      return this.apiClient.callApi(
        '/v2/tier2/{shortName}/viewing/bookings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the viewingControllerMakeBooking operation.
     * @callback module:api/ViewingControllerApi~viewingControllerMakeBookingCallback
     * @param {String} error Error message, if any.
     * @param {Boolean} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Book an appointment for a viewing slot returned from the GET verb
     * @param {String} shortName The unique client short-name
     * @param {String} forename The forename of the prospect
     * @param {String} surname The surname of the prospect
     * @param {String} mobilePhone The mobile phone number of the prospect
     * @param {String} emailAddress The email address of the prospect
     * @param {Array.<String>} propertyIDsToView An array of unique IDs of properties to view
     * @param {module:model/ViewingBookingModel} selectedViewingSlot The prospect's selected viewing slot
     * @param {Object} opts Optional parameters
     * @param {Boolean} [wantRoomInSharedProperty] Whether the prospect wants a shared property
     * @param {Number} [alertMinRent] The minimum rent amount the prospect is looking for
     * @param {Number} [alertMaxRent] The maximum rent amount the prospect is looking for
     * @param {Number} [alertNumberOfBeds] The minimum number of beds the prospect is looking for
     * @param {String} [alertAreaID] The unique ID of the area the prospect is looking for
     * @param {module:model/String} [alertTenantType] The tenanct type the prospect is looking for
     * @param {Boolean} [subscribeToEmailAlerts] Whether to subscribe the prospect to email alerts
     * @param {Boolean} [subscribeToSMSAlerts] Whether to subscribe the prospect to SMS alerts
     * @param {module:api/ViewingControllerApi~viewingControllerMakeBookingCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Boolean}
     */
    viewingControllerMakeBooking(shortName, forename, surname, mobilePhone, emailAddress, propertyIDsToView, selectedViewingSlot, opts, callback) {
      opts = opts || {};
      let postBody = selectedViewingSlot;
      // verify the required parameter 'shortName' is set
      if (shortName === undefined || shortName === null) {
        throw new Error("Missing the required parameter 'shortName' when calling viewingControllerMakeBooking");
      }
      // verify the required parameter 'forename' is set
      if (forename === undefined || forename === null) {
        throw new Error("Missing the required parameter 'forename' when calling viewingControllerMakeBooking");
      }
      // verify the required parameter 'surname' is set
      if (surname === undefined || surname === null) {
        throw new Error("Missing the required parameter 'surname' when calling viewingControllerMakeBooking");
      }
      // verify the required parameter 'mobilePhone' is set
      if (mobilePhone === undefined || mobilePhone === null) {
        throw new Error("Missing the required parameter 'mobilePhone' when calling viewingControllerMakeBooking");
      }
      // verify the required parameter 'emailAddress' is set
      if (emailAddress === undefined || emailAddress === null) {
        throw new Error("Missing the required parameter 'emailAddress' when calling viewingControllerMakeBooking");
      }
      // verify the required parameter 'propertyIDsToView' is set
      if (propertyIDsToView === undefined || propertyIDsToView === null) {
        throw new Error("Missing the required parameter 'propertyIDsToView' when calling viewingControllerMakeBooking");
      }
      // verify the required parameter 'selectedViewingSlot' is set
      if (selectedViewingSlot === undefined || selectedViewingSlot === null) {
        throw new Error("Missing the required parameter 'selectedViewingSlot' when calling viewingControllerMakeBooking");
      }

      let pathParams = {
        'shortName': shortName
      };
      let queryParams = {
        'forename': forename,
        'surname': surname,
        'mobilePhone': mobilePhone,
        'emailAddress': emailAddress,
        'propertyIDsToView': this.apiClient.buildCollectionParam(propertyIDsToView, 'multi'),
        'wantRoomInSharedProperty': opts['wantRoomInSharedProperty'],
        'alertMinRent': opts['alertMinRent'],
        'alertMaxRent': opts['alertMaxRent'],
        'alertNumberOfBeds': opts['alertNumberOfBeds'],
        'alertAreaID': opts['alertAreaID'],
        'alertTenantType': opts['alertTenantType'],
        'subscribeToEmailAlerts': opts['subscribeToEmailAlerts'],
        'subscribeToSMSAlerts': opts['subscribeToSMSAlerts']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = 'Boolean';
      return this.apiClient.callApi(
        '/v2/tier2/{shortName}/viewing/bookings', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
