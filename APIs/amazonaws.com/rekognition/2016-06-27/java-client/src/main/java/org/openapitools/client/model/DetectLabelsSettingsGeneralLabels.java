/*
 * Amazon Rekognition
 * <p>This is the API Reference for <a href=\"https://docs.aws.amazon.com/rekognition/latest/dg/images.html\">Amazon Rekognition Image</a>, <a href=\"https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html\">Amazon Rekognition Custom Labels</a>, <a href=\"https://docs.aws.amazon.com/rekognition/latest/dg/video.html\">Amazon Rekognition Stored Video</a>, <a href=\"https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html\">Amazon Rekognition Streaming Video</a>. It provides descriptions of actions, data types, common parameters, and common errors.</p> <p> <b>Amazon Rekognition Image</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AssociateFaces.html\">AssociateFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CompareFaces.html\">CompareFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html\">CreateCollection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateUser.html\">CreateUser</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteCollection.html\">DeleteCollection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteFaces.html\">DeleteFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteUser.html\">DeleteUser</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeCollection.html\">DescribeCollection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html\">DetectFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html\">DetectLabels</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html\">DetectModerationLabels</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectProtectiveEquipment.html\">DetectProtectiveEquipment</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText.html\">DetectText</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DisassociateFaces.html\">DisassociateFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetCelebrityInfo.html\">GetCelebrityInfo</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html\">IndexFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListCollections.html\">ListCollections</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListFaces.html\">ListFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListFaces.html\">ListUsers</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RecognizeCelebrities.html\">RecognizeCelebrities</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFaces.html\">SearchFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFacesByImage.html\">SearchFacesByImage</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsers.html\">SearchUsers</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsersByImage.html\">SearchUsersByImage</a> </p> </li> </ul> <p> <b>Amazon Rekognition Custom Labels</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CopyProjectVersion.html\">CopyProjectVersion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateDataset.html\">CreateDataset</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProject.html\">CreateProject</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProjectVersion.html\">CreateProjectVersion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteDataset.html\">DeleteDataset</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProject.html\">DeleteProject</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProjectPolicy.html\">DeleteProjectPolicy</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProjectVersion.html\">DeleteProjectVersion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeDataset.html\">DescribeDataset</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeProjects.html\">DescribeProjects</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeProjectVersions.html\">DescribeProjectVersions</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectCustomLabels.html\">DetectCustomLabels</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DistributeDatasetEntries.html\">DistributeDatasetEntries</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListDatasetEntries.html\">ListDatasetEntries</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListDatasetLabels.html\">ListDatasetLabels</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListProjectPolicies.html\">ListProjectPolicies</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_PutProjectPolicy.html\">PutProjectPolicy</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartProjectVersion.html\">StartProjectVersion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StopProjectVersion.html\">StopProjectVersion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UpdateDatasetEntries.html\">UpdateDatasetEntries</a> </p> </li> </ul> <p> <b>Amazon Rekognition Video Stored Video</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetCelebrityRecognition.html\">GetCelebrityRecognition</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetContentModeration.html\">GetContentModeration</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceDetection.html\">GetFaceDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceSearch.html\">GetFaceSearch</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetLabelDetection.html\">GetLabelDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetPersonTracking.html\">GetPersonTracking</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetSegmentDetection.html\">GetSegmentDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetTextDetection.html\">GetTextDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartCelebrityRecognition.html\">StartCelebrityRecognition</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartContentModeration.html\">StartContentModeration</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceDetection.html\">StartFaceDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceSearch.html\">StartFaceSearch</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartLabelDetection.html\">StartLabelDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartPersonTracking.html\">StartPersonTracking</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartSegmentDetection.html\">StartSegmentDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartTextDetection.html\">StartTextDetection</a> </p> </li> </ul> <p> <b>Amazon Rekognition Video Streaming Video</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html\">CreateStreamProcessor</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteStreamProcessor.html\">DeleteStreamProcessor</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeStreamProcessor.html\">DescribeStreamProcessor</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListStreamProcessors.html\">ListStreamProcessors</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartStreamProcessor.html\">StartStreamProcessor</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StopStreamProcessor.html\">StopStreamProcessor</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UpdateStreamProcessor.html\">UpdateStreamProcessor</a> </p> </li> </ul>
 *
 * The version of the OpenAPI document: 2016-06-27
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
import java.util.List;

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
 * DetectLabelsSettingsGeneralLabels
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:27:22.127926-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DetectLabelsSettingsGeneralLabels {
  public static final String SERIALIZED_NAME_LABEL_INCLUSION_FILTERS = "LabelInclusionFilters";
  @SerializedName(SERIALIZED_NAME_LABEL_INCLUSION_FILTERS)
  private List labelInclusionFilters;

  public static final String SERIALIZED_NAME_LABEL_EXCLUSION_FILTERS = "LabelExclusionFilters";
  @SerializedName(SERIALIZED_NAME_LABEL_EXCLUSION_FILTERS)
  private List labelExclusionFilters;

  public static final String SERIALIZED_NAME_LABEL_CATEGORY_INCLUSION_FILTERS = "LabelCategoryInclusionFilters";
  @SerializedName(SERIALIZED_NAME_LABEL_CATEGORY_INCLUSION_FILTERS)
  private List labelCategoryInclusionFilters;

  public static final String SERIALIZED_NAME_LABEL_CATEGORY_EXCLUSION_FILTERS = "LabelCategoryExclusionFilters";
  @SerializedName(SERIALIZED_NAME_LABEL_CATEGORY_EXCLUSION_FILTERS)
  private List labelCategoryExclusionFilters;

  public DetectLabelsSettingsGeneralLabels() {
  }

  public DetectLabelsSettingsGeneralLabels labelInclusionFilters(List labelInclusionFilters) {
    this.labelInclusionFilters = labelInclusionFilters;
    return this;
  }

  /**
   * Get labelInclusionFilters
   * @return labelInclusionFilters
   */
  @javax.annotation.Nullable
  public List getLabelInclusionFilters() {
    return labelInclusionFilters;
  }

  public void setLabelInclusionFilters(List labelInclusionFilters) {
    this.labelInclusionFilters = labelInclusionFilters;
  }


  public DetectLabelsSettingsGeneralLabels labelExclusionFilters(List labelExclusionFilters) {
    this.labelExclusionFilters = labelExclusionFilters;
    return this;
  }

  /**
   * Get labelExclusionFilters
   * @return labelExclusionFilters
   */
  @javax.annotation.Nullable
  public List getLabelExclusionFilters() {
    return labelExclusionFilters;
  }

  public void setLabelExclusionFilters(List labelExclusionFilters) {
    this.labelExclusionFilters = labelExclusionFilters;
  }


  public DetectLabelsSettingsGeneralLabels labelCategoryInclusionFilters(List labelCategoryInclusionFilters) {
    this.labelCategoryInclusionFilters = labelCategoryInclusionFilters;
    return this;
  }

  /**
   * Get labelCategoryInclusionFilters
   * @return labelCategoryInclusionFilters
   */
  @javax.annotation.Nullable
  public List getLabelCategoryInclusionFilters() {
    return labelCategoryInclusionFilters;
  }

  public void setLabelCategoryInclusionFilters(List labelCategoryInclusionFilters) {
    this.labelCategoryInclusionFilters = labelCategoryInclusionFilters;
  }


  public DetectLabelsSettingsGeneralLabels labelCategoryExclusionFilters(List labelCategoryExclusionFilters) {
    this.labelCategoryExclusionFilters = labelCategoryExclusionFilters;
    return this;
  }

  /**
   * Get labelCategoryExclusionFilters
   * @return labelCategoryExclusionFilters
   */
  @javax.annotation.Nullable
  public List getLabelCategoryExclusionFilters() {
    return labelCategoryExclusionFilters;
  }

  public void setLabelCategoryExclusionFilters(List labelCategoryExclusionFilters) {
    this.labelCategoryExclusionFilters = labelCategoryExclusionFilters;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DetectLabelsSettingsGeneralLabels detectLabelsSettingsGeneralLabels = (DetectLabelsSettingsGeneralLabels) o;
    return Objects.equals(this.labelInclusionFilters, detectLabelsSettingsGeneralLabels.labelInclusionFilters) &&
        Objects.equals(this.labelExclusionFilters, detectLabelsSettingsGeneralLabels.labelExclusionFilters) &&
        Objects.equals(this.labelCategoryInclusionFilters, detectLabelsSettingsGeneralLabels.labelCategoryInclusionFilters) &&
        Objects.equals(this.labelCategoryExclusionFilters, detectLabelsSettingsGeneralLabels.labelCategoryExclusionFilters);
  }

  @Override
  public int hashCode() {
    return Objects.hash(labelInclusionFilters, labelExclusionFilters, labelCategoryInclusionFilters, labelCategoryExclusionFilters);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DetectLabelsSettingsGeneralLabels {\n");
    sb.append("    labelInclusionFilters: ").append(toIndentedString(labelInclusionFilters)).append("\n");
    sb.append("    labelExclusionFilters: ").append(toIndentedString(labelExclusionFilters)).append("\n");
    sb.append("    labelCategoryInclusionFilters: ").append(toIndentedString(labelCategoryInclusionFilters)).append("\n");
    sb.append("    labelCategoryExclusionFilters: ").append(toIndentedString(labelCategoryExclusionFilters)).append("\n");
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
    openapiFields.add("LabelInclusionFilters");
    openapiFields.add("LabelExclusionFilters");
    openapiFields.add("LabelCategoryInclusionFilters");
    openapiFields.add("LabelCategoryExclusionFilters");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DetectLabelsSettingsGeneralLabels
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DetectLabelsSettingsGeneralLabels.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DetectLabelsSettingsGeneralLabels is not found in the empty JSON string", DetectLabelsSettingsGeneralLabels.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DetectLabelsSettingsGeneralLabels.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DetectLabelsSettingsGeneralLabels` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `LabelInclusionFilters`
      if (jsonObj.get("LabelInclusionFilters") != null && !jsonObj.get("LabelInclusionFilters").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("LabelInclusionFilters"));
      }
      // validate the optional field `LabelExclusionFilters`
      if (jsonObj.get("LabelExclusionFilters") != null && !jsonObj.get("LabelExclusionFilters").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("LabelExclusionFilters"));
      }
      // validate the optional field `LabelCategoryInclusionFilters`
      if (jsonObj.get("LabelCategoryInclusionFilters") != null && !jsonObj.get("LabelCategoryInclusionFilters").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("LabelCategoryInclusionFilters"));
      }
      // validate the optional field `LabelCategoryExclusionFilters`
      if (jsonObj.get("LabelCategoryExclusionFilters") != null && !jsonObj.get("LabelCategoryExclusionFilters").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("LabelCategoryExclusionFilters"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DetectLabelsSettingsGeneralLabels.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DetectLabelsSettingsGeneralLabels' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DetectLabelsSettingsGeneralLabels> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DetectLabelsSettingsGeneralLabels.class));

       return (TypeAdapter<T>) new TypeAdapter<DetectLabelsSettingsGeneralLabels>() {
           @Override
           public void write(JsonWriter out, DetectLabelsSettingsGeneralLabels value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DetectLabelsSettingsGeneralLabels read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DetectLabelsSettingsGeneralLabels given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DetectLabelsSettingsGeneralLabels
   * @throws IOException if the JSON string is invalid with respect to DetectLabelsSettingsGeneralLabels
   */
  public static DetectLabelsSettingsGeneralLabels fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DetectLabelsSettingsGeneralLabels.class);
  }

  /**
   * Convert an instance of DetectLabelsSettingsGeneralLabels to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

