/*
 * agentOS Api V2, Customer Login Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-customer
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
 * Maintenance Job Note Helper Model:-
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:04.921745-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LandlordMaintenanceJobNoteModel {
  public static final String SERIALIZED_NAME_CREATED_AT = "CreatedAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_NOTE_CONTENTS = "NoteContents";
  @SerializedName(SERIALIZED_NAME_NOTE_CONTENTS)
  private String noteContents;

  public static final String SERIALIZED_NAME_O_I_D = "OID";
  @SerializedName(SERIALIZED_NAME_O_I_D)
  private String OID;

  public LandlordMaintenanceJobNoteModel() {
  }

  public LandlordMaintenanceJobNoteModel createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Created At:-
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public LandlordMaintenanceJobNoteModel noteContents(String noteContents) {
    this.noteContents = noteContents;
    return this;
  }

  /**
   * Note Contents:-
   * @return noteContents
   */
  @javax.annotation.Nullable
  public String getNoteContents() {
    return noteContents;
  }

  public void setNoteContents(String noteContents) {
    this.noteContents = noteContents;
  }


  public LandlordMaintenanceJobNoteModel OID(String OID) {
    this.OID = OID;
    return this;
  }

  /**
   * Job ID:-
   * @return OID
   */
  @javax.annotation.Nullable
  public String getOID() {
    return OID;
  }

  public void setOID(String OID) {
    this.OID = OID;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LandlordMaintenanceJobNoteModel landlordMaintenanceJobNoteModel = (LandlordMaintenanceJobNoteModel) o;
    return Objects.equals(this.createdAt, landlordMaintenanceJobNoteModel.createdAt) &&
        Objects.equals(this.noteContents, landlordMaintenanceJobNoteModel.noteContents) &&
        Objects.equals(this.OID, landlordMaintenanceJobNoteModel.OID);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, noteContents, OID);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LandlordMaintenanceJobNoteModel {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    noteContents: ").append(toIndentedString(noteContents)).append("\n");
    sb.append("    OID: ").append(toIndentedString(OID)).append("\n");
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
    openapiFields.add("CreatedAt");
    openapiFields.add("NoteContents");
    openapiFields.add("OID");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LandlordMaintenanceJobNoteModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LandlordMaintenanceJobNoteModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LandlordMaintenanceJobNoteModel is not found in the empty JSON string", LandlordMaintenanceJobNoteModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LandlordMaintenanceJobNoteModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LandlordMaintenanceJobNoteModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("NoteContents") != null && !jsonObj.get("NoteContents").isJsonNull()) && !jsonObj.get("NoteContents").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `NoteContents` to be a primitive type in the JSON string but got `%s`", jsonObj.get("NoteContents").toString()));
      }
      if ((jsonObj.get("OID") != null && !jsonObj.get("OID").isJsonNull()) && !jsonObj.get("OID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `OID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("OID").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LandlordMaintenanceJobNoteModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LandlordMaintenanceJobNoteModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LandlordMaintenanceJobNoteModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LandlordMaintenanceJobNoteModel.class));

       return (TypeAdapter<T>) new TypeAdapter<LandlordMaintenanceJobNoteModel>() {
           @Override
           public void write(JsonWriter out, LandlordMaintenanceJobNoteModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LandlordMaintenanceJobNoteModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LandlordMaintenanceJobNoteModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LandlordMaintenanceJobNoteModel
   * @throws IOException if the JSON string is invalid with respect to LandlordMaintenanceJobNoteModel
   */
  public static LandlordMaintenanceJobNoteModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LandlordMaintenanceJobNoteModel.class);
  }

  /**
   * Convert an instance of LandlordMaintenanceJobNoteModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

