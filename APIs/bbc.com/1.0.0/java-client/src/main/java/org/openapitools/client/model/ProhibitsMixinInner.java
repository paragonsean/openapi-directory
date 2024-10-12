/*
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
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
import org.openapitools.client.model.ProhibitsFilterInner;

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
 * ProhibitsMixinInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProhibitsMixinInner {
  public static final String SERIALIZED_NAME_FILTER = "filter";
  @SerializedName(SERIALIZED_NAME_FILTER)
  private List<ProhibitsFilterInner> filter = new ArrayList<>();

  public static final String SERIALIZED_NAME_MIXIN = "mixin";
  @SerializedName(SERIALIZED_NAME_MIXIN)
  private List<ProhibitsFilterInner> mixin = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public ProhibitsMixinInner() {
  }

  public ProhibitsMixinInner filter(List<ProhibitsFilterInner> filter) {
    this.filter = filter;
    return this;
  }

  public ProhibitsMixinInner addFilterItem(ProhibitsFilterInner filterItem) {
    if (this.filter == null) {
      this.filter = new ArrayList<>();
    }
    this.filter.add(filterItem);
    return this;
  }

  /**
   * Get filter
   * @return filter
   */
  @javax.annotation.Nullable
  public List<ProhibitsFilterInner> getFilter() {
    return filter;
  }

  public void setFilter(List<ProhibitsFilterInner> filter) {
    this.filter = filter;
  }


  public ProhibitsMixinInner mixin(List<ProhibitsFilterInner> mixin) {
    this.mixin = mixin;
    return this;
  }

  public ProhibitsMixinInner addMixinItem(ProhibitsFilterInner mixinItem) {
    if (this.mixin == null) {
      this.mixin = new ArrayList<>();
    }
    this.mixin.add(mixinItem);
    return this;
  }

  /**
   * Get mixin
   * @return mixin
   */
  @javax.annotation.Nullable
  public List<ProhibitsFilterInner> getMixin() {
    return mixin;
  }

  public void setMixin(List<ProhibitsFilterInner> mixin) {
    this.mixin = mixin;
  }


  public ProhibitsMixinInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProhibitsMixinInner prohibitsMixinInner = (ProhibitsMixinInner) o;
    return Objects.equals(this.filter, prohibitsMixinInner.filter) &&
        Objects.equals(this.mixin, prohibitsMixinInner.mixin) &&
        Objects.equals(this.name, prohibitsMixinInner.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(filter, mixin, name);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProhibitsMixinInner {\n");
    sb.append("    filter: ").append(toIndentedString(filter)).append("\n");
    sb.append("    mixin: ").append(toIndentedString(mixin)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
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
    openapiFields.add("filter");
    openapiFields.add("mixin");
    openapiFields.add("name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProhibitsMixinInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProhibitsMixinInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProhibitsMixinInner is not found in the empty JSON string", ProhibitsMixinInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProhibitsMixinInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProhibitsMixinInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ProhibitsMixinInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("filter") != null && !jsonObj.get("filter").isJsonNull()) {
        JsonArray jsonArrayfilter = jsonObj.getAsJsonArray("filter");
        if (jsonArrayfilter != null) {
          // ensure the json data is an array
          if (!jsonObj.get("filter").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `filter` to be an array in the JSON string but got `%s`", jsonObj.get("filter").toString()));
          }

          // validate the optional field `filter` (array)
          for (int i = 0; i < jsonArrayfilter.size(); i++) {
            ProhibitsFilterInner.validateJsonElement(jsonArrayfilter.get(i));
          };
        }
      }
      if (jsonObj.get("mixin") != null && !jsonObj.get("mixin").isJsonNull()) {
        JsonArray jsonArraymixin = jsonObj.getAsJsonArray("mixin");
        if (jsonArraymixin != null) {
          // ensure the json data is an array
          if (!jsonObj.get("mixin").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `mixin` to be an array in the JSON string but got `%s`", jsonObj.get("mixin").toString()));
          }

          // validate the optional field `mixin` (array)
          for (int i = 0; i < jsonArraymixin.size(); i++) {
            ProhibitsFilterInner.validateJsonElement(jsonArraymixin.get(i));
          };
        }
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProhibitsMixinInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProhibitsMixinInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProhibitsMixinInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProhibitsMixinInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ProhibitsMixinInner>() {
           @Override
           public void write(JsonWriter out, ProhibitsMixinInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProhibitsMixinInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProhibitsMixinInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProhibitsMixinInner
   * @throws IOException if the JSON string is invalid with respect to ProhibitsMixinInner
   */
  public static ProhibitsMixinInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProhibitsMixinInner.class);
  }

  /**
   * Convert an instance of ProhibitsMixinInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

