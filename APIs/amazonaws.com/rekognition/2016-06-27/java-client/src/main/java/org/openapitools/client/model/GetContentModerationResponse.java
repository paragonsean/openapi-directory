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
import org.openapitools.client.model.GetContentModerationResponseGetRequestMetadata;
import org.openapitools.client.model.GetContentModerationResponseVideoMetadata;
import org.openapitools.client.model.Video;
import org.openapitools.client.model.VideoJobStatus;

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
 * GetContentModerationResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:27:22.127926-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetContentModerationResponse {
  public static final String SERIALIZED_NAME_JOB_STATUS = "JobStatus";
  @SerializedName(SERIALIZED_NAME_JOB_STATUS)
  private VideoJobStatus jobStatus;

  public static final String SERIALIZED_NAME_STATUS_MESSAGE = "StatusMessage";
  @SerializedName(SERIALIZED_NAME_STATUS_MESSAGE)
  private String statusMessage;

  public static final String SERIALIZED_NAME_VIDEO_METADATA = "VideoMetadata";
  @SerializedName(SERIALIZED_NAME_VIDEO_METADATA)
  private GetContentModerationResponseVideoMetadata videoMetadata;

  public static final String SERIALIZED_NAME_MODERATION_LABELS = "ModerationLabels";
  @SerializedName(SERIALIZED_NAME_MODERATION_LABELS)
  private List moderationLabels;

  public static final String SERIALIZED_NAME_NEXT_TOKEN = "NextToken";
  @SerializedName(SERIALIZED_NAME_NEXT_TOKEN)
  private String nextToken;

  public static final String SERIALIZED_NAME_MODERATION_MODEL_VERSION = "ModerationModelVersion";
  @SerializedName(SERIALIZED_NAME_MODERATION_MODEL_VERSION)
  private String moderationModelVersion;

  public static final String SERIALIZED_NAME_JOB_ID = "JobId";
  @SerializedName(SERIALIZED_NAME_JOB_ID)
  private String jobId;

  public static final String SERIALIZED_NAME_VIDEO = "Video";
  @SerializedName(SERIALIZED_NAME_VIDEO)
  private Video video;

  public static final String SERIALIZED_NAME_JOB_TAG = "JobTag";
  @SerializedName(SERIALIZED_NAME_JOB_TAG)
  private String jobTag;

  public static final String SERIALIZED_NAME_GET_REQUEST_METADATA = "GetRequestMetadata";
  @SerializedName(SERIALIZED_NAME_GET_REQUEST_METADATA)
  private GetContentModerationResponseGetRequestMetadata getRequestMetadata;

  public GetContentModerationResponse() {
  }

  public GetContentModerationResponse jobStatus(VideoJobStatus jobStatus) {
    this.jobStatus = jobStatus;
    return this;
  }

  /**
   * Get jobStatus
   * @return jobStatus
   */
  @javax.annotation.Nullable
  public VideoJobStatus getJobStatus() {
    return jobStatus;
  }

  public void setJobStatus(VideoJobStatus jobStatus) {
    this.jobStatus = jobStatus;
  }


  public GetContentModerationResponse statusMessage(String statusMessage) {
    this.statusMessage = statusMessage;
    return this;
  }

  /**
   * Get statusMessage
   * @return statusMessage
   */
  @javax.annotation.Nullable
  public String getStatusMessage() {
    return statusMessage;
  }

  public void setStatusMessage(String statusMessage) {
    this.statusMessage = statusMessage;
  }


  public GetContentModerationResponse videoMetadata(GetContentModerationResponseVideoMetadata videoMetadata) {
    this.videoMetadata = videoMetadata;
    return this;
  }

  /**
   * Get videoMetadata
   * @return videoMetadata
   */
  @javax.annotation.Nullable
  public GetContentModerationResponseVideoMetadata getVideoMetadata() {
    return videoMetadata;
  }

  public void setVideoMetadata(GetContentModerationResponseVideoMetadata videoMetadata) {
    this.videoMetadata = videoMetadata;
  }


  public GetContentModerationResponse moderationLabels(List moderationLabels) {
    this.moderationLabels = moderationLabels;
    return this;
  }

  /**
   * Get moderationLabels
   * @return moderationLabels
   */
  @javax.annotation.Nullable
  public List getModerationLabels() {
    return moderationLabels;
  }

  public void setModerationLabels(List moderationLabels) {
    this.moderationLabels = moderationLabels;
  }


  public GetContentModerationResponse nextToken(String nextToken) {
    this.nextToken = nextToken;
    return this;
  }

  /**
   * Get nextToken
   * @return nextToken
   */
  @javax.annotation.Nullable
  public String getNextToken() {
    return nextToken;
  }

  public void setNextToken(String nextToken) {
    this.nextToken = nextToken;
  }


  public GetContentModerationResponse moderationModelVersion(String moderationModelVersion) {
    this.moderationModelVersion = moderationModelVersion;
    return this;
  }

  /**
   * Get moderationModelVersion
   * @return moderationModelVersion
   */
  @javax.annotation.Nullable
  public String getModerationModelVersion() {
    return moderationModelVersion;
  }

  public void setModerationModelVersion(String moderationModelVersion) {
    this.moderationModelVersion = moderationModelVersion;
  }


  public GetContentModerationResponse jobId(String jobId) {
    this.jobId = jobId;
    return this;
  }

  /**
   * Get jobId
   * @return jobId
   */
  @javax.annotation.Nullable
  public String getJobId() {
    return jobId;
  }

  public void setJobId(String jobId) {
    this.jobId = jobId;
  }


  public GetContentModerationResponse video(Video video) {
    this.video = video;
    return this;
  }

  /**
   * Get video
   * @return video
   */
  @javax.annotation.Nullable
  public Video getVideo() {
    return video;
  }

  public void setVideo(Video video) {
    this.video = video;
  }


  public GetContentModerationResponse jobTag(String jobTag) {
    this.jobTag = jobTag;
    return this;
  }

  /**
   * Get jobTag
   * @return jobTag
   */
  @javax.annotation.Nullable
  public String getJobTag() {
    return jobTag;
  }

  public void setJobTag(String jobTag) {
    this.jobTag = jobTag;
  }


  public GetContentModerationResponse getRequestMetadata(GetContentModerationResponseGetRequestMetadata getRequestMetadata) {
    this.getRequestMetadata = getRequestMetadata;
    return this;
  }

  /**
   * Get getRequestMetadata
   * @return getRequestMetadata
   */
  @javax.annotation.Nullable
  public GetContentModerationResponseGetRequestMetadata getGetRequestMetadata() {
    return getRequestMetadata;
  }

  public void setGetRequestMetadata(GetContentModerationResponseGetRequestMetadata getRequestMetadata) {
    this.getRequestMetadata = getRequestMetadata;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetContentModerationResponse getContentModerationResponse = (GetContentModerationResponse) o;
    return Objects.equals(this.jobStatus, getContentModerationResponse.jobStatus) &&
        Objects.equals(this.statusMessage, getContentModerationResponse.statusMessage) &&
        Objects.equals(this.videoMetadata, getContentModerationResponse.videoMetadata) &&
        Objects.equals(this.moderationLabels, getContentModerationResponse.moderationLabels) &&
        Objects.equals(this.nextToken, getContentModerationResponse.nextToken) &&
        Objects.equals(this.moderationModelVersion, getContentModerationResponse.moderationModelVersion) &&
        Objects.equals(this.jobId, getContentModerationResponse.jobId) &&
        Objects.equals(this.video, getContentModerationResponse.video) &&
        Objects.equals(this.jobTag, getContentModerationResponse.jobTag) &&
        Objects.equals(this.getRequestMetadata, getContentModerationResponse.getRequestMetadata);
  }

  @Override
  public int hashCode() {
    return Objects.hash(jobStatus, statusMessage, videoMetadata, moderationLabels, nextToken, moderationModelVersion, jobId, video, jobTag, getRequestMetadata);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetContentModerationResponse {\n");
    sb.append("    jobStatus: ").append(toIndentedString(jobStatus)).append("\n");
    sb.append("    statusMessage: ").append(toIndentedString(statusMessage)).append("\n");
    sb.append("    videoMetadata: ").append(toIndentedString(videoMetadata)).append("\n");
    sb.append("    moderationLabels: ").append(toIndentedString(moderationLabels)).append("\n");
    sb.append("    nextToken: ").append(toIndentedString(nextToken)).append("\n");
    sb.append("    moderationModelVersion: ").append(toIndentedString(moderationModelVersion)).append("\n");
    sb.append("    jobId: ").append(toIndentedString(jobId)).append("\n");
    sb.append("    video: ").append(toIndentedString(video)).append("\n");
    sb.append("    jobTag: ").append(toIndentedString(jobTag)).append("\n");
    sb.append("    getRequestMetadata: ").append(toIndentedString(getRequestMetadata)).append("\n");
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
    openapiFields.add("JobStatus");
    openapiFields.add("StatusMessage");
    openapiFields.add("VideoMetadata");
    openapiFields.add("ModerationLabels");
    openapiFields.add("NextToken");
    openapiFields.add("ModerationModelVersion");
    openapiFields.add("JobId");
    openapiFields.add("Video");
    openapiFields.add("JobTag");
    openapiFields.add("GetRequestMetadata");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetContentModerationResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetContentModerationResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetContentModerationResponse is not found in the empty JSON string", GetContentModerationResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetContentModerationResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetContentModerationResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `JobStatus`
      if (jsonObj.get("JobStatus") != null && !jsonObj.get("JobStatus").isJsonNull()) {
        VideoJobStatus.validateJsonElement(jsonObj.get("JobStatus"));
      }
      // validate the optional field `StatusMessage`
      if (jsonObj.get("StatusMessage") != null && !jsonObj.get("StatusMessage").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("StatusMessage"));
      }
      // validate the optional field `VideoMetadata`
      if (jsonObj.get("VideoMetadata") != null && !jsonObj.get("VideoMetadata").isJsonNull()) {
        GetContentModerationResponseVideoMetadata.validateJsonElement(jsonObj.get("VideoMetadata"));
      }
      // validate the optional field `ModerationLabels`
      if (jsonObj.get("ModerationLabels") != null && !jsonObj.get("ModerationLabels").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("ModerationLabels"));
      }
      // validate the optional field `NextToken`
      if (jsonObj.get("NextToken") != null && !jsonObj.get("NextToken").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("NextToken"));
      }
      // validate the optional field `ModerationModelVersion`
      if (jsonObj.get("ModerationModelVersion") != null && !jsonObj.get("ModerationModelVersion").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("ModerationModelVersion"));
      }
      // validate the optional field `JobId`
      if (jsonObj.get("JobId") != null && !jsonObj.get("JobId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("JobId"));
      }
      // validate the optional field `Video`
      if (jsonObj.get("Video") != null && !jsonObj.get("Video").isJsonNull()) {
        Video.validateJsonElement(jsonObj.get("Video"));
      }
      // validate the optional field `JobTag`
      if (jsonObj.get("JobTag") != null && !jsonObj.get("JobTag").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("JobTag"));
      }
      // validate the optional field `GetRequestMetadata`
      if (jsonObj.get("GetRequestMetadata") != null && !jsonObj.get("GetRequestMetadata").isJsonNull()) {
        GetContentModerationResponseGetRequestMetadata.validateJsonElement(jsonObj.get("GetRequestMetadata"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetContentModerationResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetContentModerationResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetContentModerationResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetContentModerationResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<GetContentModerationResponse>() {
           @Override
           public void write(JsonWriter out, GetContentModerationResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetContentModerationResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetContentModerationResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetContentModerationResponse
   * @throws IOException if the JSON string is invalid with respect to GetContentModerationResponse
   */
  public static GetContentModerationResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetContentModerationResponse.class);
  }

  /**
   * Convert an instance of GetContentModerationResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

