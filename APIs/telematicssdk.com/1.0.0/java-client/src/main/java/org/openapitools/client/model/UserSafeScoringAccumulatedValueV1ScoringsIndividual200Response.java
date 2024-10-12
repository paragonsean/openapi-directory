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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.UserSafeScoringAccumulatedValueV1ScoringsIndividual200ResponseResult;

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
 * UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:38.418404-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response {
  public static final String SERIALIZED_NAME_ERRORS = "Errors";
  @SerializedName(SERIALIZED_NAME_ERRORS)
  private List<Object> errors = new ArrayList<>();

  public static final String SERIALIZED_NAME_RESULT = "Result";
  @SerializedName(SERIALIZED_NAME_RESULT)
  private UserSafeScoringAccumulatedValueV1ScoringsIndividual200ResponseResult result;

  public static final String SERIALIZED_NAME_STATUS = "Status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private BigDecimal status;

  public static final String SERIALIZED_NAME_TITLE = "Title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response() {
  }

  public UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response errors(List<Object> errors) {
    this.errors = errors;
    return this;
  }

  public UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response addErrorsItem(Object errorsItem) {
    if (this.errors == null) {
      this.errors = new ArrayList<>();
    }
    this.errors.add(errorsItem);
    return this;
  }

  /**
   * Get errors
   * @return errors
   */
  @javax.annotation.Nullable
  public List<Object> getErrors() {
    return errors;
  }

  public void setErrors(List<Object> errors) {
    this.errors = errors;
  }


  public UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response result(UserSafeScoringAccumulatedValueV1ScoringsIndividual200ResponseResult result) {
    this.result = result;
    return this;
  }

  /**
   * Get result
   * @return result
   */
  @javax.annotation.Nullable
  public UserSafeScoringAccumulatedValueV1ScoringsIndividual200ResponseResult getResult() {
    return result;
  }

  public void setResult(UserSafeScoringAccumulatedValueV1ScoringsIndividual200ResponseResult result) {
    this.result = result;
  }


  public UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response status(BigDecimal status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public BigDecimal getStatus() {
    return status;
  }

  public void setStatus(BigDecimal status) {
    this.status = status;
  }


  public UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response userSafeScoringAccumulatedValueV1ScoringsIndividual200Response = (UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response) o;
    return Objects.equals(this.errors, userSafeScoringAccumulatedValueV1ScoringsIndividual200Response.errors) &&
        Objects.equals(this.result, userSafeScoringAccumulatedValueV1ScoringsIndividual200Response.result) &&
        Objects.equals(this.status, userSafeScoringAccumulatedValueV1ScoringsIndividual200Response.status) &&
        Objects.equals(this.title, userSafeScoringAccumulatedValueV1ScoringsIndividual200Response.title);
  }

  @Override
  public int hashCode() {
    return Objects.hash(errors, result, status, title);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response {\n");
    sb.append("    errors: ").append(toIndentedString(errors)).append("\n");
    sb.append("    result: ").append(toIndentedString(result)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
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
    openapiFields.add("Errors");
    openapiFields.add("Result");
    openapiFields.add("Status");
    openapiFields.add("Title");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response is not found in the empty JSON string", UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("Errors") != null && !jsonObj.get("Errors").isJsonNull() && !jsonObj.get("Errors").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `Errors` to be an array in the JSON string but got `%s`", jsonObj.get("Errors").toString()));
      }
      // validate the optional field `Result`
      if (jsonObj.get("Result") != null && !jsonObj.get("Result").isJsonNull()) {
        UserSafeScoringAccumulatedValueV1ScoringsIndividual200ResponseResult.validateJsonElement(jsonObj.get("Result"));
      }
      if ((jsonObj.get("Title") != null && !jsonObj.get("Title").isJsonNull()) && !jsonObj.get("Title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response>() {
           @Override
           public void write(JsonWriter out, UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response
   * @throws IOException if the JSON string is invalid with respect to UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response
   */
  public static UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response.class);
  }

  /**
   * Convert an instance of UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

