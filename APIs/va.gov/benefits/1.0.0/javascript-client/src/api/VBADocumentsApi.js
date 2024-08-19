/**
 * Benefits Intake
 * The Benefits Intake API allows authorized third-party systems used by Veteran Service Organizations (VSOs), agencies, and Veterans to digitally submit VA benefits claim documents directly to the Veterans Benefits Administration's (VBA) claims intake process. This API handles documents related to the following benefit claim types:   * Compensation * Pension/Survivors Benefits * Education * Fiduciary * Insurance * Veteran Readiness & Employment (VRE) * Board of Veteran Appeals (BVA)  This API also provides submission status updates until documents are successfully established for VBA claim processing, eliminating the need for users to switch between systems to manually check whether documents have been successfully uploaded.  ## Background  This API provides a secure, efficient, and tracked alternative to mail or fax for VA benefit claim document submissions. Documents are uploaded directly to the VBA so they can be processed as quickly as possible.  ## Technical overview The Benefits Intake API first provides an upload location and unique submission identifier, and then accepts a payload consisting of a document in PDF format, zero or more optional attachments in PDF format, and some JSON metadata.   The metadata describes the document and attachments, and identifies the person for whom it is being submitted. This payload is encoded as binary multipart/form-data (not base64). The unique identifier supplied with the payload can subsequently be used to request the processing status of the uploaded document package.  To avoid errors and processing delays, API consumers are encouraged to validate the `zipcode`,`fileNumber`, `veteranFirstName`, `veteranLastName` and `businessLine` fields before submission according to their description in the DocumentUploadMetadata model and use the 'businessLine' attribute for the most efficient processing. Additionally, please ensure no PDF user passwords are used in submitted PDFs.   ### Attachment & file size limits There is no limit on the number of files a payload can contain, but size limits do apply.  * Uploaded documents cannot be larger than 21\" x 21\" * The entire payload cannot exceed 5 GB * No single file in a payload can exceed 100 MB  ### Date of receipt The date that documents are successfully submitted through the Benefits Intake API is used as the official VA date of receipt. However, note that until a document status of `received`, `processing`, `success`, or `vbms` is returned, a client cannot consider the document received by VA.   A status of `received` means that the document package has been transmitted, but may not be validated. Any errors with the document package, such as unreadable PDFs or a Veteran not found, will cause the status to change to `error`.  If the document status is `error`, VA has not received the submission and cannot honor the submission date as the date of receipt.  ### Authentication and Authorization API requests are authorized through a symmetric API token, provided in an HTTP header with name 'apikey'. [Request an API key.](https://developer.va.gov/apply)  ### Testing in the sandbox environment In the sandbox environment, the final status of a submission is `received` and submissions do not actually progress to the central mail repository or VBMS.   Progress beyond the `received` status can be simulated for testing. We allow passing in a `Status-Override` header on the `/uploads/{id}` endpoint so that you can change the status of your submission to simulate the various scenarios.   The available statuses are `pending`, `uploaded`, `received`, `processing`, `success`, `vbms`, and `error`. The meaning of the various statuses is listed below in Models under DocumentUploadStatusAttributes.  ### Test data We use mock test data in the sandbox environment. Data is not sent upstream and it is not necessary to align submitted test data with any other systems' data.  ### Validating documents Use the POST `/uploads/validate_document` endpoint to make sure your documents will pass system file requirements and validations before you send them through the submissions process. This step is optional but decreases the likelihood of individual document errors during the submission process.  Validations performed: * Document is a valid PDF (Note: `Content-Type` header value must be \"application/pdf\") * Document does not have a user password (an owner password is acceptable) * File size does not exceed 100 MB * Page size does not exceed 21\" x 21\"  ### Upload operation Allows a client to upload a multi-part document package (form + attachments + metadata).  1. Client Request: POST https://sandbox-api.va.gov/services/vba_documents/v1/     * No request body or parameters required  2. Service Response: A JSON API object with the following attributes:     * `guid`: An identifier used for subsequent status requests     * `location`: A URL to which the actual document package payload can be submitted in the next step. The URL is specific to this upload request, and should not be re-used for subsequent uploads. The URL is valid for 900 seconds (15 minutes) from the time of this response. If the location is not used within 15 minutes, the GUID will expire. Once expired, status checks on the GUID will return a status of `expired`.         * Note: If, after you've submitted a document, the status hasn't changed to `uploaded` before 15 minutes has elapsed, we recommend retrying the upload in order to make sure the document properly reaches our servers. If the upload continues to fail, try encoding the payload as Base64 (See below).   3. Client Request: PUT to the location URL returned in Step 2.     * Request body should be encoded as binary multipart/form-data (base64 also available - see details below), equivalent to that generated by an HTML form submission or using \"curl -F…\". The format is described in more detail below.     * No `apikey` authorization header is required for this request, as authorization is embedded in the signed location URL.  4. Service Response: The HTTP status indicates whether the upload was successful.     * Additionally, the response includes an ETag header containing an MD5 hash of the submitted payload. This can be compared to the submitted payload to ensure data integrity of the upload.  ### Status caching Due to current system limitations, data for the `/uploads/report` endpoint is cached for one hour.  A request to the `/uploads/{id}` endpoint will return a real-time status for that GUID, and update its status in `/uploads/report`.  The `updated_at` field indicates the last time the status for a given GUID was updated.  ### Document Submission Statuses **Important note:** a submission has not been received by VA until it has a status of Received, Processing, Success,  or VBMS. Detailed descriptions of what each status means are found in this table.  | Status        | What it means | | ---           |     ---     | | **Pending**   | Initial status.<br /><br />Indicates no document package has been uploaded yet.<br /><br />Date of Receipt is not yet established with this status | | **Uploaded**  | Indicates document package has been successfully uploaded (PUT) from your system to the API server but has not yet been validated.<br /><br />Date of Receipt is not yet established with this status. Any errors with the document package, such as having an unreadable PDF, may cause an Error status. | | **Received**  | Indicates document package has been received upstream of the API and is awaiting Processing.<br /><br />The VA Date of Receipt is set when this status is achieved.<br /><br />This is the final status in the sandbox environment unless further progress is simulated. | | **Processing**| Indicates the document package is being validated, processed, and made ready to route and work. | | **Success**   | Indicates the document package has been successfully received within VA's mail handling system.<br /><br />Success is the final status for a small percentage of submitted packages with claim types, Veteran types, or exception processes that are not worked in VBMS. Most submissions reach a Success status within 1 business day. A small portion will take longer; however, some submissions may take up to 2 weeks to reach a Success status. | | **VBMS**      | Indicates this document package was successfully uploaded into a Veteran's eFolder within VBMS.<br /><br />On average, submissions reach VBMS status within 3 business days; however, processing times vary and some submissions may remain in a Success status for several weeks before reaching a VBMS status.<br /><br />Some document packages are worked in VA systems other than VBMS. For these submissions, Success is the final status. | | **Error**     | Indicates that there was an error. Refer to the error code and message for further information. | | **Expired**   | After a POST request, there is a 15-minute window during which documents must be uploaded via a PUT request.<br /><br />An Expired status means the documents were not successfully uploaded within this 15-minute window. We recommend coding to retry unsuccessful uploads within 15 minutes using the same submission in case of connection issues. |  ### Optional Base64 encoding  Base64 is an encoding scheme that converts binary data into text format, so that encoded textual data can be easily transported over networks uncorrupted and without data loss.   Base64 can be used to encode binary multipart/form-data it in its entirety.  Note that the whole payload must be encoded, not individual parts/attachments.  After encoding your payload, you'll be required to preface your base64 string with `data:multipart/form-data;base64,` in order to allow our system to distinguish the file type. Your final string payload would look something like `data:multipart/form-data;base64,(encryption string)==` and close with the standard == marker.  Note that the multipart boundaries i.e. -----WebKitFormBoundaryVfOwzCyvug0JmWYo and ending ------WebKitFormBoundaryVfOwzCyvug0JmWYo- must also be included.  ### Consumer onboarding process When you're ready to move to production, [request a production API key.](https://developer.va.gov/go-live) 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import DocumentUploadFailure from '../model/DocumentUploadFailure';
import DocumentUploadStatusGuidList from '../model/DocumentUploadStatusGuidList';
import GetBenefitsDocumentUploadStatus200Response from '../model/GetBenefitsDocumentUploadStatus200Response';
import GetBenefitsDocumentUploadStatus404Response from '../model/GetBenefitsDocumentUploadStatus404Response';
import GetBenefitsDocumentUploadStatusReport200Response from '../model/GetBenefitsDocumentUploadStatusReport200Response';
import PostBenefitsDocumentUpload202Response from '../model/PostBenefitsDocumentUpload202Response';
import PostBenefitsDocumentUpload403Response from '../model/PostBenefitsDocumentUpload403Response';
import PostBenefitsDocumentUploadValidateDocument200Response from '../model/PostBenefitsDocumentUploadValidateDocument200Response';
import PostBenefitsDocumentUploadValidateDocument422Response from '../model/PostBenefitsDocumentUploadValidateDocument422Response';
import PutBenefitsDocumentUpload401Response from '../model/PutBenefitsDocumentUpload401Response';
import PutBenefitsDocumentUpload422Response from '../model/PutBenefitsDocumentUpload422Response';
import PutBenefitsDocumentUpload429Response from '../model/PutBenefitsDocumentUpload429Response';
import PutBenefitsDocumentUpload500Response from '../model/PutBenefitsDocumentUpload500Response';

/**
* VBADocuments service.
* @module api/VBADocumentsApi
* @version 1.0.0
*/
export default class VBADocumentsApi {

