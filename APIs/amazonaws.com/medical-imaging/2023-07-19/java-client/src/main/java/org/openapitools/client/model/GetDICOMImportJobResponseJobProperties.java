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
import org.openapitools.client.model.JobStatus;

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
 * GetDICOMImportJobResponseJobProperties
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:28:55.616958-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetDICOMImportJobResponseJobProperties {
  public static final String SERIALIZED_NAME_JOB_ID = "jobId";
  @SerializedName(SERIALIZED_NAME_JOB_ID)
  private String jobId;

  public static final String SERIALIZED_NAME_JOB_NAME = "jobName";
  @SerializedName(SERIALIZED_NAME_JOB_NAME)
  private String jobName;

  public static final String SERIALIZED_NAME_JOB_STATUS = "jobStatus";
  @SerializedName(SERIALIZED_NAME_JOB_STATUS)
  private JobStatus jobStatus;

  public static final String SERIALIZED_NAME_DATASTORE_ID = "datastoreId";
  @SerializedName(SERIALIZED_NAME_DATASTORE_ID)
  private String datastoreId;

  public static final String SERIALIZED_NAME_DATA_ACCESS_ROLE_ARN = "dataAccessRoleArn";
  @SerializedName(SERIALIZED_NAME_DATA_ACCESS_ROLE_ARN)
  private String dataAccessRoleArn;

  public static final String SERIALIZED_NAME_ENDED_AT = "endedAt";
  @SerializedName(SERIALIZED_NAME_ENDED_AT)
  private OffsetDateTime endedAt;

  public static final String SERIALIZED_NAME_SUBMITTED_AT = "submittedAt";
  @SerializedName(SERIALIZED_NAME_SUBMITTED_AT)
  private OffsetDateTime submittedAt;

  public static final String SERIALIZED_NAME_INPUT_S3_URI = "inputS3Uri";
  @SerializedName(SERIALIZED_NAME_INPUT_S3_URI)
  private String inputS3Uri;

  public static final String SERIALIZED_NAME_OUTPUT_S3_URI = "outputS3Uri";
  @SerializedName(SERIALIZED_NAME_OUTPUT_S3_URI)
  private String outputS3Uri;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public GetDICOMImportJobResponseJobProperties() {
  }

  public GetDICOMImportJobResponseJobProperties jobId(String jobId) {
    this.jobId = jobId;
    return this;
  }

  /**
   * Get jobId
   * @return jobId
   */
  @javax.annotation.Nonnull
  public String getJobId() {
    return jobId;
  }

  public void setJobId(String jobId) {
    this.jobId = jobId;
  }


  public GetDICOMImportJobResponseJobProperties jobName(String jobName) {
    this.jobName = jobName;
    return this;
  }

  /**
   * Get jobName
   * @return jobName
   */
  @javax.annotation.Nonnull
  public String getJobName() {
    return jobName;
  }

  public void setJobName(String jobName) {
    this.jobName = jobName;
  }


  public GetDICOMImportJobResponseJobProperties jobStatus(JobStatus jobStatus) {
    this.jobStatus = jobStatus;
    return this;
  }

  /**
   * Get jobStatus
   * @return jobStatus
   */
  @javax.annotation.Nonnull
  public JobStatus getJobStatus() {
    return jobStatus;
  }

  public void setJobStatus(JobStatus jobStatus) {
    this.jobStatus = jobStatus;
  }


  public GetDICOMImportJobResponseJobProperties datastoreId(String datastoreId) {
    this.datastoreId = datastoreId;
    return this;
  }

  /**
   * Get datastoreId
   * @return datastoreId
   */
  @javax.annotation.Nonnull
  public String getDatastoreId() {
    return datastoreId;
  }

  public void setDatastoreId(String datastoreId) {
    this.datastoreId = datastoreId;
  }


  public GetDICOMImportJobResponseJobProperties dataAccessRoleArn(String dataAccessRoleArn) {
    this.dataAccessRoleArn = dataAccessRoleArn;
    return this;
  }

  /**
   * Get dataAccessRoleArn
   * @return dataAccessRoleArn
   */
  @javax.annotation.Nonnull
  public String getDataAccessRoleArn() {
    return dataAccessRoleArn;
  }

  public void setDataAccessRoleArn(String dataAccessRoleArn) {
    this.dataAccessRoleArn = dataAccessRoleArn;
  }


  public GetDICOMImportJobResponseJobProperties endedAt(OffsetDateTime endedAt) {
    this.endedAt = endedAt;
    return this;
  }

  /**
   * Get endedAt
   * @return endedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEndedAt() {
    return endedAt;
  }

  public void setEndedAt(OffsetDateTime endedAt) {
    this.endedAt = endedAt;
  }


  public GetDICOMImportJobResponseJobProperties submittedAt(OffsetDateTime submittedAt) {
    this.submittedAt = submittedAt;
    return this;
  }

  /**
   * Get submittedAt
   * @return submittedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getSubmittedAt() {
    return submittedAt;
  }

  public void setSubmittedAt(OffsetDateTime submittedAt) {
    this.submittedAt = submittedAt;
  }


  public GetDICOMImportJobResponseJobProperties inputS3Uri(String inputS3Uri) {
    this.inputS3Uri = inputS3Uri;
    return this;
  }

  /**
   * Get inputS3Uri
   * @return inputS3Uri
   */
  @javax.annotation.Nonnull
  public String getInputS3Uri() {
    return inputS3Uri;
  }

  public void setInputS3Uri(String inputS3Uri) {
    this.inputS3Uri = inputS3Uri;
  }


  public GetDICOMImportJobResponseJobProperties outputS3Uri(String outputS3Uri) {
    this.outputS3Uri = outputS3Uri;
    return this;
  }

  /**
   * Get outputS3Uri
   * @return outputS3Uri
   */
  @javax.annotation.Nonnull
  public String getOutputS3Uri() {
    return outputS3Uri;
  }

  public void setOutputS3Uri(String outputS3Uri) {
    this.outputS3Uri = outputS3Uri;
  }


  public GetDICOMImportJobResponseJobProperties message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Get message
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetDICOMImportJobResponseJobProperties getDICOMImportJobResponseJobProperties = (GetDICOMImportJobResponseJobProperties) o;
    return Objects.equals(this.jobId, getDICOMImportJobResponseJobProperties.jobId) &&
        Objects.equals(this.jobName, getDICOMImportJobResponseJobProperties.jobName) &&
        Objects.equals(this.jobStatus, getDICOMImportJobResponseJobProperties.jobStatus) &&
        Objects.equals(this.datastoreId, getDICOMImportJobResponseJobProperties.datastoreId) &&
        Objects.equals(this.dataAccessRoleArn, getDICOMImportJobResponseJobProperties.dataAccessRoleArn) &&
        Objects.equals(this.endedAt, getDICOMImportJobResponseJobProperties.endedAt) &&
        Objects.equals(this.submittedAt, getDICOMImportJobResponseJobProperties.submittedAt) &&
        Objects.equals(this.inputS3Uri, getDICOMImportJobResponseJobProperties.inputS3Uri) &&
        Objects.equals(this.outputS3Uri, getDICOMImportJobResponseJobProperties.outputS3Uri) &&
        Objects.equals(this.message, getDICOMImportJobResponseJobProperties.message);
  }

  @Override
  public int hashCode() {
    return Objects.hash(jobId, jobName, jobStatus, datastoreId, dataAccessRoleArn, endedAt, submittedAt, inputS3Uri, outputS3Uri, message);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetDICOMImportJobResponseJobProperties {\n");
    sb.append("    jobId: ").append(toIndentedString(jobId)).append("\n");
    sb.append("    jobName: ").append(toIndentedString(jobName)).append("\n");
    sb.append("    jobStatus: ").append(toIndentedString(jobStatus)).append("\n");
    sb.append("    datastoreId: ").append(toIndentedString(datastoreId)).append("\n");
    sb.append("    dataAccessRoleArn: ").append(toIndentedString(dataAccessRoleArn)).append("\n");
    sb.append("    endedAt: ").append(toIndentedString(endedAt)).append("\n");
    sb.append("    submittedAt: ").append(toIndentedString(submittedAt)).append("\n");
    sb.append("    inputS3Uri: ").append(toIndentedString(inputS3Uri)).append("\n");
    sb.append("    outputS3Uri: ").append(toIndentedString(outputS3Uri)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
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
    openapiFields.add("jobId");
    openapiFields.add("jobName");
    openapiFields.add("jobStatus");
    openapiFields.add("datastoreId");
    openapiFields.add("dataAccessRoleArn");
    openapiFields.add("endedAt");
    openapiFields.add("submittedAt");
    openapiFields.add("inputS3Uri");
    openapiFields.add("outputS3Uri");
    openapiFields.add("message");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("jobId");
    openapiRequiredFields.add("jobName");
    openapiRequiredFields.add("jobStatus");
    openapiRequiredFields.add("datastoreId");
    openapiRequiredFields.add("dataAccessRoleArn");
    openapiRequiredFields.add("inputS3Uri");
    openapiRequiredFields.add("outputS3Uri");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetDICOMImportJobResponseJobProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetDICOMImportJobResponseJobProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetDICOMImportJobResponseJobProperties is not found in the empty JSON string", GetDICOMImportJobResponseJobProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetDICOMImportJobResponseJobProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetDICOMImportJobResponseJobProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GetDICOMImportJobResponseJobProperties.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `jobId`
      String.validateJsonElement(jsonObj.get("jobId"));
      // validate the required field `jobName`
      String.validateJsonElement(jsonObj.get("jobName"));
      // validate the required field `jobStatus`
      JobStatus.validateJsonElement(jsonObj.get("jobStatus"));
      // validate the required field `datastoreId`
      String.validateJsonElement(jsonObj.get("datastoreId"));
      // validate the required field `dataAccessRoleArn`
      String.validateJsonElement(jsonObj.get("dataAccessRoleArn"));
      // validate the optional field `endedAt`
      if (jsonObj.get("endedAt") != null && !jsonObj.get("endedAt").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("endedAt"));
      }
      // validate the optional field `submittedAt`
      if (jsonObj.get("submittedAt") != null && !jsonObj.get("submittedAt").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("submittedAt"));
      }
      // validate the required field `inputS3Uri`
      String.validateJsonElement(jsonObj.get("inputS3Uri"));
      // validate the required field `outputS3Uri`
      String.validateJsonElement(jsonObj.get("outputS3Uri"));
      // validate the optional field `message`
      if (jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("message"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetDICOMImportJobResponseJobProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetDICOMImportJobResponseJobProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetDICOMImportJobResponseJobProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetDICOMImportJobResponseJobProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<GetDICOMImportJobResponseJobProperties>() {
           @Override
           public void write(JsonWriter out, GetDICOMImportJobResponseJobProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetDICOMImportJobResponseJobProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetDICOMImportJobResponseJobProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetDICOMImportJobResponseJobProperties
   * @throws IOException if the JSON string is invalid with respect to GetDICOMImportJobResponseJobProperties
   */
  public static GetDICOMImportJobResponseJobProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetDICOMImportJobResponseJobProperties.class);
  }

  /**
   * Convert an instance of GetDICOMImportJobResponseJobProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

