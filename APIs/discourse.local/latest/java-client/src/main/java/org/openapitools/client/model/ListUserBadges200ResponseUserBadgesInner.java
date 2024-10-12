/*
 * Discourse API Documentation
 * This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 
 *
 * The version of the OpenAPI document: latest
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
 * ListUserBadges200ResponseUserBadgesInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:34.324076-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ListUserBadges200ResponseUserBadgesInner {
  public static final String SERIALIZED_NAME_BADGE_ID = "badge_id";
  @SerializedName(SERIALIZED_NAME_BADGE_ID)
  private Integer badgeId;

  public static final String SERIALIZED_NAME_CAN_FAVORITE = "can_favorite";
  @SerializedName(SERIALIZED_NAME_CAN_FAVORITE)
  private Boolean canFavorite;

  public static final String SERIALIZED_NAME_GRANTED_AT = "granted_at";
  @SerializedName(SERIALIZED_NAME_GRANTED_AT)
  private String grantedAt;

  public static final String SERIALIZED_NAME_GRANTED_BY_ID = "granted_by_id";
  @SerializedName(SERIALIZED_NAME_GRANTED_BY_ID)
  private Integer grantedById;

  public static final String SERIALIZED_NAME_GROUPING_POSITION = "grouping_position";
  @SerializedName(SERIALIZED_NAME_GROUPING_POSITION)
  private Integer groupingPosition;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IS_FAVORITE = "is_favorite";
  @SerializedName(SERIALIZED_NAME_IS_FAVORITE)
  private String isFavorite;

  public ListUserBadges200ResponseUserBadgesInner() {
  }

  public ListUserBadges200ResponseUserBadgesInner badgeId(Integer badgeId) {
    this.badgeId = badgeId;
    return this;
  }

  /**
   * Get badgeId
   * @return badgeId
   */
  @javax.annotation.Nonnull
  public Integer getBadgeId() {
    return badgeId;
  }

  public void setBadgeId(Integer badgeId) {
    this.badgeId = badgeId;
  }


  public ListUserBadges200ResponseUserBadgesInner canFavorite(Boolean canFavorite) {
    this.canFavorite = canFavorite;
    return this;
  }

  /**
   * Get canFavorite
   * @return canFavorite
   */
  @javax.annotation.Nonnull
  public Boolean getCanFavorite() {
    return canFavorite;
  }

  public void setCanFavorite(Boolean canFavorite) {
    this.canFavorite = canFavorite;
  }


  public ListUserBadges200ResponseUserBadgesInner grantedAt(String grantedAt) {
    this.grantedAt = grantedAt;
    return this;
  }

  /**
   * Get grantedAt
   * @return grantedAt
   */
  @javax.annotation.Nonnull
  public String getGrantedAt() {
    return grantedAt;
  }

  public void setGrantedAt(String grantedAt) {
    this.grantedAt = grantedAt;
  }


  public ListUserBadges200ResponseUserBadgesInner grantedById(Integer grantedById) {
    this.grantedById = grantedById;
    return this;
  }

  /**
   * Get grantedById
   * @return grantedById
   */
  @javax.annotation.Nonnull
  public Integer getGrantedById() {
    return grantedById;
  }

  public void setGrantedById(Integer grantedById) {
    this.grantedById = grantedById;
  }


  public ListUserBadges200ResponseUserBadgesInner groupingPosition(Integer groupingPosition) {
    this.groupingPosition = groupingPosition;
    return this;
  }

  /**
   * Get groupingPosition
   * @return groupingPosition
   */
  @javax.annotation.Nonnull
  public Integer getGroupingPosition() {
    return groupingPosition;
  }

  public void setGroupingPosition(Integer groupingPosition) {
    this.groupingPosition = groupingPosition;
  }


  public ListUserBadges200ResponseUserBadgesInner id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public ListUserBadges200ResponseUserBadgesInner isFavorite(String isFavorite) {
    this.isFavorite = isFavorite;
    return this;
  }

  /**
   * Get isFavorite
   * @return isFavorite
   */
  @javax.annotation.Nullable
  public String getIsFavorite() {
    return isFavorite;
  }

  public void setIsFavorite(String isFavorite) {
    this.isFavorite = isFavorite;
  }

  /**
   * A container for additional, undeclared properties.
   * This is a holder for any undeclared properties as specified with
   * the 'additionalProperties' keyword in the OAS document.
   */
  private Map<String, Object> additionalProperties;

  /**
   * Set the additional (undeclared) property with the specified name and value.
   * If the property does not already exist, create it otherwise replace it.
   *
   * @param key name of the property
   * @param value value of the property
   * @return the ListUserBadges200ResponseUserBadgesInner instance itself
   */
  public ListUserBadges200ResponseUserBadgesInner putAdditionalProperty(String key, Object value) {
    if (this.additionalProperties == null) {
        this.additionalProperties = new HashMap<String, Object>();
    }
    this.additionalProperties.put(key, value);
    return this;
  }

  /**
   * Return the additional (undeclared) property.
   *
   * @return a map of objects
   */
  public Map<String, Object> getAdditionalProperties() {
    return additionalProperties;
  }

  /**
   * Return the additional (undeclared) property with the specified name.
   *
   * @param key name of the property
   * @return an object
   */
  public Object getAdditionalProperty(String key) {
    if (this.additionalProperties == null) {
        return null;
    }
    return this.additionalProperties.get(key);
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ListUserBadges200ResponseUserBadgesInner listUserBadges200ResponseUserBadgesInner = (ListUserBadges200ResponseUserBadgesInner) o;
    return Objects.equals(this.badgeId, listUserBadges200ResponseUserBadgesInner.badgeId) &&
        Objects.equals(this.canFavorite, listUserBadges200ResponseUserBadgesInner.canFavorite) &&
        Objects.equals(this.grantedAt, listUserBadges200ResponseUserBadgesInner.grantedAt) &&
        Objects.equals(this.grantedById, listUserBadges200ResponseUserBadgesInner.grantedById) &&
        Objects.equals(this.groupingPosition, listUserBadges200ResponseUserBadgesInner.groupingPosition) &&
        Objects.equals(this.id, listUserBadges200ResponseUserBadgesInner.id) &&
        Objects.equals(this.isFavorite, listUserBadges200ResponseUserBadgesInner.isFavorite)&&
        Objects.equals(this.additionalProperties, listUserBadges200ResponseUserBadgesInner.additionalProperties);
  }

  @Override
  public int hashCode() {
    return Objects.hash(badgeId, canFavorite, grantedAt, grantedById, groupingPosition, id, isFavorite, additionalProperties);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ListUserBadges200ResponseUserBadgesInner {\n");
    sb.append("    badgeId: ").append(toIndentedString(badgeId)).append("\n");
    sb.append("    canFavorite: ").append(toIndentedString(canFavorite)).append("\n");
    sb.append("    grantedAt: ").append(toIndentedString(grantedAt)).append("\n");
    sb.append("    grantedById: ").append(toIndentedString(grantedById)).append("\n");
    sb.append("    groupingPosition: ").append(toIndentedString(groupingPosition)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isFavorite: ").append(toIndentedString(isFavorite)).append("\n");
    sb.append("    additionalProperties: ").append(toIndentedString(additionalProperties)).append("\n");
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
    openapiFields.add("badge_id");
    openapiFields.add("can_favorite");
    openapiFields.add("granted_at");
    openapiFields.add("granted_by_id");
    openapiFields.add("grouping_position");
    openapiFields.add("id");
    openapiFields.add("is_favorite");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("badge_id");
    openapiRequiredFields.add("can_favorite");
    openapiRequiredFields.add("granted_at");
    openapiRequiredFields.add("granted_by_id");
    openapiRequiredFields.add("grouping_position");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("is_favorite");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ListUserBadges200ResponseUserBadgesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ListUserBadges200ResponseUserBadgesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ListUserBadges200ResponseUserBadgesInner is not found in the empty JSON string", ListUserBadges200ResponseUserBadgesInner.openapiRequiredFields.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ListUserBadges200ResponseUserBadgesInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("granted_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `granted_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("granted_at").toString()));
      }
      if ((jsonObj.get("is_favorite") != null && !jsonObj.get("is_favorite").isJsonNull()) && !jsonObj.get("is_favorite").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `is_favorite` to be a primitive type in the JSON string but got `%s`", jsonObj.get("is_favorite").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ListUserBadges200ResponseUserBadgesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ListUserBadges200ResponseUserBadgesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ListUserBadges200ResponseUserBadgesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ListUserBadges200ResponseUserBadgesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ListUserBadges200ResponseUserBadgesInner>() {
           @Override
           public void write(JsonWriter out, ListUserBadges200ResponseUserBadgesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             obj.remove("additionalProperties");
             // serialize additional properties
             if (value.getAdditionalProperties() != null) {
               for (Map.Entry<String, Object> entry : value.getAdditionalProperties().entrySet()) {
                 if (entry.getValue() instanceof String)
                   obj.addProperty(entry.getKey(), (String) entry.getValue());
                 else if (entry.getValue() instanceof Number)
                   obj.addProperty(entry.getKey(), (Number) entry.getValue());
                 else if (entry.getValue() instanceof Boolean)
                   obj.addProperty(entry.getKey(), (Boolean) entry.getValue());
                 else if (entry.getValue() instanceof Character)
                   obj.addProperty(entry.getKey(), (Character) entry.getValue());
                 else {
                   JsonElement jsonElement = gson.toJsonTree(entry.getValue());
                   if (jsonElement.isJsonArray()) {
                     obj.add(entry.getKey(), jsonElement.getAsJsonArray());
                   } else {
                     obj.add(entry.getKey(), jsonElement.getAsJsonObject());
                   }
                 }
               }
             }
             elementAdapter.write(out, obj);
           }

           @Override
           public ListUserBadges200ResponseUserBadgesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             JsonObject jsonObj = jsonElement.getAsJsonObject();
             // store additional fields in the deserialized instance
             ListUserBadges200ResponseUserBadgesInner instance = thisAdapter.fromJsonTree(jsonObj);
             for (Map.Entry<String, JsonElement> entry : jsonObj.entrySet()) {
               if (!openapiFields.contains(entry.getKey())) {
                 if (entry.getValue().isJsonPrimitive()) { // primitive type
                   if (entry.getValue().getAsJsonPrimitive().isString())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsString());
                   else if (entry.getValue().getAsJsonPrimitive().isNumber())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsNumber());
                   else if (entry.getValue().getAsJsonPrimitive().isBoolean())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsBoolean());
                   else
                     throw new IllegalArgumentException(String.format("The field `%s` has unknown primitive type. Value: %s", entry.getKey(), entry.getValue().toString()));
                 } else if (entry.getValue().isJsonArray()) {
                     instance.putAdditionalProperty(entry.getKey(), gson.fromJson(entry.getValue(), List.class));
                 } else { // JSON object
                     instance.putAdditionalProperty(entry.getKey(), gson.fromJson(entry.getValue(), HashMap.class));
                 }
               }
             }
             return instance;
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ListUserBadges200ResponseUserBadgesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ListUserBadges200ResponseUserBadgesInner
   * @throws IOException if the JSON string is invalid with respect to ListUserBadges200ResponseUserBadgesInner
   */
  public static ListUserBadges200ResponseUserBadgesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ListUserBadges200ResponseUserBadgesInner.class);
  }

  /**
   * Convert an instance of ListUserBadges200ResponseUserBadgesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

