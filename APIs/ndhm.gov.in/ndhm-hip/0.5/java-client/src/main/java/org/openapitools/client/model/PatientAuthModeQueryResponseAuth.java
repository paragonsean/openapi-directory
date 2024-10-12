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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AuthenticationMode;
import org.openapitools.client.model.PatientAuthPurpose;

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
 * PatientAuthModeQueryResponseAuth
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:41.924748-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatientAuthModeQueryResponseAuth {
  public static final String SERIALIZED_NAME_MODES = "modes";
  @SerializedName(SERIALIZED_NAME_MODES)
  private List<AuthenticationMode> modes = new ArrayList<>();

  public static final String SERIALIZED_NAME_PURPOSE = "purpose";
  @SerializedName(SERIALIZED_NAME_PURPOSE)
  private PatientAuthPurpose purpose;

  public PatientAuthModeQueryResponseAuth() {
  }

  public PatientAuthModeQueryResponseAuth modes(List<AuthenticationMode> modes) {
    this.modes = modes;
    return this;
  }

  public PatientAuthModeQueryResponseAuth addModesItem(AuthenticationMode modesItem) {
    if (this.modes == null) {
      this.modes = new ArrayList<>();
    }
    this.modes.add(modesItem);
    return this;
  }

  /**
   * Get modes
   * @return modes
   */
  @javax.annotation.Nonnull
  public List<AuthenticationMode> getModes() {
    return modes;
  }

  public void setModes(List<AuthenticationMode> modes) {
    this.modes = modes;
  }


  public PatientAuthModeQueryResponseAuth purpose(PatientAuthPurpose purpose) {
    this.purpose = purpose;
    return this;
  }

  /**
   * Get purpose
   * @return purpose
   */
  @javax.annotation.Nonnull
  public PatientAuthPurpose getPurpose() {
    return purpose;
  }

  public void setPurpose(PatientAuthPurpose purpose) {
    this.purpose = purpose;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PatientAuthModeQueryResponseAuth patientAuthModeQueryResponseAuth = (PatientAuthModeQueryResponseAuth) o;
    return Objects.equals(this.modes, patientAuthModeQueryResponseAuth.modes) &&
        Objects.equals(this.purpose, patientAuthModeQueryResponseAuth.purpose);
  }

  @Override
  public int hashCode() {
    return Objects.hash(modes, purpose);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatientAuthModeQueryResponseAuth {\n");
    sb.append("    modes: ").append(toIndentedString(modes)).append("\n");
    sb.append("    purpose: ").append(toIndentedString(purpose)).append("\n");
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
    openapiFields.add("modes");
    openapiFields.add("purpose");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("modes");
    openapiRequiredFields.add("purpose");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PatientAuthModeQueryResponseAuth
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatientAuthModeQueryResponseAuth.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatientAuthModeQueryResponseAuth is not found in the empty JSON string", PatientAuthModeQueryResponseAuth.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatientAuthModeQueryResponseAuth.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatientAuthModeQueryResponseAuth` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatientAuthModeQueryResponseAuth.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the required json array is present
      if (jsonObj.get("modes") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("modes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `modes` to be an array in the JSON string but got `%s`", jsonObj.get("modes").toString()));
      }
      // validate the required field `purpose`
      PatientAuthPurpose.validateJsonElement(jsonObj.get("purpose"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PatientAuthModeQueryResponseAuth.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatientAuthModeQueryResponseAuth' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatientAuthModeQueryResponseAuth> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatientAuthModeQueryResponseAuth.class));

       return (TypeAdapter<T>) new TypeAdapter<PatientAuthModeQueryResponseAuth>() {
           @Override
           public void write(JsonWriter out, PatientAuthModeQueryResponseAuth value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatientAuthModeQueryResponseAuth read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatientAuthModeQueryResponseAuth given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatientAuthModeQueryResponseAuth
   * @throws IOException if the JSON string is invalid with respect to PatientAuthModeQueryResponseAuth
   */
  public static PatientAuthModeQueryResponseAuth fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatientAuthModeQueryResponseAuth.class);
  }

  /**
   * Convert an instance of PatientAuthModeQueryResponseAuth to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

