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


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.UUID;
import org.openapitools.client.model.PdfUploadAttributes;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * DocumentUploadStatusAttributes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:24.906659-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DocumentUploadStatusAttributes {
  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_DETAIL = "detail";
  @SerializedName(SERIALIZED_NAME_DETAIL)
  private String detail;

  public static final String SERIALIZED_NAME_GUID = "guid";
  @SerializedName(SERIALIZED_NAME_GUID)
  private UUID guid;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  /**
   * Document upload status. 
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    PENDING("pending"),
    
    UPLOADED("uploaded"),
    
    RECEIVED("received"),
    
    PROCESSING("processing"),
    
    SUCCESS("success"),
    
    VBMS("vbms"),
    
    ERROR("error");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_UPLOADED_PDF = "uploaded_pdf";
  @SerializedName(SERIALIZED_NAME_UPLOADED_PDF)
  private PdfUploadAttributes uploadedPdf;

  public DocumentUploadStatusAttributes() {
  }

  public DocumentUploadStatusAttributes code(String code) {
    this.code = code;
    return this;
  }

  /**
   * Unambiguous status code. Only present if status &#x3D; \&quot;error\&quot;  * &#x60;DOC101&#x60; - Invalid multipart payload provided - not a multipart, or missing one or more required parts. * &#x60;DOC102&#x60; - Invalid metadata - not parseable as JSON, incorrect fields, etc. * &#x60;DOC103&#x60; - Invalid content - not parseable as PDF. Detail field will indicate which document or attachment part was affected. * &#x60;DOC104&#x60; - Upload rejected by upstream system. Processing failed and upload must be resubmitted. Detail field will indicate nature of rejection. * &#x60;DOC105&#x60; - Invalid or unknown id * &#x60;DOC106&#x60; - File size limit exceeded. Each document may be a maximum of 100MB. * &#x60;DOC107&#x60; - Empty payload. * &#x60;DOC108&#x60; - Maximum dimensions exceeded. Height and width must be less than 21 in x 21 in. * &#x60;DOC201&#x60; - Upload server error. * &#x60;DOC202&#x60; - Error during processing by upstream system. Processing failed and upload must be resubmitted. Detail field will provide additional details where available. 
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public DocumentUploadStatusAttributes detail(String detail) {
    this.detail = detail;
    return this;
  }

  /**
   * Human readable error detail. Only present if status &#x3D; \&quot;error\&quot;
   * @return detail
   */
  @javax.annotation.Nullable
  public String getDetail() {
    return detail;
  }

  public void setDetail(String detail) {
    this.detail = detail;
  }


  public DocumentUploadStatusAttributes guid(UUID guid) {
    this.guid = guid;
    return this;
  }

  /**
   * The document upload identifier
   * @return guid
   */
  @javax.annotation.Nonnull
  public UUID getGuid() {
    return guid;
  }

  public void setGuid(UUID guid) {
    this.guid = guid;
  }


  public DocumentUploadStatusAttributes message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Human readable error description. Only present if status &#x3D; \&quot;error\&quot;
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  public DocumentUploadStatusAttributes status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Document upload status. 
   * @return status
   */
  @javax.annotation.Nonnull
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public DocumentUploadStatusAttributes updatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * The last time the submission was updated
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
  }


  public DocumentUploadStatusAttributes uploadedPdf(PdfUploadAttributes uploadedPdf) {
    this.uploadedPdf = uploadedPdf;
    return this;
  }

  /**
   * Get uploadedPdf
   * @return uploadedPdf
   */
  @javax.annotation.Nullable
  public PdfUploadAttributes getUploadedPdf() {
    return uploadedPdf;
  }

  public void setUploadedPdf(PdfUploadAttributes uploadedPdf) {
    this.uploadedPdf = uploadedPdf;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DocumentUploadStatusAttributes documentUploadStatusAttributes = (DocumentUploadStatusAttributes) o;
    return Objects.equals(this.code, documentUploadStatusAttributes.code) &&
        Objects.equals(this.detail, documentUploadStatusAttributes.detail) &&
        Objects.equals(this.guid, documentUploadStatusAttributes.guid) &&
        Objects.equals(this.message, documentUploadStatusAttributes.message) &&
        Objects.equals(this.status, documentUploadStatusAttributes.status) &&
        Objects.equals(this.updatedAt, documentUploadStatusAttributes.updatedAt) &&
        Objects.equals(this.uploadedPdf, documentUploadStatusAttributes.uploadedPdf);
  }

  @Override
  public int hashCode() {
    return Objects.hash(code, detail, guid, message, status, updatedAt, uploadedPdf);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DocumentUploadStatusAttributes {\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    detail: ").append(toIndentedString(detail)).append("\n");
    sb.append("    guid: ").append(toIndentedString(guid)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    uploadedPdf: ").append(toIndentedString(uploadedPdf)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("code");
    openapiFields.add("detail");
    openapiFields.add("guid");
    openapiFields.add("message");
    openapiFields.add("status");
    openapiFields.add("updated_at");
    openapiFields.add("uploaded_pdf");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("guid");
    openapiRequiredFields.add("status");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DocumentUploadStatusAttributes
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DocumentUploadStatusAttributes.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DocumentUploadStatusAttributes is not found in the empty JSON string", DocumentUploadStatusAttributes.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DocumentUploadStatusAttributes.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DocumentUploadStatusAttributes` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DocumentUploadStatusAttributes.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if ((jsonObj.get("detail") != null && !jsonObj.get("detail").isJsonNull()) && !jsonObj.get("detail").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `detail` to be a primitive type in the JSON string but got `%s`", jsonObj.get("detail").toString()));
      }
      if (!jsonObj.get("guid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `guid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("guid").toString()));
      }
      if ((jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) && !jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the required field `status`
      StatusEnum.validateJsonElement(jsonObj.get("status"));
      // validate the optional field `uploaded_pdf`
      if (jsonObj.get("uploaded_pdf") != null && !jsonObj.get("uploaded_pdf").isJsonNull()) {
        PdfUploadAttributes.validateJsonElement(jsonObj.get("uploaded_pdf"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DocumentUploadStatusAttributes.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DocumentUploadStatusAttributes' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DocumentUploadStatusAttributes> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DocumentUploadStatusAttributes.class));

       return (TypeAdapter<T>) new TypeAdapter<DocumentUploadStatusAttributes>() {
           @Override
           public void write(JsonWriter out, DocumentUploadStatusAttributes value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DocumentUploadStatusAttributes read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DocumentUploadStatusAttributes given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DocumentUploadStatusAttributes
   * @throws IOException if the JSON string is invalid with respect to DocumentUploadStatusAttributes
   */
  public static DocumentUploadStatusAttributes fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DocumentUploadStatusAttributes.class);
  }

  /**
   * Convert an instance of DocumentUploadStatusAttributes to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

