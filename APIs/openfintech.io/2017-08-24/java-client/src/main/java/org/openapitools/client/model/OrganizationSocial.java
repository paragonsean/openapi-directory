/*
 * OpenFinTech.io
 * # Introduction [OpenFinTech.io](https://openfintech.io) is an open database that comprises of standardized primary data for FinTech industry.<br> It contains such information as geolocation data (countries, cities, regions), organizations, currencies (national, digital, virtual, crypto), banks, digital exchangers, payment providers (PSP), payment methods, etc.<br> It is created for communication of cross-integrated micro-services on \"one language\". This is achieved through standardization of entity identifiers that are used to exchange information among different services.<br>  ### UML UML Domain Model diagram you can find [here](https://api.openfintech.io/public_domain_model.png).<br>  ### Persistence Entities are updated not more than 1 time per day.<br>  ### Terms and Conditions This *OpenFinTech.io* is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/).<br> Any rights in individual contents of the database are licensed under the [Database Contents License](http://opendatacommons.org/licenses/dbcl/1.0/).<br>  ### Contacts For any questions, please email - info@openfintech.io<br> Or you can contact us at <a href=\"https://gitter.im/paymaxicom/openfintech.io\">Gitter</a><br>  Powered by [Paymaxi](https://www.paymaxi.com)  # Get Started  If you use [POSTMAN](https://www.getpostman.com) or similar program which can operate with swagger`s files - just [download](https://docs.openfintech.io) our spec and [import it](https://www.getpostman.com/docs/importing_swagger). Also you can try live [API demo](https://api.openfintech.io).  ## Overview  The OpenFinTech API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors.<br> API is based on [JSON API](http://jsonapi.org) standard. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.<br> JSON API requires use of the JSON API media type (`application/vnd.api+json`) for exchanging data.<br> ### Additional Request Headers #### ACCEPT HEADER Your requests should always include the header: ```curl Accept: application/vnd.api+json ```  ## Authentication  To use OpenFinTech API no needed authorization.  ## Versioning  When we make changes to the API, we release new, dated versions. The current version is **2017-08-24**. Read our [API upgrades guide]() to see our API changelog and to learn more about backwards compatibility.  ## Pagination  OpenFinTech APIs to retrieve lists of banks, currencies and other resources - paginated to **100** items by default. The pagination information will be included in the list API response under the node name `meta` - contains information about listed objects [`total` - contains information about total count of listed objects, `pages` - count of pages], `links` - contain links to navigate between pages [`first` - link to first page, `prev` - link to previous page, `next` - link to next page, `last` - link to last page].<br> By default first page will be listed. For navigating through pages, use the page parameter (e.g. `page[number]`, `page[size]`).<br> The `page[size]` parameter can be used to set the number of records that you want to receive in the response.<br> The `page[number]` parameter can be used to set needed page number.<br> Example of response: ```json {   \"meta\": {     \"total\": 419,     \"pages\": 42   },   \"links\": {     \"first\": \"/v1/{path}?page[number]=1&page[size]=10\",     \"prev\": \"/v1/{path}?page[number]=39&page[size]=10\",     \"next\": \"/v1/{path}?page[number]=41&page[size]=10\",     \"last\": \"/v1/{path}?page[number]=42&page[size]=10\"   } ```  ### Sorting  OpenFinTech\\`s API supported query parameter to sort result collection [e.g. `?sort=code`]. Information about available parameters may be found in the endpoint description. Positive parameter [e.g. `?sort=code`] points to ascending sorting, negative  [e.g. `?sort=-code`] - to descending sorting. Also, supported multiple sorting parameters [e.g. `?sort=code, -name, id`, etc.] ```curl https://api.openfintech.io/v1/countries?sort=name,-area ```  ### Filtering  Filtering provided by unique query key `filter[*filtering_condition*]`. Information about available parameters may be found in the endpoint description. ```curl https://api.openfintech.io/v1/countries?filter[region]=europe ```  ## Images  OpenFinTech provides two types of images: icons and logos. To get one of those types you should to use next url pattern: ``` curl https://api.openfintech.io/v1/{path}/{id}/{icon/logo} ``` Also, images can be resized by adding next parameters: `h={height}&w={width}`. For example, you want to get organization icon with width equals to 20 pixels: ``` curl https://api.openfintech.io/v1/organizations/{id}/icon?w=20&h=20 ``` If argument height or width is missing API returns original image with real sizes.  ## Errors  API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.), and codes in the `5xx` range indicate an error with OpenFinTech's servers (these are rare).  | Code | Description | |------|-------------| | 200 - OK | Everything worked as expected. | | 400 - Bad Request | The request was unacceptable, often due to missing a required parameter. | | 401 - Unauthorized | No valid API key provided. | | 402 - Request Failed | The parameters were valid but the request failed. | | 404 - Not Found | The requested resource doesn't exist. | | 409 - Conflict | The request conflicts with another request (perhaps due to using the same idempotent key). | | 429 - Too Many Requests | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. | | 500, 502, 503, 504 - Server Errors | Something went wrong on OpenFinTech's end. (These are rare.) | 
 *
 * The version of the OpenAPI document: 2017-08-24
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
 * Social profiles
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:28:06.060998-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrganizationSocial {
  public static final String SERIALIZED_NAME_FACEBOOK = "facebook";
  @SerializedName(SERIALIZED_NAME_FACEBOOK)
  private String facebook;

  public static final String SERIALIZED_NAME_GOOGLE_PLUS = "google_plus";
  @SerializedName(SERIALIZED_NAME_GOOGLE_PLUS)
  private String googlePlus;

  public static final String SERIALIZED_NAME_LINKED_IN = "linked_in";
  @SerializedName(SERIALIZED_NAME_LINKED_IN)
  private String linkedIn;

  public static final String SERIALIZED_NAME_TWITTER = "twitter";
  @SerializedName(SERIALIZED_NAME_TWITTER)
  private String twitter;

  public static final String SERIALIZED_NAME_VKONTAKTE = "vkontakte";
  @SerializedName(SERIALIZED_NAME_VKONTAKTE)
  private String vkontakte;

  public OrganizationSocial() {
  }

  public OrganizationSocial facebook(String facebook) {
    this.facebook = facebook;
    return this;
  }

  /**
   * Get facebook
   * @return facebook
   */
  @javax.annotation.Nullable
  public String getFacebook() {
    return facebook;
  }

  public void setFacebook(String facebook) {
    this.facebook = facebook;
  }


  public OrganizationSocial googlePlus(String googlePlus) {
    this.googlePlus = googlePlus;
    return this;
  }

  /**
   * Get googlePlus
   * @return googlePlus
   */
  @javax.annotation.Nullable
  public String getGooglePlus() {
    return googlePlus;
  }

  public void setGooglePlus(String googlePlus) {
    this.googlePlus = googlePlus;
  }


  public OrganizationSocial linkedIn(String linkedIn) {
    this.linkedIn = linkedIn;
    return this;
  }

  /**
   * Get linkedIn
   * @return linkedIn
   */
  @javax.annotation.Nullable
  public String getLinkedIn() {
    return linkedIn;
  }

  public void setLinkedIn(String linkedIn) {
    this.linkedIn = linkedIn;
  }


  public OrganizationSocial twitter(String twitter) {
    this.twitter = twitter;
    return this;
  }

  /**
   * Get twitter
   * @return twitter
   */
  @javax.annotation.Nullable
  public String getTwitter() {
    return twitter;
  }

  public void setTwitter(String twitter) {
    this.twitter = twitter;
  }


  public OrganizationSocial vkontakte(String vkontakte) {
    this.vkontakte = vkontakte;
    return this;
  }

  /**
   * Get vkontakte
   * @return vkontakte
   */
  @javax.annotation.Nullable
  public String getVkontakte() {
    return vkontakte;
  }

  public void setVkontakte(String vkontakte) {
    this.vkontakte = vkontakte;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrganizationSocial organizationSocial = (OrganizationSocial) o;
    return Objects.equals(this.facebook, organizationSocial.facebook) &&
        Objects.equals(this.googlePlus, organizationSocial.googlePlus) &&
        Objects.equals(this.linkedIn, organizationSocial.linkedIn) &&
        Objects.equals(this.twitter, organizationSocial.twitter) &&
        Objects.equals(this.vkontakte, organizationSocial.vkontakte);
  }

  @Override
  public int hashCode() {
    return Objects.hash(facebook, googlePlus, linkedIn, twitter, vkontakte);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrganizationSocial {\n");
    sb.append("    facebook: ").append(toIndentedString(facebook)).append("\n");
    sb.append("    googlePlus: ").append(toIndentedString(googlePlus)).append("\n");
    sb.append("    linkedIn: ").append(toIndentedString(linkedIn)).append("\n");
    sb.append("    twitter: ").append(toIndentedString(twitter)).append("\n");
    sb.append("    vkontakte: ").append(toIndentedString(vkontakte)).append("\n");
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
    openapiFields.add("facebook");
    openapiFields.add("google_plus");
    openapiFields.add("linked_in");
    openapiFields.add("twitter");
    openapiFields.add("vkontakte");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OrganizationSocial
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrganizationSocial.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrganizationSocial is not found in the empty JSON string", OrganizationSocial.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrganizationSocial.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrganizationSocial` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("facebook") != null && !jsonObj.get("facebook").isJsonNull()) && !jsonObj.get("facebook").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `facebook` to be a primitive type in the JSON string but got `%s`", jsonObj.get("facebook").toString()));
      }
      if ((jsonObj.get("google_plus") != null && !jsonObj.get("google_plus").isJsonNull()) && !jsonObj.get("google_plus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `google_plus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("google_plus").toString()));
      }
      if ((jsonObj.get("linked_in") != null && !jsonObj.get("linked_in").isJsonNull()) && !jsonObj.get("linked_in").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `linked_in` to be a primitive type in the JSON string but got `%s`", jsonObj.get("linked_in").toString()));
      }
      if ((jsonObj.get("twitter") != null && !jsonObj.get("twitter").isJsonNull()) && !jsonObj.get("twitter").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `twitter` to be a primitive type in the JSON string but got `%s`", jsonObj.get("twitter").toString()));
      }
      if ((jsonObj.get("vkontakte") != null && !jsonObj.get("vkontakte").isJsonNull()) && !jsonObj.get("vkontakte").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vkontakte` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vkontakte").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrganizationSocial.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrganizationSocial' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrganizationSocial> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrganizationSocial.class));

       return (TypeAdapter<T>) new TypeAdapter<OrganizationSocial>() {
           @Override
           public void write(JsonWriter out, OrganizationSocial value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrganizationSocial read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrganizationSocial given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrganizationSocial
   * @throws IOException if the JSON string is invalid with respect to OrganizationSocial
   */
  public static OrganizationSocial fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrganizationSocial.class);
  }

  /**
   * Convert an instance of OrganizationSocial to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

