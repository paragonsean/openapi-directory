/*
 * Face Client
 * An API for face detection, verification, and identification.
 *
 * The version of the OpenAPI document: 1.0
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
import org.openapitools.client.model.PersistedFace;
import org.openapitools.client.model.RecognitionModel;

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
 * Face list object.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:23.692507-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FaceList {
  public static final String SERIALIZED_NAME_FACE_LIST_ID = "faceListId";
  @SerializedName(SERIALIZED_NAME_FACE_LIST_ID)
  private String faceListId;

  public static final String SERIALIZED_NAME_PERSISTED_FACES = "persistedFaces";
  @SerializedName(SERIALIZED_NAME_PERSISTED_FACES)
  private List<PersistedFace> persistedFaces = new ArrayList<>();

  public static final String SERIALIZED_NAME_RECOGNITION_MODEL = "recognitionModel";
  @SerializedName(SERIALIZED_NAME_RECOGNITION_MODEL)
  private RecognitionModel recognitionModel = RecognitionModel._01;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_USER_DATA = "userData";
  @SerializedName(SERIALIZED_NAME_USER_DATA)
  private String userData;

  public FaceList() {
  }

  public FaceList faceListId(String faceListId) {
    this.faceListId = faceListId;
    return this;
  }

  /**
   * FaceListId of the target face list.
   * @return faceListId
   */
  @javax.annotation.Nonnull
  public String getFaceListId() {
    return faceListId;
  }

  public void setFaceListId(String faceListId) {
    this.faceListId = faceListId;
  }


  public FaceList persistedFaces(List<PersistedFace> persistedFaces) {
    this.persistedFaces = persistedFaces;
    return this;
  }

  public FaceList addPersistedFacesItem(PersistedFace persistedFacesItem) {
    if (this.persistedFaces == null) {
      this.persistedFaces = new ArrayList<>();
    }
    this.persistedFaces.add(persistedFacesItem);
    return this;
  }

  /**
   * An array of persisted faces within the face list or large face list.
   * @return persistedFaces
   */
  @javax.annotation.Nullable
  public List<PersistedFace> getPersistedFaces() {
    return persistedFaces;
  }

  public void setPersistedFaces(List<PersistedFace> persistedFaces) {
    this.persistedFaces = persistedFaces;
  }


  public FaceList recognitionModel(RecognitionModel recognitionModel) {
    this.recognitionModel = recognitionModel;
    return this;
  }

  /**
   * Get recognitionModel
   * @return recognitionModel
   */
  @javax.annotation.Nullable
  public RecognitionModel getRecognitionModel() {
    return recognitionModel;
  }

  public void setRecognitionModel(RecognitionModel recognitionModel) {
    this.recognitionModel = recognitionModel;
  }


  public FaceList name(String name) {
    this.name = name;
    return this;
  }

  /**
   * User defined name, maximum length is 128.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public FaceList userData(String userData) {
    this.userData = userData;
    return this;
  }

  /**
   * User specified data. Length should not exceed 16KB.
   * @return userData
   */
  @javax.annotation.Nullable
  public String getUserData() {
    return userData;
  }

  public void setUserData(String userData) {
    this.userData = userData;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FaceList faceList = (FaceList) o;
    return Objects.equals(this.faceListId, faceList.faceListId) &&
        Objects.equals(this.persistedFaces, faceList.persistedFaces) &&
        Objects.equals(this.recognitionModel, faceList.recognitionModel) &&
        Objects.equals(this.name, faceList.name) &&
        Objects.equals(this.userData, faceList.userData);
  }

  @Override
  public int hashCode() {
    return Objects.hash(faceListId, persistedFaces, recognitionModel, name, userData);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FaceList {\n");
    sb.append("    faceListId: ").append(toIndentedString(faceListId)).append("\n");
    sb.append("    persistedFaces: ").append(toIndentedString(persistedFaces)).append("\n");
    sb.append("    recognitionModel: ").append(toIndentedString(recognitionModel)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    userData: ").append(toIndentedString(userData)).append("\n");
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
    openapiFields.add("recognitionModel");
    openapiFields.add("name");
    openapiFields.add("userData");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("faceListId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FaceList
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FaceList.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FaceList is not found in the empty JSON string", FaceList.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FaceList.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FaceList` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : FaceList.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("faceListId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `faceListId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("faceListId").toString()));
      }
      if (jsonObj.get("persistedFaces") != null && !jsonObj.get("persistedFaces").isJsonNull()) {
        JsonArray jsonArraypersistedFaces = jsonObj.getAsJsonArray("persistedFaces");
        if (jsonArraypersistedFaces != null) {
          // ensure the json data is an array
          if (!jsonObj.get("persistedFaces").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `persistedFaces` to be an array in the JSON string but got `%s`", jsonObj.get("persistedFaces").toString()));
          }

          // validate the optional field `persistedFaces` (array)
          for (int i = 0; i < jsonArraypersistedFaces.size(); i++) {
            PersistedFace.validateJsonElement(jsonArraypersistedFaces.get(i));
          };
        }
      }
      // validate the optional field `recognitionModel`
      if (jsonObj.get("recognitionModel") != null && !jsonObj.get("recognitionModel").isJsonNull()) {
        RecognitionModel.validateJsonElement(jsonObj.get("recognitionModel"));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("userData") != null && !jsonObj.get("userData").isJsonNull()) && !jsonObj.get("userData").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userData` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userData").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FaceList.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FaceList' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FaceList> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FaceList.class));

       return (TypeAdapter<T>) new TypeAdapter<FaceList>() {
           @Override
           public void write(JsonWriter out, FaceList value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FaceList read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FaceList given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FaceList
   * @throws IOException if the JSON string is invalid with respect to FaceList
   */
  public static FaceList fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FaceList.class);
  }

  /**
   * Convert an instance of FaceList to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

