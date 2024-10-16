/*
 * EVEMarketer Marketstat API
 * EVEMarketer Marketstat API is almost compatible with EVE-Central's Marketstat API.
 *
 * The version of the OpenAPI document: 1.0.1
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
import org.openapitools.client.model.MarketStatXMLInner;

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
 * ExecAPI
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:50.680413-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ExecAPI {
  public static final String SERIALIZED_NAME_MARKETSTAT = "marketstat";
  @SerializedName(SERIALIZED_NAME_MARKETSTAT)
  private List<MarketStatXMLInner> marketstat = new ArrayList<>();

  public static final String SERIALIZED_NAME_METHOD = "method";
  @SerializedName(SERIALIZED_NAME_METHOD)
  private String method;

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private String version;

  public ExecAPI() {
  }

  public ExecAPI marketstat(List<MarketStatXMLInner> marketstat) {
    this.marketstat = marketstat;
    return this;
  }

  public ExecAPI addMarketstatItem(MarketStatXMLInner marketstatItem) {
    if (this.marketstat == null) {
      this.marketstat = new ArrayList<>();
    }
    this.marketstat.add(marketstatItem);
    return this;
  }

  /**
   * Get marketstat
   * @return marketstat
   */
  @javax.annotation.Nullable
  public List<MarketStatXMLInner> getMarketstat() {
    return marketstat;
  }

  public void setMarketstat(List<MarketStatXMLInner> marketstat) {
    this.marketstat = marketstat;
  }


  public ExecAPI method(String method) {
    this.method = method;
    return this;
  }

  /**
   * Get method
   * @return method
   */
  @javax.annotation.Nullable
  public String getMethod() {
    return method;
  }

  public void setMethod(String method) {
    this.method = method;
  }


  public ExecAPI version(String version) {
    this.version = version;
    return this;
  }

  /**
   * Get version
   * @return version
   */
  @javax.annotation.Nullable
  public String getVersion() {
    return version;
  }

  public void setVersion(String version) {
    this.version = version;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ExecAPI execAPI = (ExecAPI) o;
    return Objects.equals(this.marketstat, execAPI.marketstat) &&
        Objects.equals(this.method, execAPI.method) &&
        Objects.equals(this.version, execAPI.version);
  }

  @Override
  public int hashCode() {
    return Objects.hash(marketstat, method, version);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ExecAPI {\n");
    sb.append("    marketstat: ").append(toIndentedString(marketstat)).append("\n");
    sb.append("    method: ").append(toIndentedString(method)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
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
    openapiFields.add("marketstat");
    openapiFields.add("method");
    openapiFields.add("version");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ExecAPI
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ExecAPI.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ExecAPI is not found in the empty JSON string", ExecAPI.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ExecAPI.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ExecAPI` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("marketstat") != null && !jsonObj.get("marketstat").isJsonNull()) {
        JsonArray jsonArraymarketstat = jsonObj.getAsJsonArray("marketstat");
        if (jsonArraymarketstat != null) {
          // ensure the json data is an array
          if (!jsonObj.get("marketstat").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `marketstat` to be an array in the JSON string but got `%s`", jsonObj.get("marketstat").toString()));
          }

          // validate the optional field `marketstat` (array)
          for (int i = 0; i < jsonArraymarketstat.size(); i++) {
            MarketStatXMLInner.validateJsonElement(jsonArraymarketstat.get(i));
          };
        }
      }
      if ((jsonObj.get("method") != null && !jsonObj.get("method").isJsonNull()) && !jsonObj.get("method").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `method` to be a primitive type in the JSON string but got `%s`", jsonObj.get("method").toString()));
      }
      if ((jsonObj.get("version") != null && !jsonObj.get("version").isJsonNull()) && !jsonObj.get("version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("version").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ExecAPI.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ExecAPI' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ExecAPI> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ExecAPI.class));

       return (TypeAdapter<T>) new TypeAdapter<ExecAPI>() {
           @Override
           public void write(JsonWriter out, ExecAPI value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ExecAPI read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ExecAPI given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ExecAPI
   * @throws IOException if the JSON string is invalid with respect to ExecAPI
   */
  public static ExecAPI fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ExecAPI.class);
  }

  /**
   * Convert an instance of ExecAPI to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

