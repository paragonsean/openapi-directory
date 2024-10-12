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
import AddClientPreferencesRequest from '../model/AddClientPreferencesRequest';
import AddClientProfileRequest from '../model/AddClientProfileRequest';
import AddMarketingDataRequest from '../model/AddMarketingDataRequest';
import AddMerchantContextData200Response from '../model/AddMerchantContextData200Response';
import AddMerchantContextDataRequest from '../model/AddMerchantContextDataRequest';
import AddPaymentDataRequest from '../model/AddPaymentDataRequest';
import AddShippingAddressRequest from '../model/AddShippingAddressRequest';
import GetClientProfileByEmail200Response from '../model/GetClientProfileByEmail200Response';

/**
* CartAttachments service.
* @module api/CartAttachmentsApi
* @version 1.0
*/
export default class CartAttachmentsApi {

    /**
    * Constructs a new CartAttachmentsApi. 
    * @alias module:api/CartAttachmentsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addClientPreferences operation.
     * @callback module:api/CartAttachmentsApi~addClientPreferencesCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add client preferences
     * Use this request to include client preferences information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    > This request has a time out of 12 seconds.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} orderFormId ID of the orderForm that will receive client profile information.
     * @param {module:model/AddClientPreferencesRequest} addClientPreferencesRequest 
     * @param {module:api/CartAttachmentsApi~addClientPreferencesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    addClientPreferences(contentType, accept, orderFormId, addClientPreferencesRequest, callback) {
      let postBody = addClientPreferencesRequest;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling addClientPreferences");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling addClientPreferences");
      }
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling addClientPreferences");
      }
      // verify the required parameter 'addClientPreferencesRequest' is set
      if (addClientPreferencesRequest === undefined || addClientPreferencesRequest === null) {
        throw new Error("Missing the required parameter 'addClientPreferencesRequest' when calling addClientPreferences");
      }

      let pathParams = {
        'orderFormId': orderFormId
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
        '/api/checkout/pub/orderForm/{orderFormId}/attachments/clientPreferencesData', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addClientProfile operation.
     * @callback module:api/CartAttachmentsApi~addClientProfileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add client profile
     * Use this request to include client profile information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    > This request has a time out of 12 seconds.    >⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer's data masked. You can only access the customer data with an authenticated request.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} orderFormId ID of the orderForm that will receive client profile information.
     * @param {module:model/AddClientProfileRequest} addClientProfileRequest 
     * @param {module:api/CartAttachmentsApi~addClientProfileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addClientProfile(contentType, accept, orderFormId, addClientProfileRequest, callback) {
      let postBody = addClientProfileRequest;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling addClientProfile");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling addClientProfile");
      }
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling addClientProfile");
      }
      // verify the required parameter 'addClientProfileRequest' is set
      if (addClientProfileRequest === undefined || addClientProfileRequest === null) {
        throw new Error("Missing the required parameter 'addClientProfileRequest' when calling addClientProfile");
      }

      let pathParams = {
        'orderFormId': orderFormId
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
        '/api/checkout/pub/orderForm/{orderFormId}/attachments/clientProfileData', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addMarketingData operation.
     * @callback module:api/CartAttachmentsApi~addMarketingDataCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add marketing data
     * Use this request to include marketing information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    > This request has a time out of 12 seconds.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} orderFormId ID of the orderForm that will receive client profile information.
     * @param {module:model/AddMarketingDataRequest} addMarketingDataRequest 
     * @param {module:api/CartAttachmentsApi~addMarketingDataCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addMarketingData(contentType, accept, orderFormId, addMarketingDataRequest, callback) {
      let postBody = addMarketingDataRequest;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling addMarketingData");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling addMarketingData");
      }
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling addMarketingData");
      }
      // verify the required parameter 'addMarketingDataRequest' is set
      if (addMarketingDataRequest === undefined || addMarketingDataRequest === null) {
        throw new Error("Missing the required parameter 'addMarketingDataRequest' when calling addMarketingData");
      }

      let pathParams = {
        'orderFormId': orderFormId
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
        '/api/checkout/pub/orderForm/{orderFormId}/attachments/marketingData', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addMerchantContextData operation.
     * @callback module:api/CartAttachmentsApi~addMerchantContextDataCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AddMerchantContextData200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add merchant context data
     * This endpoint is used for the merchant to add to the cart any relevant information that is related to the context of a specific order.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    > This request has a time out of 12 seconds.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} orderFormId ID of the orderForm that will receive the relevant information added by the merchant.
     * @param {module:model/AddMerchantContextDataRequest} addMerchantContextDataRequest 
     * @param {module:api/CartAttachmentsApi~addMerchantContextDataCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AddMerchantContextData200Response}
     */
    addMerchantContextData(contentType, accept, orderFormId, addMerchantContextDataRequest, callback) {
      let postBody = addMerchantContextDataRequest;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling addMerchantContextData");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling addMerchantContextData");
      }
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling addMerchantContextData");
      }
      // verify the required parameter 'addMerchantContextDataRequest' is set
      if (addMerchantContextDataRequest === undefined || addMerchantContextDataRequest === null) {
        throw new Error("Missing the required parameter 'addMerchantContextDataRequest' when calling addMerchantContextData");
      }

      let pathParams = {
        'orderFormId': orderFormId
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
      let returnType = AddMerchantContextData200Response;
      return this.apiClient.callApi(
        '/api/checkout/pub/orderForm/{orderFormId}/attachments/merchantContextData', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addPaymentData operation.
     * @callback module:api/CartAttachmentsApi~addPaymentDataCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add payment data
     * Use this request to include payment information to a given shopping cart. The payment information attachment in the shopping cart does not determine the final order payment method in itself. However, it allows tha platform to update any relevant information that may be impacted by the payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    > This request has a time out of 12 seconds.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} orderFormId ID of the orderForm that will receive client profile information.
     * @param {module:model/AddPaymentDataRequest} addPaymentDataRequest 
     * @param {module:api/CartAttachmentsApi~addPaymentDataCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addPaymentData(contentType, accept, orderFormId, addPaymentDataRequest, callback) {
      let postBody = addPaymentDataRequest;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling addPaymentData");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling addPaymentData");
      }
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling addPaymentData");
      }
      // verify the required parameter 'addPaymentDataRequest' is set
      if (addPaymentDataRequest === undefined || addPaymentDataRequest === null) {
        throw new Error("Missing the required parameter 'addPaymentDataRequest' when calling addPaymentData");
      }

      let pathParams = {
        'orderFormId': orderFormId
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
        '/api/checkout/pub/orderForm/{orderFormId}/attachments/paymentData', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addShippingAddress operation.
     * @callback module:api/CartAttachmentsApi~addShippingAddressCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add shipping address and select delivery option
     * Use this request to include shipping information and/or selected delivery option to a given shopping cart.    To add shipping addresses send the `selectedAddresses` array. For delivery option use the `logisticsInfo` array.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    > This request has a time out of 12 seconds.    >⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer's data masked. You can only access the customer data with an authenticated request.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} orderFormId ID of the orderForm that will receive client profile information.
     * @param {module:model/AddShippingAddressRequest} addShippingAddressRequest 
     * @param {module:api/CartAttachmentsApi~addShippingAddressCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addShippingAddress(contentType, accept, orderFormId, addShippingAddressRequest, callback) {
      let postBody = addShippingAddressRequest;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling addShippingAddress");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling addShippingAddress");
      }
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling addShippingAddress");
      }
      // verify the required parameter 'addShippingAddressRequest' is set
      if (addShippingAddressRequest === undefined || addShippingAddressRequest === null) {
        throw new Error("Missing the required parameter 'addShippingAddressRequest' when calling addShippingAddress");
      }

      let pathParams = {
        'orderFormId': orderFormId
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
        '/api/checkout/pub/orderForm/{orderFormId}/attachments/shippingData', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getClientProfileByEmail operation.
     * @callback module:api/CartAttachmentsApi~getClientProfileByEmailCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetClientProfileByEmail200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get client profile by email
     * Retrieve a client's profile information by providing an email address.    If the response body fields are empty, the following situations may have occurred:    1. There is no client registered with the email address provided in your store, or;  2. Client profile is invalid or incomplete. For more information, see [SmartCheckout - Customer information automatic fill-in](https://help.vtex.com/en/tutorial/smartcheckout-customer-information-automatic-fill-in--2Nuu3xAFzdhIzJIldAdtan).    >⚠️ The authentication of this endpoint can change depending on the customer context. If you are consulting information from a customer with a complete profile on the store, the response will return the customer's data masked. You can only access the customer data with an authenticated request.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} email Client's email address to be searched.
     * @param {module:api/CartAttachmentsApi~getClientProfileByEmailCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetClientProfileByEmail200Response}
     */
    getClientProfileByEmail(contentType, accept, email, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling getClientProfileByEmail");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling getClientProfileByEmail");
      }
      // verify the required parameter 'email' is set
      if (email === undefined || email === null) {
        throw new Error("Missing the required parameter 'email' when calling getClientProfileByEmail");
      }

      let pathParams = {
      };
      let queryParams = {
        'email': email
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
      let returnType = GetClientProfileByEmail200Response;
      return this.apiClient.callApi(
        '/api/checkout/pub/profiles', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
