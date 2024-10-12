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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.UUID;
import org.openapitools.client.model.SharedColorTransformationAttributesDetails;
import org.openapitools.client.model.SharedSolidFillsDetails;
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
 * SharedColorTransformationsDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:20.731713-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SharedColorTransformationsDetails {
  public static final String SERIALIZED_NAME_COLOR_TRANSFORMATION_ATTRIBUTES = "colorTransformationAttributes";
  @SerializedName(SERIALIZED_NAME_COLOR_TRANSFORMATION_ATTRIBUTES)
  private List<SharedColorTransformationAttributesDetails> colorTransformationAttributes;

  public static final String SERIALIZED_NAME_DATE_CREATED = "dateCreated";
  @SerializedName(SERIALIZED_NAME_DATE_CREATED)
  private OffsetDateTime dateCreated;

  public static final String SERIALIZED_NAME_DATE_MODIFIED = "dateModified";
  @SerializedName(SERIALIZED_NAME_DATE_MODIFIED)
  private OffsetDateTime dateModified;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PARENT_SOLID_FILL = "parentSolidFill";
  @SerializedName(SERIALIZED_NAME_PARENT_SOLID_FILL)
  private SharedSolidFillsDetails parentSolidFill;

  public static final String SERIALIZED_NAME_SOLID_FILLS_ID = "solidFillsId";
  @SerializedName(SERIALIZED_NAME_SOLID_FILLS_ID)
  private UUID solidFillsId;

  public static final String SERIALIZED_NAME_USER_CREATED = "userCreated";
  @SerializedName(SERIALIZED_NAME_USER_CREATED)
  private UUID userCreated;

  public static final String SERIALIZED_NAME_USER_MODIFIED = "userModified";
  @SerializedName(SERIALIZED_NAME_USER_MODIFIED)
  private UUID userModified;

  public SharedColorTransformationsDetails() {
  }

  public SharedColorTransformationsDetails colorTransformationAttributes(List<SharedColorTransformationAttributesDetails> colorTransformationAttributes) {
    this.colorTransformationAttributes = colorTransformationAttributes;
    return this;
  }

  public SharedColorTransformationsDetails addColorTransformationAttributesItem(SharedColorTransformationAttributesDetails colorTransformationAttributesItem) {
    if (this.colorTransformationAttributes == null) {
      this.colorTransformationAttributes = new ArrayList<>();
    }
    this.colorTransformationAttributes.add(colorTransformationAttributesItem);
    return this;
  }

  /**
   * Get colorTransformationAttributes
   * @return colorTransformationAttributes
   */
  @javax.annotation.Nullable
  public List<SharedColorTransformationAttributesDetails> getColorTransformationAttributes() {
    return colorTransformationAttributes;
  }

  public void setColorTransformationAttributes(List<SharedColorTransformationAttributesDetails> colorTransformationAttributes) {
    this.colorTransformationAttributes = colorTransformationAttributes;
  }


  public SharedColorTransformationsDetails dateCreated(OffsetDateTime dateCreated) {
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


  public SharedColorTransformationsDetails dateModified(OffsetDateTime dateModified) {
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


  public SharedColorTransformationsDetails id(UUID id) {
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


  public SharedColorTransformationsDetails name(String name) {
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


  public SharedColorTransformationsDetails parentSolidFill(SharedSolidFillsDetails parentSolidFill) {
    this.parentSolidFill = parentSolidFill;
    return this;
  }

  /**
   * Get parentSolidFill
   * @return parentSolidFill
   */
  @javax.annotation.Nullable
  public SharedSolidFillsDetails getParentSolidFill() {
    return parentSolidFill;
  }

  public void setParentSolidFill(SharedSolidFillsDetails parentSolidFill) {
    this.parentSolidFill = parentSolidFill;
  }


  public SharedColorTransformationsDetails solidFillsId(UUID solidFillsId) {
    this.solidFillsId = solidFillsId;
    return this;
  }

  /**
   * Get solidFillsId
   * @return solidFillsId
   */
  @javax.annotation.Nullable
  public UUID getSolidFillsId() {
    return solidFillsId;
  }

  public void setSolidFillsId(UUID solidFillsId) {
    this.solidFillsId = solidFillsId;
  }


  public SharedColorTransformationsDetails userCreated(UUID userCreated) {
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


  public SharedColorTransformationsDetails userModified(UUID userModified) {
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
    SharedColorTransformationsDetails sharedColorTransformationsDetails = (SharedColorTransformationsDetails) o;
    return Objects.equals(this.colorTransformationAttributes, sharedColorTransformationsDetails.colorTransformationAttributes) &&
        Objects.equals(this.dateCreated, sharedColorTransformationsDetails.dateCreated) &&
        Objects.equals(this.dateModified, sharedColorTransformationsDetails.dateModified) &&
        Objects.equals(this.id, sharedColorTransformationsDetails.id) &&
        Objects.equals(this.name, sharedColorTransformationsDetails.name) &&
        Objects.equals(this.parentSolidFill, sharedColorTransformationsDetails.parentSolidFill) &&
        Objects.equals(this.solidFillsId, sharedColorTransformationsDetails.solidFillsId) &&
        Objects.equals(this.userCreated, sharedColorTransformationsDetails.userCreated) &&
        Objects.equals(this.userModified, sharedColorTransformationsDetails.userModified);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(colorTransformationAttributes, dateCreated, dateModified, id, name, parentSolidFill, solidFillsId, userCreated, userModified);
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
    sb.append("class SharedColorTransformationsDetails {\n");
    sb.append("    colorTransformationAttributes: ").append(toIndentedString(colorTransformationAttributes)).append("\n");
    sb.append("    dateCreated: ").append(toIndentedString(dateCreated)).append("\n");
    sb.append("    dateModified: ").append(toIndentedString(dateModified)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    parentSolidFill: ").append(toIndentedString(parentSolidFill)).append("\n");
    sb.append("    solidFillsId: ").append(toIndentedString(solidFillsId)).append("\n");
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
    openapiFields.add("colorTransformationAttributes");
    openapiFields.add("dateCreated");
    openapiFields.add("dateModified");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("parentSolidFill");
    openapiFields.add("solidFillsId");
    openapiFields.add("userCreated");
    openapiFields.add("userModified");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SharedColorTransformationsDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SharedColorTransformationsDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SharedColorTransformationsDetails is not found in the empty JSON string", SharedColorTransformationsDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SharedColorTransformationsDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SharedColorTransformationsDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("colorTransformationAttributes") != null && !jsonObj.get("colorTransformationAttributes").isJsonNull()) {
        JsonArray jsonArraycolorTransformationAttributes = jsonObj.getAsJsonArray("colorTransformationAttributes");
        if (jsonArraycolorTransformationAttributes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("colorTransformationAttributes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `colorTransformationAttributes` to be an array in the JSON string but got `%s`", jsonObj.get("colorTransformationAttributes").toString()));
          }

          // validate the optional field `colorTransformationAttributes` (array)
          for (int i = 0; i < jsonArraycolorTransformationAttributes.size(); i++) {
            SharedColorTransformationAttributesDetails.validateJsonElement(jsonArraycolorTransformationAttributes.get(i));
          };
        }
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the optional field `parentSolidFill`
      if (jsonObj.get("parentSolidFill") != null && !jsonObj.get("parentSolidFill").isJsonNull()) {
        SharedSolidFillsDetails.validateJsonElement(jsonObj.get("parentSolidFill"));
      }
      if ((jsonObj.get("solidFillsId") != null && !jsonObj.get("solidFillsId").isJsonNull()) && !jsonObj.get("solidFillsId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `solidFillsId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("solidFillsId").toString()));
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
       if (!SharedColorTransformationsDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SharedColorTransformationsDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SharedColorTransformationsDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SharedColorTransformationsDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<SharedColorTransformationsDetails>() {
           @Override
           public void write(JsonWriter out, SharedColorTransformationsDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SharedColorTransformationsDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SharedColorTransformationsDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SharedColorTransformationsDetails
   * @throws IOException if the JSON string is invalid with respect to SharedColorTransformationsDetails
   */
  public static SharedColorTransformationsDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SharedColorTransformationsDetails.class);
  }

  /**
   * Convert an instance of SharedColorTransformationsDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

