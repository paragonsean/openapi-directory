/*
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
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
import java.util.UUID;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * SlideGraphics
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:20.731713-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SlideGraphics {
  public static final String SERIALIZED_NAME_GRAPHIC_TYPE_ID = "graphicTypeId";
  @SerializedName(SERIALIZED_NAME_GRAPHIC_TYPE_ID)
  private Integer graphicTypeId;

  public static final String SERIALIZED_NAME_GROUP_ELEMENTS_ID = "groupElementsId";
  @SerializedName(SERIALIZED_NAME_GROUP_ELEMENTS_ID)
  private UUID groupElementsId;

  public static final String SERIALIZED_NAME_HEIGHT = "height";
  @SerializedName(SERIALIZED_NAME_HEIGHT)
  private Integer height;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OOXML_ID = "ooxmlId";
  @SerializedName(SERIALIZED_NAME_OOXML_ID)
  private Integer ooxmlId;

  public static final String SERIALIZED_NAME_WIDTH = "width";
  @SerializedName(SERIALIZED_NAME_WIDTH)
  private Integer width;

  public static final String SERIALIZED_NAME_X_OFFSET = "xOffset";
  @SerializedName(SERIALIZED_NAME_X_OFFSET)
  private Integer xOffset;

  public static final String SERIALIZED_NAME_Y_OFFSET = "yOffset";
  @SerializedName(SERIALIZED_NAME_Y_OFFSET)
  private Integer yOffset;

  public SlideGraphics() {
  }

  public SlideGraphics graphicTypeId(Integer graphicTypeId) {
    this.graphicTypeId = graphicTypeId;
    return this;
  }

  /**
   * Get graphicTypeId
   * @return graphicTypeId
   */
  @javax.annotation.Nullable
  public Integer getGraphicTypeId() {
    return graphicTypeId;
  }

  public void setGraphicTypeId(Integer graphicTypeId) {
    this.graphicTypeId = graphicTypeId;
  }


  public SlideGraphics groupElementsId(UUID groupElementsId) {
    this.groupElementsId = groupElementsId;
    return this;
  }

  /**
   * Get groupElementsId
   * @return groupElementsId
   */
  @javax.annotation.Nullable
  public UUID getGroupElementsId() {
    return groupElementsId;
  }

  public void setGroupElementsId(UUID groupElementsId) {
    this.groupElementsId = groupElementsId;
  }


  public SlideGraphics height(Integer height) {
    this.height = height;
    return this;
  }

  /**
   * Get height
   * @return height
   */
  @javax.annotation.Nullable
  public Integer getHeight() {
    return height;
  }

  public void setHeight(Integer height) {
    this.height = height;
  }


  public SlideGraphics id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public SlideGraphics name(String name) {
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


  public SlideGraphics ooxmlId(Integer ooxmlId) {
    this.ooxmlId = ooxmlId;
    return this;
  }

  /**
   * Get ooxmlId
   * @return ooxmlId
   */
  @javax.annotation.Nullable
  public Integer getOoxmlId() {
    return ooxmlId;
  }

  public void setOoxmlId(Integer ooxmlId) {
    this.ooxmlId = ooxmlId;
  }


  public SlideGraphics width(Integer width) {
    this.width = width;
    return this;
  }

  /**
   * Get width
   * @return width
   */
  @javax.annotation.Nullable
  public Integer getWidth() {
    return width;
  }

  public void setWidth(Integer width) {
    this.width = width;
  }


  public SlideGraphics xOffset(Integer xOffset) {
    this.xOffset = xOffset;
    return this;
  }

  /**
   * Get xOffset
   * @return xOffset
   */
  @javax.annotation.Nullable
  public Integer getxOffset() {
    return xOffset;
  }

  public void setxOffset(Integer xOffset) {
    this.xOffset = xOffset;
  }


  public SlideGraphics yOffset(Integer yOffset) {
    this.yOffset = yOffset;
    return this;
  }

  /**
   * Get yOffset
   * @return yOffset
   */
  @javax.annotation.Nullable
  public Integer getyOffset() {
    return yOffset;
  }

  public void setyOffset(Integer yOffset) {
    this.yOffset = yOffset;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SlideGraphics slideGraphics = (SlideGraphics) o;
    return Objects.equals(this.graphicTypeId, slideGraphics.graphicTypeId) &&
        Objects.equals(this.groupElementsId, slideGraphics.groupElementsId) &&
        Objects.equals(this.height, slideGraphics.height) &&
        Objects.equals(this.id, slideGraphics.id) &&
        Objects.equals(this.name, slideGraphics.name) &&
        Objects.equals(this.ooxmlId, slideGraphics.ooxmlId) &&
        Objects.equals(this.width, slideGraphics.width) &&
        Objects.equals(this.xOffset, slideGraphics.xOffset) &&
        Objects.equals(this.yOffset, slideGraphics.yOffset);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(graphicTypeId, groupElementsId, height, id, name, ooxmlId, width, xOffset, yOffset);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SlideGraphics {\n");
    sb.append("    graphicTypeId: ").append(toIndentedString(graphicTypeId)).append("\n");
    sb.append("    groupElementsId: ").append(toIndentedString(groupElementsId)).append("\n");
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    ooxmlId: ").append(toIndentedString(ooxmlId)).append("\n");
    sb.append("    width: ").append(toIndentedString(width)).append("\n");
    sb.append("    xOffset: ").append(toIndentedString(xOffset)).append("\n");
    sb.append("    yOffset: ").append(toIndentedString(yOffset)).append("\n");
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
    openapiFields.add("graphicTypeId");
    openapiFields.add("groupElementsId");
    openapiFields.add("height");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("ooxmlId");
    openapiFields.add("width");
    openapiFields.add("xOffset");
    openapiFields.add("yOffset");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SlideGraphics
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SlideGraphics.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SlideGraphics is not found in the empty JSON string", SlideGraphics.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SlideGraphics.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SlideGraphics` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("groupElementsId") != null && !jsonObj.get("groupElementsId").isJsonNull()) && !jsonObj.get("groupElementsId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `groupElementsId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("groupElementsId").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SlideGraphics.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SlideGraphics' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SlideGraphics> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SlideGraphics.class));

       return (TypeAdapter<T>) new TypeAdapter<SlideGraphics>() {
           @Override
           public void write(JsonWriter out, SlideGraphics value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SlideGraphics read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SlideGraphics given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SlideGraphics
   * @throws IOException if the JSON string is invalid with respect to SlideGraphics
   */
  public static SlideGraphics fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SlideGraphics.class);
  }

  /**
   * Convert an instance of SlideGraphics to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

