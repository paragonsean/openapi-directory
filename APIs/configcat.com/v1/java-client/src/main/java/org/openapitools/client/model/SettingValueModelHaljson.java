/*
 * ConfigCat Public Management API
 * **Base API URL**: https://api.configcat.com  If you prefer the swagger documentation, you can find it here: [Swagger UI](https://api.configcat.com/swagger).  The purpose of this API is to access the ConfigCat platform programmatically.  You can **Create**, **Read**, **Update** and **Delete** any entities like **Feature Flags, Configs, Environments** or **Products** within ConfigCat.   The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON  and JSON+HAL format. Do not use this API for accessing and evaluating feature flag values. Use the [SDKs instead](https://configcat.com/docs/sdk-reference/overview).   # OpenAPI Specification  The complete specification is publicly available here: [swagger.json](v1/swagger.json).  You can use it to generate client libraries in various languages with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) or [Swagger Codegen](https://swagger.io/tools/swagger-codegen/) to interact with this API.  # Authentication This API uses the [Basic HTTP Authentication Scheme](https://en.wikipedia.org/wiki/Basic_access_authentication).   <!-- ReDoc-Inject: <security-definitions> -->  # Throttling and rate limits All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:  | Header | Description | | :- | :- | | X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. | | X-Rate-Limit-Reset     | The time when the current rate limit period resets.        |  When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header. 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@configcat.com
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
import org.openapitools.client.model.EnvironmentModelHaljsonLinks;
import org.openapitools.client.model.RolloutPercentageItemModel;
import org.openapitools.client.model.RolloutRuleModel;
import org.openapitools.client.model.SettingValueModelHaljsonEmbedded;
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
 * SettingValueModelHaljson
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:46.616681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SettingValueModelHaljson {
  public static final String SERIALIZED_NAME_EMBEDDED = "_embedded";
  @SerializedName(SERIALIZED_NAME_EMBEDDED)
  private SettingValueModelHaljsonEmbedded embedded;

  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private EnvironmentModelHaljsonLinks links;

  public static final String SERIALIZED_NAME_LAST_UPDATER_USER_EMAIL = "lastUpdaterUserEmail";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATER_USER_EMAIL)
  private String lastUpdaterUserEmail;

  public static final String SERIALIZED_NAME_LAST_UPDATER_USER_FULL_NAME = "lastUpdaterUserFullName";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATER_USER_FULL_NAME)
  private String lastUpdaterUserFullName;

  public static final String SERIALIZED_NAME_READ_ONLY = "readOnly";
  @SerializedName(SERIALIZED_NAME_READ_ONLY)
  private Boolean readOnly;

  public static final String SERIALIZED_NAME_ROLLOUT_PERCENTAGE_ITEMS = "rolloutPercentageItems";
  @SerializedName(SERIALIZED_NAME_ROLLOUT_PERCENTAGE_ITEMS)
  private List<RolloutPercentageItemModel> rolloutPercentageItems;

  public static final String SERIALIZED_NAME_ROLLOUT_RULES = "rolloutRules";
  @SerializedName(SERIALIZED_NAME_ROLLOUT_RULES)
  private List<RolloutRuleModel> rolloutRules;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private Object value = null;

  public SettingValueModelHaljson() {
  }

  public SettingValueModelHaljson embedded(SettingValueModelHaljsonEmbedded embedded) {
    this.embedded = embedded;
    return this;
  }

  /**
   * Get embedded
   * @return embedded
   */
  @javax.annotation.Nullable
  public SettingValueModelHaljsonEmbedded getEmbedded() {
    return embedded;
  }

  public void setEmbedded(SettingValueModelHaljsonEmbedded embedded) {
    this.embedded = embedded;
  }


  public SettingValueModelHaljson links(EnvironmentModelHaljsonLinks links) {
    this.links = links;
    return this;
  }

  /**
   * Get links
   * @return links
   */
  @javax.annotation.Nullable
  public EnvironmentModelHaljsonLinks getLinks() {
    return links;
  }

  public void setLinks(EnvironmentModelHaljsonLinks links) {
    this.links = links;
  }


  public SettingValueModelHaljson lastUpdaterUserEmail(String lastUpdaterUserEmail) {
    this.lastUpdaterUserEmail = lastUpdaterUserEmail;
    return this;
  }

  /**
   * Get lastUpdaterUserEmail
   * @return lastUpdaterUserEmail
   */
  @javax.annotation.Nullable
  public String getLastUpdaterUserEmail() {
    return lastUpdaterUserEmail;
  }

  public void setLastUpdaterUserEmail(String lastUpdaterUserEmail) {
    this.lastUpdaterUserEmail = lastUpdaterUserEmail;
  }


  public SettingValueModelHaljson lastUpdaterUserFullName(String lastUpdaterUserFullName) {
    this.lastUpdaterUserFullName = lastUpdaterUserFullName;
    return this;
  }

  /**
   * Get lastUpdaterUserFullName
   * @return lastUpdaterUserFullName
   */
  @javax.annotation.Nullable
  public String getLastUpdaterUserFullName() {
    return lastUpdaterUserFullName;
  }

  public void setLastUpdaterUserFullName(String lastUpdaterUserFullName) {
    this.lastUpdaterUserFullName = lastUpdaterUserFullName;
  }


  public SettingValueModelHaljson readOnly(Boolean readOnly) {
    this.readOnly = readOnly;
    return this;
  }

  /**
   * Get readOnly
   * @return readOnly
   */
  @javax.annotation.Nullable
  public Boolean getReadOnly() {
    return readOnly;
  }

  public void setReadOnly(Boolean readOnly) {
    this.readOnly = readOnly;
  }


  public SettingValueModelHaljson rolloutPercentageItems(List<RolloutPercentageItemModel> rolloutPercentageItems) {
    this.rolloutPercentageItems = rolloutPercentageItems;
    return this;
  }

  public SettingValueModelHaljson addRolloutPercentageItemsItem(RolloutPercentageItemModel rolloutPercentageItemsItem) {
    if (this.rolloutPercentageItems == null) {
      this.rolloutPercentageItems = new ArrayList<>();
    }
    this.rolloutPercentageItems.add(rolloutPercentageItemsItem);
    return this;
  }

  /**
   * The percentage rule collection.
   * @return rolloutPercentageItems
   */
  @javax.annotation.Nullable
  public List<RolloutPercentageItemModel> getRolloutPercentageItems() {
    return rolloutPercentageItems;
  }

  public void setRolloutPercentageItems(List<RolloutPercentageItemModel> rolloutPercentageItems) {
    this.rolloutPercentageItems = rolloutPercentageItems;
  }


  public SettingValueModelHaljson rolloutRules(List<RolloutRuleModel> rolloutRules) {
    this.rolloutRules = rolloutRules;
    return this;
  }

  public SettingValueModelHaljson addRolloutRulesItem(RolloutRuleModel rolloutRulesItem) {
    if (this.rolloutRules == null) {
      this.rolloutRules = new ArrayList<>();
    }
    this.rolloutRules.add(rolloutRulesItem);
    return this;
  }

  /**
   * The targeting rule collection.
   * @return rolloutRules
   */
  @javax.annotation.Nullable
  public List<RolloutRuleModel> getRolloutRules() {
    return rolloutRules;
  }

  public void setRolloutRules(List<RolloutRuleModel> rolloutRules) {
    this.rolloutRules = rolloutRules;
  }


  public SettingValueModelHaljson updatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * Get updatedAt
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
  }


  public SettingValueModelHaljson value(Object value) {
    this.value = value;
    return this;
  }

  /**
   * The value to serve. It must respect the setting type.
   * @return value
   */
  @javax.annotation.Nullable
  public Object getValue() {
    return value;
  }

  public void setValue(Object value) {
    this.value = value;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SettingValueModelHaljson settingValueModelHaljson = (SettingValueModelHaljson) o;
    return Objects.equals(this.embedded, settingValueModelHaljson.embedded) &&
        Objects.equals(this.links, settingValueModelHaljson.links) &&
        Objects.equals(this.lastUpdaterUserEmail, settingValueModelHaljson.lastUpdaterUserEmail) &&
        Objects.equals(this.lastUpdaterUserFullName, settingValueModelHaljson.lastUpdaterUserFullName) &&
        Objects.equals(this.readOnly, settingValueModelHaljson.readOnly) &&
        Objects.equals(this.rolloutPercentageItems, settingValueModelHaljson.rolloutPercentageItems) &&
        Objects.equals(this.rolloutRules, settingValueModelHaljson.rolloutRules) &&
        Objects.equals(this.updatedAt, settingValueModelHaljson.updatedAt) &&
        Objects.equals(this.value, settingValueModelHaljson.value);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(embedded, links, lastUpdaterUserEmail, lastUpdaterUserFullName, readOnly, rolloutPercentageItems, rolloutRules, updatedAt, value);
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
    sb.append("class SettingValueModelHaljson {\n");
    sb.append("    embedded: ").append(toIndentedString(embedded)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    lastUpdaterUserEmail: ").append(toIndentedString(lastUpdaterUserEmail)).append("\n");
    sb.append("    lastUpdaterUserFullName: ").append(toIndentedString(lastUpdaterUserFullName)).append("\n");
    sb.append("    readOnly: ").append(toIndentedString(readOnly)).append("\n");
    sb.append("    rolloutPercentageItems: ").append(toIndentedString(rolloutPercentageItems)).append("\n");
    sb.append("    rolloutRules: ").append(toIndentedString(rolloutRules)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
    openapiFields.add("_embedded");
    openapiFields.add("_links");
    openapiFields.add("lastUpdaterUserEmail");
    openapiFields.add("lastUpdaterUserFullName");
    openapiFields.add("readOnly");
    openapiFields.add("rolloutPercentageItems");
    openapiFields.add("rolloutRules");
    openapiFields.add("updatedAt");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SettingValueModelHaljson
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SettingValueModelHaljson.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SettingValueModelHaljson is not found in the empty JSON string", SettingValueModelHaljson.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SettingValueModelHaljson.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SettingValueModelHaljson` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `_embedded`
      if (jsonObj.get("_embedded") != null && !jsonObj.get("_embedded").isJsonNull()) {
        SettingValueModelHaljsonEmbedded.validateJsonElement(jsonObj.get("_embedded"));
      }
      // validate the optional field `_links`
      if (jsonObj.get("_links") != null && !jsonObj.get("_links").isJsonNull()) {
        EnvironmentModelHaljsonLinks.validateJsonElement(jsonObj.get("_links"));
      }
      if ((jsonObj.get("lastUpdaterUserEmail") != null && !jsonObj.get("lastUpdaterUserEmail").isJsonNull()) && !jsonObj.get("lastUpdaterUserEmail").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastUpdaterUserEmail` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastUpdaterUserEmail").toString()));
      }
      if ((jsonObj.get("lastUpdaterUserFullName") != null && !jsonObj.get("lastUpdaterUserFullName").isJsonNull()) && !jsonObj.get("lastUpdaterUserFullName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastUpdaterUserFullName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastUpdaterUserFullName").toString()));
      }
      if (jsonObj.get("rolloutPercentageItems") != null && !jsonObj.get("rolloutPercentageItems").isJsonNull()) {
        JsonArray jsonArrayrolloutPercentageItems = jsonObj.getAsJsonArray("rolloutPercentageItems");
        if (jsonArrayrolloutPercentageItems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("rolloutPercentageItems").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `rolloutPercentageItems` to be an array in the JSON string but got `%s`", jsonObj.get("rolloutPercentageItems").toString()));
          }

          // validate the optional field `rolloutPercentageItems` (array)
          for (int i = 0; i < jsonArrayrolloutPercentageItems.size(); i++) {
            RolloutPercentageItemModel.validateJsonElement(jsonArrayrolloutPercentageItems.get(i));
          };
        }
      }
      if (jsonObj.get("rolloutRules") != null && !jsonObj.get("rolloutRules").isJsonNull()) {
        JsonArray jsonArrayrolloutRules = jsonObj.getAsJsonArray("rolloutRules");
        if (jsonArrayrolloutRules != null) {
          // ensure the json data is an array
          if (!jsonObj.get("rolloutRules").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `rolloutRules` to be an array in the JSON string but got `%s`", jsonObj.get("rolloutRules").toString()));
          }

          // validate the optional field `rolloutRules` (array)
          for (int i = 0; i < jsonArrayrolloutRules.size(); i++) {
            RolloutRuleModel.validateJsonElement(jsonArrayrolloutRules.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SettingValueModelHaljson.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SettingValueModelHaljson' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SettingValueModelHaljson> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SettingValueModelHaljson.class));

       return (TypeAdapter<T>) new TypeAdapter<SettingValueModelHaljson>() {
           @Override
           public void write(JsonWriter out, SettingValueModelHaljson value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SettingValueModelHaljson read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SettingValueModelHaljson given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SettingValueModelHaljson
   * @throws IOException if the JSON string is invalid with respect to SettingValueModelHaljson
   */
  public static SettingValueModelHaljson fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SettingValueModelHaljson.class);
  }

  /**
   * Convert an instance of SettingValueModelHaljson to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

