/*
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
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
import org.openapitools.client.model.CertificateOrKeyGetSchema;

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
 * Certs
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:45.290770-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Certs {
  public static final String SERIALIZED_NAME_KEYS = "keys";
  @SerializedName(SERIALIZED_NAME_KEYS)
  private List<CertificateOrKeyGetSchema> keys = new ArrayList<>();

  public Certs() {
  }

  public Certs keys(List<CertificateOrKeyGetSchema> keys) {
    this.keys = keys;
    return this;
  }

  public Certs addKeysItem(CertificateOrKeyGetSchema keysItem) {
    if (this.keys == null) {
      this.keys = new ArrayList<>();
    }
    this.keys.add(keysItem);
    return this;
  }

  /**
   * Get keys
   * @return keys
   */
  @javax.annotation.Nullable
  public List<CertificateOrKeyGetSchema> getKeys() {
    return keys;
  }

  public void setKeys(List<CertificateOrKeyGetSchema> keys) {
    this.keys = keys;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Certs certs = (Certs) o;
    return Objects.equals(this.keys, certs.keys);
  }

  @Override
  public int hashCode() {
    return Objects.hash(keys);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Certs {\n");
    sb.append("    keys: ").append(toIndentedString(keys)).append("\n");
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
    openapiFields.add("keys");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Certs
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Certs.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Certs is not found in the empty JSON string", Certs.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Certs.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Certs` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("keys") != null && !jsonObj.get("keys").isJsonNull()) {
        JsonArray jsonArraykeys = jsonObj.getAsJsonArray("keys");
        if (jsonArraykeys != null) {
          // ensure the json data is an array
          if (!jsonObj.get("keys").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `keys` to be an array in the JSON string but got `%s`", jsonObj.get("keys").toString()));
          }

          // validate the optional field `keys` (array)
          for (int i = 0; i < jsonArraykeys.size(); i++) {
            CertificateOrKeyGetSchema.validateJsonElement(jsonArraykeys.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Certs.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Certs' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Certs> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Certs.class));

       return (TypeAdapter<T>) new TypeAdapter<Certs>() {
           @Override
           public void write(JsonWriter out, Certs value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Certs read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Certs given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Certs
   * @throws IOException if the JSON string is invalid with respect to Certs
   */
  public static Certs fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Certs.class);
  }

  /**
   * Convert an instance of Certs to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

