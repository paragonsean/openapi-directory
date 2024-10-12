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


import org.openapitools.client.model.SetsinglecustomfieldvalueRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CustomDataApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CustomDataApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CustomDataApi(ApiClient apiClient) {
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
     * Build call for removesinglecustomfieldvalue
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId The ID of the orderForm from which you want to remove the custom field value. (required)
     * @param appId ID of the app created through the Update orderForm Configuration endpoint. (required)
     * @param appFieldName Name of the app&#39;s field created through the Update orderForm Configuration endpoint and which will be deleted. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removesinglecustomfieldvalueCall(String contentType, String accept, String orderFormId, String appId, String appFieldName, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/customData/{appId}/{appFieldName}"
            .replace("{" + "orderFormId" + "}", localVarApiClient.escapeString(orderFormId.toString()))
            .replace("{" + "appId" + "}", localVarApiClient.escapeString(appId.toString()))
            .replace("{" + "appFieldName" + "}", localVarApiClient.escapeString(appFieldName.toString()));

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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call removesinglecustomfieldvalueValidateBeforeCall(String contentType, String accept, String orderFormId, String appId, String appFieldName, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling removesinglecustomfieldvalue(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling removesinglecustomfieldvalue(Async)");
        }

        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling removesinglecustomfieldvalue(Async)");
        }

        // verify the required parameter 'appId' is set
        if (appId == null) {
            throw new ApiException("Missing the required parameter 'appId' when calling removesinglecustomfieldvalue(Async)");
        }

        // verify the required parameter 'appFieldName' is set
        if (appFieldName == null) {
            throw new ApiException("Missing the required parameter 'appFieldName' when calling removesinglecustomfieldvalue(Async)");
        }

        return removesinglecustomfieldvalueCall(contentType, accept, orderFormId, appId, appFieldName, _callback);

    }

    /**
     * Remove single custom field value
     * Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can be removed by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (&#x60;appId&#x60;).    You also need to iform the specific field created in this app (identified by the &#x60;appFieldName&#x60; parameter, also passed through the URL) whose value you want to remove.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId The ID of the orderForm from which you want to remove the custom field value. (required)
     * @param appId ID of the app created through the Update orderForm Configuration endpoint. (required)
     * @param appFieldName Name of the app&#39;s field created through the Update orderForm Configuration endpoint and which will be deleted. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void removesinglecustomfieldvalue(String contentType, String accept, String orderFormId, String appId, String appFieldName) throws ApiException {
        removesinglecustomfieldvalueWithHttpInfo(contentType, accept, orderFormId, appId, appFieldName);
    }

    /**
     * Remove single custom field value
     * Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can be removed by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (&#x60;appId&#x60;).    You also need to iform the specific field created in this app (identified by the &#x60;appFieldName&#x60; parameter, also passed through the URL) whose value you want to remove.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId The ID of the orderForm from which you want to remove the custom field value. (required)
     * @param appId ID of the app created through the Update orderForm Configuration endpoint. (required)
     * @param appFieldName Name of the app&#39;s field created through the Update orderForm Configuration endpoint and which will be deleted. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> removesinglecustomfieldvalueWithHttpInfo(String contentType, String accept, String orderFormId, String appId, String appFieldName) throws ApiException {
        okhttp3.Call localVarCall = removesinglecustomfieldvalueValidateBeforeCall(contentType, accept, orderFormId, appId, appFieldName, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Remove single custom field value (asynchronously)
     * Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can be removed by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (&#x60;appId&#x60;).    You also need to iform the specific field created in this app (identified by the &#x60;appFieldName&#x60; parameter, also passed through the URL) whose value you want to remove.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param orderFormId The ID of the orderForm from which you want to remove the custom field value. (required)
     * @param appId ID of the app created through the Update orderForm Configuration endpoint. (required)
     * @param appFieldName Name of the app&#39;s field created through the Update orderForm Configuration endpoint and which will be deleted. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removesinglecustomfieldvalueAsync(String contentType, String accept, String orderFormId, String appId, String appFieldName, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = removesinglecustomfieldvalueValidateBeforeCall(contentType, accept, orderFormId, appId, appFieldName, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for setMultipleCustomFieldValues
     * @param orderFormId ID of the orderForm that will receive the new custom field values. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param appId ID of the app created with the configuration API. (required)
     * @param requestBody  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call setMultipleCustomFieldValuesCall(String orderFormId, String contentType, String accept, String appId, Map<String, Object> requestBody, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = requestBody;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/customData/{appId}"
            .replace("{" + "orderFormId" + "}", localVarApiClient.escapeString(orderFormId.toString()))
            .replace("{" + "appId" + "}", localVarApiClient.escapeString(appId.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call setMultipleCustomFieldValuesValidateBeforeCall(String orderFormId, String contentType, String accept, String appId, Map<String, Object> requestBody, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling setMultipleCustomFieldValues(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling setMultipleCustomFieldValues(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling setMultipleCustomFieldValues(Async)");
        }

        // verify the required parameter 'appId' is set
        if (appId == null) {
            throw new ApiException("Missing the required parameter 'appId' when calling setMultipleCustomFieldValues(Async)");
        }

        // verify the required parameter 'requestBody' is set
        if (requestBody == null) {
            throw new ApiException("Missing the required parameter 'requestBody' when calling setMultipleCustomFieldValues(Async)");
        }

        return setMultipleCustomFieldValuesCall(orderFormId, contentType, accept, appId, requestBody, _callback);

    }

    /**
     * Set multiple custom field values
     * Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference/configuration#updateorderformconfiguration) request. The values of these custom fields can then be updated by this request.    To do that, you need to inform the ID of the app you created with the configuration API (&#x60;appId&#x60;).    In the body of the request, for each field created in this app (&#x60;appFieldName&#x60;) you will inform a value (&#x60;appFieldValue&#x60;).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.
     * @param orderFormId ID of the orderForm that will receive the new custom field values. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param appId ID of the app created with the configuration API. (required)
     * @param requestBody  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object setMultipleCustomFieldValues(String orderFormId, String contentType, String accept, String appId, Map<String, Object> requestBody) throws ApiException {
        ApiResponse<Object> localVarResp = setMultipleCustomFieldValuesWithHttpInfo(orderFormId, contentType, accept, appId, requestBody);
        return localVarResp.getData();
    }

    /**
     * Set multiple custom field values
     * Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference/configuration#updateorderformconfiguration) request. The values of these custom fields can then be updated by this request.    To do that, you need to inform the ID of the app you created with the configuration API (&#x60;appId&#x60;).    In the body of the request, for each field created in this app (&#x60;appFieldName&#x60;) you will inform a value (&#x60;appFieldValue&#x60;).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.
     * @param orderFormId ID of the orderForm that will receive the new custom field values. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param appId ID of the app created with the configuration API. (required)
     * @param requestBody  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> setMultipleCustomFieldValuesWithHttpInfo(String orderFormId, String contentType, String accept, String appId, Map<String, Object> requestBody) throws ApiException {
        okhttp3.Call localVarCall = setMultipleCustomFieldValuesValidateBeforeCall(orderFormId, contentType, accept, appId, requestBody, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Set multiple custom field values (asynchronously)
     * Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference/configuration#updateorderformconfiguration) request. The values of these custom fields can then be updated by this request.    To do that, you need to inform the ID of the app you created with the configuration API (&#x60;appId&#x60;).    In the body of the request, for each field created in this app (&#x60;appFieldName&#x60;) you will inform a value (&#x60;appFieldValue&#x60;).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.
     * @param orderFormId ID of the orderForm that will receive the new custom field values. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param appId ID of the app created with the configuration API. (required)
     * @param requestBody  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call setMultipleCustomFieldValuesAsync(String orderFormId, String contentType, String accept, String appId, Map<String, Object> requestBody, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = setMultipleCustomFieldValuesValidateBeforeCall(orderFormId, contentType, accept, appId, requestBody, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for setSingleCustomFieldValue
     * @param orderFormId The ID of the orderForm whose custom field&#39;s value you want to change. (required)
     * @param appId ID of the app created through the Update orderForm Configuration endpoint. (required)
     * @param appFieldName Name of the app&#39;s field created through the Update orderForm Configuration endpoint. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param setsinglecustomfieldvalueRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call setSingleCustomFieldValueCall(String orderFormId, String appId, String appFieldName, String contentType, String accept, SetsinglecustomfieldvalueRequest setsinglecustomfieldvalueRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = setsinglecustomfieldvalueRequest;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/orderForm/{orderFormId}/customData/{appId}/{appFieldName}"
            .replace("{" + "orderFormId" + "}", localVarApiClient.escapeString(orderFormId.toString()))
            .replace("{" + "appId" + "}", localVarApiClient.escapeString(appId.toString()))
            .replace("{" + "appFieldName" + "}", localVarApiClient.escapeString(appFieldName.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call setSingleCustomFieldValueValidateBeforeCall(String orderFormId, String appId, String appFieldName, String contentType, String accept, SetsinglecustomfieldvalueRequest setsinglecustomfieldvalueRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orderFormId' is set
        if (orderFormId == null) {
            throw new ApiException("Missing the required parameter 'orderFormId' when calling setSingleCustomFieldValue(Async)");
        }

        // verify the required parameter 'appId' is set
        if (appId == null) {
            throw new ApiException("Missing the required parameter 'appId' when calling setSingleCustomFieldValue(Async)");
        }

        // verify the required parameter 'appFieldName' is set
        if (appFieldName == null) {
            throw new ApiException("Missing the required parameter 'appFieldName' when calling setSingleCustomFieldValue(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling setSingleCustomFieldValue(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling setSingleCustomFieldValue(Async)");
        }

        // verify the required parameter 'setsinglecustomfieldvalueRequest' is set
        if (setsinglecustomfieldvalueRequest == null) {
            throw new ApiException("Missing the required parameter 'setsinglecustomfieldvalueRequest' when calling setSingleCustomFieldValue(Async)");
        }

        return setSingleCustomFieldValueCall(orderFormId, appId, appFieldName, contentType, accept, setsinglecustomfieldvalueRequest, _callback);

    }

    /**
     * Set single custom field value
     * Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can then be updated by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (&#x60;appId&#x60;).    In the body of the request, you will inform the new value (&#x60;appFieldValue&#x60;, passed through the body) of the specific field created in this app (identified by the &#x60;appFieldName&#x60; parameter, passed through the URL).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.
     * @param orderFormId The ID of the orderForm whose custom field&#39;s value you want to change. (required)
     * @param appId ID of the app created through the Update orderForm Configuration endpoint. (required)
     * @param appFieldName Name of the app&#39;s field created through the Update orderForm Configuration endpoint. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param setsinglecustomfieldvalueRequest  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void setSingleCustomFieldValue(String orderFormId, String appId, String appFieldName, String contentType, String accept, SetsinglecustomfieldvalueRequest setsinglecustomfieldvalueRequest) throws ApiException {
        setSingleCustomFieldValueWithHttpInfo(orderFormId, appId, appFieldName, contentType, accept, setsinglecustomfieldvalueRequest);
    }

    /**
     * Set single custom field value
     * Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can then be updated by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (&#x60;appId&#x60;).    In the body of the request, you will inform the new value (&#x60;appFieldValue&#x60;, passed through the body) of the specific field created in this app (identified by the &#x60;appFieldName&#x60; parameter, passed through the URL).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.
     * @param orderFormId The ID of the orderForm whose custom field&#39;s value you want to change. (required)
     * @param appId ID of the app created through the Update orderForm Configuration endpoint. (required)
     * @param appFieldName Name of the app&#39;s field created through the Update orderForm Configuration endpoint. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param setsinglecustomfieldvalueRequest  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> setSingleCustomFieldValueWithHttpInfo(String orderFormId, String appId, String appFieldName, String contentType, String accept, SetsinglecustomfieldvalueRequest setsinglecustomfieldvalueRequest) throws ApiException {
        okhttp3.Call localVarCall = setSingleCustomFieldValueValidateBeforeCall(orderFormId, appId, appFieldName, contentType, accept, setsinglecustomfieldvalueRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Set single custom field value (asynchronously)
     * Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can then be updated by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (&#x60;appId&#x60;).    In the body of the request, you will inform the new value (&#x60;appFieldValue&#x60;, passed through the body) of the specific field created in this app (identified by the &#x60;appFieldName&#x60; parameter, passed through the URL).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.
     * @param orderFormId The ID of the orderForm whose custom field&#39;s value you want to change. (required)
     * @param appId ID of the app created through the Update orderForm Configuration endpoint. (required)
     * @param appFieldName Name of the app&#39;s field created through the Update orderForm Configuration endpoint. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param setsinglecustomfieldvalueRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call setSingleCustomFieldValueAsync(String orderFormId, String appId, String appFieldName, String contentType, String accept, SetsinglecustomfieldvalueRequest setsinglecustomfieldvalueRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = setSingleCustomFieldValueValidateBeforeCall(orderFormId, appId, appFieldName, contentType, accept, setsinglecustomfieldvalueRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
