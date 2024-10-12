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


import org.openapitools.client.model.AddClientPreferencesRequest;
import org.openapitools.client.model.AddClientProfileRequest;
import org.openapitools.client.model.AddMarketingDataRequest;
import org.openapitools.client.model.AddMerchantContextData200Response;
import org.openapitools.client.model.AddMerchantContextDataRequest;
import org.openapitools.client.model.AddPaymentDataRequest;
import org.openapitools.client.model.AddShippingAddressRequest;
import org.openapitools.client.model.GetClientProfileByEmail200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CartAttachmentsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CartAttachmentsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CartAttachmentsApi(ApiClient apiClient) {
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
     * Build call for addClientPreferences
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addClientPreferencesRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addClientPreferencesCall(String contentType, String accept, String orderFormId, AddClientPreferencesRequest addClientPreferencesRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addClientPreferencesRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/attachments/clientPreferencesData"
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
    private okhttp3.Call addClientPreferencesValidateBeforeCall(String contentType, String accept, String orderFormId, AddClientPreferencesRequest addClientPreferencesRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling addClientPreferences(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling addClientPreferences(Async)");
        }

        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling addClientPreferences(Async)");
        }

        // verify the required parameter 'addClientPreferencesRequest' is set
        if (addClientPreferencesRequest == null) {
            throw new ApiException("Missing the required parameter 'addClientPreferencesRequest' when calling addClientPreferences(Async)");
        }

        return addClientPreferencesCall(contentType, accept, orderFormId, addClientPreferencesRequest, _callback);

    }

    /**
     * Add client preferences
     * Use this request to include client preferences information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addClientPreferencesRequest  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object addClientPreferences(String contentType, String accept, String orderFormId, AddClientPreferencesRequest addClientPreferencesRequest) throws ApiException {
        ApiResponse<Object> localVarResp = addClientPreferencesWithHttpInfo(contentType, accept, orderFormId, addClientPreferencesRequest);
        return localVarResp.getData();
    }

    /**
     * Add client preferences
     * Use this request to include client preferences information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addClientPreferencesRequest  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> addClientPreferencesWithHttpInfo(String contentType, String accept, String orderFormId, AddClientPreferencesRequest addClientPreferencesRequest) throws ApiException {
        okhttp3.Call localVarCall = addClientPreferencesValidateBeforeCall(contentType, accept, orderFormId, addClientPreferencesRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add client preferences (asynchronously)
     * Use this request to include client preferences information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addClientPreferencesRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addClientPreferencesAsync(String contentType, String accept, String orderFormId, AddClientPreferencesRequest addClientPreferencesRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = addClientPreferencesValidateBeforeCall(contentType, accept, orderFormId, addClientPreferencesRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for addClientProfile
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addClientProfileRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addClientProfileCall(String contentType, String accept, String orderFormId, AddClientProfileRequest addClientProfileRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addClientProfileRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/attachments/clientProfileData"
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
    private okhttp3.Call addClientProfileValidateBeforeCall(String contentType, String accept, String orderFormId, AddClientProfileRequest addClientProfileRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling addClientProfile(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling addClientProfile(Async)");
        }

        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling addClientProfile(Async)");
        }

        // verify the required parameter 'addClientProfileRequest' is set
        if (addClientProfileRequest == null) {
            throw new ApiException("Missing the required parameter 'addClientProfileRequest' when calling addClientProfile(Async)");
        }

        return addClientProfileCall(contentType, accept, orderFormId, addClientProfileRequest, _callback);

    }

    /**
     * Add client profile
     * Use this request to include client profile information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addClientProfileRequest  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void addClientProfile(String contentType, String accept, String orderFormId, AddClientProfileRequest addClientProfileRequest) throws ApiException {
        addClientProfileWithHttpInfo(contentType, accept, orderFormId, addClientProfileRequest);
    }

    /**
     * Add client profile
     * Use this request to include client profile information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addClientProfileRequest  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> addClientProfileWithHttpInfo(String contentType, String accept, String orderFormId, AddClientProfileRequest addClientProfileRequest) throws ApiException {
        okhttp3.Call localVarCall = addClientProfileValidateBeforeCall(contentType, accept, orderFormId, addClientProfileRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Add client profile (asynchronously)
     * Use this request to include client profile information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addClientProfileRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addClientProfileAsync(String contentType, String accept, String orderFormId, AddClientProfileRequest addClientProfileRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = addClientProfileValidateBeforeCall(contentType, accept, orderFormId, addClientProfileRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for addMarketingData
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addMarketingDataRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addMarketingDataCall(String contentType, String accept, String orderFormId, AddMarketingDataRequest addMarketingDataRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addMarketingDataRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/attachments/marketingData"
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
    private okhttp3.Call addMarketingDataValidateBeforeCall(String contentType, String accept, String orderFormId, AddMarketingDataRequest addMarketingDataRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling addMarketingData(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling addMarketingData(Async)");
        }

        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling addMarketingData(Async)");
        }

        // verify the required parameter 'addMarketingDataRequest' is set
        if (addMarketingDataRequest == null) {
            throw new ApiException("Missing the required parameter 'addMarketingDataRequest' when calling addMarketingData(Async)");
        }

        return addMarketingDataCall(contentType, accept, orderFormId, addMarketingDataRequest, _callback);

    }

    /**
     * Add marketing data
     * Use this request to include marketing information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addMarketingDataRequest  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void addMarketingData(String contentType, String accept, String orderFormId, AddMarketingDataRequest addMarketingDataRequest) throws ApiException {
        addMarketingDataWithHttpInfo(contentType, accept, orderFormId, addMarketingDataRequest);
    }

    /**
     * Add marketing data
     * Use this request to include marketing information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addMarketingDataRequest  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> addMarketingDataWithHttpInfo(String contentType, String accept, String orderFormId, AddMarketingDataRequest addMarketingDataRequest) throws ApiException {
        okhttp3.Call localVarCall = addMarketingDataValidateBeforeCall(contentType, accept, orderFormId, addMarketingDataRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Add marketing data (asynchronously)
     * Use this request to include marketing information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addMarketingDataRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addMarketingDataAsync(String contentType, String accept, String orderFormId, AddMarketingDataRequest addMarketingDataRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = addMarketingDataValidateBeforeCall(contentType, accept, orderFormId, addMarketingDataRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for addMerchantContextData
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive the relevant information added by the merchant. (required)
     * @param addMerchantContextDataRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addMerchantContextDataCall(String contentType, String accept, String orderFormId, AddMerchantContextDataRequest addMerchantContextDataRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addMerchantContextDataRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/attachments/merchantContextData"
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
    private okhttp3.Call addMerchantContextDataValidateBeforeCall(String contentType, String accept, String orderFormId, AddMerchantContextDataRequest addMerchantContextDataRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling addMerchantContextData(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling addMerchantContextData(Async)");
        }

        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling addMerchantContextData(Async)");
        }

        // verify the required parameter 'addMerchantContextDataRequest' is set
        if (addMerchantContextDataRequest == null) {
            throw new ApiException("Missing the required parameter 'addMerchantContextDataRequest' when calling addMerchantContextData(Async)");
        }

        return addMerchantContextDataCall(contentType, accept, orderFormId, addMerchantContextDataRequest, _callback);

    }

    /**
     * Add merchant context data
     * This endpoint is used for the merchant to add to the cart any relevant information that is related to the context of a specific order.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive the relevant information added by the merchant. (required)
     * @param addMerchantContextDataRequest  (required)
     * @return AddMerchantContextData200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public AddMerchantContextData200Response addMerchantContextData(String contentType, String accept, String orderFormId, AddMerchantContextDataRequest addMerchantContextDataRequest) throws ApiException {
        ApiResponse<AddMerchantContextData200Response> localVarResp = addMerchantContextDataWithHttpInfo(contentType, accept, orderFormId, addMerchantContextDataRequest);
        return localVarResp.getData();
    }

    /**
     * Add merchant context data
     * This endpoint is used for the merchant to add to the cart any relevant information that is related to the context of a specific order.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive the relevant information added by the merchant. (required)
     * @param addMerchantContextDataRequest  (required)
     * @return ApiResponse&lt;AddMerchantContextData200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AddMerchantContextData200Response> addMerchantContextDataWithHttpInfo(String contentType, String accept, String orderFormId, AddMerchantContextDataRequest addMerchantContextDataRequest) throws ApiException {
        okhttp3.Call localVarCall = addMerchantContextDataValidateBeforeCall(contentType, accept, orderFormId, addMerchantContextDataRequest, null);
        Type localVarReturnType = new TypeToken<AddMerchantContextData200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add merchant context data (asynchronously)
     * This endpoint is used for the merchant to add to the cart any relevant information that is related to the context of a specific order.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive the relevant information added by the merchant. (required)
     * @param addMerchantContextDataRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addMerchantContextDataAsync(String contentType, String accept, String orderFormId, AddMerchantContextDataRequest addMerchantContextDataRequest, final ApiCallback<AddMerchantContextData200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = addMerchantContextDataValidateBeforeCall(contentType, accept, orderFormId, addMerchantContextDataRequest, _callback);
        Type localVarReturnType = new TypeToken<AddMerchantContextData200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for addPaymentData
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addPaymentDataRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addPaymentDataCall(String contentType, String accept, String orderFormId, AddPaymentDataRequest addPaymentDataRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addPaymentDataRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/attachments/paymentData"
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
    private okhttp3.Call addPaymentDataValidateBeforeCall(String contentType, String accept, String orderFormId, AddPaymentDataRequest addPaymentDataRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling addPaymentData(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling addPaymentData(Async)");
        }

        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling addPaymentData(Async)");
        }

        // verify the required parameter 'addPaymentDataRequest' is set
        if (addPaymentDataRequest == null) {
            throw new ApiException("Missing the required parameter 'addPaymentDataRequest' when calling addPaymentData(Async)");
        }

        return addPaymentDataCall(contentType, accept, orderFormId, addPaymentDataRequest, _callback);

    }

    /**
     * Add payment data
     * Use this request to include payment information to a given shopping cart. The payment information attachment in the shopping cart does not determine the final order payment method in itself. However, it allows tha platform to update any relevant information that may be impacted by the payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addPaymentDataRequest  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void addPaymentData(String contentType, String accept, String orderFormId, AddPaymentDataRequest addPaymentDataRequest) throws ApiException {
        addPaymentDataWithHttpInfo(contentType, accept, orderFormId, addPaymentDataRequest);
    }

    /**
     * Add payment data
     * Use this request to include payment information to a given shopping cart. The payment information attachment in the shopping cart does not determine the final order payment method in itself. However, it allows tha platform to update any relevant information that may be impacted by the payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addPaymentDataRequest  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> addPaymentDataWithHttpInfo(String contentType, String accept, String orderFormId, AddPaymentDataRequest addPaymentDataRequest) throws ApiException {
        okhttp3.Call localVarCall = addPaymentDataValidateBeforeCall(contentType, accept, orderFormId, addPaymentDataRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Add payment data (asynchronously)
     * Use this request to include payment information to a given shopping cart. The payment information attachment in the shopping cart does not determine the final order payment method in itself. However, it allows tha platform to update any relevant information that may be impacted by the payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addPaymentDataRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addPaymentDataAsync(String contentType, String accept, String orderFormId, AddPaymentDataRequest addPaymentDataRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = addPaymentDataValidateBeforeCall(contentType, accept, orderFormId, addPaymentDataRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for addShippingAddress
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addShippingAddressRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addShippingAddressCall(String contentType, String accept, String orderFormId, AddShippingAddressRequest addShippingAddressRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addShippingAddressRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/attachments/shippingData"
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
    private okhttp3.Call addShippingAddressValidateBeforeCall(String contentType, String accept, String orderFormId, AddShippingAddressRequest addShippingAddressRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling addShippingAddress(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling addShippingAddress(Async)");
        }

        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling addShippingAddress(Async)");
        }

        // verify the required parameter 'addShippingAddressRequest' is set
        if (addShippingAddressRequest == null) {
            throw new ApiException("Missing the required parameter 'addShippingAddressRequest' when calling addShippingAddress(Async)");
        }

        return addShippingAddressCall(contentType, accept, orderFormId, addShippingAddressRequest, _callback);

    }

    /**
     * Add shipping address and select delivery option
     * Use this request to include shipping information and/or selected delivery option to a given shopping cart.    To add shipping addresses send the &#x60;selectedAddresses&#x60; array. For delivery option use the &#x60;logisticsInfo&#x60; array.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addShippingAddressRequest  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void addShippingAddress(String contentType, String accept, String orderFormId, AddShippingAddressRequest addShippingAddressRequest) throws ApiException {
        addShippingAddressWithHttpInfo(contentType, accept, orderFormId, addShippingAddressRequest);
    }

    /**
     * Add shipping address and select delivery option
     * Use this request to include shipping information and/or selected delivery option to a given shopping cart.    To add shipping addresses send the &#x60;selectedAddresses&#x60; array. For delivery option use the &#x60;logisticsInfo&#x60; array.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addShippingAddressRequest  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> addShippingAddressWithHttpInfo(String contentType, String accept, String orderFormId, AddShippingAddressRequest addShippingAddressRequest) throws ApiException {
        okhttp3.Call localVarCall = addShippingAddressValidateBeforeCall(contentType, accept, orderFormId, addShippingAddressRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Add shipping address and select delivery option (asynchronously)
     * Use this request to include shipping information and/or selected delivery option to a given shopping cart.    To add shipping addresses send the &#x60;selectedAddresses&#x60; array. For delivery option use the &#x60;logisticsInfo&#x60; array.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId ID of the orderForm that will receive client profile information. (required)
     * @param addShippingAddressRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addShippingAddressAsync(String contentType, String accept, String orderFormId, AddShippingAddressRequest addShippingAddressRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = addShippingAddressValidateBeforeCall(contentType, accept, orderFormId, addShippingAddressRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getClientProfileByEmail
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param email Client&#39;s email address to be searched. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClientProfileByEmailCall(String contentType, String accept, String email, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/checkout/pub/profiles";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (email != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("email", email));
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
    private okhttp3.Call getClientProfileByEmailValidateBeforeCall(String contentType, String accept, String email, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling getClientProfileByEmail(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling getClientProfileByEmail(Async)");
        }

        // verify the required parameter 'email' is set
        if (email == null) {
            throw new ApiException("Missing the required parameter 'email' when calling getClientProfileByEmail(Async)");
        }

        return getClientProfileByEmailCall(contentType, accept, email, _callback);

    }

    /**
     * Get client profile by email
     * Retrieve a client&#39;s profile information by providing an email address.    If the response body fields are empty, the following situations may have occurred:    1. There is no client registered with the email address provided in your store, or;  2. Client profile is invalid or incomplete. For more information, see [SmartCheckout - Customer information automatic fill-in](https://help.vtex.com/en/tutorial/smartcheckout-customer-information-automatic-fill-in--2Nuu3xAFzdhIzJIldAdtan).    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are consulting information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param email Client&#39;s email address to be searched. (required)
     * @return GetClientProfileByEmail200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetClientProfileByEmail200Response getClientProfileByEmail(String contentType, String accept, String email) throws ApiException {
        ApiResponse<GetClientProfileByEmail200Response> localVarResp = getClientProfileByEmailWithHttpInfo(contentType, accept, email);
        return localVarResp.getData();
    }

    /**
     * Get client profile by email
     * Retrieve a client&#39;s profile information by providing an email address.    If the response body fields are empty, the following situations may have occurred:    1. There is no client registered with the email address provided in your store, or;  2. Client profile is invalid or incomplete. For more information, see [SmartCheckout - Customer information automatic fill-in](https://help.vtex.com/en/tutorial/smartcheckout-customer-information-automatic-fill-in--2Nuu3xAFzdhIzJIldAdtan).    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are consulting information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param email Client&#39;s email address to be searched. (required)
     * @return ApiResponse&lt;GetClientProfileByEmail200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetClientProfileByEmail200Response> getClientProfileByEmailWithHttpInfo(String contentType, String accept, String email) throws ApiException {
        okhttp3.Call localVarCall = getClientProfileByEmailValidateBeforeCall(contentType, accept, email, null);
        Type localVarReturnType = new TypeToken<GetClientProfileByEmail200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get client profile by email (asynchronously)
     * Retrieve a client&#39;s profile information by providing an email address.    If the response body fields are empty, the following situations may have occurred:    1. There is no client registered with the email address provided in your store, or;  2. Client profile is invalid or incomplete. For more information, see [SmartCheckout - Customer information automatic fill-in](https://help.vtex.com/en/tutorial/smartcheckout-customer-information-automatic-fill-in--2Nuu3xAFzdhIzJIldAdtan).    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are consulting information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param email Client&#39;s email address to be searched. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClientProfileByEmailAsync(String contentType, String accept, String email, final ApiCallback<GetClientProfileByEmail200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getClientProfileByEmailValidateBeforeCall(contentType, accept, email, _callback);
        Type localVarReturnType = new TypeToken<GetClientProfileByEmail200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
