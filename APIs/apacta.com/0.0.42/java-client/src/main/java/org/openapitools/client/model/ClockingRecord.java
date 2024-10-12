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
 * ClockingRecord
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ClockingRecord {
  public static final String SERIALIZED_NAME_CHECKED_IN = "checked_in";
  @SerializedName(SERIALIZED_NAME_CHECKED_IN)
  private String checkedIn;

  public static final String SERIALIZED_NAME_CHECKED_OUT = "checked_out";
  @SerializedName(SERIALIZED_NAME_CHECKED_OUT)
  private String checkedOut;

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

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private String created;

  public static final String SERIALIZED_NAME_CREATED_BY_ID = "created_by_id";
  @SerializedName(SERIALIZED_NAME_CREATED_BY_ID)
  private UUID createdById;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private String deleted;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_MODIFIED = "modified";
  @SerializedName(SERIALIZED_NAME_MODIFIED)
  private String modified;

  public static final String SERIALIZED_NAME_MODIFIED_BY_ID = "modified_by_id";
  @SerializedName(SERIALIZED_NAME_MODIFIED_BY_ID)
  private UUID modifiedById;

  public static final String SERIALIZED_NAME_PROJECT_ID = "project_id";
  @SerializedName(SERIALIZED_NAME_PROJECT_ID)
  private UUID projectId;

  public static final String SERIALIZED_NAME_USER_ID = "user_id";
  @SerializedName(SERIALIZED_NAME_USER_ID)
  private UUID userId;

  public ClockingRecord() {
  }

  public ClockingRecord(
     String created, 
     String deleted, 
     String modified
  ) {
    this();
    this.created = created;
    this.deleted = deleted;
    this.modified = modified;
  }

  public ClockingRecord checkedIn(String checkedIn) {
    this.checkedIn = checkedIn;
    return this;
  }

  /**
   * Get checkedIn
   * @return checkedIn
   */
  @javax.annotation.Nullable
  public String getCheckedIn() {
    return checkedIn;
  }

  public void setCheckedIn(String checkedIn) {
    this.checkedIn = checkedIn;
  }


  public ClockingRecord checkedOut(String checkedOut) {
    this.checkedOut = checkedOut;
    return this;
  }

  /**
   * Get checkedOut
   * @return checkedOut
   */
  @javax.annotation.Nullable
  public String getCheckedOut() {
    return checkedOut;
  }

  public void setCheckedOut(String checkedOut) {
    this.checkedOut = checkedOut;
  }


  public ClockingRecord checkinLatitude(String checkinLatitude) {
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


  public ClockingRecord checkinLongitude(String checkinLongitude) {
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


  public ClockingRecord checkoutLatitude(String checkoutLatitude) {
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


  public ClockingRecord checkoutLongitude(String checkoutLongitude) {
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


  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public String getCreated() {
    return created;
  }



  public ClockingRecord createdById(UUID createdById) {
    this.createdById = createdById;
    return this;
  }

  /**
   * Get createdById
   * @return createdById
   */
  @javax.annotation.Nullable
  public UUID getCreatedById() {
    return createdById;
  }

  public void setCreatedById(UUID createdById) {
    this.createdById = createdById;
  }


  /**
   * Only present if it&#39;s a deleted object
   * @return deleted
   */
  @javax.annotation.Nullable
  public String getDeleted() {
    return deleted;
  }



  public ClockingRecord id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  /**
   * Get modified
   * @return modified
   */
  @javax.annotation.Nullable
  public String getModified() {
    return modified;
  }



  public ClockingRecord modifiedById(UUID modifiedById) {
    this.modifiedById = modifiedById;
    return this;
  }

  /**
   * Get modifiedById
   * @return modifiedById
   */
  @javax.annotation.Nullable
  public UUID getModifiedById() {
    return modifiedById;
  }

  public void setModifiedById(UUID modifiedById) {
    this.modifiedById = modifiedById;
  }


  public ClockingRecord projectId(UUID projectId) {
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


  public ClockingRecord userId(UUID userId) {
    this.userId = userId;
    return this;
  }

  /**
   * Get userId
   * @return userId
   */
  @javax.annotation.Nullable
  public UUID getUserId() {
    return userId;
  }

  public void setUserId(UUID userId) {
    this.userId = userId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ClockingRecord clockingRecord = (ClockingRecord) o;
    return Objects.equals(this.checkedIn, clockingRecord.checkedIn) &&
        Objects.equals(this.checkedOut, clockingRecord.checkedOut) &&
        Objects.equals(this.checkinLatitude, clockingRecord.checkinLatitude) &&
        Objects.equals(this.checkinLongitude, clockingRecord.checkinLongitude) &&
        Objects.equals(this.checkoutLatitude, clockingRecord.checkoutLatitude) &&
        Objects.equals(this.checkoutLongitude, clockingRecord.checkoutLongitude) &&
        Objects.equals(this.created, clockingRecord.created) &&
        Objects.equals(this.createdById, clockingRecord.createdById) &&
        Objects.equals(this.deleted, clockingRecord.deleted) &&
        Objects.equals(this.id, clockingRecord.id) &&
        Objects.equals(this.modified, clockingRecord.modified) &&
        Objects.equals(this.modifiedById, clockingRecord.modifiedById) &&
        Objects.equals(this.projectId, clockingRecord.projectId) &&
        Objects.equals(this.userId, clockingRecord.userId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(checkedIn, checkedOut, checkinLatitude, checkinLongitude, checkoutLatitude, checkoutLongitude, created, createdById, deleted, id, modified, modifiedById, projectId, userId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ClockingRecord {\n");
    sb.append("    checkedIn: ").append(toIndentedString(checkedIn)).append("\n");
    sb.append("    checkedOut: ").append(toIndentedString(checkedOut)).append("\n");
    sb.append("    checkinLatitude: ").append(toIndentedString(checkinLatitude)).append("\n");
    sb.append("    checkinLongitude: ").append(toIndentedString(checkinLongitude)).append("\n");
    sb.append("    checkoutLatitude: ").append(toIndentedString(checkoutLatitude)).append("\n");
    sb.append("    checkoutLongitude: ").append(toIndentedString(checkoutLongitude)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    createdById: ").append(toIndentedString(createdById)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    modified: ").append(toIndentedString(modified)).append("\n");
    sb.append("    modifiedById: ").append(toIndentedString(modifiedById)).append("\n");
    sb.append("    projectId: ").append(toIndentedString(projectId)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
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
    openapiFields.add("checked_in");
    openapiFields.add("checked_out");
    openapiFields.add("checkin_latitude");
    openapiFields.add("checkin_longitude");
    openapiFields.add("checkout_latitude");
    openapiFields.add("checkout_longitude");
    openapiFields.add("created");
    openapiFields.add("created_by_id");
    openapiFields.add("deleted");
    openapiFields.add("id");
    openapiFields.add("modified");
    openapiFields.add("modified_by_id");
    openapiFields.add("project_id");
    openapiFields.add("user_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ClockingRecord
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ClockingRecord.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ClockingRecord is not found in the empty JSON string", ClockingRecord.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ClockingRecord.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ClockingRecord` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("checked_in") != null && !jsonObj.get("checked_in").isJsonNull()) && !jsonObj.get("checked_in").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `checked_in` to be a primitive type in the JSON string but got `%s`", jsonObj.get("checked_in").toString()));
      }
      if ((jsonObj.get("checked_out") != null && !jsonObj.get("checked_out").isJsonNull()) && !jsonObj.get("checked_out").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `checked_out` to be a primitive type in the JSON string but got `%s`", jsonObj.get("checked_out").toString()));
      }
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
      if ((jsonObj.get("created") != null && !jsonObj.get("created").isJsonNull()) && !jsonObj.get("created").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created").toString()));
      }
      if ((jsonObj.get("created_by_id") != null && !jsonObj.get("created_by_id").isJsonNull()) && !jsonObj.get("created_by_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by_id").toString()));
      }
      if ((jsonObj.get("deleted") != null && !jsonObj.get("deleted").isJsonNull()) && !jsonObj.get("deleted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deleted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deleted").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("modified") != null && !jsonObj.get("modified").isJsonNull()) && !jsonObj.get("modified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified").toString()));
      }
      if ((jsonObj.get("modified_by_id") != null && !jsonObj.get("modified_by_id").isJsonNull()) && !jsonObj.get("modified_by_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified_by_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified_by_id").toString()));
      }
      if ((jsonObj.get("project_id") != null && !jsonObj.get("project_id").isJsonNull()) && !jsonObj.get("project_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project_id").toString()));
      }
      if ((jsonObj.get("user_id") != null && !jsonObj.get("user_id").isJsonNull()) && !jsonObj.get("user_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `user_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("user_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ClockingRecord.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ClockingRecord' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ClockingRecord> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ClockingRecord.class));

       return (TypeAdapter<T>) new TypeAdapter<ClockingRecord>() {
           @Override
           public void write(JsonWriter out, ClockingRecord value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ClockingRecord read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ClockingRecord given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ClockingRecord
   * @throws IOException if the JSON string is invalid with respect to ClockingRecord
   */
  public static ClockingRecord fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ClockingRecord.class);
  }

  /**
   * Convert an instance of ClockingRecord to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

