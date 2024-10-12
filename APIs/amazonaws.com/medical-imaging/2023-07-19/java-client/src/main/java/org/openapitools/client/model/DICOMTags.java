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
 * The DICOM attributes returned as a part of a response. Each image set has these properties as part of a search result.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:28:55.616958-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DICOMTags {
  public static final String SERIALIZED_NAME_DI_C_O_M_PATIENT_ID = "DICOMPatientId";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_PATIENT_ID)
  private String diCOMPatientId;

  public static final String SERIALIZED_NAME_DI_C_O_M_PATIENT_NAME = "DICOMPatientName";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_PATIENT_NAME)
  private String diCOMPatientName;

  public static final String SERIALIZED_NAME_DI_C_O_M_PATIENT_BIRTH_DATE = "DICOMPatientBirthDate";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_PATIENT_BIRTH_DATE)
  private String diCOMPatientBirthDate;

  public static final String SERIALIZED_NAME_DI_C_O_M_PATIENT_SEX = "DICOMPatientSex";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_PATIENT_SEX)
  private String diCOMPatientSex;

  public static final String SERIALIZED_NAME_DI_C_O_M_STUDY_INSTANCE_U_I_D = "DICOMStudyInstanceUID";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_STUDY_INSTANCE_U_I_D)
  private String diCOMStudyInstanceUID;

  public static final String SERIALIZED_NAME_DI_C_O_M_STUDY_ID = "DICOMStudyId";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_STUDY_ID)
  private String diCOMStudyId;

  public static final String SERIALIZED_NAME_DI_C_O_M_STUDY_DESCRIPTION = "DICOMStudyDescription";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_STUDY_DESCRIPTION)
  private String diCOMStudyDescription;

  public static final String SERIALIZED_NAME_DI_C_O_M_NUMBER_OF_STUDY_RELATED_SERIES = "DICOMNumberOfStudyRelatedSeries";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_NUMBER_OF_STUDY_RELATED_SERIES)
  private Integer diCOMNumberOfStudyRelatedSeries;

  public static final String SERIALIZED_NAME_DI_C_O_M_NUMBER_OF_STUDY_RELATED_INSTANCES = "DICOMNumberOfStudyRelatedInstances";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_NUMBER_OF_STUDY_RELATED_INSTANCES)
  private Integer diCOMNumberOfStudyRelatedInstances;

  public static final String SERIALIZED_NAME_DI_C_O_M_ACCESSION_NUMBER = "DICOMAccessionNumber";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_ACCESSION_NUMBER)
  private String diCOMAccessionNumber;

  public static final String SERIALIZED_NAME_DI_C_O_M_STUDY_DATE = "DICOMStudyDate";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_STUDY_DATE)
  private String diCOMStudyDate;

  public static final String SERIALIZED_NAME_DI_C_O_M_STUDY_TIME = "DICOMStudyTime";
  @SerializedName(SERIALIZED_NAME_DI_C_O_M_STUDY_TIME)
  private String diCOMStudyTime;

  public DICOMTags() {
  }

  public DICOMTags diCOMPatientId(String diCOMPatientId) {
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


  public DICOMTags diCOMPatientName(String diCOMPatientName) {
    this.diCOMPatientName = diCOMPatientName;
    return this;
  }

  /**
   * Get diCOMPatientName
   * @return diCOMPatientName
   */
  @javax.annotation.Nullable
  public String getDiCOMPatientName() {
    return diCOMPatientName;
  }

  public void setDiCOMPatientName(String diCOMPatientName) {
    this.diCOMPatientName = diCOMPatientName;
  }


  public DICOMTags diCOMPatientBirthDate(String diCOMPatientBirthDate) {
    this.diCOMPatientBirthDate = diCOMPatientBirthDate;
    return this;
  }

  /**
   * Get diCOMPatientBirthDate
   * @return diCOMPatientBirthDate
   */
  @javax.annotation.Nullable
  public String getDiCOMPatientBirthDate() {
    return diCOMPatientBirthDate;
  }

  public void setDiCOMPatientBirthDate(String diCOMPatientBirthDate) {
    this.diCOMPatientBirthDate = diCOMPatientBirthDate;
  }


  public DICOMTags diCOMPatientSex(String diCOMPatientSex) {
    this.diCOMPatientSex = diCOMPatientSex;
    return this;
  }

  /**
   * Get diCOMPatientSex
   * @return diCOMPatientSex
   */
  @javax.annotation.Nullable
  public String getDiCOMPatientSex() {
    return diCOMPatientSex;
  }

  public void setDiCOMPatientSex(String diCOMPatientSex) {
    this.diCOMPatientSex = diCOMPatientSex;
  }


  public DICOMTags diCOMStudyInstanceUID(String diCOMStudyInstanceUID) {
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


  public DICOMTags diCOMStudyId(String diCOMStudyId) {
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


  public DICOMTags diCOMStudyDescription(String diCOMStudyDescription) {
    this.diCOMStudyDescription = diCOMStudyDescription;
    return this;
  }

  /**
   * Get diCOMStudyDescription
   * @return diCOMStudyDescription
   */
  @javax.annotation.Nullable
  public String getDiCOMStudyDescription() {
    return diCOMStudyDescription;
  }

  public void setDiCOMStudyDescription(String diCOMStudyDescription) {
    this.diCOMStudyDescription = diCOMStudyDescription;
  }


  public DICOMTags diCOMNumberOfStudyRelatedSeries(Integer diCOMNumberOfStudyRelatedSeries) {
    this.diCOMNumberOfStudyRelatedSeries = diCOMNumberOfStudyRelatedSeries;
    return this;
  }

  /**
   * Get diCOMNumberOfStudyRelatedSeries
   * @return diCOMNumberOfStudyRelatedSeries
   */
  @javax.annotation.Nullable
  public Integer getDiCOMNumberOfStudyRelatedSeries() {
    return diCOMNumberOfStudyRelatedSeries;
  }

  public void setDiCOMNumberOfStudyRelatedSeries(Integer diCOMNumberOfStudyRelatedSeries) {
    this.diCOMNumberOfStudyRelatedSeries = diCOMNumberOfStudyRelatedSeries;
  }


  public DICOMTags diCOMNumberOfStudyRelatedInstances(Integer diCOMNumberOfStudyRelatedInstances) {
    this.diCOMNumberOfStudyRelatedInstances = diCOMNumberOfStudyRelatedInstances;
    return this;
  }

  /**
   * Get diCOMNumberOfStudyRelatedInstances
   * @return diCOMNumberOfStudyRelatedInstances
   */
  @javax.annotation.Nullable
  public Integer getDiCOMNumberOfStudyRelatedInstances() {
    return diCOMNumberOfStudyRelatedInstances;
  }

  public void setDiCOMNumberOfStudyRelatedInstances(Integer diCOMNumberOfStudyRelatedInstances) {
    this.diCOMNumberOfStudyRelatedInstances = diCOMNumberOfStudyRelatedInstances;
  }


  public DICOMTags diCOMAccessionNumber(String diCOMAccessionNumber) {
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


  public DICOMTags diCOMStudyDate(String diCOMStudyDate) {
    this.diCOMStudyDate = diCOMStudyDate;
    return this;
  }

  /**
   * Get diCOMStudyDate
   * @return diCOMStudyDate
   */
  @javax.annotation.Nullable
  public String getDiCOMStudyDate() {
    return diCOMStudyDate;
  }

  public void setDiCOMStudyDate(String diCOMStudyDate) {
    this.diCOMStudyDate = diCOMStudyDate;
  }


  public DICOMTags diCOMStudyTime(String diCOMStudyTime) {
    this.diCOMStudyTime = diCOMStudyTime;
    return this;
  }

  /**
   * Get diCOMStudyTime
   * @return diCOMStudyTime
   */
  @javax.annotation.Nullable
  public String getDiCOMStudyTime() {
    return diCOMStudyTime;
  }

  public void setDiCOMStudyTime(String diCOMStudyTime) {
    this.diCOMStudyTime = diCOMStudyTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DICOMTags diCOMTags = (DICOMTags) o;
    return Objects.equals(this.diCOMPatientId, diCOMTags.diCOMPatientId) &&
        Objects.equals(this.diCOMPatientName, diCOMTags.diCOMPatientName) &&
        Objects.equals(this.diCOMPatientBirthDate, diCOMTags.diCOMPatientBirthDate) &&
        Objects.equals(this.diCOMPatientSex, diCOMTags.diCOMPatientSex) &&
        Objects.equals(this.diCOMStudyInstanceUID, diCOMTags.diCOMStudyInstanceUID) &&
        Objects.equals(this.diCOMStudyId, diCOMTags.diCOMStudyId) &&
        Objects.equals(this.diCOMStudyDescription, diCOMTags.diCOMStudyDescription) &&
        Objects.equals(this.diCOMNumberOfStudyRelatedSeries, diCOMTags.diCOMNumberOfStudyRelatedSeries) &&
        Objects.equals(this.diCOMNumberOfStudyRelatedInstances, diCOMTags.diCOMNumberOfStudyRelatedInstances) &&
        Objects.equals(this.diCOMAccessionNumber, diCOMTags.diCOMAccessionNumber) &&
        Objects.equals(this.diCOMStudyDate, diCOMTags.diCOMStudyDate) &&
        Objects.equals(this.diCOMStudyTime, diCOMTags.diCOMStudyTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(diCOMPatientId, diCOMPatientName, diCOMPatientBirthDate, diCOMPatientSex, diCOMStudyInstanceUID, diCOMStudyId, diCOMStudyDescription, diCOMNumberOfStudyRelatedSeries, diCOMNumberOfStudyRelatedInstances, diCOMAccessionNumber, diCOMStudyDate, diCOMStudyTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DICOMTags {\n");
    sb.append("    diCOMPatientId: ").append(toIndentedString(diCOMPatientId)).append("\n");
    sb.append("    diCOMPatientName: ").append(toIndentedString(diCOMPatientName)).append("\n");
    sb.append("    diCOMPatientBirthDate: ").append(toIndentedString(diCOMPatientBirthDate)).append("\n");
    sb.append("    diCOMPatientSex: ").append(toIndentedString(diCOMPatientSex)).append("\n");
    sb.append("    diCOMStudyInstanceUID: ").append(toIndentedString(diCOMStudyInstanceUID)).append("\n");
    sb.append("    diCOMStudyId: ").append(toIndentedString(diCOMStudyId)).append("\n");
    sb.append("    diCOMStudyDescription: ").append(toIndentedString(diCOMStudyDescription)).append("\n");
    sb.append("    diCOMNumberOfStudyRelatedSeries: ").append(toIndentedString(diCOMNumberOfStudyRelatedSeries)).append("\n");
    sb.append("    diCOMNumberOfStudyRelatedInstances: ").append(toIndentedString(diCOMNumberOfStudyRelatedInstances)).append("\n");
    sb.append("    diCOMAccessionNumber: ").append(toIndentedString(diCOMAccessionNumber)).append("\n");
    sb.append("    diCOMStudyDate: ").append(toIndentedString(diCOMStudyDate)).append("\n");
    sb.append("    diCOMStudyTime: ").append(toIndentedString(diCOMStudyTime)).append("\n");
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
    openapiFields.add("DICOMPatientName");
    openapiFields.add("DICOMPatientBirthDate");
    openapiFields.add("DICOMPatientSex");
    openapiFields.add("DICOMStudyInstanceUID");
    openapiFields.add("DICOMStudyId");
    openapiFields.add("DICOMStudyDescription");
    openapiFields.add("DICOMNumberOfStudyRelatedSeries");
    openapiFields.add("DICOMNumberOfStudyRelatedInstances");
    openapiFields.add("DICOMAccessionNumber");
    openapiFields.add("DICOMStudyDate");
    openapiFields.add("DICOMStudyTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DICOMTags
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DICOMTags.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DICOMTags is not found in the empty JSON string", DICOMTags.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DICOMTags.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DICOMTags` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `DICOMPatientId`
      if (jsonObj.get("DICOMPatientId") != null && !jsonObj.get("DICOMPatientId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMPatientId"));
      }
      // validate the optional field `DICOMPatientName`
      if (jsonObj.get("DICOMPatientName") != null && !jsonObj.get("DICOMPatientName").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMPatientName"));
      }
      // validate the optional field `DICOMPatientBirthDate`
      if (jsonObj.get("DICOMPatientBirthDate") != null && !jsonObj.get("DICOMPatientBirthDate").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMPatientBirthDate"));
      }
      // validate the optional field `DICOMPatientSex`
      if (jsonObj.get("DICOMPatientSex") != null && !jsonObj.get("DICOMPatientSex").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMPatientSex"));
      }
      // validate the optional field `DICOMStudyInstanceUID`
      if (jsonObj.get("DICOMStudyInstanceUID") != null && !jsonObj.get("DICOMStudyInstanceUID").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMStudyInstanceUID"));
      }
      // validate the optional field `DICOMStudyId`
      if (jsonObj.get("DICOMStudyId") != null && !jsonObj.get("DICOMStudyId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMStudyId"));
      }
      // validate the optional field `DICOMStudyDescription`
      if (jsonObj.get("DICOMStudyDescription") != null && !jsonObj.get("DICOMStudyDescription").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMStudyDescription"));
      }
      // validate the optional field `DICOMNumberOfStudyRelatedSeries`
      if (jsonObj.get("DICOMNumberOfStudyRelatedSeries") != null && !jsonObj.get("DICOMNumberOfStudyRelatedSeries").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("DICOMNumberOfStudyRelatedSeries"));
      }
      // validate the optional field `DICOMNumberOfStudyRelatedInstances`
      if (jsonObj.get("DICOMNumberOfStudyRelatedInstances") != null && !jsonObj.get("DICOMNumberOfStudyRelatedInstances").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("DICOMNumberOfStudyRelatedInstances"));
      }
      // validate the optional field `DICOMAccessionNumber`
      if (jsonObj.get("DICOMAccessionNumber") != null && !jsonObj.get("DICOMAccessionNumber").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMAccessionNumber"));
      }
      // validate the optional field `DICOMStudyDate`
      if (jsonObj.get("DICOMStudyDate") != null && !jsonObj.get("DICOMStudyDate").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMStudyDate"));
      }
      // validate the optional field `DICOMStudyTime`
      if (jsonObj.get("DICOMStudyTime") != null && !jsonObj.get("DICOMStudyTime").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DICOMStudyTime"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DICOMTags.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DICOMTags' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DICOMTags> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DICOMTags.class));

       return (TypeAdapter<T>) new TypeAdapter<DICOMTags>() {
           @Override
           public void write(JsonWriter out, DICOMTags value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DICOMTags read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DICOMTags given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DICOMTags
   * @throws IOException if the JSON string is invalid with respect to DICOMTags
   */
  public static DICOMTags fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DICOMTags.class);
  }

  /**
   * Convert an instance of DICOMTags to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

