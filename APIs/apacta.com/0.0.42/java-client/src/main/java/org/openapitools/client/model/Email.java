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
 * Email
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Email {
  public static final String SERIALIZED_NAME_API_RESPONSE = "api_response";
  @SerializedName(SERIALIZED_NAME_API_RESPONSE)
  private String _apiResponse;

  public static final String SERIALIZED_NAME_BODY = "body";
  @SerializedName(SERIALIZED_NAME_BODY)
  private String body;

  public static final String SERIALIZED_NAME_CARBON_COPY = "carbon_copy";
  @SerializedName(SERIALIZED_NAME_CARBON_COPY)
  private String carbonCopy;

  public static final String SERIALIZED_NAME_COMPANY_ID = "company_id";
  @SerializedName(SERIALIZED_NAME_COMPANY_ID)
  private UUID companyId;

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

  public static final String SERIALIZED_NAME_IS_SENT = "is_sent";
  @SerializedName(SERIALIZED_NAME_IS_SENT)
  private Boolean isSent;

  public static final String SERIALIZED_NAME_MODIFIED = "modified";
  @SerializedName(SERIALIZED_NAME_MODIFIED)
  private String modified;

  public static final String SERIALIZED_NAME_RECIPIENTS = "recipients";
  @SerializedName(SERIALIZED_NAME_RECIPIENTS)
  private String recipients;

  public static final String SERIALIZED_NAME_REPLY_TO = "reply_to";
  @SerializedName(SERIALIZED_NAME_REPLY_TO)
  private String replyTo;

  public static final String SERIALIZED_NAME_SUBJECT = "subject";
  @SerializedName(SERIALIZED_NAME_SUBJECT)
  private String subject;

  public Email() {
  }

  public Email(
     String created, 
     String deleted, 
     String modified
  ) {
    this();
    this.created = created;
    this.deleted = deleted;
    this.modified = modified;
  }

  public Email _apiResponse(String _apiResponse) {
    this._apiResponse = _apiResponse;
    return this;
  }

  /**
   * Get _apiResponse
   * @return _apiResponse
   */
  @javax.annotation.Nullable
  public String getApiResponse() {
    return _apiResponse;
  }

  public void setApiResponse(String _apiResponse) {
    this._apiResponse = _apiResponse;
  }


  public Email body(String body) {
    this.body = body;
    return this;
  }

  /**
   * Get body
   * @return body
   */
  @javax.annotation.Nullable
  public String getBody() {
    return body;
  }

  public void setBody(String body) {
    this.body = body;
  }


  public Email carbonCopy(String carbonCopy) {
    this.carbonCopy = carbonCopy;
    return this;
  }

  /**
   * Get carbonCopy
   * @return carbonCopy
   */
  @javax.annotation.Nullable
  public String getCarbonCopy() {
    return carbonCopy;
  }

  public void setCarbonCopy(String carbonCopy) {
    this.carbonCopy = carbonCopy;
  }


  public Email companyId(UUID companyId) {
    this.companyId = companyId;
    return this;
  }

  /**
   * Get companyId
   * @return companyId
   */
  @javax.annotation.Nullable
  public UUID getCompanyId() {
    return companyId;
  }

  public void setCompanyId(UUID companyId) {
    this.companyId = companyId;
  }


  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public String getCreated() {
    return created;
  }



  public Email createdById(UUID createdById) {
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



  public Email id(UUID id) {
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


  public Email isSent(Boolean isSent) {
    this.isSent = isSent;
    return this;
  }

  /**
   * Get isSent
   * @return isSent
   */
  @javax.annotation.Nullable
  public Boolean getIsSent() {
    return isSent;
  }

  public void setIsSent(Boolean isSent) {
    this.isSent = isSent;
  }


  /**
   * Get modified
   * @return modified
   */
  @javax.annotation.Nullable
  public String getModified() {
    return modified;
  }



  public Email recipients(String recipients) {
    this.recipients = recipients;
    return this;
  }

  /**
   * Get recipients
   * @return recipients
   */
  @javax.annotation.Nullable
  public String getRecipients() {
    return recipients;
  }

  public void setRecipients(String recipients) {
    this.recipients = recipients;
  }


  public Email replyTo(String replyTo) {
    this.replyTo = replyTo;
    return this;
  }

  /**
   * Get replyTo
   * @return replyTo
   */
  @javax.annotation.Nullable
  public String getReplyTo() {
    return replyTo;
  }

  public void setReplyTo(String replyTo) {
    this.replyTo = replyTo;
  }


  public Email subject(String subject) {
    this.subject = subject;
    return this;
  }

  /**
   * Get subject
   * @return subject
   */
  @javax.annotation.Nullable
  public String getSubject() {
    return subject;
  }

  public void setSubject(String subject) {
    this.subject = subject;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Email email = (Email) o;
    return Objects.equals(this._apiResponse, email._apiResponse) &&
        Objects.equals(this.body, email.body) &&
        Objects.equals(this.carbonCopy, email.carbonCopy) &&
        Objects.equals(this.companyId, email.companyId) &&
        Objects.equals(this.created, email.created) &&
        Objects.equals(this.createdById, email.createdById) &&
        Objects.equals(this.deleted, email.deleted) &&
        Objects.equals(this.id, email.id) &&
        Objects.equals(this.isSent, email.isSent) &&
        Objects.equals(this.modified, email.modified) &&
        Objects.equals(this.recipients, email.recipients) &&
        Objects.equals(this.replyTo, email.replyTo) &&
        Objects.equals(this.subject, email.subject);
  }

  @Override
  public int hashCode() {
    return Objects.hash(_apiResponse, body, carbonCopy, companyId, created, createdById, deleted, id, isSent, modified, recipients, replyTo, subject);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Email {\n");
    sb.append("    _apiResponse: ").append(toIndentedString(_apiResponse)).append("\n");
    sb.append("    body: ").append(toIndentedString(body)).append("\n");
    sb.append("    carbonCopy: ").append(toIndentedString(carbonCopy)).append("\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    createdById: ").append(toIndentedString(createdById)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isSent: ").append(toIndentedString(isSent)).append("\n");
    sb.append("    modified: ").append(toIndentedString(modified)).append("\n");
    sb.append("    recipients: ").append(toIndentedString(recipients)).append("\n");
    sb.append("    replyTo: ").append(toIndentedString(replyTo)).append("\n");
    sb.append("    subject: ").append(toIndentedString(subject)).append("\n");
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
    openapiFields.add("api_response");
    openapiFields.add("body");
    openapiFields.add("carbon_copy");
    openapiFields.add("company_id");
    openapiFields.add("created");
    openapiFields.add("created_by_id");
    openapiFields.add("deleted");
    openapiFields.add("id");
    openapiFields.add("is_sent");
    openapiFields.add("modified");
    openapiFields.add("recipients");
    openapiFields.add("reply_to");
    openapiFields.add("subject");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Email
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Email.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Email is not found in the empty JSON string", Email.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Email.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Email` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("api_response") != null && !jsonObj.get("api_response").isJsonNull()) && !jsonObj.get("api_response").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `api_response` to be a primitive type in the JSON string but got `%s`", jsonObj.get("api_response").toString()));
      }
      if ((jsonObj.get("body") != null && !jsonObj.get("body").isJsonNull()) && !jsonObj.get("body").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `body` to be a primitive type in the JSON string but got `%s`", jsonObj.get("body").toString()));
      }
      if ((jsonObj.get("carbon_copy") != null && !jsonObj.get("carbon_copy").isJsonNull()) && !jsonObj.get("carbon_copy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `carbon_copy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("carbon_copy").toString()));
      }
      if ((jsonObj.get("company_id") != null && !jsonObj.get("company_id").isJsonNull()) && !jsonObj.get("company_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_id").toString()));
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
      if ((jsonObj.get("recipients") != null && !jsonObj.get("recipients").isJsonNull()) && !jsonObj.get("recipients").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `recipients` to be a primitive type in the JSON string but got `%s`", jsonObj.get("recipients").toString()));
      }
      if ((jsonObj.get("reply_to") != null && !jsonObj.get("reply_to").isJsonNull()) && !jsonObj.get("reply_to").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reply_to` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reply_to").toString()));
      }
      if ((jsonObj.get("subject") != null && !jsonObj.get("subject").isJsonNull()) && !jsonObj.get("subject").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subject` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subject").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Email.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Email' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Email> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Email.class));

       return (TypeAdapter<T>) new TypeAdapter<Email>() {
           @Override
           public void write(JsonWriter out, Email value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Email read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Email given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Email
   * @throws IOException if the JSON string is invalid with respect to Email
   */
  public static Email fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Email.class);
  }

  /**
   * Convert an instance of Email to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

