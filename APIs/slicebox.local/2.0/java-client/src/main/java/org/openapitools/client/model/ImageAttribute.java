/*
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
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
 * ImageAttribute
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:37.231084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ImageAttribute {
  public static final String SERIALIZED_NAME_DEPTH = "depth";
  @SerializedName(SERIALIZED_NAME_DEPTH)
  private Integer depth;

  public static final String SERIALIZED_NAME_ELEMENT = "element";
  @SerializedName(SERIALIZED_NAME_ELEMENT)
  private String element;

  public static final String SERIALIZED_NAME_GROUP = "group";
  @SerializedName(SERIALIZED_NAME_GROUP)
  private String group;

  public static final String SERIALIZED_NAME_LENGTH = "length";
  @SerializedName(SERIALIZED_NAME_LENGTH)
  private Integer length;

  public static final String SERIALIZED_NAME_MULTIPLICITY = "multiplicity";
  @SerializedName(SERIALIZED_NAME_MULTIPLICITY)
  private Integer multiplicity;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PATH = "path";
  @SerializedName(SERIALIZED_NAME_PATH)
  private String path;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private String value;

  public static final String SERIALIZED_NAME_VR = "vr";
  @SerializedName(SERIALIZED_NAME_VR)
  private String vr;

  public ImageAttribute() {
  }

  public ImageAttribute depth(Integer depth) {
    this.depth = depth;
    return this;
  }

  /**
   * Get depth
   * @return depth
   */
  @javax.annotation.Nullable
  public Integer getDepth() {
    return depth;
  }

  public void setDepth(Integer depth) {
    this.depth = depth;
  }


  public ImageAttribute element(String element) {
    this.element = element;
    return this;
  }

  /**
   * Get element
   * @return element
   */
  @javax.annotation.Nullable
  public String getElement() {
    return element;
  }

  public void setElement(String element) {
    this.element = element;
  }


  public ImageAttribute group(String group) {
    this.group = group;
    return this;
  }

  /**
   * Get group
   * @return group
   */
  @javax.annotation.Nullable
  public String getGroup() {
    return group;
  }

  public void setGroup(String group) {
    this.group = group;
  }


  public ImageAttribute length(Integer length) {
    this.length = length;
    return this;
  }

  /**
   * Get length
   * @return length
   */
  @javax.annotation.Nullable
  public Integer getLength() {
    return length;
  }

  public void setLength(Integer length) {
    this.length = length;
  }


  public ImageAttribute multiplicity(Integer multiplicity) {
    this.multiplicity = multiplicity;
    return this;
  }

  /**
   * Get multiplicity
   * @return multiplicity
   */
  @javax.annotation.Nullable
  public Integer getMultiplicity() {
    return multiplicity;
  }

  public void setMultiplicity(Integer multiplicity) {
    this.multiplicity = multiplicity;
  }


  public ImageAttribute name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ImageAttribute path(String path) {
    this.path = path;
    return this;
  }

  /**
   * Get path
   * @return path
   */
  @javax.annotation.Nullable
  public String getPath() {
    return path;
  }

  public void setPath(String path) {
    this.path = path;
  }


  public ImageAttribute value(String value) {
    this.value = value;
    return this;
  }

  /**
   * Get value
   * @return value
   */
  @javax.annotation.Nullable
  public String getValue() {
    return value;
  }

  public void setValue(String value) {
    this.value = value;
  }


  public ImageAttribute vr(String vr) {
    this.vr = vr;
    return this;
  }

  /**
   * Get vr
   * @return vr
   */
  @javax.annotation.Nullable
  public String getVr() {
    return vr;
  }

  public void setVr(String vr) {
    this.vr = vr;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ImageAttribute imageAttribute = (ImageAttribute) o;
    return Objects.equals(this.depth, imageAttribute.depth) &&
        Objects.equals(this.element, imageAttribute.element) &&
        Objects.equals(this.group, imageAttribute.group) &&
        Objects.equals(this.length, imageAttribute.length) &&
        Objects.equals(this.multiplicity, imageAttribute.multiplicity) &&
        Objects.equals(this.name, imageAttribute.name) &&
        Objects.equals(this.path, imageAttribute.path) &&
        Objects.equals(this.value, imageAttribute.value) &&
        Objects.equals(this.vr, imageAttribute.vr);
  }

  @Override
  public int hashCode() {
    return Objects.hash(depth, element, group, length, multiplicity, name, path, value, vr);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ImageAttribute {\n");
    sb.append("    depth: ").append(toIndentedString(depth)).append("\n");
    sb.append("    element: ").append(toIndentedString(element)).append("\n");
    sb.append("    group: ").append(toIndentedString(group)).append("\n");
    sb.append("    length: ").append(toIndentedString(length)).append("\n");
    sb.append("    multiplicity: ").append(toIndentedString(multiplicity)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    path: ").append(toIndentedString(path)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("    vr: ").append(toIndentedString(vr)).append("\n");
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
    openapiFields.add("depth");
    openapiFields.add("element");
    openapiFields.add("group");
    openapiFields.add("length");
    openapiFields.add("multiplicity");
    openapiFields.add("name");
    openapiFields.add("path");
    openapiFields.add("value");
    openapiFields.add("vr");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ImageAttribute
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ImageAttribute.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ImageAttribute is not found in the empty JSON string", ImageAttribute.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ImageAttribute.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ImageAttribute` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("element") != null && !jsonObj.get("element").isJsonNull()) && !jsonObj.get("element").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `element` to be a primitive type in the JSON string but got `%s`", jsonObj.get("element").toString()));
      }
      if ((jsonObj.get("group") != null && !jsonObj.get("group").isJsonNull()) && !jsonObj.get("group").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `group` to be a primitive type in the JSON string but got `%s`", jsonObj.get("group").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("path") != null && !jsonObj.get("path").isJsonNull()) && !jsonObj.get("path").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `path` to be a primitive type in the JSON string but got `%s`", jsonObj.get("path").toString()));
      }
      if ((jsonObj.get("value") != null && !jsonObj.get("value").isJsonNull()) && !jsonObj.get("value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value").toString()));
      }
      if ((jsonObj.get("vr") != null && !jsonObj.get("vr").isJsonNull()) && !jsonObj.get("vr").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vr` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vr").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ImageAttribute.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ImageAttribute' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ImageAttribute> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ImageAttribute.class));

       return (TypeAdapter<T>) new TypeAdapter<ImageAttribute>() {
           @Override
           public void write(JsonWriter out, ImageAttribute value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ImageAttribute read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ImageAttribute given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ImageAttribute
   * @throws IOException if the JSON string is invalid with respect to ImageAttribute
   */
  public static ImageAttribute fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ImageAttribute.class);
  }

  /**
   * Convert an instance of ImageAttribute to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

