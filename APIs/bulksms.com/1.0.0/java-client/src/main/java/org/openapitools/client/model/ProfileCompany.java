/*
 * BulkSMS JSON REST API
 * ## Overview  The JSON REST API allows you to submit and receive [BulkSMS](https://www.bulksms.com/) messages. You can also get access to past messages and see your account profile.  The base URL to use for this service is `https://api.bulksms.com/v1`.  The base URL cannot be used on its own; you must append a path that identifies an operation and you may have to specify some path parameters as well.  [Click here](/developer/) to go to the main BulkSMS developer site.  In order to give you an idea on how the API can be used, some JSON snippets are provided below.  Have a look at the [messages section](#tag/Message) for more information.  Probably the most simple example  ``` {     \"to\": \"+27001234567\",     \"body\": \"Hello World!\" } ```   You can send unicode automatically using the `auto-unicode` query parameter.  Alternatively, you can specify `UNICODE` for the `encoding` property in the request body.  Please note: when `auto-unicode` is specified and the value of the `encoding` property is `UNICODE`, the message will always be sent as `UNICODE`.  Here is an example that sets the `encoding` explicitly  ``` {   \"to\": \"+27001234567\",   \"body\": \"Dobrá práce! Jak se máš?\",   \"encoding\": \"UNICODE\" } ```  You can also specify a from number  ``` {     \"from\": \"+27007654321\",     \"to\": \"+27001234567\",     \"body\": \"Hello World!\" } ```  Similar to above, but repliable  ``` {     \"from\": { \"type\": \"REPLIABLE\" },     \"to\": \"+27001234567\",     \"body\": \"Hello World!\" } ```  A message to a group called Everyone  ``` {     \"to\": { \"type\": \"GROUP\", \"name\": \"Everyone\" },     \"body\": \"Hello World!\" } ```  A message to multiple recipients  ``` {     \"to\": [\"+27001234567\", \"+27002345678\", \"+27003456789\"],     \"body\": \"Happy Holidays!\" } ```  Sending more than one message in the same request  ``` [     {         \"to\": \"+27001234567\",         \"body\": \"Hello World!\"     },     {         \"to\": \"+27002345678\",         \"body\": \"Hello Universe!\"     } ] ```  **The insecure base URL `http://api.bulksms.com/v1` is deprecated** and may in future result in a `301` redirect response, or insecure requests may be rejected outright. Please use the secure (`https`) URI above.  ### HTTP Content Type  All API methods expect requests to supply a `Content-Type` header with the value `application/json`. All responses will have the `Content-Type` header set to `application/json`.  ### JSON Formatting  You are advised to format your JSON resources according to strict JSON format rules. While the API does attempt to parse strictly invalid JSON documents, doing so may lead to incorrect interpretation and unexpected results.  Good JSON libraries will produce valid JSON suitable for submission, but if you are manually generating the JSON text, be careful to follow the JSON format. This include correct escaping of control characters and double quoting of property names.  See the [JSON specification](https://tools.ietf.org/html/rfc4627) for further information.  ### Date Formatting  Dates are formatted according to ISO-8601, such as `1970-01-01T10:00:00+01:00` for 1st January 1970, 10AM UTC+1.  See the [Wikipedia ISO 8601 reference](https://en.wikipedia.org/wiki/ISO_8601) for further information.  Specifically, calendar dates are formatted with the 'extended' format `YYYY-MM-DD`. Basic format, week dates and ordinal dates are not supported. Times are also formatted in the 'extended' format `hh:mm:ss`. Hours, minutes and seconds are mandatory. Offset from UTC must be provided; this is to ensure that there is no misunderstanding regarding times provided to the API.  The format we look for is `yyyy-MM-ddThh:mm:ss[Z|[+-]hh:mm]`  Examples of valid date/times are`2011-12-31T12:00:00Z` `2011-12-31T12:00:00+02:00`  ### Entity Format Modifications  It is expected that over time some changes will be made to the request and response formats of various methods available in the API. Where possible, these will be implemented in a backwards compatible way. To make this possible you are required to ignore unknown properties. This enables the addition of information in response documents while maintaining compatibility with older clients.  ### Optional Request Entity Properties  There are many instances where requests can be made without having to specify every single property allowable in the request format. Any such optional properties are noted as such in the documentation and their default value is noted. 
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
 * ProfileCompany
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:01.416061-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProfileCompany {
  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_TAX_REFERENCE = "taxReference";
  @SerializedName(SERIALIZED_NAME_TAX_REFERENCE)
  private String taxReference;

  public ProfileCompany() {
  }

  public ProfileCompany name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ProfileCompany taxReference(String taxReference) {
    this.taxReference = taxReference;
    return this;
  }

  /**
   * Get taxReference
   * @return taxReference
   */
  @javax.annotation.Nullable
  public String getTaxReference() {
    return taxReference;
  }

  public void setTaxReference(String taxReference) {
    this.taxReference = taxReference;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProfileCompany profileCompany = (ProfileCompany) o;
    return Objects.equals(this.name, profileCompany.name) &&
        Objects.equals(this.taxReference, profileCompany.taxReference);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, taxReference);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProfileCompany {\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    taxReference: ").append(toIndentedString(taxReference)).append("\n");
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
    openapiFields.add("name");
    openapiFields.add("taxReference");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProfileCompany
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProfileCompany.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProfileCompany is not found in the empty JSON string", ProfileCompany.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProfileCompany.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProfileCompany` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("taxReference") != null && !jsonObj.get("taxReference").isJsonNull()) && !jsonObj.get("taxReference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `taxReference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("taxReference").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProfileCompany.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProfileCompany' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProfileCompany> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProfileCompany.class));

       return (TypeAdapter<T>) new TypeAdapter<ProfileCompany>() {
           @Override
           public void write(JsonWriter out, ProfileCompany value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProfileCompany read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProfileCompany given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProfileCompany
   * @throws IOException if the JSON string is invalid with respect to ProfileCompany
   */
  public static ProfileCompany fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProfileCompany.class);
  }

  /**
   * Convert an instance of ProfileCompany to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

