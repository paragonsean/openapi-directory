/*
 * AWS Health Imaging
 * <p>This is the <i>AWS HealthImaging API Reference</i>. AWS HealthImaging is an AWS service for storing, accessing, and analyzing medical images. For an introduction to the service, see the <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide\"> <i>AWS HealthImaging Developer Guide</i> </a>.</p> <note> <p>We recommend using one of the AWS Software Development Kits (SDKs) for your programming language, as they take care of request authentication, serialization, and connection management. For more information, see <a href=\"http://aws.amazon.com/developer/tools\">Tools to build on AWS</a>.</p> <p>For information about using AWS HealthImaging API actions in one of the language-specific AWS SDKs, refer to the <i>See Also</i> link at the end of each section that describes an API action or data type.</p> </note> <p>The following sections list AWS HealthImaging API actions categorized according to functionality. Links are provided to actions within this Reference, along with links back to corresponding sections in the <i>AWS HealthImaging Developer Guide</i> so you can view console procedures and CLI/SDK code examples.</p> <p class=\"title\"> <b>Data store actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CreateDatastore.html\">CreateDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/create-data-store.html\">Creating a data store</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDatastore.html\">GetDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-data-store.html\">Getting data store properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDatastores.html\">ListDatastores</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-data-stores.html\">Listing data stores</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteDatastore.html\">DeleteDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-data-store.html\">Deleting a data store</a>.</p> </li> </ul> <p class=\"title\"> <b>Import job actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_StartDICOMImportJob.html\">StartDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/start-dicom-import-job.html\">Starting an import job</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDICOMImportJob.html\">GetDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-dicom-import-job.html\">Getting import job properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDICOMImportJobs.html\">ListDICOMImportJobs</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-dicom-import-jobs.html\">Listing import jobs</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set access actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_SearchImageSets.html\">SearchImageSets</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/search-image-sets.html\">Searching image sets</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSet.html\">GetImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-properties.html\">Getting image set properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSetMetadata.html\">GetImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-metadata.html\">Getting image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageFrame.html\">GetImageFrame</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-frame.html\">Getting image set pixel data</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set modification actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListImageSetVersions.html\">ListImageSetVersions</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-image-set-versions.html\">Listing image set versions</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UpdateImageSetMetadata.html\">UpdateImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/update-image-set-metadata.html\">Updating image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CopyImageSet.html\">CopyImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/copy-image-set.html\">Copying an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteImageSet.html\">DeleteImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-image-set.html\">Deleting an image set</a>.</p> </li> </ul> <p class=\"title\"> <b>Tagging actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_TagResource.html\">TagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListTagsForResource.html\">ListTagsForResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UntagResource.html\">UntagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2023-07-19
 * Contact: mike.ralphson@gmail.com
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


import org.openapitools.client.model.CopyImageSetRequest;
import org.openapitools.client.model.CopyImageSetResponse;
import org.openapitools.client.model.CreateDatastoreRequest;
import org.openapitools.client.model.CreateDatastoreResponse;
import org.openapitools.client.model.DeleteDatastoreResponse;
import org.openapitools.client.model.DeleteImageSetResponse;
import org.openapitools.client.model.GetDICOMImportJobResponse;
import org.openapitools.client.model.GetDatastoreResponse;
import org.openapitools.client.model.GetImageFrameRequest;
import org.openapitools.client.model.GetImageFrameResponse;
import org.openapitools.client.model.GetImageSetMetadataResponse;
import org.openapitools.client.model.GetImageSetResponse;
import org.openapitools.client.model.ListDICOMImportJobsResponse;
import org.openapitools.client.model.ListDatastoresResponse;
import org.openapitools.client.model.ListImageSetVersionsResponse;
import org.openapitools.client.model.ListTagsForResourceResponse;
import org.openapitools.client.model.SearchImageSetsRequest;
import org.openapitools.client.model.SearchImageSetsResponse;
import org.openapitools.client.model.StartDICOMImportJobRequest;
import org.openapitools.client.model.StartDICOMImportJobResponse;
import org.openapitools.client.model.TagResourceRequest;
import org.openapitools.client.model.UpdateImageSetMetadataRequest;
import org.openapitools.client.model.UpdateImageSetMetadataResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DefaultApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DefaultApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DefaultApi(ApiClient apiClient) {
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
     * Build call for copyImageSet
     * @param datastoreId The data store identifier. (required)
     * @param sourceImageSetId The source image set identifier. (required)
     * @param copyImageSetRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call copyImageSetCall(String datastoreId, String sourceImageSetId, CopyImageSetRequest copyImageSetRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = copyImageSetRequest;

        // create path and map variables
        String localVarPath = "/datastore/{datastoreId}/imageSet/{sourceImageSetId}/copyImageSet"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()))
            .replace("{" + "sourceImageSetId" + "}", localVarApiClient.escapeString(sourceImageSetId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call copyImageSetValidateBeforeCall(String datastoreId, String sourceImageSetId, CopyImageSetRequest copyImageSetRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling copyImageSet(Async)");
        }

        // verify the required parameter 'sourceImageSetId' is set
        if (sourceImageSetId == null) {
            throw new ApiException("Missing the required parameter 'sourceImageSetId' when calling copyImageSet(Async)");
        }

        // verify the required parameter 'copyImageSetRequest' is set
        if (copyImageSetRequest == null) {
            throw new ApiException("Missing the required parameter 'copyImageSetRequest' when calling copyImageSet(Async)");
        }

        return copyImageSetCall(datastoreId, sourceImageSetId, copyImageSetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Copy an image set.
     * @param datastoreId The data store identifier. (required)
     * @param sourceImageSetId The source image set identifier. (required)
     * @param copyImageSetRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return CopyImageSetResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public CopyImageSetResponse copyImageSet(String datastoreId, String sourceImageSetId, CopyImageSetRequest copyImageSetRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<CopyImageSetResponse> localVarResp = copyImageSetWithHttpInfo(datastoreId, sourceImageSetId, copyImageSetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Copy an image set.
     * @param datastoreId The data store identifier. (required)
     * @param sourceImageSetId The source image set identifier. (required)
     * @param copyImageSetRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;CopyImageSetResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CopyImageSetResponse> copyImageSetWithHttpInfo(String datastoreId, String sourceImageSetId, CopyImageSetRequest copyImageSetRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = copyImageSetValidateBeforeCall(datastoreId, sourceImageSetId, copyImageSetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<CopyImageSetResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Copy an image set.
     * @param datastoreId The data store identifier. (required)
     * @param sourceImageSetId The source image set identifier. (required)
     * @param copyImageSetRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call copyImageSetAsync(String datastoreId, String sourceImageSetId, CopyImageSetRequest copyImageSetRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<CopyImageSetResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = copyImageSetValidateBeforeCall(datastoreId, sourceImageSetId, copyImageSetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<CopyImageSetResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createDatastore
     * @param createDatastoreRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createDatastoreCall(CreateDatastoreRequest createDatastoreRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createDatastoreRequest;

        // create path and map variables
        String localVarPath = "/datastore";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createDatastoreValidateBeforeCall(CreateDatastoreRequest createDatastoreRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'createDatastoreRequest' is set
        if (createDatastoreRequest == null) {
            throw new ApiException("Missing the required parameter 'createDatastoreRequest' when calling createDatastore(Async)");
        }

        return createDatastoreCall(createDatastoreRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Create a data store.
     * @param createDatastoreRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return CreateDatastoreResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public CreateDatastoreResponse createDatastore(CreateDatastoreRequest createDatastoreRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<CreateDatastoreResponse> localVarResp = createDatastoreWithHttpInfo(createDatastoreRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Create a data store.
     * @param createDatastoreRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;CreateDatastoreResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateDatastoreResponse> createDatastoreWithHttpInfo(CreateDatastoreRequest createDatastoreRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = createDatastoreValidateBeforeCall(createDatastoreRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<CreateDatastoreResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Create a data store.
     * @param createDatastoreRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createDatastoreAsync(CreateDatastoreRequest createDatastoreRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<CreateDatastoreResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = createDatastoreValidateBeforeCall(createDatastoreRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<CreateDatastoreResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDatastore
     * @param datastoreId The data store identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatastoreCall(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/datastore/{datastoreId}"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteDatastoreValidateBeforeCall(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling deleteDatastore(Async)");
        }

        return deleteDatastoreCall(datastoreId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Delete a data store.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before a data store can be deleted, you must first delete all image sets within it.&lt;/p&gt; &lt;/note&gt;
     * @param datastoreId The data store identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return DeleteDatastoreResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public DeleteDatastoreResponse deleteDatastore(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<DeleteDatastoreResponse> localVarResp = deleteDatastoreWithHttpInfo(datastoreId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Delete a data store.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before a data store can be deleted, you must first delete all image sets within it.&lt;/p&gt; &lt;/note&gt;
     * @param datastoreId The data store identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;DeleteDatastoreResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteDatastoreResponse> deleteDatastoreWithHttpInfo(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deleteDatastoreValidateBeforeCall(datastoreId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<DeleteDatastoreResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Delete a data store.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before a data store can be deleted, you must first delete all image sets within it.&lt;/p&gt; &lt;/note&gt;
     * @param datastoreId The data store identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatastoreAsync(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<DeleteDatastoreResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDatastoreValidateBeforeCall(datastoreId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<DeleteDatastoreResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteImageSet
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteImageSetCall(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/datastore/{datastoreId}/imageSet/{imageSetId}/deleteImageSet"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()))
            .replace("{" + "imageSetId" + "}", localVarApiClient.escapeString(imageSetId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteImageSetValidateBeforeCall(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling deleteImageSet(Async)");
        }

        // verify the required parameter 'imageSetId' is set
        if (imageSetId == null) {
            throw new ApiException("Missing the required parameter 'imageSetId' when calling deleteImageSet(Async)");
        }

        return deleteImageSetCall(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Delete an image set.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return DeleteImageSetResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public DeleteImageSetResponse deleteImageSet(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<DeleteImageSetResponse> localVarResp = deleteImageSetWithHttpInfo(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Delete an image set.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;DeleteImageSetResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteImageSetResponse> deleteImageSetWithHttpInfo(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deleteImageSetValidateBeforeCall(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<DeleteImageSetResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Delete an image set.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteImageSetAsync(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<DeleteImageSetResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteImageSetValidateBeforeCall(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<DeleteImageSetResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDICOMImportJob
     * @param datastoreId The data store identifier. (required)
     * @param jobId The import job identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDICOMImportJobCall(String datastoreId, String jobId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/getDICOMImportJob/datastore/{datastoreId}/job/{jobId}"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()))
            .replace("{" + "jobId" + "}", localVarApiClient.escapeString(jobId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getDICOMImportJobValidateBeforeCall(String datastoreId, String jobId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling getDICOMImportJob(Async)");
        }

        // verify the required parameter 'jobId' is set
        if (jobId == null) {
            throw new ApiException("Missing the required parameter 'jobId' when calling getDICOMImportJob(Async)");
        }

        return getDICOMImportJobCall(datastoreId, jobId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Get the import job properties to learn more about the job or job progress.
     * @param datastoreId The data store identifier. (required)
     * @param jobId The import job identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetDICOMImportJobResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public GetDICOMImportJobResponse getDICOMImportJob(String datastoreId, String jobId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetDICOMImportJobResponse> localVarResp = getDICOMImportJobWithHttpInfo(datastoreId, jobId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Get the import job properties to learn more about the job or job progress.
     * @param datastoreId The data store identifier. (required)
     * @param jobId The import job identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetDICOMImportJobResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDICOMImportJobResponse> getDICOMImportJobWithHttpInfo(String datastoreId, String jobId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getDICOMImportJobValidateBeforeCall(datastoreId, jobId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetDICOMImportJobResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Get the import job properties to learn more about the job or job progress.
     * @param datastoreId The data store identifier. (required)
     * @param jobId The import job identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDICOMImportJobAsync(String datastoreId, String jobId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetDICOMImportJobResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDICOMImportJobValidateBeforeCall(datastoreId, jobId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetDICOMImportJobResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatastore
     * @param datastoreId The data store identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatastoreCall(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/datastore/{datastoreId}"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getDatastoreValidateBeforeCall(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling getDatastore(Async)");
        }

        return getDatastoreCall(datastoreId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Get data store properties.
     * @param datastoreId The data store identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetDatastoreResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public GetDatastoreResponse getDatastore(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetDatastoreResponse> localVarResp = getDatastoreWithHttpInfo(datastoreId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Get data store properties.
     * @param datastoreId The data store identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetDatastoreResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDatastoreResponse> getDatastoreWithHttpInfo(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getDatastoreValidateBeforeCall(datastoreId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetDatastoreResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Get data store properties.
     * @param datastoreId The data store identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatastoreAsync(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetDatastoreResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatastoreValidateBeforeCall(datastoreId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetDatastoreResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getImageFrame
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param getImageFrameRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getImageFrameCall(String datastoreId, String imageSetId, GetImageFrameRequest getImageFrameRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = getImageFrameRequest;

        // create path and map variables
        String localVarPath = "/datastore/{datastoreId}/imageSet/{imageSetId}/getImageFrame"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()))
            .replace("{" + "imageSetId" + "}", localVarApiClient.escapeString(imageSetId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getImageFrameValidateBeforeCall(String datastoreId, String imageSetId, GetImageFrameRequest getImageFrameRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling getImageFrame(Async)");
        }

        // verify the required parameter 'imageSetId' is set
        if (imageSetId == null) {
            throw new ApiException("Missing the required parameter 'imageSetId' when calling getImageFrame(Async)");
        }

        // verify the required parameter 'getImageFrameRequest' is set
        if (getImageFrameRequest == null) {
            throw new ApiException("Missing the required parameter 'getImageFrameRequest' when calling getImageFrame(Async)");
        }

        return getImageFrameCall(datastoreId, imageSetId, getImageFrameRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Get an image frame (pixel data) for an image set.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param getImageFrameRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetImageFrameResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public GetImageFrameResponse getImageFrame(String datastoreId, String imageSetId, GetImageFrameRequest getImageFrameRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetImageFrameResponse> localVarResp = getImageFrameWithHttpInfo(datastoreId, imageSetId, getImageFrameRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Get an image frame (pixel data) for an image set.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param getImageFrameRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetImageFrameResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetImageFrameResponse> getImageFrameWithHttpInfo(String datastoreId, String imageSetId, GetImageFrameRequest getImageFrameRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getImageFrameValidateBeforeCall(datastoreId, imageSetId, getImageFrameRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetImageFrameResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Get an image frame (pixel data) for an image set.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param getImageFrameRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getImageFrameAsync(String datastoreId, String imageSetId, GetImageFrameRequest getImageFrameRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetImageFrameResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getImageFrameValidateBeforeCall(datastoreId, imageSetId, getImageFrameRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetImageFrameResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getImageSet
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param version The image set version identifier. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getImageSetCall(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String version, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/datastore/{datastoreId}/imageSet/{imageSetId}/getImageSet"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()))
            .replace("{" + "imageSetId" + "}", localVarApiClient.escapeString(imageSetId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (version != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("version", version));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getImageSetValidateBeforeCall(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String version, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling getImageSet(Async)");
        }

        // verify the required parameter 'imageSetId' is set
        if (imageSetId == null) {
            throw new ApiException("Missing the required parameter 'imageSetId' when calling getImageSet(Async)");
        }

        return getImageSetCall(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, version, _callback);

    }

    /**
     * 
     * Get image set properties.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param version The image set version identifier. (optional)
     * @return GetImageSetResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public GetImageSetResponse getImageSet(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String version) throws ApiException {
        ApiResponse<GetImageSetResponse> localVarResp = getImageSetWithHttpInfo(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, version);
        return localVarResp.getData();
    }

    /**
     * 
     * Get image set properties.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param version The image set version identifier. (optional)
     * @return ApiResponse&lt;GetImageSetResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetImageSetResponse> getImageSetWithHttpInfo(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String version) throws ApiException {
        okhttp3.Call localVarCall = getImageSetValidateBeforeCall(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, version, null);
        Type localVarReturnType = new TypeToken<GetImageSetResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Get image set properties.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param version The image set version identifier. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getImageSetAsync(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String version, final ApiCallback<GetImageSetResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getImageSetValidateBeforeCall(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, version, _callback);
        Type localVarReturnType = new TypeToken<GetImageSetResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getImageSetMetadata
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param version The image set version identifier. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getImageSetMetadataCall(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String version, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/datastore/{datastoreId}/imageSet/{imageSetId}/getImageSetMetadata"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()))
            .replace("{" + "imageSetId" + "}", localVarApiClient.escapeString(imageSetId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (version != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("version", version));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getImageSetMetadataValidateBeforeCall(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String version, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling getImageSetMetadata(Async)");
        }

        // verify the required parameter 'imageSetId' is set
        if (imageSetId == null) {
            throw new ApiException("Missing the required parameter 'imageSetId' when calling getImageSetMetadata(Async)");
        }

        return getImageSetMetadataCall(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, version, _callback);

    }

    /**
     * 
     * Get metadata attributes for an image set.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param version The image set version identifier. (optional)
     * @return GetImageSetMetadataResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public GetImageSetMetadataResponse getImageSetMetadata(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String version) throws ApiException {
        ApiResponse<GetImageSetMetadataResponse> localVarResp = getImageSetMetadataWithHttpInfo(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, version);
        return localVarResp.getData();
    }

    /**
     * 
     * Get metadata attributes for an image set.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param version The image set version identifier. (optional)
     * @return ApiResponse&lt;GetImageSetMetadataResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetImageSetMetadataResponse> getImageSetMetadataWithHttpInfo(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String version) throws ApiException {
        okhttp3.Call localVarCall = getImageSetMetadataValidateBeforeCall(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, version, null);
        Type localVarReturnType = new TypeToken<GetImageSetMetadataResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Get metadata attributes for an image set.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param version The image set version identifier. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getImageSetMetadataAsync(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String version, final ApiCallback<GetImageSetMetadataResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getImageSetMetadataValidateBeforeCall(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, version, _callback);
        Type localVarReturnType = new TypeToken<GetImageSetMetadataResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listDICOMImportJobs
     * @param datastoreId The data store identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param jobStatus The filters for listing import jobs based on status. (optional)
     * @param nextToken The pagination token used to request the list of import jobs on the next page. (optional)
     * @param maxResults The max results count. The upper bound is determined by load testing. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listDICOMImportJobsCall(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String jobStatus, String nextToken, Integer maxResults, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/listDICOMImportJobs/datastore/{datastoreId}"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (jobStatus != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("jobStatus", jobStatus));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listDICOMImportJobsValidateBeforeCall(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String jobStatus, String nextToken, Integer maxResults, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling listDICOMImportJobs(Async)");
        }

        return listDICOMImportJobsCall(datastoreId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, jobStatus, nextToken, maxResults, _callback);

    }

    /**
     * 
     * List import jobs created by this AWS account for a specific data store.
     * @param datastoreId The data store identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param jobStatus The filters for listing import jobs based on status. (optional)
     * @param nextToken The pagination token used to request the list of import jobs on the next page. (optional)
     * @param maxResults The max results count. The upper bound is determined by load testing. (optional)
     * @return ListDICOMImportJobsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ListDICOMImportJobsResponse listDICOMImportJobs(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String jobStatus, String nextToken, Integer maxResults) throws ApiException {
        ApiResponse<ListDICOMImportJobsResponse> localVarResp = listDICOMImportJobsWithHttpInfo(datastoreId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, jobStatus, nextToken, maxResults);
        return localVarResp.getData();
    }

    /**
     * 
     * List import jobs created by this AWS account for a specific data store.
     * @param datastoreId The data store identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param jobStatus The filters for listing import jobs based on status. (optional)
     * @param nextToken The pagination token used to request the list of import jobs on the next page. (optional)
     * @param maxResults The max results count. The upper bound is determined by load testing. (optional)
     * @return ApiResponse&lt;ListDICOMImportJobsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListDICOMImportJobsResponse> listDICOMImportJobsWithHttpInfo(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String jobStatus, String nextToken, Integer maxResults) throws ApiException {
        okhttp3.Call localVarCall = listDICOMImportJobsValidateBeforeCall(datastoreId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, jobStatus, nextToken, maxResults, null);
        Type localVarReturnType = new TypeToken<ListDICOMImportJobsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * List import jobs created by this AWS account for a specific data store.
     * @param datastoreId The data store identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param jobStatus The filters for listing import jobs based on status. (optional)
     * @param nextToken The pagination token used to request the list of import jobs on the next page. (optional)
     * @param maxResults The max results count. The upper bound is determined by load testing. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listDICOMImportJobsAsync(String datastoreId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String jobStatus, String nextToken, Integer maxResults, final ApiCallback<ListDICOMImportJobsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listDICOMImportJobsValidateBeforeCall(datastoreId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, jobStatus, nextToken, maxResults, _callback);
        Type localVarReturnType = new TypeToken<ListDICOMImportJobsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listDatastores
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param datastoreStatus The data store status. (optional)
     * @param nextToken The pagination token used to request the list of data stores on the next page. (optional)
     * @param maxResults Valid Range: Minimum value of 1. Maximum value of 50. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listDatastoresCall(String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String datastoreStatus, String nextToken, Integer maxResults, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/datastore";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (datastoreStatus != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("datastoreStatus", datastoreStatus));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listDatastoresValidateBeforeCall(String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String datastoreStatus, String nextToken, Integer maxResults, final ApiCallback _callback) throws ApiException {
        return listDatastoresCall(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, datastoreStatus, nextToken, maxResults, _callback);

    }

    /**
     * 
     * List data stores created by this AWS account.
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param datastoreStatus The data store status. (optional)
     * @param nextToken The pagination token used to request the list of data stores on the next page. (optional)
     * @param maxResults Valid Range: Minimum value of 1. Maximum value of 50. (optional)
     * @return ListDatastoresResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
     </table>
     */
    public ListDatastoresResponse listDatastores(String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String datastoreStatus, String nextToken, Integer maxResults) throws ApiException {
        ApiResponse<ListDatastoresResponse> localVarResp = listDatastoresWithHttpInfo(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, datastoreStatus, nextToken, maxResults);
        return localVarResp.getData();
    }

    /**
     * 
     * List data stores created by this AWS account.
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param datastoreStatus The data store status. (optional)
     * @param nextToken The pagination token used to request the list of data stores on the next page. (optional)
     * @param maxResults Valid Range: Minimum value of 1. Maximum value of 50. (optional)
     * @return ApiResponse&lt;ListDatastoresResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListDatastoresResponse> listDatastoresWithHttpInfo(String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String datastoreStatus, String nextToken, Integer maxResults) throws ApiException {
        okhttp3.Call localVarCall = listDatastoresValidateBeforeCall(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, datastoreStatus, nextToken, maxResults, null);
        Type localVarReturnType = new TypeToken<ListDatastoresResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * List data stores created by this AWS account.
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param datastoreStatus The data store status. (optional)
     * @param nextToken The pagination token used to request the list of data stores on the next page. (optional)
     * @param maxResults Valid Range: Minimum value of 1. Maximum value of 50. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listDatastoresAsync(String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String datastoreStatus, String nextToken, Integer maxResults, final ApiCallback<ListDatastoresResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listDatastoresValidateBeforeCall(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, datastoreStatus, nextToken, maxResults, _callback);
        Type localVarReturnType = new TypeToken<ListDatastoresResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listImageSetVersions
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param nextToken The pagination token used to request the list of image set versions on the next page. (optional)
     * @param maxResults The max results count. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listImageSetVersionsCall(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String nextToken, Integer maxResults, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/datastore/{datastoreId}/imageSet/{imageSetId}/listImageSetVersions"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()))
            .replace("{" + "imageSetId" + "}", localVarApiClient.escapeString(imageSetId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listImageSetVersionsValidateBeforeCall(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String nextToken, Integer maxResults, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling listImageSetVersions(Async)");
        }

        // verify the required parameter 'imageSetId' is set
        if (imageSetId == null) {
            throw new ApiException("Missing the required parameter 'imageSetId' when calling listImageSetVersions(Async)");
        }

        return listImageSetVersionsCall(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, _callback);

    }

    /**
     * 
     * List image set versions.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param nextToken The pagination token used to request the list of image set versions on the next page. (optional)
     * @param maxResults The max results count. (optional)
     * @return ListImageSetVersionsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ListImageSetVersionsResponse listImageSetVersions(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String nextToken, Integer maxResults) throws ApiException {
        ApiResponse<ListImageSetVersionsResponse> localVarResp = listImageSetVersionsWithHttpInfo(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
        return localVarResp.getData();
    }

    /**
     * 
     * List image set versions.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param nextToken The pagination token used to request the list of image set versions on the next page. (optional)
     * @param maxResults The max results count. (optional)
     * @return ApiResponse&lt;ListImageSetVersionsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListImageSetVersionsResponse> listImageSetVersionsWithHttpInfo(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String nextToken, Integer maxResults) throws ApiException {
        okhttp3.Call localVarCall = listImageSetVersionsValidateBeforeCall(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, null);
        Type localVarReturnType = new TypeToken<ListImageSetVersionsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * List image set versions.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param nextToken The pagination token used to request the list of image set versions on the next page. (optional)
     * @param maxResults The max results count. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listImageSetVersionsAsync(String datastoreId, String imageSetId, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String nextToken, Integer maxResults, final ApiCallback<ListImageSetVersionsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listImageSetVersionsValidateBeforeCall(datastoreId, imageSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, _callback);
        Type localVarReturnType = new TypeToken<ListImageSetVersionsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listTagsForResource
     * @param resourceArn The Amazon Resource Name (ARN) of the medical imaging resource to list tags for. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTagsForResourceCall(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/tags/{resourceArn}"
            .replace("{" + "resourceArn" + "}", localVarApiClient.escapeString(resourceArn.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listTagsForResourceValidateBeforeCall(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'resourceArn' is set
        if (resourceArn == null) {
            throw new ApiException("Missing the required parameter 'resourceArn' when calling listTagsForResource(Async)");
        }

        return listTagsForResourceCall(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Lists all tags associated with a medical imaging resource.
     * @param resourceArn The Amazon Resource Name (ARN) of the medical imaging resource to list tags for. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ListTagsForResourceResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ListTagsForResourceResponse listTagsForResource(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<ListTagsForResourceResponse> localVarResp = listTagsForResourceWithHttpInfo(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Lists all tags associated with a medical imaging resource.
     * @param resourceArn The Amazon Resource Name (ARN) of the medical imaging resource to list tags for. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;ListTagsForResourceResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListTagsForResourceResponse> listTagsForResourceWithHttpInfo(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = listTagsForResourceValidateBeforeCall(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<ListTagsForResourceResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Lists all tags associated with a medical imaging resource.
     * @param resourceArn The Amazon Resource Name (ARN) of the medical imaging resource to list tags for. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTagsForResourceAsync(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<ListTagsForResourceResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listTagsForResourceValidateBeforeCall(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<ListTagsForResourceResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for searchImageSets
     * @param datastoreId The identifier of the data store where the image sets reside. (required)
     * @param searchImageSetsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults The maximum number of results that can be returned in a search. (optional)
     * @param nextToken The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call searchImageSetsCall(String datastoreId, SearchImageSetsRequest searchImageSetsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, Integer maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = searchImageSetsRequest;

        // create path and map variables
        String localVarPath = "/datastore/{datastoreId}/searchImageSets"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call searchImageSetsValidateBeforeCall(String datastoreId, SearchImageSetsRequest searchImageSetsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, Integer maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling searchImageSets(Async)");
        }

        // verify the required parameter 'searchImageSetsRequest' is set
        if (searchImageSetsRequest == null) {
            throw new ApiException("Missing the required parameter 'searchImageSetsRequest' when calling searchImageSets(Async)");
        }

        return searchImageSetsCall(datastoreId, searchImageSetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Search image sets based on defined input attributes.
     * @param datastoreId The identifier of the data store where the image sets reside. (required)
     * @param searchImageSetsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults The maximum number of results that can be returned in a search. (optional)
     * @param nextToken The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended. (optional)
     * @return SearchImageSetsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public SearchImageSetsResponse searchImageSets(String datastoreId, SearchImageSetsRequest searchImageSetsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, Integer maxResults, String nextToken) throws ApiException {
        ApiResponse<SearchImageSetsResponse> localVarResp = searchImageSetsWithHttpInfo(datastoreId, searchImageSetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Search image sets based on defined input attributes.
     * @param datastoreId The identifier of the data store where the image sets reside. (required)
     * @param searchImageSetsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults The maximum number of results that can be returned in a search. (optional)
     * @param nextToken The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended. (optional)
     * @return ApiResponse&lt;SearchImageSetsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SearchImageSetsResponse> searchImageSetsWithHttpInfo(String datastoreId, SearchImageSetsRequest searchImageSetsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, Integer maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = searchImageSetsValidateBeforeCall(datastoreId, searchImageSetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<SearchImageSetsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Search image sets based on defined input attributes.
     * @param datastoreId The identifier of the data store where the image sets reside. (required)
     * @param searchImageSetsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults The maximum number of results that can be returned in a search. (optional)
     * @param nextToken The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call searchImageSetsAsync(String datastoreId, SearchImageSetsRequest searchImageSetsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, Integer maxResults, String nextToken, final ApiCallback<SearchImageSetsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = searchImageSetsValidateBeforeCall(datastoreId, searchImageSetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<SearchImageSetsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for startDICOMImportJob
     * @param datastoreId The data store identifier. (required)
     * @param startDICOMImportJobRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call startDICOMImportJobCall(String datastoreId, StartDICOMImportJobRequest startDICOMImportJobRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = startDICOMImportJobRequest;

        // create path and map variables
        String localVarPath = "/startDICOMImportJob/datastore/{datastoreId}"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call startDICOMImportJobValidateBeforeCall(String datastoreId, StartDICOMImportJobRequest startDICOMImportJobRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling startDICOMImportJob(Async)");
        }

        // verify the required parameter 'startDICOMImportJobRequest' is set
        if (startDICOMImportJobRequest == null) {
            throw new ApiException("Missing the required parameter 'startDICOMImportJobRequest' when calling startDICOMImportJob(Async)");
        }

        return startDICOMImportJobCall(datastoreId, startDICOMImportJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Start importing bulk data into an &lt;code&gt;ACTIVE&lt;/code&gt; data store. The import job imports DICOM P10 files found in the S3 prefix specified by the &lt;code&gt;inputS3Uri&lt;/code&gt; parameter. The import job stores processing results in the file specified by the &lt;code&gt;outputS3Uri&lt;/code&gt; parameter.
     * @param datastoreId The data store identifier. (required)
     * @param startDICOMImportJobRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return StartDICOMImportJobResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public StartDICOMImportJobResponse startDICOMImportJob(String datastoreId, StartDICOMImportJobRequest startDICOMImportJobRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<StartDICOMImportJobResponse> localVarResp = startDICOMImportJobWithHttpInfo(datastoreId, startDICOMImportJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Start importing bulk data into an &lt;code&gt;ACTIVE&lt;/code&gt; data store. The import job imports DICOM P10 files found in the S3 prefix specified by the &lt;code&gt;inputS3Uri&lt;/code&gt; parameter. The import job stores processing results in the file specified by the &lt;code&gt;outputS3Uri&lt;/code&gt; parameter.
     * @param datastoreId The data store identifier. (required)
     * @param startDICOMImportJobRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;StartDICOMImportJobResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<StartDICOMImportJobResponse> startDICOMImportJobWithHttpInfo(String datastoreId, StartDICOMImportJobRequest startDICOMImportJobRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = startDICOMImportJobValidateBeforeCall(datastoreId, startDICOMImportJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<StartDICOMImportJobResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Start importing bulk data into an &lt;code&gt;ACTIVE&lt;/code&gt; data store. The import job imports DICOM P10 files found in the S3 prefix specified by the &lt;code&gt;inputS3Uri&lt;/code&gt; parameter. The import job stores processing results in the file specified by the &lt;code&gt;outputS3Uri&lt;/code&gt; parameter.
     * @param datastoreId The data store identifier. (required)
     * @param startDICOMImportJobRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call startDICOMImportJobAsync(String datastoreId, StartDICOMImportJobRequest startDICOMImportJobRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<StartDICOMImportJobResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = startDICOMImportJobValidateBeforeCall(datastoreId, startDICOMImportJobRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<StartDICOMImportJobResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for tagResource
     * @param resourceArn The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to. (required)
     * @param tagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call tagResourceCall(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = tagResourceRequest;

        // create path and map variables
        String localVarPath = "/tags/{resourceArn}"
            .replace("{" + "resourceArn" + "}", localVarApiClient.escapeString(resourceArn.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call tagResourceValidateBeforeCall(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'resourceArn' is set
        if (resourceArn == null) {
            throw new ApiException("Missing the required parameter 'resourceArn' when calling tagResource(Async)");
        }

        // verify the required parameter 'tagResourceRequest' is set
        if (tagResourceRequest == null) {
            throw new ApiException("Missing the required parameter 'tagResourceRequest' when calling tagResource(Async)");
        }

        return tagResourceCall(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Adds a user-specifed key and value tag to a medical imaging resource.
     * @param resourceArn The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to. (required)
     * @param tagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public Object tagResource(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = tagResourceWithHttpInfo(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Adds a user-specifed key and value tag to a medical imaging resource.
     * @param resourceArn The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to. (required)
     * @param tagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> tagResourceWithHttpInfo(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = tagResourceValidateBeforeCall(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Adds a user-specifed key and value tag to a medical imaging resource.
     * @param resourceArn The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to. (required)
     * @param tagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call tagResourceAsync(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = tagResourceValidateBeforeCall(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for untagResource
     * @param resourceArn The Amazon Resource Name (ARN) of the medical imaging resource that tags are being removed from. (required)
     * @param tagKeys The keys for the tags to be removed from the medical imaging resource. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call untagResourceCall(String resourceArn, List<String> tagKeys, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/tags/{resourceArn}#tagKeys"
            .replace("{" + "resourceArn" + "}", localVarApiClient.escapeString(resourceArn.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (tagKeys != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "tagKeys", tagKeys));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call untagResourceValidateBeforeCall(String resourceArn, List<String> tagKeys, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'resourceArn' is set
        if (resourceArn == null) {
            throw new ApiException("Missing the required parameter 'resourceArn' when calling untagResource(Async)");
        }

        // verify the required parameter 'tagKeys' is set
        if (tagKeys == null) {
            throw new ApiException("Missing the required parameter 'tagKeys' when calling untagResource(Async)");
        }

        return untagResourceCall(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Removes tags from a medical imaging resource.
     * @param resourceArn The Amazon Resource Name (ARN) of the medical imaging resource that tags are being removed from. (required)
     * @param tagKeys The keys for the tags to be removed from the medical imaging resource. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public Object untagResource(String resourceArn, List<String> tagKeys, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = untagResourceWithHttpInfo(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Removes tags from a medical imaging resource.
     * @param resourceArn The Amazon Resource Name (ARN) of the medical imaging resource that tags are being removed from. (required)
     * @param tagKeys The keys for the tags to be removed from the medical imaging resource. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> untagResourceWithHttpInfo(String resourceArn, List<String> tagKeys, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = untagResourceValidateBeforeCall(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Removes tags from a medical imaging resource.
     * @param resourceArn The Amazon Resource Name (ARN) of the medical imaging resource that tags are being removed from. (required)
     * @param tagKeys The keys for the tags to be removed from the medical imaging resource. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call untagResourceAsync(String resourceArn, List<String> tagKeys, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = untagResourceValidateBeforeCall(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateImageSetMetadata
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param latestVersion The latest image set version identifier. (required)
     * @param updateImageSetMetadataRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateImageSetMetadataCall(String datastoreId, String imageSetId, String latestVersion, UpdateImageSetMetadataRequest updateImageSetMetadataRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateImageSetMetadataRequest;

        // create path and map variables
        String localVarPath = "/datastore/{datastoreId}/imageSet/{imageSetId}/updateImageSetMetadata#latestVersion"
            .replace("{" + "datastoreId" + "}", localVarApiClient.escapeString(datastoreId.toString()))
            .replace("{" + "imageSetId" + "}", localVarApiClient.escapeString(imageSetId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (latestVersion != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("latestVersion", latestVersion));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
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

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateImageSetMetadataValidateBeforeCall(String datastoreId, String imageSetId, String latestVersion, UpdateImageSetMetadataRequest updateImageSetMetadataRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datastoreId' is set
        if (datastoreId == null) {
            throw new ApiException("Missing the required parameter 'datastoreId' when calling updateImageSetMetadata(Async)");
        }

        // verify the required parameter 'imageSetId' is set
        if (imageSetId == null) {
            throw new ApiException("Missing the required parameter 'imageSetId' when calling updateImageSetMetadata(Async)");
        }

        // verify the required parameter 'latestVersion' is set
        if (latestVersion == null) {
            throw new ApiException("Missing the required parameter 'latestVersion' when calling updateImageSetMetadata(Async)");
        }

        // verify the required parameter 'updateImageSetMetadataRequest' is set
        if (updateImageSetMetadataRequest == null) {
            throw new ApiException("Missing the required parameter 'updateImageSetMetadataRequest' when calling updateImageSetMetadata(Async)");
        }

        return updateImageSetMetadataCall(datastoreId, imageSetId, latestVersion, updateImageSetMetadataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Update image set metadata attributes.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param latestVersion The latest image set version identifier. (required)
     * @param updateImageSetMetadataRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return UpdateImageSetMetadataResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public UpdateImageSetMetadataResponse updateImageSetMetadata(String datastoreId, String imageSetId, String latestVersion, UpdateImageSetMetadataRequest updateImageSetMetadataRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<UpdateImageSetMetadataResponse> localVarResp = updateImageSetMetadataWithHttpInfo(datastoreId, imageSetId, latestVersion, updateImageSetMetadataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Update image set metadata attributes.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param latestVersion The latest image set version identifier. (required)
     * @param updateImageSetMetadataRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;UpdateImageSetMetadataResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateImageSetMetadataResponse> updateImageSetMetadataWithHttpInfo(String datastoreId, String imageSetId, String latestVersion, UpdateImageSetMetadataRequest updateImageSetMetadataRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = updateImageSetMetadataValidateBeforeCall(datastoreId, imageSetId, latestVersion, updateImageSetMetadataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<UpdateImageSetMetadataResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Update image set metadata attributes.
     * @param datastoreId The data store identifier. (required)
     * @param imageSetId The image set identifier. (required)
     * @param latestVersion The latest image set version identifier. (required)
     * @param updateImageSetMetadataRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 486 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateImageSetMetadataAsync(String datastoreId, String imageSetId, String latestVersion, UpdateImageSetMetadataRequest updateImageSetMetadataRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<UpdateImageSetMetadataResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateImageSetMetadataValidateBeforeCall(datastoreId, imageSetId, latestVersion, updateImageSetMetadataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<UpdateImageSetMetadataResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
