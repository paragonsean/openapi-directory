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
import org.openapitools.client.model.SearchByAttributeValueDICOMStudyDateAndTime;

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
 * The search input attribute value.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:28:55.616958-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SearchByAttributeValue {
  public static final String SERIALIZED_NAME_DI_C_O_M_PATIENT_ID = "DICOMPatientId";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_PATIENT_ID)
  private String diCOMPatientId;

  public static final String SERIALIZED_NAME_DI_C_O_M_ACCESSION_NUMBER = "DICOMAccessionNumber";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_ACCESSION_NUMBER)
  private String diCOMAccessionNumber;

  public static final String SERIALIZED_NAME_DI_C_O_M_STUDY_ID = "DICOMStudyId";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_STUDY_ID)
  private String diCOMStudyId;

  public static final String SERIALIZED_NAME_DI_C_O_M_STUDY_INSTANCE_U_I_D = "DICOMStudyInstanceUID";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_STUDY_INSTANCE_U_I_D)
  private String diCOMStudyInstanceUID;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_DI_C_O_M_STUDY_DATE_AND_TIME = "DICOMStudyDateAndTime";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_STUDY_DATE_AND_TIME)
  private SearchByAttributeValueDICOMStudyDateAndTime diCOMStudyDateAndTime;

  public SearchByAttributeValue() {
  }

  public SearchByAttributeValue diCOMPatientId(String diCOMPatientId) {
    this.diCOMPatientId = diCOMPatientId;
    return this;
  }

  /**
   * Get diCOMPatientId
   * @return diCOMPatientId
   */
  @javax.annotation.Nullable
  public String getDiCOMPatientId() {
    return diCOMPatientId;
  }

  public void setDiCOMPatientId(String diCOMPatientId) {
    this.diCOMPatientId = diCOMPatientId;
  }


  public SearchByAttributeValue diCOMAccessionNumber(String diCOMAccessionNumber) {
    this.diCOMAccessionNumber = diCOMAccessionNumber;
    return this;
  }

  /**
   * Get diCOMAccessionNumber
   * @return diCOMAccessionNumber
   */
  @javax.annotation.Nullable
  public String getDiCOMAccessionNumber() {
    return diCOMAccessionNumber;
  }

  public void setDiCOMAccessionNumber(String diCOMAccessionNumber) {
    this.diCOMAccessionNumber = diCOMAccessionNumber;
  }


  public SearchByAttributeValue diCOMStudyId(String diCOMStudyId) {
    this.diCOMStudyId = diCOMStudyId;
    return this;
  }

  /**
   * Get diCOMStudyId
   * @return diCOMStudyId
   */
  @javax.annotation.Nullable
  public String getDiCOMStudyId() {
    return diCOMStudyId;
  }

  public void setDiCOMStudyId(String diCOMStudyId) {
    this.diCOMStudyId = diCOMStudyId;
  }


  public SearchByAttributeValue diCOMStudyInstanceUID(String diCOMStudyInstanceUID) {
    this.diCOMStudyInstanceUID = diCOMStudyInstanceUID;
    return this;
  }

  /**
   * Get diCOMStudyInstanceUID
   * @return diCOMStudyInstanceUID
   */
  @javax.annotation.Nullable
  public String getDiCOMStudyInstanceUID() {
    return diCOMStudyInstanceUID;
  }

  public void setDiCOMStudyInstanceUID(String diCOMStudyInstanceUID) {
    this.diCOMStudyInstanceUID = diCOMStudyInstanceUID;
  }


  public SearchByAttributeValue createdAt(OffsetDateTime createdAt) {
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


  public SearchByAttributeValue diCOMStudyDateAndTime(SearchByAttributeValueDICOMStudyDateAndTime diCOMStudyDateAndTime) {
    this.diCOMStudyDateAndTime = diCOMStudyDateAndTime;
    return this;
  }

  /**
   * Get diCOMStudyDateAndTime
   * @return diCOMStudyDateAndTime
   */
  @javax.annotation.Nullable
  public SearchByAttributeValueDICOMStudyDateAndTime getDiCOMStudyDateAndTime() {
    return diCOMStudyDateAndTime;
  }

  public void setDiCOMStudyDateAndTime(SearchByAttributeValueDICOMStudyDateAndTime diCOMStudyDateAndTime) {
    this.diCOMStudyDateAndTime = diCOMStudyDateAndTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SearchByAttributeValue searchByAttributeValue = (SearchByAttributeValue) o;
    return Objects.equals(this.diCOMPatientId, searchByAttributeValue.diCOMPatientId) &&
        Objects.equals(this.diCOMAccessionNumber, searchByAttributeValue.diCOMAccessionNumber) &&
        Objects.equals(this.diCOMStudyId, searchByAttributeValue.diCOMStudyId) &&
        Objects.equals(this.diCOMStudyInstanceUID, searchByAttributeValue.diCOMStudyInstanceUID) &&
        Objects.equals(this.createdAt, searchByAttributeValue.createdAt) &&
        Objects.equals(this.diCOMStudyDateAndTime, searchByAttributeValue.diCOMStudyDateAndTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(diCOMPatientId, diCOMAccessionNumber, diCOMStudyId, diCOMStudyInstanceUID, createdAt, diCOMStudyDateAndTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SearchByAttributeValue {\n");
    sb.append("    diCOMPatientId: ").append(toIndentedString(diCOMPatientId)).append("\n");
    sb.append("    diCOMAccessionNumber: ").append(toIndentedString(diCOMAccessionNumber)).append("\n");
    sb.append("    diCOMStudyId: ").append(toIndentedString(diCOMStudyId)).append("\n");
    sb.append("    diCOMStudyInstanceUID: ").append(toIndentedString(diCOMStudyInstanceUID)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    diCOMStudyDateAndTime: ").append(toIndentedString(diCOMStudyDateAndTime)).append("\n");
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
    openapiFields.add("DICOMPatientId");
    openapiFields.add("DICOMAccessionNumber");
    openapiFields.add("DICOMStudyId");
    openapiFields.add("DICOMStudyInstanceUID");
    openapiFields.add("createdAt");
    openapiFields.add("DICOMStudyDateAndTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SearchByAttributeValue
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SearchByAttributeValue.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SearchByAttributeValue is not found in the empty JSON string", SearchByAttributeValue.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SearchByAttributeValue.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SearchByAttributeValue` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `DICOMPatientId`
      if (jsonObj.get("DICOMPatientId") != null && !jsonObj.get("DICOMPatientId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMPatientId"));
      }
      // validate the optional field `DICOMAccessionNumber`
      if (jsonObj.get("DICOMAccessionNumber") != null && !jsonObj.get("DICOMAccessionNumber").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMAccessionNumber"));
      }
      // validate the optional field `DICOMStudyId`
      if (jsonObj.get("DICOMStudyId") != null && !jsonObj.get("DICOMStudyId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMStudyId"));
      }
      // validate the optional field `DICOMStudyInstanceUID`
      if (jsonObj.get("DICOMStudyInstanceUID") != null && !jsonObj.get("DICOMStudyInstanceUID").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMStudyInstanceUID"));
      }
      // validate the optional field `createdAt`
      if (jsonObj.get("createdAt") != null && !jsonObj.get("createdAt").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("createdAt"));
      }
      // validate the optional field `DICOMStudyDateAndTime`
      if (jsonObj.get("DICOMStudyDateAndTime") != null && !jsonObj.get("DICOMStudyDateAndTime").isJsonNull()) {
        SearchByAttributeValueDICOMStudyDateAndTime.validateJsonElement(jsonObj.get("DICOMStudyDateAndTime"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SearchByAttributeValue.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SearchByAttributeValue' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SearchByAttributeValue> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SearchByAttributeValue.class));

       return (TypeAdapter<T>) new TypeAdapter<SearchByAttributeValue>() {
           @Override
           public void write(JsonWriter out, SearchByAttributeValue value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SearchByAttributeValue read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SearchByAttributeValue given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SearchByAttributeValue
   * @throws IOException if the JSON string is invalid with respect to SearchByAttributeValue
   */
  public static SearchByAttributeValue fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SearchByAttributeValue.class);
  }

  /**
   * Convert an instance of SearchByAttributeValue to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

