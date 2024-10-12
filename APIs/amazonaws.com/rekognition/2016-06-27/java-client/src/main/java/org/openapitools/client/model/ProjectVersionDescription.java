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
import org.openapitools.client.model.ProjectVersionDescriptionEvaluationResult;
import org.openapitools.client.model.ProjectVersionDescriptionManifestSummary;
import org.openapitools.client.model.ProjectVersionDescriptionOutputConfig;
import org.openapitools.client.model.ProjectVersionDescriptionTestingDataResult;
import org.openapitools.client.model.ProjectVersionDescriptionTrainingDataResult;
import org.openapitools.client.model.ProjectVersionStatus;

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
 * A description of a version of an Amazon Rekognition Custom Labels model.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:27:22.127926-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProjectVersionDescription {
  public static final String SERIALIZED_NAME_PROJECT_VERSION_ARN = "ProjectVersionArn";
  @SerializedName(SERIALIZED_NAME_PROJECT_VERSION_ARN)
  private String projectVersionArn;

  public static final String SERIALIZED_NAME_CREATION_TIMESTAMP = "CreationTimestamp";
  @SerializedName(SERIALIZED_NAME_CREATION_TIMESTAMP)
  private OffsetDateTime creationTimestamp;

  public static final String SERIALIZED_NAME_MIN_INFERENCE_UNITS = "MinInferenceUnits";
  @SerializedName(SERIALIZED_NAME_MIN_INFERENCE_UNITS)
  private Integer minInferenceUnits;

  public static final String SERIALIZED_NAME_STATUS = "Status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private ProjectVersionStatus status;

  public static final String SERIALIZED_NAME_STATUS_MESSAGE = "StatusMessage";
  @SerializedName(SERIALIZED_NAME_STATUS_MESSAGE)
  private String statusMessage;

  public static final String SERIALIZED_NAME_BILLABLE_TRAINING_TIME_IN_SECONDS = "BillableTrainingTimeInSeconds";
  @SerializedName(SERIALIZED_NAME_BILLABLE_TRAINING_TIME_IN_SECONDS)
  private Integer billableTrainingTimeInSeconds;

  public static final String SERIALIZED_NAME_TRAINING_END_TIMESTAMP = "TrainingEndTimestamp";
  @SerializedName(SERIALIZED_NAME_TRAINING_END_TIMESTAMP)
  private OffsetDateTime trainingEndTimestamp;

  public static final String SERIALIZED_NAME_OUTPUT_CONFIG = "OutputConfig";
  @SerializedName(SERIALIZED_NAME_OUTPUT_CONFIG)
  private ProjectVersionDescriptionOutputConfig outputConfig;

  public static final String SERIALIZED_NAME_TRAINING_DATA_RESULT = "TrainingDataResult";
  @SerializedName(SERIALIZED_NAME_TRAINING_DATA_RESULT)
  private ProjectVersionDescriptionTrainingDataResult trainingDataResult;

  public static final String SERIALIZED_NAME_TESTING_DATA_RESULT = "TestingDataResult";
  @SerializedName(SERIALIZED_NAME_TESTING_DATA_RESULT)
  private ProjectVersionDescriptionTestingDataResult testingDataResult;

  public static final String SERIALIZED_NAME_EVALUATION_RESULT = "EvaluationResult";
  @SerializedName(SERIALIZED_NAME_EVALUATION_RESULT)
  private ProjectVersionDescriptionEvaluationResult evaluationResult;

  public static final String SERIALIZED_NAME_MANIFEST_SUMMARY = "ManifestSummary";
  @SerializedName(SERIALIZED_NAME_MANIFEST_SUMMARY)
  private ProjectVersionDescriptionManifestSummary manifestSummary;

  public static final String SERIALIZED_NAME_KMS_KEY_ID = "KmsKeyId";
  @SerializedName(SERIALIZED_NAME_KMS_KEY_ID)
  private String kmsKeyId;

  public static final String SERIALIZED_NAME_MAX_INFERENCE_UNITS = "MaxInferenceUnits";
  @SerializedName(SERIALIZED_NAME_MAX_INFERENCE_UNITS)
  private Integer maxInferenceUnits;

  public static final String SERIALIZED_NAME_SOURCE_PROJECT_VERSION_ARN = "SourceProjectVersionArn";
  @SerializedName(SERIALIZED_NAME_SOURCE_PROJECT_VERSION_ARN)
  private String sourceProjectVersionArn;

  public ProjectVersionDescription() {
  }

  public ProjectVersionDescription projectVersionArn(String projectVersionArn) {
    this.projectVersionArn = projectVersionArn;
    return this;
  }

  /**
   * Get projectVersionArn
   * @return projectVersionArn
   */
  @javax.annotation.Nullable
  public String getProjectVersionArn() {
    return projectVersionArn;
  }

  public void setProjectVersionArn(String projectVersionArn) {
    this.projectVersionArn = projectVersionArn;
  }


  public ProjectVersionDescription creationTimestamp(OffsetDateTime creationTimestamp) {
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


  public ProjectVersionDescription minInferenceUnits(Integer minInferenceUnits) {
    this.minInferenceUnits = minInferenceUnits;
    return this;
  }

  /**
   * Get minInferenceUnits
   * @return minInferenceUnits
   */
  @javax.annotation.Nullable
  public Integer getMinInferenceUnits() {
    return minInferenceUnits;
  }

  public void setMinInferenceUnits(Integer minInferenceUnits) {
    this.minInferenceUnits = minInferenceUnits;
  }


  public ProjectVersionDescription status(ProjectVersionStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public ProjectVersionStatus getStatus() {
    return status;
  }

  public void setStatus(ProjectVersionStatus status) {
    this.status = status;
  }


  public ProjectVersionDescription statusMessage(String statusMessage) {
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


  public ProjectVersionDescription billableTrainingTimeInSeconds(Integer billableTrainingTimeInSeconds) {
    this.billableTrainingTimeInSeconds = billableTrainingTimeInSeconds;
    return this;
  }

  /**
   * Get billableTrainingTimeInSeconds
   * @return billableTrainingTimeInSeconds
   */
  @javax.annotation.Nullable
  public Integer getBillableTrainingTimeInSeconds() {
    return billableTrainingTimeInSeconds;
  }

  public void setBillableTrainingTimeInSeconds(Integer billableTrainingTimeInSeconds) {
    this.billableTrainingTimeInSeconds = billableTrainingTimeInSeconds;
  }


  public ProjectVersionDescription trainingEndTimestamp(OffsetDateTime trainingEndTimestamp) {
    this.trainingEndTimestamp = trainingEndTimestamp;
    return this;
  }

  /**
   * Get trainingEndTimestamp
   * @return trainingEndTimestamp
   */
  @javax.annotation.Nullable
  public OffsetDateTime getTrainingEndTimestamp() {
    return trainingEndTimestamp;
  }

  public void setTrainingEndTimestamp(OffsetDateTime trainingEndTimestamp) {
    this.trainingEndTimestamp = trainingEndTimestamp;
  }


  public ProjectVersionDescription outputConfig(ProjectVersionDescriptionOutputConfig outputConfig) {
    this.outputConfig = outputConfig;
    return this;
  }

  /**
   * Get outputConfig
   * @return outputConfig
   */
  @javax.annotation.Nullable
  public ProjectVersionDescriptionOutputConfig getOutputConfig() {
    return outputConfig;
  }

  public void setOutputConfig(ProjectVersionDescriptionOutputConfig outputConfig) {
    this.outputConfig = outputConfig;
  }


  public ProjectVersionDescription trainingDataResult(ProjectVersionDescriptionTrainingDataResult trainingDataResult) {
    this.trainingDataResult = trainingDataResult;
    return this;
  }

  /**
   * Get trainingDataResult
   * @return trainingDataResult
   */
  @javax.annotation.Nullable
  public ProjectVersionDescriptionTrainingDataResult getTrainingDataResult() {
    return trainingDataResult;
  }

  public void setTrainingDataResult(ProjectVersionDescriptionTrainingDataResult trainingDataResult) {
    this.trainingDataResult = trainingDataResult;
  }


  public ProjectVersionDescription testingDataResult(ProjectVersionDescriptionTestingDataResult testingDataResult) {
    this.testingDataResult = testingDataResult;
    return this;
  }

  /**
   * Get testingDataResult
   * @return testingDataResult
   */
  @javax.annotation.Nullable
  public ProjectVersionDescriptionTestingDataResult getTestingDataResult() {
    return testingDataResult;
  }

  public void setTestingDataResult(ProjectVersionDescriptionTestingDataResult testingDataResult) {
    this.testingDataResult = testingDataResult;
  }


  public ProjectVersionDescription evaluationResult(ProjectVersionDescriptionEvaluationResult evaluationResult) {
    this.evaluationResult = evaluationResult;
    return this;
  }

  /**
   * Get evaluationResult
   * @return evaluationResult
   */
  @javax.annotation.Nullable
  public ProjectVersionDescriptionEvaluationResult getEvaluationResult() {
    return evaluationResult;
  }

  public void setEvaluationResult(ProjectVersionDescriptionEvaluationResult evaluationResult) {
    this.evaluationResult = evaluationResult;
  }


  public ProjectVersionDescription manifestSummary(ProjectVersionDescriptionManifestSummary manifestSummary) {
    this.manifestSummary = manifestSummary;
    return this;
  }

  /**
   * Get manifestSummary
   * @return manifestSummary
   */
  @javax.annotation.Nullable
  public ProjectVersionDescriptionManifestSummary getManifestSummary() {
    return manifestSummary;
  }

  public void setManifestSummary(ProjectVersionDescriptionManifestSummary manifestSummary) {
    this.manifestSummary = manifestSummary;
  }


  public ProjectVersionDescription kmsKeyId(String kmsKeyId) {
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


  public ProjectVersionDescription maxInferenceUnits(Integer maxInferenceUnits) {
    this.maxInferenceUnits = maxInferenceUnits;
    return this;
  }

  /**
   * Get maxInferenceUnits
   * @return maxInferenceUnits
   */
  @javax.annotation.Nullable
  public Integer getMaxInferenceUnits() {
    return maxInferenceUnits;
  }

  public void setMaxInferenceUnits(Integer maxInferenceUnits) {
    this.maxInferenceUnits = maxInferenceUnits;
  }


  public ProjectVersionDescription sourceProjectVersionArn(String sourceProjectVersionArn) {
    this.sourceProjectVersionArn = sourceProjectVersionArn;
    return this;
  }

  /**
   * Get sourceProjectVersionArn
   * @return sourceProjectVersionArn
   */
  @javax.annotation.Nullable
  public String getSourceProjectVersionArn() {
    return sourceProjectVersionArn;
  }

  public void setSourceProjectVersionArn(String sourceProjectVersionArn) {
    this.sourceProjectVersionArn = sourceProjectVersionArn;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProjectVersionDescription projectVersionDescription = (ProjectVersionDescription) o;
    return Objects.equals(this.projectVersionArn, projectVersionDescription.projectVersionArn) &&
        Objects.equals(this.creationTimestamp, projectVersionDescription.creationTimestamp) &&
        Objects.equals(this.minInferenceUnits, projectVersionDescription.minInferenceUnits) &&
        Objects.equals(this.status, projectVersionDescription.status) &&
        Objects.equals(this.statusMessage, projectVersionDescription.statusMessage) &&
        Objects.equals(this.billableTrainingTimeInSeconds, projectVersionDescription.billableTrainingTimeInSeconds) &&
        Objects.equals(this.trainingEndTimestamp, projectVersionDescription.trainingEndTimestamp) &&
        Objects.equals(this.outputConfig, projectVersionDescription.outputConfig) &&
        Objects.equals(this.trainingDataResult, projectVersionDescription.trainingDataResult) &&
        Objects.equals(this.testingDataResult, projectVersionDescription.testingDataResult) &&
        Objects.equals(this.evaluationResult, projectVersionDescription.evaluationResult) &&
        Objects.equals(this.manifestSummary, projectVersionDescription.manifestSummary) &&
        Objects.equals(this.kmsKeyId, projectVersionDescription.kmsKeyId) &&
        Objects.equals(this.maxInferenceUnits, projectVersionDescription.maxInferenceUnits) &&
        Objects.equals(this.sourceProjectVersionArn, projectVersionDescription.sourceProjectVersionArn);
  }

  @Override
  public int hashCode() {
    return Objects.hash(projectVersionArn, creationTimestamp, minInferenceUnits, status, statusMessage, billableTrainingTimeInSeconds, trainingEndTimestamp, outputConfig, trainingDataResult, testingDataResult, evaluationResult, manifestSummary, kmsKeyId, maxInferenceUnits, sourceProjectVersionArn);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProjectVersionDescription {\n");
    sb.append("    projectVersionArn: ").append(toIndentedString(projectVersionArn)).append("\n");
    sb.append("    creationTimestamp: ").append(toIndentedString(creationTimestamp)).append("\n");
    sb.append("    minInferenceUnits: ").append(toIndentedString(minInferenceUnits)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    statusMessage: ").append(toIndentedString(statusMessage)).append("\n");
    sb.append("    billableTrainingTimeInSeconds: ").append(toIndentedString(billableTrainingTimeInSeconds)).append("\n");
    sb.append("    trainingEndTimestamp: ").append(toIndentedString(trainingEndTimestamp)).append("\n");
    sb.append("    outputConfig: ").append(toIndentedString(outputConfig)).append("\n");
    sb.append("    trainingDataResult: ").append(toIndentedString(trainingDataResult)).append("\n");
    sb.append("    testingDataResult: ").append(toIndentedString(testingDataResult)).append("\n");
    sb.append("    evaluationResult: ").append(toIndentedString(evaluationResult)).append("\n");
    sb.append("    manifestSummary: ").append(toIndentedString(manifestSummary)).append("\n");
    sb.append("    kmsKeyId: ").append(toIndentedString(kmsKeyId)).append("\n");
    sb.append("    maxInferenceUnits: ").append(toIndentedString(maxInferenceUnits)).append("\n");
    sb.append("    sourceProjectVersionArn: ").append(toIndentedString(sourceProjectVersionArn)).append("\n");
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
    openapiFields.add("ProjectVersionArn");
    openapiFields.add("CreationTimestamp");
    openapiFields.add("MinInferenceUnits");
    openapiFields.add("Status");
    openapiFields.add("StatusMessage");
    openapiFields.add("BillableTrainingTimeInSeconds");
    openapiFields.add("TrainingEndTimestamp");
    openapiFields.add("OutputConfig");
    openapiFields.add("TrainingDataResult");
    openapiFields.add("TestingDataResult");
    openapiFields.add("EvaluationResult");
    openapiFields.add("ManifestSummary");
    openapiFields.add("KmsKeyId");
    openapiFields.add("MaxInferenceUnits");
    openapiFields.add("SourceProjectVersionArn");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProjectVersionDescription
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProjectVersionDescription.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProjectVersionDescription is not found in the empty JSON string", ProjectVersionDescription.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProjectVersionDescription.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProjectVersionDescription` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `ProjectVersionArn`
      if (jsonObj.get("ProjectVersionArn") != null && !jsonObj.get("ProjectVersionArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("ProjectVersionArn"));
      }
      // validate the optional field `CreationTimestamp`
      if (jsonObj.get("CreationTimestamp") != null && !jsonObj.get("CreationTimestamp").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("CreationTimestamp"));
      }
      // validate the optional field `MinInferenceUnits`
      if (jsonObj.get("MinInferenceUnits") != null && !jsonObj.get("MinInferenceUnits").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("MinInferenceUnits"));
      }
      // validate the optional field `Status`
      if (jsonObj.get("Status") != null && !jsonObj.get("Status").isJsonNull()) {
        ProjectVersionStatus.validateJsonElement(jsonObj.get("Status"));
      }
      // validate the optional field `StatusMessage`
      if (jsonObj.get("StatusMessage") != null && !jsonObj.get("StatusMessage").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("StatusMessage"));
      }
      // validate the optional field `BillableTrainingTimeInSeconds`
      if (jsonObj.get("BillableTrainingTimeInSeconds") != null && !jsonObj.get("BillableTrainingTimeInSeconds").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("BillableTrainingTimeInSeconds"));
      }
      // validate the optional field `TrainingEndTimestamp`
      if (jsonObj.get("TrainingEndTimestamp") != null && !jsonObj.get("TrainingEndTimestamp").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("TrainingEndTimestamp"));
      }
      // validate the optional field `OutputConfig`
      if (jsonObj.get("OutputConfig") != null && !jsonObj.get("OutputConfig").isJsonNull()) {
        ProjectVersionDescriptionOutputConfig.validateJsonElement(jsonObj.get("OutputConfig"));
      }
      // validate the optional field `TrainingDataResult`
      if (jsonObj.get("TrainingDataResult") != null && !jsonObj.get("TrainingDataResult").isJsonNull()) {
        ProjectVersionDescriptionTrainingDataResult.validateJsonElement(jsonObj.get("TrainingDataResult"));
      }
      // validate the optional field `TestingDataResult`
      if (jsonObj.get("TestingDataResult") != null && !jsonObj.get("TestingDataResult").isJsonNull()) {
        ProjectVersionDescriptionTestingDataResult.validateJsonElement(jsonObj.get("TestingDataResult"));
      }
      // validate the optional field `EvaluationResult`
      if (jsonObj.get("EvaluationResult") != null && !jsonObj.get("EvaluationResult").isJsonNull()) {
        ProjectVersionDescriptionEvaluationResult.validateJsonElement(jsonObj.get("EvaluationResult"));
      }
      // validate the optional field `ManifestSummary`
      if (jsonObj.get("ManifestSummary") != null && !jsonObj.get("ManifestSummary").isJsonNull()) {
        ProjectVersionDescriptionManifestSummary.validateJsonElement(jsonObj.get("ManifestSummary"));
      }
      // validate the optional field `KmsKeyId`
      if (jsonObj.get("KmsKeyId") != null && !jsonObj.get("KmsKeyId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("KmsKeyId"));
      }
      // validate the optional field `MaxInferenceUnits`
      if (jsonObj.get("MaxInferenceUnits") != null && !jsonObj.get("MaxInferenceUnits").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("MaxInferenceUnits"));
      }
      // validate the optional field `SourceProjectVersionArn`
      if (jsonObj.get("SourceProjectVersionArn") != null && !jsonObj.get("SourceProjectVersionArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("SourceProjectVersionArn"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProjectVersionDescription.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProjectVersionDescription' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProjectVersionDescription> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProjectVersionDescription.class));

       return (TypeAdapter<T>) new TypeAdapter<ProjectVersionDescription>() {
           @Override
           public void write(JsonWriter out, ProjectVersionDescription value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProjectVersionDescription read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProjectVersionDescription given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProjectVersionDescription
   * @throws IOException if the JSON string is invalid with respect to ProjectVersionDescription
   */
  public static ProjectVersionDescription fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProjectVersionDescription.class);
  }

  /**
   * Convert an instance of ProjectVersionDescription to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

