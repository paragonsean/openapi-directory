/*
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
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
import java.util.UUID;
import org.openapitools.client.model.GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner;

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
 * GetCompaniesVendorsExpenseStatistics200ResponseDataInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetCompaniesVendorsExpenseStatistics200ResponseDataInner {
  public static final String SERIALIZED_NAME_LAST_MONTH = "last_month";
  @SerializedName(SERIALIZED_NAME_LAST_MONTH)
  private List<GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner> lastMonth = new ArrayList<>();

  public static final String SERIALIZED_NAME_THIRTY_DAYS = "thirty_days";
  @SerializedName(SERIALIZED_NAME_THIRTY_DAYS)
  private List<GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner> thirtyDays = new ArrayList<>();

  public static final String SERIALIZED_NAME_VENDOR_ID = "vendor_id";
  @SerializedName(SERIALIZED_NAME_VENDOR_ID)
  private UUID vendorId;

  public GetCompaniesVendorsExpenseStatistics200ResponseDataInner() {
  }

  public GetCompaniesVendorsExpenseStatistics200ResponseDataInner lastMonth(List<GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner> lastMonth) {
    this.lastMonth = lastMonth;
    return this;
  }

  public GetCompaniesVendorsExpenseStatistics200ResponseDataInner addLastMonthItem(GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner lastMonthItem) {
    if (this.lastMonth == null) {
      this.lastMonth = new ArrayList<>();
    }
    this.lastMonth.add(lastMonthItem);
    return this;
  }

  /**
   * Get lastMonth
   * @return lastMonth
   */
  @javax.annotation.Nullable
  public List<GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner> getLastMonth() {
    return lastMonth;
  }

  public void setLastMonth(List<GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner> lastMonth) {
    this.lastMonth = lastMonth;
  }


  public GetCompaniesVendorsExpenseStatistics200ResponseDataInner thirtyDays(List<GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner> thirtyDays) {
    this.thirtyDays = thirtyDays;
    return this;
  }

  public GetCompaniesVendorsExpenseStatistics200ResponseDataInner addThirtyDaysItem(GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner thirtyDaysItem) {
    if (this.thirtyDays == null) {
      this.thirtyDays = new ArrayList<>();
    }
    this.thirtyDays.add(thirtyDaysItem);
    return this;
  }

  /**
   * Get thirtyDays
   * @return thirtyDays
   */
  @javax.annotation.Nullable
  public List<GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner> getThirtyDays() {
    return thirtyDays;
  }

  public void setThirtyDays(List<GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner> thirtyDays) {
    this.thirtyDays = thirtyDays;
  }


  public GetCompaniesVendorsExpenseStatistics200ResponseDataInner vendorId(UUID vendorId) {
    this.vendorId = vendorId;
    return this;
  }

  /**
   * Get vendorId
   * @return vendorId
   */
  @javax.annotation.Nullable
  public UUID getVendorId() {
    return vendorId;
  }

  public void setVendorId(UUID vendorId) {
    this.vendorId = vendorId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetCompaniesVendorsExpenseStatistics200ResponseDataInner getCompaniesVendorsExpenseStatistics200ResponseDataInner = (GetCompaniesVendorsExpenseStatistics200ResponseDataInner) o;
    return Objects.equals(this.lastMonth, getCompaniesVendorsExpenseStatistics200ResponseDataInner.lastMonth) &&
        Objects.equals(this.thirtyDays, getCompaniesVendorsExpenseStatistics200ResponseDataInner.thirtyDays) &&
        Objects.equals(this.vendorId, getCompaniesVendorsExpenseStatistics200ResponseDataInner.vendorId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(lastMonth, thirtyDays, vendorId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetCompaniesVendorsExpenseStatistics200ResponseDataInner {\n");
    sb.append("    lastMonth: ").append(toIndentedString(lastMonth)).append("\n");
    sb.append("    thirtyDays: ").append(toIndentedString(thirtyDays)).append("\n");
    sb.append("    vendorId: ").append(toIndentedString(vendorId)).append("\n");
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
    openapiFields.add("last_month");
    openapiFields.add("thirty_days");
    openapiFields.add("vendor_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetCompaniesVendorsExpenseStatistics200ResponseDataInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetCompaniesVendorsExpenseStatistics200ResponseDataInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetCompaniesVendorsExpenseStatistics200ResponseDataInner is not found in the empty JSON string", GetCompaniesVendorsExpenseStatistics200ResponseDataInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetCompaniesVendorsExpenseStatistics200ResponseDataInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetCompaniesVendorsExpenseStatistics200ResponseDataInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("last_month") != null && !jsonObj.get("last_month").isJsonNull()) {
        JsonArray jsonArraylastMonth = jsonObj.getAsJsonArray("last_month");
        if (jsonArraylastMonth != null) {
          // ensure the json data is an array
          if (!jsonObj.get("last_month").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `last_month` to be an array in the JSON string but got `%s`", jsonObj.get("last_month").toString()));
          }

          // validate the optional field `last_month` (array)
          for (int i = 0; i < jsonArraylastMonth.size(); i++) {
            GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner.validateJsonElement(jsonArraylastMonth.get(i));
          };
        }
      }
      if (jsonObj.get("thirty_days") != null && !jsonObj.get("thirty_days").isJsonNull()) {
        JsonArray jsonArraythirtyDays = jsonObj.getAsJsonArray("thirty_days");
        if (jsonArraythirtyDays != null) {
          // ensure the json data is an array
          if (!jsonObj.get("thirty_days").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `thirty_days` to be an array in the JSON string but got `%s`", jsonObj.get("thirty_days").toString()));
          }

          // validate the optional field `thirty_days` (array)
          for (int i = 0; i < jsonArraythirtyDays.size(); i++) {
            GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner.validateJsonElement(jsonArraythirtyDays.get(i));
          };
        }
      }
      if ((jsonObj.get("vendor_id") != null && !jsonObj.get("vendor_id").isJsonNull()) && !jsonObj.get("vendor_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vendor_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vendor_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetCompaniesVendorsExpenseStatistics200ResponseDataInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetCompaniesVendorsExpenseStatistics200ResponseDataInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetCompaniesVendorsExpenseStatistics200ResponseDataInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetCompaniesVendorsExpenseStatistics200ResponseDataInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetCompaniesVendorsExpenseStatistics200ResponseDataInner>() {
           @Override
           public void write(JsonWriter out, GetCompaniesVendorsExpenseStatistics200ResponseDataInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetCompaniesVendorsExpenseStatistics200ResponseDataInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetCompaniesVendorsExpenseStatistics200ResponseDataInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetCompaniesVendorsExpenseStatistics200ResponseDataInner
   * @throws IOException if the JSON string is invalid with respect to GetCompaniesVendorsExpenseStatistics200ResponseDataInner
   */
  public static GetCompaniesVendorsExpenseStatistics200ResponseDataInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetCompaniesVendorsExpenseStatistics200ResponseDataInner.class);
  }

  /**
   * Convert an instance of GetCompaniesVendorsExpenseStatistics200ResponseDataInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

