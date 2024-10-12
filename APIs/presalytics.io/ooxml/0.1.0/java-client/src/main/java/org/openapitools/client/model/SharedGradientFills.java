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
 * SharedGradientFills
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:20.731713-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SharedGradientFills {
  public static final String SERIALIZED_NAME_ANGLE = "angle";
  @SerializedName(SERIALIZED_NAME_ANGLE)
  private Integer angle;

  public static final String SERIALIZED_NAME_FILL_MAP_ID = "fillMapId";
  @SerializedName(SERIALIZED_NAME_FILL_MAP_ID)
  private UUID fillMapId;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_IS_PATH = "isPath";
  @SerializedName(SERIALIZED_NAME_IS_PATH)
  private Boolean isPath;

  public static final String SERIALIZED_NAME_PATH_TYPE = "pathType";
  @SerializedName(SERIALIZED_NAME_PATH_TYPE)
  private String pathType;

  public static final String SERIALIZED_NAME_ROTATE_WITH_SHAPE = "rotateWithShape";
  @SerializedName(SERIALIZED_NAME_ROTATE_WITH_SHAPE)
  private Boolean rotateWithShape;

  public SharedGradientFills() {
  }

  public SharedGradientFills angle(Integer angle) {
    this.angle = angle;
    return this;
  }

  /**
   * Get angle
   * @return angle
   */
  @javax.annotation.Nullable
  public Integer getAngle() {
    return angle;
  }

  public void setAngle(Integer angle) {
    this.angle = angle;
  }


  public SharedGradientFills fillMapId(UUID fillMapId) {
    this.fillMapId = fillMapId;
    return this;
  }

  /**
   * Get fillMapId
   * @return fillMapId
   */
  @javax.annotation.Nullable
  public UUID getFillMapId() {
    return fillMapId;
  }

  public void setFillMapId(UUID fillMapId) {
    this.fillMapId = fillMapId;
  }


  public SharedGradientFills id(UUID id) {
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


  public SharedGradientFills isPath(Boolean isPath) {
    this.isPath = isPath;
    return this;
  }

  /**
   * Get isPath
   * @return isPath
   */
  @javax.annotation.Nullable
  public Boolean getIsPath() {
    return isPath;
  }

  public void setIsPath(Boolean isPath) {
    this.isPath = isPath;
  }


  public SharedGradientFills pathType(String pathType) {
    this.pathType = pathType;
    return this;
  }

  /**
   * Get pathType
   * @return pathType
   */
  @javax.annotation.Nullable
  public String getPathType() {
    return pathType;
  }

  public void setPathType(String pathType) {
    this.pathType = pathType;
  }


  public SharedGradientFills rotateWithShape(Boolean rotateWithShape) {
    this.rotateWithShape = rotateWithShape;
    return this;
  }

  /**
   * Get rotateWithShape
   * @return rotateWithShape
   */
  @javax.annotation.Nullable
  public Boolean getRotateWithShape() {
    return rotateWithShape;
  }

  public void setRotateWithShape(Boolean rotateWithShape) {
    this.rotateWithShape = rotateWithShape;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SharedGradientFills sharedGradientFills = (SharedGradientFills) o;
    return Objects.equals(this.angle, sharedGradientFills.angle) &&
        Objects.equals(this.fillMapId, sharedGradientFills.fillMapId) &&
        Objects.equals(this.id, sharedGradientFills.id) &&
        Objects.equals(this.isPath, sharedGradientFills.isPath) &&
        Objects.equals(this.pathType, sharedGradientFills.pathType) &&
        Objects.equals(this.rotateWithShape, sharedGradientFills.rotateWithShape);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(angle, fillMapId, id, isPath, pathType, rotateWithShape);
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
    sb.append("class SharedGradientFills {\n");
    sb.append("    angle: ").append(toIndentedString(angle)).append("\n");
    sb.append("    fillMapId: ").append(toIndentedString(fillMapId)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isPath: ").append(toIndentedString(isPath)).append("\n");
    sb.append("    pathType: ").append(toIndentedString(pathType)).append("\n");
    sb.append("    rotateWithShape: ").append(toIndentedString(rotateWithShape)).append("\n");
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
    openapiFields.add("angle");
    openapiFields.add("fillMapId");
    openapiFields.add("id");
    openapiFields.add("isPath");
    openapiFields.add("pathType");
    openapiFields.add("rotateWithShape");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SharedGradientFills
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SharedGradientFills.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SharedGradientFills is not found in the empty JSON string", SharedGradientFills.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SharedGradientFills.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SharedGradientFills` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("fillMapId") != null && !jsonObj.get("fillMapId").isJsonNull()) && !jsonObj.get("fillMapId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fillMapId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fillMapId").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("pathType") != null && !jsonObj.get("pathType").isJsonNull()) && !jsonObj.get("pathType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pathType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pathType").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SharedGradientFills.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SharedGradientFills' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SharedGradientFills> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SharedGradientFills.class));

       return (TypeAdapter<T>) new TypeAdapter<SharedGradientFills>() {
           @Override
           public void write(JsonWriter out, SharedGradientFills value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SharedGradientFills read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SharedGradientFills given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SharedGradientFills
   * @throws IOException if the JSON string is invalid with respect to SharedGradientFills
   */
  public static SharedGradientFills fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SharedGradientFills.class);
  }

  /**
   * Convert an instance of SharedGradientFills to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

