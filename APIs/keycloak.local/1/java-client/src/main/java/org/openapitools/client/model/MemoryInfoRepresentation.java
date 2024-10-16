/*
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
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
 * MemoryInfoRepresentation
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.227825-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class MemoryInfoRepresentation {
  public static final String SERIALIZED_NAME_FREE = "free";
  @SerializedName(SERIALIZED_NAME_FREE)
  private Long free;

  public static final String SERIALIZED_NAME_FREE_FORMATED = "freeFormated";
  @SerializedName(SERIALIZED_NAME_FREE_FORMATED)
  private String freeFormated;

  public static final String SERIALIZED_NAME_FREE_PERCENTAGE = "freePercentage";
  @SerializedName(SERIALIZED_NAME_FREE_PERCENTAGE)
  private Long freePercentage;

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private Long total;

  public static final String SERIALIZED_NAME_TOTAL_FORMATED = "totalFormated";
  @SerializedName(SERIALIZED_NAME_TOTAL_FORMATED)
  private String totalFormated;

  public static final String SERIALIZED_NAME_USED = "used";
  @SerializedName(SERIALIZED_NAME_USED)
  private Long used;

  public static final String SERIALIZED_NAME_USED_FORMATED = "usedFormated";
  @SerializedName(SERIALIZED_NAME_USED_FORMATED)
  private String usedFormated;

  public MemoryInfoRepresentation() {
  }

  public MemoryInfoRepresentation free(Long free) {
    this.free = free;
    return this;
  }

  /**
   * Get free
   * @return free
   */
  @javax.annotation.Nullable
  public Long getFree() {
    return free;
  }

  public void setFree(Long free) {
    this.free = free;
  }


  public MemoryInfoRepresentation freeFormated(String freeFormated) {
    this.freeFormated = freeFormated;
    return this;
  }

  /**
   * Get freeFormated
   * @return freeFormated
   */
  @javax.annotation.Nullable
  public String getFreeFormated() {
    return freeFormated;
  }

  public void setFreeFormated(String freeFormated) {
    this.freeFormated = freeFormated;
  }


  public MemoryInfoRepresentation freePercentage(Long freePercentage) {
    this.freePercentage = freePercentage;
    return this;
  }

  /**
   * Get freePercentage
   * @return freePercentage
   */
  @javax.annotation.Nullable
  public Long getFreePercentage() {
    return freePercentage;
  }

  public void setFreePercentage(Long freePercentage) {
    this.freePercentage = freePercentage;
  }


  public MemoryInfoRepresentation total(Long total) {
    this.total = total;
    return this;
  }

  /**
   * Get total
   * @return total
   */
  @javax.annotation.Nullable
  public Long getTotal() {
    return total;
  }

  public void setTotal(Long total) {
    this.total = total;
  }


  public MemoryInfoRepresentation totalFormated(String totalFormated) {
    this.totalFormated = totalFormated;
    return this;
  }

  /**
   * Get totalFormated
   * @return totalFormated
   */
  @javax.annotation.Nullable
  public String getTotalFormated() {
    return totalFormated;
  }

  public void setTotalFormated(String totalFormated) {
    this.totalFormated = totalFormated;
  }


  public MemoryInfoRepresentation used(Long used) {
    this.used = used;
    return this;
  }

  /**
   * Get used
   * @return used
   */
  @javax.annotation.Nullable
  public Long getUsed() {
    return used;
  }

  public void setUsed(Long used) {
    this.used = used;
  }


  public MemoryInfoRepresentation usedFormated(String usedFormated) {
    this.usedFormated = usedFormated;
    return this;
  }

  /**
   * Get usedFormated
   * @return usedFormated
   */
  @javax.annotation.Nullable
  public String getUsedFormated() {
    return usedFormated;
  }

  public void setUsedFormated(String usedFormated) {
    this.usedFormated = usedFormated;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MemoryInfoRepresentation memoryInfoRepresentation = (MemoryInfoRepresentation) o;
    return Objects.equals(this.free, memoryInfoRepresentation.free) &&
        Objects.equals(this.freeFormated, memoryInfoRepresentation.freeFormated) &&
        Objects.equals(this.freePercentage, memoryInfoRepresentation.freePercentage) &&
        Objects.equals(this.total, memoryInfoRepresentation.total) &&
        Objects.equals(this.totalFormated, memoryInfoRepresentation.totalFormated) &&
        Objects.equals(this.used, memoryInfoRepresentation.used) &&
        Objects.equals(this.usedFormated, memoryInfoRepresentation.usedFormated);
  }

  @Override
  public int hashCode() {
    return Objects.hash(free, freeFormated, freePercentage, total, totalFormated, used, usedFormated);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MemoryInfoRepresentation {\n");
    sb.append("    free: ").append(toIndentedString(free)).append("\n");
    sb.append("    freeFormated: ").append(toIndentedString(freeFormated)).append("\n");
    sb.append("    freePercentage: ").append(toIndentedString(freePercentage)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
    sb.append("    totalFormated: ").append(toIndentedString(totalFormated)).append("\n");
    sb.append("    used: ").append(toIndentedString(used)).append("\n");
    sb.append("    usedFormated: ").append(toIndentedString(usedFormated)).append("\n");
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
    openapiFields.add("free");
    openapiFields.add("freeFormated");
    openapiFields.add("freePercentage");
    openapiFields.add("total");
    openapiFields.add("totalFormated");
    openapiFields.add("used");
    openapiFields.add("usedFormated");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to MemoryInfoRepresentation
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!MemoryInfoRepresentation.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in MemoryInfoRepresentation is not found in the empty JSON string", MemoryInfoRepresentation.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!MemoryInfoRepresentation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `MemoryInfoRepresentation` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("freeFormated") != null && !jsonObj.get("freeFormated").isJsonNull()) && !jsonObj.get("freeFormated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `freeFormated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("freeFormated").toString()));
      }
      if ((jsonObj.get("totalFormated") != null && !jsonObj.get("totalFormated").isJsonNull()) && !jsonObj.get("totalFormated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `totalFormated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("totalFormated").toString()));
      }
      if ((jsonObj.get("usedFormated") != null && !jsonObj.get("usedFormated").isJsonNull()) && !jsonObj.get("usedFormated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `usedFormated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("usedFormated").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!MemoryInfoRepresentation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'MemoryInfoRepresentation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<MemoryInfoRepresentation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(MemoryInfoRepresentation.class));

       return (TypeAdapter<T>) new TypeAdapter<MemoryInfoRepresentation>() {
           @Override
           public void write(JsonWriter out, MemoryInfoRepresentation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public MemoryInfoRepresentation read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of MemoryInfoRepresentation given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of MemoryInfoRepresentation
   * @throws IOException if the JSON string is invalid with respect to MemoryInfoRepresentation
   */
  public static MemoryInfoRepresentation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, MemoryInfoRepresentation.class);
  }

  /**
   * Convert an instance of MemoryInfoRepresentation to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

