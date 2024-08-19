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
import java.util.Arrays;

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
 * Identifying properties about the document payload being submitted
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:24.906659-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DocumentUploadMetadata {
  /**
   * Optional parameter (can be missing or empty). The values are:&lt;br&gt;&lt;br&gt; CMP - Compensation requests such as those related to disability, unemployment, and pandemic claims&lt;br&gt;&lt;br&gt; PMC - Pension requests including survivor’s pension&lt;br&gt;&lt;br&gt; INS - Insurance such as life insurance, disability insurance, and other health insurance&lt;br&gt;&lt;br&gt; EDU - Education benefits, programs, and affiliations&lt;br&gt;&lt;br&gt; VRE - Veteran Readiness &amp; Employment such as employment questionnaires, employment discrimination, employment verification&lt;br&gt;&lt;br&gt; BVA - Board of Veteran Appeals&lt;br&gt;&lt;br&gt; FID - Fiduciary / financial appointee, including family member benefits&lt;br&gt;&lt;br&gt; NCA - National Cemetery Administration&lt;br&gt;&lt;br&gt; OTH - Other (this value if used, will be treated as CMP)&lt;br&gt; 
   */
  @JsonAdapter(BusinessLineEnum.Adapter.class)
  public enum BusinessLineEnum {
    CMP("CMP"),
    
    PMC("PMC"),
    
    INS("INS"),
    
    EDU("EDU"),
    
    VRE("VRE"),
    
    BVA("BVA"),
    
    FID("FID"),
    
    NCA("NCA"),
    
    OTH("OTH");

    private String value;

    BusinessLineEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static BusinessLineEnum fromValue(String value) {
      for (BusinessLineEnum b : BusinessLineEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<BusinessLineEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final BusinessLineEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public BusinessLineEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return BusinessLineEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      BusinessLineEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_BUSINESS_LINE = "businessLine";
  @SerializedName(SERIALIZED_NAME_BUSINESS_LINE)
  private BusinessLineEnum businessLine;

  public static final String SERIALIZED_NAME_DOC_TYPE = "docType";
  @SerializedName(SERIALIZED_NAME_DOC_TYPE)
  private String docType;

  public static final String SERIALIZED_NAME_FILE_NUMBER = "fileNumber";
  @SerializedName(SERIALIZED_NAME_FILE_NUMBER)
  private String fileNumber;

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private String source;

  public static final String SERIALIZED_NAME_VETERAN_FIRST_NAME = "veteranFirstName";
  @SerializedName(SERIALIZED_NAME_VETERAN_FIRST_NAME)
  private String veteranFirstName;

  public static final String SERIALIZED_NAME_VETERAN_LAST_NAME = "veteranLastName";
  @SerializedName(SERIALIZED_NAME_VETERAN_LAST_NAME)
  private String veteranLastName;

  public static final String SERIALIZED_NAME_ZIP_CODE = "zipCode";
  @SerializedName(SERIALIZED_NAME_ZIP_CODE)
  private String zipCode;

  public DocumentUploadMetadata() {
  }

  public DocumentUploadMetadata businessLine(BusinessLineEnum businessLine) {
    this.businessLine = businessLine;
    return this;
  }

  /**
   * Optional parameter (can be missing or empty). The values are:&lt;br&gt;&lt;br&gt; CMP - Compensation requests such as those related to disability, unemployment, and pandemic claims&lt;br&gt;&lt;br&gt; PMC - Pension requests including survivor’s pension&lt;br&gt;&lt;br&gt; INS - Insurance such as life insurance, disability insurance, and other health insurance&lt;br&gt;&lt;br&gt; EDU - Education benefits, programs, and affiliations&lt;br&gt;&lt;br&gt; VRE - Veteran Readiness &amp; Employment such as employment questionnaires, employment discrimination, employment verification&lt;br&gt;&lt;br&gt; BVA - Board of Veteran Appeals&lt;br&gt;&lt;br&gt; FID - Fiduciary / financial appointee, including family member benefits&lt;br&gt;&lt;br&gt; NCA - National Cemetery Administration&lt;br&gt;&lt;br&gt; OTH - Other (this value if used, will be treated as CMP)&lt;br&gt; 
   * @return businessLine
   */
  @javax.annotation.Nullable
  public BusinessLineEnum getBusinessLine() {
    return businessLine;
  }

  public void setBusinessLine(BusinessLineEnum businessLine) {
    this.businessLine = businessLine;
  }


  public DocumentUploadMetadata docType(String docType) {
    this.docType = docType;
    return this;
  }

  /**
   * VBA form number of the document
   * @return docType
   */
  @javax.annotation.Nullable
  public String getDocType() {
    return docType;
  }

  public void setDocType(String docType) {
    this.docType = docType;
  }


  public DocumentUploadMetadata fileNumber(String fileNumber) {
    this.fileNumber = fileNumber;
    return this;
  }

  /**
   * The Veteran&#39;s file number is exactly 9 digits with no alpha characters, hyphens, spaces or punctuation. In most cases, this is the Veteran&#39;s SSN but may also be an 8 digit BIRL number. If no file number has been established or if it is unknown, the application should use the Veteran&#39;s SSN and the file number will be associated with the submission later in the process. Incorrect file numbers can cause delays.
   * @return fileNumber
   */
  @javax.annotation.Nonnull
  public String getFileNumber() {
    return fileNumber;
  }

  public void setFileNumber(String fileNumber) {
    this.fileNumber = fileNumber;
  }


  public DocumentUploadMetadata source(String source) {
    this.source = source;
    return this;
  }

  /**
   * System, installation, or entity submitting the document
   * @return source
   */
  @javax.annotation.Nonnull
  public String getSource() {
    return source;
  }

  public void setSource(String source) {
    this.source = source;
  }


  public DocumentUploadMetadata veteranFirstName(String veteranFirstName) {
    this.veteranFirstName = veteranFirstName;
    return this;
  }

  /**
   * Veteran first name. Cannot be missing or empty or longer than 50 characters. Only upper/lower case letters, hyphens(-), spaces and forward-slash(/) allowed.
   * @return veteranFirstName
   */
  @javax.annotation.Nonnull
  public String getVeteranFirstName() {
    return veteranFirstName;
  }

  public void setVeteranFirstName(String veteranFirstName) {
    this.veteranFirstName = veteranFirstName;
  }


  public DocumentUploadMetadata veteranLastName(String veteranLastName) {
    this.veteranLastName = veteranLastName;
    return this;
  }

  /**
   * Veteran last name. Cannot be missing or empty or longer than 50 characters. Only upper/lower case letters, hyphens(-), spaces and forward-slash(/) allowed.
   * @return veteranLastName
   */
  @javax.annotation.Nonnull
  public String getVeteranLastName() {
    return veteranLastName;
  }

  public void setVeteranLastName(String veteranLastName) {
    this.veteranLastName = veteranLastName;
  }


  public DocumentUploadMetadata zipCode(String zipCode) {
    this.zipCode = zipCode;
    return this;
  }

  /**
   * Veteran zip code. Either five digits (XXXXX) or five digits then four digits separated by a hyphen (XXXXX-XXXX). Use &#39;00000&#39; for Veterans with non-US addresses.
   * @return zipCode
   */
  @javax.annotation.Nonnull
  public String getZipCode() {
    return zipCode;
  }

  public void setZipCode(String zipCode) {
    this.zipCode = zipCode;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DocumentUploadMetadata documentUploadMetadata = (DocumentUploadMetadata) o;
    return Objects.equals(this.businessLine, documentUploadMetadata.businessLine) &&
        Objects.equals(this.docType, documentUploadMetadata.docType) &&
        Objects.equals(this.fileNumber, documentUploadMetadata.fileNumber) &&
        Objects.equals(this.source, documentUploadMetadata.source) &&
        Objects.equals(this.veteranFirstName, documentUploadMetadata.veteranFirstName) &&
        Objects.equals(this.veteranLastName, documentUploadMetadata.veteranLastName) &&
        Objects.equals(this.zipCode, documentUploadMetadata.zipCode);
  }

  @Override
  public int hashCode() {
    return Objects.hash(businessLine, docType, fileNumber, source, veteranFirstName, veteranLastName, zipCode);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DocumentUploadMetadata {\n");
    sb.append("    businessLine: ").append(toIndentedString(businessLine)).append("\n");
    sb.append("    docType: ").append(toIndentedString(docType)).append("\n");
    sb.append("    fileNumber: ").append(toIndentedString(fileNumber)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    veteranFirstName: ").append(toIndentedString(veteranFirstName)).append("\n");
    sb.append("    veteranLastName: ").append(toIndentedString(veteranLastName)).append("\n");
    sb.append("    zipCode: ").append(toIndentedString(zipCode)).append("\n");
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
    openapiFields.add("businessLine");
    openapiFields.add("docType");
    openapiFields.add("fileNumber");
    openapiFields.add("source");
    openapiFields.add("veteranFirstName");
    openapiFields.add("veteranLastName");
    openapiFields.add("zipCode");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("fileNumber");
    openapiRequiredFields.add("source");
    openapiRequiredFields.add("veteranFirstName");
    openapiRequiredFields.add("veteranLastName");
    openapiRequiredFields.add("zipCode");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DocumentUploadMetadata
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DocumentUploadMetadata.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DocumentUploadMetadata is not found in the empty JSON string", DocumentUploadMetadata.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DocumentUploadMetadata.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DocumentUploadMetadata` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DocumentUploadMetadata.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("businessLine") != null && !jsonObj.get("businessLine").isJsonNull()) && !jsonObj.get("businessLine").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `businessLine` to be a primitive type in the JSON string but got `%s`", jsonObj.get("businessLine").toString()));
      }
      // validate the optional field `businessLine`
      if (jsonObj.get("businessLine") != null && !jsonObj.get("businessLine").isJsonNull()) {
        BusinessLineEnum.validateJsonElement(jsonObj.get("businessLine"));
      }
      if ((jsonObj.get("docType") != null && !jsonObj.get("docType").isJsonNull()) && !jsonObj.get("docType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `docType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("docType").toString()));
      }
      if (!jsonObj.get("fileNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fileNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fileNumber").toString()));
      }
      if (!jsonObj.get("source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source").toString()));
      }
      if (!jsonObj.get("veteranFirstName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `veteranFirstName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("veteranFirstName").toString()));
      }
      if (!jsonObj.get("veteranLastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `veteranLastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("veteranLastName").toString()));
      }
      if (!jsonObj.get("zipCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `zipCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("zipCode").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DocumentUploadMetadata.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DocumentUploadMetadata' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DocumentUploadMetadata> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DocumentUploadMetadata.class));

       return (TypeAdapter<T>) new TypeAdapter<DocumentUploadMetadata>() {
           @Override
           public void write(JsonWriter out, DocumentUploadMetadata value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DocumentUploadMetadata read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DocumentUploadMetadata given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DocumentUploadMetadata
   * @throws IOException if the JSON string is invalid with respect to DocumentUploadMetadata
   */
  public static DocumentUploadMetadata fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DocumentUploadMetadata.class);
  }

  /**
   * Convert an instance of DocumentUploadMetadata to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

