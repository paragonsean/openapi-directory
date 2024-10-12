/*
 * Quick start - Telematics SDK
 * # Introduction We have prepared a set of APIs for quick start to integrate telematics SDK that powers mobile telematics inside 3rd party mobile applications.  * [CONTACT US](https://telematicssdk.com) * [SANDBOX](https://userdatahub.com) * [DEV.PORTAL](https://docs.telematicssdk.com) * [DEMO APP](https://raxeltelematics.com/telematics-app)   # Overview Datamotion provides telematics infrastructure for mobile applications.   Telematics SDK turns any smartphone into telematics data gathering device to collect Location, driving and behavior data. API services unlocks power of your mobile application  There are 3 groups of methods: * 1 - user management * 2 - statistics for mobile app * 3 - statistics for back-end(s)  in certain cases you will need SNS or any other notification services. read more [here](https://docs.telematicssdk.com/platform-features/sns) # Possible architecture  There are three common schemes that are used by our clients. These schemes can be combined * Collect, Process, Store (required: 1&2) * Collect, Process (required: 1& sns) * Collect (required 1&sns)   ## Collect, Process, Store ![Collect, Process, Store](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection%2C+processing%2C+storage)  ## Collect, Process ![Collect, Process](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+and+processing)  ## Collect ![Collect](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+only)  *** ![Telematic sdk](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Github/transportation_small.png)  # Common use-cases: * Safe and efficient driving * Usage-based insurance * Safe driving assessment * Driver assessment * Trip log * Geo-analysis * Accident monitoring * Driving engagements * Location based services * Realtime Tracking and beyond  # How to start * Register a [SANDBOX ACCOUNT](https://userdatahub.com) * Get [CREDENTIALS](https://docs.userdatahub.com/sandbox/credentials)  * Follow the guide from [DEVELOPER POERTAL](https://docs.telematicssdk.com)  # Authentication To create a user on datamotion platform, you require to use InstanceID and InstanceKEY. You can get it in Datahub -> management -> user-service credentials  Once you create a user, you will get Device token, JWT token and refresh token. then, you will use it for APIs
 *
 * The version of the OpenAPI document: 1.0.0
 * 
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
import java.math.BigDecimal;
import java.util.Arrays;

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
 * UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:38.418404-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner {
  public static final String SERIALIZED_NAME_ACCELERATION_SCORE = "AccelerationScore";
  @SerializedName(SERIALIZED_NAME_ACCELERATION_SCORE)
  private BigDecimal accelerationScore;

  public static final String SERIALIZED_NAME_APP_ID = "AppId";
  @SerializedName(SERIALIZED_NAME_APP_ID)
  private String appId;

  public static final String SERIALIZED_NAME_BRAKING_SCORE = "BrakingScore";
  @SerializedName(SERIALIZED_NAME_BRAKING_SCORE)
  private BigDecimal brakingScore;

  public static final String SERIALIZED_NAME_CALC_DATE = "CalcDate";
  @SerializedName(SERIALIZED_NAME_CALC_DATE)
  private String calcDate;

  public static final String SERIALIZED_NAME_COMPANY_ID = "CompanyId";
  @SerializedName(SERIALIZED_NAME_COMPANY_ID)
  private String companyId;

  public static final String SERIALIZED_NAME_CORNERING_SCORE = "CorneringScore";
  @SerializedName(SERIALIZED_NAME_CORNERING_SCORE)
  private BigDecimal corneringScore;

  public static final String SERIALIZED_NAME_DEVICE_TOKEN = "DeviceToken";
  @SerializedName(SERIALIZED_NAME_DEVICE_TOKEN)
  private String deviceToken;

  public static final String SERIALIZED_NAME_DISTRACTED_SCORE = "DistractedScore";
  @SerializedName(SERIALIZED_NAME_DISTRACTED_SCORE)
  private BigDecimal distractedScore;

  public static final String SERIALIZED_NAME_INSTANCE_ID = "InstanceId";
  @SerializedName(SERIALIZED_NAME_INSTANCE_ID)
  private String instanceId;

  public static final String SERIALIZED_NAME_OVERALL_SCORE = "OverallScore";
  @SerializedName(SERIALIZED_NAME_OVERALL_SCORE)
  private BigDecimal overallScore;

  public static final String SERIALIZED_NAME_SPEEDING_SCORE = "SpeedingScore";
  @SerializedName(SERIALIZED_NAME_SPEEDING_SCORE)
  private BigDecimal speedingScore;

  public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner() {
  }

  public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner accelerationScore(BigDecimal accelerationScore) {
    this.accelerationScore = accelerationScore;
    return this;
  }

  /**
   * Get accelerationScore
   * @return accelerationScore
   */
  @javax.annotation.Nullable
  public BigDecimal getAccelerationScore() {
    return accelerationScore;
  }

  public void setAccelerationScore(BigDecimal accelerationScore) {
    this.accelerationScore = accelerationScore;
  }


  public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner appId(String appId) {
    this.appId = appId;
    return this;
  }

  /**
   * Get appId
   * @return appId
   */
  @javax.annotation.Nullable
  public String getAppId() {
    return appId;
  }

  public void setAppId(String appId) {
    this.appId = appId;
  }


  public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner brakingScore(BigDecimal brakingScore) {
    this.brakingScore = brakingScore;
    return this;
  }

  /**
   * Get brakingScore
   * @return brakingScore
   */
  @javax.annotation.Nullable
  public BigDecimal getBrakingScore() {
    return brakingScore;
  }

  public void setBrakingScore(BigDecimal brakingScore) {
    this.brakingScore = brakingScore;
  }


  public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner calcDate(String calcDate) {
    this.calcDate = calcDate;
    return this;
  }

  /**
   * Get calcDate
   * @return calcDate
   */
  @javax.annotation.Nullable
  public String getCalcDate() {
    return calcDate;
  }

  public void setCalcDate(String calcDate) {
    this.calcDate = calcDate;
  }


  public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner companyId(String companyId) {
    this.companyId = companyId;
    return this;
  }

  /**
   * Get companyId
   * @return companyId
   */
  @javax.annotation.Nullable
  public String getCompanyId() {
    return companyId;
  }

  public void setCompanyId(String companyId) {
    this.companyId = companyId;
  }


  public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner corneringScore(BigDecimal corneringScore) {
    this.corneringScore = corneringScore;
    return this;
  }

  /**
   * Get corneringScore
   * @return corneringScore
   */
  @javax.annotation.Nullable
  public BigDecimal getCorneringScore() {
    return corneringScore;
  }

  public void setCorneringScore(BigDecimal corneringScore) {
    this.corneringScore = corneringScore;
  }


  public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner deviceToken(String deviceToken) {
    this.deviceToken = deviceToken;
    return this;
  }

  /**
   * Get deviceToken
   * @return deviceToken
   */
  @javax.annotation.Nullable
  public String getDeviceToken() {
    return deviceToken;
  }

  public void setDeviceToken(String deviceToken) {
    this.deviceToken = deviceToken;
  }


  public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner distractedScore(BigDecimal distractedScore) {
    this.distractedScore = distractedScore;
    return this;
  }

  /**
   * Get distractedScore
   * @return distractedScore
   */
  @javax.annotation.Nullable
  public BigDecimal getDistractedScore() {
    return distractedScore;
  }

  public void setDistractedScore(BigDecimal distractedScore) {
    this.distractedScore = distractedScore;
  }


  public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner instanceId(String instanceId) {
    this.instanceId = instanceId;
    return this;
  }

  /**
   * Get instanceId
   * @return instanceId
   */
  @javax.annotation.Nullable
  public String getInstanceId() {
    return instanceId;
  }

  public void setInstanceId(String instanceId) {
    this.instanceId = instanceId;
  }


  public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner overallScore(BigDecimal overallScore) {
    this.overallScore = overallScore;
    return this;
  }

  /**
   * Get overallScore
   * @return overallScore
   */
  @javax.annotation.Nullable
  public BigDecimal getOverallScore() {
    return overallScore;
  }

  public void setOverallScore(BigDecimal overallScore) {
    this.overallScore = overallScore;
  }


  public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner speedingScore(BigDecimal speedingScore) {
    this.speedingScore = speedingScore;
    return this;
  }

  /**
   * Get speedingScore
   * @return speedingScore
   */
  @javax.annotation.Nullable
  public BigDecimal getSpeedingScore() {
    return speedingScore;
  }

  public void setSpeedingScore(BigDecimal speedingScore) {
    this.speedingScore = speedingScore;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner userSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner = (UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner) o;
    return Objects.equals(this.accelerationScore, userSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.accelerationScore) &&
        Objects.equals(this.appId, userSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.appId) &&
        Objects.equals(this.brakingScore, userSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.brakingScore) &&
        Objects.equals(this.calcDate, userSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.calcDate) &&
        Objects.equals(this.companyId, userSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.companyId) &&
        Objects.equals(this.corneringScore, userSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.corneringScore) &&
        Objects.equals(this.deviceToken, userSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.deviceToken) &&
        Objects.equals(this.distractedScore, userSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.distractedScore) &&
        Objects.equals(this.instanceId, userSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.instanceId) &&
        Objects.equals(this.overallScore, userSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.overallScore) &&
        Objects.equals(this.speedingScore, userSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.speedingScore);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accelerationScore, appId, brakingScore, calcDate, companyId, corneringScore, deviceToken, distractedScore, instanceId, overallScore, speedingScore);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner {\n");
    sb.append("    accelerationScore: ").append(toIndentedString(accelerationScore)).append("\n");
    sb.append("    appId: ").append(toIndentedString(appId)).append("\n");
    sb.append("    brakingScore: ").append(toIndentedString(brakingScore)).append("\n");
    sb.append("    calcDate: ").append(toIndentedString(calcDate)).append("\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    corneringScore: ").append(toIndentedString(corneringScore)).append("\n");
    sb.append("    deviceToken: ").append(toIndentedString(deviceToken)).append("\n");
    sb.append("    distractedScore: ").append(toIndentedString(distractedScore)).append("\n");
    sb.append("    instanceId: ").append(toIndentedString(instanceId)).append("\n");
    sb.append("    overallScore: ").append(toIndentedString(overallScore)).append("\n");
    sb.append("    speedingScore: ").append(toIndentedString(speedingScore)).append("\n");
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
    openapiFields.add("AccelerationScore");
    openapiFields.add("AppId");
    openapiFields.add("BrakingScore");
    openapiFields.add("CalcDate");
    openapiFields.add("CompanyId");
    openapiFields.add("CorneringScore");
    openapiFields.add("DeviceToken");
    openapiFields.add("DistractedScore");
    openapiFields.add("InstanceId");
    openapiFields.add("OverallScore");
    openapiFields.add("SpeedingScore");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner is not found in the empty JSON string", UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("AppId") != null && !jsonObj.get("AppId").isJsonNull()) && !jsonObj.get("AppId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `AppId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("AppId").toString()));
      }
      if ((jsonObj.get("CalcDate") != null && !jsonObj.get("CalcDate").isJsonNull()) && !jsonObj.get("CalcDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CalcDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CalcDate").toString()));
      }
      if ((jsonObj.get("CompanyId") != null && !jsonObj.get("CompanyId").isJsonNull()) && !jsonObj.get("CompanyId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CompanyId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CompanyId").toString()));
      }
      if ((jsonObj.get("DeviceToken") != null && !jsonObj.get("DeviceToken").isJsonNull()) && !jsonObj.get("DeviceToken").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DeviceToken` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DeviceToken").toString()));
      }
      if ((jsonObj.get("InstanceId") != null && !jsonObj.get("InstanceId").isJsonNull()) && !jsonObj.get("InstanceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `InstanceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("InstanceId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.class));

       return (TypeAdapter<T>) new TypeAdapter<UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner>() {
           @Override
           public void write(JsonWriter out, UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner
   * @throws IOException if the JSON string is invalid with respect to UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner
   */
  public static UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner.class);
  }

  /**
   * Convert an instance of UserSafeScoringDailyValueV1ScoringsIndividualDaily200ResponseResultInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

