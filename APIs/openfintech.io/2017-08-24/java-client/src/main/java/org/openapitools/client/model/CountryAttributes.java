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
 * CountryAttributes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:28:06.060998-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CountryAttributes {
  public static final String SERIALIZED_NAME_AREA = "area";
  @SerializedName(SERIALIZED_NAME_AREA)
  private String area;

  public static final String SERIALIZED_NAME_CALLING_CODES = "calling_codes";
  @SerializedName(SERIALIZED_NAME_CALLING_CODES)
  private List<Integer> callingCodes = new ArrayList<>();

  public static final String SERIALIZED_NAME_CAPITAL = "capital";
  @SerializedName(SERIALIZED_NAME_CAPITAL)
  private String capital;

  public static final String SERIALIZED_NAME_CODE_ALPHA3 = "code_alpha3";
  @SerializedName(SERIALIZED_NAME_CODE_ALPHA3)
  private String codeAlpha3;

  public static final String SERIALIZED_NAME_LANGUAGES = "languages";
  @SerializedName(SERIALIZED_NAME_LANGUAGES)
  private List<String> languages = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NATIVE_NAME = "native_name";
  @SerializedName(SERIALIZED_NAME_NATIVE_NAME)
  private String nativeName;

  public static final String SERIALIZED_NAME_POPULATION = "population";
  @SerializedName(SERIALIZED_NAME_POPULATION)
  private String population;

  public static final String SERIALIZED_NAME_REGION = "region";
  @SerializedName(SERIALIZED_NAME_REGION)
  private String region;

  public static final String SERIALIZED_NAME_SUB_REGION = "sub_region";
  @SerializedName(SERIALIZED_NAME_SUB_REGION)
  private String subRegion;

  public static final String SERIALIZED_NAME_TIMEZONES = "timezones";
  @SerializedName(SERIALIZED_NAME_TIMEZONES)
  private List<String> timezones = new ArrayList<>();

  public static final String SERIALIZED_NAME_TOP_LEVEL_DOMAINS = "top_level_domains";
  @SerializedName(SERIALIZED_NAME_TOP_LEVEL_DOMAINS)
  private List<String> topLevelDomains = new ArrayList<>();

  public CountryAttributes() {
  }

  public CountryAttributes area(String area) {
    this.area = area;
    return this;
  }

  /**
   * Countryâ€™s area (sq km)
   * @return area
   */
  @javax.annotation.Nullable
  public String getArea() {
    return area;
  }

  public void setArea(String area) {
    this.area = area;
  }


  public CountryAttributes callingCodes(List<Integer> callingCodes) {
    this.callingCodes = callingCodes;
    return this;
  }

  public CountryAttributes addCallingCodesItem(Integer callingCodesItem) {
    if (this.callingCodes == null) {
      this.callingCodes = new ArrayList<>();
    }
    this.callingCodes.add(callingCodesItem);
    return this;
  }

  /**
   * Array of country&#x60;s phone codes
   * @return callingCodes
   */
  @javax.annotation.Nullable
  public List<Integer> getCallingCodes() {
    return callingCodes;
  }

  public void setCallingCodes(List<Integer> callingCodes) {
    this.callingCodes = callingCodes;
  }


  public CountryAttributes capital(String capital) {
    this.capital = capital;
    return this;
  }

  /**
   * Countryâ€™s capital
   * @return capital
   */
  @javax.annotation.Nullable
  public String getCapital() {
    return capital;
  }

  public void setCapital(String capital) {
    this.capital = capital;
  }


  public CountryAttributes codeAlpha3(String codeAlpha3) {
    this.codeAlpha3 = codeAlpha3;
    return this;
  }

  /**
   * Country&#x60;s ISO alpha3 code
   * @return codeAlpha3
   */
  @javax.annotation.Nullable
  public String getCodeAlpha3() {
    return codeAlpha3;
  }

  public void setCodeAlpha3(String codeAlpha3) {
    this.codeAlpha3 = codeAlpha3;
  }


  public CountryAttributes languages(List<String> languages) {
    this.languages = languages;
    return this;
  }

  public CountryAttributes addLanguagesItem(String languagesItem) {
    if (this.languages == null) {
      this.languages = new ArrayList<>();
    }
    this.languages.add(languagesItem);
    return this;
  }

  /**
   * Array of country&#x60;s languages
   * @return languages
   */
  @javax.annotation.Nullable
  public List<String> getLanguages() {
    return languages;
  }

  public void setLanguages(List<String> languages) {
    this.languages = languages;
  }


  public CountryAttributes name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Country&#x60;s name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CountryAttributes nativeName(String nativeName) {
    this.nativeName = nativeName;
    return this;
  }

  /**
   * Country&#x60;s nativ name
   * @return nativeName
   */
  @javax.annotation.Nullable
  public String getNativeName() {
    return nativeName;
  }

  public void setNativeName(String nativeName) {
    this.nativeName = nativeName;
  }


  public CountryAttributes population(String population) {
    this.population = population;
    return this;
  }

  /**
   * Countryâ€™s population
   * @return population
   */
  @javax.annotation.Nullable
  public String getPopulation() {
    return population;
  }

  public void setPopulation(String population) {
    this.population = population;
  }


  public CountryAttributes region(String region) {
    this.region = region;
    return this;
  }

  /**
   * Countryâ€™s region:&lt;br&gt;    * Africa   * Americas   * Asia   * Europe   * Oceania   * Polar 
   * @return region
   */
  @javax.annotation.Nullable
  public String getRegion() {
    return region;
  }

  public void setRegion(String region) {
    this.region = region;
  }


  public CountryAttributes subRegion(String subRegion) {
    this.subRegion = subRegion;
    return this;
  }

  /**
   * Countryâ€™s sub region:&lt;br&gt;    * Northern Africa   * Southern Africa   * Western Africa   * Eastern Africa   * Middle Africa   * Northern America   * South America   * Central America   * Caribbean   * Southern Asia   * Western Asia   * Eastern Asia   * South-Eastern Asia   * Central Asia   * Northern Europe   * Southern Europe   * Western Europe   * Eastern Europe   * Polynesia   * Australia and New Zealand   * Micronesia   * Melanesia 
   * @return subRegion
   */
  @javax.annotation.Nullable
  public String getSubRegion() {
    return subRegion;
  }

  public void setSubRegion(String subRegion) {
    this.subRegion = subRegion;
  }


  public CountryAttributes timezones(List<String> timezones) {
    this.timezones = timezones;
    return this;
  }

  public CountryAttributes addTimezonesItem(String timezonesItem) {
    if (this.timezones == null) {
      this.timezones = new ArrayList<>();
    }
    this.timezones.add(timezonesItem);
    return this;
  }

  /**
   * Array of country&#x60;s timezones (UTC)
   * @return timezones
   */
  @javax.annotation.Nullable
  public List<String> getTimezones() {
    return timezones;
  }

  public void setTimezones(List<String> timezones) {
    this.timezones = timezones;
  }


  public CountryAttributes topLevelDomains(List<String> topLevelDomains) {
    this.topLevelDomains = topLevelDomains;
    return this;
  }

  public CountryAttributes addTopLevelDomainsItem(String topLevelDomainsItem) {
    if (this.topLevelDomains == null) {
      this.topLevelDomains = new ArrayList<>();
    }
    this.topLevelDomains.add(topLevelDomainsItem);
    return this;
  }

  /**
   * Array of country&#x60;s domains
   * @return topLevelDomains
   */
  @javax.annotation.Nullable
  public List<String> getTopLevelDomains() {
    return topLevelDomains;
  }

  public void setTopLevelDomains(List<String> topLevelDomains) {
    this.topLevelDomains = topLevelDomains;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CountryAttributes countryAttributes = (CountryAttributes) o;
    return Objects.equals(this.area, countryAttributes.area) &&
        Objects.equals(this.callingCodes, countryAttributes.callingCodes) &&
        Objects.equals(this.capital, countryAttributes.capital) &&
        Objects.equals(this.codeAlpha3, countryAttributes.codeAlpha3) &&
        Objects.equals(this.languages, countryAttributes.languages) &&
        Objects.equals(this.name, countryAttributes.name) &&
        Objects.equals(this.nativeName, countryAttributes.nativeName) &&
        Objects.equals(this.population, countryAttributes.population) &&
        Objects.equals(this.region, countryAttributes.region) &&
        Objects.equals(this.subRegion, countryAttributes.subRegion) &&
        Objects.equals(this.timezones, countryAttributes.timezones) &&
        Objects.equals(this.topLevelDomains, countryAttributes.topLevelDomains);
  }

  @Override
  public int hashCode() {
    return Objects.hash(area, callingCodes, capital, codeAlpha3, languages, name, nativeName, population, region, subRegion, timezones, topLevelDomains);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CountryAttributes {\n");
    sb.append("    area: ").append(toIndentedString(area)).append("\n");
    sb.append("    callingCodes: ").append(toIndentedString(callingCodes)).append("\n");
    sb.append("    capital: ").append(toIndentedString(capital)).append("\n");
    sb.append("    codeAlpha3: ").append(toIndentedString(codeAlpha3)).append("\n");
    sb.append("    languages: ").append(toIndentedString(languages)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    nativeName: ").append(toIndentedString(nativeName)).append("\n");
    sb.append("    population: ").append(toIndentedString(population)).append("\n");
    sb.append("    region: ").append(toIndentedString(region)).append("\n");
    sb.append("    subRegion: ").append(toIndentedString(subRegion)).append("\n");
    sb.append("    timezones: ").append(toIndentedString(timezones)).append("\n");
    sb.append("    topLevelDomains: ").append(toIndentedString(topLevelDomains)).append("\n");
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
    openapiFields.add("area");
    openapiFields.add("calling_codes");
    openapiFields.add("capital");
    openapiFields.add("code_alpha3");
    openapiFields.add("languages");
    openapiFields.add("name");
    openapiFields.add("native_name");
    openapiFields.add("population");
    openapiFields.add("region");
    openapiFields.add("sub_region");
    openapiFields.add("timezones");
    openapiFields.add("top_level_domains");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CountryAttributes
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CountryAttributes.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CountryAttributes is not found in the empty JSON string", CountryAttributes.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CountryAttributes.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CountryAttributes` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("area") != null && !jsonObj.get("area").isJsonNull()) && !jsonObj.get("area").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `area` to be a primitive type in the JSON string but got `%s`", jsonObj.get("area").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("calling_codes") != null && !jsonObj.get("calling_codes").isJsonNull() && !jsonObj.get("calling_codes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `calling_codes` to be an array in the JSON string but got `%s`", jsonObj.get("calling_codes").toString()));
      }
      if ((jsonObj.get("capital") != null && !jsonObj.get("capital").isJsonNull()) && !jsonObj.get("capital").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `capital` to be a primitive type in the JSON string but got `%s`", jsonObj.get("capital").toString()));
      }
      if ((jsonObj.get("code_alpha3") != null && !jsonObj.get("code_alpha3").isJsonNull()) && !jsonObj.get("code_alpha3").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code_alpha3` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code_alpha3").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("languages") != null && !jsonObj.get("languages").isJsonNull() && !jsonObj.get("languages").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `languages` to be an array in the JSON string but got `%s`", jsonObj.get("languages").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("native_name") != null && !jsonObj.get("native_name").isJsonNull()) && !jsonObj.get("native_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `native_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("native_name").toString()));
      }
      if ((jsonObj.get("population") != null && !jsonObj.get("population").isJsonNull()) && !jsonObj.get("population").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `population` to be a primitive type in the JSON string but got `%s`", jsonObj.get("population").toString()));
      }
      if ((jsonObj.get("region") != null && !jsonObj.get("region").isJsonNull()) && !jsonObj.get("region").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `region` to be a primitive type in the JSON string but got `%s`", jsonObj.get("region").toString()));
      }
      if ((jsonObj.get("sub_region") != null && !jsonObj.get("sub_region").isJsonNull()) && !jsonObj.get("sub_region").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sub_region` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sub_region").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("timezones") != null && !jsonObj.get("timezones").isJsonNull() && !jsonObj.get("timezones").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `timezones` to be an array in the JSON string but got `%s`", jsonObj.get("timezones").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("top_level_domains") != null && !jsonObj.get("top_level_domains").isJsonNull() && !jsonObj.get("top_level_domains").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `top_level_domains` to be an array in the JSON string but got `%s`", jsonObj.get("top_level_domains").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CountryAttributes.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CountryAttributes' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CountryAttributes> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CountryAttributes.class));

       return (TypeAdapter<T>) new TypeAdapter<CountryAttributes>() {
           @Override
           public void write(JsonWriter out, CountryAttributes value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CountryAttributes read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CountryAttributes given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CountryAttributes
   * @throws IOException if the JSON string is invalid with respect to CountryAttributes
   */
  public static CountryAttributes fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CountryAttributes.class);
  }

  /**
   * Convert an instance of CountryAttributes to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

