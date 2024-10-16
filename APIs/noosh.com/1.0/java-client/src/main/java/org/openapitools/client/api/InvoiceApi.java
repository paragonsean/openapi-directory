/*
 * Noosh API application
 * Full description of Noosh API
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


import org.openapitools.client.model.FileListResponseVO;
import org.openapitools.client.model.HTTPStatusVO;
import org.openapitools.client.model.InvoiceDetailListExpandVO;
import org.openapitools.client.model.InvoiceExpandVO;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class InvoiceApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public InvoiceApi() {
        this(Configuration.getDefaultApiClient());
    }

    public InvoiceApi(ApiClient apiClient) {
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
     * Build call for getInvoice
     * @param workgroupId  (required)
     * @param projectId  (required)
     * @param invoiceId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful retrieval </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceCall(String workgroupId, String projectId, String invoiceId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/workgroups/{workgroup_id}/projects/{project_id}/invoices/{invoice_id}"
            .replace("{" + "workgroup_id" + "}", localVarApiClient.escapeString(workgroupId.toString()))
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "invoice_id" + "}", localVarApiClient.escapeString(invoiceId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "*/*",
            "application/json",
            "application/x-json-smile",
            "application/x-yaml",
            "application/xml",
            "text/csv",
            "text/x-yaml",
            "text/xml"
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
    private okhttp3.Call getInvoiceValidateBeforeCall(String workgroupId, String projectId, String invoiceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'workgroupId' is set
        if (workgroupId == null) {
            throw new ApiException("Missing the required parameter 'workgroupId' when calling getInvoice(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling getInvoice(Async)");
        }

        // verify the required parameter 'invoiceId' is set
        if (invoiceId == null) {
            throw new ApiException("Missing the required parameter 'invoiceId' when calling getInvoice(Async)");
        }

        return getInvoiceCall(workgroupId, projectId, invoiceId, _callback);

    }

    /**
     * List a specific invoice of project Level
     * List a specific invoice of project Level
     * @param workgroupId  (required)
     * @param projectId  (required)
     * @param invoiceId  (required)
     * @return InvoiceExpandVO
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful retrieval </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public InvoiceExpandVO getInvoice(String workgroupId, String projectId, String invoiceId) throws ApiException {
        ApiResponse<InvoiceExpandVO> localVarResp = getInvoiceWithHttpInfo(workgroupId, projectId, invoiceId);
        return localVarResp.getData();
    }

    /**
     * List a specific invoice of project Level
     * List a specific invoice of project Level
     * @param workgroupId  (required)
     * @param projectId  (required)
     * @param invoiceId  (required)
     * @return ApiResponse&lt;InvoiceExpandVO&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful retrieval </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<InvoiceExpandVO> getInvoiceWithHttpInfo(String workgroupId, String projectId, String invoiceId) throws ApiException {
        okhttp3.Call localVarCall = getInvoiceValidateBeforeCall(workgroupId, projectId, invoiceId, null);
        Type localVarReturnType = new TypeToken<InvoiceExpandVO>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List a specific invoice of project Level (asynchronously)
     * List a specific invoice of project Level
     * @param workgroupId  (required)
     * @param projectId  (required)
     * @param invoiceId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful retrieval </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceAsync(String workgroupId, String projectId, String invoiceId, final ApiCallback<InvoiceExpandVO> _callback) throws ApiException {

        okhttp3.Call localVarCall = getInvoiceValidateBeforeCall(workgroupId, projectId, invoiceId, _callback);
        Type localVarReturnType = new TypeToken<InvoiceExpandVO>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getInvoiceFiles
     * @param workgroupId  (required)
     * @param projectId  (required)
     * @param invoiceId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful retrieval </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceFilesCall(String workgroupId, String projectId, String invoiceId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/workgroups/{workgroup_id}/projects/{project_id}/invoices/{invoice_id}/files"
            .replace("{" + "workgroup_id" + "}", localVarApiClient.escapeString(workgroupId.toString()))
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "invoice_id" + "}", localVarApiClient.escapeString(invoiceId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "*/*",
            "application/json",
            "application/x-json-smile",
            "application/x-yaml",
            "application/xml",
            "text/csv",
            "text/x-yaml",
            "text/xml"
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
    private okhttp3.Call getInvoiceFilesValidateBeforeCall(String workgroupId, String projectId, String invoiceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'workgroupId' is set
        if (workgroupId == null) {
            throw new ApiException("Missing the required parameter 'workgroupId' when calling getInvoiceFiles(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling getInvoiceFiles(Async)");
        }

        // verify the required parameter 'invoiceId' is set
        if (invoiceId == null) {
            throw new ApiException("Missing the required parameter 'invoiceId' when calling getInvoiceFiles(Async)");
        }

        return getInvoiceFilesCall(workgroupId, projectId, invoiceId, _callback);

    }

    /**
     * List files of invoice Level
     * List files of invoice Level
     * @param workgroupId  (required)
     * @param projectId  (required)
     * @param invoiceId  (required)
     * @return FileListResponseVO
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful retrieval </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public FileListResponseVO getInvoiceFiles(String workgroupId, String projectId, String invoiceId) throws ApiException {
        ApiResponse<FileListResponseVO> localVarResp = getInvoiceFilesWithHttpInfo(workgroupId, projectId, invoiceId);
        return localVarResp.getData();
    }

    /**
     * List files of invoice Level
     * List files of invoice Level
     * @param workgroupId  (required)
     * @param projectId  (required)
     * @param invoiceId  (required)
     * @return ApiResponse&lt;FileListResponseVO&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful retrieval </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<FileListResponseVO> getInvoiceFilesWithHttpInfo(String workgroupId, String projectId, String invoiceId) throws ApiException {
        okhttp3.Call localVarCall = getInvoiceFilesValidateBeforeCall(workgroupId, projectId, invoiceId, null);
        Type localVarReturnType = new TypeToken<FileListResponseVO>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List files of invoice Level (asynchronously)
     * List files of invoice Level
     * @param workgroupId  (required)
     * @param projectId  (required)
     * @param invoiceId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful retrieval </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceFilesAsync(String workgroupId, String projectId, String invoiceId, final ApiCallback<FileListResponseVO> _callback) throws ApiException {

        okhttp3.Call localVarCall = getInvoiceFilesValidateBeforeCall(workgroupId, projectId, invoiceId, _callback);
        Type localVarReturnType = new TypeToken<FileListResponseVO>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getInvoices
     * @param workgroupId  (required)
     * @param projectId  (required)
     * @param orderId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful retrieval </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoicesCall(String workgroupId, String projectId, String orderId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/workgroups/{workgroup_id}/projects/{project_id}/invoices/orders/{order_id}"
            .replace("{" + "workgroup_id" + "}", localVarApiClient.escapeString(workgroupId.toString()))
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "order_id" + "}", localVarApiClient.escapeString(orderId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "*/*",
            "application/json",
            "application/x-json-smile",
            "application/x-yaml",
            "application/xml",
            "text/csv",
            "text/x-yaml",
            "text/xml"
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
    private okhttp3.Call getInvoicesValidateBeforeCall(String workgroupId, String projectId, String orderId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'workgroupId' is set
        if (workgroupId == null) {
            throw new ApiException("Missing the required parameter 'workgroupId' when calling getInvoices(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling getInvoices(Async)");
        }

        // verify the required parameter 'orderId' is set
        if (orderId == null) {
            throw new ApiException("Missing the required parameter 'orderId' when calling getInvoices(Async)");
        }

        return getInvoicesCall(workgroupId, projectId, orderId, _callback);

    }

    /**
     * List invoices by a specific order
     * List invoices by a specific order
     * @param workgroupId  (required)
     * @param projectId  (required)
     * @param orderId  (required)
     * @return InvoiceDetailListExpandVO
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful retrieval </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public InvoiceDetailListExpandVO getInvoices(String workgroupId, String projectId, String orderId) throws ApiException {
        ApiResponse<InvoiceDetailListExpandVO> localVarResp = getInvoicesWithHttpInfo(workgroupId, projectId, orderId);
        return localVarResp.getData();
    }

    /**
     * List invoices by a specific order
     * List invoices by a specific order
     * @param workgroupId  (required)
     * @param projectId  (required)
     * @param orderId  (required)
     * @return ApiResponse&lt;InvoiceDetailListExpandVO&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful retrieval </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<InvoiceDetailListExpandVO> getInvoicesWithHttpInfo(String workgroupId, String projectId, String orderId) throws ApiException {
        okhttp3.Call localVarCall = getInvoicesValidateBeforeCall(workgroupId, projectId, orderId, null);
        Type localVarReturnType = new TypeToken<InvoiceDetailListExpandVO>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List invoices by a specific order (asynchronously)
     * List invoices by a specific order
     * @param workgroupId  (required)
     * @param projectId  (required)
     * @param orderId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful retrieval </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoicesAsync(String workgroupId, String projectId, String orderId, final ApiCallback<InvoiceDetailListExpandVO> _callback) throws ApiException {

        okhttp3.Call localVarCall = getInvoicesValidateBeforeCall(workgroupId, projectId, orderId, _callback);
        Type localVarReturnType = new TypeToken<InvoiceDetailListExpandVO>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
