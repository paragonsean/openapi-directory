/*
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
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
 * HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:41.924748-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner {
  public static final String SERIALIZED_NAME_CARE_CONTEXT_REFERENCE = "careContextReference";
  @SerializedName(SERIALIZED_NAME_CARE_CONTEXT_REFERENCE)
  private String careContextReference;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  /**
   * Gets or Sets hiStatus
   */
  @JsonAdapter(HiStatusEnum.Adapter.class)
  public enum HiStatusEnum {
    DELIVERED("DELIVERED"),
    
    OK("OK"),
    
    ERRORED("ERRORED");

    private String value;

    HiStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static HiStatusEnum fromValue(String value) {
      for (HiStatusEnum b : HiStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<HiStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final HiStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public HiStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return HiStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      HiStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_HI_STATUS = "hiStatus";
  @SerializedName(SERIALIZED_NAME_HI_STATUS)
  private HiStatusEnum hiStatus;

  public HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner() {
  }

  public HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner careContextReference(String careContextReference) {
    this.careContextReference = careContextReference;
    return this;
  }

  /**
   * Get careContextReference
   * @return careContextReference
   */
  @javax.annotation.Nonnull
  public String getCareContextReference() {
    return careContextReference;
  }

  public void setCareContextReference(String careContextReference) {
    this.careContextReference = careContextReference;
  }


  public HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner hiStatus(HiStatusEnum hiStatus) {
    this.hiStatus = hiStatus;
    return this;
  }

  /**
   * Get hiStatus
   * @return hiStatus
   */
  @javax.annotation.Nonnull
  public HiStatusEnum getHiStatus() {
    return hiStatus;
  }

  public void setHiStatus(HiStatusEnum hiStatus) {
    this.hiStatus = hiStatus;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner healthInformationNotificationNotificationStatusNotificationStatusResponsesInner = (HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner) o;
    return Objects.equals(this.careContextReference, healthInformationNotificationNotificationStatusNotificationStatusResponsesInner.careContextReference) &&
        Objects.equals(this.description, healthInformationNotificationNotificationStatusNotificationStatusResponsesInner.description) &&
        Objects.equals(this.hiStatus, healthInformationNotificationNotificationStatusNotificationStatusResponsesInner.hiStatus);
  }

  @Override
  public int hashCode() {
    return Objects.hash(careContextReference, description, hiStatus);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner {\n");
    sb.append("    careContextReference: ").append(toIndentedString(careContextReference)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    hiStatus: ").append(toIndentedString(hiStatus)).append("\n");
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
    openapiFields.add("careContextReference");
    openapiFields.add("description");
    openapiFields.add("hiStatus");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("careContextReference");
    openapiRequiredFields.add("hiStatus");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner is not found in the empty JSON string", HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("careContextReference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `careContextReference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("careContextReference").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (!jsonObj.get("hiStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `hiStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("hiStatus").toString()));
      }
      // validate the required field `hiStatus`
      HiStatusEnum.validateJsonElement(jsonObj.get("hiStatus"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner>() {
           @Override
           public void write(JsonWriter out, HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner
   * @throws IOException if the JSON string is invalid with respect to HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner
   */
  public static HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.class);
  }

  /**
   * Convert an instance of HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

