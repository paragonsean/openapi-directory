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
import org.openapitools.client.model.SegmentDetectionShotSegment;
import org.openapitools.client.model.SegmentDetectionTechnicalCueSegment;
import org.openapitools.client.model.SegmentType;

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
 * A technical cue or shot detection segment detected in a video. An array of &lt;code&gt;SegmentDetection&lt;/code&gt; objects containing all segments detected in a stored video is returned by &lt;a&gt;GetSegmentDetection&lt;/a&gt;. 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:27:22.127926-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SegmentDetection {
  public static final String SERIALIZED_NAME_TYPE = "Type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private SegmentType type;

  public static final String SERIALIZED_NAME_START_TIMESTAMP_MILLIS = "StartTimestampMillis";
  @SerializedName(SERIALIZED_NAME_START_TIMESTAMP_MILLIS)
  private Integer startTimestampMillis;

  public static final String SERIALIZED_NAME_END_TIMESTAMP_MILLIS = "EndTimestampMillis";
  @SerializedName(SERIALIZED_NAME_END_TIMESTAMP_MILLIS)
  private Integer endTimestampMillis;

  public static final String SERIALIZED_NAME_DURATION_MILLIS = "DurationMillis";
  @SerializedName(SERIALIZED_NAME_DURATION_MILLIS)
  private Integer durationMillis;

  public static final String SERIALIZED_NAME_START_TIMECODE_S_M_P_T_E = "StartTimecodeSMPTE";
  @SerializedName(SERIALIZED_NAME_START_TIMECODE_S_M_P_T_E)
  private String startTimecodeSMPTE;

  public static final String SERIALIZED_NAME_END_TIMECODE_S_M_P_T_E = "EndTimecodeSMPTE";
  @SerializedName(SERIALIZED_NAME_END_TIMECODE_S_M_P_T_E)
  private String endTimecodeSMPTE;

  public static final String SERIALIZED_NAME_DURATION_S_M_P_T_E = "DurationSMPTE";
  @SerializedName(SERIALIZED_NAME_DURATION_S_M_P_T_E)
  private String durationSMPTE;

  public static final String SERIALIZED_NAME_TECHNICAL_CUE_SEGMENT = "TechnicalCueSegment";
  @SerializedName(SERIALIZED_NAME_TECHNICAL_CUE_SEGMENT)
  private SegmentDetectionTechnicalCueSegment technicalCueSegment;

  public static final String SERIALIZED_NAME_SHOT_SEGMENT = "ShotSegment";
  @SerializedName(SERIALIZED_NAME_SHOT_SEGMENT)
  private SegmentDetectionShotSegment shotSegment;

  public static final String SERIALIZED_NAME_START_FRAME_NUMBER = "StartFrameNumber";
  @SerializedName(SERIALIZED_NAME_START_FRAME_NUMBER)
  private Integer startFrameNumber;

  public static final String SERIALIZED_NAME_END_FRAME_NUMBER = "EndFrameNumber";
  @SerializedName(SERIALIZED_NAME_END_FRAME_NUMBER)
  private Integer endFrameNumber;

  public static final String SERIALIZED_NAME_DURATION_FRAMES = "DurationFrames";
  @SerializedName(SERIALIZED_NAME_DURATION_FRAMES)
  private Integer durationFrames;

  public SegmentDetection() {
  }

  public SegmentDetection type(SegmentType type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public SegmentType getType() {
    return type;
  }

  public void setType(SegmentType type) {
    this.type = type;
  }


  public SegmentDetection startTimestampMillis(Integer startTimestampMillis) {
    this.startTimestampMillis = startTimestampMillis;
    return this;
  }

  /**
   * Get startTimestampMillis
   * @return startTimestampMillis
   */
  @javax.annotation.Nullable
  public Integer getStartTimestampMillis() {
    return startTimestampMillis;
  }

  public void setStartTimestampMillis(Integer startTimestampMillis) {
    this.startTimestampMillis = startTimestampMillis;
  }


  public SegmentDetection endTimestampMillis(Integer endTimestampMillis) {
    this.endTimestampMillis = endTimestampMillis;
    return this;
  }

  /**
   * Get endTimestampMillis
   * @return endTimestampMillis
   */
  @javax.annotation.Nullable
  public Integer getEndTimestampMillis() {
    return endTimestampMillis;
  }

  public void setEndTimestampMillis(Integer endTimestampMillis) {
    this.endTimestampMillis = endTimestampMillis;
  }


  public SegmentDetection durationMillis(Integer durationMillis) {
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


  public SegmentDetection startTimecodeSMPTE(String startTimecodeSMPTE) {
    this.startTimecodeSMPTE = startTimecodeSMPTE;
    return this;
  }

  /**
   * Get startTimecodeSMPTE
   * @return startTimecodeSMPTE
   */
  @javax.annotation.Nullable
  public String getStartTimecodeSMPTE() {
    return startTimecodeSMPTE;
  }

  public void setStartTimecodeSMPTE(String startTimecodeSMPTE) {
    this.startTimecodeSMPTE = startTimecodeSMPTE;
  }


  public SegmentDetection endTimecodeSMPTE(String endTimecodeSMPTE) {
    this.endTimecodeSMPTE = endTimecodeSMPTE;
    return this;
  }

  /**
   * Get endTimecodeSMPTE
   * @return endTimecodeSMPTE
   */
  @javax.annotation.Nullable
  public String getEndTimecodeSMPTE() {
    return endTimecodeSMPTE;
  }

  public void setEndTimecodeSMPTE(String endTimecodeSMPTE) {
    this.endTimecodeSMPTE = endTimecodeSMPTE;
  }


  public SegmentDetection durationSMPTE(String durationSMPTE) {
    this.durationSMPTE = durationSMPTE;
    return this;
  }

  /**
   * Get durationSMPTE
   * @return durationSMPTE
   */
  @javax.annotation.Nullable
  public String getDurationSMPTE() {
    return durationSMPTE;
  }

  public void setDurationSMPTE(String durationSMPTE) {
    this.durationSMPTE = durationSMPTE;
  }


  public SegmentDetection technicalCueSegment(SegmentDetectionTechnicalCueSegment technicalCueSegment) {
    this.technicalCueSegment = technicalCueSegment;
    return this;
  }

  /**
   * Get technicalCueSegment
   * @return technicalCueSegment
   */
  @javax.annotation.Nullable
  public SegmentDetectionTechnicalCueSegment getTechnicalCueSegment() {
    return technicalCueSegment;
  }

  public void setTechnicalCueSegment(SegmentDetectionTechnicalCueSegment technicalCueSegment) {
    this.technicalCueSegment = technicalCueSegment;
  }


  public SegmentDetection shotSegment(SegmentDetectionShotSegment shotSegment) {
    this.shotSegment = shotSegment;
    return this;
  }

  /**
   * Get shotSegment
   * @return shotSegment
   */
  @javax.annotation.Nullable
  public SegmentDetectionShotSegment getShotSegment() {
    return shotSegment;
  }

  public void setShotSegment(SegmentDetectionShotSegment shotSegment) {
    this.shotSegment = shotSegment;
  }


  public SegmentDetection startFrameNumber(Integer startFrameNumber) {
    this.startFrameNumber = startFrameNumber;
    return this;
  }

  /**
   * Get startFrameNumber
   * @return startFrameNumber
   */
  @javax.annotation.Nullable
  public Integer getStartFrameNumber() {
    return startFrameNumber;
  }

  public void setStartFrameNumber(Integer startFrameNumber) {
    this.startFrameNumber = startFrameNumber;
  }


  public SegmentDetection endFrameNumber(Integer endFrameNumber) {
    this.endFrameNumber = endFrameNumber;
    return this;
  }

  /**
   * Get endFrameNumber
   * @return endFrameNumber
   */
  @javax.annotation.Nullable
  public Integer getEndFrameNumber() {
    return endFrameNumber;
  }

  public void setEndFrameNumber(Integer endFrameNumber) {
    this.endFrameNumber = endFrameNumber;
  }


  public SegmentDetection durationFrames(Integer durationFrames) {
    this.durationFrames = durationFrames;
    return this;
  }

  /**
   * Get durationFrames
   * @return durationFrames
   */
  @javax.annotation.Nullable
  public Integer getDurationFrames() {
    return durationFrames;
  }

  public void setDurationFrames(Integer durationFrames) {
    this.durationFrames = durationFrames;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SegmentDetection segmentDetection = (SegmentDetection) o;
    return Objects.equals(this.type, segmentDetection.type) &&
        Objects.equals(this.startTimestampMillis, segmentDetection.startTimestampMillis) &&
        Objects.equals(this.endTimestampMillis, segmentDetection.endTimestampMillis) &&
        Objects.equals(this.durationMillis, segmentDetection.durationMillis) &&
        Objects.equals(this.startTimecodeSMPTE, segmentDetection.startTimecodeSMPTE) &&
        Objects.equals(this.endTimecodeSMPTE, segmentDetection.endTimecodeSMPTE) &&
        Objects.equals(this.durationSMPTE, segmentDetection.durationSMPTE) &&
        Objects.equals(this.technicalCueSegment, segmentDetection.technicalCueSegment) &&
        Objects.equals(this.shotSegment, segmentDetection.shotSegment) &&
        Objects.equals(this.startFrameNumber, segmentDetection.startFrameNumber) &&
        Objects.equals(this.endFrameNumber, segmentDetection.endFrameNumber) &&
        Objects.equals(this.durationFrames, segmentDetection.durationFrames);
  }

  @Override
  public int hashCode() {
    return Objects.hash(type, startTimestampMillis, endTimestampMillis, durationMillis, startTimecodeSMPTE, endTimecodeSMPTE, durationSMPTE, technicalCueSegment, shotSegment, startFrameNumber, endFrameNumber, durationFrames);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SegmentDetection {\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    startTimestampMillis: ").append(toIndentedString(startTimestampMillis)).append("\n");
    sb.append("    endTimestampMillis: ").append(toIndentedString(endTimestampMillis)).append("\n");
    sb.append("    durationMillis: ").append(toIndentedString(durationMillis)).append("\n");
    sb.append("    startTimecodeSMPTE: ").append(toIndentedString(startTimecodeSMPTE)).append("\n");
    sb.append("    endTimecodeSMPTE: ").append(toIndentedString(endTimecodeSMPTE)).append("\n");
    sb.append("    durationSMPTE: ").append(toIndentedString(durationSMPTE)).append("\n");
    sb.append("    technicalCueSegment: ").append(toIndentedString(technicalCueSegment)).append("\n");
    sb.append("    shotSegment: ").append(toIndentedString(shotSegment)).append("\n");
    sb.append("    startFrameNumber: ").append(toIndentedString(startFrameNumber)).append("\n");
    sb.append("    endFrameNumber: ").append(toIndentedString(endFrameNumber)).append("\n");
    sb.append("    durationFrames: ").append(toIndentedString(durationFrames)).append("\n");
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
    openapiFields.add("Type");
    openapiFields.add("StartTimestampMillis");
    openapiFields.add("EndTimestampMillis");
    openapiFields.add("DurationMillis");
    openapiFields.add("StartTimecodeSMPTE");
    openapiFields.add("EndTimecodeSMPTE");
    openapiFields.add("DurationSMPTE");
    openapiFields.add("TechnicalCueSegment");
    openapiFields.add("ShotSegment");
    openapiFields.add("StartFrameNumber");
    openapiFields.add("EndFrameNumber");
    openapiFields.add("DurationFrames");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SegmentDetection
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SegmentDetection.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SegmentDetection is not found in the empty JSON string", SegmentDetection.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SegmentDetection.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SegmentDetection` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `Type`
      if (jsonObj.get("Type") != null && !jsonObj.get("Type").isJsonNull()) {
        SegmentType.validateJsonElement(jsonObj.get("Type"));
      }
      // validate the optional field `StartTimestampMillis`
      if (jsonObj.get("StartTimestampMillis") != null && !jsonObj.get("StartTimestampMillis").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("StartTimestampMillis"));
      }
      // validate the optional field `EndTimestampMillis`
      if (jsonObj.get("EndTimestampMillis") != null && !jsonObj.get("EndTimestampMillis").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("EndTimestampMillis"));
      }
      // validate the optional field `DurationMillis`
      if (jsonObj.get("DurationMillis") != null && !jsonObj.get("DurationMillis").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("DurationMillis"));
      }
      // validate the optional field `StartTimecodeSMPTE`
      if (jsonObj.get("StartTimecodeSMPTE") != null && !jsonObj.get("StartTimecodeSMPTE").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("StartTimecodeSMPTE"));
      }
      // validate the optional field `EndTimecodeSMPTE`
      if (jsonObj.get("EndTimecodeSMPTE") != null && !jsonObj.get("EndTimecodeSMPTE").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("EndTimecodeSMPTE"));
      }
      // validate the optional field `DurationSMPTE`
      if (jsonObj.get("DurationSMPTE") != null && !jsonObj.get("DurationSMPTE").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("DurationSMPTE"));
      }
      // validate the optional field `TechnicalCueSegment`
      if (jsonObj.get("TechnicalCueSegment") != null && !jsonObj.get("TechnicalCueSegment").isJsonNull()) {
        SegmentDetectionTechnicalCueSegment.validateJsonElement(jsonObj.get("TechnicalCueSegment"));
      }
      // validate the optional field `ShotSegment`
      if (jsonObj.get("ShotSegment") != null && !jsonObj.get("ShotSegment").isJsonNull()) {
        SegmentDetectionShotSegment.validateJsonElement(jsonObj.get("ShotSegment"));
      }
      // validate the optional field `StartFrameNumber`
      if (jsonObj.get("StartFrameNumber") != null && !jsonObj.get("StartFrameNumber").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("StartFrameNumber"));
      }
      // validate the optional field `EndFrameNumber`
      if (jsonObj.get("EndFrameNumber") != null && !jsonObj.get("EndFrameNumber").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("EndFrameNumber"));
      }
      // validate the optional field `DurationFrames`
      if (jsonObj.get("DurationFrames") != null && !jsonObj.get("DurationFrames").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("DurationFrames"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SegmentDetection.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SegmentDetection' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SegmentDetection> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SegmentDetection.class));

       return (TypeAdapter<T>) new TypeAdapter<SegmentDetection>() {
           @Override
           public void write(JsonWriter out, SegmentDetection value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SegmentDetection read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SegmentDetection given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SegmentDetection
   * @throws IOException if the JSON string is invalid with respect to SegmentDetection
   */
  public static SegmentDetection fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SegmentDetection.class);
  }

  /**
   * Convert an instance of SegmentDetection to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

