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
import AddCoupons200Response from '../model/AddCoupons200Response';
import AddCouponsRequest from '../model/AddCouponsRequest';
import CartSimulation200Response from '../model/CartSimulation200Response';
import CartSimulationRequest from '../model/CartSimulationRequest';
import IgnoreProfileDataRequest from '../model/IgnoreProfileDataRequest';
import Items200Response from '../model/Items200Response';
import ItemsRequest from '../model/ItemsRequest';
import ItemsUpdate200Response from '../model/ItemsUpdate200Response';
import ItemsUpdateRequest from '../model/ItemsUpdateRequest';
import PriceChangeRequest from '../model/PriceChangeRequest';

/**
* ShoppingCart service.
* @module api/ShoppingCartApi
* @version 1.0
*/
export default class ShoppingCartApi {

    /**
    * Constructs a new ShoppingCartApi. 
    * @alias module:api/ShoppingCartApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addCoupons operation.
     * @callback module:api/ShoppingCartApi~addCouponsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AddCoupons200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add coupons to the cart
     * Use this request to add coupons to a given shopping cart.
     * @param {String} orderFormId ID of the orderForm that will receive coupon information.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:model/AddCouponsRequest} addCouponsRequest 
     * @param {module:api/ShoppingCartApi~addCouponsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AddCoupons200Response}
     */
    addCoupons(orderFormId, contentType, accept, addCouponsRequest, callback) {
      let postBody = addCouponsRequest;
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling addCoupons");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling addCoupons");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling addCoupons");
      }
      // verify the required parameter 'addCouponsRequest' is set
      if (addCouponsRequest === undefined || addCouponsRequest === null) {
        throw new Error("Missing the required parameter 'addCouponsRequest' when calling addCoupons");
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
      let returnType = AddCoupons200Response;
      return this.apiClient.callApi(
        '/api/checkout/pub/orderForm/{orderFormId}/coupons', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cartSimulation operation.
     * @callback module:api/ShoppingCartApi~cartSimulationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CartSimulation200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Cart simulation
     * This endpoint is used to simulate a cart in VTEX Checkout.    It receives an **SKU ID**, the **quantity** of items in the cart and the ID of the **Seller**.    It sends back all information about the cart, such as the selling price of each item, rates and benefits data, payment and logistics info.    This is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data.    **Important**: The fields (`sku id`, `quantity`, `seller`, `country`, `postalCode` and `geoCoordinates`) are just examples of content that you can simulate in your cart. You can add more fields to the request as per your need. Access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) guide to check the available fields.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {Number} [rnbBehavior = 0)] This parameter defines which promotions apply to the simulation. Use `0` for simulations at cart stage, which means all promotions apply. In case of window simulation use `1`, which indicates promotions that apply nominal discounts over the total purchase value shouldn't be considered on the simulation.    Note that if this not sent, the parameter is `1`.
     * @param {Number} [sc] Trade Policy (Sales Channel) identification.
     * @param {module:model/CartSimulationRequest} [cartSimulationRequest] 
     * @param {module:api/ShoppingCartApi~cartSimulationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CartSimulation200Response}
     */
    cartSimulation(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['cartSimulationRequest'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling cartSimulation");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling cartSimulation");
      }

      let pathParams = {
      };
      let queryParams = {
        'RnbBehavior': opts['rnbBehavior'],
        'sc': opts['sc']
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
      let returnType = CartSimulation200Response;
      return this.apiClient.callApi(
        '/api/checkout/pub/orderForms/simulation', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createANewCart operation.
     * @callback module:api/ShoppingCartApi~createANewCartCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get current or create a new cart
     * You can use this request to get your current shopping cart information (`orderFormId`) or to create a new cart.    **Important**: To create a new empty shopping cart you need to send this request with the query param `forceNewCart=true`.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` obtained in response is the identification code of the newly created cart.    > This request has a time out of 45 seconds.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {Boolean} [forceNewCart = true)] Use this query parameter to create a new empty shopping cart.
     * @param {module:api/ShoppingCartApi~createANewCartCallback} callback The callback function, accepting three arguments: error, data, response
     */
    createANewCart(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling createANewCart");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling createANewCart");
      }

      let pathParams = {
      };
      let queryParams = {
        'forceNewCart': opts['forceNewCart']
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
        '/api/checkout/pub/orderForm', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCartInformationById operation.
     * @callback module:api/ShoppingCartApi~getCartInformationByIdCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get cart information by ID
     * Use this request to get all information associated to a given shopping  cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    > This request has a time out of 45 seconds.
     * @param {String} orderFormId ID of the orderForm corresponding to the cart whose information you want to retrieve.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {Boolean} [refreshOutdatedData = true)] It is possible to use the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/cart-update#itemsupdate) so as to allow outdated information in the `orderForm`, which may improve performance in some cases. To guarantee that all cart information is updated, send this request with this parameter as `true`. We recommend doing this in the final stages of the shopping experience, starting from the checkout page.
     * @param {module:api/ShoppingCartApi~getCartInformationByIdCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getCartInformationById(orderFormId, contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling getCartInformationById");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling getCartInformationById");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling getCartInformationById");
      }

      let pathParams = {
        'orderFormId': orderFormId
      };
      let queryParams = {
        'refreshOutdatedData': opts['refreshOutdatedData']
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
        '/api/checkout/pub/orderForm/{orderFormId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCartInstallments operation.
     * @callback module:api/ShoppingCartApi~getCartInstallmentsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Cart installments
     * Retrieves possible amount of installments and respective values for a given cart with a given payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    This endpoint can be used to get the installment options for only one payment method at a time.    This endpoint should be called only after the selected `orderForm` already has a `paymentData`.
     * @param {String} orderFormId ID of the `orderForm` to be consulted for installments.
     * @param {Number} paymentSystem ID of the payment method to be consulted for installments.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:api/ShoppingCartApi~getCartInstallmentsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getCartInstallments(orderFormId, paymentSystem, contentType, accept, callback) {
      let postBody = null;
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling getCartInstallments");
      }
      // verify the required parameter 'paymentSystem' is set
      if (paymentSystem === undefined || paymentSystem === null) {
        throw new Error("Missing the required parameter 'paymentSystem' when calling getCartInstallments");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling getCartInstallments");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling getCartInstallments");
      }

      let pathParams = {
        'orderFormId': orderFormId
      };
      let queryParams = {
        'paymentSystem': paymentSystem
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
        '/api/checkout/pub/orderForm/{orderFormId}/installments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the ignoreProfileData operation.
     * @callback module:api/ShoppingCartApi~ignoreProfileDataCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Ignore profile data
     * When a shopper provides an email address at Checkout, the platform tries to retrieve existing profile information for that email and add it to the shopping cart information. Use this request if you want to change this behavior for a given cart, meaning profile information will not be included in the order automattically.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    Note that this request will only work if you have not sent the `clientProfileData` to the cart yet. Sending it to a cart that already has a `clientProfileData` should return a status `403 Forbidden` error, with an `Access denied` message.
     * @param {String} orderFormId ID of the orderForm corresponding to the cart whose items will have the price changed.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:model/IgnoreProfileDataRequest} ignoreProfileDataRequest 
     * @param {module:api/ShoppingCartApi~ignoreProfileDataCallback} callback The callback function, accepting three arguments: error, data, response
     */
    ignoreProfileData(orderFormId, contentType, accept, ignoreProfileDataRequest, callback) {
      let postBody = ignoreProfileDataRequest;
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling ignoreProfileData");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling ignoreProfileData");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling ignoreProfileData");
      }
      // verify the required parameter 'ignoreProfileDataRequest' is set
      if (ignoreProfileDataRequest === undefined || ignoreProfileDataRequest === null) {
        throw new Error("Missing the required parameter 'ignoreProfileDataRequest' when calling ignoreProfileData");
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
        '/api/checkout/pub/orderForm/{orderFormId}/profile', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the items operation.
     * @callback module:api/ShoppingCartApi~itemsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Items200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add cart items
     * Use this request to add a new item to the shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    > This request has a time out of 45 seconds.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} orderFormId ID of the orderForm corresponding to the cart in which the new item will be added.
     * @param {module:model/ItemsRequest} itemsRequest 
     * @param {Object} opts Optional parameters
     * @param {Array.<Object>} [allowedOutdatedData] In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is `”paymentData”`.
     * @param {module:api/ShoppingCartApi~itemsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Items200Response}
     */
    items(contentType, accept, orderFormId, itemsRequest, opts, callback) {
      opts = opts || {};
      let postBody = itemsRequest;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling items");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling items");
      }
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling items");
      }
      // verify the required parameter 'itemsRequest' is set
      if (itemsRequest === undefined || itemsRequest === null) {
        throw new Error("Missing the required parameter 'itemsRequest' when calling items");
      }

      let pathParams = {
        'orderFormId': orderFormId
      };
      let queryParams = {
        'allowedOutdatedData': this.apiClient.buildCollectionParam(opts['allowedOutdatedData'], 'multi')
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
      let returnType = Items200Response;
      return this.apiClient.callApi(
        '/api/checkout/pub/orderForm/{orderFormId}/items', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the itemsUpdate operation.
     * @callback module:api/ShoppingCartApi~itemsUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ItemsUpdate200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update cart items
     * You can use this request to:    1. Change the quantity of one or more items in a specific cart.  2. Remove an item from the cart (by sending the `quantity` value = `0` in the request body).    **Important**: To remove all items from the cart at the same time, use the [Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems) endpoint.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    > This request has a time out of 45 seconds.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} orderFormId ID of the `orderForm` corresponding to the cart whose items you want to update.
     * @param {module:model/ItemsUpdateRequest} itemsUpdateRequest 
     * @param {Object} opts Optional parameters
     * @param {Array.<Object>} [allowedOutdatedData] In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is `”paymentData”`.
     * @param {module:api/ShoppingCartApi~itemsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ItemsUpdate200Response}
     */
    itemsUpdate(contentType, accept, orderFormId, itemsUpdateRequest, opts, callback) {
      opts = opts || {};
      let postBody = itemsUpdateRequest;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling itemsUpdate");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling itemsUpdate");
      }
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling itemsUpdate");
      }
      // verify the required parameter 'itemsUpdateRequest' is set
      if (itemsUpdateRequest === undefined || itemsUpdateRequest === null) {
        throw new Error("Missing the required parameter 'itemsUpdateRequest' when calling itemsUpdate");
      }

      let pathParams = {
        'orderFormId': orderFormId
      };
      let queryParams = {
        'allowedOutdatedData': this.apiClient.buildCollectionParam(opts['allowedOutdatedData'], 'multi')
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
      let returnType = ItemsUpdate200Response;
      return this.apiClient.callApi(
        '/api/checkout/pub/orderForm/{orderFormId}/items/update', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the priceChange operation.
     * @callback module:api/ShoppingCartApi~priceChangeCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Change price
     * This request changes the price of an SKU in a cart. You can also perform type of bulk price change with the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#itemsupdate)    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    You need to inform which cart you are referring to, by sending its `orderFormId`; and what is the item whose price you want to change, by sending its `itemIndex`.    You also need to pass the new price value in the body.    Remember that, to use this endpoint, the feature of *manual price* must be active. To check if it's active, use the [Get orderForm configuration](https://developers.vtex.com/reference#getorderformconfiguration) endpoint. To make it active, use the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) endpoint, making the `allowManualPrice` field `true`.    > Whenever you use this request to change the price of an item, all items in that cart with the same SKU are affected by this change. This applies even to items that share the SKU but have been separated into different objects in the `items` array due to customizations or attachments, for example.
     * @param {String} orderFormId ID of the orderForm corresponding to the cart whose items will have the price changed.
     * @param {String} itemIndex The index of the item in the cart. Each cart item is identified by an index, starting in 0.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:model/PriceChangeRequest} priceChangeRequest 
     * @param {module:api/ShoppingCartApi~priceChangeCallback} callback The callback function, accepting three arguments: error, data, response
     */
    priceChange(orderFormId, itemIndex, contentType, accept, priceChangeRequest, callback) {
      let postBody = priceChangeRequest;
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling priceChange");
      }
      // verify the required parameter 'itemIndex' is set
      if (itemIndex === undefined || itemIndex === null) {
        throw new Error("Missing the required parameter 'itemIndex' when calling priceChange");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling priceChange");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling priceChange");
      }
      // verify the required parameter 'priceChangeRequest' is set
      if (priceChangeRequest === undefined || priceChangeRequest === null) {
        throw new Error("Missing the required parameter 'priceChangeRequest' when calling priceChange");
      }

      let pathParams = {
        'orderFormId': orderFormId,
        'itemIndex': itemIndex
      };
      let queryParams = {
      };
      let headerParams = {
        'Content-Type': contentType,
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = ['appToken', 'appKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/checkout/pub/orderForm/{orderFormId}/items/{itemIndex}/price', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeAllItems operation.
     * @callback module:api/ShoppingCartApi~removeAllItemsCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove all items
     * This request removes all items from a given cart, leaving it empty.    You must send an empty JSON in the body of the request.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.    **Important**: **Request Body** must always be sent with empty value \"{ }\" in this endpoint.
     * @param {String} orderFormId ID of the orderForm corresponding to the cart whose items you want to remove.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {Object.<String, Object>} [body] 
     * @param {module:api/ShoppingCartApi~removeAllItemsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    removeAllItems(orderFormId, contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['body'];
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling removeAllItems");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling removeAllItems");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling removeAllItems");
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
        '/api/checkout/pub/orderForm/{orderFormId}/items/removeAll', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeallpersonaldata operation.
     * @callback module:api/ShoppingCartApi~removeallpersonaldataCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove all personal data
     * This call removes all user information, making a cart anonymous while leaving the items.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information about it. Hence, the `orderFormId` is the identification code of a given cart.    This call works by creating a new orderForm, setting a new cookie, and returning a redirect 302 to the cart URL (`/checkout/#/orderform`).
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} orderFormId ID of the orderForm corresponding to the cart whose user's personal data you want to remove.
     * @param {module:api/ShoppingCartApi~removeallpersonaldataCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    removeallpersonaldata(contentType, accept, orderFormId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling removeallpersonaldata");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling removeallpersonaldata");
      }
      // verify the required parameter 'orderFormId' is set
      if (orderFormId === undefined || orderFormId === null) {
        throw new Error("Missing the required parameter 'orderFormId' when calling removeallpersonaldata");
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
      let contentTypes = [];
      let accepts = ['text/plain'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/checkout/changeToAnonymousUser/{orderFormId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
