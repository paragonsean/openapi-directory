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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.OrganizationAddress;
import org.openapitools.client.model.OrganizationAttributesIcon;
import org.openapitools.client.model.OrganizationAttributesLogo;
import org.openapitools.client.model.OrganizationContacts;
import org.openapitools.client.model.OrganizationSocial;

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
 * OrganizationAttributes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:28:06.060998-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrganizationAttributes {
  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private OrganizationAddress address;

  public static final String SERIALIZED_NAME_BLOG = "blog";
  @SerializedName(SERIALIZED_NAME_BLOG)
  private String blog;

  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_CONTACTS = "contacts";
  @SerializedName(SERIALIZED_NAME_CONTACTS)
  private OrganizationContacts contacts;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ICON = "icon";
  @SerializedName(SERIALIZED_NAME_ICON)
  private OrganizationAttributesIcon icon;

  public static final String SERIALIZED_NAME_INDUSTRIES = "industries";
  @SerializedName(SERIALIZED_NAME_INDUSTRIES)
  private List<String> industries = new ArrayList<>();

  public static final String SERIALIZED_NAME_LOGO = "logo";
  @SerializedName(SERIALIZED_NAME_LOGO)
  private OrganizationAttributesLogo logo;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SITE = "site";
  @SerializedName(SERIALIZED_NAME_SITE)
  private String site;

  public static final String SERIALIZED_NAME_SOCIAL_PROFILES = "social_profiles";
  @SerializedName(SERIALIZED_NAME_SOCIAL_PROFILES)
  private OrganizationSocial socialProfiles;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_WIKI = "wiki";
  @SerializedName(SERIALIZED_NAME_WIKI)
  private String wiki;

  public OrganizationAttributes() {
  }

  public OrganizationAttributes address(OrganizationAddress address) {
    this.address = address;
    return this;
  }

  /**
   * Get address
   * @return address
   */
  @javax.annotation.Nullable
  public OrganizationAddress getAddress() {
    return address;
  }

  public void setAddress(OrganizationAddress address) {
    this.address = address;
  }


  public OrganizationAttributes blog(String blog) {
    this.blog = blog;
    return this;
  }

  /**
   * Organization&#x60;s blog
   * @return blog
   */
  @javax.annotation.Nullable
  public String getBlog() {
    return blog;
  }

  public void setBlog(String blog) {
    this.blog = blog;
  }


  public OrganizationAttributes code(String code) {
    this.code = code;
    return this;
  }

  /**
   * Organization&#x60;s code
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public OrganizationAttributes contacts(OrganizationContacts contacts) {
    this.contacts = contacts;
    return this;
  }

  /**
   * Get contacts
   * @return contacts
   */
  @javax.annotation.Nullable
  public OrganizationContacts getContacts() {
    return contacts;
  }

  public void setContacts(OrganizationContacts contacts) {
    this.contacts = contacts;
  }


  public OrganizationAttributes description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public OrganizationAttributes icon(OrganizationAttributesIcon icon) {
    this.icon = icon;
    return this;
  }

  /**
   * Get icon
   * @return icon
   */
  @javax.annotation.Nullable
  public OrganizationAttributesIcon getIcon() {
    return icon;
  }

  public void setIcon(OrganizationAttributesIcon icon) {
    this.icon = icon;
  }


  public OrganizationAttributes industries(List<String> industries) {
    this.industries = industries;
    return this;
  }

  public OrganizationAttributes addIndustriesItem(String industriesItem) {
    if (this.industries == null) {
      this.industries = new ArrayList<>();
    }
    this.industries.add(industriesItem);
    return this;
  }

  /**
   * Industries
   * @return industries
   */
  @javax.annotation.Nullable
  public List<String> getIndustries() {
    return industries;
  }

  public void setIndustries(List<String> industries) {
    this.industries = industries;
  }


  public OrganizationAttributes logo(OrganizationAttributesLogo logo) {
    this.logo = logo;
    return this;
  }

  /**
   * Get logo
   * @return logo
   */
  @javax.annotation.Nullable
  public OrganizationAttributesLogo getLogo() {
    return logo;
  }

  public void setLogo(OrganizationAttributesLogo logo) {
    this.logo = logo;
  }


  public OrganizationAttributes name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Organization&#x60;s name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public OrganizationAttributes site(String site) {
    this.site = site;
    return this;
  }

  /**
   * Organization&#x60;s site
   * @return site
   */
  @javax.annotation.Nullable
  public String getSite() {
    return site;
  }

  public void setSite(String site) {
    this.site = site;
  }


  public OrganizationAttributes socialProfiles(OrganizationSocial socialProfiles) {
    this.socialProfiles = socialProfiles;
    return this;
  }

  /**
   * Get socialProfiles
   * @return socialProfiles
   */
  @javax.annotation.Nullable
  public OrganizationSocial getSocialProfiles() {
    return socialProfiles;
  }

  public void setSocialProfiles(OrganizationSocial socialProfiles) {
    this.socialProfiles = socialProfiles;
  }


  public OrganizationAttributes status(String status) {
    this.status = status;
    return this;
  }

  /**
   * Organization&#x60;s status [active, liquidated, deleted]
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public OrganizationAttributes wiki(String wiki) {
    this.wiki = wiki;
    return this;
  }

  /**
   * Organization&#x60;s wiki
   * @return wiki
   */
  @javax.annotation.Nullable
  public String getWiki() {
    return wiki;
  }

  public void setWiki(String wiki) {
    this.wiki = wiki;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrganizationAttributes organizationAttributes = (OrganizationAttributes) o;
    return Objects.equals(this.address, organizationAttributes.address) &&
        Objects.equals(this.blog, organizationAttributes.blog) &&
        Objects.equals(this.code, organizationAttributes.code) &&
        Objects.equals(this.contacts, organizationAttributes.contacts) &&
        Objects.equals(this.description, organizationAttributes.description) &&
        Objects.equals(this.icon, organizationAttributes.icon) &&
        Objects.equals(this.industries, organizationAttributes.industries) &&
        Objects.equals(this.logo, organizationAttributes.logo) &&
        Objects.equals(this.name, organizationAttributes.name) &&
        Objects.equals(this.site, organizationAttributes.site) &&
        Objects.equals(this.socialProfiles, organizationAttributes.socialProfiles) &&
        Objects.equals(this.status, organizationAttributes.status) &&
        Objects.equals(this.wiki, organizationAttributes.wiki);
  }

  @Override
  public int hashCode() {
    return Objects.hash(address, blog, code, contacts, description, icon, industries, logo, name, site, socialProfiles, status, wiki);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrganizationAttributes {\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    blog: ").append(toIndentedString(blog)).append("\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    contacts: ").append(toIndentedString(contacts)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    icon: ").append(toIndentedString(icon)).append("\n");
    sb.append("    industries: ").append(toIndentedString(industries)).append("\n");
    sb.append("    logo: ").append(toIndentedString(logo)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    site: ").append(toIndentedString(site)).append("\n");
    sb.append("    socialProfiles: ").append(toIndentedString(socialProfiles)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    wiki: ").append(toIndentedString(wiki)).append("\n");
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
    openapiFields.add("address");
    openapiFields.add("blog");
    openapiFields.add("code");
    openapiFields.add("contacts");
    openapiFields.add("description");
    openapiFields.add("icon");
    openapiFields.add("industries");
    openapiFields.add("logo");
    openapiFields.add("name");
    openapiFields.add("site");
    openapiFields.add("social_profiles");
    openapiFields.add("status");
    openapiFields.add("wiki");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OrganizationAttributes
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrganizationAttributes.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrganizationAttributes is not found in the empty JSON string", OrganizationAttributes.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrganizationAttributes.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrganizationAttributes` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `address`
      if (jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) {
        OrganizationAddress.validateJsonElement(jsonObj.get("address"));
      }
      if ((jsonObj.get("blog") != null && !jsonObj.get("blog").isJsonNull()) && !jsonObj.get("blog").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `blog` to be a primitive type in the JSON string but got `%s`", jsonObj.get("blog").toString()));
      }
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      // validate the optional field `contacts`
      if (jsonObj.get("contacts") != null && !jsonObj.get("contacts").isJsonNull()) {
        OrganizationContacts.validateJsonElement(jsonObj.get("contacts"));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // validate the optional field `icon`
      if (jsonObj.get("icon") != null && !jsonObj.get("icon").isJsonNull()) {
        OrganizationAttributesIcon.validateJsonElement(jsonObj.get("icon"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("industries") != null && !jsonObj.get("industries").isJsonNull() && !jsonObj.get("industries").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `industries` to be an array in the JSON string but got `%s`", jsonObj.get("industries").toString()));
      }
      // validate the optional field `logo`
      if (jsonObj.get("logo") != null && !jsonObj.get("logo").isJsonNull()) {
        OrganizationAttributesLogo.validateJsonElement(jsonObj.get("logo"));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("site") != null && !jsonObj.get("site").isJsonNull()) && !jsonObj.get("site").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `site` to be a primitive type in the JSON string but got `%s`", jsonObj.get("site").toString()));
      }
      // validate the optional field `social_profiles`
      if (jsonObj.get("social_profiles") != null && !jsonObj.get("social_profiles").isJsonNull()) {
        OrganizationSocial.validateJsonElement(jsonObj.get("social_profiles"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if ((jsonObj.get("wiki") != null && !jsonObj.get("wiki").isJsonNull()) && !jsonObj.get("wiki").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `wiki` to be a primitive type in the JSON string but got `%s`", jsonObj.get("wiki").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrganizationAttributes.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrganizationAttributes' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrganizationAttributes> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrganizationAttributes.class));

       return (TypeAdapter<T>) new TypeAdapter<OrganizationAttributes>() {
           @Override
           public void write(JsonWriter out, OrganizationAttributes value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrganizationAttributes read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrganizationAttributes given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrganizationAttributes
   * @throws IOException if the JSON string is invalid with respect to OrganizationAttributes
   */
  public static OrganizationAttributes fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrganizationAttributes.class);
  }

  /**
   * Convert an instance of OrganizationAttributes to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

