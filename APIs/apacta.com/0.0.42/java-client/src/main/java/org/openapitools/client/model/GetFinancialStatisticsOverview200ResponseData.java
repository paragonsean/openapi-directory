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
 * GetFinancialStatisticsOverview200ResponseData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetFinancialStatisticsOverview200ResponseData {
  public static final String SERIALIZED_NAME_EXPENSES_SALES_PRICE = "expensesSalesPrice";
  @SerializedName(SERIALIZED_NAME_EXPENSES_SALES_PRICE)
  private Float expensesSalesPrice;

  public static final String SERIALIZED_NAME_INVOICED_AMOUNT = "invoicedAmount";
  @SerializedName(SERIALIZED_NAME_INVOICED_AMOUNT)
  private Float invoicedAmount;

  public static final String SERIALIZED_NAME_MARGIN = "margin";
  @SerializedName(SERIALIZED_NAME_MARGIN)
  private Float margin;

  public static final String SERIALIZED_NAME_MATERIAL_RENTALS_COST_PRICE = "materialRentalsCostPrice";
  @SerializedName(SERIALIZED_NAME_MATERIAL_RENTALS_COST_PRICE)
  private Float materialRentalsCostPrice;

  public static final String SERIALIZED_NAME_PRODUCTS_COST_PRICE = "productsCostPrice";
  @SerializedName(SERIALIZED_NAME_PRODUCTS_COST_PRICE)
  private Float productsCostPrice;

  public static final String SERIALIZED_NAME_TOTAL_WORKING_HOURS = "totalWorkingHours";
  @SerializedName(SERIALIZED_NAME_TOTAL_WORKING_HOURS)
  private String totalWorkingHours;

  public GetFinancialStatisticsOverview200ResponseData() {
  }

  public GetFinancialStatisticsOverview200ResponseData expensesSalesPrice(Float expensesSalesPrice) {
    this.expensesSalesPrice = expensesSalesPrice;
    return this;
  }

  /**
   * Get expensesSalesPrice
   * @return expensesSalesPrice
   */
  @javax.annotation.Nullable
  public Float getExpensesSalesPrice() {
    return expensesSalesPrice;
  }

  public void setExpensesSalesPrice(Float expensesSalesPrice) {
    this.expensesSalesPrice = expensesSalesPrice;
  }


  public GetFinancialStatisticsOverview200ResponseData invoicedAmount(Float invoicedAmount) {
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


  public GetFinancialStatisticsOverview200ResponseData margin(Float margin) {
    this.margin = margin;
    return this;
  }

  /**
   * Get margin
   * @return margin
   */
  @javax.annotation.Nullable
  public Float getMargin() {
    return margin;
  }

  public void setMargin(Float margin) {
    this.margin = margin;
  }


  public GetFinancialStatisticsOverview200ResponseData materialRentalsCostPrice(Float materialRentalsCostPrice) {
    this.materialRentalsCostPrice = materialRentalsCostPrice;
    return this;
  }

  /**
   * Get materialRentalsCostPrice
   * @return materialRentalsCostPrice
   */
  @javax.annotation.Nullable
  public Float getMaterialRentalsCostPrice() {
    return materialRentalsCostPrice;
  }

  public void setMaterialRentalsCostPrice(Float materialRentalsCostPrice) {
    this.materialRentalsCostPrice = materialRentalsCostPrice;
  }


  public GetFinancialStatisticsOverview200ResponseData productsCostPrice(Float productsCostPrice) {
    this.productsCostPrice = productsCostPrice;
    return this;
  }

  /**
   * Get productsCostPrice
   * @return productsCostPrice
   */
  @javax.annotation.Nullable
  public Float getProductsCostPrice() {
    return productsCostPrice;
  }

  public void setProductsCostPrice(Float productsCostPrice) {
    this.productsCostPrice = productsCostPrice;
  }


  public GetFinancialStatisticsOverview200ResponseData totalWorkingHours(String totalWorkingHours) {
    this.totalWorkingHours = totalWorkingHours;
    return this;
  }

  /**
   * Get totalWorkingHours
   * @return totalWorkingHours
   */
  @javax.annotation.Nullable
  public String getTotalWorkingHours() {
    return totalWorkingHours;
  }

  public void setTotalWorkingHours(String totalWorkingHours) {
    this.totalWorkingHours = totalWorkingHours;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetFinancialStatisticsOverview200ResponseData getFinancialStatisticsOverview200ResponseData = (GetFinancialStatisticsOverview200ResponseData) o;
    return Objects.equals(this.expensesSalesPrice, getFinancialStatisticsOverview200ResponseData.expensesSalesPrice) &&
        Objects.equals(this.invoicedAmount, getFinancialStatisticsOverview200ResponseData.invoicedAmount) &&
        Objects.equals(this.margin, getFinancialStatisticsOverview200ResponseData.margin) &&
        Objects.equals(this.materialRentalsCostPrice, getFinancialStatisticsOverview200ResponseData.materialRentalsCostPrice) &&
        Objects.equals(this.productsCostPrice, getFinancialStatisticsOverview200ResponseData.productsCostPrice) &&
        Objects.equals(this.totalWorkingHours, getFinancialStatisticsOverview200ResponseData.totalWorkingHours);
  }

  @Override
  public int hashCode() {
    return Objects.hash(expensesSalesPrice, invoicedAmount, margin, materialRentalsCostPrice, productsCostPrice, totalWorkingHours);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetFinancialStatisticsOverview200ResponseData {\n");
    sb.append("    expensesSalesPrice: ").append(toIndentedString(expensesSalesPrice)).append("\n");
    sb.append("    invoicedAmount: ").append(toIndentedString(invoicedAmount)).append("\n");
    sb.append("    margin: ").append(toIndentedString(margin)).append("\n");
    sb.append("    materialRentalsCostPrice: ").append(toIndentedString(materialRentalsCostPrice)).append("\n");
    sb.append("    productsCostPrice: ").append(toIndentedString(productsCostPrice)).append("\n");
    sb.append("    totalWorkingHours: ").append(toIndentedString(totalWorkingHours)).append("\n");
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
    openapiFields.add("expensesSalesPrice");
    openapiFields.add("invoicedAmount");
    openapiFields.add("margin");
    openapiFields.add("materialRentalsCostPrice");
    openapiFields.add("productsCostPrice");
    openapiFields.add("totalWorkingHours");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetFinancialStatisticsOverview200ResponseData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetFinancialStatisticsOverview200ResponseData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetFinancialStatisticsOverview200ResponseData is not found in the empty JSON string", GetFinancialStatisticsOverview200ResponseData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetFinancialStatisticsOverview200ResponseData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetFinancialStatisticsOverview200ResponseData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("totalWorkingHours") != null && !jsonObj.get("totalWorkingHours").isJsonNull()) && !jsonObj.get("totalWorkingHours").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `totalWorkingHours` to be a primitive type in the JSON string but got `%s`", jsonObj.get("totalWorkingHours").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetFinancialStatisticsOverview200ResponseData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetFinancialStatisticsOverview200ResponseData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetFinancialStatisticsOverview200ResponseData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetFinancialStatisticsOverview200ResponseData.class));

       return (TypeAdapter<T>) new TypeAdapter<GetFinancialStatisticsOverview200ResponseData>() {
           @Override
           public void write(JsonWriter out, GetFinancialStatisticsOverview200ResponseData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetFinancialStatisticsOverview200ResponseData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetFinancialStatisticsOverview200ResponseData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetFinancialStatisticsOverview200ResponseData
   * @throws IOException if the JSON string is invalid with respect to GetFinancialStatisticsOverview200ResponseData
   */
  public static GetFinancialStatisticsOverview200ResponseData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetFinancialStatisticsOverview200ResponseData.class);
  }

  /**
   * Convert an instance of GetFinancialStatisticsOverview200ResponseData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

