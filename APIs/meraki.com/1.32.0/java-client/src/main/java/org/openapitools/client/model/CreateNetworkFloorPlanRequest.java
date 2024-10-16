/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
import org.openapitools.client.model.CreateNetworkFloorPlanRequestBottomLeftCorner;
import org.openapitools.client.model.CreateNetworkFloorPlanRequestBottomRightCorner;
import org.openapitools.client.model.CreateNetworkFloorPlanRequestCenter;
import org.openapitools.client.model.CreateNetworkFloorPlanRequestTopLeftCorner;
import org.openapitools.client.model.CreateNetworkFloorPlanRequestTopRightCorner;

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
 * CreateNetworkFloorPlanRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateNetworkFloorPlanRequest {
  public static final String SERIALIZED_NAME_BOTTOM_LEFT_CORNER = "bottomLeftCorner";
  @SerializedName(SERIALIZED_NAME_BOTTOM_LEFT_CORNER)
  private CreateNetworkFloorPlanRequestBottomLeftCorner bottomLeftCorner;

  public static final String SERIALIZED_NAME_BOTTOM_RIGHT_CORNER = "bottomRightCorner";
  @SerializedName(SERIALIZED_NAME_BOTTOM_RIGHT_CORNER)
  private CreateNetworkFloorPlanRequestBottomRightCorner bottomRightCorner;

  public static final String SERIALIZED_NAME_CENTER = "center";
  @SerializedName(SERIALIZED_NAME_CENTER)
  private CreateNetworkFloorPlanRequestCenter center;

  public static final String SERIALIZED_NAME_IMAGE_CONTENTS = "imageContents";
  @SerializedName(SERIALIZED_NAME_IMAGE_CONTENTS)
  private byte[] imageContents;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_TOP_LEFT_CORNER = "topLeftCorner";
  @SerializedName(SERIALIZED_NAME_TOP_LEFT_CORNER)
  private CreateNetworkFloorPlanRequestTopLeftCorner topLeftCorner;

  public static final String SERIALIZED_NAME_TOP_RIGHT_CORNER = "topRightCorner";
  @SerializedName(SERIALIZED_NAME_TOP_RIGHT_CORNER)
  private CreateNetworkFloorPlanRequestTopRightCorner topRightCorner;

  public CreateNetworkFloorPlanRequest() {
  }

  public CreateNetworkFloorPlanRequest bottomLeftCorner(CreateNetworkFloorPlanRequestBottomLeftCorner bottomLeftCorner) {
    this.bottomLeftCorner = bottomLeftCorner;
    return this;
  }

  /**
   * Get bottomLeftCorner
   * @return bottomLeftCorner
   */
  @javax.annotation.Nullable
  public CreateNetworkFloorPlanRequestBottomLeftCorner getBottomLeftCorner() {
    return bottomLeftCorner;
  }

  public void setBottomLeftCorner(CreateNetworkFloorPlanRequestBottomLeftCorner bottomLeftCorner) {
    this.bottomLeftCorner = bottomLeftCorner;
  }


  public CreateNetworkFloorPlanRequest bottomRightCorner(CreateNetworkFloorPlanRequestBottomRightCorner bottomRightCorner) {
    this.bottomRightCorner = bottomRightCorner;
    return this;
  }

  /**
   * Get bottomRightCorner
   * @return bottomRightCorner
   */
  @javax.annotation.Nullable
  public CreateNetworkFloorPlanRequestBottomRightCorner getBottomRightCorner() {
    return bottomRightCorner;
  }

  public void setBottomRightCorner(CreateNetworkFloorPlanRequestBottomRightCorner bottomRightCorner) {
    this.bottomRightCorner = bottomRightCorner;
  }


  public CreateNetworkFloorPlanRequest center(CreateNetworkFloorPlanRequestCenter center) {
    this.center = center;
    return this;
  }

  /**
   * Get center
   * @return center
   */
  @javax.annotation.Nullable
  public CreateNetworkFloorPlanRequestCenter getCenter() {
    return center;
  }

  public void setCenter(CreateNetworkFloorPlanRequestCenter center) {
    this.center = center;
  }


  public CreateNetworkFloorPlanRequest imageContents(byte[] imageContents) {
    this.imageContents = imageContents;
    return this;
  }

  /**
   * The file contents (a base 64 encoded string) of your image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in.
   * @return imageContents
   */
  @javax.annotation.Nonnull
  public byte[] getImageContents() {
    return imageContents;
  }

  public void setImageContents(byte[] imageContents) {
    this.imageContents = imageContents;
  }


  public CreateNetworkFloorPlanRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of your floor plan.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CreateNetworkFloorPlanRequest topLeftCorner(CreateNetworkFloorPlanRequestTopLeftCorner topLeftCorner) {
    this.topLeftCorner = topLeftCorner;
    return this;
  }

  /**
   * Get topLeftCorner
   * @return topLeftCorner
   */
  @javax.annotation.Nullable
  public CreateNetworkFloorPlanRequestTopLeftCorner getTopLeftCorner() {
    return topLeftCorner;
  }

  public void setTopLeftCorner(CreateNetworkFloorPlanRequestTopLeftCorner topLeftCorner) {
    this.topLeftCorner = topLeftCorner;
  }


  public CreateNetworkFloorPlanRequest topRightCorner(CreateNetworkFloorPlanRequestTopRightCorner topRightCorner) {
    this.topRightCorner = topRightCorner;
    return this;
  }

  /**
   * Get topRightCorner
   * @return topRightCorner
   */
  @javax.annotation.Nullable
  public CreateNetworkFloorPlanRequestTopRightCorner getTopRightCorner() {
    return topRightCorner;
  }

  public void setTopRightCorner(CreateNetworkFloorPlanRequestTopRightCorner topRightCorner) {
    this.topRightCorner = topRightCorner;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateNetworkFloorPlanRequest createNetworkFloorPlanRequest = (CreateNetworkFloorPlanRequest) o;
    return Objects.equals(this.bottomLeftCorner, createNetworkFloorPlanRequest.bottomLeftCorner) &&
        Objects.equals(this.bottomRightCorner, createNetworkFloorPlanRequest.bottomRightCorner) &&
        Objects.equals(this.center, createNetworkFloorPlanRequest.center) &&
        Arrays.equals(this.imageContents, createNetworkFloorPlanRequest.imageContents) &&
        Objects.equals(this.name, createNetworkFloorPlanRequest.name) &&
        Objects.equals(this.topLeftCorner, createNetworkFloorPlanRequest.topLeftCorner) &&
        Objects.equals(this.topRightCorner, createNetworkFloorPlanRequest.topRightCorner);
  }

  @Override
  public int hashCode() {
    return Objects.hash(bottomLeftCorner, bottomRightCorner, center, Arrays.hashCode(imageContents), name, topLeftCorner, topRightCorner);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateNetworkFloorPlanRequest {\n");
    sb.append("    bottomLeftCorner: ").append(toIndentedString(bottomLeftCorner)).append("\n");
    sb.append("    bottomRightCorner: ").append(toIndentedString(bottomRightCorner)).append("\n");
    sb.append("    center: ").append(toIndentedString(center)).append("\n");
    sb.append("    imageContents: ").append(toIndentedString(imageContents)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    topLeftCorner: ").append(toIndentedString(topLeftCorner)).append("\n");
    sb.append("    topRightCorner: ").append(toIndentedString(topRightCorner)).append("\n");
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
    openapiFields.add("bottomLeftCorner");
    openapiFields.add("bottomRightCorner");
    openapiFields.add("center");
    openapiFields.add("imageContents");
    openapiFields.add("name");
    openapiFields.add("topLeftCorner");
    openapiFields.add("topRightCorner");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("imageContents");
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateNetworkFloorPlanRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateNetworkFloorPlanRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateNetworkFloorPlanRequest is not found in the empty JSON string", CreateNetworkFloorPlanRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateNetworkFloorPlanRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateNetworkFloorPlanRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateNetworkFloorPlanRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `bottomLeftCorner`
      if (jsonObj.get("bottomLeftCorner") != null && !jsonObj.get("bottomLeftCorner").isJsonNull()) {
        CreateNetworkFloorPlanRequestBottomLeftCorner.validateJsonElement(jsonObj.get("bottomLeftCorner"));
      }
      // validate the optional field `bottomRightCorner`
      if (jsonObj.get("bottomRightCorner") != null && !jsonObj.get("bottomRightCorner").isJsonNull()) {
        CreateNetworkFloorPlanRequestBottomRightCorner.validateJsonElement(jsonObj.get("bottomRightCorner"));
      }
      // validate the optional field `center`
      if (jsonObj.get("center") != null && !jsonObj.get("center").isJsonNull()) {
        CreateNetworkFloorPlanRequestCenter.validateJsonElement(jsonObj.get("center"));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the optional field `topLeftCorner`
      if (jsonObj.get("topLeftCorner") != null && !jsonObj.get("topLeftCorner").isJsonNull()) {
        CreateNetworkFloorPlanRequestTopLeftCorner.validateJsonElement(jsonObj.get("topLeftCorner"));
      }
      // validate the optional field `topRightCorner`
      if (jsonObj.get("topRightCorner") != null && !jsonObj.get("topRightCorner").isJsonNull()) {
        CreateNetworkFloorPlanRequestTopRightCorner.validateJsonElement(jsonObj.get("topRightCorner"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateNetworkFloorPlanRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateNetworkFloorPlanRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateNetworkFloorPlanRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateNetworkFloorPlanRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateNetworkFloorPlanRequest>() {
           @Override
           public void write(JsonWriter out, CreateNetworkFloorPlanRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateNetworkFloorPlanRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateNetworkFloorPlanRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateNetworkFloorPlanRequest
   * @throws IOException if the JSON string is invalid with respect to CreateNetworkFloorPlanRequest
   */
  public static CreateNetworkFloorPlanRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateNetworkFloorPlanRequest.class);
  }

  /**
   * Convert an instance of CreateNetworkFloorPlanRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

