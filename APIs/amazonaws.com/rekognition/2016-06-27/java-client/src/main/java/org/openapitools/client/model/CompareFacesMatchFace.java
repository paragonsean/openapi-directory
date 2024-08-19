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
import org.openapitools.client.model.ComparedFaceBoundingBox;
import org.openapitools.client.model.ComparedFacePose;
import org.openapitools.client.model.ComparedFaceQuality;
import org.openapitools.client.model.ComparedFaceSmile;

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
 * CompareFacesMatchFace
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:27:22.127926-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CompareFacesMatchFace {
  public static final String SERIALIZED_NAME_BOUNDING_BOX = "BoundingBox";
  @SerializedName(SERIALIZED_NAME_BOUNDING_BOX)
  private ComparedFaceBoundingBox boundingBox;

  public static final String SERIALIZED_NAME_CONFIDENCE = "Confidence";
  @SerializedName(SERIALIZED_NAME_CONFIDENCE)
  private Float confidence;

  public static final String SERIALIZED_NAME_LANDMARKS = "Landmarks";
  @SerializedName(SERIALIZED_NAME_LANDMARKS)
  private List landmarks;

  public static final String SERIALIZED_NAME_POSE = "Pose";
  @SerializedName(SERIALIZED_NAME_POSE)
  private ComparedFacePose pose;

  public static final String SERIALIZED_NAME_QUALITY = "Quality";
  @SerializedName(SERIALIZED_NAME_QUALITY)
  private ComparedFaceQuality quality;

  public static final String SERIALIZED_NAME_EMOTIONS = "Emotions";
  @SerializedName(SERIALIZED_NAME_EMOTIONS)
  private List emotions;

  public static final String SERIALIZED_NAME_SMILE = "Smile";
  @SerializedName(SERIALIZED_NAME_SMILE)
  private ComparedFaceSmile smile;

  public CompareFacesMatchFace() {
  }

  public CompareFacesMatchFace boundingBox(ComparedFaceBoundingBox boundingBox) {
    this.boundingBox = boundingBox;
    return this;
  }

  /**
   * Get boundingBox
   * @return boundingBox
   */
  @javax.annotation.Nullable
  public ComparedFaceBoundingBox getBoundingBox() {
    return boundingBox;
  }

  public void setBoundingBox(ComparedFaceBoundingBox boundingBox) {
    this.boundingBox = boundingBox;
  }


  public CompareFacesMatchFace confidence(Float confidence) {
    this.confidence = confidence;
    return this;
  }

  /**
   * Get confidence
   * @return confidence
   */
  @javax.annotation.Nullable
  public Float getConfidence() {
    return confidence;
  }

  public void setConfidence(Float confidence) {
    this.confidence = confidence;
  }


  public CompareFacesMatchFace landmarks(List landmarks) {
    this.landmarks = landmarks;
    return this;
  }

  /**
   * Get landmarks
   * @return landmarks
   */
  @javax.annotation.Nullable
  public List getLandmarks() {
    return landmarks;
  }

  public void setLandmarks(List landmarks) {
    this.landmarks = landmarks;
  }


  public CompareFacesMatchFace pose(ComparedFacePose pose) {
    this.pose = pose;
    return this;
  }

  /**
   * Get pose
   * @return pose
   */
  @javax.annotation.Nullable
  public ComparedFacePose getPose() {
    return pose;
  }

  public void setPose(ComparedFacePose pose) {
    this.pose = pose;
  }


  public CompareFacesMatchFace quality(ComparedFaceQuality quality) {
    this.quality = quality;
    return this;
  }

  /**
   * Get quality
   * @return quality
   */
  @javax.annotation.Nullable
  public ComparedFaceQuality getQuality() {
    return quality;
  }

  public void setQuality(ComparedFaceQuality quality) {
    this.quality = quality;
  }


  public CompareFacesMatchFace emotions(List emotions) {
    this.emotions = emotions;
    return this;
  }

  /**
   * Get emotions
   * @return emotions
   */
  @javax.annotation.Nullable
  public List getEmotions() {
    return emotions;
  }

  public void setEmotions(List emotions) {
    this.emotions = emotions;
  }


  public CompareFacesMatchFace smile(ComparedFaceSmile smile) {
    this.smile = smile;
    return this;
  }

  /**
   * Get smile
   * @return smile
   */
  @javax.annotation.Nullable
  public ComparedFaceSmile getSmile() {
    return smile;
  }

  public void setSmile(ComparedFaceSmile smile) {
    this.smile = smile;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CompareFacesMatchFace compareFacesMatchFace = (CompareFacesMatchFace) o;
    return Objects.equals(this.boundingBox, compareFacesMatchFace.boundingBox) &&
        Objects.equals(this.confidence, compareFacesMatchFace.confidence) &&
        Objects.equals(this.landmarks, compareFacesMatchFace.landmarks) &&
        Objects.equals(this.pose, compareFacesMatchFace.pose) &&
        Objects.equals(this.quality, compareFacesMatchFace.quality) &&
        Objects.equals(this.emotions, compareFacesMatchFace.emotions) &&
        Objects.equals(this.smile, compareFacesMatchFace.smile);
  }

  @Override
  public int hashCode() {
    return Objects.hash(boundingBox, confidence, landmarks, pose, quality, emotions, smile);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CompareFacesMatchFace {\n");
    sb.append("    boundingBox: ").append(toIndentedString(boundingBox)).append("\n");
    sb.append("    confidence: ").append(toIndentedString(confidence)).append("\n");
    sb.append("    landmarks: ").append(toIndentedString(landmarks)).append("\n");
    sb.append("    pose: ").append(toIndentedString(pose)).append("\n");
    sb.append("    quality: ").append(toIndentedString(quality)).append("\n");
    sb.append("    emotions: ").append(toIndentedString(emotions)).append("\n");
    sb.append("    smile: ").append(toIndentedString(smile)).append("\n");
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
    openapiFields.add("BoundingBox");
    openapiFields.add("Confidence");
    openapiFields.add("Landmarks");
    openapiFields.add("Pose");
    openapiFields.add("Quality");
    openapiFields.add("Emotions");
    openapiFields.add("Smile");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CompareFacesMatchFace
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CompareFacesMatchFace.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CompareFacesMatchFace is not found in the empty JSON string", CompareFacesMatchFace.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CompareFacesMatchFace.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CompareFacesMatchFace` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `BoundingBox`
      if (jsonObj.get("BoundingBox") != null && !jsonObj.get("BoundingBox").isJsonNull()) {
        ComparedFaceBoundingBox.validateJsonElement(jsonObj.get("BoundingBox"));
      }
      // validate the optional field `Confidence`
      if (jsonObj.get("Confidence") != null && !jsonObj.get("Confidence").isJsonNull()) {
        Float.validateJsonElement(jsonObj.get("Confidence"));
      }
      // validate the optional field `Landmarks`
      if (jsonObj.get("Landmarks") != null && !jsonObj.get("Landmarks").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("Landmarks"));
      }
      // validate the optional field `Pose`
      if (jsonObj.get("Pose") != null && !jsonObj.get("Pose").isJsonNull()) {
        ComparedFacePose.validateJsonElement(jsonObj.get("Pose"));
      }
      // validate the optional field `Quality`
      if (jsonObj.get("Quality") != null && !jsonObj.get("Quality").isJsonNull()) {
        ComparedFaceQuality.validateJsonElement(jsonObj.get("Quality"));
      }
      // validate the optional field `Emotions`
      if (jsonObj.get("Emotions") != null && !jsonObj.get("Emotions").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("Emotions"));
      }
      // validate the optional field `Smile`
      if (jsonObj.get("Smile") != null && !jsonObj.get("Smile").isJsonNull()) {
        ComparedFaceSmile.validateJsonElement(jsonObj.get("Smile"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CompareFacesMatchFace.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CompareFacesMatchFace' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CompareFacesMatchFace> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CompareFacesMatchFace.class));

       return (TypeAdapter<T>) new TypeAdapter<CompareFacesMatchFace>() {
           @Override
           public void write(JsonWriter out, CompareFacesMatchFace value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CompareFacesMatchFace read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CompareFacesMatchFace given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CompareFacesMatchFace
   * @throws IOException if the JSON string is invalid with respect to CompareFacesMatchFace
   */
  public static CompareFacesMatchFace fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CompareFacesMatchFace.class);
  }

  /**
   * Convert an instance of CompareFacesMatchFace to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

