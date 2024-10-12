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
import org.openapitools.client.model.CurrencyAttributesIcon;

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
 * Array of currencies attributes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:28:06.060998-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CurrencyAttributes {
  public static final String SERIALIZED_NAME_CATEGORY = "category";
  @SerializedName(SERIALIZED_NAME_CATEGORY)
  private String category;

  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_CODE_ESTANDARDS_ALPHA = "code_estandards_alpha";
  @SerializedName(SERIALIZED_NAME_CODE_ESTANDARDS_ALPHA)
  private String codeEstandardsAlpha;

  public static final String SERIALIZED_NAME_CODE_ISO_ALPHA3 = "code_iso_alpha3";
  @SerializedName(SERIALIZED_NAME_CODE_ISO_ALPHA3)
  private String codeIsoAlpha3;

  public static final String SERIALIZED_NAME_CODE_ISO_NUMERIC3 = "code_iso_numeric3";
  @SerializedName(SERIALIZED_NAME_CODE_ISO_NUMERIC3)
  private Integer codeIsoNumeric3;

  public static final String SERIALIZED_NAME_CODE_JSON_ALPHA = "code_json_alpha";
  @SerializedName(SERIALIZED_NAME_CODE_JSON_ALPHA)
  private String codeJsonAlpha;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private String created;

  public static final String SERIALIZED_NAME_CURRENCY_TYPE = "currency_type";
  @SerializedName(SERIALIZED_NAME_CURRENCY_TYPE)
  private String currencyType;

  public static final String SERIALIZED_NAME_DECIMAL_E = "decimal_e";
  @SerializedName(SERIALIZED_NAME_DECIMAL_E)
  private String decimalE;

  public static final String SERIALIZED_NAME_ICON = "icon";
  @SerializedName(SERIALIZED_NAME_ICON)
  private CurrencyAttributesIcon icon;

  public static final String SERIALIZED_NAME_ISSUER = "issuer";
  @SerializedName(SERIALIZED_NAME_ISSUER)
  private String issuer;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NATIVE_SYMBOL = "native_symbol";
  @SerializedName(SERIALIZED_NAME_NATIVE_SYMBOL)
  private String nativeSymbol;

  public static final String SERIALIZED_NAME_SYMBOL = "symbol";
  @SerializedName(SERIALIZED_NAME_SYMBOL)
  private String symbol;

  public CurrencyAttributes() {
  }

  public CurrencyAttributes category(String category) {
    this.category = category;
    return this;
  }

  /**
   * Currency category
   * @return category
   */
  @javax.annotation.Nullable
  public String getCategory() {
    return category;
  }

  public void setCategory(String category) {
    this.category = category;
  }


  public CurrencyAttributes code(String code) {
    this.code = code;
    return this;
  }

  /**
   * Currency system code
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public CurrencyAttributes codeEstandardsAlpha(String codeEstandardsAlpha) {
    this.codeEstandardsAlpha = codeEstandardsAlpha;
    return this;
  }

  /**
   * Get codeEstandardsAlpha
   * @return codeEstandardsAlpha
   */
  @javax.annotation.Nullable
  public String getCodeEstandardsAlpha() {
    return codeEstandardsAlpha;
  }

  public void setCodeEstandardsAlpha(String codeEstandardsAlpha) {
    this.codeEstandardsAlpha = codeEstandardsAlpha;
  }


  public CurrencyAttributes codeIsoAlpha3(String codeIsoAlpha3) {
    this.codeIsoAlpha3 = codeIsoAlpha3;
    return this;
  }

  /**
   * Currency ISO code
   * @return codeIsoAlpha3
   */
  @javax.annotation.Nullable
  public String getCodeIsoAlpha3() {
    return codeIsoAlpha3;
  }

  public void setCodeIsoAlpha3(String codeIsoAlpha3) {
    this.codeIsoAlpha3 = codeIsoAlpha3;
  }


  public CurrencyAttributes codeIsoNumeric3(Integer codeIsoNumeric3) {
    this.codeIsoNumeric3 = codeIsoNumeric3;
    return this;
  }

  /**
   * Currency ISO numeric code
   * @return codeIsoNumeric3
   */
  @javax.annotation.Nullable
  public Integer getCodeIsoNumeric3() {
    return codeIsoNumeric3;
  }

  public void setCodeIsoNumeric3(Integer codeIsoNumeric3) {
    this.codeIsoNumeric3 = codeIsoNumeric3;
  }


  public CurrencyAttributes codeJsonAlpha(String codeJsonAlpha) {
    this.codeJsonAlpha = codeJsonAlpha;
    return this;
  }

  /**
   * Get codeJsonAlpha
   * @return codeJsonAlpha
   */
  @javax.annotation.Nullable
  public String getCodeJsonAlpha() {
    return codeJsonAlpha;
  }

  public void setCodeJsonAlpha(String codeJsonAlpha) {
    this.codeJsonAlpha = codeJsonAlpha;
  }


  public CurrencyAttributes created(String created) {
    this.created = created;
    return this;
  }

  /**
   * Created date in system (in Unixtime)
   * @return created
   */
  @javax.annotation.Nullable
  public String getCreated() {
    return created;
  }

  public void setCreated(String created) {
    this.created = created;
  }


  public CurrencyAttributes currencyType(String currencyType) {
    this.currencyType = currencyType;
    return this;
  }

  /**
   * Type of currencies [national, digital, virtual, metal, energy]
   * @return currencyType
   */
  @javax.annotation.Nullable
  public String getCurrencyType() {
    return currencyType;
  }

  public void setCurrencyType(String currencyType) {
    this.currencyType = currencyType;
  }


  public CurrencyAttributes decimalE(String decimalE) {
    this.decimalE = decimalE;
    return this;
  }

  /**
   * Number of digits after the decimal separator
   * @return decimalE
   */
  @javax.annotation.Nullable
  public String getDecimalE() {
    return decimalE;
  }

  public void setDecimalE(String decimalE) {
    this.decimalE = decimalE;
  }


  public CurrencyAttributes icon(CurrencyAttributesIcon icon) {
    this.icon = icon;
    return this;
  }

  /**
   * Get icon
   * @return icon
   */
  @javax.annotation.Nullable
  public CurrencyAttributesIcon getIcon() {
    return icon;
  }

  public void setIcon(CurrencyAttributesIcon icon) {
    this.icon = icon;
  }


  public CurrencyAttributes issuer(String issuer) {
    this.issuer = issuer;
    return this;
  }

  /**
   * Currency&#x60;s issuer
   * @return issuer
   */
  @javax.annotation.Nullable
  public String getIssuer() {
    return issuer;
  }

  public void setIssuer(String issuer) {
    this.issuer = issuer;
  }


  public CurrencyAttributes name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Currency description
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CurrencyAttributes nativeSymbol(String nativeSymbol) {
    this.nativeSymbol = nativeSymbol;
    return this;
  }

  /**
   * Currencyâ€™s symbol. In general, only for nationals currencies
   * @return nativeSymbol
   */
  @javax.annotation.Nullable
  public String getNativeSymbol() {
    return nativeSymbol;
  }

  public void setNativeSymbol(String nativeSymbol) {
    this.nativeSymbol = nativeSymbol;
  }


  public CurrencyAttributes symbol(String symbol) {
    this.symbol = symbol;
    return this;
  }

  /**
   * Currencyâ€™s symbol. In general, only for nationals currencies
   * @return symbol
   */
  @javax.annotation.Nullable
  public String getSymbol() {
    return symbol;
  }

  public void setSymbol(String symbol) {
    this.symbol = symbol;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CurrencyAttributes currencyAttributes = (CurrencyAttributes) o;
    return Objects.equals(this.category, currencyAttributes.category) &&
        Objects.equals(this.code, currencyAttributes.code) &&
        Objects.equals(this.codeEstandardsAlpha, currencyAttributes.codeEstandardsAlpha) &&
        Objects.equals(this.codeIsoAlpha3, currencyAttributes.codeIsoAlpha3) &&
        Objects.equals(this.codeIsoNumeric3, currencyAttributes.codeIsoNumeric3) &&
        Objects.equals(this.codeJsonAlpha, currencyAttributes.codeJsonAlpha) &&
        Objects.equals(this.created, currencyAttributes.created) &&
        Objects.equals(this.currencyType, currencyAttributes.currencyType) &&
        Objects.equals(this.decimalE, currencyAttributes.decimalE) &&
        Objects.equals(this.icon, currencyAttributes.icon) &&
        Objects.equals(this.issuer, currencyAttributes.issuer) &&
        Objects.equals(this.name, currencyAttributes.name) &&
        Objects.equals(this.nativeSymbol, currencyAttributes.nativeSymbol) &&
        Objects.equals(this.symbol, currencyAttributes.symbol);
  }

  @Override
  public int hashCode() {
    return Objects.hash(category, code, codeEstandardsAlpha, codeIsoAlpha3, codeIsoNumeric3, codeJsonAlpha, created, currencyType, decimalE, icon, issuer, name, nativeSymbol, symbol);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CurrencyAttributes {\n");
    sb.append("    category: ").append(toIndentedString(category)).append("\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    codeEstandardsAlpha: ").append(toIndentedString(codeEstandardsAlpha)).append("\n");
    sb.append("    codeIsoAlpha3: ").append(toIndentedString(codeIsoAlpha3)).append("\n");
    sb.append("    codeIsoNumeric3: ").append(toIndentedString(codeIsoNumeric3)).append("\n");
    sb.append("    codeJsonAlpha: ").append(toIndentedString(codeJsonAlpha)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    currencyType: ").append(toIndentedString(currencyType)).append("\n");
    sb.append("    decimalE: ").append(toIndentedString(decimalE)).append("\n");
    sb.append("    icon: ").append(toIndentedString(icon)).append("\n");
    sb.append("    issuer: ").append(toIndentedString(issuer)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    nativeSymbol: ").append(toIndentedString(nativeSymbol)).append("\n");
    sb.append("    symbol: ").append(toIndentedString(symbol)).append("\n");
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
    openapiFields.add("category");
    openapiFields.add("code");
    openapiFields.add("code_estandards_alpha");
    openapiFields.add("code_iso_alpha3");
    openapiFields.add("code_iso_numeric3");
    openapiFields.add("code_json_alpha");
    openapiFields.add("created");
    openapiFields.add("currency_type");
    openapiFields.add("decimal_e");
    openapiFields.add("icon");
    openapiFields.add("issuer");
    openapiFields.add("name");
    openapiFields.add("native_symbol");
    openapiFields.add("symbol");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CurrencyAttributes
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CurrencyAttributes.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CurrencyAttributes is not found in the empty JSON string", CurrencyAttributes.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CurrencyAttributes.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CurrencyAttributes` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("category") != null && !jsonObj.get("category").isJsonNull()) && !jsonObj.get("category").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `category` to be a primitive type in the JSON string but got `%s`", jsonObj.get("category").toString()));
      }
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if ((jsonObj.get("code_estandards_alpha") != null && !jsonObj.get("code_estandards_alpha").isJsonNull()) && !jsonObj.get("code_estandards_alpha").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code_estandards_alpha` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code_estandards_alpha").toString()));
      }
      if ((jsonObj.get("code_iso_alpha3") != null && !jsonObj.get("code_iso_alpha3").isJsonNull()) && !jsonObj.get("code_iso_alpha3").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code_iso_alpha3` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code_iso_alpha3").toString()));
      }
      if ((jsonObj.get("code_json_alpha") != null && !jsonObj.get("code_json_alpha").isJsonNull()) && !jsonObj.get("code_json_alpha").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code_json_alpha` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code_json_alpha").toString()));
      }
      if ((jsonObj.get("created") != null && !jsonObj.get("created").isJsonNull()) && !jsonObj.get("created").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created").toString()));
      }
      if ((jsonObj.get("currency_type") != null && !jsonObj.get("currency_type").isJsonNull()) && !jsonObj.get("currency_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency_type").toString()));
      }
      if ((jsonObj.get("decimal_e") != null && !jsonObj.get("decimal_e").isJsonNull()) && !jsonObj.get("decimal_e").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `decimal_e` to be a primitive type in the JSON string but got `%s`", jsonObj.get("decimal_e").toString()));
      }
      // validate the optional field `icon`
      if (jsonObj.get("icon") != null && !jsonObj.get("icon").isJsonNull()) {
        CurrencyAttributesIcon.validateJsonElement(jsonObj.get("icon"));
      }
      if ((jsonObj.get("issuer") != null && !jsonObj.get("issuer").isJsonNull()) && !jsonObj.get("issuer").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `issuer` to be a primitive type in the JSON string but got `%s`", jsonObj.get("issuer").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("native_symbol") != null && !jsonObj.get("native_symbol").isJsonNull()) && !jsonObj.get("native_symbol").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `native_symbol` to be a primitive type in the JSON string but got `%s`", jsonObj.get("native_symbol").toString()));
      }
      if ((jsonObj.get("symbol") != null && !jsonObj.get("symbol").isJsonNull()) && !jsonObj.get("symbol").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `symbol` to be a primitive type in the JSON string but got `%s`", jsonObj.get("symbol").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CurrencyAttributes.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CurrencyAttributes' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CurrencyAttributes> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CurrencyAttributes.class));

       return (TypeAdapter<T>) new TypeAdapter<CurrencyAttributes>() {
           @Override
           public void write(JsonWriter out, CurrencyAttributes value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CurrencyAttributes read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CurrencyAttributes given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CurrencyAttributes
   * @throws IOException if the JSON string is invalid with respect to CurrencyAttributes
   */
  public static CurrencyAttributes fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CurrencyAttributes.class);
  }

  /**
   * Convert an instance of CurrencyAttributes to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

