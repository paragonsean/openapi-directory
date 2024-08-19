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
import org.openapitools.client.model.FaceDetailAgeRange;
import org.openapitools.client.model.FaceDetailBeard;
import org.openapitools.client.model.FaceDetailBoundingBox;
import org.openapitools.client.model.FaceDetailEyeDirection;
import org.openapitools.client.model.FaceDetailEyeglasses;
import org.openapitools.client.model.FaceDetailEyesOpen;
import org.openapitools.client.model.FaceDetailFaceOccluded;
import org.openapitools.client.model.FaceDetailGender;
import org.openapitools.client.model.FaceDetailMouthOpen;
import org.openapitools.client.model.FaceDetailMustache;
import org.openapitools.client.model.FaceDetailPose;
import org.openapitools.client.model.FaceDetailQuality;
import org.openapitools.client.model.FaceDetailSmile;
import org.openapitools.client.model.FaceDetailSunglasses;

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
 * CelebrityDetailFace
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:27:22.127926-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CelebrityDetailFace {
  public static final String SERIALIZED_NAME_BOUNDING_BOX = "BoundingBox";
  @SerializedName(SERIALIZED_NAME_BOUNDING_BOX)
  private FaceDetailBoundingBox boundingBox;

  public static final String SERIALIZED_NAME_AGE_RANGE = "AgeRange";
  @SerializedName(SERIALIZED_NAME_AGE_RANGE)
  private FaceDetailAgeRange ageRange;

  public static final String SERIALIZED_NAME_SMILE = "Smile";
  @SerializedName(SERIALIZED_NAME_SMILE)
  private FaceDetailSmile smile;

  public static final String SERIALIZED_NAME_EYEGLASSES = "Eyeglasses";
  @SerializedName(SERIALIZED_NAME_EYEGLASSES)
  private FaceDetailEyeglasses eyeglasses;

  public static final String SERIALIZED_NAME_SUNGLASSES = "Sunglasses";
  @SerializedName(SERIALIZED_NAME_SUNGLASSES)
  private FaceDetailSunglasses sunglasses;

  public static final String SERIALIZED_NAME_GENDER = "Gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private FaceDetailGender gender;

  public static final String SERIALIZED_NAME_BEARD = "Beard";
  @SerializedName(SERIALIZED_NAME_BEARD)
  private FaceDetailBeard beard;

  public static final String SERIALIZED_NAME_MUSTACHE = "Mustache";
  @SerializedName(SERIALIZED_NAME_MUSTACHE)
  private FaceDetailMustache mustache;

  public static final String SERIALIZED_NAME_EYES_OPEN = "EyesOpen";
  @SerializedName(SERIALIZED_NAME_EYES_OPEN)
  private FaceDetailEyesOpen eyesOpen;

  public static final String SERIALIZED_NAME_MOUTH_OPEN = "MouthOpen";
  @SerializedName(SERIALIZED_NAME_MOUTH_OPEN)
  private FaceDetailMouthOpen mouthOpen;

  public static final String SERIALIZED_NAME_EMOTIONS = "Emotions";
  @SerializedName(SERIALIZED_NAME_EMOTIONS)
  private List emotions;

  public static final String SERIALIZED_NAME_LANDMARKS = "Landmarks";
  @SerializedName(SERIALIZED_NAME_LANDMARKS)
  private List landmarks;

  public static final String SERIALIZED_NAME_POSE = "Pose";
  @SerializedName(SERIALIZED_NAME_POSE)
  private FaceDetailPose pose;

  public static final String SERIALIZED_NAME_QUALITY = "Quality";
  @SerializedName(SERIALIZED_NAME_QUALITY)
  private FaceDetailQuality quality;

  public static final String SERIALIZED_NAME_CONFIDENCE = "Confidence";
  @SerializedName(SERIALIZED_NAME_CONFIDENCE)
  private Float confidence;

  public static final String SERIALIZED_NAME_FACE_OCCLUDED = "FaceOccluded";
  @SerializedName(SERIALIZED_NAME_FACE_OCCLUDED)
  private FaceDetailFaceOccluded faceOccluded;

  public static final String SERIALIZED_NAME_EYE_DIRECTION = "EyeDirection";
  @SerializedName(SERIALIZED_NAME_EYE_DIRECTION)
  private FaceDetailEyeDirection eyeDirection;

  public CelebrityDetailFace() {
  }

  public CelebrityDetailFace boundingBox(FaceDetailBoundingBox boundingBox) {
    this.boundingBox = boundingBox;
    return this;
  }

  /**
   * Get boundingBox
   * @return boundingBox
   */
  @javax.annotation.Nullable
  public FaceDetailBoundingBox getBoundingBox() {
    return boundingBox;
  }

  public void setBoundingBox(FaceDetailBoundingBox boundingBox) {
    this.boundingBox = boundingBox;
  }


  public CelebrityDetailFace ageRange(FaceDetailAgeRange ageRange) {
    this.ageRange = ageRange;
    return this;
  }

  /**
   * Get ageRange
   * @return ageRange
   */
  @javax.annotation.Nullable
  public FaceDetailAgeRange getAgeRange() {
    return ageRange;
  }

  public void setAgeRange(FaceDetailAgeRange ageRange) {
    this.ageRange = ageRange;
  }


  public CelebrityDetailFace smile(FaceDetailSmile smile) {
    this.smile = smile;
    return this;
  }

  /**
   * Get smile
   * @return smile
   */
  @javax.annotation.Nullable
  public FaceDetailSmile getSmile() {
    return smile;
  }

  public void setSmile(FaceDetailSmile smile) {
    this.smile = smile;
  }


  public CelebrityDetailFace eyeglasses(FaceDetailEyeglasses eyeglasses) {
    this.eyeglasses = eyeglasses;
    return this;
  }

  /**
   * Get eyeglasses
   * @return eyeglasses
   */
  @javax.annotation.Nullable
  public FaceDetailEyeglasses getEyeglasses() {
    return eyeglasses;
  }

  public void setEyeglasses(FaceDetailEyeglasses eyeglasses) {
    this.eyeglasses = eyeglasses;
  }


  public CelebrityDetailFace sunglasses(FaceDetailSunglasses sunglasses) {
    this.sunglasses = sunglasses;
    return this;
  }

  /**
   * Get sunglasses
   * @return sunglasses
   */
  @javax.annotation.Nullable
  public FaceDetailSunglasses getSunglasses() {
    return sunglasses;
  }

  public void setSunglasses(FaceDetailSunglasses sunglasses) {
    this.sunglasses = sunglasses;
  }


  public CelebrityDetailFace gender(FaceDetailGender gender) {
    this.gender = gender;
    return this;
  }

  /**
   * Get gender
   * @return gender
   */
  @javax.annotation.Nullable
  public FaceDetailGender getGender() {
    return gender;
  }

  public void setGender(FaceDetailGender gender) {
    this.gender = gender;
  }


  public CelebrityDetailFace beard(FaceDetailBeard beard) {
    this.beard = beard;
    return this;
  }

  /**
   * Get beard
   * @return beard
   */
  @javax.annotation.Nullable
  public FaceDetailBeard getBeard() {
    return beard;
  }

  public void setBeard(FaceDetailBeard beard) {
    this.beard = beard;
  }


  public CelebrityDetailFace mustache(FaceDetailMustache mustache) {
    this.mustache = mustache;
    return this;
  }

  /**
   * Get mustache
   * @return mustache
   */
  @javax.annotation.Nullable
  public FaceDetailMustache getMustache() {
    return mustache;
  }

  public void setMustache(FaceDetailMustache mustache) {
    this.mustache = mustache;
  }


  public CelebrityDetailFace eyesOpen(FaceDetailEyesOpen eyesOpen) {
    this.eyesOpen = eyesOpen;
    return this;
  }

  /**
   * Get eyesOpen
   * @return eyesOpen
   */
  @javax.annotation.Nullable
  public FaceDetailEyesOpen getEyesOpen() {
    return eyesOpen;
  }

  public void setEyesOpen(FaceDetailEyesOpen eyesOpen) {
    this.eyesOpen = eyesOpen;
  }


  public CelebrityDetailFace mouthOpen(FaceDetailMouthOpen mouthOpen) {
    this.mouthOpen = mouthOpen;
    return this;
  }

  /**
   * Get mouthOpen
   * @return mouthOpen
   */
  @javax.annotation.Nullable
  public FaceDetailMouthOpen getMouthOpen() {
    return mouthOpen;
  }

  public void setMouthOpen(FaceDetailMouthOpen mouthOpen) {
    this.mouthOpen = mouthOpen;
  }


  public CelebrityDetailFace emotions(List emotions) {
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


  public CelebrityDetailFace landmarks(List landmarks) {
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


  public CelebrityDetailFace pose(FaceDetailPose pose) {
    this.pose = pose;
    return this;
  }

  /**
   * Get pose
   * @return pose
   */
  @javax.annotation.Nullable
  public FaceDetailPose getPose() {
    return pose;
  }

  public void setPose(FaceDetailPose pose) {
    this.pose = pose;
  }


  public CelebrityDetailFace quality(FaceDetailQuality quality) {
    this.quality = quality;
    return this;
  }

  /**
   * Get quality
   * @return quality
   */
  @javax.annotation.Nullable
  public FaceDetailQuality getQuality() {
    return quality;
  }

  public void setQuality(FaceDetailQuality quality) {
    this.quality = quality;
  }


  public CelebrityDetailFace confidence(Float confidence) {
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


  public CelebrityDetailFace faceOccluded(FaceDetailFaceOccluded faceOccluded) {
    this.faceOccluded = faceOccluded;
    return this;
  }

  /**
   * Get faceOccluded
   * @return faceOccluded
   */
  @javax.annotation.Nullable
  public FaceDetailFaceOccluded getFaceOccluded() {
    return faceOccluded;
  }

  public void setFaceOccluded(FaceDetailFaceOccluded faceOccluded) {
    this.faceOccluded = faceOccluded;
  }


  public CelebrityDetailFace eyeDirection(FaceDetailEyeDirection eyeDirection) {
    this.eyeDirection = eyeDirection;
    return this;
  }

  /**
   * Get eyeDirection
   * @return eyeDirection
   */
  @javax.annotation.Nullable
  public FaceDetailEyeDirection getEyeDirection() {
    return eyeDirection;
  }

  public void setEyeDirection(FaceDetailEyeDirection eyeDirection) {
    this.eyeDirection = eyeDirection;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CelebrityDetailFace celebrityDetailFace = (CelebrityDetailFace) o;
    return Objects.equals(this.boundingBox, celebrityDetailFace.boundingBox) &&
        Objects.equals(this.ageRange, celebrityDetailFace.ageRange) &&
        Objects.equals(this.smile, celebrityDetailFace.smile) &&
        Objects.equals(this.eyeglasses, celebrityDetailFace.eyeglasses) &&
        Objects.equals(this.sunglasses, celebrityDetailFace.sunglasses) &&
        Objects.equals(this.gender, celebrityDetailFace.gender) &&
        Objects.equals(this.beard, celebrityDetailFace.beard) &&
        Objects.equals(this.mustache, celebrityDetailFace.mustache) &&
        Objects.equals(this.eyesOpen, celebrityDetailFace.eyesOpen) &&
        Objects.equals(this.mouthOpen, celebrityDetailFace.mouthOpen) &&
        Objects.equals(this.emotions, celebrityDetailFace.emotions) &&
        Objects.equals(this.landmarks, celebrityDetailFace.landmarks) &&
        Objects.equals(this.pose, celebrityDetailFace.pose) &&
        Objects.equals(this.quality, celebrityDetailFace.quality) &&
        Objects.equals(this.confidence, celebrityDetailFace.confidence) &&
        Objects.equals(this.faceOccluded, celebrityDetailFace.faceOccluded) &&
        Objects.equals(this.eyeDirection, celebrityDetailFace.eyeDirection);
  }

  @Override
  public int hashCode() {
    return Objects.hash(boundingBox, ageRange, smile, eyeglasses, sunglasses, gender, beard, mustache, eyesOpen, mouthOpen, emotions, landmarks, pose, quality, confidence, faceOccluded, eyeDirection);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CelebrityDetailFace {\n");
    sb.append("    boundingBox: ").append(toIndentedString(boundingBox)).append("\n");
    sb.append("    ageRange: ").append(toIndentedString(ageRange)).append("\n");
    sb.append("    smile: ").append(toIndentedString(smile)).append("\n");
    sb.append("    eyeglasses: ").append(toIndentedString(eyeglasses)).append("\n");
    sb.append("    sunglasses: ").append(toIndentedString(sunglasses)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    beard: ").append(toIndentedString(beard)).append("\n");
    sb.append("    mustache: ").append(toIndentedString(mustache)).append("\n");
    sb.append("    eyesOpen: ").append(toIndentedString(eyesOpen)).append("\n");
    sb.append("    mouthOpen: ").append(toIndentedString(mouthOpen)).append("\n");
    sb.append("    emotions: ").append(toIndentedString(emotions)).append("\n");
    sb.append("    landmarks: ").append(toIndentedString(landmarks)).append("\n");
    sb.append("    pose: ").append(toIndentedString(pose)).append("\n");
    sb.append("    quality: ").append(toIndentedString(quality)).append("\n");
    sb.append("    confidence: ").append(toIndentedString(confidence)).append("\n");
    sb.append("    faceOccluded: ").append(toIndentedString(faceOccluded)).append("\n");
    sb.append("    eyeDirection: ").append(toIndentedString(eyeDirection)).append("\n");
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
    openapiFields.add("AgeRange");
    openapiFields.add("Smile");
    openapiFields.add("Eyeglasses");
    openapiFields.add("Sunglasses");
    openapiFields.add("Gender");
    openapiFields.add("Beard");
    openapiFields.add("Mustache");
    openapiFields.add("EyesOpen");
    openapiFields.add("MouthOpen");
    openapiFields.add("Emotions");
    openapiFields.add("Landmarks");
    openapiFields.add("Pose");
    openapiFields.add("Quality");
    openapiFields.add("Confidence");
    openapiFields.add("FaceOccluded");
    openapiFields.add("EyeDirection");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CelebrityDetailFace
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CelebrityDetailFace.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CelebrityDetailFace is not found in the empty JSON string", CelebrityDetailFace.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CelebrityDetailFace.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CelebrityDetailFace` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `BoundingBox`
      if (jsonObj.get("BoundingBox") != null && !jsonObj.get("BoundingBox").isJsonNull()) {
        FaceDetailBoundingBox.validateJsonElement(jsonObj.get("BoundingBox"));
      }
      // validate the optional field `AgeRange`
      if (jsonObj.get("AgeRange") != null && !jsonObj.get("AgeRange").isJsonNull()) {
        FaceDetailAgeRange.validateJsonElement(jsonObj.get("AgeRange"));
      }
      // validate the optional field `Smile`
      if (jsonObj.get("Smile") != null && !jsonObj.get("Smile").isJsonNull()) {
        FaceDetailSmile.validateJsonElement(jsonObj.get("Smile"));
      }
      // validate the optional field `Eyeglasses`
      if (jsonObj.get("Eyeglasses") != null && !jsonObj.get("Eyeglasses").isJsonNull()) {
        FaceDetailEyeglasses.validateJsonElement(jsonObj.get("Eyeglasses"));
      }
      // validate the optional field `Sunglasses`
      if (jsonObj.get("Sunglasses") != null && !jsonObj.get("Sunglasses").isJsonNull()) {
        FaceDetailSunglasses.validateJsonElement(jsonObj.get("Sunglasses"));
      }
      // validate the optional field `Gender`
      if (jsonObj.get("Gender") != null && !jsonObj.get("Gender").isJsonNull()) {
        FaceDetailGender.validateJsonElement(jsonObj.get("Gender"));
      }
      // validate the optional field `Beard`
      if (jsonObj.get("Beard") != null && !jsonObj.get("Beard").isJsonNull()) {
        FaceDetailBeard.validateJsonElement(jsonObj.get("Beard"));
      }
      // validate the optional field `Mustache`
      if (jsonObj.get("Mustache") != null && !jsonObj.get("Mustache").isJsonNull()) {
        FaceDetailMustache.validateJsonElement(jsonObj.get("Mustache"));
      }
      // validate the optional field `EyesOpen`
      if (jsonObj.get("EyesOpen") != null && !jsonObj.get("EyesOpen").isJsonNull()) {
        FaceDetailEyesOpen.validateJsonElement(jsonObj.get("EyesOpen"));
      }
      // validate the optional field `MouthOpen`
      if (jsonObj.get("MouthOpen") != null && !jsonObj.get("MouthOpen").isJsonNull()) {
        FaceDetailMouthOpen.validateJsonElement(jsonObj.get("MouthOpen"));
      }
      // validate the optional field `Emotions`
      if (jsonObj.get("Emotions") != null && !jsonObj.get("Emotions").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("Emotions"));
      }
      // validate the optional field `Landmarks`
      if (jsonObj.get("Landmarks") != null && !jsonObj.get("Landmarks").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("Landmarks"));
      }
      // validate the optional field `Pose`
      if (jsonObj.get("Pose") != null && !jsonObj.get("Pose").isJsonNull()) {
        FaceDetailPose.validateJsonElement(jsonObj.get("Pose"));
      }
      // validate the optional field `Quality`
      if (jsonObj.get("Quality") != null && !jsonObj.get("Quality").isJsonNull()) {
        FaceDetailQuality.validateJsonElement(jsonObj.get("Quality"));
      }
      // validate the optional field `Confidence`
      if (jsonObj.get("Confidence") != null && !jsonObj.get("Confidence").isJsonNull()) {
        Float.validateJsonElement(jsonObj.get("Confidence"));
      }
      // validate the optional field `FaceOccluded`
      if (jsonObj.get("FaceOccluded") != null && !jsonObj.get("FaceOccluded").isJsonNull()) {
        FaceDetailFaceOccluded.validateJsonElement(jsonObj.get("FaceOccluded"));
      }
      // validate the optional field `EyeDirection`
      if (jsonObj.get("EyeDirection") != null && !jsonObj.get("EyeDirection").isJsonNull()) {
        FaceDetailEyeDirection.validateJsonElement(jsonObj.get("EyeDirection"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CelebrityDetailFace.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CelebrityDetailFace' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CelebrityDetailFace> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CelebrityDetailFace.class));

       return (TypeAdapter<T>) new TypeAdapter<CelebrityDetailFace>() {
           @Override
           public void write(JsonWriter out, CelebrityDetailFace value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CelebrityDetailFace read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CelebrityDetailFace given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CelebrityDetailFace
   * @throws IOException if the JSON string is invalid with respect to CelebrityDetailFace
   */
  public static CelebrityDetailFace fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CelebrityDetailFace.class);
  }

  /**
   * Convert an instance of CelebrityDetailFace to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

