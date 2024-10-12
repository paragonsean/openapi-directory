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


import ApiClient from './ApiClient';
import DocumentUploadAttributes from './model/DocumentUploadAttributes';
import DocumentUploadFailure from './model/DocumentUploadFailure';
import DocumentUploadMetadata from './model/DocumentUploadMetadata';
import DocumentUploadPath from './model/DocumentUploadPath';
import DocumentUploadStatus from './model/DocumentUploadStatus';
import DocumentUploadStatusAttributes from './model/DocumentUploadStatusAttributes';
import DocumentUploadStatusGuidList from './model/DocumentUploadStatusGuidList';
import DocumentUploadSubmission from './model/DocumentUploadSubmission';
import DocumentUploadSubmissionAttributes from './model/DocumentUploadSubmissionAttributes';
import DocumentValidationErrorModel from './model/DocumentValidationErrorModel';
import ErrorModel from './model/ErrorModel';
import GetBenefitsDocumentUploadStatus200Response from './model/GetBenefitsDocumentUploadStatus200Response';
import GetBenefitsDocumentUploadStatus404Response from './model/GetBenefitsDocumentUploadStatus404Response';
import GetBenefitsDocumentUploadStatusReport200Response from './model/GetBenefitsDocumentUploadStatusReport200Response';
import PdfDimensionAttributes from './model/PdfDimensionAttributes';
import PdfUploadAttributes from './model/PdfUploadAttributes';
import PdfUploadAttributesContent from './model/PdfUploadAttributesContent';
import PdfUploadAttributesContentAttachmentsInner from './model/PdfUploadAttributesContentAttachmentsInner';
import PostBenefitsDocumentUpload202Response from './model/PostBenefitsDocumentUpload202Response';
import PostBenefitsDocumentUpload403Response from './model/PostBenefitsDocumentUpload403Response';
import PostBenefitsDocumentUploadValidateDocument200Response from './model/PostBenefitsDocumentUploadValidateDocument200Response';
import PostBenefitsDocumentUploadValidateDocument200ResponseData from './model/PostBenefitsDocumentUploadValidateDocument200ResponseData';
import PostBenefitsDocumentUploadValidateDocument200ResponseDataAttributes from './model/PostBenefitsDocumentUploadValidateDocument200ResponseDataAttributes';
import PostBenefitsDocumentUploadValidateDocument422Response from './model/PostBenefitsDocumentUploadValidateDocument422Response';
import PutBenefitsDocumentUpload401Response from './model/PutBenefitsDocumentUpload401Response';
import PutBenefitsDocumentUpload422Response from './model/PutBenefitsDocumentUpload422Response';
import PutBenefitsDocumentUpload429Response from './model/PutBenefitsDocumentUpload429Response';
import PutBenefitsDocumentUpload500Response from './model/PutBenefitsDocumentUpload500Response';
import VBADocumentsApi from './api/VBADocumentsApi';


