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
import org.openapitools.client.model.VideoColorRange;

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
 * GetCelebrityRecognitionResponseVideoMetadata
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:27:22.127926-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetCelebrityRecognitionResponseVideoMetadata {
  public static final String SERIALIZED_NAME_CODEC = "Codec";
  @SerializedName(SERIALIZED_NAME_CODEC)
  private String codec;

  public static final String SERIALIZED_NAME_DURATION_MILLIS = "DurationMillis";
  @SerializedName(SERIALIZED_NAME_DURATION_MILLIS)
  private Integer durationMillis;

  public static final String SERIALIZED_NAME_FORMAT = "Format";
  @SerializedName(SERIALIZED_NAME_FORMAT)
  private String format;

  public static final String SERIALIZED_NAME_FRAME_RATE = "FrameRate";
  @SerializedName(SERIALIZED_NAME_FRAME_RATE)
  private Float frameRate;

  public static final String SERIALIZED_NAME_FRAME_HEIGHT = "FrameHeight";
  @SerializedName(SERIALIZED_NAME_FRAME_HEIGHT)
  private Integer frameHeight;

  public static final String SERIALIZED_NAME_FRAME_WIDTH = "FrameWidth";
  @SerializedName(SERIALIZED_NAME_FRAME_WIDTH)
  private Integer frameWidth;

  public static final String SERIALIZED_NAME_COLOR_RANGE = "ColorRange";
  @SerializedName(SERIALIZED_NAME_COLOR_RANGE)
  private VideoColorRange colorRange;

  public GetCelebrityRecognitionResponseVideoMetadata() {
  }

  public GetCelebrityRecognitionResponseVideoMetadata codec(String codec) {
    this.codec = codec;
    return this;
  }

  /**
   * Get codec
   * @return codec
   */
  @javax.annotation.Nullable
  public String getCodec() {
    return codec;
  }

  public void setCodec(String codec) {
    this.codec = codec;
  }


  public GetCelebrityRecognitionResponseVideoMetadata durationMillis(Integer durationMillis) {
    this.durationMillis = durationMillis;
    return this;
  }

  /**
   * Get durationMillis
   * @return durationMillis
   */
  @javax.annotation.Nullable
  public Integer getDurationMillis() {
    return durationMillis;
  }

  public void setDurationMillis(Integer durationMillis) {
    this.durationMillis = durationMillis;
  }


  public GetCelebrityRecognitionResponseVideoMetadata format(String format) {
    this.format = format;
    return this;
  }

  /**
   * Get format
   * @return format
   */
  @javax.annotation.Nullable
  public String getFormat() {
    return format;
  }

  public void setFormat(String format) {
    this.format = format;
  }


  public GetCelebrityRecognitionResponseVideoMetadata frameRate(Float frameRate) {
    this.frameRate = frameRate;
    return this;
  }

  /**
   * Get frameRate
   * @return frameRate
   */
  @javax.annotation.Nullable
  public Float getFrameRate() {
    return frameRate;
  }

  public void setFrameRate(Float frameRate) {
    this.frameRate = frameRate;
  }


  public GetCelebrityRecognitionResponseVideoMetadata frameHeight(Integer frameHeight) {
    this.frameHeight = frameHeight;
    return this;
  }

  /**
   * Get frameHeight
   * @return frameHeight
   */
  @javax.annotation.Nullable
  public Integer getFrameHeight() {
    return frameHeight;
  }

  public void setFrameHeight(Integer frameHeight) {
    this.frameHeight = frameHeight;
  }


  public GetCelebrityRecognitionResponseVideoMetadata frameWidth(Integer frameWidth) {
    this.frameWidth = frameWidth;
    return this;
  }

  /**
   * Get frameWidth
   * @return frameWidth
   */
  @javax.annotation.Nullable
  public Integer getFrameWidth() {
    return frameWidth;
  }

  public void setFrameWidth(Integer frameWidth) {
    this.frameWidth = frameWidth;
  }


  public GetCelebrityRecognitionResponseVideoMetadata colorRange(VideoColorRange colorRange) {
    this.colorRange = colorRange;
    return this;
  }

  /**
   * Get colorRange
   * @return colorRange
   */
  @javax.annotation.Nullable
  public VideoColorRange getColorRange() {
    return colorRange;
  }

  public void setColorRange(VideoColorRange colorRange) {
    this.colorRange = colorRange;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetCelebrityRecognitionResponseVideoMetadata getCelebrityRecognitionResponseVideoMetadata = (GetCelebrityRecognitionResponseVideoMetadata) o;
    return Objects.equals(this.codec, getCelebrityRecognitionResponseVideoMetadata.codec) &&
        Objects.equals(this.durationMillis, getCelebrityRecognitionResponseVideoMetadata.durationMillis) &&
        Objects.equals(this.format, getCelebrityRecognitionResponseVideoMetadata.format) &&
        Objects.equals(this.frameRate, getCelebrityRecognitionResponseVideoMetadata.frameRate) &&
        Objects.equals(this.frameHeight, getCelebrityRecognitionResponseVideoMetadata.frameHeight) &&
        Objects.equals(this.frameWidth, getCelebrityRecognitionResponseVideoMetadata.frameWidth) &&
        Objects.equals(this.colorRange, getCelebrityRecognitionResponseVideoMetadata.colorRange);
  }

  @Override
  public int hashCode() {
    return Objects.hash(codec, durationMillis, format, frameRate, frameHeight, frameWidth, colorRange);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetCelebrityRecognitionResponseVideoMetadata {\n");
    sb.append("    codec: ").append(toIndentedString(codec)).append("\n");
    sb.append("    durationMillis: ").append(toIndentedString(durationMillis)).append("\n");
    sb.append("    format: ").append(toIndentedString(format)).append("\n");
    sb.append("    frameRate: ").append(toIndentedString(frameRate)).append("\n");
    sb.append("    frameHeight: ").append(toIndentedString(frameHeight)).append("\n");
    sb.append("    frameWidth: ").append(toIndentedString(frameWidth)).append("\n");
    sb.append("    colorRange: ").append(toIndentedString(colorRange)).append("\n");
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
    openapiFields.add("Codec");
    openapiFields.add("DurationMillis");
    openapiFields.add("Format");
    openapiFields.add("FrameRate");
    openapiFields.add("FrameHeight");
    openapiFields.add("FrameWidth");
    openapiFields.add("ColorRange");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetCelebrityRecognitionResponseVideoMetadata
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetCelebrityRecognitionResponseVideoMetadata.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetCelebrityRecognitionResponseVideoMetadata is not found in the empty JSON string", GetCelebrityRecognitionResponseVideoMetadata.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetCelebrityRecognitionResponseVideoMetadata.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetCelebrityRecognitionResponseVideoMetadata` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `Codec`
      if (jsonObj.get("Codec") != null && !jsonObj.get("Codec").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("Codec"));
      }
      // validate the optional field `DurationMillis`
      if (jsonObj.get("DurationMillis") != null && !jsonObj.get("DurationMillis").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("DurationMillis"));
      }
      // validate the optional field `Format`
      if (jsonObj.get("Format") != null && !jsonObj.get("Format").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("Format"));
      }
      // validate the optional field `FrameRate`
      if (jsonObj.get("FrameRate") != null && !jsonObj.get("FrameRate").isJsonNull()) {
        Float.validateJsonElement(jsonObj.get("FrameRate"));
      }
      // validate the optional field `FrameHeight`
      if (jsonObj.get("FrameHeight") != null && !jsonObj.get("FrameHeight").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("FrameHeight"));
      }
      // validate the optional field `FrameWidth`
      if (jsonObj.get("FrameWidth") != null && !jsonObj.get("FrameWidth").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("FrameWidth"));
      }
      // validate the optional field `ColorRange`
      if (jsonObj.get("ColorRange") != null && !jsonObj.get("ColorRange").isJsonNull()) {
        VideoColorRange.validateJsonElement(jsonObj.get("ColorRange"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetCelebrityRecognitionResponseVideoMetadata.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetCelebrityRecognitionResponseVideoMetadata' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetCelebrityRecognitionResponseVideoMetadata> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetCelebrityRecognitionResponseVideoMetadata.class));

       return (TypeAdapter<T>) new TypeAdapter<GetCelebrityRecognitionResponseVideoMetadata>() {
           @Override
           public void write(JsonWriter out, GetCelebrityRecognitionResponseVideoMetadata value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetCelebrityRecognitionResponseVideoMetadata read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetCelebrityRecognitionResponseVideoMetadata given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetCelebrityRecognitionResponseVideoMetadata
   * @throws IOException if the JSON string is invalid with respect to GetCelebrityRecognitionResponseVideoMetadata
   */
  public static GetCelebrityRecognitionResponseVideoMetadata fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetCelebrityRecognitionResponseVideoMetadata.class);
  }

  /**
   * Convert an instance of GetCelebrityRecognitionResponseVideoMetadata to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

