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

import org.openapitools.client.ApiException;
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
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for VbaDocumentsApi
 */
@Disabled
public class VbaDocumentsApiTest {

    private final VbaDocumentsApi api = new VbaDocumentsApi();

    /**
     * Download zip of \&quot;what the server sees\&quot;
     *
     * An endpoint that will allow you to see exactly what the server sees. We split apart all submitted docs and metadata and zip the file to make it available to you to help with debugging purposes. Files are deleted after 10 days. Only available in testing environments, not production.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getBenefitsDocumentUploadDownloadTest() throws ApiException {
        UUID id = null;
        File response = api.getBenefitsDocumentUploadDownload(id);
        // TODO: test validations
    }

    /**
     * Get status for a previous benefits document upload
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getBenefitsDocumentUploadStatusTest() throws ApiException {
        UUID id = null;
        GetBenefitsDocumentUploadStatus200Response response = api.getBenefitsDocumentUploadStatus(id);
        // TODO: test validations
    }

    /**
     * Get a bulk status report for a list of previous uploads
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getBenefitsDocumentUploadStatusReportTest() throws ApiException {
        DocumentUploadStatusGuidList documentUploadStatusGuidList = null;
        GetBenefitsDocumentUploadStatusReport200Response response = api.getBenefitsDocumentUploadStatusReport(documentUploadStatusGuidList);
        // TODO: test validations
    }

    /**
     * Get a location for subsequent document upload PUT request
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postBenefitsDocumentUploadTest() throws ApiException {
        PostBenefitsDocumentUpload202Response response = api.postBenefitsDocumentUpload();
        // TODO: test validations
    }

    /**
     * Validate an individual document against system file requirements
     *
     * Using this endpoint will decrease the likelihood of errors associated with individual documents during the submission process. Validations performed: * Document is a valid PDF (Note: &#x60;Content-Type&#x60; header value must be \&quot;application/pdf\&quot;) * Document does not have a user password (an owner password is acceptable) * File size does not exceed 100 MB * Page size does not exceed 21\&quot; x 21\&quot;  Each PDF document is sent as a direct file upload. The request body should contain nothing other than the document in binary format. Binary multipart/form-data encoding is not supported. This endpoint does NOT validate metadata in JSON format.  This endpoint does NOT initiate the claims intake process or submit data to that process. After using this endpoint, individual PDF documents can be combined and submitted as a payload using PUT &#x60;/path&#x60;.  A &#x60;200&#x60; response confirms that the individual document provided passes the system requirements.  A &#x60;422&#x60; response indicates one or more problems with the document that should be resolved before submitting it in the full document submission payload. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postBenefitsDocumentUploadValidateDocumentTest() throws ApiException {
        PostBenefitsDocumentUploadValidateDocument200Response response = api.postBenefitsDocumentUploadValidateDocument();
        // TODO: test validations
    }

    /**
     * Accepts document upload.
     *
     * Accepts document metadata, document binary, and attachment binaries. Full URL, including query parameters, provided from POST &#x60;/document_uploads&#x60;.  ## Example Payload  The following demonstrates a (redacted) multipart payload suitable for submitting to the PUT endpoint. Most programming languages should have provisions for assembling a multipart payload like this without having to do so manually.  &#x60;&#x60;&#x60; --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;metadata\&quot; Content-Type: application/json  {\&quot;veteranFirstName\&quot;: \&quot;Jane\&quot;, \&quot;veteranLastName\&quot;: \&quot;Doe\&quot;, \&quot;fileNumber\&quot;: \&quot;012345678\&quot;, \&quot;zipCode\&quot;: \&quot;97202\&quot;, \&quot;source\&quot;: \&quot;MyVSO\&quot;, \&quot;docType\&quot;: \&quot;21-22\&quot; \&quot;businessLine\&quot;: \&quot;CMP\&quot;} --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;content\&quot; Content-Type: application/pdf  &lt;Binary PDF contents&gt; --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;attachment1\&quot; Content-Type: application/pdf  &lt;Binary PDF attachment contents&gt; --17de1ed8f01442b2a2d7a93506314b76-- &#x60;&#x60;&#x60;  This PUT request would have an overall HTTP Content-Type header:  &#x60;&#x60;&#x60; Content-Type: multipart/form-data; boundary&#x3D;17de1ed8f01442b2a2d7a93506314b76 &#x60;&#x60;&#x60;  Note that the Content-Disposition parameter \&quot;name\&quot; in each part must be the expected values \&quot;metadata\&quot;, \&quot;content\&quot;, \&quot;attachment1\&quot;...\&quot;attachmentN\&quot;. The attachment attributes must be named  exactly as they are listed here (case sensitive), for example: \&quot;attachment_1\&quot; or \&quot;Attachment2\&quot; are invalid.  This is an example curl command:  &#x60;&#x60;&#x60; curl -v -L -X PUT &#39;&lt;Location from \\uploads&gt;&#39; -F &#39;metadata&#x3D;\&quot;{\\\&quot;veteranFirstName\\\&quot;: \\\&quot;Jane\\\&quot;,\\\&quot;veteranLastName\\\&quot;: \\\&quot;Doe\\\&quot;,\\\&quot;fileNumber\\\&quot;: \\\&quot;012345678\\\&quot;,\\\&quot;zipCode\\\&quot;: \\\&quot;97202\\\&quot;,\\\&quot;source\\\&quot;: \\\&quot;MyVSO\\\&quot;,\\\&quot;docType\\\&quot;: \\\&quot;21-22\\\&quot;,\\\&quot;businessLine\\\&quot;: \\\&quot;CMP\\\&quot;}\&quot;;type&#x3D;application/json&#39; -F &#39;content&#x3D;@\&quot;content.pdf\&quot;&#39; -F &#39;attachment1&#x3D;@\&quot;file1.pdf\&quot;&#39; -F &#39;attachment2&#x3D;@\&quot;another_file.pdf\&quot;&#39; &#x60;&#x60;&#x60; 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putBenefitsDocumentUploadTest() throws ApiException {
        String contentMD5 = null;
        api.putBenefitsDocumentUpload(contentMD5);
        // TODO: test validations
    }

}
