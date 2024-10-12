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
 * StartDICOMImportJobRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:28:55.616958-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class StartDICOMImportJobRequest {
  public static final String SERIALIZED_NAME_JOB_NAME = "jobName";
  @SerializedName(SERIALIZED_NAME_JOB_NAME)
  private String jobName;

  public static final String SERIALIZED_NAME_DATA_ACCESS_ROLE_ARN = "dataAccessRoleArn";
  @SerializedName(SERIALIZED_NAME_DATA_ACCESS_ROLE_ARN)
  private String dataAccessRoleArn;

  public static final String SERIALIZED_NAME_CLIENT_TOKEN = "clientToken";
  @SerializedName(SERIALIZED_NAME_CLIENT_TOKEN)
  private String clientToken;

  public static final String SERIALIZED_NAME_INPUT_S3_URI = "inputS3Uri";
  @SerializedName(SERIALIZED_NAME_INPUT_S3_URI)
  private String inputS3Uri;

  public static final String SERIALIZED_NAME_OUTPUT_S3_URI = "outputS3Uri";
  @SerializedName(SERIALIZED_NAME_OUTPUT_S3_URI)
  private String outputS3Uri;

  public StartDICOMImportJobRequest() {
  }

  public StartDICOMImportJobRequest jobName(String jobName) {
    this.jobName = jobName;
    return this;
  }

  /**
   * The import job name.
   * @return jobName
   */
  @javax.annotation.Nullable
  public String getJobName() {
    return jobName;
  }

  public void setJobName(String jobName) {
    this.jobName = jobName;
  }


  public StartDICOMImportJobRequest dataAccessRoleArn(String dataAccessRoleArn) {
    this.dataAccessRoleArn = dataAccessRoleArn;
    return this;
  }

  /**
   * The Amazon Resource Name (ARN) of the IAM role that grants permission to access medical imaging resources.
   * @return dataAccessRoleArn
   */
  @javax.annotation.Nonnull
  public String getDataAccessRoleArn() {
    return dataAccessRoleArn;
  }

  public void setDataAccessRoleArn(String dataAccessRoleArn) {
    this.dataAccessRoleArn = dataAccessRoleArn;
  }


  public StartDICOMImportJobRequest clientToken(String clientToken) {
    this.clientToken = clientToken;
    return this;
  }

  /**
   * A unique identifier for API idempotency.
   * @return clientToken
   */
  @javax.annotation.Nonnull
  public String getClientToken() {
    return clientToken;
  }

  public void setClientToken(String clientToken) {
    this.clientToken = clientToken;
  }


  public StartDICOMImportJobRequest inputS3Uri(String inputS3Uri) {
    this.inputS3Uri = inputS3Uri;
    return this;
  }

  /**
   * The input prefix path for the S3 bucket that contains the DICOM files to be imported.
   * @return inputS3Uri
   */
  @javax.annotation.Nonnull
  public String getInputS3Uri() {
    return inputS3Uri;
  }

  public void setInputS3Uri(String inputS3Uri) {
    this.inputS3Uri = inputS3Uri;
  }


  public StartDICOMImportJobRequest outputS3Uri(String outputS3Uri) {
    this.outputS3Uri = outputS3Uri;
    return this;
  }

  /**
   * The output prefix of the S3 bucket to upload the results of the DICOM import job.
   * @return outputS3Uri
   */
  @javax.annotation.Nonnull
  public String getOutputS3Uri() {
    return outputS3Uri;
  }

  public void setOutputS3Uri(String outputS3Uri) {
    this.outputS3Uri = outputS3Uri;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StartDICOMImportJobRequest startDICOMImportJobRequest = (StartDICOMImportJobRequest) o;
    return Objects.equals(this.jobName, startDICOMImportJobRequest.jobName) &&
        Objects.equals(this.dataAccessRoleArn, startDICOMImportJobRequest.dataAccessRoleArn) &&
        Objects.equals(this.clientToken, startDICOMImportJobRequest.clientToken) &&
        Objects.equals(this.inputS3Uri, startDICOMImportJobRequest.inputS3Uri) &&
        Objects.equals(this.outputS3Uri, startDICOMImportJobRequest.outputS3Uri);
  }

  @Override
  public int hashCode() {
    return Objects.hash(jobName, dataAccessRoleArn, clientToken, inputS3Uri, outputS3Uri);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class StartDICOMImportJobRequest {\n");
    sb.append("    jobName: ").append(toIndentedString(jobName)).append("\n");
    sb.append("    dataAccessRoleArn: ").append(toIndentedString(dataAccessRoleArn)).append("\n");
    sb.append("    clientToken: ").append(toIndentedString(clientToken)).append("\n");
    sb.append("    inputS3Uri: ").append(toIndentedString(inputS3Uri)).append("\n");
    sb.append("    outputS3Uri: ").append(toIndentedString(outputS3Uri)).append("\n");
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
    openapiFields.add("jobName");
    openapiFields.add("dataAccessRoleArn");
    openapiFields.add("clientToken");
    openapiFields.add("inputS3Uri");
    openapiFields.add("outputS3Uri");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("dataAccessRoleArn");
    openapiRequiredFields.add("clientToken");
    openapiRequiredFields.add("inputS3Uri");
    openapiRequiredFields.add("outputS3Uri");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to StartDICOMImportJobRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!StartDICOMImportJobRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in StartDICOMImportJobRequest is not found in the empty JSON string", StartDICOMImportJobRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!StartDICOMImportJobRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `StartDICOMImportJobRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : StartDICOMImportJobRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("jobName") != null && !jsonObj.get("jobName").isJsonNull()) && !jsonObj.get("jobName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `jobName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("jobName").toString()));
      }
      if (!jsonObj.get("dataAccessRoleArn").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dataAccessRoleArn` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dataAccessRoleArn").toString()));
      }
      if (!jsonObj.get("clientToken").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `clientToken` to be a primitive type in the JSON string but got `%s`", jsonObj.get("clientToken").toString()));
      }
      if (!jsonObj.get("inputS3Uri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `inputS3Uri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("inputS3Uri").toString()));
      }
      if (!jsonObj.get("outputS3Uri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `outputS3Uri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("outputS3Uri").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!StartDICOMImportJobRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'StartDICOMImportJobRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<StartDICOMImportJobRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(StartDICOMImportJobRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<StartDICOMImportJobRequest>() {
           @Override
           public void write(JsonWriter out, StartDICOMImportJobRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public StartDICOMImportJobRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of StartDICOMImportJobRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of StartDICOMImportJobRequest
   * @throws IOException if the JSON string is invalid with respect to StartDICOMImportJobRequest
   */
  public static StartDICOMImportJobRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, StartDICOMImportJobRequest.class);
  }

  /**
   * Convert an instance of StartDICOMImportJobRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

