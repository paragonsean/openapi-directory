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
import java.util.Map;
import org.openapitools.client.model.CreateProjectVersionRequestOutputConfig;
import org.openapitools.client.model.CreateProjectVersionRequestTestingData;
import org.openapitools.client.model.CreateProjectVersionRequestTrainingData;

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
 * CreateProjectVersionRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:27:22.127926-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateProjectVersionRequest {
  public static final String SERIALIZED_NAME_PROJECT_ARN = "ProjectArn";
  @SerializedName(SERIALIZED_NAME_PROJECT_ARN)
  private String projectArn;

  public static final String SERIALIZED_NAME_VERSION_NAME = "VersionName";
  @SerializedName(SERIALIZED_NAME_VERSION_NAME)
  private String versionName;

  public static final String SERIALIZED_NAME_OUTPUT_CONFIG = "OutputConfig";
  @SerializedName(SERIALIZED_NAME_OUTPUT_CONFIG)
  private CreateProjectVersionRequestOutputConfig outputConfig;

  public static final String SERIALIZED_NAME_TRAINING_DATA = "TrainingData";
  @SerializedName(SERIALIZED_NAME_TRAINING_DATA)
  private CreateProjectVersionRequestTrainingData trainingData;

  public static final String SERIALIZED_NAME_TESTING_DATA = "TestingData";
  @SerializedName(SERIALIZED_NAME_TESTING_DATA)
  private CreateProjectVersionRequestTestingData testingData;

  public static final String SERIALIZED_NAME_TAGS = "Tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private Map tags;

  public static final String SERIALIZED_NAME_KMS_KEY_ID = "KmsKeyId";
  @SerializedName(SERIALIZED_NAME_KMS_KEY_ID)
  private String kmsKeyId;

  public CreateProjectVersionRequest() {
  }

  public CreateProjectVersionRequest projectArn(String projectArn) {
    this.projectArn = projectArn;
    return this;
  }

  /**
   * Get projectArn
   * @return projectArn
   */
  @javax.annotation.Nonnull
  public String getProjectArn() {
    return projectArn;
  }

  public void setProjectArn(String projectArn) {
    this.projectArn = projectArn;
  }


  public CreateProjectVersionRequest versionName(String versionName) {
    this.versionName = versionName;
    return this;
  }

  /**
   * Get versionName
   * @return versionName
   */
  @javax.annotation.Nonnull
  public String getVersionName() {
    return versionName;
  }

  public void setVersionName(String versionName) {
    this.versionName = versionName;
  }


  public CreateProjectVersionRequest outputConfig(CreateProjectVersionRequestOutputConfig outputConfig) {
    this.outputConfig = outputConfig;
    return this;
  }

  /**
   * Get outputConfig
   * @return outputConfig
   */
  @javax.annotation.Nonnull
  public CreateProjectVersionRequestOutputConfig getOutputConfig() {
    return outputConfig;
  }

  public void setOutputConfig(CreateProjectVersionRequestOutputConfig outputConfig) {
    this.outputConfig = outputConfig;
  }


  public CreateProjectVersionRequest trainingData(CreateProjectVersionRequestTrainingData trainingData) {
    this.trainingData = trainingData;
    return this;
  }

  /**
   * Get trainingData
   * @return trainingData
   */
  @javax.annotation.Nullable
  public CreateProjectVersionRequestTrainingData getTrainingData() {
    return trainingData;
  }

  public void setTrainingData(CreateProjectVersionRequestTrainingData trainingData) {
    this.trainingData = trainingData;
  }


  public CreateProjectVersionRequest testingData(CreateProjectVersionRequestTestingData testingData) {
    this.testingData = testingData;
    return this;
  }

  /**
   * Get testingData
   * @return testingData
   */
  @javax.annotation.Nullable
  public CreateProjectVersionRequestTestingData getTestingData() {
    return testingData;
  }

  public void setTestingData(CreateProjectVersionRequestTestingData testingData) {
    this.testingData = testingData;
  }


  public CreateProjectVersionRequest tags(Map tags) {
    this.tags = tags;
    return this;
  }

  /**
   * Get tags
   * @return tags
   */
  @javax.annotation.Nullable
  public Map getTags() {
    return tags;
  }

  public void setTags(Map tags) {
    this.tags = tags;
  }


  public CreateProjectVersionRequest kmsKeyId(String kmsKeyId) {
    this.kmsKeyId = kmsKeyId;
    return this;
  }

  /**
   * Get kmsKeyId
   * @return kmsKeyId
   */
  @javax.annotation.Nullable
  public String getKmsKeyId() {
    return kmsKeyId;
  }

  public void setKmsKeyId(String kmsKeyId) {
    this.kmsKeyId = kmsKeyId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateProjectVersionRequest createProjectVersionRequest = (CreateProjectVersionRequest) o;
    return Objects.equals(this.projectArn, createProjectVersionRequest.projectArn) &&
        Objects.equals(this.versionName, createProjectVersionRequest.versionName) &&
        Objects.equals(this.outputConfig, createProjectVersionRequest.outputConfig) &&
        Objects.equals(this.trainingData, createProjectVersionRequest.trainingData) &&
        Objects.equals(this.testingData, createProjectVersionRequest.testingData) &&
        Objects.equals(this.tags, createProjectVersionRequest.tags) &&
        Objects.equals(this.kmsKeyId, createProjectVersionRequest.kmsKeyId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(projectArn, versionName, outputConfig, trainingData, testingData, tags, kmsKeyId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateProjectVersionRequest {\n");
    sb.append("    projectArn: ").append(toIndentedString(projectArn)).append("\n");
    sb.append("    versionName: ").append(toIndentedString(versionName)).append("\n");
    sb.append("    outputConfig: ").append(toIndentedString(outputConfig)).append("\n");
    sb.append("    trainingData: ").append(toIndentedString(trainingData)).append("\n");
    sb.append("    testingData: ").append(toIndentedString(testingData)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    kmsKeyId: ").append(toIndentedString(kmsKeyId)).append("\n");
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
    openapiFields.add("ProjectArn");
    openapiFields.add("VersionName");
    openapiFields.add("OutputConfig");
    openapiFields.add("TrainingData");
    openapiFields.add("TestingData");
    openapiFields.add("Tags");
    openapiFields.add("KmsKeyId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("ProjectArn");
    openapiRequiredFields.add("VersionName");
    openapiRequiredFields.add("OutputConfig");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateProjectVersionRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateProjectVersionRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateProjectVersionRequest is not found in the empty JSON string", CreateProjectVersionRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateProjectVersionRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateProjectVersionRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateProjectVersionRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `ProjectArn`
      String.validateJsonElement(jsonObj.get("ProjectArn"));
      // validate the required field `VersionName`
      String.validateJsonElement(jsonObj.get("VersionName"));
      // validate the required field `OutputConfig`
      CreateProjectVersionRequestOutputConfig.validateJsonElement(jsonObj.get("OutputConfig"));
      // validate the optional field `TrainingData`
      if (jsonObj.get("TrainingData") != null && !jsonObj.get("TrainingData").isJsonNull()) {
        CreateProjectVersionRequestTrainingData.validateJsonElement(jsonObj.get("TrainingData"));
      }
      // validate the optional field `TestingData`
      if (jsonObj.get("TestingData") != null && !jsonObj.get("TestingData").isJsonNull()) {
        CreateProjectVersionRequestTestingData.validateJsonElement(jsonObj.get("TestingData"));
      }
      // validate the optional field `Tags`
      if (jsonObj.get("Tags") != null && !jsonObj.get("Tags").isJsonNull()) {
        Map.validateJsonElement(jsonObj.get("Tags"));
      }
      // validate the optional field `KmsKeyId`
      if (jsonObj.get("KmsKeyId") != null && !jsonObj.get("KmsKeyId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("KmsKeyId"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateProjectVersionRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateProjectVersionRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateProjectVersionRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateProjectVersionRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateProjectVersionRequest>() {
           @Override
           public void write(JsonWriter out, CreateProjectVersionRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateProjectVersionRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateProjectVersionRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateProjectVersionRequest
   * @throws IOException if the JSON string is invalid with respect to CreateProjectVersionRequest
   */
  public static CreateProjectVersionRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateProjectVersionRequest.class);
  }

  /**
   * Convert an instance of CreateProjectVersionRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

