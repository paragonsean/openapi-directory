/*
 * LetMC Api V2, Free (Tier 1)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-free-tier
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
 * Stores the &#39;Sales&#39; type fields for property ownable as a stepping stone to a full on BO when we finally get the go ahead to write sales!!
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:12.156803-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PropertyModel {
  public static final String SERIALIZED_NAME_AREA = "Area";
  @SerializedName(SERIALIZED_NAME_AREA)
  private String area;

  public static final String SERIALIZED_NAME_BRANCH = "Branch";
  @SerializedName(SERIALIZED_NAME_BRANCH)
  private String branch;

  public static final String SERIALIZED_NAME_DESCRIPTION = "Description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ETAG = "ETag";
  @SerializedName(SERIALIZED_NAME_ETAG)
  private String etag;

  public static final String SERIALIZED_NAME_FULL_ADDRESS = "FullAddress";
  @SerializedName(SERIALIZED_NAME_FULL_ADDRESS)
  private String fullAddress;

  public static final String SERIALIZED_NAME_GLOBAL_REFERENCE = "GlobalReference";
  @SerializedName(SERIALIZED_NAME_GLOBAL_REFERENCE)
  private String globalReference;

  public static final String SERIALIZED_NAME_MAIN_PHOTO = "MainPhoto";
  @SerializedName(SERIALIZED_NAME_MAIN_PHOTO)
  private String mainPhoto;

  public static final String SERIALIZED_NAME_MANAGED_BY_STAFF = "ManagedByStaff";
  @SerializedName(SERIALIZED_NAME_MANAGED_BY_STAFF)
  private String managedByStaff;

  public static final String SERIALIZED_NAME_O_I_D = "OID";
  @SerializedName(SERIALIZED_NAME_O_I_D)
  private String OID;

  public static final String SERIALIZED_NAME_PROPERTY_SOURCE = "PropertySource";
  @SerializedName(SERIALIZED_NAME_PROPERTY_SOURCE)
  private String propertySource;

  /**
   * The block or property type.
   */
  @JsonAdapter(PropertyTypeEnum.Adapter.class)
  public enum PropertyTypeEnum {
    HOUSE("House"),
    
    FLAT_APARTMENT("FlatApartment"),
    
    BUNGALOW("Bungalow"),
    
    LAND("Land"),
    
    HOUSE_FLAT_SHARE("HouseFlatShare"),
    
    GARAGE_PARKING("GarageParking"),
    
    COMMERCIAL_PROPERTY("CommercialProperty"),
    
    BLOCK("Block"),
    
    TERRACED_HOUSE("TerracedHouse"),
    
    END_TERRACE_HOUSE("EndTerraceHouse"),
    
    SEMI_DETACHED_HOUSE("SemiDetachedHouse"),
    
    DETACHED_HOUSE("DetachedHouse"),
    
    SEMI_DETACHED_BUNGALOW("SemiDetachedBungalow"),
    
    TOWN_HOUSE("TownHouse"),
    
    COTTAGE("Cottage"),
    
    SERVICED_APARTMENT("ServicedApartment"),
    
    STUDIO("Studio"),
    
    APARTMENT("Apartment"),
    
    BARN("Barn"),
    
    FARM_HOUSE("FarmHouse"),
    
    PENTHOUSE("Penthouse"),
    
    BUILDING_PLOT("BuildingPlot"),
    
    DETACHED_BUNGALOW("DetachedBungalow"),
    
    LINK_DETACHED("LinkDetached"),
    
    MID_TERRACED_BUNGALOW("MidTerracedBungalow"),
    
    LAND_RESIDENTIAL("LandResidential");

    private String value;

    PropertyTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PropertyTypeEnum fromValue(String value) {
      for (PropertyTypeEnum b : PropertyTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PropertyTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PropertyTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PropertyTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PropertyTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PropertyTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROPERTY_TYPE = "PropertyType";
  @SerializedName(SERIALIZED_NAME_PROPERTY_TYPE)
  private PropertyTypeEnum propertyType;

  public static final String SERIALIZED_NAME_ROOM_NAME = "RoomName";
  @SerializedName(SERIALIZED_NAME_ROOM_NAME)
  private String roomName;

  public static final String SERIALIZED_NAME_VIDEO_U_R_L = "VideoURL";
  @SerializedName(SERIALIZED_NAME_VIDEO_U_R_L)
  private String videoURL;

  public PropertyModel() {
  }

  public PropertyModel area(String area) {
    this.area = area;
    return this;
  }

  /**
   * The area the property is located in.
   * @return area
   */
  @javax.annotation.Nullable
  public String getArea() {
    return area;
  }

  public void setArea(String area) {
    this.area = area;
  }


  public PropertyModel branch(String branch) {
    this.branch = branch;
    return this;
  }

  /**
   * The branch the block, property or room is assigned to
   * @return branch
   */
  @javax.annotation.Nullable
  public String getBranch() {
    return branch;
  }

  public void setBranch(String branch) {
    this.branch = branch;
  }


  public PropertyModel description(String description) {
    this.description = description;
    return this;
  }

  /**
   * The block, property or room description.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public PropertyModel etag(String etag) {
    this.etag = etag;
    return this;
  }

  /**
   * A unique identifier defining the object and change revision.
   * @return etag
   */
  @javax.annotation.Nullable
  public String getEtag() {
    return etag;
  }

  public void setEtag(String etag) {
    this.etag = etag;
  }


  public PropertyModel fullAddress(String fullAddress) {
    this.fullAddress = fullAddress;
    return this;
  }

  /**
   * The full address of a block, property or room, formatted with line breaks such that it may be used on a letter directly.
   * @return fullAddress
   */
  @javax.annotation.Nullable
  public String getFullAddress() {
    return fullAddress;
  }

  public void setFullAddress(String fullAddress) {
    this.fullAddress = fullAddress;
  }


  public PropertyModel globalReference(String globalReference) {
    this.globalReference = globalReference;
    return this;
  }

  /**
   * The global reference to this block, property or room
   * @return globalReference
   */
  @javax.annotation.Nullable
  public String getGlobalReference() {
    return globalReference;
  }

  public void setGlobalReference(String globalReference) {
    this.globalReference = globalReference;
  }


  public PropertyModel mainPhoto(String mainPhoto) {
    this.mainPhoto = mainPhoto;
    return this;
  }

  /**
   * Gets the main photo, if there is one.
   * @return mainPhoto
   */
  @javax.annotation.Nullable
  public String getMainPhoto() {
    return mainPhoto;
  }

  public void setMainPhoto(String mainPhoto) {
    this.mainPhoto = mainPhoto;
  }


  public PropertyModel managedByStaff(String managedByStaff) {
    this.managedByStaff = managedByStaff;
    return this;
  }

  /**
   * The staff memeber that manages the block, property or room
   * @return managedByStaff
   */
  @javax.annotation.Nullable
  public String getManagedByStaff() {
    return managedByStaff;
  }

  public void setManagedByStaff(String managedByStaff) {
    this.managedByStaff = managedByStaff;
  }


  public PropertyModel OID(String OID) {
    this.OID = OID;
    return this;
  }

  /**
   * The unique Object ID (OID).
   * @return OID
   */
  @javax.annotation.Nullable
  public String getOID() {
    return OID;
  }

  public void setOID(String OID) {
    this.OID = OID;
  }


  public PropertyModel propertySource(String propertySource) {
    this.propertySource = propertySource;
    return this;
  }

  /**
   * The block, property or room source type
   * @return propertySource
   */
  @javax.annotation.Nullable
  public String getPropertySource() {
    return propertySource;
  }

  public void setPropertySource(String propertySource) {
    this.propertySource = propertySource;
  }


  public PropertyModel propertyType(PropertyTypeEnum propertyType) {
    this.propertyType = propertyType;
    return this;
  }

  /**
   * The block or property type.
   * @return propertyType
   */
  @javax.annotation.Nullable
  public PropertyTypeEnum getPropertyType() {
    return propertyType;
  }

  public void setPropertyType(PropertyTypeEnum propertyType) {
    this.propertyType = propertyType;
  }


  public PropertyModel roomName(String roomName) {
    this.roomName = roomName;
    return this;
  }

  /**
   * The room name (if applicable).
   * @return roomName
   */
  @javax.annotation.Nullable
  public String getRoomName() {
    return roomName;
  }

  public void setRoomName(String roomName) {
    this.roomName = roomName;
  }


  public PropertyModel videoURL(String videoURL) {
    this.videoURL = videoURL;
    return this;
  }

  /**
   * URL of the video linked to the property
   * @return videoURL
   */
  @javax.annotation.Nullable
  public String getVideoURL() {
    return videoURL;
  }

  public void setVideoURL(String videoURL) {
    this.videoURL = videoURL;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PropertyModel propertyModel = (PropertyModel) o;
    return Objects.equals(this.area, propertyModel.area) &&
        Objects.equals(this.branch, propertyModel.branch) &&
        Objects.equals(this.description, propertyModel.description) &&
        Objects.equals(this.etag, propertyModel.etag) &&
        Objects.equals(this.fullAddress, propertyModel.fullAddress) &&
        Objects.equals(this.globalReference, propertyModel.globalReference) &&
        Objects.equals(this.mainPhoto, propertyModel.mainPhoto) &&
        Objects.equals(this.managedByStaff, propertyModel.managedByStaff) &&
        Objects.equals(this.OID, propertyModel.OID) &&
        Objects.equals(this.propertySource, propertyModel.propertySource) &&
        Objects.equals(this.propertyType, propertyModel.propertyType) &&
        Objects.equals(this.roomName, propertyModel.roomName) &&
        Objects.equals(this.videoURL, propertyModel.videoURL);
  }

  @Override
  public int hashCode() {
    return Objects.hash(area, branch, description, etag, fullAddress, globalReference, mainPhoto, managedByStaff, OID, propertySource, propertyType, roomName, videoURL);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PropertyModel {\n");
    sb.append("    area: ").append(toIndentedString(area)).append("\n");
    sb.append("    branch: ").append(toIndentedString(branch)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    etag: ").append(toIndentedString(etag)).append("\n");
    sb.append("    fullAddress: ").append(toIndentedString(fullAddress)).append("\n");
    sb.append("    globalReference: ").append(toIndentedString(globalReference)).append("\n");
    sb.append("    mainPhoto: ").append(toIndentedString(mainPhoto)).append("\n");
    sb.append("    managedByStaff: ").append(toIndentedString(managedByStaff)).append("\n");
    sb.append("    OID: ").append(toIndentedString(OID)).append("\n");
    sb.append("    propertySource: ").append(toIndentedString(propertySource)).append("\n");
    sb.append("    propertyType: ").append(toIndentedString(propertyType)).append("\n");
    sb.append("    roomName: ").append(toIndentedString(roomName)).append("\n");
    sb.append("    videoURL: ").append(toIndentedString(videoURL)).append("\n");
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
    openapiFields.add("Area");
    openapiFields.add("Branch");
    openapiFields.add("Description");
    openapiFields.add("ETag");
    openapiFields.add("FullAddress");
    openapiFields.add("GlobalReference");
    openapiFields.add("MainPhoto");
    openapiFields.add("ManagedByStaff");
    openapiFields.add("OID");
    openapiFields.add("PropertySource");
    openapiFields.add("PropertyType");
    openapiFields.add("RoomName");
    openapiFields.add("VideoURL");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PropertyModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PropertyModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PropertyModel is not found in the empty JSON string", PropertyModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PropertyModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PropertyModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Area") != null && !jsonObj.get("Area").isJsonNull()) && !jsonObj.get("Area").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Area` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Area").toString()));
      }
      if ((jsonObj.get("Branch") != null && !jsonObj.get("Branch").isJsonNull()) && !jsonObj.get("Branch").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Branch` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Branch").toString()));
      }
      if ((jsonObj.get("Description") != null && !jsonObj.get("Description").isJsonNull()) && !jsonObj.get("Description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Description").toString()));
      }
      if ((jsonObj.get("ETag") != null && !jsonObj.get("ETag").isJsonNull()) && !jsonObj.get("ETag").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ETag` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ETag").toString()));
      }
      if ((jsonObj.get("FullAddress") != null && !jsonObj.get("FullAddress").isJsonNull()) && !jsonObj.get("FullAddress").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `FullAddress` to be a primitive type in the JSON string but got `%s`", jsonObj.get("FullAddress").toString()));
      }
      if ((jsonObj.get("GlobalReference") != null && !jsonObj.get("GlobalReference").isJsonNull()) && !jsonObj.get("GlobalReference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `GlobalReference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("GlobalReference").toString()));
      }
      if ((jsonObj.get("MainPhoto") != null && !jsonObj.get("MainPhoto").isJsonNull()) && !jsonObj.get("MainPhoto").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `MainPhoto` to be a primitive type in the JSON string but got `%s`", jsonObj.get("MainPhoto").toString()));
      }
      if ((jsonObj.get("ManagedByStaff") != null && !jsonObj.get("ManagedByStaff").isJsonNull()) && !jsonObj.get("ManagedByStaff").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ManagedByStaff` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ManagedByStaff").toString()));
      }
      if ((jsonObj.get("OID") != null && !jsonObj.get("OID").isJsonNull()) && !jsonObj.get("OID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `OID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("OID").toString()));
      }
      if ((jsonObj.get("PropertySource") != null && !jsonObj.get("PropertySource").isJsonNull()) && !jsonObj.get("PropertySource").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PropertySource` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PropertySource").toString()));
      }
      if ((jsonObj.get("PropertyType") != null && !jsonObj.get("PropertyType").isJsonNull()) && !jsonObj.get("PropertyType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PropertyType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PropertyType").toString()));
      }
      // validate the optional field `PropertyType`
      if (jsonObj.get("PropertyType") != null && !jsonObj.get("PropertyType").isJsonNull()) {
        PropertyTypeEnum.validateJsonElement(jsonObj.get("PropertyType"));
      }
      if ((jsonObj.get("RoomName") != null && !jsonObj.get("RoomName").isJsonNull()) && !jsonObj.get("RoomName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `RoomName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("RoomName").toString()));
      }
      if ((jsonObj.get("VideoURL") != null && !jsonObj.get("VideoURL").isJsonNull()) && !jsonObj.get("VideoURL").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `VideoURL` to be a primitive type in the JSON string but got `%s`", jsonObj.get("VideoURL").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PropertyModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PropertyModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PropertyModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PropertyModel.class));

       return (TypeAdapter<T>) new TypeAdapter<PropertyModel>() {
           @Override
           public void write(JsonWriter out, PropertyModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PropertyModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PropertyModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PropertyModel
   * @throws IOException if the JSON string is invalid with respect to PropertyModel
   */
  public static PropertyModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PropertyModel.class);
  }

  /**
   * Convert an instance of PropertyModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

