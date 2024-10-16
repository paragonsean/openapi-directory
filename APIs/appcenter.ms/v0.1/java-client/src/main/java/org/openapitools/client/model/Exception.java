/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ExceptionFramesInner;

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
 * a exception
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Exception {
  public static final String SERIALIZED_NAME_FRAMES = "frames";
  @SerializedName(SERIALIZED_NAME_FRAMES)
  private List<ExceptionFramesInner> frames = new ArrayList<>();

  public static final String SERIALIZED_NAME_INNER_EXCEPTIONS = "inner_exceptions";
  @SerializedName(SERIALIZED_NAME_INNER_EXCEPTIONS)
  private List<Exception> innerExceptions = new ArrayList<>();

  /**
   * SDK/Platform this thread is beeing generated from
   */
  @JsonAdapter(PlatformEnum.Adapter.class)
  public enum PlatformEnum {
    IOS("ios"),
    
    ANDROID("android"),
    
    XAMARIN("xamarin"),
    
    REACT_NATIVE("react-native"),
    
    NDK("ndk"),
    
    UNITY("unity"),
    
    OTHER("other");

    private String value;

    PlatformEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PlatformEnum fromValue(String value) {
      for (PlatformEnum b : PlatformEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PlatformEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PlatformEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PlatformEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PlatformEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PlatformEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PLATFORM = "platform";
  @SerializedName(SERIALIZED_NAME_PLATFORM)
  private PlatformEnum platform;

  public static final String SERIALIZED_NAME_REASON = "reason";
  @SerializedName(SERIALIZED_NAME_REASON)
  private String reason;

  public static final String SERIALIZED_NAME_RELEVANT = "relevant";
  @SerializedName(SERIALIZED_NAME_RELEVANT)
  private Boolean relevant;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public Exception() {
  }

  public Exception frames(List<ExceptionFramesInner> frames) {
    this.frames = frames;
    return this;
  }

  public Exception addFramesItem(ExceptionFramesInner framesItem) {
    if (this.frames == null) {
      this.frames = new ArrayList<>();
    }
    this.frames.add(framesItem);
    return this;
  }

  /**
   * frames of the excetpion
   * @return frames
   */
  @javax.annotation.Nonnull
  public List<ExceptionFramesInner> getFrames() {
    return frames;
  }

  public void setFrames(List<ExceptionFramesInner> frames) {
    this.frames = frames;
  }


  public Exception innerExceptions(List<Exception> innerExceptions) {
    this.innerExceptions = innerExceptions;
    return this;
  }

  public Exception addInnerExceptionsItem(Exception innerExceptionsItem) {
    if (this.innerExceptions == null) {
      this.innerExceptions = new ArrayList<>();
    }
    this.innerExceptions.add(innerExceptionsItem);
    return this;
  }

  /**
   * Get innerExceptions
   * @return innerExceptions
   */
  @javax.annotation.Nullable
  public List<Exception> getInnerExceptions() {
    return innerExceptions;
  }

  public void setInnerExceptions(List<Exception> innerExceptions) {
    this.innerExceptions = innerExceptions;
  }


  public Exception platform(PlatformEnum platform) {
    this.platform = platform;
    return this;
  }

  /**
   * SDK/Platform this thread is beeing generated from
   * @return platform
   */
  @javax.annotation.Nullable
  public PlatformEnum getPlatform() {
    return platform;
  }

  public void setPlatform(PlatformEnum platform) {
    this.platform = platform;
  }


  public Exception reason(String reason) {
    this.reason = reason;
    return this;
  }

  /**
   * Reason of the exception
   * @return reason
   */
  @javax.annotation.Nullable
  public String getReason() {
    return reason;
  }

  public void setReason(String reason) {
    this.reason = reason;
  }


  public Exception relevant(Boolean relevant) {
    this.relevant = relevant;
    return this;
  }

  /**
   * relevant exception (crashed)
   * @return relevant
   */
  @javax.annotation.Nullable
  public Boolean getRelevant() {
    return relevant;
  }

  public void setRelevant(Boolean relevant) {
    this.relevant = relevant;
  }


  public Exception type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Type of the exception (NSSomethingException, NullPointerException)
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Exception exception = (Exception) o;
    return Objects.equals(this.frames, exception.frames) &&
        Objects.equals(this.innerExceptions, exception.innerExceptions) &&
        Objects.equals(this.platform, exception.platform) &&
        Objects.equals(this.reason, exception.reason) &&
        Objects.equals(this.relevant, exception.relevant) &&
        Objects.equals(this.type, exception.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(frames, innerExceptions, platform, reason, relevant, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Exception {\n");
    sb.append("    frames: ").append(toIndentedString(frames)).append("\n");
    sb.append("    innerExceptions: ").append(toIndentedString(innerExceptions)).append("\n");
    sb.append("    platform: ").append(toIndentedString(platform)).append("\n");
    sb.append("    reason: ").append(toIndentedString(reason)).append("\n");
    sb.append("    relevant: ").append(toIndentedString(relevant)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("frames");
    openapiFields.add("inner_exceptions");
    openapiFields.add("platform");
    openapiFields.add("reason");
    openapiFields.add("relevant");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("frames");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Exception
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Exception.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Exception is not found in the empty JSON string", Exception.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Exception.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Exception` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Exception.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("frames").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `frames` to be an array in the JSON string but got `%s`", jsonObj.get("frames").toString()));
      }

      JsonArray jsonArrayframes = jsonObj.getAsJsonArray("frames");
      // validate the required field `frames` (array)
      for (int i = 0; i < jsonArrayframes.size(); i++) {
        ExceptionFramesInner.validateJsonElement(jsonArrayframes.get(i));
      };
      if (jsonObj.get("inner_exceptions") != null && !jsonObj.get("inner_exceptions").isJsonNull()) {
        JsonArray jsonArrayinnerExceptions = jsonObj.getAsJsonArray("inner_exceptions");
        if (jsonArrayinnerExceptions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("inner_exceptions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `inner_exceptions` to be an array in the JSON string but got `%s`", jsonObj.get("inner_exceptions").toString()));
          }

          // validate the optional field `inner_exceptions` (array)
          for (int i = 0; i < jsonArrayinnerExceptions.size(); i++) {
            Exception.validateJsonElement(jsonArrayinnerExceptions.get(i));
          };
        }
      }
      if ((jsonObj.get("platform") != null && !jsonObj.get("platform").isJsonNull()) && !jsonObj.get("platform").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `platform` to be a primitive type in the JSON string but got `%s`", jsonObj.get("platform").toString()));
      }
      // validate the optional field `platform`
      if (jsonObj.get("platform") != null && !jsonObj.get("platform").isJsonNull()) {
        PlatformEnum.validateJsonElement(jsonObj.get("platform"));
      }
      if ((jsonObj.get("reason") != null && !jsonObj.get("reason").isJsonNull()) && !jsonObj.get("reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reason").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Exception.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Exception' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Exception> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Exception.class));

       return (TypeAdapter<T>) new TypeAdapter<Exception>() {
           @Override
           public void write(JsonWriter out, Exception value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Exception read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Exception given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Exception
   * @throws IOException if the JSON string is invalid with respect to Exception
   */
  public static Exception fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Exception.class);
  }

  /**
   * Convert an instance of Exception to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

