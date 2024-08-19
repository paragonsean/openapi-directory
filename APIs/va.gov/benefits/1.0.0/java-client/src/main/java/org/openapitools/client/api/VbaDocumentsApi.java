/*
 * Benefits Intake
 * The Benefits Intake API allows authorized third-party systems used by Veteran Service Organizations (VSOs), agencies, and Veterans to digitally submit VA benefits claim documents directly to the Veterans Benefits Administration's (VBA) claims intake process. This API handles documents related to the following benefit claim types:   * Compensation * Pension/Survivors Benefits * Education * Fiduciary * Insurance * Veteran Readiness & Employment (VRE) * Board of Veteran Appeals (BVA)  This API also provides submission status updates until documents are successfully established for VBA claim processing, eliminating the need for users to switch between systems to manually check whether documents have been successfully uploaded.  ## Background  This API provides a secure, efficient, and tracked alternative to mail or fax for VA benefit claim document submissions. Documents are uploaded directly to the VBA so they can be processed as quickly as possible.  ## Technical overview The Benefits Intake API first provides an upload location and unique submission identifier, and then accepts a payload consisting of a document in PDF format, zero or more optional attachments in PDF format, and some JSON metadata.   The metadata describes the document and attachments, and identifies the person for whom it is being submitted. This payload is encoded as binary multipart/form-data (not base64). The unique identifier supplied with the payload can subsequently be used to request the processing status of the uploaded document package.  To avoid errors and processing delays, API consumers are encouraged to validate the `zipcode`,`fileNumber`, `veteranFirstName`, `veteranLastName` and `businessLine` fields before submission according to their description in the DocumentUploadMetadata model and use the 'businessLine' attribute for the most efficient processing. Additionally, please ensure no PDF user passwords are used in submitted PDFs.   ### Attachment & file size limits There is no limit on the number of files a payload can contain, but size limits do apply.  * Uploaded documents cannot be larger than 21\" x 21\" * The entire payload cannot exceed 5 GB * No single file in a payload can exceed 100 MB  ### Date of receipt The date that documents are successfully submitted through the Benefits Intake API is used as the official VA date of receipt. However, note that until a document status of `received`, `processing`, `success`, or `vbms` is returned, a client cannot consider the document received by VA.   A status of `received` means that the document package has been transmitted, but may not be validated. Any errors with the document package, such as unreadable PDFs or a Veteran not found, will cause the status to change to `error`.  If the document status is `error`, VA has not received the submission and cannot honor the submission date as the date of receipt.  ### Authentication and Authorization API requests are authorized through a symmetric API token, provided in an HTTP header with name 'apikey'. [Request an API key.](https://developer.va.gov/apply)  ### Testing in the sandbox environment In the sandbox environment, the final status of a submission is `received` and submissions do not actually progress to the central mail repository or VBMS.   Progress beyond the `received` status can be simulated for testing. We allow passing in a `Status-Override` header on the `/uploads/{id}` endpoint so that you can change the status of your submission to simulate the various scenarios.   The available statuses are `pending`, `uploaded`, `received`, `processing`, `success`, `vbms`, and `error`. The meaning of the various statuses is listed below in Models under DocumentUploadStatusAttributes.  ### Test data We use mock test data in the sandbox environment. Data is not sent upstream and it is not necessary to align submitted test data with any other systems' data.  ### Validating documents Use the POST `/uploads/validate_document` endpoint to make sure your documents will pass system file requirements and validations before you send them through the submissions process. This step is optional but decreases the likelihood of individual document errors during the submission process.  Validations performed: * Document is a valid PDF (Note: `Content-Type` header value must be \"application/pdf\") * Document does not have a user password (an owner password is acceptable) * File size does not exceed 100 MB * Page size does not exceed 21\" x 21\"  ### Upload operation Allows a client to upload a multi-part document package (form + attachments + metadata).  1. Client Request: POST https://sandbox-api.va.gov/services/vba_documents/v1/     * No request body or parameters required  2. Service Response: A JSON API object with the following attributes:     * `guid`: An identifier used for subsequent status requests     * `location`: A URL to which the actual document package payload can be submitted in the next step. The URL is specific to this upload request, and should not be re-used for subsequent uploads. The URL is valid for 900 seconds (15 minutes) from the time of this response. If the location is not used within 15 minutes, the GUID will expire. Once expired, status checks on the GUID will return a status of `expired`.         * Note: If, after you've submitted a document, the status hasn't changed to `uploaded` before 15 minutes has elapsed, we recommend retrying the upload in order to make sure the document properly reaches our servers. If the upload continues to fail, try encoding the payload as Base64 (See below).   3. Client Request: PUT to the location URL returned in Step 2.     * Request body should be encoded as binary multipart/form-data (base64 also available - see details below), equivalent to that generated by an HTML form submission or using \"curl -F…\". The format is described in more detail below.     * No `apikey` authorization header is required for this request, as authorization is embedded in the signed location URL.  4. Service Response: The HTTP status indicates whether the upload was successful.     * Additionally, the response includes an ETag header containing an MD5 hash of the submitted payload. This can be compared to the submitted payload to ensure data integrity of the upload.  ### Status caching Due to current system limitations, data for the `/uploads/report` endpoint is cached for one hour.  A request to the `/uploads/{id}` endpoint will return a real-time status for that GUID, and update its status in `/uploads/report`.  The `updated_at` field indicates the last time the status for a given GUID was updated.  ### Document Submission Statuses **Important note:** a submission has not been received by VA until it has a status of Received, Processing, Success,  or VBMS. Detailed descriptions of what each status means are found in this table.  | Status        | What it means | | ---           |     ---     | | **Pending**   | Initial status.<br /><br />Indicates no document package has been uploaded yet.<br /><br />Date of Receipt is not yet established with this status | | **Uploaded**  | Indicates document package has been successfully uploaded (PUT) from your system to the API server but has not yet been validated.<br /><br />Date of Receipt is not yet established with this status. Any errors with the document package, such as having an unreadable PDF, may cause an Error status. | | **Received**  | Indicates document package has been received upstream of the API and is awaiting Processing.<br /><br />The VA Date of Receipt is set when this status is achieved.<br /><br />This is the final status in the sandbox environment unless further progress is simulated. | | **Processing**| Indicates the document package is being validated, processed, and made ready to route and work. | | **Success**   | Indicates the document package has been successfully received within VA's mail handling system.<br /><br />Success is the final status for a small percentage of submitted packages with claim types, Veteran types, or exception processes that are not worked in VBMS. Most submissions reach a Success status within 1 business day. A small portion will take longer; however, some submissions may take up to 2 weeks to reach a Success status. | | **VBMS**      | Indicates this document package was successfully uploaded into a Veteran's eFolder within VBMS.<br /><br />On average, submissions reach VBMS status within 3 business days; however, processing times vary and some submissions may remain in a Success status for several weeks before reaching a VBMS status.<br /><br />Some document packages are worked in VA systems other than VBMS. For these submissions, Success is the final status. | | **Error**     | Indicates that there was an error. Refer to the error code and message for further information. | | **Expired**   | After a POST request, there is a 15-minute window during which documents must be uploaded via a PUT request.<br /><br />An Expired status means the documents were not successfully uploaded within this 15-minute window. We recommend coding to retry unsuccessful uploads within 15 minutes using the same submission in case of connection issues. |  ### Optional Base64 encoding  Base64 is an encoding scheme that converts binary data into text format, so that encoded textual data can be easily transported over networks uncorrupted and without data loss.   Base64 can be used to encode binary multipart/form-data it in its entirety.  Note that the whole payload must be encoded, not individual parts/attachments.  After encoding your payload, you'll be required to preface your base64 string with `data:multipart/form-data;base64,` in order to allow our system to distinguish the file type. Your final string payload would look something like `data:multipart/form-data;base64,(encryption string)==` and close with the standard == marker.  Note that the multipart boundaries i.e. -----WebKitFormBoundaryVfOwzCyvug0JmWYo and ending ------WebKitFormBoundaryVfOwzCyvug0JmWYo- must also be included.  ### Consumer onboarding process When you're ready to move to production, [request a production API key.](https://developer.va.gov/go-live) 
 *
 * The version of the OpenAPI document: 1.0.0
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


import org.openapitools.client.model.DocumentUploadFailure;
import org.openapitools.client.model.DocumentUploadStatusGuidList;
import java.io.File;
import org.openapitools.client.model.GetBenefitsDocumentUploadStatus200Response;
import org.openapitools.client.model.GetBenefitsDocumentUploadStatus404Response;
import org.openapitools.client.model.GetBenefitsDocumentUploadStatusReport200Response;
import org.openapitools.client.model.PostBenefitsDocumentUpload202Response;
import org.openapitools.client.model.PostBenefitsDocumentUpload403Response;
import org.openapitools.client.model.PostBenefitsDocumentUploadValidateDocument200Response;
import org.openapitools.client.model.PostBenefitsDocumentUploadValidateDocument422Response;
import org.openapitools.client.model.PutBenefitsDocumentUpload401Response;
import org.openapitools.client.model.PutBenefitsDocumentUpload422Response;
import org.openapitools.client.model.PutBenefitsDocumentUpload429Response;
import org.openapitools.client.model.PutBenefitsDocumentUpload500Response;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class VbaDocumentsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public VbaDocumentsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public VbaDocumentsApi(ApiClient apiClient) {
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
     * Build call for getBenefitsDocumentUploadDownload
     * @param id ID as returned by a previous create upload request (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Zip file with the contents of your payload as parsed by our server </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBenefitsDocumentUploadDownloadCall(UUID id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/uploads/{id}/download"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/zip",
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

        String[] localVarAuthNames = new String[] { "apikey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getBenefitsDocumentUploadDownloadValidateBeforeCall(UUID id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getBenefitsDocumentUploadDownload(Async)");
        }

        return getBenefitsDocumentUploadDownloadCall(id, _callback);

    }

    /**
     * Download zip of \&quot;what the server sees\&quot;
     * An endpoint that will allow you to see exactly what the server sees. We split apart all submitted docs and metadata and zip the file to make it available to you to help with debugging purposes. Files are deleted after 10 days. Only available in testing environments, not production.
     * @param id ID as returned by a previous create upload request (required)
     * @return File
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Zip file with the contents of your payload as parsed by our server </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public File getBenefitsDocumentUploadDownload(UUID id) throws ApiException {
        ApiResponse<File> localVarResp = getBenefitsDocumentUploadDownloadWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Download zip of \&quot;what the server sees\&quot;
     * An endpoint that will allow you to see exactly what the server sees. We split apart all submitted docs and metadata and zip the file to make it available to you to help with debugging purposes. Files are deleted after 10 days. Only available in testing environments, not production.
     * @param id ID as returned by a previous create upload request (required)
     * @return ApiResponse&lt;File&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Zip file with the contents of your payload as parsed by our server </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<File> getBenefitsDocumentUploadDownloadWithHttpInfo(UUID id) throws ApiException {
        okhttp3.Call localVarCall = getBenefitsDocumentUploadDownloadValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<File>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Download zip of \&quot;what the server sees\&quot; (asynchronously)
     * An endpoint that will allow you to see exactly what the server sees. We split apart all submitted docs and metadata and zip the file to make it available to you to help with debugging purposes. Files are deleted after 10 days. Only available in testing environments, not production.
     * @param id ID as returned by a previous create upload request (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Zip file with the contents of your payload as parsed by our server </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBenefitsDocumentUploadDownloadAsync(UUID id, final ApiCallback<File> _callback) throws ApiException {

        okhttp3.Call localVarCall = getBenefitsDocumentUploadDownloadValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<File>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getBenefitsDocumentUploadStatus
     * @param id ID as returned by a previous create upload request (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Upload status retrieved successfully </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBenefitsDocumentUploadStatusCall(UUID id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/uploads/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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

        String[] localVarAuthNames = new String[] { "apikey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getBenefitsDocumentUploadStatusValidateBeforeCall(UUID id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getBenefitsDocumentUploadStatus(Async)");
        }

        return getBenefitsDocumentUploadStatusCall(id, _callback);

    }

    /**
     * Get status for a previous benefits document upload
     * 
     * @param id ID as returned by a previous create upload request (required)
     * @return GetBenefitsDocumentUploadStatus200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Upload status retrieved successfully </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public GetBenefitsDocumentUploadStatus200Response getBenefitsDocumentUploadStatus(UUID id) throws ApiException {
        ApiResponse<GetBenefitsDocumentUploadStatus200Response> localVarResp = getBenefitsDocumentUploadStatusWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Get status for a previous benefits document upload
     * 
     * @param id ID as returned by a previous create upload request (required)
     * @return ApiResponse&lt;GetBenefitsDocumentUploadStatus200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Upload status retrieved successfully </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetBenefitsDocumentUploadStatus200Response> getBenefitsDocumentUploadStatusWithHttpInfo(UUID id) throws ApiException {
        okhttp3.Call localVarCall = getBenefitsDocumentUploadStatusValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<GetBenefitsDocumentUploadStatus200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get status for a previous benefits document upload (asynchronously)
     * 
     * @param id ID as returned by a previous create upload request (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Upload status retrieved successfully </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBenefitsDocumentUploadStatusAsync(UUID id, final ApiCallback<GetBenefitsDocumentUploadStatus200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getBenefitsDocumentUploadStatusValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<GetBenefitsDocumentUploadStatus200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getBenefitsDocumentUploadStatusReport
     * @param documentUploadStatusGuidList List of GUIDs for which to retrieve current status (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Upload status report retrieved successfully </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request - invalid or missing list of guids </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBenefitsDocumentUploadStatusReportCall(DocumentUploadStatusGuidList documentUploadStatusGuidList, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = documentUploadStatusGuidList;

        // create path and map variables
        String localVarPath = "/uploads/report";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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

        String[] localVarAuthNames = new String[] { "apikey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getBenefitsDocumentUploadStatusReportValidateBeforeCall(DocumentUploadStatusGuidList documentUploadStatusGuidList, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'documentUploadStatusGuidList' is set
        if (documentUploadStatusGuidList == null) {
            throw new ApiException("Missing the required parameter 'documentUploadStatusGuidList' when calling getBenefitsDocumentUploadStatusReport(Async)");
        }

        return getBenefitsDocumentUploadStatusReportCall(documentUploadStatusGuidList, _callback);

    }

    /**
     * Get a bulk status report for a list of previous uploads
     * 
     * @param documentUploadStatusGuidList List of GUIDs for which to retrieve current status (required)
     * @return GetBenefitsDocumentUploadStatusReport200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Upload status report retrieved successfully </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request - invalid or missing list of guids </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public GetBenefitsDocumentUploadStatusReport200Response getBenefitsDocumentUploadStatusReport(DocumentUploadStatusGuidList documentUploadStatusGuidList) throws ApiException {
        ApiResponse<GetBenefitsDocumentUploadStatusReport200Response> localVarResp = getBenefitsDocumentUploadStatusReportWithHttpInfo(documentUploadStatusGuidList);
        return localVarResp.getData();
    }

    /**
     * Get a bulk status report for a list of previous uploads
     * 
     * @param documentUploadStatusGuidList List of GUIDs for which to retrieve current status (required)
     * @return ApiResponse&lt;GetBenefitsDocumentUploadStatusReport200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Upload status report retrieved successfully </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request - invalid or missing list of guids </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetBenefitsDocumentUploadStatusReport200Response> getBenefitsDocumentUploadStatusReportWithHttpInfo(DocumentUploadStatusGuidList documentUploadStatusGuidList) throws ApiException {
        okhttp3.Call localVarCall = getBenefitsDocumentUploadStatusReportValidateBeforeCall(documentUploadStatusGuidList, null);
        Type localVarReturnType = new TypeToken<GetBenefitsDocumentUploadStatusReport200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a bulk status report for a list of previous uploads (asynchronously)
     * 
     * @param documentUploadStatusGuidList List of GUIDs for which to retrieve current status (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Upload status report retrieved successfully </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request - invalid or missing list of guids </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBenefitsDocumentUploadStatusReportAsync(DocumentUploadStatusGuidList documentUploadStatusGuidList, final ApiCallback<GetBenefitsDocumentUploadStatusReport200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getBenefitsDocumentUploadStatusReportValidateBeforeCall(documentUploadStatusGuidList, _callback);
        Type localVarReturnType = new TypeToken<GetBenefitsDocumentUploadStatusReport200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postBenefitsDocumentUpload
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Accepted. Location generated </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postBenefitsDocumentUploadCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/uploads";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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

        String[] localVarAuthNames = new String[] { "apikey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postBenefitsDocumentUploadValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return postBenefitsDocumentUploadCall(_callback);

    }

    /**
     * Get a location for subsequent document upload PUT request
     * 
     * @return PostBenefitsDocumentUpload202Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Accepted. Location generated </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public PostBenefitsDocumentUpload202Response postBenefitsDocumentUpload() throws ApiException {
        ApiResponse<PostBenefitsDocumentUpload202Response> localVarResp = postBenefitsDocumentUploadWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get a location for subsequent document upload PUT request
     * 
     * @return ApiResponse&lt;PostBenefitsDocumentUpload202Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Accepted. Location generated </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PostBenefitsDocumentUpload202Response> postBenefitsDocumentUploadWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = postBenefitsDocumentUploadValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<PostBenefitsDocumentUpload202Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a location for subsequent document upload PUT request (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Accepted. Location generated </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postBenefitsDocumentUploadAsync(final ApiCallback<PostBenefitsDocumentUpload202Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = postBenefitsDocumentUploadValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<PostBenefitsDocumentUpload202Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postBenefitsDocumentUploadValidateDocument
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Document passed system requirements </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Document did NOT pass system requirements </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postBenefitsDocumentUploadValidateDocumentCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/uploads/validate_document";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
    private okhttp3.Call postBenefitsDocumentUploadValidateDocumentValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return postBenefitsDocumentUploadValidateDocumentCall(_callback);

    }

    /**
     * Validate an individual document against system file requirements
     * Using this endpoint will decrease the likelihood of errors associated with individual documents during the submission process. Validations performed: * Document is a valid PDF (Note: &#x60;Content-Type&#x60; header value must be \&quot;application/pdf\&quot;) * Document does not have a user password (an owner password is acceptable) * File size does not exceed 100 MB * Page size does not exceed 21\&quot; x 21\&quot;  Each PDF document is sent as a direct file upload. The request body should contain nothing other than the document in binary format. Binary multipart/form-data encoding is not supported. This endpoint does NOT validate metadata in JSON format.  This endpoint does NOT initiate the claims intake process or submit data to that process. After using this endpoint, individual PDF documents can be combined and submitted as a payload using PUT &#x60;/path&#x60;.  A &#x60;200&#x60; response confirms that the individual document provided passes the system requirements.  A &#x60;422&#x60; response indicates one or more problems with the document that should be resolved before submitting it in the full document submission payload. 
     * @return PostBenefitsDocumentUploadValidateDocument200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Document passed system requirements </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Document did NOT pass system requirements </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public PostBenefitsDocumentUploadValidateDocument200Response postBenefitsDocumentUploadValidateDocument() throws ApiException {
        ApiResponse<PostBenefitsDocumentUploadValidateDocument200Response> localVarResp = postBenefitsDocumentUploadValidateDocumentWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Validate an individual document against system file requirements
     * Using this endpoint will decrease the likelihood of errors associated with individual documents during the submission process. Validations performed: * Document is a valid PDF (Note: &#x60;Content-Type&#x60; header value must be \&quot;application/pdf\&quot;) * Document does not have a user password (an owner password is acceptable) * File size does not exceed 100 MB * Page size does not exceed 21\&quot; x 21\&quot;  Each PDF document is sent as a direct file upload. The request body should contain nothing other than the document in binary format. Binary multipart/form-data encoding is not supported. This endpoint does NOT validate metadata in JSON format.  This endpoint does NOT initiate the claims intake process or submit data to that process. After using this endpoint, individual PDF documents can be combined and submitted as a payload using PUT &#x60;/path&#x60;.  A &#x60;200&#x60; response confirms that the individual document provided passes the system requirements.  A &#x60;422&#x60; response indicates one or more problems with the document that should be resolved before submitting it in the full document submission payload. 
     * @return ApiResponse&lt;PostBenefitsDocumentUploadValidateDocument200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Document passed system requirements </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Document did NOT pass system requirements </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PostBenefitsDocumentUploadValidateDocument200Response> postBenefitsDocumentUploadValidateDocumentWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = postBenefitsDocumentUploadValidateDocumentValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<PostBenefitsDocumentUploadValidateDocument200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Validate an individual document against system file requirements (asynchronously)
     * Using this endpoint will decrease the likelihood of errors associated with individual documents during the submission process. Validations performed: * Document is a valid PDF (Note: &#x60;Content-Type&#x60; header value must be \&quot;application/pdf\&quot;) * Document does not have a user password (an owner password is acceptable) * File size does not exceed 100 MB * Page size does not exceed 21\&quot; x 21\&quot;  Each PDF document is sent as a direct file upload. The request body should contain nothing other than the document in binary format. Binary multipart/form-data encoding is not supported. This endpoint does NOT validate metadata in JSON format.  This endpoint does NOT initiate the claims intake process or submit data to that process. After using this endpoint, individual PDF documents can be combined and submitted as a payload using PUT &#x60;/path&#x60;.  A &#x60;200&#x60; response confirms that the individual document provided passes the system requirements.  A &#x60;422&#x60; response indicates one or more problems with the document that should be resolved before submitting it in the full document submission payload. 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Document passed system requirements </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Document did NOT pass system requirements </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postBenefitsDocumentUploadValidateDocumentAsync(final ApiCallback<PostBenefitsDocumentUploadValidateDocument200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = postBenefitsDocumentUploadValidateDocumentValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<PostBenefitsDocumentUploadValidateDocument200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putBenefitsDocumentUpload
     * @param contentMD5 Base64-encoded 128-bit MD5 digest of the message. Use for integrity control (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Document upload staged </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Document upload failed </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putBenefitsDocumentUploadCall(String contentMD5, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/path";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (contentMD5 != null) {
            localVarHeaderParams.put("Content-MD5", localVarApiClient.parameterToString(contentMD5));
        }

        final String[] localVarAccepts = {
            "application/json",
            "application/xml"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putBenefitsDocumentUploadValidateBeforeCall(String contentMD5, final ApiCallback _callback) throws ApiException {
        return putBenefitsDocumentUploadCall(contentMD5, _callback);

    }

    /**
     * Accepts document upload.
     * Accepts document metadata, document binary, and attachment binaries. Full URL, including query parameters, provided from POST &#x60;/document_uploads&#x60;.  ## Example Payload  The following demonstrates a (redacted) multipart payload suitable for submitting to the PUT endpoint. Most programming languages should have provisions for assembling a multipart payload like this without having to do so manually.  &#x60;&#x60;&#x60; --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;metadata\&quot; Content-Type: application/json  {\&quot;veteranFirstName\&quot;: \&quot;Jane\&quot;, \&quot;veteranLastName\&quot;: \&quot;Doe\&quot;, \&quot;fileNumber\&quot;: \&quot;012345678\&quot;, \&quot;zipCode\&quot;: \&quot;97202\&quot;, \&quot;source\&quot;: \&quot;MyVSO\&quot;, \&quot;docType\&quot;: \&quot;21-22\&quot; \&quot;businessLine\&quot;: \&quot;CMP\&quot;} --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;content\&quot; Content-Type: application/pdf  &lt;Binary PDF contents&gt; --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;attachment1\&quot; Content-Type: application/pdf  &lt;Binary PDF attachment contents&gt; --17de1ed8f01442b2a2d7a93506314b76-- &#x60;&#x60;&#x60;  This PUT request would have an overall HTTP Content-Type header:  &#x60;&#x60;&#x60; Content-Type: multipart/form-data; boundary&#x3D;17de1ed8f01442b2a2d7a93506314b76 &#x60;&#x60;&#x60;  Note that the Content-Disposition parameter \&quot;name\&quot; in each part must be the expected values \&quot;metadata\&quot;, \&quot;content\&quot;, \&quot;attachment1\&quot;...\&quot;attachmentN\&quot;. The attachment attributes must be named  exactly as they are listed here (case sensitive), for example: \&quot;attachment_1\&quot; or \&quot;Attachment2\&quot; are invalid.  This is an example curl command:  &#x60;&#x60;&#x60; curl -v -L -X PUT &#39;&lt;Location from \\uploads&gt;&#39; -F &#39;metadata&#x3D;\&quot;{\\\&quot;veteranFirstName\\\&quot;: \\\&quot;Jane\\\&quot;,\\\&quot;veteranLastName\\\&quot;: \\\&quot;Doe\\\&quot;,\\\&quot;fileNumber\\\&quot;: \\\&quot;012345678\\\&quot;,\\\&quot;zipCode\\\&quot;: \\\&quot;97202\\\&quot;,\\\&quot;source\\\&quot;: \\\&quot;MyVSO\\\&quot;,\\\&quot;docType\\\&quot;: \\\&quot;21-22\\\&quot;,\\\&quot;businessLine\\\&quot;: \\\&quot;CMP\\\&quot;}\&quot;;type&#x3D;application/json&#39; -F &#39;content&#x3D;@\&quot;content.pdf\&quot;&#39; -F &#39;attachment1&#x3D;@\&quot;file1.pdf\&quot;&#39; -F &#39;attachment2&#x3D;@\&quot;another_file.pdf\&quot;&#39; &#x60;&#x60;&#x60; 
     * @param contentMD5 Base64-encoded 128-bit MD5 digest of the message. Use for integrity control (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Document upload staged </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Document upload failed </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public void putBenefitsDocumentUpload(String contentMD5) throws ApiException {
        putBenefitsDocumentUploadWithHttpInfo(contentMD5);
    }

    /**
     * Accepts document upload.
     * Accepts document metadata, document binary, and attachment binaries. Full URL, including query parameters, provided from POST &#x60;/document_uploads&#x60;.  ## Example Payload  The following demonstrates a (redacted) multipart payload suitable for submitting to the PUT endpoint. Most programming languages should have provisions for assembling a multipart payload like this without having to do so manually.  &#x60;&#x60;&#x60; --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;metadata\&quot; Content-Type: application/json  {\&quot;veteranFirstName\&quot;: \&quot;Jane\&quot;, \&quot;veteranLastName\&quot;: \&quot;Doe\&quot;, \&quot;fileNumber\&quot;: \&quot;012345678\&quot;, \&quot;zipCode\&quot;: \&quot;97202\&quot;, \&quot;source\&quot;: \&quot;MyVSO\&quot;, \&quot;docType\&quot;: \&quot;21-22\&quot; \&quot;businessLine\&quot;: \&quot;CMP\&quot;} --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;content\&quot; Content-Type: application/pdf  &lt;Binary PDF contents&gt; --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;attachment1\&quot; Content-Type: application/pdf  &lt;Binary PDF attachment contents&gt; --17de1ed8f01442b2a2d7a93506314b76-- &#x60;&#x60;&#x60;  This PUT request would have an overall HTTP Content-Type header:  &#x60;&#x60;&#x60; Content-Type: multipart/form-data; boundary&#x3D;17de1ed8f01442b2a2d7a93506314b76 &#x60;&#x60;&#x60;  Note that the Content-Disposition parameter \&quot;name\&quot; in each part must be the expected values \&quot;metadata\&quot;, \&quot;content\&quot;, \&quot;attachment1\&quot;...\&quot;attachmentN\&quot;. The attachment attributes must be named  exactly as they are listed here (case sensitive), for example: \&quot;attachment_1\&quot; or \&quot;Attachment2\&quot; are invalid.  This is an example curl command:  &#x60;&#x60;&#x60; curl -v -L -X PUT &#39;&lt;Location from \\uploads&gt;&#39; -F &#39;metadata&#x3D;\&quot;{\\\&quot;veteranFirstName\\\&quot;: \\\&quot;Jane\\\&quot;,\\\&quot;veteranLastName\\\&quot;: \\\&quot;Doe\\\&quot;,\\\&quot;fileNumber\\\&quot;: \\\&quot;012345678\\\&quot;,\\\&quot;zipCode\\\&quot;: \\\&quot;97202\\\&quot;,\\\&quot;source\\\&quot;: \\\&quot;MyVSO\\\&quot;,\\\&quot;docType\\\&quot;: \\\&quot;21-22\\\&quot;,\\\&quot;businessLine\\\&quot;: \\\&quot;CMP\\\&quot;}\&quot;;type&#x3D;application/json&#39; -F &#39;content&#x3D;@\&quot;content.pdf\&quot;&#39; -F &#39;attachment1&#x3D;@\&quot;file1.pdf\&quot;&#39; -F &#39;attachment2&#x3D;@\&quot;another_file.pdf\&quot;&#39; &#x60;&#x60;&#x60; 
     * @param contentMD5 Base64-encoded 128-bit MD5 digest of the message. Use for integrity control (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Document upload staged </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Document upload failed </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> putBenefitsDocumentUploadWithHttpInfo(String contentMD5) throws ApiException {
        okhttp3.Call localVarCall = putBenefitsDocumentUploadValidateBeforeCall(contentMD5, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Accepts document upload. (asynchronously)
     * Accepts document metadata, document binary, and attachment binaries. Full URL, including query parameters, provided from POST &#x60;/document_uploads&#x60;.  ## Example Payload  The following demonstrates a (redacted) multipart payload suitable for submitting to the PUT endpoint. Most programming languages should have provisions for assembling a multipart payload like this without having to do so manually.  &#x60;&#x60;&#x60; --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;metadata\&quot; Content-Type: application/json  {\&quot;veteranFirstName\&quot;: \&quot;Jane\&quot;, \&quot;veteranLastName\&quot;: \&quot;Doe\&quot;, \&quot;fileNumber\&quot;: \&quot;012345678\&quot;, \&quot;zipCode\&quot;: \&quot;97202\&quot;, \&quot;source\&quot;: \&quot;MyVSO\&quot;, \&quot;docType\&quot;: \&quot;21-22\&quot; \&quot;businessLine\&quot;: \&quot;CMP\&quot;} --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;content\&quot; Content-Type: application/pdf  &lt;Binary PDF contents&gt; --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;attachment1\&quot; Content-Type: application/pdf  &lt;Binary PDF attachment contents&gt; --17de1ed8f01442b2a2d7a93506314b76-- &#x60;&#x60;&#x60;  This PUT request would have an overall HTTP Content-Type header:  &#x60;&#x60;&#x60; Content-Type: multipart/form-data; boundary&#x3D;17de1ed8f01442b2a2d7a93506314b76 &#x60;&#x60;&#x60;  Note that the Content-Disposition parameter \&quot;name\&quot; in each part must be the expected values \&quot;metadata\&quot;, \&quot;content\&quot;, \&quot;attachment1\&quot;...\&quot;attachmentN\&quot;. The attachment attributes must be named  exactly as they are listed here (case sensitive), for example: \&quot;attachment_1\&quot; or \&quot;Attachment2\&quot; are invalid.  This is an example curl command:  &#x60;&#x60;&#x60; curl -v -L -X PUT &#39;&lt;Location from \\uploads&gt;&#39; -F &#39;metadata&#x3D;\&quot;{\\\&quot;veteranFirstName\\\&quot;: \\\&quot;Jane\\\&quot;,\\\&quot;veteranLastName\\\&quot;: \\\&quot;Doe\\\&quot;,\\\&quot;fileNumber\\\&quot;: \\\&quot;012345678\\\&quot;,\\\&quot;zipCode\\\&quot;: \\\&quot;97202\\\&quot;,\\\&quot;source\\\&quot;: \\\&quot;MyVSO\\\&quot;,\\\&quot;docType\\\&quot;: \\\&quot;21-22\\\&quot;,\\\&quot;businessLine\\\&quot;: \\\&quot;CMP\\\&quot;}\&quot;;type&#x3D;application/json&#39; -F &#39;content&#x3D;@\&quot;content.pdf\&quot;&#39; -F &#39;attachment1&#x3D;@\&quot;file1.pdf\&quot;&#39; -F &#39;attachment2&#x3D;@\&quot;another_file.pdf\&quot;&#39; &#x60;&#x60;&#x60; 
     * @param contentMD5 Base64-encoded 128-bit MD5 digest of the message. Use for integrity control (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Document upload staged </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized request </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Document upload failed </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putBenefitsDocumentUploadAsync(String contentMD5, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = putBenefitsDocumentUploadValidateBeforeCall(contentMD5, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