/**
* The Benefits Intake API allows authorized third-party systems used by Veteran Service Organizations (VSOs), agencies, and Veterans to digitally submit VA benefits claim documents directly to the Veterans Benefits Administration&#39;s (VBA) claims intake process. This API handles documents related to the following benefit claim types:   * Compensation * Pension/Survivors Benefits * Education * Fiduciary * Insurance * Veteran Readiness &amp; Employment (VRE) * Board of Veteran Appeals (BVA)  This API also provides submission status updates until documents are successfully established for VBA claim processing, eliminating the need for users to switch between systems to manually check whether documents have been successfully uploaded.  ## Background  This API provides a secure, efficient, and tracked alternative to mail or fax for VA benefit claim document submissions. Documents are uploaded directly to the VBA so they can be processed as quickly as possible.  ## Technical overview The Benefits Intake API first provides an upload location and unique submission identifier, and then accepts a payload consisting of a document in PDF format, zero or more optional attachments in PDF format, and some JSON metadata.   The metadata describes the document and attachments, and identifies the person for whom it is being submitted. This payload is encoded as binary multipart/form-data (not base64). The unique identifier supplied with the payload can subsequently be used to request the processing status of the uploaded document package.  To avoid errors and processing delays, API consumers are encouraged to validate the &#x60;zipcode&#x60;,&#x60;fileNumber&#x60;, &#x60;veteranFirstName&#x60;, &#x60;veteranLastName&#x60; and &#x60;businessLine&#x60; fields before submission according to their description in the DocumentUploadMetadata model and use the &#39;businessLine&#39; attribute for the most efficient processing. Additionally, please ensure no PDF user passwords are used in submitted PDFs.   ### Attachment &amp; file size limits There is no limit on the number of files a payload can contain, but size limits do apply.  * Uploaded documents cannot be larger than 21\&quot; x 21\&quot; * The entire payload cannot exceed 5 GB * No single file in a payload can exceed 100 MB  ### Date of receipt The date that documents are successfully submitted through the Benefits Intake API is used as the official VA date of receipt. However, note that until a document status of &#x60;received&#x60;, &#x60;processing&#x60;, &#x60;success&#x60;, or &#x60;vbms&#x60; is returned, a client cannot consider the document received by VA.   A status of &#x60;received&#x60; means that the document package has been transmitted, but may not be validated. Any errors with the document package, such as unreadable PDFs or a Veteran not found, will cause the status to change to &#x60;error&#x60;.  If the document status is &#x60;error&#x60;, VA has not received the submission and cannot honor the submission date as the date of receipt.  ### Authentication and Authorization API requests are authorized through a symmetric API token, provided in an HTTP header with name &#39;apikey&#39;. [Request an API key.](https://developer.va.gov/apply)  ### Testing in the sandbox environment In the sandbox environment, the final status of a submission is &#x60;received&#x60; and submissions do not actually progress to the central mail repository or VBMS.   Progress beyond the &#x60;received&#x60; status can be simulated for testing. We allow passing in a &#x60;Status-Override&#x60; header on the &#x60;/uploads/{id}&#x60; endpoint so that you can change the status of your submission to simulate the various scenarios.   The available statuses are &#x60;pending&#x60;, &#x60;uploaded&#x60;, &#x60;received&#x60;, &#x60;processing&#x60;, &#x60;success&#x60;, &#x60;vbms&#x60;, and &#x60;error&#x60;. The meaning of the various statuses is listed below in Models under DocumentUploadStatusAttributes.  ### Test data We use mock test data in the sandbox environment. Data is not sent upstream and it is not necessary to align submitted test data with any other systems&#39; data.  ### Validating documents Use the POST &#x60;/uploads/validate_document&#x60; endpoint to make sure your documents will pass system file requirements and validations before you send them through the submissions process. This step is optional but decreases the likelihood of individual document errors during the submission process.  Validations performed: * Document is a valid PDF (Note: &#x60;Content-Type&#x60; header value must be \&quot;application/pdf\&quot;) * Document does not have a user password (an owner password is acceptable) * File size does not exceed 100 MB * Page size does not exceed 21\&quot; x 21\&quot;  ### Upload operation Allows a client to upload a multi-part document package (form + attachments + metadata).  1. Client Request: POST https://sandbox-api.va.gov/services/vba_documents/v1/     * No request body or parameters required  2. Service Response: A JSON API object with the following attributes:     * &#x60;guid&#x60;: An identifier used for subsequent status requests     * &#x60;location&#x60;: A URL to which the actual document package payload can be submitted in the next step. The URL is specific to this upload request, and should not be re-used for subsequent uploads. The URL is valid for 900 seconds (15 minutes) from the time of this response. If the location is not used within 15 minutes, the GUID will expire. Once expired, status checks on the GUID will return a status of &#x60;expired&#x60;.         * Note: If, after you&#39;ve submitted a document, the status hasn&#39;t changed to &#x60;uploaded&#x60; before 15 minutes has elapsed, we recommend retrying the upload in order to make sure the document properly reaches our servers. If the upload continues to fail, try encoding the payload as Base64 (See below).   3. Client Request: PUT to the location URL returned in Step 2.     * Request body should be encoded as binary multipart/form-data (base64 also available - see details below), equivalent to that generated by an HTML form submission or using \&quot;curl -F…\&quot;. The format is described in more detail below.     * No &#x60;apikey&#x60; authorization header is required for this request, as authorization is embedded in the signed location URL.  4. Service Response: The HTTP status indicates whether the upload was successful.     * Additionally, the response includes an ETag header containing an MD5 hash of the submitted payload. This can be compared to the submitted payload to ensure data integrity of the upload.  ### Status caching Due to current system limitations, data for the &#x60;/uploads/report&#x60; endpoint is cached for one hour.  A request to the &#x60;/uploads/{id}&#x60; endpoint will return a real-time status for that GUID, and update its status in &#x60;/uploads/report&#x60;.  The &#x60;updated_at&#x60; field indicates the last time the status for a given GUID was updated.  ### Document Submission Statuses **Important note:** a submission has not been received by VA until it has a status of Received, Processing, Success,  or VBMS. Detailed descriptions of what each status means are found in this table.  | Status        | What it means | | ---           |     ---     | | **Pending**   | Initial status.&lt;br /&gt;&lt;br /&gt;Indicates no document package has been uploaded yet.&lt;br /&gt;&lt;br /&gt;Date of Receipt is not yet established with this status | | **Uploaded**  | Indicates document package has been successfully uploaded (PUT) from your system to the API server but has not yet been validated.&lt;br /&gt;&lt;br /&gt;Date of Receipt is not yet established with this status. Any errors with the document package, such as having an unreadable PDF, may cause an Error status. | | **Received**  | Indicates document package has been received upstream of the API and is awaiting Processing.&lt;br /&gt;&lt;br /&gt;The VA Date of Receipt is set when this status is achieved.&lt;br /&gt;&lt;br /&gt;This is the final status in the sandbox environment unless further progress is simulated. | | **Processing**| Indicates the document package is being validated, processed, and made ready to route and work. | | **Success**   | Indicates the document package has been successfully received within VA&#39;s mail handling system.&lt;br /&gt;&lt;br /&gt;Success is the final status for a small percentage of submitted packages with claim types, Veteran types, or exception processes that are not worked in VBMS. Most submissions reach a Success status within 1 business day. A small portion will take longer; however, some submissions may take up to 2 weeks to reach a Success status. | | **VBMS**      | Indicates this document package was successfully uploaded into a Veteran&#39;s eFolder within VBMS.&lt;br /&gt;&lt;br /&gt;On average, submissions reach VBMS status within 3 business days; however, processing times vary and some submissions may remain in a Success status for several weeks before reaching a VBMS status.&lt;br /&gt;&lt;br /&gt;Some document packages are worked in VA systems other than VBMS. For these submissions, Success is the final status. | | **Error**     | Indicates that there was an error. Refer to the error code and message for further information. | | **Expired**   | After a POST request, there is a 15-minute window during which documents must be uploaded via a PUT request.&lt;br /&gt;&lt;br /&gt;An Expired status means the documents were not successfully uploaded within this 15-minute window. We recommend coding to retry unsuccessful uploads within 15 minutes using the same submission in case of connection issues. |  ### Optional Base64 encoding  Base64 is an encoding scheme that converts binary data into text format, so that encoded textual data can be easily transported over networks uncorrupted and without data loss.   Base64 can be used to encode binary multipart/form-data it in its entirety.  Note that the whole payload must be encoded, not individual parts/attachments.  After encoding your payload, you&#39;ll be required to preface your base64 string with &#x60;data:multipart/form-data;base64,&#x60; in order to allow our system to distinguish the file type. Your final string payload would look something like &#x60;data:multipart/form-data;base64,(encryption string)&#x3D;&#x3D;&#x60; and close with the standard &#x3D;&#x3D; marker.  Note that the multipart boundaries i.e. -----WebKitFormBoundaryVfOwzCyvug0JmWYo and ending ------WebKitFormBoundaryVfOwzCyvug0JmWYo- must also be included.  ### Consumer onboarding process When you&#39;re ready to move to production, [request a production API key.](https://developer.va.gov/go-live) .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var BenefitsIntake = require('index'); // See note below*.
* var xxxSvc = new BenefitsIntake.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new BenefitsIntake.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new BenefitsIntake.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new BenefitsIntake.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The DocumentUploadAttributes model constructor.
     * @property {module:model/DocumentUploadAttributes}
     */
    DocumentUploadAttributes,

    /**
     * The DocumentUploadFailure model constructor.
     * @property {module:model/DocumentUploadFailure}
     */
    DocumentUploadFailure,

    /**
     * The DocumentUploadMetadata model constructor.
     * @property {module:model/DocumentUploadMetadata}
     */
    DocumentUploadMetadata,

    /**
     * The DocumentUploadPath model constructor.
     * @property {module:model/DocumentUploadPath}
     */
    DocumentUploadPath,

    /**
     * The DocumentUploadStatus model constructor.
     * @property {module:model/DocumentUploadStatus}
     */
    DocumentUploadStatus,

    /**
     * The DocumentUploadStatusAttributes model constructor.
     * @property {module:model/DocumentUploadStatusAttributes}
     */
    DocumentUploadStatusAttributes,

    /**
     * The DocumentUploadStatusGuidList model constructor.
     * @property {module:model/DocumentUploadStatusGuidList}
     */
    DocumentUploadStatusGuidList,

    /**
     * The DocumentUploadSubmission model constructor.
     * @property {module:model/DocumentUploadSubmission}
     */
    DocumentUploadSubmission,

    /**
     * The DocumentUploadSubmissionAttributes model constructor.
     * @property {module:model/DocumentUploadSubmissionAttributes}
     */
    DocumentUploadSubmissionAttributes,

    /**
     * The DocumentValidationErrorModel model constructor.
     * @property {module:model/DocumentValidationErrorModel}
     */
    DocumentValidationErrorModel,

    /**
     * The ErrorModel model constructor.
     * @property {module:model/ErrorModel}
     */
    ErrorModel,

    /**
     * The GetBenefitsDocumentUploadStatus200Response model constructor.
     * @property {module:model/GetBenefitsDocumentUploadStatus200Response}
     */
    GetBenefitsDocumentUploadStatus200Response,

    /**
     * The GetBenefitsDocumentUploadStatus404Response model constructor.
     * @property {module:model/GetBenefitsDocumentUploadStatus404Response}
     */
    GetBenefitsDocumentUploadStatus404Response,

    /**
     * The GetBenefitsDocumentUploadStatusReport200Response model constructor.
     * @property {module:model/GetBenefitsDocumentUploadStatusReport200Response}
     */
    GetBenefitsDocumentUploadStatusReport200Response,

    /**
     * The PdfDimensionAttributes model constructor.
     * @property {module:model/PdfDimensionAttributes}
     */
    PdfDimensionAttributes,

    /**
     * The PdfUploadAttributes model constructor.
     * @property {module:model/PdfUploadAttributes}
     */
    PdfUploadAttributes,

    /**
     * The PdfUploadAttributesContent model constructor.
     * @property {module:model/PdfUploadAttributesContent}
     */
    PdfUploadAttributesContent,

    /**
     * The PdfUploadAttributesContentAttachmentsInner model constructor.
     * @property {module:model/PdfUploadAttributesContentAttachmentsInner}
     */
    PdfUploadAttributesContentAttachmentsInner,

    /**
     * The PostBenefitsDocumentUpload202Response model constructor.
     * @property {module:model/PostBenefitsDocumentUpload202Response}
     */
    PostBenefitsDocumentUpload202Response,

    /**
     * The PostBenefitsDocumentUpload403Response model constructor.
     * @property {module:model/PostBenefitsDocumentUpload403Response}
     */
    PostBenefitsDocumentUpload403Response,

    /**
     * The PostBenefitsDocumentUploadValidateDocument200Response model constructor.
     * @property {module:model/PostBenefitsDocumentUploadValidateDocument200Response}
     */
    PostBenefitsDocumentUploadValidateDocument200Response,

    /**
     * The PostBenefitsDocumentUploadValidateDocument200ResponseData model constructor.
     * @property {module:model/PostBenefitsDocumentUploadValidateDocument200ResponseData}
     */
    PostBenefitsDocumentUploadValidateDocument200ResponseData,

    /**
     * The PostBenefitsDocumentUploadValidateDocument200ResponseDataAttributes model constructor.
     * @property {module:model/PostBenefitsDocumentUploadValidateDocument200ResponseDataAttributes}
     */
    PostBenefitsDocumentUploadValidateDocument200ResponseDataAttributes,

    /**
     * The PostBenefitsDocumentUploadValidateDocument422Response model constructor.
     * @property {module:model/PostBenefitsDocumentUploadValidateDocument422Response}
     */
    PostBenefitsDocumentUploadValidateDocument422Response,

    /**
     * The PutBenefitsDocumentUpload401Response model constructor.
     * @property {module:model/PutBenefitsDocumentUpload401Response}
     */
    PutBenefitsDocumentUpload401Response,

    /**
     * The PutBenefitsDocumentUpload422Response model constructor.
     * @property {module:model/PutBenefitsDocumentUpload422Response}
     */
    PutBenefitsDocumentUpload422Response,

    /**
     * The PutBenefitsDocumentUpload429Response model constructor.
     * @property {module:model/PutBenefitsDocumentUpload429Response}
     */
    PutBenefitsDocumentUpload429Response,

    /**
     * The PutBenefitsDocumentUpload500Response model constructor.
     * @property {module:model/PutBenefitsDocumentUpload500Response}
     */
    PutBenefitsDocumentUpload500Response,

    /**
    * The VBADocumentsApi service constructor.
    * @property {module:api/VBADocumentsApi}
    */
    VBADocumentsApi
};
