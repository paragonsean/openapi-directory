/*
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
 * A DTO for an IActivityRunStatus
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:35.511967-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BuildSystemSharedDTOActivityRunStatus {
  public static final String SERIALIZED_NAME_CURRENT_STEP = "CurrentStep";
  @SerializedName(SERIALIZED_NAME_CURRENT_STEP)
  private Integer currentStep;

  /**
   * The status of the ActivityRun
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    READY("Ready"),
    
    IN_PROGRESS("InProgress"),
    
    SUCCEEDED("Succeeded"),
    
    CANCELLED("Cancelled"),
    
    FAILED("Failed");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "Status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_STEP_PROGRESS = "StepProgress";
  @SerializedName(SERIALIZED_NAME_STEP_PROGRESS)
  private Integer stepProgress;

  public static final String SERIALIZED_NAME_STEP_STATUS = "StepStatus";
  @SerializedName(SERIALIZED_NAME_STEP_STATUS)
  private String stepStatus;

  public BuildSystemSharedDTOActivityRunStatus() {
  }

  public BuildSystemSharedDTOActivityRunStatus currentStep(Integer currentStep) {
    this.currentStep = currentStep;
    return this;
  }

  /**
   * The activity step currently executing, indicated by numeric order
   * @return currentStep
   */
  @javax.annotation.Nullable
  public Integer getCurrentStep() {
    return currentStep;
  }

  public void setCurrentStep(Integer currentStep) {
    this.currentStep = currentStep;
  }


  public BuildSystemSharedDTOActivityRunStatus status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * The status of the ActivityRun
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public BuildSystemSharedDTOActivityRunStatus stepProgress(Integer stepProgress) {
    this.stepProgress = stepProgress;
    return this;
  }

  /**
   * The percent progress from the currently executing step.  This value shall be null if progress is not available
   * @return stepProgress
   */
  @javax.annotation.Nullable
  public Integer getStepProgress() {
    return stepProgress;
  }

  public void setStepProgress(Integer stepProgress) {
    this.stepProgress = stepProgress;
  }


  public BuildSystemSharedDTOActivityRunStatus stepStatus(String stepStatus) {
    this.stepStatus = stepStatus;
    return this;
  }

  /**
   * The status text from the currently executing step
   * @return stepStatus
   */
  @javax.annotation.Nullable
  public String getStepStatus() {
    return stepStatus;
  }

  public void setStepStatus(String stepStatus) {
    this.stepStatus = stepStatus;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BuildSystemSharedDTOActivityRunStatus buildSystemSharedDTOActivityRunStatus = (BuildSystemSharedDTOActivityRunStatus) o;
    return Objects.equals(this.currentStep, buildSystemSharedDTOActivityRunStatus.currentStep) &&
        Objects.equals(this.status, buildSystemSharedDTOActivityRunStatus.status) &&
        Objects.equals(this.stepProgress, buildSystemSharedDTOActivityRunStatus.stepProgress) &&
        Objects.equals(this.stepStatus, buildSystemSharedDTOActivityRunStatus.stepStatus);
  }

  @Override
  public int hashCode() {
    return Objects.hash(currentStep, status, stepProgress, stepStatus);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BuildSystemSharedDTOActivityRunStatus {\n");
    sb.append("    currentStep: ").append(toIndentedString(currentStep)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    stepProgress: ").append(toIndentedString(stepProgress)).append("\n");
    sb.append("    stepStatus: ").append(toIndentedString(stepStatus)).append("\n");
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
    openapiFields.add("CurrentStep");
    openapiFields.add("Status");
    openapiFields.add("StepProgress");
    openapiFields.add("StepStatus");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BuildSystemSharedDTOActivityRunStatus
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BuildSystemSharedDTOActivityRunStatus.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BuildSystemSharedDTOActivityRunStatus is not found in the empty JSON string", BuildSystemSharedDTOActivityRunStatus.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BuildSystemSharedDTOActivityRunStatus.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BuildSystemSharedDTOActivityRunStatus` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Status") != null && !jsonObj.get("Status").isJsonNull()) && !jsonObj.get("Status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Status").toString()));
      }
      // validate the optional field `Status`
      if (jsonObj.get("Status") != null && !jsonObj.get("Status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("Status"));
      }
      if ((jsonObj.get("StepStatus") != null && !jsonObj.get("StepStatus").isJsonNull()) && !jsonObj.get("StepStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `StepStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("StepStatus").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BuildSystemSharedDTOActivityRunStatus.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BuildSystemSharedDTOActivityRunStatus' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BuildSystemSharedDTOActivityRunStatus> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BuildSystemSharedDTOActivityRunStatus.class));

       return (TypeAdapter<T>) new TypeAdapter<BuildSystemSharedDTOActivityRunStatus>() {
           @Override
           public void write(JsonWriter out, BuildSystemSharedDTOActivityRunStatus value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BuildSystemSharedDTOActivityRunStatus read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BuildSystemSharedDTOActivityRunStatus given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BuildSystemSharedDTOActivityRunStatus
   * @throws IOException if the JSON string is invalid with respect to BuildSystemSharedDTOActivityRunStatus
   */
  public static BuildSystemSharedDTOActivityRunStatus fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BuildSystemSharedDTOActivityRunStatus.class);
  }

  /**
   * Convert an instance of BuildSystemSharedDTOActivityRunStatus to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

