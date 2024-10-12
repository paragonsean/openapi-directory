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
import org.openapitools.client.model.ImageSetState;
import org.openapitools.client.model.ImageSetWorkflowStatus;

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
 * CopyImageSetResponseSourceImageSetProperties
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:28:55.616958-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CopyImageSetResponseSourceImageSetProperties {
  public static final String SERIALIZED_NAME_IMAGE_SET_ID = "imageSetId";
  @SerializedName(SERIALIZED_NAME_IMAGE_SET_ID)
  private String imageSetId;

  public static final String SERIALIZED_NAME_LATEST_VERSION_ID = "latestVersionId";
  @SerializedName(SERIALIZED_NAME_LATEST_VERSION_ID)
  private String latestVersionId;

  public static final String SERIALIZED_NAME_IMAGE_SET_STATE = "imageSetState";
  @SerializedName(SERIALIZED_NAME_IMAGE_SET_STATE)
  private ImageSetState imageSetState;

  public static final String SERIALIZED_NAME_IMAGE_SET_WORKFLOW_STATUS = "imageSetWorkflowStatus";
  @SerializedName(SERIALIZED_NAME_IMAGE_SET_WORKFLOW_STATUS)
  private ImageSetWorkflowStatus imageSetWorkflowStatus;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_IMAGE_SET_ARN = "imageSetArn";
  @SerializedName(SERIALIZED_NAME_IMAGE_SET_ARN)
  private String imageSetArn;

  public CopyImageSetResponseSourceImageSetProperties() {
  }

  public CopyImageSetResponseSourceImageSetProperties imageSetId(String imageSetId) {
    this.imageSetId = imageSetId;
    return this;
  }

  /**
   * Get imageSetId
   * @return imageSetId
   */
  @javax.annotation.Nonnull
  public String getImageSetId() {
    return imageSetId;
  }

  public void setImageSetId(String imageSetId) {
    this.imageSetId = imageSetId;
  }


  public CopyImageSetResponseSourceImageSetProperties latestVersionId(String latestVersionId) {
    this.latestVersionId = latestVersionId;
    return this;
  }

  /**
   * Get latestVersionId
   * @return latestVersionId
   */
  @javax.annotation.Nonnull
  public String getLatestVersionId() {
    return latestVersionId;
  }

  public void setLatestVersionId(String latestVersionId) {
    this.latestVersionId = latestVersionId;
  }


  public CopyImageSetResponseSourceImageSetProperties imageSetState(ImageSetState imageSetState) {
    this.imageSetState = imageSetState;
    return this;
  }

  /**
   * Get imageSetState
   * @return imageSetState
   */
  @javax.annotation.Nullable
  public ImageSetState getImageSetState() {
    return imageSetState;
  }

  public void setImageSetState(ImageSetState imageSetState) {
    this.imageSetState = imageSetState;
  }


  public CopyImageSetResponseSourceImageSetProperties imageSetWorkflowStatus(ImageSetWorkflowStatus imageSetWorkflowStatus) {
    this.imageSetWorkflowStatus = imageSetWorkflowStatus;
    return this;
  }

  /**
   * Get imageSetWorkflowStatus
   * @return imageSetWorkflowStatus
   */
  @javax.annotation.Nullable
  public ImageSetWorkflowStatus getImageSetWorkflowStatus() {
    return imageSetWorkflowStatus;
  }

  public void setImageSetWorkflowStatus(ImageSetWorkflowStatus imageSetWorkflowStatus) {
    this.imageSetWorkflowStatus = imageSetWorkflowStatus;
  }


  public CopyImageSetResponseSourceImageSetProperties createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public CopyImageSetResponseSourceImageSetProperties updatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * Get updatedAt
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
  }


  public CopyImageSetResponseSourceImageSetProperties imageSetArn(String imageSetArn) {
    this.imageSetArn = imageSetArn;
    return this;
  }

  /**
   * Get imageSetArn
   * @return imageSetArn
   */
  @javax.annotation.Nullable
  public String getImageSetArn() {
    return imageSetArn;
  }

  public void setImageSetArn(String imageSetArn) {
    this.imageSetArn = imageSetArn;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CopyImageSetResponseSourceImageSetProperties copyImageSetResponseSourceImageSetProperties = (CopyImageSetResponseSourceImageSetProperties) o;
    return Objects.equals(this.imageSetId, copyImageSetResponseSourceImageSetProperties.imageSetId) &&
        Objects.equals(this.latestVersionId, copyImageSetResponseSourceImageSetProperties.latestVersionId) &&
        Objects.equals(this.imageSetState, copyImageSetResponseSourceImageSetProperties.imageSetState) &&
        Objects.equals(this.imageSetWorkflowStatus, copyImageSetResponseSourceImageSetProperties.imageSetWorkflowStatus) &&
        Objects.equals(this.createdAt, copyImageSetResponseSourceImageSetProperties.createdAt) &&
        Objects.equals(this.updatedAt, copyImageSetResponseSourceImageSetProperties.updatedAt) &&
        Objects.equals(this.imageSetArn, copyImageSetResponseSourceImageSetProperties.imageSetArn);
  }

  @Override
  public int hashCode() {
    return Objects.hash(imageSetId, latestVersionId, imageSetState, imageSetWorkflowStatus, createdAt, updatedAt, imageSetArn);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CopyImageSetResponseSourceImageSetProperties {\n");
    sb.append("    imageSetId: ").append(toIndentedString(imageSetId)).append("\n");
    sb.append("    latestVersionId: ").append(toIndentedString(latestVersionId)).append("\n");
    sb.append("    imageSetState: ").append(toIndentedString(imageSetState)).append("\n");
    sb.append("    imageSetWorkflowStatus: ").append(toIndentedString(imageSetWorkflowStatus)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    imageSetArn: ").append(toIndentedString(imageSetArn)).append("\n");
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
    openapiFields.add("imageSetId");
    openapiFields.add("latestVersionId");
    openapiFields.add("imageSetState");
    openapiFields.add("imageSetWorkflowStatus");
    openapiFields.add("createdAt");
    openapiFields.add("updatedAt");
    openapiFields.add("imageSetArn");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("imageSetId");
    openapiRequiredFields.add("latestVersionId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CopyImageSetResponseSourceImageSetProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CopyImageSetResponseSourceImageSetProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CopyImageSetResponseSourceImageSetProperties is not found in the empty JSON string", CopyImageSetResponseSourceImageSetProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CopyImageSetResponseSourceImageSetProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CopyImageSetResponseSourceImageSetProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CopyImageSetResponseSourceImageSetProperties.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `imageSetId`
      String.validateJsonElement(jsonObj.get("imageSetId"));
      // validate the required field `latestVersionId`
      String.validateJsonElement(jsonObj.get("latestVersionId"));
      // validate the optional field `imageSetState`
      if (jsonObj.get("imageSetState") != null && !jsonObj.get("imageSetState").isJsonNull()) {
        ImageSetState.validateJsonElement(jsonObj.get("imageSetState"));
      }
      // validate the optional field `imageSetWorkflowStatus`
      if (jsonObj.get("imageSetWorkflowStatus") != null && !jsonObj.get("imageSetWorkflowStatus").isJsonNull()) {
        ImageSetWorkflowStatus.validateJsonElement(jsonObj.get("imageSetWorkflowStatus"));
      }
      // validate the optional field `createdAt`
      if (jsonObj.get("createdAt") != null && !jsonObj.get("createdAt").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("createdAt"));
      }
      // validate the optional field `updatedAt`
      if (jsonObj.get("updatedAt") != null && !jsonObj.get("updatedAt").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("updatedAt"));
      }
      // validate the optional field `imageSetArn`
      if (jsonObj.get("imageSetArn") != null && !jsonObj.get("imageSetArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("imageSetArn"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CopyImageSetResponseSourceImageSetProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CopyImageSetResponseSourceImageSetProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CopyImageSetResponseSourceImageSetProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CopyImageSetResponseSourceImageSetProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<CopyImageSetResponseSourceImageSetProperties>() {
           @Override
           public void write(JsonWriter out, CopyImageSetResponseSourceImageSetProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CopyImageSetResponseSourceImageSetProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CopyImageSetResponseSourceImageSetProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CopyImageSetResponseSourceImageSetProperties
   * @throws IOException if the JSON string is invalid with respect to CopyImageSetResponseSourceImageSetProperties
   */
  public static CopyImageSetResponseSourceImageSetProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CopyImageSetResponseSourceImageSetProperties.class);
  }

  /**
   * Convert an instance of CopyImageSetResponseSourceImageSetProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

