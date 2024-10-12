/*
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.PlaceOrder200Response;
import org.openapitools.client.model.PlaceOrderFromExistingOrderFormRequest;
import org.openapitools.client.model.PlaceOrderRequest;
import org.openapitools.client.model.ProcessOrder500Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class OrderPlacementApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public OrderPlacementApi() {
        this(Configuration.getDefaultApiClient());
    }

    public OrderPlacementApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for placeOrder
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param sc Trade Policy (Sales Channel) identification. This query can be used to create an order for a specific sales channel. (optional)
     * @param placeOrderRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call placeOrderCall(String contentType, String accept, Integer sc, PlaceOrderRequest placeOrderRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = placeOrderRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orders";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (sc != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sc", sc));
        }

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call placeOrderValidateBeforeCall(String contentType, String accept, Integer sc, PlaceOrderRequest placeOrderRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling placeOrder(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling placeOrder(Async)");
        }

        return placeOrderCall(contentType, accept, sc, placeOrderRequest, _callback);

    }

    /**
     * Place order
     * Places order without having any prior cart information. This means all information on items, client, payment and shipping must be sent in the body.    &gt;⚠️ The authentication of this endpoint is required if you are creating an order with an item that has an attachment that creates a Subscription. For more information, access [Subscriptions API](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3).
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param sc Trade Policy (Sales Channel) identification. This query can be used to create an order for a specific sales channel. (optional)
     * @param placeOrderRequest  (optional)
     * @return PlaceOrder200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public PlaceOrder200Response placeOrder(String contentType, String accept, Integer sc, PlaceOrderRequest placeOrderRequest) throws ApiException {
        ApiResponse<PlaceOrder200Response> localVarResp = placeOrderWithHttpInfo(contentType, accept, sc, placeOrderRequest);
        return localVarResp.getData();
    }

    /**
     * Place order
     * Places order without having any prior cart information. This means all information on items, client, payment and shipping must be sent in the body.    &gt;⚠️ The authentication of this endpoint is required if you are creating an order with an item that has an attachment that creates a Subscription. For more information, access [Subscriptions API](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3).
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param sc Trade Policy (Sales Channel) identification. This query can be used to create an order for a specific sales channel. (optional)
     * @param placeOrderRequest  (optional)
     * @return ApiResponse&lt;PlaceOrder200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PlaceOrder200Response> placeOrderWithHttpInfo(String contentType, String accept, Integer sc, PlaceOrderRequest placeOrderRequest) throws ApiException {
        okhttp3.Call localVarCall = placeOrderValidateBeforeCall(contentType, accept, sc, placeOrderRequest, null);
        Type localVarReturnType = new TypeToken<PlaceOrder200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Place order (asynchronously)
     * Places order without having any prior cart information. This means all information on items, client, payment and shipping must be sent in the body.    &gt;⚠️ The authentication of this endpoint is required if you are creating an order with an item that has an attachment that creates a Subscription. For more information, access [Subscriptions API](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3).
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param sc Trade Policy (Sales Channel) identification. This query can be used to create an order for a specific sales channel. (optional)
     * @param placeOrderRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call placeOrderAsync(String contentType, String accept, Integer sc, PlaceOrderRequest placeOrderRequest, final ApiCallback<PlaceOrder200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = placeOrderValidateBeforeCall(contentType, accept, sc, placeOrderRequest, _callback);
        Type localVarReturnType = new TypeToken<PlaceOrder200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for placeOrderFromExistingOrderForm
     * @param orderFormId ID of the &#x60;orderForm&#x60; corresponding to the cart from which to place the order. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param placeOrderFromExistingOrderFormRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call placeOrderFromExistingOrderFormCall(String orderFormId, String contentType, String accept, PlaceOrderFromExistingOrderFormRequest placeOrderFromExistingOrderFormRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = placeOrderFromExistingOrderFormRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/transaction"
            .replace("{" + "orderFormId" + "}", localVarApiClient.escapeString(orderFormId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call placeOrderFromExistingOrderFormValidateBeforeCall(String orderFormId, String contentType, String accept, PlaceOrderFromExistingOrderFormRequest placeOrderFromExistingOrderFormRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling placeOrderFromExistingOrderForm(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling placeOrderFromExistingOrderForm(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling placeOrderFromExistingOrderForm(Async)");
        }

        return placeOrderFromExistingOrderFormCall(orderFormId, contentType, accept, placeOrderFromExistingOrderFormRequest, _callback);

    }

    /**
     * Place order from an existing cart
     * This endpoint places an order from an existing &#x60;orderForm&#x60; object, meaning an existing cart.    After the creation of an order with this request, you have five minutes to send payment information and then request payment processing.
     * @param orderFormId ID of the &#x60;orderForm&#x60; corresponding to the cart from which to place the order. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param placeOrderFromExistingOrderFormRequest  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public Object placeOrderFromExistingOrderForm(String orderFormId, String contentType, String accept, PlaceOrderFromExistingOrderFormRequest placeOrderFromExistingOrderFormRequest) throws ApiException {
        ApiResponse<Object> localVarResp = placeOrderFromExistingOrderFormWithHttpInfo(orderFormId, contentType, accept, placeOrderFromExistingOrderFormRequest);
        return localVarResp.getData();
    }

    /**
     * Place order from an existing cart
     * This endpoint places an order from an existing &#x60;orderForm&#x60; object, meaning an existing cart.    After the creation of an order with this request, you have five minutes to send payment information and then request payment processing.
     * @param orderFormId ID of the &#x60;orderForm&#x60; corresponding to the cart from which to place the order. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param placeOrderFromExistingOrderFormRequest  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> placeOrderFromExistingOrderFormWithHttpInfo(String orderFormId, String contentType, String accept, PlaceOrderFromExistingOrderFormRequest placeOrderFromExistingOrderFormRequest) throws ApiException {
        okhttp3.Call localVarCall = placeOrderFromExistingOrderFormValidateBeforeCall(orderFormId, contentType, accept, placeOrderFromExistingOrderFormRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Place order from an existing cart (asynchronously)
     * This endpoint places an order from an existing &#x60;orderForm&#x60; object, meaning an existing cart.    After the creation of an order with this request, you have five minutes to send payment information and then request payment processing.
     * @param orderFormId ID of the &#x60;orderForm&#x60; corresponding to the cart from which to place the order. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param placeOrderFromExistingOrderFormRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call placeOrderFromExistingOrderFormAsync(String orderFormId, String contentType, String accept, PlaceOrderFromExistingOrderFormRequest placeOrderFromExistingOrderFormRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = placeOrderFromExistingOrderFormValidateBeforeCall(orderFormId, contentType, accept, placeOrderFromExistingOrderFormRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for processOrder
     * @param orderGroup Order group. It is the part of the &#x60;orderId&#x60; that comes before the &#x60;-&#x60;. For example, the &#x60;orderGroup&#x60; of the order &#x60;123456789-01&#x60; is &#x60;123456789&#x60;. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param cookie VTEX Chekout cookie associated with a specific order. Use the &#x60;Vtex_CHKO_Auth&#x60; and the &#x60;CheckoutDataAccess&#x60; cookies returned by the [Place order](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorder) or [Place order from existing cart](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorderfromexistingorderform) API requests, like a browser would. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call processOrderCall(String orderGroup, String contentType, String accept, String cookie, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/gatewayCallback/{orderGroup}"
            .replace("{" + "orderGroup" + "}", localVarApiClient.escapeString(orderGroup.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        if (cookie != null) {
            localVarHeaderParams.put("Cookie", localVarApiClient.parameterToString(cookie));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call processOrderValidateBeforeCall(String orderGroup, String contentType, String accept, String cookie, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orderGroup' is set
        if (orderGroup == null) {
            throw new ApiException("Missing the required parameter 'orderGroup' when calling processOrder(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling processOrder(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling processOrder(Async)");
        }

        // verify the required parameter 'cookie' is set
        if (cookie == null) {
            throw new ApiException("Missing the required parameter 'cookie' when calling processOrder(Async)");
        }

        return processOrderCall(orderGroup, contentType, accept, cookie, _callback);

    }

    /**
     * Process order
     * Order processing callback request, which is made after an order&#39;s payment is approved.    &gt; This request has to be made until five minutes after the [Place order](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders) or [Place order from existing cart](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction) request has been made, or else, the order will not be processed.
     * @param orderGroup Order group. It is the part of the &#x60;orderId&#x60; that comes before the &#x60;-&#x60;. For example, the &#x60;orderGroup&#x60; of the order &#x60;123456789-01&#x60; is &#x60;123456789&#x60;. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param cookie VTEX Chekout cookie associated with a specific order. Use the &#x60;Vtex_CHKO_Auth&#x60; and the &#x60;CheckoutDataAccess&#x60; cookies returned by the [Place order](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorder) or [Place order from existing cart](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorderfromexistingorderform) API requests, like a browser would. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public void processOrder(String orderGroup, String contentType, String accept, String cookie) throws ApiException {
        processOrderWithHttpInfo(orderGroup, contentType, accept, cookie);
    }

    /**
     * Process order
     * Order processing callback request, which is made after an order&#39;s payment is approved.    &gt; This request has to be made until five minutes after the [Place order](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders) or [Place order from existing cart](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction) request has been made, or else, the order will not be processed.
     * @param orderGroup Order group. It is the part of the &#x60;orderId&#x60; that comes before the &#x60;-&#x60;. For example, the &#x60;orderGroup&#x60; of the order &#x60;123456789-01&#x60; is &#x60;123456789&#x60;. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param cookie VTEX Chekout cookie associated with a specific order. Use the &#x60;Vtex_CHKO_Auth&#x60; and the &#x60;CheckoutDataAccess&#x60; cookies returned by the [Place order](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorder) or [Place order from existing cart](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorderfromexistingorderform) API requests, like a browser would. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> processOrderWithHttpInfo(String orderGroup, String contentType, String accept, String cookie) throws ApiException {
        okhttp3.Call localVarCall = processOrderValidateBeforeCall(orderGroup, contentType, accept, cookie, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Process order (asynchronously)
     * Order processing callback request, which is made after an order&#39;s payment is approved.    &gt; This request has to be made until five minutes after the [Place order](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders) or [Place order from existing cart](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction) request has been made, or else, the order will not be processed.
     * @param orderGroup Order group. It is the part of the &#x60;orderId&#x60; that comes before the &#x60;-&#x60;. For example, the &#x60;orderGroup&#x60; of the order &#x60;123456789-01&#x60; is &#x60;123456789&#x60;. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param cookie VTEX Chekout cookie associated with a specific order. Use the &#x60;Vtex_CHKO_Auth&#x60; and the &#x60;CheckoutDataAccess&#x60; cookies returned by the [Place order](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorder) or [Place order from existing cart](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorderfromexistingorderform) API requests, like a browser would. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call processOrderAsync(String orderGroup, String contentType, String accept, String cookie, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = processOrderValidateBeforeCall(orderGroup, contentType, accept, cookie, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
