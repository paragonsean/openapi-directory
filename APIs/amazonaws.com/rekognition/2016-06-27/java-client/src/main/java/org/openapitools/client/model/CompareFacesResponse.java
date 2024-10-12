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
import org.openapitools.client.model.CompareFacesResponseSourceImageFace;
import org.openapitools.client.model.OrientationCorrection;

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
 * CompareFacesResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:27:22.127926-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CompareFacesResponse {
  public static final String SERIALIZED_NAME_SOURCE_IMAGE_FACE = "SourceImageFace";
  @SerializedName(SERIALIZED_NAME_SOURCE_IMAGE_FACE)
  private CompareFacesResponseSourceImageFace sourceImageFace;

  public static final String SERIALIZED_NAME_FACE_MATCHES = "FaceMatches";
  @SerializedName(SERIALIZED_NAME_FACE_MATCHES)
  private List faceMatches;

  public static final String SERIALIZED_NAME_UNMATCHED_FACES = "UnmatchedFaces";
  @SerializedName(SERIALIZED_NAME_UNMATCHED_FACES)
  private List unmatchedFaces;

  public static final String SERIALIZED_NAME_SOURCE_IMAGE_ORIENTATION_CORRECTION = "SourceImageOrientationCorrection";
  @SerializedName(SERIALIZED_NAME_SOURCE_IMAGE_ORIENTATION_CORRECTION)
  private OrientationCorrection sourceImageOrientationCorrection;

  public static final String SERIALIZED_NAME_TARGET_IMAGE_ORIENTATION_CORRECTION = "TargetImageOrientationCorrection";
  @SerializedName(SERIALIZED_NAME_TARGET_IMAGE_ORIENTATION_CORRECTION)
  private OrientationCorrection targetImageOrientationCorrection;

  public CompareFacesResponse() {
  }

  public CompareFacesResponse sourceImageFace(CompareFacesResponseSourceImageFace sourceImageFace) {
    this.sourceImageFace = sourceImageFace;
    return this;
  }

  /**
   * Get sourceImageFace
   * @return sourceImageFace
   */
  @javax.annotation.Nullable
  public CompareFacesResponseSourceImageFace getSourceImageFace() {
    return sourceImageFace;
  }

  public void setSourceImageFace(CompareFacesResponseSourceImageFace sourceImageFace) {
    this.sourceImageFace = sourceImageFace;
  }


  public CompareFacesResponse faceMatches(List faceMatches) {
    this.faceMatches = faceMatches;
    return this;
  }

  /**
   * Get faceMatches
   * @return faceMatches
   */
  @javax.annotation.Nullable
  public List getFaceMatches() {
    return faceMatches;
  }

  public void setFaceMatches(List faceMatches) {
    this.faceMatches = faceMatches;
  }


  public CompareFacesResponse unmatchedFaces(List unmatchedFaces) {
    this.unmatchedFaces = unmatchedFaces;
    return this;
  }

  /**
   * Get unmatchedFaces
   * @return unmatchedFaces
   */
  @javax.annotation.Nullable
  public List getUnmatchedFaces() {
    return unmatchedFaces;
  }

  public void setUnmatchedFaces(List unmatchedFaces) {
    this.unmatchedFaces = unmatchedFaces;
  }


  public CompareFacesResponse sourceImageOrientationCorrection(OrientationCorrection sourceImageOrientationCorrection) {
    this.sourceImageOrientationCorrection = sourceImageOrientationCorrection;
    return this;
  }

  /**
   * Get sourceImageOrientationCorrection
   * @return sourceImageOrientationCorrection
   */
  @javax.annotation.Nullable
  public OrientationCorrection getSourceImageOrientationCorrection() {
    return sourceImageOrientationCorrection;
  }

  public void setSourceImageOrientationCorrection(OrientationCorrection sourceImageOrientationCorrection) {
    this.sourceImageOrientationCorrection = sourceImageOrientationCorrection;
  }


  public CompareFacesResponse targetImageOrientationCorrection(OrientationCorrection targetImageOrientationCorrection) {
    this.targetImageOrientationCorrection = targetImageOrientationCorrection;
    return this;
  }

  /**
   * Get targetImageOrientationCorrection
   * @return targetImageOrientationCorrection
   */
  @javax.annotation.Nullable
  public OrientationCorrection getTargetImageOrientationCorrection() {
    return targetImageOrientationCorrection;
  }

  public void setTargetImageOrientationCorrection(OrientationCorrection targetImageOrientationCorrection) {
    this.targetImageOrientationCorrection = targetImageOrientationCorrection;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CompareFacesResponse compareFacesResponse = (CompareFacesResponse) o;
    return Objects.equals(this.sourceImageFace, compareFacesResponse.sourceImageFace) &&
        Objects.equals(this.faceMatches, compareFacesResponse.faceMatches) &&
        Objects.equals(this.unmatchedFaces, compareFacesResponse.unmatchedFaces) &&
        Objects.equals(this.sourceImageOrientationCorrection, compareFacesResponse.sourceImageOrientationCorrection) &&
        Objects.equals(this.targetImageOrientationCorrection, compareFacesResponse.targetImageOrientationCorrection);
  }

  @Override
  public int hashCode() {
    return Objects.hash(sourceImageFace, faceMatches, unmatchedFaces, sourceImageOrientationCorrection, targetImageOrientationCorrection);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CompareFacesResponse {\n");
    sb.append("    sourceImageFace: ").append(toIndentedString(sourceImageFace)).append("\n");
    sb.append("    faceMatches: ").append(toIndentedString(faceMatches)).append("\n");
    sb.append("    unmatchedFaces: ").append(toIndentedString(unmatchedFaces)).append("\n");
    sb.append("    sourceImageOrientationCorrection: ").append(toIndentedString(sourceImageOrientationCorrection)).append("\n");
    sb.append("    targetImageOrientationCorrection: ").append(toIndentedString(targetImageOrientationCorrection)).append("\n");
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
    openapiFields.add("SourceImageFace");
    openapiFields.add("FaceMatches");
    openapiFields.add("UnmatchedFaces");
    openapiFields.add("SourceImageOrientationCorrection");
    openapiFields.add("TargetImageOrientationCorrection");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CompareFacesResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CompareFacesResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CompareFacesResponse is not found in the empty JSON string", CompareFacesResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CompareFacesResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CompareFacesResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `SourceImageFace`
      if (jsonObj.get("SourceImageFace") != null && !jsonObj.get("SourceImageFace").isJsonNull()) {
        CompareFacesResponseSourceImageFace.validateJsonElement(jsonObj.get("SourceImageFace"));
      }
      // validate the optional field `FaceMatches`
      if (jsonObj.get("FaceMatches") != null && !jsonObj.get("FaceMatches").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("FaceMatches"));
      }
      // validate the optional field `UnmatchedFaces`
      if (jsonObj.get("UnmatchedFaces") != null && !jsonObj.get("UnmatchedFaces").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("UnmatchedFaces"));
      }
      // validate the optional field `SourceImageOrientationCorrection`
      if (jsonObj.get("SourceImageOrientationCorrection") != null && !jsonObj.get("SourceImageOrientationCorrection").isJsonNull()) {
        OrientationCorrection.validateJsonElement(jsonObj.get("SourceImageOrientationCorrection"));
      }
      // validate the optional field `TargetImageOrientationCorrection`
      if (jsonObj.get("TargetImageOrientationCorrection") != null && !jsonObj.get("TargetImageOrientationCorrection").isJsonNull()) {
        OrientationCorrection.validateJsonElement(jsonObj.get("TargetImageOrientationCorrection"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CompareFacesResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CompareFacesResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CompareFacesResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CompareFacesResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<CompareFacesResponse>() {
           @Override
           public void write(JsonWriter out, CompareFacesResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CompareFacesResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CompareFacesResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CompareFacesResponse
   * @throws IOException if the JSON string is invalid with respect to CompareFacesResponse
   */
  public static CompareFacesResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CompareFacesResponse.class);
  }

  /**
   * Convert an instance of CompareFacesResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