    /**
    * Constructs a new VBADocumentsApi. 
    * @alias module:api/VBADocumentsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getBenefitsDocumentUploadDownload operation.
     * @callback module:api/VBADocumentsApi~getBenefitsDocumentUploadDownloadCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Download zip of \"what the server sees\"
     * An endpoint that will allow you to see exactly what the server sees. We split apart all submitted docs and metadata and zip the file to make it available to you to help with debugging purposes. Files are deleted after 10 days. Only available in testing environments, not production.
     * @param {String} id ID as returned by a previous create upload request
     * @param {module:api/VBADocumentsApi~getBenefitsDocumentUploadDownloadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    getBenefitsDocumentUploadDownload(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getBenefitsDocumentUploadDownload");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = [];
      let accepts = ['application/zip', 'application/json'];
      let returnType = File;
      return this.apiClient.callApi(
        '/uploads/{id}/download', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getBenefitsDocumentUploadStatus operation.
     * @callback module:api/VBADocumentsApi~getBenefitsDocumentUploadStatusCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetBenefitsDocumentUploadStatus200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get status for a previous benefits document upload
     * @param {String} id ID as returned by a previous create upload request
     * @param {module:api/VBADocumentsApi~getBenefitsDocumentUploadStatusCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetBenefitsDocumentUploadStatus200Response}
     */
    getBenefitsDocumentUploadStatus(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getBenefitsDocumentUploadStatus");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetBenefitsDocumentUploadStatus200Response;
      return this.apiClient.callApi(
        '/uploads/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getBenefitsDocumentUploadStatusReport operation.
     * @callback module:api/VBADocumentsApi~getBenefitsDocumentUploadStatusReportCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetBenefitsDocumentUploadStatusReport200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a bulk status report for a list of previous uploads
     * @param {module:model/DocumentUploadStatusGuidList} documentUploadStatusGuidList List of GUIDs for which to retrieve current status
     * @param {module:api/VBADocumentsApi~getBenefitsDocumentUploadStatusReportCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetBenefitsDocumentUploadStatusReport200Response}
     */
    getBenefitsDocumentUploadStatusReport(documentUploadStatusGuidList, callback) {
      let postBody = documentUploadStatusGuidList;
      // verify the required parameter 'documentUploadStatusGuidList' is set
      if (documentUploadStatusGuidList === undefined || documentUploadStatusGuidList === null) {
        throw new Error("Missing the required parameter 'documentUploadStatusGuidList' when calling getBenefitsDocumentUploadStatusReport");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetBenefitsDocumentUploadStatusReport200Response;
      return this.apiClient.callApi(
        '/uploads/report', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postBenefitsDocumentUpload operation.
     * @callback module:api/VBADocumentsApi~postBenefitsDocumentUploadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PostBenefitsDocumentUpload202Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a location for subsequent document upload PUT request
     * @param {module:api/VBADocumentsApi~postBenefitsDocumentUploadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PostBenefitsDocumentUpload202Response}
     */
    postBenefitsDocumentUpload(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PostBenefitsDocumentUpload202Response;
      return this.apiClient.callApi(
        '/uploads', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postBenefitsDocumentUploadValidateDocument operation.
     * @callback module:api/VBADocumentsApi~postBenefitsDocumentUploadValidateDocumentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PostBenefitsDocumentUploadValidateDocument200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Validate an individual document against system file requirements
     * Using this endpoint will decrease the likelihood of errors associated with individual documents during the submission process. Validations performed: * Document is a valid PDF (Note: `Content-Type` header value must be \"application/pdf\") * Document does not have a user password (an owner password is acceptable) * File size does not exceed 100 MB * Page size does not exceed 21\" x 21\"  Each PDF document is sent as a direct file upload. The request body should contain nothing other than the document in binary format. Binary multipart/form-data encoding is not supported. This endpoint does NOT validate metadata in JSON format.  This endpoint does NOT initiate the claims intake process or submit data to that process. After using this endpoint, individual PDF documents can be combined and submitted as a payload using PUT `/path`.  A `200` response confirms that the individual document provided passes the system requirements.  A `422` response indicates one or more problems with the document that should be resolved before submitting it in the full document submission payload. 
     * @param {module:api/VBADocumentsApi~postBenefitsDocumentUploadValidateDocumentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PostBenefitsDocumentUploadValidateDocument200Response}
     */
    postBenefitsDocumentUploadValidateDocument(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PostBenefitsDocumentUploadValidateDocument200Response;
      return this.apiClient.callApi(
        '/uploads/validate_document', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putBenefitsDocumentUpload operation.
     * @callback module:api/VBADocumentsApi~putBenefitsDocumentUploadCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Accepts document upload.
     * Accepts document metadata, document binary, and attachment binaries. Full URL, including query parameters, provided from POST `/document_uploads`.  ## Example Payload  The following demonstrates a (redacted) multipart payload suitable for submitting to the PUT endpoint. Most programming languages should have provisions for assembling a multipart payload like this without having to do so manually.  ``` --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name=\"metadata\" Content-Type: application/json  {\"veteranFirstName\": \"Jane\", \"veteranLastName\": \"Doe\", \"fileNumber\": \"012345678\", \"zipCode\": \"97202\", \"source\": \"MyVSO\", \"docType\": \"21-22\" \"businessLine\": \"CMP\"} --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name=\"content\" Content-Type: application/pdf  <Binary PDF contents> --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name=\"attachment1\" Content-Type: application/pdf  <Binary PDF attachment contents> --17de1ed8f01442b2a2d7a93506314b76-- ```  This PUT request would have an overall HTTP Content-Type header:  ``` Content-Type: multipart/form-data; boundary=17de1ed8f01442b2a2d7a93506314b76 ```  Note that the Content-Disposition parameter \"name\" in each part must be the expected values \"metadata\", \"content\", \"attachment1\"...\"attachmentN\". The attachment attributes must be named  exactly as they are listed here (case sensitive), for example: \"attachment_1\" or \"Attachment2\" are invalid.  This is an example curl command:  ``` curl -v -L -X PUT '<Location from \\uploads>' -F 'metadata=\"{\\\"veteranFirstName\\\": \\\"Jane\\\",\\\"veteranLastName\\\": \\\"Doe\\\",\\\"fileNumber\\\": \\\"012345678\\\",\\\"zipCode\\\": \\\"97202\\\",\\\"source\\\": \\\"MyVSO\\\",\\\"docType\\\": \\\"21-22\\\",\\\"businessLine\\\": \\\"CMP\\\"}\";type=application/json' -F 'content=@\"content.pdf\"' -F 'attachment1=@\"file1.pdf\"' -F 'attachment2=@\"another_file.pdf\"' ``` 
     * @param {Object} opts Optional parameters
     * @param {String} [contentMD5] Base64-encoded 128-bit MD5 digest of the message. Use for integrity control
     * @param {module:api/VBADocumentsApi~putBenefitsDocumentUploadCallback} callback The callback function, accepting three arguments: error, data, response
     */
    putBenefitsDocumentUpload(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Content-MD5': opts['contentMD5']
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = null;
      return this.apiClient.callApi(
        '/path', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
