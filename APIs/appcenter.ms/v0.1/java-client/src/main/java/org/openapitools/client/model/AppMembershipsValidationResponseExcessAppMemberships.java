/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
import org.openapitools.client.model.AppMembershipsResponseMembershipsInner;

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
 * AppMembershipsValidationResponseExcessAppMemberships
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppMembershipsValidationResponseExcessAppMemberships {
  public static final String SERIALIZED_NAME_APP_USERS_MEMBERSHIPS = "app_users_memberships";
  @SerializedName(SERIALIZED_NAME_APP_USERS_MEMBERSHIPS)
  private List<AppMembershipsResponseMembershipsInner> appUsersMemberships = new ArrayList<>();

  public static final String SERIALIZED_NAME_DISTRIBUTION_GROUP_MEMBERSHIPS = "distribution_group_memberships";
  @SerializedName(SERIALIZED_NAME_DISTRIBUTION_GROUP_MEMBERSHIPS)
  private List<AppMembershipsResponseMembershipsInner> distributionGroupMemberships = new ArrayList<>();

  public static final String SERIALIZED_NAME_ORGANIZATION_ADMIN_MEMBERSHIPS = "organization_admin_memberships";
  @SerializedName(SERIALIZED_NAME_ORGANIZATION_ADMIN_MEMBERSHIPS)
  private List<AppMembershipsResponseMembershipsInner> organizationAdminMemberships = new ArrayList<>();

  public AppMembershipsValidationResponseExcessAppMemberships() {
  }

  public AppMembershipsValidationResponseExcessAppMemberships appUsersMemberships(List<AppMembershipsResponseMembershipsInner> appUsersMemberships) {
    this.appUsersMemberships = appUsersMemberships;
    return this;
  }

  public AppMembershipsValidationResponseExcessAppMemberships addAppUsersMembershipsItem(AppMembershipsResponseMembershipsInner appUsersMembershipsItem) {
    if (this.appUsersMemberships == null) {
      this.appUsersMemberships = new ArrayList<>();
    }
    this.appUsersMemberships.add(appUsersMembershipsItem);
    return this;
  }

  /**
   * Get appUsersMemberships
   * @return appUsersMemberships
   */
  @javax.annotation.Nullable
  public List<AppMembershipsResponseMembershipsInner> getAppUsersMemberships() {
    return appUsersMemberships;
  }

  public void setAppUsersMemberships(List<AppMembershipsResponseMembershipsInner> appUsersMemberships) {
    this.appUsersMemberships = appUsersMemberships;
  }


  public AppMembershipsValidationResponseExcessAppMemberships distributionGroupMemberships(List<AppMembershipsResponseMembershipsInner> distributionGroupMemberships) {
    this.distributionGroupMemberships = distributionGroupMemberships;
    return this;
  }

  public AppMembershipsValidationResponseExcessAppMemberships addDistributionGroupMembershipsItem(AppMembershipsResponseMembershipsInner distributionGroupMembershipsItem) {
    if (this.distributionGroupMemberships == null) {
      this.distributionGroupMemberships = new ArrayList<>();
    }
    this.distributionGroupMemberships.add(distributionGroupMembershipsItem);
    return this;
  }

  /**
   * Get distributionGroupMemberships
   * @return distributionGroupMemberships
   */
  @javax.annotation.Nullable
  public List<AppMembershipsResponseMembershipsInner> getDistributionGroupMemberships() {
    return distributionGroupMemberships;
  }

  public void setDistributionGroupMemberships(List<AppMembershipsResponseMembershipsInner> distributionGroupMemberships) {
    this.distributionGroupMemberships = distributionGroupMemberships;
  }


  public AppMembershipsValidationResponseExcessAppMemberships organizationAdminMemberships(List<AppMembershipsResponseMembershipsInner> organizationAdminMemberships) {
    this.organizationAdminMemberships = organizationAdminMemberships;
    return this;
  }

  public AppMembershipsValidationResponseExcessAppMemberships addOrganizationAdminMembershipsItem(AppMembershipsResponseMembershipsInner organizationAdminMembershipsItem) {
    if (this.organizationAdminMemberships == null) {
      this.organizationAdminMemberships = new ArrayList<>();
    }
    this.organizationAdminMemberships.add(organizationAdminMembershipsItem);
    return this;
  }

  /**
   * Get organizationAdminMemberships
   * @return organizationAdminMemberships
   */
  @javax.annotation.Nullable
  public List<AppMembershipsResponseMembershipsInner> getOrganizationAdminMemberships() {
    return organizationAdminMemberships;
  }

  public void setOrganizationAdminMemberships(List<AppMembershipsResponseMembershipsInner> organizationAdminMemberships) {
    this.organizationAdminMemberships = organizationAdminMemberships;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppMembershipsValidationResponseExcessAppMemberships appMembershipsValidationResponseExcessAppMemberships = (AppMembershipsValidationResponseExcessAppMemberships) o;
    return Objects.equals(this.appUsersMemberships, appMembershipsValidationResponseExcessAppMemberships.appUsersMemberships) &&
        Objects.equals(this.distributionGroupMemberships, appMembershipsValidationResponseExcessAppMemberships.distributionGroupMemberships) &&
        Objects.equals(this.organizationAdminMemberships, appMembershipsValidationResponseExcessAppMemberships.organizationAdminMemberships);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appUsersMemberships, distributionGroupMemberships, organizationAdminMemberships);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppMembershipsValidationResponseExcessAppMemberships {\n");
    sb.append("    appUsersMemberships: ").append(toIndentedString(appUsersMemberships)).append("\n");
    sb.append("    distributionGroupMemberships: ").append(toIndentedString(distributionGroupMemberships)).append("\n");
    sb.append("    organizationAdminMemberships: ").append(toIndentedString(organizationAdminMemberships)).append("\n");
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
    openapiFields.add("app_users_memberships");
    openapiFields.add("distribution_group_memberships");
    openapiFields.add("organization_admin_memberships");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppMembershipsValidationResponseExcessAppMemberships
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppMembershipsValidationResponseExcessAppMemberships.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppMembershipsValidationResponseExcessAppMemberships is not found in the empty JSON string", AppMembershipsValidationResponseExcessAppMemberships.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppMembershipsValidationResponseExcessAppMemberships.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppMembershipsValidationResponseExcessAppMemberships` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("app_users_memberships") != null && !jsonObj.get("app_users_memberships").isJsonNull()) {
        JsonArray jsonArrayappUsersMemberships = jsonObj.getAsJsonArray("app_users_memberships");
        if (jsonArrayappUsersMemberships != null) {
          // ensure the json data is an array
          if (!jsonObj.get("app_users_memberships").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `app_users_memberships` to be an array in the JSON string but got `%s`", jsonObj.get("app_users_memberships").toString()));
          }

          // validate the optional field `app_users_memberships` (array)
          for (int i = 0; i < jsonArrayappUsersMemberships.size(); i++) {
            AppMembershipsResponseMembershipsInner.validateJsonElement(jsonArrayappUsersMemberships.get(i));
          };
        }
      }
      if (jsonObj.get("distribution_group_memberships") != null && !jsonObj.get("distribution_group_memberships").isJsonNull()) {
        JsonArray jsonArraydistributionGroupMemberships = jsonObj.getAsJsonArray("distribution_group_memberships");
        if (jsonArraydistributionGroupMemberships != null) {
          // ensure the json data is an array
          if (!jsonObj.get("distribution_group_memberships").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `distribution_group_memberships` to be an array in the JSON string but got `%s`", jsonObj.get("distribution_group_memberships").toString()));
          }

          // validate the optional field `distribution_group_memberships` (array)
          for (int i = 0; i < jsonArraydistributionGroupMemberships.size(); i++) {
            AppMembershipsResponseMembershipsInner.validateJsonElement(jsonArraydistributionGroupMemberships.get(i));
          };
        }
      }
      if (jsonObj.get("organization_admin_memberships") != null && !jsonObj.get("organization_admin_memberships").isJsonNull()) {
        JsonArray jsonArrayorganizationAdminMemberships = jsonObj.getAsJsonArray("organization_admin_memberships");
        if (jsonArrayorganizationAdminMemberships != null) {
          // ensure the json data is an array
          if (!jsonObj.get("organization_admin_memberships").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `organization_admin_memberships` to be an array in the JSON string but got `%s`", jsonObj.get("organization_admin_memberships").toString()));
          }

          // validate the optional field `organization_admin_memberships` (array)
          for (int i = 0; i < jsonArrayorganizationAdminMemberships.size(); i++) {
            AppMembershipsResponseMembershipsInner.validateJsonElement(jsonArrayorganizationAdminMemberships.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppMembershipsValidationResponseExcessAppMemberships.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppMembershipsValidationResponseExcessAppMemberships' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppMembershipsValidationResponseExcessAppMemberships> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppMembershipsValidationResponseExcessAppMemberships.class));

       return (TypeAdapter<T>) new TypeAdapter<AppMembershipsValidationResponseExcessAppMemberships>() {
           @Override
           public void write(JsonWriter out, AppMembershipsValidationResponseExcessAppMemberships value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppMembershipsValidationResponseExcessAppMemberships read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppMembershipsValidationResponseExcessAppMemberships given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppMembershipsValidationResponseExcessAppMemberships
   * @throws IOException if the JSON string is invalid with respect to AppMembershipsValidationResponseExcessAppMemberships
   */
  public static AppMembershipsValidationResponseExcessAppMemberships fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppMembershipsValidationResponseExcessAppMemberships.class);
  }

  /**
   * Convert an instance of AppMembershipsValidationResponseExcessAppMemberships to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

