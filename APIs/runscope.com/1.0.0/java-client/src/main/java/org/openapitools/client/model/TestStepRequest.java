/*
 * Runscope API
 * Manage Runscope programmatically.
 *
 * The version of the OpenAPI document: 1.0.0
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
import org.openapitools.client.model.Assertion;
import org.openapitools.client.model.Variable;

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
 * TestStepRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:55.705127-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TestStepRequest {
  public static final String SERIALIZED_NAME_STEP_TYPE = "step_type";
  @SerializedName(SERIALIZED_NAME_STEP_TYPE)
  private String stepType;

  public static final String SERIALIZED_NAME_ASSERTIONS = "assertions";
  @SerializedName(SERIALIZED_NAME_ASSERTIONS)
  private List<Assertion> assertions = new ArrayList<>();

  public static final String SERIALIZED_NAME_AUTH = "auth";
  @SerializedName(SERIALIZED_NAME_AUTH)
  private Object auth;

  public static final String SERIALIZED_NAME_BEFORE_SCRIPTS = "before_scripts";
  @SerializedName(SERIALIZED_NAME_BEFORE_SCRIPTS)
  private List<String> beforeScripts = new ArrayList<>();

  public static final String SERIALIZED_NAME_BODY = "body";
  @SerializedName(SERIALIZED_NAME_BODY)
  private String body;

  public static final String SERIALIZED_NAME_FORM = "form";
  @SerializedName(SERIALIZED_NAME_FORM)
  private Object form;

  public static final String SERIALIZED_NAME_HEADERS = "headers";
  @SerializedName(SERIALIZED_NAME_HEADERS)
  private Object headers;

  public static final String SERIALIZED_NAME_METHOD = "method";
  @SerializedName(SERIALIZED_NAME_METHOD)
  private String method;

  public static final String SERIALIZED_NAME_NOTE = "note";
  @SerializedName(SERIALIZED_NAME_NOTE)
  private String note;

  public static final String SERIALIZED_NAME_SCRIPTS = "scripts";
  @SerializedName(SERIALIZED_NAME_SCRIPTS)
  private List<String> scripts = new ArrayList<>();

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public static final String SERIALIZED_NAME_VARIABLES = "variables";
  @SerializedName(SERIALIZED_NAME_VARIABLES)
  private List<Variable> variables = new ArrayList<>();

  public TestStepRequest() {
  }

  public TestStepRequest stepType(String stepType) {
    this.stepType = stepType;
    return this;
  }

  /**
   * Type of test step -- request, pause, condition, ghost-inspector, or subtest.
   * @return stepType
   */
  @javax.annotation.Nullable
  public String getStepType() {
    return stepType;
  }

  public void setStepType(String stepType) {
    this.stepType = stepType;
  }


  public TestStepRequest assertions(List<Assertion> assertions) {
    this.assertions = assertions;
    return this;
  }

  public TestStepRequest addAssertionsItem(Assertion assertionsItem) {
    if (this.assertions == null) {
      this.assertions = new ArrayList<>();
    }
    this.assertions.add(assertionsItem);
    return this;
  }

  /**
   * A list of assertions to apply to the HTTP response from this request.
   * @return assertions
   */
  @javax.annotation.Nullable
  public List<Assertion> getAssertions() {
    return assertions;
  }

  public void setAssertions(List<Assertion> assertions) {
    this.assertions = assertions;
  }


  public TestStepRequest auth(Object auth) {
    this.auth = auth;
    return this;
  }

  /**
   * An authentication object with either basic, oauth1, or client_certificate credentials for authenticating this request.
   * @return auth
   */
  @javax.annotation.Nullable
  public Object getAuth() {
    return auth;
  }

  public void setAuth(Object auth) {
    this.auth = auth;
  }


  public TestStepRequest beforeScripts(List<String> beforeScripts) {
    this.beforeScripts = beforeScripts;
    return this;
  }

  public TestStepRequest addBeforeScriptsItem(String beforeScriptsItem) {
    if (this.beforeScripts == null) {
      this.beforeScripts = new ArrayList<>();
    }
    this.beforeScripts.add(beforeScriptsItem);
    return this;
  }

  /**
   * A list of pre-request scripts to run before this request.
   * @return beforeScripts
   */
  @javax.annotation.Nullable
  public List<String> getBeforeScripts() {
    return beforeScripts;
  }

  public void setBeforeScripts(List<String> beforeScripts) {
    this.beforeScripts = beforeScripts;
  }


  public TestStepRequest body(String body) {
    this.body = body;
    return this;
  }

  /**
   * A string to use as the body of the request.
   * @return body
   */
  @javax.annotation.Nullable
  public String getBody() {
    return body;
  }

  public void setBody(String body) {
    this.body = body;
  }


  public TestStepRequest form(Object form) {
    this.form = form;
    return this;
  }

  /**
   * An object with keys as form post parameter names matched to their values. Values can either be a single string or an array of strings.
   * @return form
   */
  @javax.annotation.Nullable
  public Object getForm() {
    return form;
  }

  public void setForm(Object form) {
    this.form = form;
  }


  public TestStepRequest headers(Object headers) {
    this.headers = headers;
    return this;
  }

  /**
   * An object with keys as header names matched to their values. Values can either be a single string or an array of strings.
   * @return headers
   */
  @javax.annotation.Nullable
  public Object getHeaders() {
    return headers;
  }

  public void setHeaders(Object headers) {
    this.headers = headers;
  }


  public TestStepRequest method(String method) {
    this.method = method;
    return this;
  }

  /**
   * The HTTP method for this request step. E.g. GET, POST, PUT, DELETE, etc.
   * @return method
   */
  @javax.annotation.Nullable
  public String getMethod() {
    return method;
  }

  public void setMethod(String method) {
    this.method = method;
  }


  public TestStepRequest note(String note) {
    this.note = note;
    return this;
  }

  /**
   * A description or note for this request step.
   * @return note
   */
  @javax.annotation.Nullable
  public String getNote() {
    return note;
  }

  public void setNote(String note) {
    this.note = note;
  }


  public TestStepRequest scripts(List<String> scripts) {
    this.scripts = scripts;
    return this;
  }

  public TestStepRequest addScriptsItem(String scriptsItem) {
    if (this.scripts == null) {
      this.scripts = new ArrayList<>();
    }
    this.scripts.add(scriptsItem);
    return this;
  }

  /**
   * A list of post-response scripts to run after this request.
   * @return scripts
   */
  @javax.annotation.Nullable
  public List<String> getScripts() {
    return scripts;
  }

  public void setScripts(List<String> scripts) {
    this.scripts = scripts;
  }


  public TestStepRequest url(String url) {
    this.url = url;
    return this;
  }

  /**
   * The URL to make a request to for this step. This may contain both query string parameters and variables.
   * @return url
   */
  @javax.annotation.Nullable
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }


  public TestStepRequest variables(List<Variable> variables) {
    this.variables = variables;
    return this;
  }

  public TestStepRequest addVariablesItem(Variable variablesItem) {
    if (this.variables == null) {
      this.variables = new ArrayList<>();
    }
    this.variables.add(variablesItem);
    return this;
  }

  /**
   * A list of variables to extract out of the HTTP response from this request.
   * @return variables
   */
  @javax.annotation.Nullable
  public List<Variable> getVariables() {
    return variables;
  }

  public void setVariables(List<Variable> variables) {
    this.variables = variables;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TestStepRequest testStepRequest = (TestStepRequest) o;
    return Objects.equals(this.stepType, testStepRequest.stepType) &&
        Objects.equals(this.assertions, testStepRequest.assertions) &&
        Objects.equals(this.auth, testStepRequest.auth) &&
        Objects.equals(this.beforeScripts, testStepRequest.beforeScripts) &&
        Objects.equals(this.body, testStepRequest.body) &&
        Objects.equals(this.form, testStepRequest.form) &&
        Objects.equals(this.headers, testStepRequest.headers) &&
        Objects.equals(this.method, testStepRequest.method) &&
        Objects.equals(this.note, testStepRequest.note) &&
        Objects.equals(this.scripts, testStepRequest.scripts) &&
        Objects.equals(this.url, testStepRequest.url) &&
        Objects.equals(this.variables, testStepRequest.variables);
  }

  @Override
  public int hashCode() {
    return Objects.hash(stepType, assertions, auth, beforeScripts, body, form, headers, method, note, scripts, url, variables);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TestStepRequest {\n");
    sb.append("    stepType: ").append(toIndentedString(stepType)).append("\n");
    sb.append("    assertions: ").append(toIndentedString(assertions)).append("\n");
    sb.append("    auth: ").append(toIndentedString(auth)).append("\n");
    sb.append("    beforeScripts: ").append(toIndentedString(beforeScripts)).append("\n");
    sb.append("    body: ").append(toIndentedString(body)).append("\n");
    sb.append("    form: ").append(toIndentedString(form)).append("\n");
    sb.append("    headers: ").append(toIndentedString(headers)).append("\n");
    sb.append("    method: ").append(toIndentedString(method)).append("\n");
    sb.append("    note: ").append(toIndentedString(note)).append("\n");
    sb.append("    scripts: ").append(toIndentedString(scripts)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
    sb.append("    variables: ").append(toIndentedString(variables)).append("\n");
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
    openapiFields.add("step_type");
    openapiFields.add("assertions");
    openapiFields.add("auth");
    openapiFields.add("before_scripts");
    openapiFields.add("body");
    openapiFields.add("form");
    openapiFields.add("headers");
    openapiFields.add("method");
    openapiFields.add("note");
    openapiFields.add("scripts");
    openapiFields.add("url");
    openapiFields.add("variables");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TestStepRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TestStepRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TestStepRequest is not found in the empty JSON string", TestStepRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TestStepRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TestStepRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("step_type") != null && !jsonObj.get("step_type").isJsonNull()) && !jsonObj.get("step_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `step_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("step_type").toString()));
      }
      if (jsonObj.get("assertions") != null && !jsonObj.get("assertions").isJsonNull()) {
        JsonArray jsonArrayassertions = jsonObj.getAsJsonArray("assertions");
        if (jsonArrayassertions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("assertions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `assertions` to be an array in the JSON string but got `%s`", jsonObj.get("assertions").toString()));
          }

          // validate the optional field `assertions` (array)
          for (int i = 0; i < jsonArrayassertions.size(); i++) {
            Assertion.validateJsonElement(jsonArrayassertions.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("before_scripts") != null && !jsonObj.get("before_scripts").isJsonNull() && !jsonObj.get("before_scripts").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `before_scripts` to be an array in the JSON string but got `%s`", jsonObj.get("before_scripts").toString()));
      }
      if ((jsonObj.get("body") != null && !jsonObj.get("body").isJsonNull()) && !jsonObj.get("body").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `body` to be a primitive type in the JSON string but got `%s`", jsonObj.get("body").toString()));
      }
      if ((jsonObj.get("method") != null && !jsonObj.get("method").isJsonNull()) && !jsonObj.get("method").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `method` to be a primitive type in the JSON string but got `%s`", jsonObj.get("method").toString()));
      }
      if ((jsonObj.get("note") != null && !jsonObj.get("note").isJsonNull()) && !jsonObj.get("note").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `note` to be a primitive type in the JSON string but got `%s`", jsonObj.get("note").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("scripts") != null && !jsonObj.get("scripts").isJsonNull() && !jsonObj.get("scripts").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `scripts` to be an array in the JSON string but got `%s`", jsonObj.get("scripts").toString()));
      }
      if ((jsonObj.get("url") != null && !jsonObj.get("url").isJsonNull()) && !jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
      if (jsonObj.get("variables") != null && !jsonObj.get("variables").isJsonNull()) {
        JsonArray jsonArrayvariables = jsonObj.getAsJsonArray("variables");
        if (jsonArrayvariables != null) {
          // ensure the json data is an array
          if (!jsonObj.get("variables").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `variables` to be an array in the JSON string but got `%s`", jsonObj.get("variables").toString()));
          }

          // validate the optional field `variables` (array)
          for (int i = 0; i < jsonArrayvariables.size(); i++) {
            Variable.validateJsonElement(jsonArrayvariables.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TestStepRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TestStepRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TestStepRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TestStepRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<TestStepRequest>() {
           @Override
           public void write(JsonWriter out, TestStepRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TestStepRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TestStepRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TestStepRequest
   * @throws IOException if the JSON string is invalid with respect to TestStepRequest
   */
  public static TestStepRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TestStepRequest.class);
  }

  /**
   * Convert an instance of TestStepRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

