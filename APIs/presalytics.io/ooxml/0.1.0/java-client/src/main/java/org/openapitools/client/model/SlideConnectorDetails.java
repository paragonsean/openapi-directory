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
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.UUID;
import org.openapitools.client.model.SharedEffectsDetails;
import org.openapitools.client.model.SharedFillMapDetails;
import org.openapitools.client.model.SharedLinesDetails;
import org.openapitools.client.model.SlideGroupElementsDetails;
import org.openapitools.client.model.SlideShapesDetails;
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
 * SlideConnectorDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:20.731713-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SlideConnectorDetails {
  public static final String SERIALIZED_NAME_BASE_ELEMENT_BLOB_URL = "baseElementBlobUrl";
  @SerializedName(SERIALIZED_NAME_BASE_ELEMENT_BLOB_URL)
  private String baseElementBlobUrl;

  public static final String SERIALIZED_NAME_CHANGED_BASE_ELEMENT_BLOB_URL = "changedBaseElementBlobUrl";
  @SerializedName(SERIALIZED_NAME_CHANGED_BASE_ELEMENT_BLOB_URL)
  private String changedBaseElementBlobUrl;

  public static final String SERIALIZED_NAME_DATE_CREATED = "dateCreated";
  @SerializedName(SERIALIZED_NAME_DATE_CREATED)
  private OffsetDateTime dateCreated;

  public static final String SERIALIZED_NAME_DATE_MODIFIED = "dateModified";
  @SerializedName(SERIALIZED_NAME_DATE_MODIFIED)
  private OffsetDateTime dateModified;

  public static final String SERIALIZED_NAME_EFFECT = "effect";
  @SerializedName(SERIALIZED_NAME_EFFECT)
  private SharedEffectsDetails effect;

  public static final String SERIALIZED_NAME_END_CONNECTION_IDX = "endConnectionIdx";
  @SerializedName(SERIALIZED_NAME_END_CONNECTION_IDX)
  private Integer endConnectionIdx;

  public static final String SERIALIZED_NAME_END_CONNECTION_SHAPE = "endConnectionShape";
  @SerializedName(SERIALIZED_NAME_END_CONNECTION_SHAPE)
  private SlideShapesDetails endConnectionShape;

  public static final String SERIALIZED_NAME_END_CONNECTION_SHAPE_ID = "endConnectionShapeId";
  @SerializedName(SERIALIZED_NAME_END_CONNECTION_SHAPE_ID)
  private UUID endConnectionShapeId;

  public static final String SERIALIZED_NAME_FILL_MAP = "fillMap";
  @SerializedName(SERIALIZED_NAME_FILL_MAP)
  private SharedFillMapDetails fillMap;

  public static final String SERIALIZED_NAME_FLIP_HORIZONTAL = "flipHorizontal";
  @SerializedName(SERIALIZED_NAME_FLIP_HORIZONTAL)
  private Boolean flipHorizontal;

  public static final String SERIALIZED_NAME_FLIP_VERTICAL = "flipVertical";
  @SerializedName(SERIALIZED_NAME_FLIP_VERTICAL)
  private Boolean flipVertical;

  public static final String SERIALIZED_NAME_FREE_FORM_PATH_XML = "freeFormPathXml";
  @SerializedName(SERIALIZED_NAME_FREE_FORM_PATH_XML)
  private String freeFormPathXml;

  public static final String SERIALIZED_NAME_GROUP_ELEMENT = "groupElement";
  @SerializedName(SERIALIZED_NAME_GROUP_ELEMENT)
  private SlideGroupElementsDetails groupElement;

  public static final String SERIALIZED_NAME_GROUP_ELEMENTS_ID = "groupElementsId";
  @SerializedName(SERIALIZED_NAME_GROUP_ELEMENTS_ID)
  private UUID groupElementsId;

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

  public static final String SERIALIZED_NAME_LINE = "line";
  @SerializedName(SERIALIZED_NAME_LINE)
  private SharedLinesDetails line;

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

  public static final String SERIALIZED_NAME_START_CONNECTION_IDX = "startConnectionIdx";
  @SerializedName(SERIALIZED_NAME_START_CONNECTION_IDX)
  private Integer startConnectionIdx;

  public static final String SERIALIZED_NAME_START_CONNECTION_SHAPE = "startConnectionShape";
  @SerializedName(SERIALIZED_NAME_START_CONNECTION_SHAPE)
  private SlideShapesDetails startConnectionShape;

  public static final String SERIALIZED_NAME_START_CONNECTION_SHAPE_ID = "startConnectionShapeId";
  @SerializedName(SERIALIZED_NAME_START_CONNECTION_SHAPE_ID)
  private UUID startConnectionShapeId;

  public static final String SERIALIZED_NAME_SVG_BLOB_URL = "svgBlobUrl";
  @SerializedName(SERIALIZED_NAME_SVG_BLOB_URL)
  private String svgBlobUrl;

  public static final String SERIALIZED_NAME_USER_CREATED = "userCreated";
  @SerializedName(SERIALIZED_NAME_USER_CREATED)
  private UUID userCreated;

  public static final String SERIALIZED_NAME_USER_MODIFIED = "userModified";
  @SerializedName(SERIALIZED_NAME_USER_MODIFIED)
  private UUID userModified;

  public SlideConnectorDetails() {
  }

  public SlideConnectorDetails baseElementBlobUrl(String baseElementBlobUrl) {
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


  public SlideConnectorDetails changedBaseElementBlobUrl(String changedBaseElementBlobUrl) {
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


  public SlideConnectorDetails dateCreated(OffsetDateTime dateCreated) {
    this.dateCreated = dateCreated;
    return this;
  }

  /**
   * Get dateCreated
   * @return dateCreated
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateCreated() {
    return dateCreated;
  }

  public void setDateCreated(OffsetDateTime dateCreated) {
    this.dateCreated = dateCreated;
  }


  public SlideConnectorDetails dateModified(OffsetDateTime dateModified) {
    this.dateModified = dateModified;
    return this;
  }

  /**
   * Get dateModified
   * @return dateModified
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateModified() {
    return dateModified;
  }

  public void setDateModified(OffsetDateTime dateModified) {
    this.dateModified = dateModified;
  }


  public SlideConnectorDetails effect(SharedEffectsDetails effect) {
    this.effect = effect;
    return this;
  }

  /**
   * Get effect
   * @return effect
   */
  @javax.annotation.Nullable
  public SharedEffectsDetails getEffect() {
    return effect;
  }

  public void setEffect(SharedEffectsDetails effect) {
    this.effect = effect;
  }


  public SlideConnectorDetails endConnectionIdx(Integer endConnectionIdx) {
    this.endConnectionIdx = endConnectionIdx;
    return this;
  }

  /**
   * Get endConnectionIdx
   * @return endConnectionIdx
   */
  @javax.annotation.Nullable
  public Integer getEndConnectionIdx() {
    return endConnectionIdx;
  }

  public void setEndConnectionIdx(Integer endConnectionIdx) {
    this.endConnectionIdx = endConnectionIdx;
  }


  public SlideConnectorDetails endConnectionShape(SlideShapesDetails endConnectionShape) {
    this.endConnectionShape = endConnectionShape;
    return this;
  }

  /**
   * Get endConnectionShape
   * @return endConnectionShape
   */
  @javax.annotation.Nullable
  public SlideShapesDetails getEndConnectionShape() {
    return endConnectionShape;
  }

  public void setEndConnectionShape(SlideShapesDetails endConnectionShape) {
    this.endConnectionShape = endConnectionShape;
  }


  public SlideConnectorDetails endConnectionShapeId(UUID endConnectionShapeId) {
    this.endConnectionShapeId = endConnectionShapeId;
    return this;
  }

  /**
   * Get endConnectionShapeId
   * @return endConnectionShapeId
   */
  @javax.annotation.Nullable
  public UUID getEndConnectionShapeId() {
    return endConnectionShapeId;
  }

  public void setEndConnectionShapeId(UUID endConnectionShapeId) {
    this.endConnectionShapeId = endConnectionShapeId;
  }


  public SlideConnectorDetails fillMap(SharedFillMapDetails fillMap) {
    this.fillMap = fillMap;
    return this;
  }

  /**
   * Get fillMap
   * @return fillMap
   */
  @javax.annotation.Nullable
  public SharedFillMapDetails getFillMap() {
    return fillMap;
  }

  public void setFillMap(SharedFillMapDetails fillMap) {
    this.fillMap = fillMap;
  }


  public SlideConnectorDetails flipHorizontal(Boolean flipHorizontal) {
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


  public SlideConnectorDetails flipVertical(Boolean flipVertical) {
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


  public SlideConnectorDetails freeFormPathXml(String freeFormPathXml) {
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


  public SlideConnectorDetails groupElement(SlideGroupElementsDetails groupElement) {
    this.groupElement = groupElement;
    return this;
  }

  /**
   * Get groupElement
   * @return groupElement
   */
  @javax.annotation.Nullable
  public SlideGroupElementsDetails getGroupElement() {
    return groupElement;
  }

  public void setGroupElement(SlideGroupElementsDetails groupElement) {
    this.groupElement = groupElement;
  }


  public SlideConnectorDetails groupElementsId(UUID groupElementsId) {
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


  public SlideConnectorDetails hidden(Boolean hidden) {
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


  public SlideConnectorDetails id(UUID id) {
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


  public SlideConnectorDetails isThemeEffect(Boolean isThemeEffect) {
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


  public SlideConnectorDetails isThemeFill(Boolean isThemeFill) {
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


  public SlideConnectorDetails isThemeLine(Boolean isThemeLine) {
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


  public SlideConnectorDetails line(SharedLinesDetails line) {
    this.line = line;
    return this;
  }

  /**
   * Get line
   * @return line
   */
  @javax.annotation.Nullable
  public SharedLinesDetails getLine() {
    return line;
  }

  public void setLine(SharedLinesDetails line) {
    this.line = line;
  }


  public SlideConnectorDetails name(String name) {
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


  public SlideConnectorDetails ooxmlId(Integer ooxmlId) {
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


  public SlideConnectorDetails packageUri(String packageUri) {
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


  public SlideConnectorDetails presetTypeId(String presetTypeId) {
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


  public SlideConnectorDetails rotation(Integer rotation) {
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


  public SlideConnectorDetails startConnectionIdx(Integer startConnectionIdx) {
    this.startConnectionIdx = startConnectionIdx;
    return this;
  }

  /**
   * Get startConnectionIdx
   * @return startConnectionIdx
   */
  @javax.annotation.Nullable
  public Integer getStartConnectionIdx() {
    return startConnectionIdx;
  }

  public void setStartConnectionIdx(Integer startConnectionIdx) {
    this.startConnectionIdx = startConnectionIdx;
  }


  public SlideConnectorDetails startConnectionShape(SlideShapesDetails startConnectionShape) {
    this.startConnectionShape = startConnectionShape;
    return this;
  }

  /**
   * Get startConnectionShape
   * @return startConnectionShape
   */
  @javax.annotation.Nullable
  public SlideShapesDetails getStartConnectionShape() {
    return startConnectionShape;
  }

  public void setStartConnectionShape(SlideShapesDetails startConnectionShape) {
    this.startConnectionShape = startConnectionShape;
  }


  public SlideConnectorDetails startConnectionShapeId(UUID startConnectionShapeId) {
    this.startConnectionShapeId = startConnectionShapeId;
    return this;
  }

  /**
   * Get startConnectionShapeId
   * @return startConnectionShapeId
   */
  @javax.annotation.Nullable
  public UUID getStartConnectionShapeId() {
    return startConnectionShapeId;
  }

  public void setStartConnectionShapeId(UUID startConnectionShapeId) {
    this.startConnectionShapeId = startConnectionShapeId;
  }


  public SlideConnectorDetails svgBlobUrl(String svgBlobUrl) {
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


  public SlideConnectorDetails userCreated(UUID userCreated) {
    this.userCreated = userCreated;
    return this;
  }

  /**
   * Get userCreated
   * @return userCreated
   */
  @javax.annotation.Nullable
  public UUID getUserCreated() {
    return userCreated;
  }

  public void setUserCreated(UUID userCreated) {
    this.userCreated = userCreated;
  }


  public SlideConnectorDetails userModified(UUID userModified) {
    this.userModified = userModified;
    return this;
  }

  /**
   * Get userModified
   * @return userModified
   */
  @javax.annotation.Nullable
  public UUID getUserModified() {
    return userModified;
  }

  public void setUserModified(UUID userModified) {
    this.userModified = userModified;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SlideConnectorDetails slideConnectorDetails = (SlideConnectorDetails) o;
    return Objects.equals(this.baseElementBlobUrl, slideConnectorDetails.baseElementBlobUrl) &&
        Objects.equals(this.changedBaseElementBlobUrl, slideConnectorDetails.changedBaseElementBlobUrl) &&
        Objects.equals(this.dateCreated, slideConnectorDetails.dateCreated) &&
        Objects.equals(this.dateModified, slideConnectorDetails.dateModified) &&
        Objects.equals(this.effect, slideConnectorDetails.effect) &&
        Objects.equals(this.endConnectionIdx, slideConnectorDetails.endConnectionIdx) &&
        Objects.equals(this.endConnectionShape, slideConnectorDetails.endConnectionShape) &&
        Objects.equals(this.endConnectionShapeId, slideConnectorDetails.endConnectionShapeId) &&
        Objects.equals(this.fillMap, slideConnectorDetails.fillMap) &&
        Objects.equals(this.flipHorizontal, slideConnectorDetails.flipHorizontal) &&
        Objects.equals(this.flipVertical, slideConnectorDetails.flipVertical) &&
        Objects.equals(this.freeFormPathXml, slideConnectorDetails.freeFormPathXml) &&
        Objects.equals(this.groupElement, slideConnectorDetails.groupElement) &&
        Objects.equals(this.groupElementsId, slideConnectorDetails.groupElementsId) &&
        Objects.equals(this.hidden, slideConnectorDetails.hidden) &&
        Objects.equals(this.id, slideConnectorDetails.id) &&
        Objects.equals(this.isThemeEffect, slideConnectorDetails.isThemeEffect) &&
        Objects.equals(this.isThemeFill, slideConnectorDetails.isThemeFill) &&
        Objects.equals(this.isThemeLine, slideConnectorDetails.isThemeLine) &&
        Objects.equals(this.line, slideConnectorDetails.line) &&
        Objects.equals(this.name, slideConnectorDetails.name) &&
        Objects.equals(this.ooxmlId, slideConnectorDetails.ooxmlId) &&
        Objects.equals(this.packageUri, slideConnectorDetails.packageUri) &&
        Objects.equals(this.presetTypeId, slideConnectorDetails.presetTypeId) &&
        Objects.equals(this.rotation, slideConnectorDetails.rotation) &&
        Objects.equals(this.startConnectionIdx, slideConnectorDetails.startConnectionIdx) &&
        Objects.equals(this.startConnectionShape, slideConnectorDetails.startConnectionShape) &&
        Objects.equals(this.startConnectionShapeId, slideConnectorDetails.startConnectionShapeId) &&
        Objects.equals(this.svgBlobUrl, slideConnectorDetails.svgBlobUrl) &&
        Objects.equals(this.userCreated, slideConnectorDetails.userCreated) &&
        Objects.equals(this.userModified, slideConnectorDetails.userModified);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(baseElementBlobUrl, changedBaseElementBlobUrl, dateCreated, dateModified, effect, endConnectionIdx, endConnectionShape, endConnectionShapeId, fillMap, flipHorizontal, flipVertical, freeFormPathXml, groupElement, groupElementsId, hidden, id, isThemeEffect, isThemeFill, isThemeLine, line, name, ooxmlId, packageUri, presetTypeId, rotation, startConnectionIdx, startConnectionShape, startConnectionShapeId, svgBlobUrl, userCreated, userModified);
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
    sb.append("class SlideConnectorDetails {\n");
    sb.append("    baseElementBlobUrl: ").append(toIndentedString(baseElementBlobUrl)).append("\n");
    sb.append("    changedBaseElementBlobUrl: ").append(toIndentedString(changedBaseElementBlobUrl)).append("\n");
    sb.append("    dateCreated: ").append(toIndentedString(dateCreated)).append("\n");
    sb.append("    dateModified: ").append(toIndentedString(dateModified)).append("\n");
    sb.append("    effect: ").append(toIndentedString(effect)).append("\n");
    sb.append("    endConnectionIdx: ").append(toIndentedString(endConnectionIdx)).append("\n");
    sb.append("    endConnectionShape: ").append(toIndentedString(endConnectionShape)).append("\n");
    sb.append("    endConnectionShapeId: ").append(toIndentedString(endConnectionShapeId)).append("\n");
    sb.append("    fillMap: ").append(toIndentedString(fillMap)).append("\n");
    sb.append("    flipHorizontal: ").append(toIndentedString(flipHorizontal)).append("\n");
    sb.append("    flipVertical: ").append(toIndentedString(flipVertical)).append("\n");
    sb.append("    freeFormPathXml: ").append(toIndentedString(freeFormPathXml)).append("\n");
    sb.append("    groupElement: ").append(toIndentedString(groupElement)).append("\n");
    sb.append("    groupElementsId: ").append(toIndentedString(groupElementsId)).append("\n");
    sb.append("    hidden: ").append(toIndentedString(hidden)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isThemeEffect: ").append(toIndentedString(isThemeEffect)).append("\n");
    sb.append("    isThemeFill: ").append(toIndentedString(isThemeFill)).append("\n");
    sb.append("    isThemeLine: ").append(toIndentedString(isThemeLine)).append("\n");
    sb.append("    line: ").append(toIndentedString(line)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    ooxmlId: ").append(toIndentedString(ooxmlId)).append("\n");
    sb.append("    packageUri: ").append(toIndentedString(packageUri)).append("\n");
    sb.append("    presetTypeId: ").append(toIndentedString(presetTypeId)).append("\n");
    sb.append("    rotation: ").append(toIndentedString(rotation)).append("\n");
    sb.append("    startConnectionIdx: ").append(toIndentedString(startConnectionIdx)).append("\n");
    sb.append("    startConnectionShape: ").append(toIndentedString(startConnectionShape)).append("\n");
    sb.append("    startConnectionShapeId: ").append(toIndentedString(startConnectionShapeId)).append("\n");
    sb.append("    svgBlobUrl: ").append(toIndentedString(svgBlobUrl)).append("\n");
    sb.append("    userCreated: ").append(toIndentedString(userCreated)).append("\n");
    sb.append("    userModified: ").append(toIndentedString(userModified)).append("\n");
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
    openapiFields.add("dateCreated");
    openapiFields.add("dateModified");
    openapiFields.add("effect");
    openapiFields.add("endConnectionIdx");
    openapiFields.add("endConnectionShape");
    openapiFields.add("endConnectionShapeId");
    openapiFields.add("fillMap");
    openapiFields.add("flipHorizontal");
    openapiFields.add("flipVertical");
    openapiFields.add("freeFormPathXml");
    openapiFields.add("groupElement");
    openapiFields.add("groupElementsId");
    openapiFields.add("hidden");
    openapiFields.add("id");
    openapiFields.add("isThemeEffect");
    openapiFields.add("isThemeFill");
    openapiFields.add("isThemeLine");
    openapiFields.add("line");
    openapiFields.add("name");
    openapiFields.add("ooxmlId");
    openapiFields.add("packageUri");
    openapiFields.add("presetTypeId");
    openapiFields.add("rotation");
    openapiFields.add("startConnectionIdx");
    openapiFields.add("startConnectionShape");
    openapiFields.add("startConnectionShapeId");
    openapiFields.add("svgBlobUrl");
    openapiFields.add("userCreated");
    openapiFields.add("userModified");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SlideConnectorDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SlideConnectorDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SlideConnectorDetails is not found in the empty JSON string", SlideConnectorDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SlideConnectorDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SlideConnectorDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("baseElementBlobUrl") != null && !jsonObj.get("baseElementBlobUrl").isJsonNull()) && !jsonObj.get("baseElementBlobUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `baseElementBlobUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("baseElementBlobUrl").toString()));
      }
      if ((jsonObj.get("changedBaseElementBlobUrl") != null && !jsonObj.get("changedBaseElementBlobUrl").isJsonNull()) && !jsonObj.get("changedBaseElementBlobUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `changedBaseElementBlobUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("changedBaseElementBlobUrl").toString()));
      }
      // validate the optional field `effect`
      if (jsonObj.get("effect") != null && !jsonObj.get("effect").isJsonNull()) {
        SharedEffectsDetails.validateJsonElement(jsonObj.get("effect"));
      }
      // validate the optional field `endConnectionShape`
      if (jsonObj.get("endConnectionShape") != null && !jsonObj.get("endConnectionShape").isJsonNull()) {
        SlideShapesDetails.validateJsonElement(jsonObj.get("endConnectionShape"));
      }
      if ((jsonObj.get("endConnectionShapeId") != null && !jsonObj.get("endConnectionShapeId").isJsonNull()) && !jsonObj.get("endConnectionShapeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `endConnectionShapeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("endConnectionShapeId").toString()));
      }
      // validate the optional field `fillMap`
      if (jsonObj.get("fillMap") != null && !jsonObj.get("fillMap").isJsonNull()) {
        SharedFillMapDetails.validateJsonElement(jsonObj.get("fillMap"));
      }
      if ((jsonObj.get("freeFormPathXml") != null && !jsonObj.get("freeFormPathXml").isJsonNull()) && !jsonObj.get("freeFormPathXml").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `freeFormPathXml` to be a primitive type in the JSON string but got `%s`", jsonObj.get("freeFormPathXml").toString()));
      }
      // validate the optional field `groupElement`
      if (jsonObj.get("groupElement") != null && !jsonObj.get("groupElement").isJsonNull()) {
        SlideGroupElementsDetails.validateJsonElement(jsonObj.get("groupElement"));
      }
      if ((jsonObj.get("groupElementsId") != null && !jsonObj.get("groupElementsId").isJsonNull()) && !jsonObj.get("groupElementsId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `groupElementsId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("groupElementsId").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `line`
      if (jsonObj.get("line") != null && !jsonObj.get("line").isJsonNull()) {
        SharedLinesDetails.validateJsonElement(jsonObj.get("line"));
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
      // validate the optional field `startConnectionShape`
      if (jsonObj.get("startConnectionShape") != null && !jsonObj.get("startConnectionShape").isJsonNull()) {
        SlideShapesDetails.validateJsonElement(jsonObj.get("startConnectionShape"));
      }
      if ((jsonObj.get("startConnectionShapeId") != null && !jsonObj.get("startConnectionShapeId").isJsonNull()) && !jsonObj.get("startConnectionShapeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `startConnectionShapeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("startConnectionShapeId").toString()));
      }
      if ((jsonObj.get("svgBlobUrl") != null && !jsonObj.get("svgBlobUrl").isJsonNull()) && !jsonObj.get("svgBlobUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `svgBlobUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("svgBlobUrl").toString()));
      }
      if ((jsonObj.get("userCreated") != null && !jsonObj.get("userCreated").isJsonNull()) && !jsonObj.get("userCreated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userCreated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userCreated").toString()));
      }
      if ((jsonObj.get("userModified") != null && !jsonObj.get("userModified").isJsonNull()) && !jsonObj.get("userModified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userModified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userModified").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SlideConnectorDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SlideConnectorDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SlideConnectorDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SlideConnectorDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<SlideConnectorDetails>() {
           @Override
           public void write(JsonWriter out, SlideConnectorDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SlideConnectorDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SlideConnectorDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SlideConnectorDetails
   * @throws IOException if the JSON string is invalid with respect to SlideConnectorDetails
   */
  public static SlideConnectorDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SlideConnectorDetails.class);
  }

  /**
   * Convert an instance of SlideConnectorDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

