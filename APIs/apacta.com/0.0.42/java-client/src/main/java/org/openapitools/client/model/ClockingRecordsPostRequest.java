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
import java.util.UUID;

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
 * ClockingRecordsPostRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ClockingRecordsPostRequest {
  public static final String SERIALIZED_NAME_CHECKIN_LATITUDE = "checkin_latitude";
  @SerializedName(SERIALIZED_NAME_CHECKIN_LATITUDE)
  private String checkinLatitude;

  public static final String SERIALIZED_NAME_CHECKIN_LONGITUDE = "checkin_longitude";
  @SerializedName(SERIALIZED_NAME_CHECKIN_LONGITUDE)
  private String checkinLongitude;

  public static final String SERIALIZED_NAME_CHECKOUT_LATITUDE = "checkout_latitude";
  @SerializedName(SERIALIZED_NAME_CHECKOUT_LATITUDE)
  private String checkoutLatitude;

  public static final String SERIALIZED_NAME_CHECKOUT_LONGITUDE = "checkout_longitude";
  @SerializedName(SERIALIZED_NAME_CHECKOUT_LONGITUDE)
  private String checkoutLongitude;

  public static final String SERIALIZED_NAME_PROJECT_ID = "project_id";
  @SerializedName(SERIALIZED_NAME_PROJECT_ID)
  private UUID projectId;

  public ClockingRecordsPostRequest() {
  }

  public ClockingRecordsPostRequest checkinLatitude(String checkinLatitude) {
    this.checkinLatitude = checkinLatitude;
    return this;
  }

  /**
   * Get checkinLatitude
   * @return checkinLatitude
   */
  @javax.annotation.Nullable
  public String getCheckinLatitude() {
    return checkinLatitude;
  }

  public void setCheckinLatitude(String checkinLatitude) {
    this.checkinLatitude = checkinLatitude;
  }


  public ClockingRecordsPostRequest checkinLongitude(String checkinLongitude) {
    this.checkinLongitude = checkinLongitude;
    return this;
  }

  /**
   * Get checkinLongitude
   * @return checkinLongitude
   */
  @javax.annotation.Nullable
  public String getCheckinLongitude() {
    return checkinLongitude;
  }

  public void setCheckinLongitude(String checkinLongitude) {
    this.checkinLongitude = checkinLongitude;
  }


  public ClockingRecordsPostRequest checkoutLatitude(String checkoutLatitude) {
    this.checkoutLatitude = checkoutLatitude;
    return this;
  }

  /**
   * Get checkoutLatitude
   * @return checkoutLatitude
   */
  @javax.annotation.Nullable
  public String getCheckoutLatitude() {
    return checkoutLatitude;
  }

  public void setCheckoutLatitude(String checkoutLatitude) {
    this.checkoutLatitude = checkoutLatitude;
  }


  public ClockingRecordsPostRequest checkoutLongitude(String checkoutLongitude) {
    this.checkoutLongitude = checkoutLongitude;
    return this;
  }

  /**
   * Get checkoutLongitude
   * @return checkoutLongitude
   */
  @javax.annotation.Nullable
  public String getCheckoutLongitude() {
    return checkoutLongitude;
  }

  public void setCheckoutLongitude(String checkoutLongitude) {
    this.checkoutLongitude = checkoutLongitude;
  }


  public ClockingRecordsPostRequest projectId(UUID projectId) {
    this.projectId = projectId;
    return this;
  }

  /**
   * Get projectId
   * @return projectId
   */
  @javax.annotation.Nullable
  public UUID getProjectId() {
    return projectId;
  }

  public void setProjectId(UUID projectId) {
    this.projectId = projectId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ClockingRecordsPostRequest clockingRecordsPostRequest = (ClockingRecordsPostRequest) o;
    return Objects.equals(this.checkinLatitude, clockingRecordsPostRequest.checkinLatitude) &&
        Objects.equals(this.checkinLongitude, clockingRecordsPostRequest.checkinLongitude) &&
        Objects.equals(this.checkoutLatitude, clockingRecordsPostRequest.checkoutLatitude) &&
        Objects.equals(this.checkoutLongitude, clockingRecordsPostRequest.checkoutLongitude) &&
        Objects.equals(this.projectId, clockingRecordsPostRequest.projectId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(checkinLatitude, checkinLongitude, checkoutLatitude, checkoutLongitude, projectId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ClockingRecordsPostRequest {\n");
    sb.append("    checkinLatitude: ").append(toIndentedString(checkinLatitude)).append("\n");
    sb.append("    checkinLongitude: ").append(toIndentedString(checkinLongitude)).append("\n");
    sb.append("    checkoutLatitude: ").append(toIndentedString(checkoutLatitude)).append("\n");
    sb.append("    checkoutLongitude: ").append(toIndentedString(checkoutLongitude)).append("\n");
    sb.append("    projectId: ").append(toIndentedString(projectId)).append("\n");
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
    openapiFields.add("checkin_latitude");
    openapiFields.add("checkin_longitude");
    openapiFields.add("checkout_latitude");
    openapiFields.add("checkout_longitude");
    openapiFields.add("project_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ClockingRecordsPostRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ClockingRecordsPostRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ClockingRecordsPostRequest is not found in the empty JSON string", ClockingRecordsPostRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ClockingRecordsPostRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ClockingRecordsPostRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("checkin_latitude") != null && !jsonObj.get("checkin_latitude").isJsonNull()) && !jsonObj.get("checkin_latitude").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `checkin_latitude` to be a primitive type in the JSON string but got `%s`", jsonObj.get("checkin_latitude").toString()));
      }
      if ((jsonObj.get("checkin_longitude") != null && !jsonObj.get("checkin_longitude").isJsonNull()) && !jsonObj.get("checkin_longitude").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `checkin_longitude` to be a primitive type in the JSON string but got `%s`", jsonObj.get("checkin_longitude").toString()));
      }
      if ((jsonObj.get("checkout_latitude") != null && !jsonObj.get("checkout_latitude").isJsonNull()) && !jsonObj.get("checkout_latitude").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `checkout_latitude` to be a primitive type in the JSON string but got `%s`", jsonObj.get("checkout_latitude").toString()));
      }
      if ((jsonObj.get("checkout_longitude") != null && !jsonObj.get("checkout_longitude").isJsonNull()) && !jsonObj.get("checkout_longitude").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `checkout_longitude` to be a primitive type in the JSON string but got `%s`", jsonObj.get("checkout_longitude").toString()));
      }
      if ((jsonObj.get("project_id") != null && !jsonObj.get("project_id").isJsonNull()) && !jsonObj.get("project_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ClockingRecordsPostRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ClockingRecordsPostRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ClockingRecordsPostRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ClockingRecordsPostRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<ClockingRecordsPostRequest>() {
           @Override
           public void write(JsonWriter out, ClockingRecordsPostRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ClockingRecordsPostRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ClockingRecordsPostRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ClockingRecordsPostRequest
   * @throws IOException if the JSON string is invalid with respect to ClockingRecordsPostRequest
   */
  public static ClockingRecordsPostRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ClockingRecordsPostRequest.class);
  }

  /**
   * Convert an instance of ClockingRecordsPostRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

