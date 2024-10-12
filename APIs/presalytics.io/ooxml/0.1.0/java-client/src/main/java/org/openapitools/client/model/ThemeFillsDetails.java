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
import org.openapitools.client.model.SharedFillMapDetails;
import org.openapitools.client.model.ThemeThemesDetails;
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
 * ThemeFillsDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:20.731713-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ThemeFillsDetails {
  public static final String SERIALIZED_NAME_DATE_CREATED = "dateCreated";
  @SerializedName(SERIALIZED_NAME_DATE_CREATED)
  private OffsetDateTime dateCreated;

  public static final String SERIALIZED_NAME_DATE_MODIFIED = "dateModified";
  @SerializedName(SERIALIZED_NAME_DATE_MODIFIED)
  private OffsetDateTime dateModified;

  public static final String SERIALIZED_NAME_FILL_MAP = "fillMap";
  @SerializedName(SERIALIZED_NAME_FILL_MAP)
  private SharedFillMapDetails fillMap;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_INTENSITY_ID = "intensityId";
  @SerializedName(SERIALIZED_NAME_INTENSITY_ID)
  private Integer intensityId;

  public static final String SERIALIZED_NAME_THEME = "theme";
  @SerializedName(SERIALIZED_NAME_THEME)
  private ThemeThemesDetails theme;

  public static final String SERIALIZED_NAME_THEME_ID = "themeId";
  @SerializedName(SERIALIZED_NAME_THEME_ID)
  private UUID themeId;

  public static final String SERIALIZED_NAME_USER_CREATED = "userCreated";
  @SerializedName(SERIALIZED_NAME_USER_CREATED)
  private UUID userCreated;

  public static final String SERIALIZED_NAME_USER_MODIFIED = "userModified";
  @SerializedName(SERIALIZED_NAME_USER_MODIFIED)
  private UUID userModified;

  public ThemeFillsDetails() {
  }

  public ThemeFillsDetails dateCreated(OffsetDateTime dateCreated) {
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


  public ThemeFillsDetails dateModified(OffsetDateTime dateModified) {
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


  public ThemeFillsDetails fillMap(SharedFillMapDetails fillMap) {
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


  public ThemeFillsDetails id(UUID id) {
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


  public ThemeFillsDetails intensityId(Integer intensityId) {
    this.intensityId = intensityId;
    return this;
  }

  /**
   * Get intensityId
   * @return intensityId
   */
  @javax.annotation.Nullable
  public Integer getIntensityId() {
    return intensityId;
  }

  public void setIntensityId(Integer intensityId) {
    this.intensityId = intensityId;
  }


  public ThemeFillsDetails theme(ThemeThemesDetails theme) {
    this.theme = theme;
    return this;
  }

  /**
   * Get theme
   * @return theme
   */
  @javax.annotation.Nullable
  public ThemeThemesDetails getTheme() {
    return theme;
  }

  public void setTheme(ThemeThemesDetails theme) {
    this.theme = theme;
  }


  public ThemeFillsDetails themeId(UUID themeId) {
    this.themeId = themeId;
    return this;
  }

  /**
   * Get themeId
   * @return themeId
   */
  @javax.annotation.Nullable
  public UUID getThemeId() {
    return themeId;
  }

  public void setThemeId(UUID themeId) {
    this.themeId = themeId;
  }


  public ThemeFillsDetails userCreated(UUID userCreated) {
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


  public ThemeFillsDetails userModified(UUID userModified) {
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
    ThemeFillsDetails themeFillsDetails = (ThemeFillsDetails) o;
    return Objects.equals(this.dateCreated, themeFillsDetails.dateCreated) &&
        Objects.equals(this.dateModified, themeFillsDetails.dateModified) &&
        Objects.equals(this.fillMap, themeFillsDetails.fillMap) &&
        Objects.equals(this.id, themeFillsDetails.id) &&
        Objects.equals(this.intensityId, themeFillsDetails.intensityId) &&
        Objects.equals(this.theme, themeFillsDetails.theme) &&
        Objects.equals(this.themeId, themeFillsDetails.themeId) &&
        Objects.equals(this.userCreated, themeFillsDetails.userCreated) &&
        Objects.equals(this.userModified, themeFillsDetails.userModified);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(dateCreated, dateModified, fillMap, id, intensityId, theme, themeId, userCreated, userModified);
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
    sb.append("class ThemeFillsDetails {\n");
    sb.append("    dateCreated: ").append(toIndentedString(dateCreated)).append("\n");
    sb.append("    dateModified: ").append(toIndentedString(dateModified)).append("\n");
    sb.append("    fillMap: ").append(toIndentedString(fillMap)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    intensityId: ").append(toIndentedString(intensityId)).append("\n");
    sb.append("    theme: ").append(toIndentedString(theme)).append("\n");
    sb.append("    themeId: ").append(toIndentedString(themeId)).append("\n");
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
    openapiFields.add("dateCreated");
    openapiFields.add("dateModified");
    openapiFields.add("fillMap");
    openapiFields.add("id");
    openapiFields.add("intensityId");
    openapiFields.add("theme");
    openapiFields.add("themeId");
    openapiFields.add("userCreated");
    openapiFields.add("userModified");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ThemeFillsDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ThemeFillsDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ThemeFillsDetails is not found in the empty JSON string", ThemeFillsDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ThemeFillsDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ThemeFillsDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `fillMap`
      if (jsonObj.get("fillMap") != null && !jsonObj.get("fillMap").isJsonNull()) {
        SharedFillMapDetails.validateJsonElement(jsonObj.get("fillMap"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `theme`
      if (jsonObj.get("theme") != null && !jsonObj.get("theme").isJsonNull()) {
        ThemeThemesDetails.validateJsonElement(jsonObj.get("theme"));
      }
      if ((jsonObj.get("themeId") != null && !jsonObj.get("themeId").isJsonNull()) && !jsonObj.get("themeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `themeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("themeId").toString()));
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
       if (!ThemeFillsDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ThemeFillsDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ThemeFillsDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ThemeFillsDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<ThemeFillsDetails>() {
           @Override
           public void write(JsonWriter out, ThemeFillsDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ThemeFillsDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ThemeFillsDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ThemeFillsDetails
   * @throws IOException if the JSON string is invalid with respect to ThemeFillsDetails
   */
  public static ThemeFillsDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ThemeFillsDetails.class);
  }

  /**
   * Convert an instance of ThemeFillsDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

