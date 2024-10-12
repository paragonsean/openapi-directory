/*
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
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
import org.openapitools.client.model.LocalizedString;

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
 * FrequentFlyerInfo
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:07.622305-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FrequentFlyerInfo {
  public static final String SERIALIZED_NAME_FREQUENT_FLYER_NUMBER = "frequentFlyerNumber";
  @SerializedName(SERIALIZED_NAME_FREQUENT_FLYER_NUMBER)
  private String frequentFlyerNumber;

  public static final String SERIALIZED_NAME_FREQUENT_FLYER_PROGRAM_NAME = "frequentFlyerProgramName";
  @SerializedName(SERIALIZED_NAME_FREQUENT_FLYER_PROGRAM_NAME)
  private LocalizedString frequentFlyerProgramName;

  public static final String SERIALIZED_NAME_KIND = "kind";
  @SerializedName(SERIALIZED_NAME_KIND)
  private String kind;

  public FrequentFlyerInfo() {
  }

  public FrequentFlyerInfo frequentFlyerNumber(String frequentFlyerNumber) {
    this.frequentFlyerNumber = frequentFlyerNumber;
    return this;
  }

  /**
   * Frequent flyer number. Required for each nested object of kind &#x60;walletobjects#frequentFlyerInfo&#x60;.
   * @return frequentFlyerNumber
   */
  @javax.annotation.Nullable
  public String getFrequentFlyerNumber() {
    return frequentFlyerNumber;
  }

  public void setFrequentFlyerNumber(String frequentFlyerNumber) {
    this.frequentFlyerNumber = frequentFlyerNumber;
  }


  public FrequentFlyerInfo frequentFlyerProgramName(LocalizedString frequentFlyerProgramName) {
    this.frequentFlyerProgramName = frequentFlyerProgramName;
    return this;
  }

  /**
   * Get frequentFlyerProgramName
   * @return frequentFlyerProgramName
   */
  @javax.annotation.Nullable
  public LocalizedString getFrequentFlyerProgramName() {
    return frequentFlyerProgramName;
  }

  public void setFrequentFlyerProgramName(LocalizedString frequentFlyerProgramName) {
    this.frequentFlyerProgramName = frequentFlyerProgramName;
  }


  public FrequentFlyerInfo kind(String kind) {
    this.kind = kind;
    return this;
  }

  /**
   * Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#frequentFlyerInfo\&quot;&#x60;.
   * @return kind
   */
  @javax.annotation.Nullable
  public String getKind() {
    return kind;
  }

  public void setKind(String kind) {
    this.kind = kind;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FrequentFlyerInfo frequentFlyerInfo = (FrequentFlyerInfo) o;
    return Objects.equals(this.frequentFlyerNumber, frequentFlyerInfo.frequentFlyerNumber) &&
        Objects.equals(this.frequentFlyerProgramName, frequentFlyerInfo.frequentFlyerProgramName) &&
        Objects.equals(this.kind, frequentFlyerInfo.kind);
  }

  @Override
  public int hashCode() {
    return Objects.hash(frequentFlyerNumber, frequentFlyerProgramName, kind);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FrequentFlyerInfo {\n");
    sb.append("    frequentFlyerNumber: ").append(toIndentedString(frequentFlyerNumber)).append("\n");
    sb.append("    frequentFlyerProgramName: ").append(toIndentedString(frequentFlyerProgramName)).append("\n");
    sb.append("    kind: ").append(toIndentedString(kind)).append("\n");
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
    openapiFields.add("frequentFlyerNumber");
    openapiFields.add("frequentFlyerProgramName");
    openapiFields.add("kind");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FrequentFlyerInfo
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FrequentFlyerInfo.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FrequentFlyerInfo is not found in the empty JSON string", FrequentFlyerInfo.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FrequentFlyerInfo.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FrequentFlyerInfo` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("frequentFlyerNumber") != null && !jsonObj.get("frequentFlyerNumber").isJsonNull()) && !jsonObj.get("frequentFlyerNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `frequentFlyerNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("frequentFlyerNumber").toString()));
      }
      // validate the optional field `frequentFlyerProgramName`
      if (jsonObj.get("frequentFlyerProgramName") != null && !jsonObj.get("frequentFlyerProgramName").isJsonNull()) {
        LocalizedString.validateJsonElement(jsonObj.get("frequentFlyerProgramName"));
      }
      if ((jsonObj.get("kind") != null && !jsonObj.get("kind").isJsonNull()) && !jsonObj.get("kind").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `kind` to be a primitive type in the JSON string but got `%s`", jsonObj.get("kind").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FrequentFlyerInfo.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FrequentFlyerInfo' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FrequentFlyerInfo> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FrequentFlyerInfo.class));

       return (TypeAdapter<T>) new TypeAdapter<FrequentFlyerInfo>() {
           @Override
           public void write(JsonWriter out, FrequentFlyerInfo value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FrequentFlyerInfo read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FrequentFlyerInfo given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FrequentFlyerInfo
   * @throws IOException if the JSON string is invalid with respect to FrequentFlyerInfo
   */
  public static FrequentFlyerInfo fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FrequentFlyerInfo.class);
  }

  /**
   * Convert an instance of FrequentFlyerInfo to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

