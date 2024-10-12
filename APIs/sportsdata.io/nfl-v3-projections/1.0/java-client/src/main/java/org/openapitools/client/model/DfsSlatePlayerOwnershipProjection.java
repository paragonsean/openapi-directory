/*
 * NFL v3 Projections
 * NFL projected stats API.
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
import java.math.BigDecimal;
import java.util.Arrays;
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
 * DfsSlatePlayerOwnershipProjection
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:29.432938-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DfsSlatePlayerOwnershipProjection {
  public static final String SERIALIZED_NAME_FANTASY_DEFENSE_PLAYER_I_D = "FantasyDefensePlayerID";
  @SerializedName(SERIALIZED_NAME_FANTASY_DEFENSE_PLAYER_I_D)
  private Integer fantasyDefensePlayerID;

  public static final String SERIALIZED_NAME_IS_CAPTAIN = "IsCaptain";
  @SerializedName(SERIALIZED_NAME_IS_CAPTAIN)
  private Boolean isCaptain;

  public static final String SERIALIZED_NAME_PLAYER_I_D = "PlayerID";
  @SerializedName(SERIALIZED_NAME_PLAYER_I_D)
  private Integer playerID;

  public static final String SERIALIZED_NAME_PROJECTED_OWNERSHIP_PERCENTAGE = "ProjectedOwnershipPercentage";
  @SerializedName(SERIALIZED_NAME_PROJECTED_OWNERSHIP_PERCENTAGE)
  private BigDecimal projectedOwnershipPercentage;

  public static final String SERIALIZED_NAME_SLATE_I_D = "SlateID";
  @SerializedName(SERIALIZED_NAME_SLATE_I_D)
  private Integer slateID;

  public DfsSlatePlayerOwnershipProjection() {
  }

  public DfsSlatePlayerOwnershipProjection fantasyDefensePlayerID(Integer fantasyDefensePlayerID) {
    this.fantasyDefensePlayerID = fantasyDefensePlayerID;
    return this;
  }

  /**
   * Get fantasyDefensePlayerID
   * @return fantasyDefensePlayerID
   */
  @javax.annotation.Nullable
  public Integer getFantasyDefensePlayerID() {
    return fantasyDefensePlayerID;
  }

  public void setFantasyDefensePlayerID(Integer fantasyDefensePlayerID) {
    this.fantasyDefensePlayerID = fantasyDefensePlayerID;
  }


  public DfsSlatePlayerOwnershipProjection isCaptain(Boolean isCaptain) {
    this.isCaptain = isCaptain;
    return this;
  }

  /**
   * Get isCaptain
   * @return isCaptain
   */
  @javax.annotation.Nullable
  public Boolean getIsCaptain() {
    return isCaptain;
  }

  public void setIsCaptain(Boolean isCaptain) {
    this.isCaptain = isCaptain;
  }


  public DfsSlatePlayerOwnershipProjection playerID(Integer playerID) {
    this.playerID = playerID;
    return this;
  }

  /**
   * Get playerID
   * @return playerID
   */
  @javax.annotation.Nullable
  public Integer getPlayerID() {
    return playerID;
  }

  public void setPlayerID(Integer playerID) {
    this.playerID = playerID;
  }


  public DfsSlatePlayerOwnershipProjection projectedOwnershipPercentage(BigDecimal projectedOwnershipPercentage) {
    this.projectedOwnershipPercentage = projectedOwnershipPercentage;
    return this;
  }

  /**
   * Get projectedOwnershipPercentage
   * @return projectedOwnershipPercentage
   */
  @javax.annotation.Nullable
  public BigDecimal getProjectedOwnershipPercentage() {
    return projectedOwnershipPercentage;
  }

  public void setProjectedOwnershipPercentage(BigDecimal projectedOwnershipPercentage) {
    this.projectedOwnershipPercentage = projectedOwnershipPercentage;
  }


  public DfsSlatePlayerOwnershipProjection slateID(Integer slateID) {
    this.slateID = slateID;
    return this;
  }

  /**
   * Get slateID
   * @return slateID
   */
  @javax.annotation.Nullable
  public Integer getSlateID() {
    return slateID;
  }

  public void setSlateID(Integer slateID) {
    this.slateID = slateID;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DfsSlatePlayerOwnershipProjection dfsSlatePlayerOwnershipProjection = (DfsSlatePlayerOwnershipProjection) o;
    return Objects.equals(this.fantasyDefensePlayerID, dfsSlatePlayerOwnershipProjection.fantasyDefensePlayerID) &&
        Objects.equals(this.isCaptain, dfsSlatePlayerOwnershipProjection.isCaptain) &&
        Objects.equals(this.playerID, dfsSlatePlayerOwnershipProjection.playerID) &&
        Objects.equals(this.projectedOwnershipPercentage, dfsSlatePlayerOwnershipProjection.projectedOwnershipPercentage) &&
        Objects.equals(this.slateID, dfsSlatePlayerOwnershipProjection.slateID);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(fantasyDefensePlayerID, isCaptain, playerID, projectedOwnershipPercentage, slateID);
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
    sb.append("class DfsSlatePlayerOwnershipProjection {\n");
    sb.append("    fantasyDefensePlayerID: ").append(toIndentedString(fantasyDefensePlayerID)).append("\n");
    sb.append("    isCaptain: ").append(toIndentedString(isCaptain)).append("\n");
    sb.append("    playerID: ").append(toIndentedString(playerID)).append("\n");
    sb.append("    projectedOwnershipPercentage: ").append(toIndentedString(projectedOwnershipPercentage)).append("\n");
    sb.append("    slateID: ").append(toIndentedString(slateID)).append("\n");
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
    openapiFields.add("FantasyDefensePlayerID");
    openapiFields.add("IsCaptain");
    openapiFields.add("PlayerID");
    openapiFields.add("ProjectedOwnershipPercentage");
    openapiFields.add("SlateID");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DfsSlatePlayerOwnershipProjection
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DfsSlatePlayerOwnershipProjection.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DfsSlatePlayerOwnershipProjection is not found in the empty JSON string", DfsSlatePlayerOwnershipProjection.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DfsSlatePlayerOwnershipProjection.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DfsSlatePlayerOwnershipProjection` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DfsSlatePlayerOwnershipProjection.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DfsSlatePlayerOwnershipProjection' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DfsSlatePlayerOwnershipProjection> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DfsSlatePlayerOwnershipProjection.class));

       return (TypeAdapter<T>) new TypeAdapter<DfsSlatePlayerOwnershipProjection>() {
           @Override
           public void write(JsonWriter out, DfsSlatePlayerOwnershipProjection value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DfsSlatePlayerOwnershipProjection read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DfsSlatePlayerOwnershipProjection given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DfsSlatePlayerOwnershipProjection
   * @throws IOException if the JSON string is invalid with respect to DfsSlatePlayerOwnershipProjection
   */
  public static DfsSlatePlayerOwnershipProjection fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DfsSlatePlayerOwnershipProjection.class);
  }

  /**
   * Convert an instance of DfsSlatePlayerOwnershipProjection to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

