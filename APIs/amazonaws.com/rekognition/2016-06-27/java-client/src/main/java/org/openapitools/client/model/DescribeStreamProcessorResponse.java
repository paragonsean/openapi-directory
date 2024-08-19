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
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CreateStreamProcessorRequestDataSharingPreference;
import org.openapitools.client.model.CreateStreamProcessorRequestSettings;
import org.openapitools.client.model.DescribeStreamProcessorResponseInput;
import org.openapitools.client.model.DescribeStreamProcessorResponseOutput;
import org.openapitools.client.model.StreamProcessorNotificationChannel;
import org.openapitools.client.model.StreamProcessorStatus;

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
 * DescribeStreamProcessorResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:27:22.127926-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DescribeStreamProcessorResponse {
  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_STREAM_PROCESSOR_ARN = "StreamProcessorArn";
  @SerializedName(SERIALIZED_NAME_STREAM_PROCESSOR_ARN)
  private String streamProcessorArn;

  public static final String SERIALIZED_NAME_STATUS = "Status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StreamProcessorStatus status;

  public static final String SERIALIZED_NAME_STATUS_MESSAGE = "StatusMessage";
  @SerializedName(SERIALIZED_NAME_STATUS_MESSAGE)
  private String statusMessage;

  public static final String SERIALIZED_NAME_CREATION_TIMESTAMP = "CreationTimestamp";
  @SerializedName(SERIALIZED_NAME_CREATION_TIMESTAMP)
  private OffsetDateTime creationTimestamp;

  public static final String SERIALIZED_NAME_LAST_UPDATE_TIMESTAMP = "LastUpdateTimestamp";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATE_TIMESTAMP)
  private OffsetDateTime lastUpdateTimestamp;

  public static final String SERIALIZED_NAME_INPUT = "Input";
  @SerializedName(SERIALIZED_NAME_INPUT)
  private DescribeStreamProcessorResponseInput input;

  public static final String SERIALIZED_NAME_OUTPUT = "Output";
  @SerializedName(SERIALIZED_NAME_OUTPUT)
  private DescribeStreamProcessorResponseOutput output;

  public static final String SERIALIZED_NAME_ROLE_ARN = "RoleArn";
  @SerializedName(SERIALIZED_NAME_ROLE_ARN)
  private String roleArn;

  public static final String SERIALIZED_NAME_SETTINGS = "Settings";
  @SerializedName(SERIALIZED_NAME_SETTINGS)
  private CreateStreamProcessorRequestSettings settings;

  public static final String SERIALIZED_NAME_NOTIFICATION_CHANNEL = "NotificationChannel";
  @SerializedName(SERIALIZED_NAME_NOTIFICATION_CHANNEL)
  private StreamProcessorNotificationChannel notificationChannel;

  public static final String SERIALIZED_NAME_KMS_KEY_ID = "KmsKeyId";
  @SerializedName(SERIALIZED_NAME_KMS_KEY_ID)
  private String kmsKeyId;

  public static final String SERIALIZED_NAME_REGIONS_OF_INTEREST = "RegionsOfInterest";
  @SerializedName(SERIALIZED_NAME_REGIONS_OF_INTEREST)
  private List regionsOfInterest;

  public static final String SERIALIZED_NAME_DATA_SHARING_PREFERENCE = "DataSharingPreference";
  @SerializedName(SERIALIZED_NAME_DATA_SHARING_PREFERENCE)
  private CreateStreamProcessorRequestDataSharingPreference dataSharingPreference;

  public DescribeStreamProcessorResponse() {
  }

  public DescribeStreamProcessorResponse name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public DescribeStreamProcessorResponse streamProcessorArn(String streamProcessorArn) {
    this.streamProcessorArn = streamProcessorArn;
    return this;
  }

  /**
   * Get streamProcessorArn
   * @return streamProcessorArn
   */
  @javax.annotation.Nullable
  public String getStreamProcessorArn() {
    return streamProcessorArn;
  }

  public void setStreamProcessorArn(String streamProcessorArn) {
    this.streamProcessorArn = streamProcessorArn;
  }


  public DescribeStreamProcessorResponse status(StreamProcessorStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public StreamProcessorStatus getStatus() {
    return status;
  }

  public void setStatus(StreamProcessorStatus status) {
    this.status = status;
  }


  public DescribeStreamProcessorResponse statusMessage(String statusMessage) {
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


  public DescribeStreamProcessorResponse creationTimestamp(OffsetDateTime creationTimestamp) {
    this.creationTimestamp = creationTimestamp;
    return this;
  }

  /**
   * Get creationTimestamp
   * @return creationTimestamp
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreationTimestamp() {
    return creationTimestamp;
  }

  public void setCreationTimestamp(OffsetDateTime creationTimestamp) {
    this.creationTimestamp = creationTimestamp;
  }


  public DescribeStreamProcessorResponse lastUpdateTimestamp(OffsetDateTime lastUpdateTimestamp) {
    this.lastUpdateTimestamp = lastUpdateTimestamp;
    return this;
  }

  /**
   * Get lastUpdateTimestamp
   * @return lastUpdateTimestamp
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastUpdateTimestamp() {
    return lastUpdateTimestamp;
  }

  public void setLastUpdateTimestamp(OffsetDateTime lastUpdateTimestamp) {
    this.lastUpdateTimestamp = lastUpdateTimestamp;
  }


  public DescribeStreamProcessorResponse input(DescribeStreamProcessorResponseInput input) {
    this.input = input;
    return this;
  }

  /**
   * Get input
   * @return input
   */
  @javax.annotation.Nullable
  public DescribeStreamProcessorResponseInput getInput() {
    return input;
  }

  public void setInput(DescribeStreamProcessorResponseInput input) {
    this.input = input;
  }


  public DescribeStreamProcessorResponse output(DescribeStreamProcessorResponseOutput output) {
    this.output = output;
    return this;
  }

  /**
   * Get output
   * @return output
   */
  @javax.annotation.Nullable
  public DescribeStreamProcessorResponseOutput getOutput() {
    return output;
  }

  public void setOutput(DescribeStreamProcessorResponseOutput output) {
    this.output = output;
  }


  public DescribeStreamProcessorResponse roleArn(String roleArn) {
    this.roleArn = roleArn;
    return this;
  }

  /**
   * Get roleArn
   * @return roleArn
   */
  @javax.annotation.Nullable
  public String getRoleArn() {
    return roleArn;
  }

  public void setRoleArn(String roleArn) {
    this.roleArn = roleArn;
  }


  public DescribeStreamProcessorResponse settings(CreateStreamProcessorRequestSettings settings) {
    this.settings = settings;
    return this;
  }

  /**
   * Get settings
   * @return settings
   */
  @javax.annotation.Nullable
  public CreateStreamProcessorRequestSettings getSettings() {
    return settings;
  }

  public void setSettings(CreateStreamProcessorRequestSettings settings) {
    this.settings = settings;
  }


  public DescribeStreamProcessorResponse notificationChannel(StreamProcessorNotificationChannel notificationChannel) {
    this.notificationChannel = notificationChannel;
    return this;
  }

  /**
   * Get notificationChannel
   * @return notificationChannel
   */
  @javax.annotation.Nullable
  public StreamProcessorNotificationChannel getNotificationChannel() {
    return notificationChannel;
  }

  public void setNotificationChannel(StreamProcessorNotificationChannel notificationChannel) {
    this.notificationChannel = notificationChannel;
  }


  public DescribeStreamProcessorResponse kmsKeyId(String kmsKeyId) {
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


  public DescribeStreamProcessorResponse regionsOfInterest(List regionsOfInterest) {
    this.regionsOfInterest = regionsOfInterest;
    return this;
  }

  /**
   * Get regionsOfInterest
   * @return regionsOfInterest
   */
  @javax.annotation.Nullable
  public List getRegionsOfInterest() {
    return regionsOfInterest;
  }

  public void setRegionsOfInterest(List regionsOfInterest) {
    this.regionsOfInterest = regionsOfInterest;
  }


  public DescribeStreamProcessorResponse dataSharingPreference(CreateStreamProcessorRequestDataSharingPreference dataSharingPreference) {
    this.dataSharingPreference = dataSharingPreference;
    return this;
  }

  /**
   * Get dataSharingPreference
   * @return dataSharingPreference
   */
  @javax.annotation.Nullable
  public CreateStreamProcessorRequestDataSharingPreference getDataSharingPreference() {
    return dataSharingPreference;
  }

  public void setDataSharingPreference(CreateStreamProcessorRequestDataSharingPreference dataSharingPreference) {
    this.dataSharingPreference = dataSharingPreference;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DescribeStreamProcessorResponse describeStreamProcessorResponse = (DescribeStreamProcessorResponse) o;
    return Objects.equals(this.name, describeStreamProcessorResponse.name) &&
        Objects.equals(this.streamProcessorArn, describeStreamProcessorResponse.streamProcessorArn) &&
        Objects.equals(this.status, describeStreamProcessorResponse.status) &&
        Objects.equals(this.statusMessage, describeStreamProcessorResponse.statusMessage) &&
        Objects.equals(this.creationTimestamp, describeStreamProcessorResponse.creationTimestamp) &&
        Objects.equals(this.lastUpdateTimestamp, describeStreamProcessorResponse.lastUpdateTimestamp) &&
        Objects.equals(this.input, describeStreamProcessorResponse.input) &&
        Objects.equals(this.output, describeStreamProcessorResponse.output) &&
        Objects.equals(this.roleArn, describeStreamProcessorResponse.roleArn) &&
        Objects.equals(this.settings, describeStreamProcessorResponse.settings) &&
        Objects.equals(this.notificationChannel, describeStreamProcessorResponse.notificationChannel) &&
        Objects.equals(this.kmsKeyId, describeStreamProcessorResponse.kmsKeyId) &&
        Objects.equals(this.regionsOfInterest, describeStreamProcessorResponse.regionsOfInterest) &&
        Objects.equals(this.dataSharingPreference, describeStreamProcessorResponse.dataSharingPreference);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, streamProcessorArn, status, statusMessage, creationTimestamp, lastUpdateTimestamp, input, output, roleArn, settings, notificationChannel, kmsKeyId, regionsOfInterest, dataSharingPreference);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DescribeStreamProcessorResponse {\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    streamProcessorArn: ").append(toIndentedString(streamProcessorArn)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    statusMessage: ").append(toIndentedString(statusMessage)).append("\n");
    sb.append("    creationTimestamp: ").append(toIndentedString(creationTimestamp)).append("\n");
    sb.append("    lastUpdateTimestamp: ").append(toIndentedString(lastUpdateTimestamp)).append("\n");
    sb.append("    input: ").append(toIndentedString(input)).append("\n");
    sb.append("    output: ").append(toIndentedString(output)).append("\n");
    sb.append("    roleArn: ").append(toIndentedString(roleArn)).append("\n");
    sb.append("    settings: ").append(toIndentedString(settings)).append("\n");
    sb.append("    notificationChannel: ").append(toIndentedString(notificationChannel)).append("\n");
    sb.append("    kmsKeyId: ").append(toIndentedString(kmsKeyId)).append("\n");
    sb.append("    regionsOfInterest: ").append(toIndentedString(regionsOfInterest)).append("\n");
    sb.append("    dataSharingPreference: ").append(toIndentedString(dataSharingPreference)).append("\n");
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
    openapiFields.add("Name");
    openapiFields.add("StreamProcessorArn");
    openapiFields.add("Status");
    openapiFields.add("StatusMessage");
    openapiFields.add("CreationTimestamp");
    openapiFields.add("LastUpdateTimestamp");
    openapiFields.add("Input");
    openapiFields.add("Output");
    openapiFields.add("RoleArn");
    openapiFields.add("Settings");
    openapiFields.add("NotificationChannel");
    openapiFields.add("KmsKeyId");
    openapiFields.add("RegionsOfInterest");
    openapiFields.add("DataSharingPreference");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DescribeStreamProcessorResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DescribeStreamProcessorResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DescribeStreamProcessorResponse is not found in the empty JSON string", DescribeStreamProcessorResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DescribeStreamProcessorResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DescribeStreamProcessorResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `Name`
      if (jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("Name"));
      }
      // validate the optional field `StreamProcessorArn`
      if (jsonObj.get("StreamProcessorArn") != null && !jsonObj.get("StreamProcessorArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("StreamProcessorArn"));
      }
      // validate the optional field `Status`
      if (jsonObj.get("Status") != null && !jsonObj.get("Status").isJsonNull()) {
        StreamProcessorStatus.validateJsonElement(jsonObj.get("Status"));
      }
      // validate the optional field `StatusMessage`
      if (jsonObj.get("StatusMessage") != null && !jsonObj.get("StatusMessage").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("StatusMessage"));
      }
      // validate the optional field `CreationTimestamp`
      if (jsonObj.get("CreationTimestamp") != null && !jsonObj.get("CreationTimestamp").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("CreationTimestamp"));
      }
      // validate the optional field `LastUpdateTimestamp`
      if (jsonObj.get("LastUpdateTimestamp") != null && !jsonObj.get("LastUpdateTimestamp").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("LastUpdateTimestamp"));
      }
      // validate the optional field `Input`
      if (jsonObj.get("Input") != null && !jsonObj.get("Input").isJsonNull()) {
        DescribeStreamProcessorResponseInput.validateJsonElement(jsonObj.get("Input"));
      }
      // validate the optional field `Output`
      if (jsonObj.get("Output") != null && !jsonObj.get("Output").isJsonNull()) {
        DescribeStreamProcessorResponseOutput.validateJsonElement(jsonObj.get("Output"));
      }
      // validate the optional field `RoleArn`
      if (jsonObj.get("RoleArn") != null && !jsonObj.get("RoleArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("RoleArn"));
      }
      // validate the optional field `Settings`
      if (jsonObj.get("Settings") != null && !jsonObj.get("Settings").isJsonNull()) {
        CreateStreamProcessorRequestSettings.validateJsonElement(jsonObj.get("Settings"));
      }
      // validate the optional field `NotificationChannel`
      if (jsonObj.get("NotificationChannel") != null && !jsonObj.get("NotificationChannel").isJsonNull()) {
        StreamProcessorNotificationChannel.validateJsonElement(jsonObj.get("NotificationChannel"));
      }
      // validate the optional field `KmsKeyId`
      if (jsonObj.get("KmsKeyId") != null && !jsonObj.get("KmsKeyId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("KmsKeyId"));
      }
      // validate the optional field `RegionsOfInterest`
      if (jsonObj.get("RegionsOfInterest") != null && !jsonObj.get("RegionsOfInterest").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("RegionsOfInterest"));
      }
      // validate the optional field `DataSharingPreference`
      if (jsonObj.get("DataSharingPreference") != null && !jsonObj.get("DataSharingPreference").isJsonNull()) {
        CreateStreamProcessorRequestDataSharingPreference.validateJsonElement(jsonObj.get("DataSharingPreference"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DescribeStreamProcessorResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DescribeStreamProcessorResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DescribeStreamProcessorResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DescribeStreamProcessorResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<DescribeStreamProcessorResponse>() {
           @Override
           public void write(JsonWriter out, DescribeStreamProcessorResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DescribeStreamProcessorResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DescribeStreamProcessorResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DescribeStreamProcessorResponse
   * @throws IOException if the JSON string is invalid with respect to DescribeStreamProcessorResponse
   */
  public static DescribeStreamProcessorResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DescribeStreamProcessorResponse.class);
  }

  /**
   * Convert an instance of DescribeStreamProcessorResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

