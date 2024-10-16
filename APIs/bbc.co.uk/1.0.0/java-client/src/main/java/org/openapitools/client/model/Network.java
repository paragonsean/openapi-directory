/*
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
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
import org.openapitools.client.model.CategorySummary;
import org.openapitools.client.model.Contact;
import org.openapitools.client.model.DateRange;
import org.openapitools.client.model.Service;

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
 * Network
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:46.845451-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Network {
  public static final String SERIALIZED_NAME_ACTIVE = "active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private Boolean active;

  public static final String SERIALIZED_NAME_CONTACTS = "contacts";
  @SerializedName(SERIALIZED_NAME_CONTACTS)
  private List<Contact> contacts = new ArrayList<>();

  public static final String SERIALIZED_NAME_DATE_RANGES = "date_ranges";
  @SerializedName(SERIALIZED_NAME_DATE_RANGES)
  private List<DateRange> dateRanges = new ArrayList<>();

  public static final String SERIALIZED_NAME_GROUP = "group";
  @SerializedName(SERIALIZED_NAME_GROUP)
  private String group;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INTERNATIONAL = "international";
  @SerializedName(SERIALIZED_NAME_INTERNATIONAL)
  private Boolean international;

  public static final String SERIALIZED_NAME_KEY = "key";
  @SerializedName(SERIALIZED_NAME_KEY)
  private String key;

  public static final String SERIALIZED_NAME_PRESET = "preset";
  @SerializedName(SERIALIZED_NAME_PRESET)
  private Boolean preset;

  public static final String SERIALIZED_NAME_PROMOTED_CATEGORY_SUMMARIES = "promoted_category_summaries";
  @SerializedName(SERIALIZED_NAME_PROMOTED_CATEGORY_SUMMARIES)
  private List<CategorySummary> promotedCategorySummaries = new ArrayList<>();

  public static final String SERIALIZED_NAME_SERVICES = "services";
  @SerializedName(SERIALIZED_NAME_SERVICES)
  private List<Service> services = new ArrayList<>();

  public static final String SERIALIZED_NAME_SHORT_TITLE = "short_title";
  @SerializedName(SERIALIZED_NAME_SHORT_TITLE)
  private String shortTitle;

  public static final String SERIALIZED_NAME_SORT = "sort";
  @SerializedName(SERIALIZED_NAME_SORT)
  private Integer sort;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public Network() {
  }

  public Network active(Boolean active) {
    this.active = active;
    return this;
  }

  /**
   * Get active
   * @return active
   */
  @javax.annotation.Nonnull
  public Boolean getActive() {
    return active;
  }

  public void setActive(Boolean active) {
    this.active = active;
  }


  public Network contacts(List<Contact> contacts) {
    this.contacts = contacts;
    return this;
  }

  public Network addContactsItem(Contact contactsItem) {
    if (this.contacts == null) {
      this.contacts = new ArrayList<>();
    }
    this.contacts.add(contactsItem);
    return this;
  }

  /**
   * Get contacts
   * @return contacts
   */
  @javax.annotation.Nonnull
  public List<Contact> getContacts() {
    return contacts;
  }

  public void setContacts(List<Contact> contacts) {
    this.contacts = contacts;
  }


  public Network dateRanges(List<DateRange> dateRanges) {
    this.dateRanges = dateRanges;
    return this;
  }

  public Network addDateRangesItem(DateRange dateRangesItem) {
    if (this.dateRanges == null) {
      this.dateRanges = new ArrayList<>();
    }
    this.dateRanges.add(dateRangesItem);
    return this;
  }

  /**
   * Get dateRanges
   * @return dateRanges
   */
  @javax.annotation.Nonnull
  public List<DateRange> getDateRanges() {
    return dateRanges;
  }

  public void setDateRanges(List<DateRange> dateRanges) {
    this.dateRanges = dateRanges;
  }


  public Network group(String group) {
    this.group = group;
    return this;
  }

  /**
   * Get group
   * @return group
   */
  @javax.annotation.Nonnull
  public String getGroup() {
    return group;
  }

  public void setGroup(String group) {
    this.group = group;
  }


  public Network id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public Network international(Boolean international) {
    this.international = international;
    return this;
  }

  /**
   * Get international
   * @return international
   */
  @javax.annotation.Nonnull
  public Boolean getInternational() {
    return international;
  }

  public void setInternational(Boolean international) {
    this.international = international;
  }


  public Network key(String key) {
    this.key = key;
    return this;
  }

  /**
   * Get key
   * @return key
   */
  @javax.annotation.Nonnull
  public String getKey() {
    return key;
  }

  public void setKey(String key) {
    this.key = key;
  }


  public Network preset(Boolean preset) {
    this.preset = preset;
    return this;
  }

  /**
   * Get preset
   * @return preset
   */
  @javax.annotation.Nonnull
  public Boolean getPreset() {
    return preset;
  }

  public void setPreset(Boolean preset) {
    this.preset = preset;
  }


  public Network promotedCategorySummaries(List<CategorySummary> promotedCategorySummaries) {
    this.promotedCategorySummaries = promotedCategorySummaries;
    return this;
  }

  public Network addPromotedCategorySummariesItem(CategorySummary promotedCategorySummariesItem) {
    if (this.promotedCategorySummaries == null) {
      this.promotedCategorySummaries = new ArrayList<>();
    }
    this.promotedCategorySummaries.add(promotedCategorySummariesItem);
    return this;
  }

  /**
   * Get promotedCategorySummaries
   * @return promotedCategorySummaries
   */
  @javax.annotation.Nullable
  public List<CategorySummary> getPromotedCategorySummaries() {
    return promotedCategorySummaries;
  }

  public void setPromotedCategorySummaries(List<CategorySummary> promotedCategorySummaries) {
    this.promotedCategorySummaries = promotedCategorySummaries;
  }


  public Network services(List<Service> services) {
    this.services = services;
    return this;
  }

  public Network addServicesItem(Service servicesItem) {
    if (this.services == null) {
      this.services = new ArrayList<>();
    }
    this.services.add(servicesItem);
    return this;
  }

  /**
   * Get services
   * @return services
   */
  @javax.annotation.Nonnull
  public List<Service> getServices() {
    return services;
  }

  public void setServices(List<Service> services) {
    this.services = services;
  }


  public Network shortTitle(String shortTitle) {
    this.shortTitle = shortTitle;
    return this;
  }

  /**
   * Get shortTitle
   * @return shortTitle
   */
  @javax.annotation.Nonnull
  public String getShortTitle() {
    return shortTitle;
  }

  public void setShortTitle(String shortTitle) {
    this.shortTitle = shortTitle;
  }


  public Network sort(Integer sort) {
    this.sort = sort;
    return this;
  }

  /**
   * Get sort
   * @return sort
   */
  @javax.annotation.Nonnull
  public Integer getSort() {
    return sort;
  }

  public void setSort(Integer sort) {
    this.sort = sort;
  }


  public Network title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nonnull
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public Network type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nonnull
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Network network = (Network) o;
    return Objects.equals(this.active, network.active) &&
        Objects.equals(this.contacts, network.contacts) &&
        Objects.equals(this.dateRanges, network.dateRanges) &&
        Objects.equals(this.group, network.group) &&
        Objects.equals(this.id, network.id) &&
        Objects.equals(this.international, network.international) &&
        Objects.equals(this.key, network.key) &&
        Objects.equals(this.preset, network.preset) &&
        Objects.equals(this.promotedCategorySummaries, network.promotedCategorySummaries) &&
        Objects.equals(this.services, network.services) &&
        Objects.equals(this.shortTitle, network.shortTitle) &&
        Objects.equals(this.sort, network.sort) &&
        Objects.equals(this.title, network.title) &&
        Objects.equals(this.type, network.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, contacts, dateRanges, group, id, international, key, preset, promotedCategorySummaries, services, shortTitle, sort, title, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Network {\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    contacts: ").append(toIndentedString(contacts)).append("\n");
    sb.append("    dateRanges: ").append(toIndentedString(dateRanges)).append("\n");
    sb.append("    group: ").append(toIndentedString(group)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    international: ").append(toIndentedString(international)).append("\n");
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    preset: ").append(toIndentedString(preset)).append("\n");
    sb.append("    promotedCategorySummaries: ").append(toIndentedString(promotedCategorySummaries)).append("\n");
    sb.append("    services: ").append(toIndentedString(services)).append("\n");
    sb.append("    shortTitle: ").append(toIndentedString(shortTitle)).append("\n");
    sb.append("    sort: ").append(toIndentedString(sort)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("active");
    openapiFields.add("contacts");
    openapiFields.add("date_ranges");
    openapiFields.add("group");
    openapiFields.add("id");
    openapiFields.add("international");
    openapiFields.add("key");
    openapiFields.add("preset");
    openapiFields.add("promoted_category_summaries");
    openapiFields.add("services");
    openapiFields.add("short_title");
    openapiFields.add("sort");
    openapiFields.add("title");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("active");
    openapiRequiredFields.add("contacts");
    openapiRequiredFields.add("date_ranges");
    openapiRequiredFields.add("group");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("international");
    openapiRequiredFields.add("key");
    openapiRequiredFields.add("preset");
    openapiRequiredFields.add("services");
    openapiRequiredFields.add("short_title");
    openapiRequiredFields.add("sort");
    openapiRequiredFields.add("title");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Network
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Network.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Network is not found in the empty JSON string", Network.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Network.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Network` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Network.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("contacts").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `contacts` to be an array in the JSON string but got `%s`", jsonObj.get("contacts").toString()));
      }

      JsonArray jsonArraycontacts = jsonObj.getAsJsonArray("contacts");
      // validate the required field `contacts` (array)
      for (int i = 0; i < jsonArraycontacts.size(); i++) {
        Contact.validateJsonElement(jsonArraycontacts.get(i));
      };
      // ensure the json data is an array
      if (!jsonObj.get("date_ranges").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `date_ranges` to be an array in the JSON string but got `%s`", jsonObj.get("date_ranges").toString()));
      }

      JsonArray jsonArraydateRanges = jsonObj.getAsJsonArray("date_ranges");
      // validate the required field `date_ranges` (array)
      for (int i = 0; i < jsonArraydateRanges.size(); i++) {
        DateRange.validateJsonElement(jsonArraydateRanges.get(i));
      };
      if (!jsonObj.get("group").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `group` to be a primitive type in the JSON string but got `%s`", jsonObj.get("group").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("key").toString()));
      }
      if (jsonObj.get("promoted_category_summaries") != null && !jsonObj.get("promoted_category_summaries").isJsonNull()) {
        JsonArray jsonArraypromotedCategorySummaries = jsonObj.getAsJsonArray("promoted_category_summaries");
        if (jsonArraypromotedCategorySummaries != null) {
          // ensure the json data is an array
          if (!jsonObj.get("promoted_category_summaries").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `promoted_category_summaries` to be an array in the JSON string but got `%s`", jsonObj.get("promoted_category_summaries").toString()));
          }

          // validate the optional field `promoted_category_summaries` (array)
          for (int i = 0; i < jsonArraypromotedCategorySummaries.size(); i++) {
            CategorySummary.validateJsonElement(jsonArraypromotedCategorySummaries.get(i));
          };
        }
      }
      // ensure the json data is an array
      if (!jsonObj.get("services").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `services` to be an array in the JSON string but got `%s`", jsonObj.get("services").toString()));
      }

      JsonArray jsonArrayservices = jsonObj.getAsJsonArray("services");
      // validate the required field `services` (array)
      for (int i = 0; i < jsonArrayservices.size(); i++) {
        Service.validateJsonElement(jsonArrayservices.get(i));
      };
      if (!jsonObj.get("short_title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `short_title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("short_title").toString()));
      }
      if (!jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Network.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Network' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Network> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Network.class));

       return (TypeAdapter<T>) new TypeAdapter<Network>() {
           @Override
           public void write(JsonWriter out, Network value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Network read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Network given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Network
   * @throws IOException if the JSON string is invalid with respect to Network
   */
  public static Network fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Network.class);
  }

  /**
   * Convert an instance of Network to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

