/*
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
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
import org.openapitools.client.model.Contact;

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
 * Request object for adding new contacts to an existing contact list
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:09.684594-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AddContactListContactsRequest {
  public static final String SERIALIZED_NAME_CONTACT_IDS = "contactIds";
  @SerializedName(SERIALIZED_NAME_CONTACT_IDS)
  private List<Long> contactIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_CONTACT_NUMBERS = "contactNumbers";
  @SerializedName(SERIALIZED_NAME_CONTACT_NUMBERS)
  private List<String> contactNumbers = new ArrayList<>();

  public static final String SERIALIZED_NAME_CONTACT_NUMBERS_FIELD = "contactNumbersField";
  @SerializedName(SERIALIZED_NAME_CONTACT_NUMBERS_FIELD)
  private String contactNumbersField;

  public static final String SERIALIZED_NAME_CONTACTS = "contacts";
  @SerializedName(SERIALIZED_NAME_CONTACTS)
  private List<Contact> contacts = new ArrayList<>();

  public static final String SERIALIZED_NAME_USE_CUSTOM_FIELDS = "useCustomFields";
  @SerializedName(SERIALIZED_NAME_USE_CUSTOM_FIELDS)
  private Boolean useCustomFields;

  public AddContactListContactsRequest() {
  }

  public AddContactListContactsRequest contactIds(List<Long> contactIds) {
    this.contactIds = contactIds;
    return this;
  }

  public AddContactListContactsRequest addContactIdsItem(Long contactIdsItem) {
    if (this.contactIds == null) {
      this.contactIds = new ArrayList<>();
    }
    this.contactIds.add(contactIdsItem);
    return this;
  }

  /**
   * A list of ids of existing contacts in CallFire system
   * @return contactIds
   */
  @javax.annotation.Nullable
  public List<Long> getContactIds() {
    return contactIds;
  }

  public void setContactIds(List<Long> contactIds) {
    this.contactIds = contactIds;
  }


  public AddContactListContactsRequest contactNumbers(List<String> contactNumbers) {
    this.contactNumbers = contactNumbers;
    return this;
  }

  public AddContactListContactsRequest addContactNumbersItem(String contactNumbersItem) {
    if (this.contactNumbers == null) {
      this.contactNumbers = new ArrayList<>();
    }
    this.contactNumbers.add(contactNumbersItem);
    return this;
  }

  /**
   * A phone number in E.164 format (11-digit). Examples: 12132000384
   * @return contactNumbers
   */
  @javax.annotation.Nullable
  public List<String> getContactNumbers() {
    return contactNumbers;
  }

  public void setContactNumbers(List<String> contactNumbers) {
    this.contactNumbers = contactNumbers;
  }


  public AddContactListContactsRequest contactNumbersField(String contactNumbersField) {
    this.contactNumbersField = contactNumbersField;
    return this;
  }

  /**
   * A type of phone number (homePhone, workPhone, mobilePhone). This parameter works together with contactNumbers and specifies which types of numbers are included to a list
   * @return contactNumbersField
   */
  @javax.annotation.Nullable
  public String getContactNumbersField() {
    return contactNumbersField;
  }

  public void setContactNumbersField(String contactNumbersField) {
    this.contactNumbersField = contactNumbersField;
  }


  public AddContactListContactsRequest contacts(List<Contact> contacts) {
    this.contacts = contacts;
    return this;
  }

  public AddContactListContactsRequest addContactsItem(Contact contactsItem) {
    if (this.contacts == null) {
      this.contacts = new ArrayList<>();
    }
    this.contacts.add(contactsItem);
    return this;
  }

  /**
   * A list of new contact objects which need to be added
   * @return contacts
   */
  @javax.annotation.Nullable
  public List<Contact> getContacts() {
    return contacts;
  }

  public void setContacts(List<Contact> contacts) {
    this.contacts = contacts;
  }


  public AddContactListContactsRequest useCustomFields(Boolean useCustomFields) {
    this.useCustomFields = useCustomFields;
    return this;
  }

  /**
   * A flag to indicate how to define property names for contacts. If true, uses the field and property names exactly as defined. If false will assign custom properties and fields to A, B, C, etc
   * @return useCustomFields
   */
  @javax.annotation.Nullable
  public Boolean getUseCustomFields() {
    return useCustomFields;
  }

  public void setUseCustomFields(Boolean useCustomFields) {
    this.useCustomFields = useCustomFields;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddContactListContactsRequest addContactListContactsRequest = (AddContactListContactsRequest) o;
    return Objects.equals(this.contactIds, addContactListContactsRequest.contactIds) &&
        Objects.equals(this.contactNumbers, addContactListContactsRequest.contactNumbers) &&
        Objects.equals(this.contactNumbersField, addContactListContactsRequest.contactNumbersField) &&
        Objects.equals(this.contacts, addContactListContactsRequest.contacts) &&
        Objects.equals(this.useCustomFields, addContactListContactsRequest.useCustomFields);
  }

  @Override
  public int hashCode() {
    return Objects.hash(contactIds, contactNumbers, contactNumbersField, contacts, useCustomFields);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AddContactListContactsRequest {\n");
    sb.append("    contactIds: ").append(toIndentedString(contactIds)).append("\n");
    sb.append("    contactNumbers: ").append(toIndentedString(contactNumbers)).append("\n");
    sb.append("    contactNumbersField: ").append(toIndentedString(contactNumbersField)).append("\n");
    sb.append("    contacts: ").append(toIndentedString(contacts)).append("\n");
    sb.append("    useCustomFields: ").append(toIndentedString(useCustomFields)).append("\n");
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
    openapiFields.add("contactIds");
    openapiFields.add("contactNumbers");
    openapiFields.add("contactNumbersField");
    openapiFields.add("contacts");
    openapiFields.add("useCustomFields");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AddContactListContactsRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AddContactListContactsRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AddContactListContactsRequest is not found in the empty JSON string", AddContactListContactsRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AddContactListContactsRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AddContactListContactsRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("contactIds") != null && !jsonObj.get("contactIds").isJsonNull() && !jsonObj.get("contactIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `contactIds` to be an array in the JSON string but got `%s`", jsonObj.get("contactIds").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("contactNumbers") != null && !jsonObj.get("contactNumbers").isJsonNull() && !jsonObj.get("contactNumbers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `contactNumbers` to be an array in the JSON string but got `%s`", jsonObj.get("contactNumbers").toString()));
      }
      if ((jsonObj.get("contactNumbersField") != null && !jsonObj.get("contactNumbersField").isJsonNull()) && !jsonObj.get("contactNumbersField").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contactNumbersField` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contactNumbersField").toString()));
      }
      if (jsonObj.get("contacts") != null && !jsonObj.get("contacts").isJsonNull()) {
        JsonArray jsonArraycontacts = jsonObj.getAsJsonArray("contacts");
        if (jsonArraycontacts != null) {
          // ensure the json data is an array
          if (!jsonObj.get("contacts").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `contacts` to be an array in the JSON string but got `%s`", jsonObj.get("contacts").toString()));
          }

          // validate the optional field `contacts` (array)
          for (int i = 0; i < jsonArraycontacts.size(); i++) {
            Contact.validateJsonElement(jsonArraycontacts.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AddContactListContactsRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AddContactListContactsRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AddContactListContactsRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AddContactListContactsRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<AddContactListContactsRequest>() {
           @Override
           public void write(JsonWriter out, AddContactListContactsRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AddContactListContactsRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AddContactListContactsRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AddContactListContactsRequest
   * @throws IOException if the JSON string is invalid with respect to AddContactListContactsRequest
   */
  public static AddContactListContactsRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AddContactListContactsRequest.class);
  }

  /**
   * Convert an instance of AddContactListContactsRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

