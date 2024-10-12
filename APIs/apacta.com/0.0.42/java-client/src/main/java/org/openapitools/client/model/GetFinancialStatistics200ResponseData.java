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
 * GetFinancialStatistics200ResponseData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetFinancialStatistics200ResponseData {
  public static final String SERIALIZED_NAME_INVOICED_AMOUNT = "invoicedAmount";
  @SerializedName(SERIALIZED_NAME_INVOICED_AMOUNT)
  private Float invoicedAmount;

  public static final String SERIALIZED_NAME_INVOICED_WORKING_HOURS = "invoicedWorkingHours";
  @SerializedName(SERIALIZED_NAME_INVOICED_WORKING_HOURS)
  private String invoicedWorkingHours;

  public static final String SERIALIZED_NAME_NOT_INVOICED_AMOUNT = "notInvoicedAmount";
  @SerializedName(SERIALIZED_NAME_NOT_INVOICED_AMOUNT)
  private Float notInvoicedAmount;

  public static final String SERIALIZED_NAME_NOT_INVOICED_WORKING_HOURS = "notInvoicedWorkingHours";
  @SerializedName(SERIALIZED_NAME_NOT_INVOICED_WORKING_HOURS)
  private String notInvoicedWorkingHours;

  public static final String SERIALIZED_NAME_PRODUCTS_COSTS = "productsCosts";
  @SerializedName(SERIALIZED_NAME_PRODUCTS_COSTS)
  private Float productsCosts;

  public static final String SERIALIZED_NAME_PRODUCTS_SALES = "productsSales";
  @SerializedName(SERIALIZED_NAME_PRODUCTS_SALES)
  private Float productsSales;

  public static final String SERIALIZED_NAME_RENTALS_COSTS = "rentalsCosts";
  @SerializedName(SERIALIZED_NAME_RENTALS_COSTS)
  private Float rentalsCosts;

  public static final String SERIALIZED_NAME_RENTALS_SALES = "rentalsSales";
  @SerializedName(SERIALIZED_NAME_RENTALS_SALES)
  private Float rentalsSales;

  public static final String SERIALIZED_NAME_TOTAL_COSTS = "totalCosts";
  @SerializedName(SERIALIZED_NAME_TOTAL_COSTS)
  private Float totalCosts;

  public static final String SERIALIZED_NAME_TOTAL_SALES = "totalSales";
  @SerializedName(SERIALIZED_NAME_TOTAL_SALES)
  private Float totalSales;

  public static final String SERIALIZED_NAME_WORK_TIME_COSTS = "workTimeCosts";
  @SerializedName(SERIALIZED_NAME_WORK_TIME_COSTS)
  private Float workTimeCosts;

  public static final String SERIALIZED_NAME_WORK_TIME_SALES = "workTimeSales";
  @SerializedName(SERIALIZED_NAME_WORK_TIME_SALES)
  private Float workTimeSales;

  public GetFinancialStatistics200ResponseData() {
  }

  public GetFinancialStatistics200ResponseData invoicedAmount(Float invoicedAmount) {
    this.invoicedAmount = invoicedAmount;
    return this;
  }

  /**
   * Get invoicedAmount
   * @return invoicedAmount
   */
  @javax.annotation.Nullable
  public Float getInvoicedAmount() {
    return invoicedAmount;
  }

  public void setInvoicedAmount(Float invoicedAmount) {
    this.invoicedAmount = invoicedAmount;
  }


  public GetFinancialStatistics200ResponseData invoicedWorkingHours(String invoicedWorkingHours) {
    this.invoicedWorkingHours = invoicedWorkingHours;
    return this;
  }

  /**
   * Get invoicedWorkingHours
   * @return invoicedWorkingHours
   */
  @javax.annotation.Nullable
  public String getInvoicedWorkingHours() {
    return invoicedWorkingHours;
  }

  public void setInvoicedWorkingHours(String invoicedWorkingHours) {
    this.invoicedWorkingHours = invoicedWorkingHours;
  }


  public GetFinancialStatistics200ResponseData notInvoicedAmount(Float notInvoicedAmount) {
    this.notInvoicedAmount = notInvoicedAmount;
    return this;
  }

  /**
   * Get notInvoicedAmount
   * @return notInvoicedAmount
   */
  @javax.annotation.Nullable
  public Float getNotInvoicedAmount() {
    return notInvoicedAmount;
  }

  public void setNotInvoicedAmount(Float notInvoicedAmount) {
    this.notInvoicedAmount = notInvoicedAmount;
  }


  public GetFinancialStatistics200ResponseData notInvoicedWorkingHours(String notInvoicedWorkingHours) {
    this.notInvoicedWorkingHours = notInvoicedWorkingHours;
    return this;
  }

  /**
   * Get notInvoicedWorkingHours
   * @return notInvoicedWorkingHours
   */
  @javax.annotation.Nullable
  public String getNotInvoicedWorkingHours() {
    return notInvoicedWorkingHours;
  }

  public void setNotInvoicedWorkingHours(String notInvoicedWorkingHours) {
    this.notInvoicedWorkingHours = notInvoicedWorkingHours;
  }


  public GetFinancialStatistics200ResponseData productsCosts(Float productsCosts) {
    this.productsCosts = productsCosts;
    return this;
  }

  /**
   * Get productsCosts
   * @return productsCosts
   */
  @javax.annotation.Nullable
  public Float getProductsCosts() {
    return productsCosts;
  }

  public void setProductsCosts(Float productsCosts) {
    this.productsCosts = productsCosts;
  }


  public GetFinancialStatistics200ResponseData productsSales(Float productsSales) {
    this.productsSales = productsSales;
    return this;
  }

  /**
   * Get productsSales
   * @return productsSales
   */
  @javax.annotation.Nullable
  public Float getProductsSales() {
    return productsSales;
  }

  public void setProductsSales(Float productsSales) {
    this.productsSales = productsSales;
  }


  public GetFinancialStatistics200ResponseData rentalsCosts(Float rentalsCosts) {
    this.rentalsCosts = rentalsCosts;
    return this;
  }

  /**
   * Get rentalsCosts
   * @return rentalsCosts
   */
  @javax.annotation.Nullable
  public Float getRentalsCosts() {
    return rentalsCosts;
  }

  public void setRentalsCosts(Float rentalsCosts) {
    this.rentalsCosts = rentalsCosts;
  }


  public GetFinancialStatistics200ResponseData rentalsSales(Float rentalsSales) {
    this.rentalsSales = rentalsSales;
    return this;
  }

  /**
   * Get rentalsSales
   * @return rentalsSales
   */
  @javax.annotation.Nullable
  public Float getRentalsSales() {
    return rentalsSales;
  }

  public void setRentalsSales(Float rentalsSales) {
    this.rentalsSales = rentalsSales;
  }


  public GetFinancialStatistics200ResponseData totalCosts(Float totalCosts) {
    this.totalCosts = totalCosts;
    return this;
  }

  /**
   * Get totalCosts
   * @return totalCosts
   */
  @javax.annotation.Nullable
  public Float getTotalCosts() {
    return totalCosts;
  }

  public void setTotalCosts(Float totalCosts) {
    this.totalCosts = totalCosts;
  }


  public GetFinancialStatistics200ResponseData totalSales(Float totalSales) {
    this.totalSales = totalSales;
    return this;
  }

  /**
   * Get totalSales
   * @return totalSales
   */
  @javax.annotation.Nullable
  public Float getTotalSales() {
    return totalSales;
  }

  public void setTotalSales(Float totalSales) {
    this.totalSales = totalSales;
  }


  public GetFinancialStatistics200ResponseData workTimeCosts(Float workTimeCosts) {
    this.workTimeCosts = workTimeCosts;
    return this;
  }

  /**
   * Get workTimeCosts
   * @return workTimeCosts
   */
  @javax.annotation.Nullable
  public Float getWorkTimeCosts() {
    return workTimeCosts;
  }

  public void setWorkTimeCosts(Float workTimeCosts) {
    this.workTimeCosts = workTimeCosts;
  }


  public GetFinancialStatistics200ResponseData workTimeSales(Float workTimeSales) {
    this.workTimeSales = workTimeSales;
    return this;
  }

  /**
   * Get workTimeSales
   * @return workTimeSales
   */
  @javax.annotation.Nullable
  public Float getWorkTimeSales() {
    return workTimeSales;
  }

  public void setWorkTimeSales(Float workTimeSales) {
    this.workTimeSales = workTimeSales;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetFinancialStatistics200ResponseData getFinancialStatistics200ResponseData = (GetFinancialStatistics200ResponseData) o;
    return Objects.equals(this.invoicedAmount, getFinancialStatistics200ResponseData.invoicedAmount) &&
        Objects.equals(this.invoicedWorkingHours, getFinancialStatistics200ResponseData.invoicedWorkingHours) &&
        Objects.equals(this.notInvoicedAmount, getFinancialStatistics200ResponseData.notInvoicedAmount) &&
        Objects.equals(this.notInvoicedWorkingHours, getFinancialStatistics200ResponseData.notInvoicedWorkingHours) &&
        Objects.equals(this.productsCosts, getFinancialStatistics200ResponseData.productsCosts) &&
        Objects.equals(this.productsSales, getFinancialStatistics200ResponseData.productsSales) &&
        Objects.equals(this.rentalsCosts, getFinancialStatistics200ResponseData.rentalsCosts) &&
        Objects.equals(this.rentalsSales, getFinancialStatistics200ResponseData.rentalsSales) &&
        Objects.equals(this.totalCosts, getFinancialStatistics200ResponseData.totalCosts) &&
        Objects.equals(this.totalSales, getFinancialStatistics200ResponseData.totalSales) &&
        Objects.equals(this.workTimeCosts, getFinancialStatistics200ResponseData.workTimeCosts) &&
        Objects.equals(this.workTimeSales, getFinancialStatistics200ResponseData.workTimeSales);
  }

  @Override
  public int hashCode() {
    return Objects.hash(invoicedAmount, invoicedWorkingHours, notInvoicedAmount, notInvoicedWorkingHours, productsCosts, productsSales, rentalsCosts, rentalsSales, totalCosts, totalSales, workTimeCosts, workTimeSales);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetFinancialStatistics200ResponseData {\n");
    sb.append("    invoicedAmount: ").append(toIndentedString(invoicedAmount)).append("\n");
    sb.append("    invoicedWorkingHours: ").append(toIndentedString(invoicedWorkingHours)).append("\n");
    sb.append("    notInvoicedAmount: ").append(toIndentedString(notInvoicedAmount)).append("\n");
    sb.append("    notInvoicedWorkingHours: ").append(toIndentedString(notInvoicedWorkingHours)).append("\n");
    sb.append("    productsCosts: ").append(toIndentedString(productsCosts)).append("\n");
    sb.append("    productsSales: ").append(toIndentedString(productsSales)).append("\n");
    sb.append("    rentalsCosts: ").append(toIndentedString(rentalsCosts)).append("\n");
    sb.append("    rentalsSales: ").append(toIndentedString(rentalsSales)).append("\n");
    sb.append("    totalCosts: ").append(toIndentedString(totalCosts)).append("\n");
    sb.append("    totalSales: ").append(toIndentedString(totalSales)).append("\n");
    sb.append("    workTimeCosts: ").append(toIndentedString(workTimeCosts)).append("\n");
    sb.append("    workTimeSales: ").append(toIndentedString(workTimeSales)).append("\n");
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
    openapiFields.add("invoicedAmount");
    openapiFields.add("invoicedWorkingHours");
    openapiFields.add("notInvoicedAmount");
    openapiFields.add("notInvoicedWorkingHours");
    openapiFields.add("productsCosts");
    openapiFields.add("productsSales");
    openapiFields.add("rentalsCosts");
    openapiFields.add("rentalsSales");
    openapiFields.add("totalCosts");
    openapiFields.add("totalSales");
    openapiFields.add("workTimeCosts");
    openapiFields.add("workTimeSales");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetFinancialStatistics200ResponseData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetFinancialStatistics200ResponseData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetFinancialStatistics200ResponseData is not found in the empty JSON string", GetFinancialStatistics200ResponseData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetFinancialStatistics200ResponseData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetFinancialStatistics200ResponseData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("invoicedWorkingHours") != null && !jsonObj.get("invoicedWorkingHours").isJsonNull()) && !jsonObj.get("invoicedWorkingHours").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `invoicedWorkingHours` to be a primitive type in the JSON string but got `%s`", jsonObj.get("invoicedWorkingHours").toString()));
      }
      if ((jsonObj.get("notInvoicedWorkingHours") != null && !jsonObj.get("notInvoicedWorkingHours").isJsonNull()) && !jsonObj.get("notInvoicedWorkingHours").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notInvoicedWorkingHours` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notInvoicedWorkingHours").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetFinancialStatistics200ResponseData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetFinancialStatistics200ResponseData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetFinancialStatistics200ResponseData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetFinancialStatistics200ResponseData.class));

       return (TypeAdapter<T>) new TypeAdapter<GetFinancialStatistics200ResponseData>() {
           @Override
           public void write(JsonWriter out, GetFinancialStatistics200ResponseData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetFinancialStatistics200ResponseData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetFinancialStatistics200ResponseData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetFinancialStatistics200ResponseData
   * @throws IOException if the JSON string is invalid with respect to GetFinancialStatistics200ResponseData
   */
  public static GetFinancialStatistics200ResponseData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetFinancialStatistics200ResponseData.class);
  }

  /**
   * Convert an instance of GetFinancialStatistics200ResponseData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

