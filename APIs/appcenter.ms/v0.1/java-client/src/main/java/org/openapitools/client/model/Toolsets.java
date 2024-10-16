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
import org.openapitools.client.model.BuildsListToolsets200ResponseNodeInner;
import org.openapitools.client.model.BuildsListToolsets200ResponseXamarinInner;
import org.openapitools.client.model.BuildsListToolsets200ResponseXcodeInner;

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
 * Set of toolsets available for app
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Toolsets {
  public static final String SERIALIZED_NAME_NODE = "node";
  @SerializedName(SERIALIZED_NAME_NODE)
  private List<BuildsListToolsets200ResponseNodeInner> node = new ArrayList<>();

  public static final String SERIALIZED_NAME_XAMARIN = "xamarin";
  @SerializedName(SERIALIZED_NAME_XAMARIN)
  private List<BuildsListToolsets200ResponseXamarinInner> xamarin = new ArrayList<>();

  public static final String SERIALIZED_NAME_XCODE = "xcode";
  @SerializedName(SERIALIZED_NAME_XCODE)
  private List<BuildsListToolsets200ResponseXcodeInner> xcode = new ArrayList<>();

  public Toolsets() {
  }

  public Toolsets node(List<BuildsListToolsets200ResponseNodeInner> node) {
    this.node = node;
    return this;
  }

  public Toolsets addNodeItem(BuildsListToolsets200ResponseNodeInner nodeItem) {
    if (this.node == null) {
      this.node = new ArrayList<>();
    }
    this.node.add(nodeItem);
    return this;
  }

  /**
   * A list of Node versions
   * @return node
   */
  @javax.annotation.Nullable
  public List<BuildsListToolsets200ResponseNodeInner> getNode() {
    return node;
  }

  public void setNode(List<BuildsListToolsets200ResponseNodeInner> node) {
    this.node = node;
  }


  public Toolsets xamarin(List<BuildsListToolsets200ResponseXamarinInner> xamarin) {
    this.xamarin = xamarin;
    return this;
  }

  public Toolsets addXamarinItem(BuildsListToolsets200ResponseXamarinInner xamarinItem) {
    if (this.xamarin == null) {
      this.xamarin = new ArrayList<>();
    }
    this.xamarin.add(xamarinItem);
    return this;
  }

  /**
   * A list of Xamarin SDK bundles
   * @return xamarin
   */
  @javax.annotation.Nullable
  public List<BuildsListToolsets200ResponseXamarinInner> getXamarin() {
    return xamarin;
  }

  public void setXamarin(List<BuildsListToolsets200ResponseXamarinInner> xamarin) {
    this.xamarin = xamarin;
  }


  public Toolsets xcode(List<BuildsListToolsets200ResponseXcodeInner> xcode) {
    this.xcode = xcode;
    return this;
  }

  public Toolsets addXcodeItem(BuildsListToolsets200ResponseXcodeInner xcodeItem) {
    if (this.xcode == null) {
      this.xcode = new ArrayList<>();
    }
    this.xcode.add(xcodeItem);
    return this;
  }

  /**
   * A list of Xcode versions
   * @return xcode
   */
  @javax.annotation.Nullable
  public List<BuildsListToolsets200ResponseXcodeInner> getXcode() {
    return xcode;
  }

  public void setXcode(List<BuildsListToolsets200ResponseXcodeInner> xcode) {
    this.xcode = xcode;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Toolsets toolsets = (Toolsets) o;
    return Objects.equals(this.node, toolsets.node) &&
        Objects.equals(this.xamarin, toolsets.xamarin) &&
        Objects.equals(this.xcode, toolsets.xcode);
  }

  @Override
  public int hashCode() {
    return Objects.hash(node, xamarin, xcode);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Toolsets {\n");
    sb.append("    node: ").append(toIndentedString(node)).append("\n");
    sb.append("    xamarin: ").append(toIndentedString(xamarin)).append("\n");
    sb.append("    xcode: ").append(toIndentedString(xcode)).append("\n");
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
    openapiFields.add("node");
    openapiFields.add("xamarin");
    openapiFields.add("xcode");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Toolsets
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Toolsets.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Toolsets is not found in the empty JSON string", Toolsets.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Toolsets.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Toolsets` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("node") != null && !jsonObj.get("node").isJsonNull()) {
        JsonArray jsonArraynode = jsonObj.getAsJsonArray("node");
        if (jsonArraynode != null) {
          // ensure the json data is an array
          if (!jsonObj.get("node").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `node` to be an array in the JSON string but got `%s`", jsonObj.get("node").toString()));
          }

          // validate the optional field `node` (array)
          for (int i = 0; i < jsonArraynode.size(); i++) {
            BuildsListToolsets200ResponseNodeInner.validateJsonElement(jsonArraynode.get(i));
          };
        }
      }
      if (jsonObj.get("xamarin") != null && !jsonObj.get("xamarin").isJsonNull()) {
        JsonArray jsonArrayxamarin = jsonObj.getAsJsonArray("xamarin");
        if (jsonArrayxamarin != null) {
          // ensure the json data is an array
          if (!jsonObj.get("xamarin").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `xamarin` to be an array in the JSON string but got `%s`", jsonObj.get("xamarin").toString()));
          }

          // validate the optional field `xamarin` (array)
          for (int i = 0; i < jsonArrayxamarin.size(); i++) {
            BuildsListToolsets200ResponseXamarinInner.validateJsonElement(jsonArrayxamarin.get(i));
          };
        }
      }
      if (jsonObj.get("xcode") != null && !jsonObj.get("xcode").isJsonNull()) {
        JsonArray jsonArrayxcode = jsonObj.getAsJsonArray("xcode");
        if (jsonArrayxcode != null) {
          // ensure the json data is an array
          if (!jsonObj.get("xcode").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `xcode` to be an array in the JSON string but got `%s`", jsonObj.get("xcode").toString()));
          }

          // validate the optional field `xcode` (array)
          for (int i = 0; i < jsonArrayxcode.size(); i++) {
            BuildsListToolsets200ResponseXcodeInner.validateJsonElement(jsonArrayxcode.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Toolsets.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Toolsets' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Toolsets> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Toolsets.class));

       return (TypeAdapter<T>) new TypeAdapter<Toolsets>() {
           @Override
           public void write(JsonWriter out, Toolsets value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Toolsets read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Toolsets given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Toolsets
   * @throws IOException if the JSON string is invalid with respect to Toolsets
   */
  public static Toolsets fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Toolsets.class);
  }

  /**
   * Convert an instance of Toolsets to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

