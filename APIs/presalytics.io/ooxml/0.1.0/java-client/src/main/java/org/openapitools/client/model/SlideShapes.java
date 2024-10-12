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
 * SlideShapes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:20.731713-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SlideShapes {
  public static final String SERIALIZED_NAME_BASE_ELEMENT_BLOB_URL = "baseElementBlobUrl";
  @SerializedName(SERIALIZED_NAME_BASE_ELEMENT_BLOB_URL)
  private String baseElementBlobUrl;

  public static final String SERIALIZED_NAME_CHANGED_BASE_ELEMENT_BLOB_URL = "changedBaseElementBlobUrl";
  @SerializedName(SERIALIZED_NAME_CHANGED_BASE_ELEMENT_BLOB_URL)
  private String changedBaseElementBlobUrl;

  public static final String SERIALIZED_NAME_FLIP_HORIZONTAL = "flipHorizontal";
  @SerializedName(SERIALIZED_NAME_FLIP_HORIZONTAL)
  private Boolean flipHorizontal;

  public static final String SERIALIZED_NAME_FLIP_VERTICAL = "flipVertical";
  @SerializedName(SERIALIZED_NAME_FLIP_VERTICAL)
  private Boolean flipVertical;

  public static final String SERIALIZED_NAME_FREE_FORM_PATH_XML = "freeFormPathXml";
  @SerializedName(SERIALIZED_NAME_FREE_FORM_PATH_XML)
  private String freeFormPathXml;

  public static final String SERIALIZED_NAME_GROUP_ELEMENTS_ID = "groupElementsId";
  @SerializedName(SERIALIZED_NAME_GROUP_ELEMENTS_ID)
  private UUID groupElementsId;

  public static final String SERIALIZED_NAME_HEIGHT = "height";
  @SerializedName(SERIALIZED_NAME_HEIGHT)
  private Integer height;

  public static final String SERIALIZED_NAME_HIDDEN = "hidden";
  @SerializedName(SERIALIZED_NAME_HIDDEN)
  private Boolean hidden;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_IS_THEME_EFFECT = "isThemeEffect";
  @SerializedName(SERIALIZED_NAME_IS_THEME_EFFECT)
  private Boolean isThemeEffect;

  public static final String SERIALIZED_NAME_IS_THEME_FILL = "isThemeFill";
  @SerializedName(SERIALIZED_NAME_IS_THEME_FILL)
  private Boolean isThemeFill;

  public static final String SERIALIZED_NAME_IS_THEME_LINE = "isThemeLine";
  @SerializedName(SERIALIZED_NAME_IS_THEME_LINE)
  private Boolean isThemeLine;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OOXML_ID = "ooxmlId";
  @SerializedName(SERIALIZED_NAME_OOXML_ID)
  private Integer ooxmlId;

  public static final String SERIALIZED_NAME_PACKAGE_URI = "packageUri";
  @SerializedName(SERIALIZED_NAME_PACKAGE_URI)
  private String packageUri;

  public static final String SERIALIZED_NAME_PRESET_TYPE_ID = "presetTypeId";
  @SerializedName(SERIALIZED_NAME_PRESET_TYPE_ID)
  private String presetTypeId;

  public static final String SERIALIZED_NAME_ROTATION = "rotation";
  @SerializedName(SERIALIZED_NAME_ROTATION)
  private Integer rotation;

  public static final String SERIALIZED_NAME_SVG_BLOB_URL = "svgBlobUrl";
  @SerializedName(SERIALIZED_NAME_SVG_BLOB_URL)
  private String svgBlobUrl;

  public static final String SERIALIZED_NAME_WIDTH = "width";
  @SerializedName(SERIALIZED_NAME_WIDTH)
  private Integer width;

  public static final String SERIALIZED_NAME_X_OFFSET = "xOffset";
  @SerializedName(SERIALIZED_NAME_X_OFFSET)
  private Integer xOffset;

  public static final String SERIALIZED_NAME_Y_OFFSET = "yOffset";
  @SerializedName(SERIALIZED_NAME_Y_OFFSET)
  private Integer yOffset;

  public SlideShapes() {
  }

  public SlideShapes baseElementBlobUrl(String baseElementBlobUrl) {
    this.baseElementBlobUrl = baseElementBlobUrl;
    return this;
  }

  /**
   * Get baseElementBlobUrl
   * @return baseElementBlobUrl
   */
  @javax.annotation.Nullable
  public String getBaseElementBlobUrl() {
    return baseElementBlobUrl;
  }

  public void setBaseElementBlobUrl(String baseElementBlobUrl) {
    this.baseElementBlobUrl = baseElementBlobUrl;
  }


  public SlideShapes changedBaseElementBlobUrl(String changedBaseElementBlobUrl) {
    this.changedBaseElementBlobUrl = changedBaseElementBlobUrl;
    return this;
  }

  /**
   * Get changedBaseElementBlobUrl
   * @return changedBaseElementBlobUrl
   */
  @javax.annotation.Nullable
  public String getChangedBaseElementBlobUrl() {
    return changedBaseElementBlobUrl;
  }

  public void setChangedBaseElementBlobUrl(String changedBaseElementBlobUrl) {
    this.changedBaseElementBlobUrl = changedBaseElementBlobUrl;
  }


  public SlideShapes flipHorizontal(Boolean flipHorizontal) {
    this.flipHorizontal = flipHorizontal;
    return this;
  }

  /**
   * Get flipHorizontal
   * @return flipHorizontal
   */
  @javax.annotation.Nullable
  public Boolean getFlipHorizontal() {
    return flipHorizontal;
  }

  public void setFlipHorizontal(Boolean flipHorizontal) {
    this.flipHorizontal = flipHorizontal;
  }


  public SlideShapes flipVertical(Boolean flipVertical) {
    this.flipVertical = flipVertical;
    return this;
  }

  /**
   * Get flipVertical
   * @return flipVertical
   */
  @javax.annotation.Nullable
  public Boolean getFlipVertical() {
    return flipVertical;
  }

  public void setFlipVertical(Boolean flipVertical) {
    this.flipVertical = flipVertical;
  }


  public SlideShapes freeFormPathXml(String freeFormPathXml) {
    this.freeFormPathXml = freeFormPathXml;
    return this;
  }

  /**
   * Get freeFormPathXml
   * @return freeFormPathXml
   */
  @javax.annotation.Nullable
  public String getFreeFormPathXml() {
    return freeFormPathXml;
  }

  public void setFreeFormPathXml(String freeFormPathXml) {
    this.freeFormPathXml = freeFormPathXml;
  }


  public SlideShapes groupElementsId(UUID groupElementsId) {
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


  public SlideShapes height(Integer height) {
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


  public SlideShapes hidden(Boolean hidden) {
    this.hidden = hidden;
    return this;
  }

  /**
   * Get hidden
   * @return hidden
   */
  @javax.annotation.Nullable
  public Boolean getHidden() {
    return hidden;
  }

  public void setHidden(Boolean hidden) {
    this.hidden = hidden;
  }


  public SlideShapes id(UUID id) {
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


  public SlideShapes isThemeEffect(Boolean isThemeEffect) {
    this.isThemeEffect = isThemeEffect;
    return this;
  }

  /**
   * Get isThemeEffect
   * @return isThemeEffect
   */
  @javax.annotation.Nullable
  public Boolean getIsThemeEffect() {
    return isThemeEffect;
  }

  public void setIsThemeEffect(Boolean isThemeEffect) {
    this.isThemeEffect = isThemeEffect;
  }


  public SlideShapes isThemeFill(Boolean isThemeFill) {
    this.isThemeFill = isThemeFill;
    return this;
  }

  /**
   * Get isThemeFill
   * @return isThemeFill
   */
  @javax.annotation.Nullable
  public Boolean getIsThemeFill() {
    return isThemeFill;
  }

  public void setIsThemeFill(Boolean isThemeFill) {
    this.isThemeFill = isThemeFill;
  }


  public SlideShapes isThemeLine(Boolean isThemeLine) {
    this.isThemeLine = isThemeLine;
    return this;
  }

  /**
   * Get isThemeLine
   * @return isThemeLine
   */
  @javax.annotation.Nullable
  public Boolean getIsThemeLine() {
    return isThemeLine;
  }

  public void setIsThemeLine(Boolean isThemeLine) {
    this.isThemeLine = isThemeLine;
  }


  public SlideShapes name(String name) {
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


  public SlideShapes ooxmlId(Integer ooxmlId) {
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


  public SlideShapes packageUri(String packageUri) {
    this.packageUri = packageUri;
    return this;
  }

  /**
   * Get packageUri
   * @return packageUri
   */
  @javax.annotation.Nullable
  public String getPackageUri() {
    return packageUri;
  }

  public void setPackageUri(String packageUri) {
    this.packageUri = packageUri;
  }


  public SlideShapes presetTypeId(String presetTypeId) {
    this.presetTypeId = presetTypeId;
    return this;
  }

  /**
   * Get presetTypeId
   * @return presetTypeId
   */
  @javax.annotation.Nullable
  public String getPresetTypeId() {
    return presetTypeId;
  }

  public void setPresetTypeId(String presetTypeId) {
    this.presetTypeId = presetTypeId;
  }


  public SlideShapes rotation(Integer rotation) {
    this.rotation = rotation;
    return this;
  }

  /**
   * Get rotation
   * @return rotation
   */
  @javax.annotation.Nullable
  public Integer getRotation() {
    return rotation;
  }

  public void setRotation(Integer rotation) {
    this.rotation = rotation;
  }


  public SlideShapes svgBlobUrl(String svgBlobUrl) {
    this.svgBlobUrl = svgBlobUrl;
    return this;
  }

  /**
   * Get svgBlobUrl
   * @return svgBlobUrl
   */
  @javax.annotation.Nullable
  public String getSvgBlobUrl() {
    return svgBlobUrl;
  }

  public void setSvgBlobUrl(String svgBlobUrl) {
    this.svgBlobUrl = svgBlobUrl;
  }


  public SlideShapes width(Integer width) {
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


  public SlideShapes xOffset(Integer xOffset) {
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


  public SlideShapes yOffset(Integer yOffset) {
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
    SlideShapes slideShapes = (SlideShapes) o;
    return Objects.equals(this.baseElementBlobUrl, slideShapes.baseElementBlobUrl) &&
        Objects.equals(this.changedBaseElementBlobUrl, slideShapes.changedBaseElementBlobUrl) &&
        Objects.equals(this.flipHorizontal, slideShapes.flipHorizontal) &&
        Objects.equals(this.flipVertical, slideShapes.flipVertical) &&
        Objects.equals(this.freeFormPathXml, slideShapes.freeFormPathXml) &&
        Objects.equals(this.groupElementsId, slideShapes.groupElementsId) &&
        Objects.equals(this.height, slideShapes.height) &&
        Objects.equals(this.hidden, slideShapes.hidden) &&
        Objects.equals(this.id, slideShapes.id) &&
        Objects.equals(this.isThemeEffect, slideShapes.isThemeEffect) &&
        Objects.equals(this.isThemeFill, slideShapes.isThemeFill) &&
        Objects.equals(this.isThemeLine, slideShapes.isThemeLine) &&
        Objects.equals(this.name, slideShapes.name) &&
        Objects.equals(this.ooxmlId, slideShapes.ooxmlId) &&
        Objects.equals(this.packageUri, slideShapes.packageUri) &&
        Objects.equals(this.presetTypeId, slideShapes.presetTypeId) &&
        Objects.equals(this.rotation, slideShapes.rotation) &&
        Objects.equals(this.svgBlobUrl, slideShapes.svgBlobUrl) &&
        Objects.equals(this.width, slideShapes.width) &&
        Objects.equals(this.xOffset, slideShapes.xOffset) &&
        Objects.equals(this.yOffset, slideShapes.yOffset);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(baseElementBlobUrl, changedBaseElementBlobUrl, flipHorizontal, flipVertical, freeFormPathXml, groupElementsId, height, hidden, id, isThemeEffect, isThemeFill, isThemeLine, name, ooxmlId, packageUri, presetTypeId, rotation, svgBlobUrl, width, xOffset, yOffset);
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
    sb.append("class SlideShapes {\n");
    sb.append("    baseElementBlobUrl: ").append(toIndentedString(baseElementBlobUrl)).append("\n");
    sb.append("    changedBaseElementBlobUrl: ").append(toIndentedString(changedBaseElementBlobUrl)).append("\n");
    sb.append("    flipHorizontal: ").append(toIndentedString(flipHorizontal)).append("\n");
    sb.append("    flipVertical: ").append(toIndentedString(flipVertical)).append("\n");
    sb.append("    freeFormPathXml: ").append(toIndentedString(freeFormPathXml)).append("\n");
    sb.append("    groupElementsId: ").append(toIndentedString(groupElementsId)).append("\n");
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
    sb.append("    hidden: ").append(toIndentedString(hidden)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isThemeEffect: ").append(toIndentedString(isThemeEffect)).append("\n");
    sb.append("    isThemeFill: ").append(toIndentedString(isThemeFill)).append("\n");
    sb.append("    isThemeLine: ").append(toIndentedString(isThemeLine)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    ooxmlId: ").append(toIndentedString(ooxmlId)).append("\n");
    sb.append("    packageUri: ").append(toIndentedString(packageUri)).append("\n");
    sb.append("    presetTypeId: ").append(toIndentedString(presetTypeId)).append("\n");
    sb.append("    rotation: ").append(toIndentedString(rotation)).append("\n");
    sb.append("    svgBlobUrl: ").append(toIndentedString(svgBlobUrl)).append("\n");
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
    openapiFields.add("baseElementBlobUrl");
    openapiFields.add("changedBaseElementBlobUrl");
    openapiFields.add("flipHorizontal");
    openapiFields.add("flipVertical");
    openapiFields.add("freeFormPathXml");
    openapiFields.add("groupElementsId");
    openapiFields.add("height");
    openapiFields.add("hidden");
    openapiFields.add("id");
    openapiFields.add("isThemeEffect");
    openapiFields.add("isThemeFill");
    openapiFields.add("isThemeLine");
    openapiFields.add("name");
    openapiFields.add("ooxmlId");
    openapiFields.add("packageUri");
    openapiFields.add("presetTypeId");
    openapiFields.add("rotation");
    openapiFields.add("svgBlobUrl");
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
   * @throws IOException if the JSON Element is invalid with respect to SlideShapes
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SlideShapes.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SlideShapes is not found in the empty JSON string", SlideShapes.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SlideShapes.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SlideShapes` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("baseElementBlobUrl") != null && !jsonObj.get("baseElementBlobUrl").isJsonNull()) && !jsonObj.get("baseElementBlobUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `baseElementBlobUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("baseElementBlobUrl").toString()));
      }
      if ((jsonObj.get("changedBaseElementBlobUrl") != null && !jsonObj.get("changedBaseElementBlobUrl").isJsonNull()) && !jsonObj.get("changedBaseElementBlobUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `changedBaseElementBlobUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("changedBaseElementBlobUrl").toString()));
      }
      if ((jsonObj.get("freeFormPathXml") != null && !jsonObj.get("freeFormPathXml").isJsonNull()) && !jsonObj.get("freeFormPathXml").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `freeFormPathXml` to be a primitive type in the JSON string but got `%s`", jsonObj.get("freeFormPathXml").toString()));
      }
      if ((jsonObj.get("groupElementsId") != null && !jsonObj.get("groupElementsId").isJsonNull()) && !jsonObj.get("groupElementsId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `groupElementsId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("groupElementsId").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("packageUri") != null && !jsonObj.get("packageUri").isJsonNull()) && !jsonObj.get("packageUri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `packageUri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("packageUri").toString()));
      }
      if ((jsonObj.get("presetTypeId") != null && !jsonObj.get("presetTypeId").isJsonNull()) && !jsonObj.get("presetTypeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `presetTypeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("presetTypeId").toString()));
      }
      if ((jsonObj.get("svgBlobUrl") != null && !jsonObj.get("svgBlobUrl").isJsonNull()) && !jsonObj.get("svgBlobUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `svgBlobUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("svgBlobUrl").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SlideShapes.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SlideShapes' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SlideShapes> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SlideShapes.class));

       return (TypeAdapter<T>) new TypeAdapter<SlideShapes>() {
           @Override
           public void write(JsonWriter out, SlideShapes value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SlideShapes read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SlideShapes given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SlideShapes
   * @throws IOException if the JSON string is invalid with respect to SlideShapes
   */
  public static SlideShapes fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SlideShapes.class);
  }

  /**
   * Convert an instance of SlideShapes to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

