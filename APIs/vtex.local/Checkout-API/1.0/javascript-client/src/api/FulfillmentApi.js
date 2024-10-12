/**
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";

/**
* Fulfillment service.
* @module api/FulfillmentApi
* @version 1.0
*/
export default class FulfillmentApi {

    /**
    * Constructs a new FulfillmentApi. 
    * @alias module:api/FulfillmentApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getAddressByPostalCode operation.
     * @callback module:api/FulfillmentApi~getAddressByPostalCodeCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get address by postal code
     * Retrieves address information for a given postal code and country.    This request can be used to implement auto complete functionality when a customer needs to fill in an address.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} countryCode Three letter country code refering to the `postalCode` field.
     * @param {String} postalCode Postal code.
     * @param {module:api/FulfillmentApi~getAddressByPostalCodeCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAddressByPostalCode(contentType, accept, countryCode, postalCode, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling getAddressByPostalCode");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling getAddressByPostalCode");
      }
      // verify the required parameter 'countryCode' is set
      if (countryCode === undefined || countryCode === null) {
        throw new Error("Missing the required parameter 'countryCode' when calling getAddressByPostalCode");
      }
      // verify the required parameter 'postalCode' is set
      if (postalCode === undefined || postalCode === null) {
        throw new Error("Missing the required parameter 'postalCode' when calling getAddressByPostalCode");
      }

      let pathParams = {
        'countryCode': countryCode,
        'postalCode': postalCode
      };
      let queryParams = {
      };
      let headerParams = {
        'Content-Type': contentType,
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/checkout/pub/postal-code/{countryCode}/{postalCode}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listPickupPpointsByLocation operation.
     * @callback module:api/FulfillmentApi~listPickupPpointsByLocationCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List pickup points by location
     * Retrieves information on pickup points close to a given location determined by geocoordinates or postal code.    The pickup points returned are not necessarily all active ones. Make sure to validate the information consumed by integrations.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {Array.<Number>} [geoCoordinates] Geocoordinates (first longitude, then latitude) around which to search for pickup points. If you use this type of search, do not pass postal and country codes.
     * @param {String} [postalCode = '1234000')] Postal code around which to search for pickup points. If you use this type of search, make sure to pass a `countryCode` and do not pass `geoCoordinates`.
     * @param {String} [countryCode = 'BRA')] Three letter country code refering to the `postalCode` field. Pass the country code only if you are searching pickup points by postal code.
     * @param {module:api/FulfillmentApi~listPickupPpointsByLocationCallback} callback The callback function, accepting three arguments: error, data, response
     */
    listPickupPpointsByLocation(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling listPickupPpointsByLocation");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling listPickupPpointsByLocation");
      }

      let pathParams = {
      };
      let queryParams = {
        'geoCoordinates': this.apiClient.buildCollectionParam(opts['geoCoordinates'], 'multi'),
        'postalCode': opts['postalCode'],
        'countryCode': opts['countryCode']
      };
      let headerParams = {
        'Content-Type': contentType,
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/checkout/pub/pickup-points', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
