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
import SetsinglecustomfieldvalueRequest from '../model/SetsinglecustomfieldvalueRequest';

/**
* CustomData service.
* @module api/CustomDataApi
* @version 1.0
*/
export default class CustomDataApi {

    /**
    * Constructs a new CustomDataApi. 
    * @alias module:api/CustomDataApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the removesinglecustomfieldvalue operation.
     * @callback module:api/CustomDataApi~removesinglecustomfieldvalueCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove single custom field value
     * Your account may create `apps`, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can be removed by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (`appId`).    You also need to iform the specific field created in this app (identified by the `appFieldName` parameter, also passed through the URL) whose value you want to remove.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} orderFormId The ID of the orderForm from which you want to remove the custom field value.
     * @param {String} appId ID of the app created through the Update orderForm Configuration endpoint.
     * @param {String} appFieldName Name of the app's field created through the Update orderForm Configuration endpoint and which will be deleted.
     * @param {module:api/CustomDataApi~removesinglecustomfieldvalueCallback} callback The callback function, accepting three arguments: error, data, response
     */
    removesinglecustomfieldvalue(contentType, accept, orderFormId, appId, appFieldName, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling removesinglecustomfieldvalue");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling removesinglecustomfieldvalue");
      }
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling removesinglecustomfieldvalue");
      }
      // verify the required parameter 'appId' is set
      if (appId === undefined || appId === null) {
        throw new Error("Missing the required parameter 'appId' when calling removesinglecustomfieldvalue");
      }
      // verify the required parameter 'appFieldName' is set
      if (appFieldName === undefined || appFieldName === null) {
        throw new Error("Missing the required parameter 'appFieldName' when calling removesinglecustomfieldvalue");
      }

      let pathParams = {
        'orderFormId': orderFormId,
        'appId': appId,
        'appFieldName': appFieldName
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
        '/api/checkout/pub/orderForm/{orderFormId}/customData/{appId}/{appFieldName}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the setMultipleCustomFieldValues operation.
     * @callback module:api/CustomDataApi~setMultipleCustomFieldValuesCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set multiple custom field values
     * Your account may create `apps`, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference/configuration#updateorderformconfiguration) request. The values of these custom fields can then be updated by this request.    To do that, you need to inform the ID of the app you created with the configuration API (`appId`).    In the body of the request, for each field created in this app (`appFieldName`) you will inform a value (`appFieldValue`).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.
     * @param {String} orderFormId ID of the orderForm that will receive the new custom field values.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} appId ID of the app created with the configuration API.
     * @param {Object.<String, {String: Object}>} requestBody 
     * @param {module:api/CustomDataApi~setMultipleCustomFieldValuesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    setMultipleCustomFieldValues(orderFormId, contentType, accept, appId, requestBody, callback) {
      let postBody = requestBody;
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling setMultipleCustomFieldValues");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling setMultipleCustomFieldValues");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling setMultipleCustomFieldValues");
      }
      // verify the required parameter 'appId' is set
      if (appId === undefined || appId === null) {
        throw new Error("Missing the required parameter 'appId' when calling setMultipleCustomFieldValues");
      }
      // verify the required parameter 'requestBody' is set
      if (requestBody === undefined || requestBody === null) {
        throw new Error("Missing the required parameter 'requestBody' when calling setMultipleCustomFieldValues");
      }

      let pathParams = {
        'orderFormId': orderFormId,
        'appId': appId
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/api/checkout/pub/orderForm/{orderFormId}/customData/{appId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the setSingleCustomFieldValue operation.
     * @callback module:api/CustomDataApi~setSingleCustomFieldValueCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set single custom field value
     * Your account may create `apps`, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can then be updated by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (`appId`).    In the body of the request, you will inform the new value (`appFieldValue`, passed through the body) of the specific field created in this app (identified by the `appFieldName` parameter, passed through the URL).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.
     * @param {String} orderFormId The ID of the orderForm whose custom field's value you want to change.
     * @param {String} appId ID of the app created through the Update orderForm Configuration endpoint.
     * @param {String} appFieldName Name of the app's field created through the Update orderForm Configuration endpoint.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:model/SetsinglecustomfieldvalueRequest} setsinglecustomfieldvalueRequest 
     * @param {module:api/CustomDataApi~setSingleCustomFieldValueCallback} callback The callback function, accepting three arguments: error, data, response
     */
    setSingleCustomFieldValue(orderFormId, appId, appFieldName, contentType, accept, setsinglecustomfieldvalueRequest, callback) {
      let postBody = setsinglecustomfieldvalueRequest;
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling setSingleCustomFieldValue");
      }
      // verify the required parameter 'appId' is set
      if (appId === undefined || appId === null) {
        throw new Error("Missing the required parameter 'appId' when calling setSingleCustomFieldValue");
      }
      // verify the required parameter 'appFieldName' is set
      if (appFieldName === undefined || appFieldName === null) {
        throw new Error("Missing the required parameter 'appFieldName' when calling setSingleCustomFieldValue");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling setSingleCustomFieldValue");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling setSingleCustomFieldValue");
      }
      // verify the required parameter 'setsinglecustomfieldvalueRequest' is set
      if (setsinglecustomfieldvalueRequest === undefined || setsinglecustomfieldvalueRequest === null) {
        throw new Error("Missing the required parameter 'setsinglecustomfieldvalueRequest' when calling setSingleCustomFieldValue");
      }

      let pathParams = {
        'orderFormId': orderFormId,
        'appId': appId,
        'appFieldName': appFieldName
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/checkout/pub/orderForm/{orderFormId}/customData/{appId}/{appFieldName}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
