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


import org.openapitools.client.model.AddCoupons200Response;
import org.openapitools.client.model.AddCouponsRequest;
import org.openapitools.client.model.CartSimulation200Response;
import org.openapitools.client.model.CartSimulationRequest;
import org.openapitools.client.model.IgnoreProfileDataRequest;
import org.openapitools.client.model.Items200Response;
import org.openapitools.client.model.ItemsRequest;
import org.openapitools.client.model.ItemsUpdate200Response;
import org.openapitools.client.model.ItemsUpdateRequest;
import org.openapitools.client.model.PriceChangeRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ShoppingCartApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ShoppingCartApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ShoppingCartApi(ApiClient apiClient) {
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
     * Build call for addCoupons
     * @param orderFormId ID of the orderForm that will receive coupon information. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param addCouponsRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addCouponsCall(String orderFormId, String contentType, String accept, AddCouponsRequest addCouponsRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addCouponsRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/coupons"
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
    private okhttp3.Call addCouponsValidateBeforeCall(String orderFormId, String contentType, String accept, AddCouponsRequest addCouponsRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling addCoupons(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling addCoupons(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling addCoupons(Async)");
        }

        // verify the required parameter 'addCouponsRequest' is set
        if (addCouponsRequest == null) {
            throw new ApiException("Missing the required parameter 'addCouponsRequest' when calling addCoupons(Async)");
        }

        return addCouponsCall(orderFormId, contentType, accept, addCouponsRequest, _callback);

    }

    /**
     * Add coupons to the cart
     * Use this request to add coupons to a given shopping cart.
     * @param orderFormId ID of the orderForm that will receive coupon information. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param addCouponsRequest  (required)
     * @return AddCoupons200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public AddCoupons200Response addCoupons(String orderFormId, String contentType, String accept, AddCouponsRequest addCouponsRequest) throws ApiException {
        ApiResponse<AddCoupons200Response> localVarResp = addCouponsWithHttpInfo(orderFormId, contentType, accept, addCouponsRequest);
        return localVarResp.getData();
    }

    /**
     * Add coupons to the cart
     * Use this request to add coupons to a given shopping cart.
     * @param orderFormId ID of the orderForm that will receive coupon information. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param addCouponsRequest  (required)
     * @return ApiResponse&lt;AddCoupons200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AddCoupons200Response> addCouponsWithHttpInfo(String orderFormId, String contentType, String accept, AddCouponsRequest addCouponsRequest) throws ApiException {
        okhttp3.Call localVarCall = addCouponsValidateBeforeCall(orderFormId, contentType, accept, addCouponsRequest, null);
        Type localVarReturnType = new TypeToken<AddCoupons200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add coupons to the cart (asynchronously)
     * Use this request to add coupons to a given shopping cart.
     * @param orderFormId ID of the orderForm that will receive coupon information. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param addCouponsRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addCouponsAsync(String orderFormId, String contentType, String accept, AddCouponsRequest addCouponsRequest, final ApiCallback<AddCoupons200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = addCouponsValidateBeforeCall(orderFormId, contentType, accept, addCouponsRequest, _callback);
        Type localVarReturnType = new TypeToken<AddCoupons200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for cartSimulation
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param rnbBehavior This parameter defines which promotions apply to the simulation. Use &#x60;0&#x60; for simulations at cart stage, which means all promotions apply. In case of window simulation use &#x60;1&#x60;, which indicates promotions that apply nominal discounts over the total purchase value shouldn&#39;t be considered on the simulation.    Note that if this not sent, the parameter is &#x60;1&#x60;. (optional, default to 0)
     * @param sc Trade Policy (Sales Channel) identification. (optional)
     * @param cartSimulationRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cartSimulationCall(String contentType, String accept, Integer rnbBehavior, Integer sc, CartSimulationRequest cartSimulationRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = cartSimulationRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForms/simulation";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (rnbBehavior != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("RnbBehavior", rnbBehavior));
        }

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call cartSimulationValidateBeforeCall(String contentType, String accept, Integer rnbBehavior, Integer sc, CartSimulationRequest cartSimulationRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling cartSimulation(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling cartSimulation(Async)");
        }

        return cartSimulationCall(contentType, accept, rnbBehavior, sc, cartSimulationRequest, _callback);

    }

    /**
     * Cart simulation
     * This endpoint is used to simulate a cart in VTEX Checkout.    It receives an **SKU ID**, the **quantity** of items in the cart and the ID of the **Seller**.    It sends back all information about the cart, such as the selling price of each item, rates and benefits data, payment and logistics info.    This is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data.    **Important**: The fields (&#x60;sku id&#x60;, &#x60;quantity&#x60;, &#x60;seller&#x60;, &#x60;country&#x60;, &#x60;postalCode&#x60; and &#x60;geoCoordinates&#x60;) are just examples of content that you can simulate in your cart. You can add more fields to the request as per your need. Access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) guide to check the available fields.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param rnbBehavior This parameter defines which promotions apply to the simulation. Use &#x60;0&#x60; for simulations at cart stage, which means all promotions apply. In case of window simulation use &#x60;1&#x60;, which indicates promotions that apply nominal discounts over the total purchase value shouldn&#39;t be considered on the simulation.    Note that if this not sent, the parameter is &#x60;1&#x60;. (optional, default to 0)
     * @param sc Trade Policy (Sales Channel) identification. (optional)
     * @param cartSimulationRequest  (optional)
     * @return CartSimulation200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public CartSimulation200Response cartSimulation(String contentType, String accept, Integer rnbBehavior, Integer sc, CartSimulationRequest cartSimulationRequest) throws ApiException {
        ApiResponse<CartSimulation200Response> localVarResp = cartSimulationWithHttpInfo(contentType, accept, rnbBehavior, sc, cartSimulationRequest);
        return localVarResp.getData();
    }

    /**
     * Cart simulation
     * This endpoint is used to simulate a cart in VTEX Checkout.    It receives an **SKU ID**, the **quantity** of items in the cart and the ID of the **Seller**.    It sends back all information about the cart, such as the selling price of each item, rates and benefits data, payment and logistics info.    This is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data.    **Important**: The fields (&#x60;sku id&#x60;, &#x60;quantity&#x60;, &#x60;seller&#x60;, &#x60;country&#x60;, &#x60;postalCode&#x60; and &#x60;geoCoordinates&#x60;) are just examples of content that you can simulate in your cart. You can add more fields to the request as per your need. Access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) guide to check the available fields.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param rnbBehavior This parameter defines which promotions apply to the simulation. Use &#x60;0&#x60; for simulations at cart stage, which means all promotions apply. In case of window simulation use &#x60;1&#x60;, which indicates promotions that apply nominal discounts over the total purchase value shouldn&#39;t be considered on the simulation.    Note that if this not sent, the parameter is &#x60;1&#x60;. (optional, default to 0)
     * @param sc Trade Policy (Sales Channel) identification. (optional)
     * @param cartSimulationRequest  (optional)
     * @return ApiResponse&lt;CartSimulation200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CartSimulation200Response> cartSimulationWithHttpInfo(String contentType, String accept, Integer rnbBehavior, Integer sc, CartSimulationRequest cartSimulationRequest) throws ApiException {
        okhttp3.Call localVarCall = cartSimulationValidateBeforeCall(contentType, accept, rnbBehavior, sc, cartSimulationRequest, null);
        Type localVarReturnType = new TypeToken<CartSimulation200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Cart simulation (asynchronously)
     * This endpoint is used to simulate a cart in VTEX Checkout.    It receives an **SKU ID**, the **quantity** of items in the cart and the ID of the **Seller**.    It sends back all information about the cart, such as the selling price of each item, rates and benefits data, payment and logistics info.    This is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data.    **Important**: The fields (&#x60;sku id&#x60;, &#x60;quantity&#x60;, &#x60;seller&#x60;, &#x60;country&#x60;, &#x60;postalCode&#x60; and &#x60;geoCoordinates&#x60;) are just examples of content that you can simulate in your cart. You can add more fields to the request as per your need. Access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) guide to check the available fields.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param rnbBehavior This parameter defines which promotions apply to the simulation. Use &#x60;0&#x60; for simulations at cart stage, which means all promotions apply. In case of window simulation use &#x60;1&#x60;, which indicates promotions that apply nominal discounts over the total purchase value shouldn&#39;t be considered on the simulation.    Note that if this not sent, the parameter is &#x60;1&#x60;. (optional, default to 0)
     * @param sc Trade Policy (Sales Channel) identification. (optional)
     * @param cartSimulationRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cartSimulationAsync(String contentType, String accept, Integer rnbBehavior, Integer sc, CartSimulationRequest cartSimulationRequest, final ApiCallback<CartSimulation200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = cartSimulationValidateBeforeCall(contentType, accept, rnbBehavior, sc, cartSimulationRequest, _callback);
        Type localVarReturnType = new TypeToken<CartSimulation200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createANewCart
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param forceNewCart Use this query parameter to create a new empty shopping cart. (optional, default to true)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createANewCartCall(String contentType, String accept, Boolean forceNewCart, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/checkout/pub/orderForm";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (forceNewCart != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("forceNewCart", forceNewCart));
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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createANewCartValidateBeforeCall(String contentType, String accept, Boolean forceNewCart, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling createANewCart(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling createANewCart(Async)");
        }

        return createANewCartCall(contentType, accept, forceNewCart, _callback);

    }

    /**
     * Get current or create a new cart
     * You can use this request to get your current shopping cart information (&#x60;orderFormId&#x60;) or to create a new cart.    **Important**: To create a new empty shopping cart you need to send this request with the query param &#x60;forceNewCart&#x3D;true&#x60;.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; obtained in response is the identification code of the newly created cart.    &gt; This request has a time out of 45 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param forceNewCart Use this query parameter to create a new empty shopping cart. (optional, default to true)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void createANewCart(String contentType, String accept, Boolean forceNewCart) throws ApiException {
        createANewCartWithHttpInfo(contentType, accept, forceNewCart);
    }

    /**
     * Get current or create a new cart
     * You can use this request to get your current shopping cart information (&#x60;orderFormId&#x60;) or to create a new cart.    **Important**: To create a new empty shopping cart you need to send this request with the query param &#x60;forceNewCart&#x3D;true&#x60;.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; obtained in response is the identification code of the newly created cart.    &gt; This request has a time out of 45 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param forceNewCart Use this query parameter to create a new empty shopping cart. (optional, default to true)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> createANewCartWithHttpInfo(String contentType, String accept, Boolean forceNewCart) throws ApiException {
        okhttp3.Call localVarCall = createANewCartValidateBeforeCall(contentType, accept, forceNewCart, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get current or create a new cart (asynchronously)
     * You can use this request to get your current shopping cart information (&#x60;orderFormId&#x60;) or to create a new cart.    **Important**: To create a new empty shopping cart you need to send this request with the query param &#x60;forceNewCart&#x3D;true&#x60;.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; obtained in response is the identification code of the newly created cart.    &gt; This request has a time out of 45 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param forceNewCart Use this query parameter to create a new empty shopping cart. (optional, default to true)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createANewCartAsync(String contentType, String accept, Boolean forceNewCart, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = createANewCartValidateBeforeCall(contentType, accept, forceNewCart, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getCartInformationById
     * @param orderFormId ID of the orderForm corresponding to the cart whose information you want to retrieve. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refreshOutdatedData It is possible to use the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/cart-update#itemsupdate) so as to allow outdated information in the &#x60;orderForm&#x60;, which may improve performance in some cases. To guarantee that all cart information is updated, send this request with this parameter as &#x60;true&#x60;. We recommend doing this in the final stages of the shopping experience, starting from the checkout page. (optional, default to true)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCartInformationByIdCall(String orderFormId, String contentType, String accept, Boolean refreshOutdatedData, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}"
            .replace("{" + "orderFormId" + "}", localVarApiClient.escapeString(orderFormId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (refreshOutdatedData != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("refreshOutdatedData", refreshOutdatedData));
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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getCartInformationByIdValidateBeforeCall(String orderFormId, String contentType, String accept, Boolean refreshOutdatedData, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling getCartInformationById(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling getCartInformationById(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling getCartInformationById(Async)");
        }

        return getCartInformationByIdCall(orderFormId, contentType, accept, refreshOutdatedData, _callback);

    }

    /**
     * Get cart information by ID
     * Use this request to get all information associated to a given shopping  cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.
     * @param orderFormId ID of the orderForm corresponding to the cart whose information you want to retrieve. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refreshOutdatedData It is possible to use the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/cart-update#itemsupdate) so as to allow outdated information in the &#x60;orderForm&#x60;, which may improve performance in some cases. To guarantee that all cart information is updated, send this request with this parameter as &#x60;true&#x60;. We recommend doing this in the final stages of the shopping experience, starting from the checkout page. (optional, default to true)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void getCartInformationById(String orderFormId, String contentType, String accept, Boolean refreshOutdatedData) throws ApiException {
        getCartInformationByIdWithHttpInfo(orderFormId, contentType, accept, refreshOutdatedData);
    }

    /**
     * Get cart information by ID
     * Use this request to get all information associated to a given shopping  cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.
     * @param orderFormId ID of the orderForm corresponding to the cart whose information you want to retrieve. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refreshOutdatedData It is possible to use the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/cart-update#itemsupdate) so as to allow outdated information in the &#x60;orderForm&#x60;, which may improve performance in some cases. To guarantee that all cart information is updated, send this request with this parameter as &#x60;true&#x60;. We recommend doing this in the final stages of the shopping experience, starting from the checkout page. (optional, default to true)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> getCartInformationByIdWithHttpInfo(String orderFormId, String contentType, String accept, Boolean refreshOutdatedData) throws ApiException {
        okhttp3.Call localVarCall = getCartInformationByIdValidateBeforeCall(orderFormId, contentType, accept, refreshOutdatedData, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get cart information by ID (asynchronously)
     * Use this request to get all information associated to a given shopping  cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.
     * @param orderFormId ID of the orderForm corresponding to the cart whose information you want to retrieve. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refreshOutdatedData It is possible to use the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/cart-update#itemsupdate) so as to allow outdated information in the &#x60;orderForm&#x60;, which may improve performance in some cases. To guarantee that all cart information is updated, send this request with this parameter as &#x60;true&#x60;. We recommend doing this in the final stages of the shopping experience, starting from the checkout page. (optional, default to true)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCartInformationByIdAsync(String orderFormId, String contentType, String accept, Boolean refreshOutdatedData, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getCartInformationByIdValidateBeforeCall(orderFormId, contentType, accept, refreshOutdatedData, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getCartInstallments
     * @param orderFormId ID of the &#x60;orderForm&#x60; to be consulted for installments. (required)
     * @param paymentSystem ID of the payment method to be consulted for installments. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCartInstallmentsCall(String orderFormId, Integer paymentSystem, String contentType, String accept, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/installments"
            .replace("{" + "orderFormId" + "}", localVarApiClient.escapeString(orderFormId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (paymentSystem != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("paymentSystem", paymentSystem));
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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getCartInstallmentsValidateBeforeCall(String orderFormId, Integer paymentSystem, String contentType, String accept, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling getCartInstallments(Async)");
        }

        // verify the required parameter 'paymentSystem' is set
        if (paymentSystem == null) {
            throw new ApiException("Missing the required parameter 'paymentSystem' when calling getCartInstallments(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling getCartInstallments(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling getCartInstallments(Async)");
        }

        return getCartInstallmentsCall(orderFormId, paymentSystem, contentType, accept, _callback);

    }

    /**
     * Cart installments
     * Retrieves possible amount of installments and respective values for a given cart with a given payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This endpoint can be used to get the installment options for only one payment method at a time.    This endpoint should be called only after the selected &#x60;orderForm&#x60; already has a &#x60;paymentData&#x60;.
     * @param orderFormId ID of the &#x60;orderForm&#x60; to be consulted for installments. (required)
     * @param paymentSystem ID of the payment method to be consulted for installments. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void getCartInstallments(String orderFormId, Integer paymentSystem, String contentType, String accept) throws ApiException {
        getCartInstallmentsWithHttpInfo(orderFormId, paymentSystem, contentType, accept);
    }

    /**
     * Cart installments
     * Retrieves possible amount of installments and respective values for a given cart with a given payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This endpoint can be used to get the installment options for only one payment method at a time.    This endpoint should be called only after the selected &#x60;orderForm&#x60; already has a &#x60;paymentData&#x60;.
     * @param orderFormId ID of the &#x60;orderForm&#x60; to be consulted for installments. (required)
     * @param paymentSystem ID of the payment method to be consulted for installments. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> getCartInstallmentsWithHttpInfo(String orderFormId, Integer paymentSystem, String contentType, String accept) throws ApiException {
        okhttp3.Call localVarCall = getCartInstallmentsValidateBeforeCall(orderFormId, paymentSystem, contentType, accept, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Cart installments (asynchronously)
     * Retrieves possible amount of installments and respective values for a given cart with a given payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This endpoint can be used to get the installment options for only one payment method at a time.    This endpoint should be called only after the selected &#x60;orderForm&#x60; already has a &#x60;paymentData&#x60;.
     * @param orderFormId ID of the &#x60;orderForm&#x60; to be consulted for installments. (required)
     * @param paymentSystem ID of the payment method to be consulted for installments. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCartInstallmentsAsync(String orderFormId, Integer paymentSystem, String contentType, String accept, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getCartInstallmentsValidateBeforeCall(orderFormId, paymentSystem, contentType, accept, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for ignoreProfileData
     * @param orderFormId ID of the orderForm corresponding to the cart whose items will have the price changed. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param ignoreProfileDataRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call ignoreProfileDataCall(String orderFormId, String contentType, String accept, IgnoreProfileDataRequest ignoreProfileDataRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = ignoreProfileDataRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/profile"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "PATCH", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call ignoreProfileDataValidateBeforeCall(String orderFormId, String contentType, String accept, IgnoreProfileDataRequest ignoreProfileDataRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling ignoreProfileData(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling ignoreProfileData(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling ignoreProfileData(Async)");
        }

        // verify the required parameter 'ignoreProfileDataRequest' is set
        if (ignoreProfileDataRequest == null) {
            throw new ApiException("Missing the required parameter 'ignoreProfileDataRequest' when calling ignoreProfileData(Async)");
        }

        return ignoreProfileDataCall(orderFormId, contentType, accept, ignoreProfileDataRequest, _callback);

    }

    /**
     * Ignore profile data
     * When a shopper provides an email address at Checkout, the platform tries to retrieve existing profile information for that email and add it to the shopping cart information. Use this request if you want to change this behavior for a given cart, meaning profile information will not be included in the order automattically.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    Note that this request will only work if you have not sent the &#x60;clientProfileData&#x60; to the cart yet. Sending it to a cart that already has a &#x60;clientProfileData&#x60; should return a status &#x60;403 Forbidden&#x60; error, with an &#x60;Access denied&#x60; message.
     * @param orderFormId ID of the orderForm corresponding to the cart whose items will have the price changed. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param ignoreProfileDataRequest  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void ignoreProfileData(String orderFormId, String contentType, String accept, IgnoreProfileDataRequest ignoreProfileDataRequest) throws ApiException {
        ignoreProfileDataWithHttpInfo(orderFormId, contentType, accept, ignoreProfileDataRequest);
    }

    /**
     * Ignore profile data
     * When a shopper provides an email address at Checkout, the platform tries to retrieve existing profile information for that email and add it to the shopping cart information. Use this request if you want to change this behavior for a given cart, meaning profile information will not be included in the order automattically.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    Note that this request will only work if you have not sent the &#x60;clientProfileData&#x60; to the cart yet. Sending it to a cart that already has a &#x60;clientProfileData&#x60; should return a status &#x60;403 Forbidden&#x60; error, with an &#x60;Access denied&#x60; message.
     * @param orderFormId ID of the orderForm corresponding to the cart whose items will have the price changed. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param ignoreProfileDataRequest  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> ignoreProfileDataWithHttpInfo(String orderFormId, String contentType, String accept, IgnoreProfileDataRequest ignoreProfileDataRequest) throws ApiException {
        okhttp3.Call localVarCall = ignoreProfileDataValidateBeforeCall(orderFormId, contentType, accept, ignoreProfileDataRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Ignore profile data (asynchronously)
     * When a shopper provides an email address at Checkout, the platform tries to retrieve existing profile information for that email and add it to the shopping cart information. Use this request if you want to change this behavior for a given cart, meaning profile information will not be included in the order automattically.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    Note that this request will only work if you have not sent the &#x60;clientProfileData&#x60; to the cart yet. Sending it to a cart that already has a &#x60;clientProfileData&#x60; should return a status &#x60;403 Forbidden&#x60; error, with an &#x60;Access denied&#x60; message.
     * @param orderFormId ID of the orderForm corresponding to the cart whose items will have the price changed. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param ignoreProfileDataRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call ignoreProfileDataAsync(String orderFormId, String contentType, String accept, IgnoreProfileDataRequest ignoreProfileDataRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = ignoreProfileDataValidateBeforeCall(orderFormId, contentType, accept, ignoreProfileDataRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for items
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm corresponding to the cart in which the new item will be added. (required)
     * @param itemsRequest  (required)
     * @param allowedOutdatedData In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call itemsCall(String contentType, String accept, String orderFormId, ItemsRequest itemsRequest, List<Object> allowedOutdatedData, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = itemsRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/items"
            .replace("{" + "orderFormId" + "}", localVarApiClient.escapeString(orderFormId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (allowedOutdatedData != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "allowedOutdatedData", allowedOutdatedData));
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call itemsValidateBeforeCall(String contentType, String accept, String orderFormId, ItemsRequest itemsRequest, List<Object> allowedOutdatedData, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling items(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling items(Async)");
        }

        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling items(Async)");
        }

        // verify the required parameter 'itemsRequest' is set
        if (itemsRequest == null) {
            throw new ApiException("Missing the required parameter 'itemsRequest' when calling items(Async)");
        }

        return itemsCall(contentType, accept, orderFormId, itemsRequest, allowedOutdatedData, _callback);

    }

    /**
     * Add cart items
     * Use this request to add a new item to the shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm corresponding to the cart in which the new item will be added. (required)
     * @param itemsRequest  (required)
     * @param allowedOutdatedData In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;. (optional)
     * @return Items200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Items200Response items(String contentType, String accept, String orderFormId, ItemsRequest itemsRequest, List<Object> allowedOutdatedData) throws ApiException {
        ApiResponse<Items200Response> localVarResp = itemsWithHttpInfo(contentType, accept, orderFormId, itemsRequest, allowedOutdatedData);
        return localVarResp.getData();
    }

    /**
     * Add cart items
     * Use this request to add a new item to the shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm corresponding to the cart in which the new item will be added. (required)
     * @param itemsRequest  (required)
     * @param allowedOutdatedData In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;. (optional)
     * @return ApiResponse&lt;Items200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Items200Response> itemsWithHttpInfo(String contentType, String accept, String orderFormId, ItemsRequest itemsRequest, List<Object> allowedOutdatedData) throws ApiException {
        okhttp3.Call localVarCall = itemsValidateBeforeCall(contentType, accept, orderFormId, itemsRequest, allowedOutdatedData, null);
        Type localVarReturnType = new TypeToken<Items200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add cart items (asynchronously)
     * Use this request to add a new item to the shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm corresponding to the cart in which the new item will be added. (required)
     * @param itemsRequest  (required)
     * @param allowedOutdatedData In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call itemsAsync(String contentType, String accept, String orderFormId, ItemsRequest itemsRequest, List<Object> allowedOutdatedData, final ApiCallback<Items200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = itemsValidateBeforeCall(contentType, accept, orderFormId, itemsRequest, allowedOutdatedData, _callback);
        Type localVarReturnType = new TypeToken<Items200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for itemsUpdate
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the &#x60;orderForm&#x60; corresponding to the cart whose items you want to update. (required)
     * @param itemsUpdateRequest  (required)
     * @param allowedOutdatedData In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call itemsUpdateCall(String contentType, String accept, String orderFormId, ItemsUpdateRequest itemsUpdateRequest, List<Object> allowedOutdatedData, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = itemsUpdateRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/items/update"
            .replace("{" + "orderFormId" + "}", localVarApiClient.escapeString(orderFormId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (allowedOutdatedData != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "allowedOutdatedData", allowedOutdatedData));
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call itemsUpdateValidateBeforeCall(String contentType, String accept, String orderFormId, ItemsUpdateRequest itemsUpdateRequest, List<Object> allowedOutdatedData, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling itemsUpdate(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling itemsUpdate(Async)");
        }

        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling itemsUpdate(Async)");
        }

        // verify the required parameter 'itemsUpdateRequest' is set
        if (itemsUpdateRequest == null) {
            throw new ApiException("Missing the required parameter 'itemsUpdateRequest' when calling itemsUpdate(Async)");
        }

        return itemsUpdateCall(contentType, accept, orderFormId, itemsUpdateRequest, allowedOutdatedData, _callback);

    }

    /**
     * Update cart items
     * You can use this request to:    1. Change the quantity of one or more items in a specific cart.  2. Remove an item from the cart (by sending the &#x60;quantity&#x60; value &#x3D; &#x60;0&#x60; in the request body).    **Important**: To remove all items from the cart at the same time, use the [Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems) endpoint.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the &#x60;orderForm&#x60; corresponding to the cart whose items you want to update. (required)
     * @param itemsUpdateRequest  (required)
     * @param allowedOutdatedData In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;. (optional)
     * @return ItemsUpdate200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ItemsUpdate200Response itemsUpdate(String contentType, String accept, String orderFormId, ItemsUpdateRequest itemsUpdateRequest, List<Object> allowedOutdatedData) throws ApiException {
        ApiResponse<ItemsUpdate200Response> localVarResp = itemsUpdateWithHttpInfo(contentType, accept, orderFormId, itemsUpdateRequest, allowedOutdatedData);
        return localVarResp.getData();
    }

    /**
     * Update cart items
     * You can use this request to:    1. Change the quantity of one or more items in a specific cart.  2. Remove an item from the cart (by sending the &#x60;quantity&#x60; value &#x3D; &#x60;0&#x60; in the request body).    **Important**: To remove all items from the cart at the same time, use the [Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems) endpoint.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the &#x60;orderForm&#x60; corresponding to the cart whose items you want to update. (required)
     * @param itemsUpdateRequest  (required)
     * @param allowedOutdatedData In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;. (optional)
     * @return ApiResponse&lt;ItemsUpdate200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ItemsUpdate200Response> itemsUpdateWithHttpInfo(String contentType, String accept, String orderFormId, ItemsUpdateRequest itemsUpdateRequest, List<Object> allowedOutdatedData) throws ApiException {
        okhttp3.Call localVarCall = itemsUpdateValidateBeforeCall(contentType, accept, orderFormId, itemsUpdateRequest, allowedOutdatedData, null);
        Type localVarReturnType = new TypeToken<ItemsUpdate200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update cart items (asynchronously)
     * You can use this request to:    1. Change the quantity of one or more items in a specific cart.  2. Remove an item from the cart (by sending the &#x60;quantity&#x60; value &#x3D; &#x60;0&#x60; in the request body).    **Important**: To remove all items from the cart at the same time, use the [Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems) endpoint.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the &#x60;orderForm&#x60; corresponding to the cart whose items you want to update. (required)
     * @param itemsUpdateRequest  (required)
     * @param allowedOutdatedData In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call itemsUpdateAsync(String contentType, String accept, String orderFormId, ItemsUpdateRequest itemsUpdateRequest, List<Object> allowedOutdatedData, final ApiCallback<ItemsUpdate200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = itemsUpdateValidateBeforeCall(contentType, accept, orderFormId, itemsUpdateRequest, allowedOutdatedData, _callback);
        Type localVarReturnType = new TypeToken<ItemsUpdate200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for priceChange
     * @param orderFormId ID of the orderForm corresponding to the cart whose items will have the price changed. (required)
     * @param itemIndex The index of the item in the cart. Each cart item is identified by an index, starting in 0. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param priceChangeRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call priceChangeCall(String orderFormId, String itemIndex, String contentType, String accept, PriceChangeRequest priceChangeRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = priceChangeRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/items/{itemIndex}/price"
            .replace("{" + "orderFormId" + "}", localVarApiClient.escapeString(orderFormId.toString()))
            .replace("{" + "itemIndex" + "}", localVarApiClient.escapeString(itemIndex.toString()));

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

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call priceChangeValidateBeforeCall(String orderFormId, String itemIndex, String contentType, String accept, PriceChangeRequest priceChangeRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling priceChange(Async)");
        }

        // verify the required parameter 'itemIndex' is set
        if (itemIndex == null) {
            throw new ApiException("Missing the required parameter 'itemIndex' when calling priceChange(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling priceChange(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling priceChange(Async)");
        }

        // verify the required parameter 'priceChangeRequest' is set
        if (priceChangeRequest == null) {
            throw new ApiException("Missing the required parameter 'priceChangeRequest' when calling priceChange(Async)");
        }

        return priceChangeCall(orderFormId, itemIndex, contentType, accept, priceChangeRequest, _callback);

    }

    /**
     * Change price
     * This request changes the price of an SKU in a cart. You can also perform type of bulk price change with the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#itemsupdate)    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    You need to inform which cart you are referring to, by sending its &#x60;orderFormId&#x60;; and what is the item whose price you want to change, by sending its &#x60;itemIndex&#x60;.    You also need to pass the new price value in the body.    Remember that, to use this endpoint, the feature of *manual price* must be active. To check if it&#39;s active, use the [Get orderForm configuration](https://developers.vtex.com/reference#getorderformconfiguration) endpoint. To make it active, use the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) endpoint, making the &#x60;allowManualPrice&#x60; field &#x60;true&#x60;.    &gt; Whenever you use this request to change the price of an item, all items in that cart with the same SKU are affected by this change. This applies even to items that share the SKU but have been separated into different objects in the &#x60;items&#x60; array due to customizations or attachments, for example.
     * @param orderFormId ID of the orderForm corresponding to the cart whose items will have the price changed. (required)
     * @param itemIndex The index of the item in the cart. Each cart item is identified by an index, starting in 0. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param priceChangeRequest  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void priceChange(String orderFormId, String itemIndex, String contentType, String accept, PriceChangeRequest priceChangeRequest) throws ApiException {
        priceChangeWithHttpInfo(orderFormId, itemIndex, contentType, accept, priceChangeRequest);
    }

    /**
     * Change price
     * This request changes the price of an SKU in a cart. You can also perform type of bulk price change with the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#itemsupdate)    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    You need to inform which cart you are referring to, by sending its &#x60;orderFormId&#x60;; and what is the item whose price you want to change, by sending its &#x60;itemIndex&#x60;.    You also need to pass the new price value in the body.    Remember that, to use this endpoint, the feature of *manual price* must be active. To check if it&#39;s active, use the [Get orderForm configuration](https://developers.vtex.com/reference#getorderformconfiguration) endpoint. To make it active, use the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) endpoint, making the &#x60;allowManualPrice&#x60; field &#x60;true&#x60;.    &gt; Whenever you use this request to change the price of an item, all items in that cart with the same SKU are affected by this change. This applies even to items that share the SKU but have been separated into different objects in the &#x60;items&#x60; array due to customizations or attachments, for example.
     * @param orderFormId ID of the orderForm corresponding to the cart whose items will have the price changed. (required)
     * @param itemIndex The index of the item in the cart. Each cart item is identified by an index, starting in 0. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param priceChangeRequest  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> priceChangeWithHttpInfo(String orderFormId, String itemIndex, String contentType, String accept, PriceChangeRequest priceChangeRequest) throws ApiException {
        okhttp3.Call localVarCall = priceChangeValidateBeforeCall(orderFormId, itemIndex, contentType, accept, priceChangeRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Change price (asynchronously)
     * This request changes the price of an SKU in a cart. You can also perform type of bulk price change with the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#itemsupdate)    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    You need to inform which cart you are referring to, by sending its &#x60;orderFormId&#x60;; and what is the item whose price you want to change, by sending its &#x60;itemIndex&#x60;.    You also need to pass the new price value in the body.    Remember that, to use this endpoint, the feature of *manual price* must be active. To check if it&#39;s active, use the [Get orderForm configuration](https://developers.vtex.com/reference#getorderformconfiguration) endpoint. To make it active, use the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) endpoint, making the &#x60;allowManualPrice&#x60; field &#x60;true&#x60;.    &gt; Whenever you use this request to change the price of an item, all items in that cart with the same SKU are affected by this change. This applies even to items that share the SKU but have been separated into different objects in the &#x60;items&#x60; array due to customizations or attachments, for example.
     * @param orderFormId ID of the orderForm corresponding to the cart whose items will have the price changed. (required)
     * @param itemIndex The index of the item in the cart. Each cart item is identified by an index, starting in 0. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param priceChangeRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call priceChangeAsync(String orderFormId, String itemIndex, String contentType, String accept, PriceChangeRequest priceChangeRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = priceChangeValidateBeforeCall(orderFormId, itemIndex, contentType, accept, priceChangeRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for removeAllItems
     * @param orderFormId ID of the orderForm corresponding to the cart whose items you want to remove. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param body  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removeAllItemsCall(String orderFormId, String contentType, String accept, Object body, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = body;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/items/removeAll"
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
    private okhttp3.Call removeAllItemsValidateBeforeCall(String orderFormId, String contentType, String accept, Object body, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling removeAllItems(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling removeAllItems(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling removeAllItems(Async)");
        }

        return removeAllItemsCall(orderFormId, contentType, accept, body, _callback);

    }

    /**
     * Remove all items
     * This request removes all items from a given cart, leaving it empty.    You must send an empty JSON in the body of the request.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    **Important**: **Request Body** must always be sent with empty value \&quot;{ }\&quot; in this endpoint.
     * @param orderFormId ID of the orderForm corresponding to the cart whose items you want to remove. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param body  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public Object removeAllItems(String orderFormId, String contentType, String accept, Object body) throws ApiException {
        ApiResponse<Object> localVarResp = removeAllItemsWithHttpInfo(orderFormId, contentType, accept, body);
        return localVarResp.getData();
    }

    /**
     * Remove all items
     * This request removes all items from a given cart, leaving it empty.    You must send an empty JSON in the body of the request.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    **Important**: **Request Body** must always be sent with empty value \&quot;{ }\&quot; in this endpoint.
     * @param orderFormId ID of the orderForm corresponding to the cart whose items you want to remove. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param body  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> removeAllItemsWithHttpInfo(String orderFormId, String contentType, String accept, Object body) throws ApiException {
        okhttp3.Call localVarCall = removeAllItemsValidateBeforeCall(orderFormId, contentType, accept, body, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Remove all items (asynchronously)
     * This request removes all items from a given cart, leaving it empty.    You must send an empty JSON in the body of the request.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    **Important**: **Request Body** must always be sent with empty value \&quot;{ }\&quot; in this endpoint.
     * @param orderFormId ID of the orderForm corresponding to the cart whose items you want to remove. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param body  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removeAllItemsAsync(String orderFormId, String contentType, String accept, Object body, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = removeAllItemsValidateBeforeCall(orderFormId, contentType, accept, body, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for removeallpersonaldata
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm corresponding to the cart whose user&#39;s personal data you want to remove. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removeallpersonaldataCall(String contentType, String accept, String orderFormId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/checkout/changeToAnonymousUser/{orderFormId}"
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
            "text/plain"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call removeallpersonaldataValidateBeforeCall(String contentType, String accept, String orderFormId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling removeallpersonaldata(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling removeallpersonaldata(Async)");
        }

        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling removeallpersonaldata(Async)");
        }

        return removeallpersonaldataCall(contentType, accept, orderFormId, _callback);

    }

    /**
     * Remove all personal data
     * This call removes all user information, making a cart anonymous while leaving the items.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information about it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This call works by creating a new orderForm, setting a new cookie, and returning a redirect 302 to the cart URL (&#x60;/checkout/#/orderform&#x60;).
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm corresponding to the cart whose user&#39;s personal data you want to remove. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object removeallpersonaldata(String contentType, String accept, String orderFormId) throws ApiException {
        ApiResponse<Object> localVarResp = removeallpersonaldataWithHttpInfo(contentType, accept, orderFormId);
        return localVarResp.getData();
    }

    /**
     * Remove all personal data
     * This call removes all user information, making a cart anonymous while leaving the items.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information about it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This call works by creating a new orderForm, setting a new cookie, and returning a redirect 302 to the cart URL (&#x60;/checkout/#/orderform&#x60;).
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm corresponding to the cart whose user&#39;s personal data you want to remove. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> removeallpersonaldataWithHttpInfo(String contentType, String accept, String orderFormId) throws ApiException {
        okhttp3.Call localVarCall = removeallpersonaldataValidateBeforeCall(contentType, accept, orderFormId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Remove all personal data (asynchronously)
     * This call removes all user information, making a cart anonymous while leaving the items.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information about it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This call works by creating a new orderForm, setting a new cookie, and returning a redirect 302 to the cart URL (&#x60;/checkout/#/orderform&#x60;).
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm corresponding to the cart whose user&#39;s personal data you want to remove. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removeallpersonaldataAsync(String contentType, String accept, String orderFormId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = removeallpersonaldataValidateBeforeCall(contentType, accept, orderFormId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
