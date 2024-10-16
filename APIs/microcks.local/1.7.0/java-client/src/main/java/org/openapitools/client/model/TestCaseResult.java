/*
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.TestStepResult;

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
 * Companion objects for TestResult. Each TestCaseResult correspond to a particuliar service operation / action reference by the operationName field. TestCaseResults owns a collection of TestStepResults (one for every request associated to service operation / action).
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:29.619783-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TestCaseResult {
  public static final String SERIALIZED_NAME_ELAPSED_TIME = "elapsedTime";
  @SerializedName(SERIALIZED_NAME_ELAPSED_TIME)
  private BigDecimal elapsedTime;

  public static final String SERIALIZED_NAME_OPERATION_NAME = "operationName";
  @SerializedName(SERIALIZED_NAME_OPERATION_NAME)
  private String operationName;

  public static final String SERIALIZED_NAME_SUCCESS = "success";
  @SerializedName(SERIALIZED_NAME_SUCCESS)
  private Boolean success;

  public static final String SERIALIZED_NAME_TEST_STEP_RESULTS = "testStepResults";
  @SerializedName(SERIALIZED_NAME_TEST_STEP_RESULTS)
  private List<TestStepResult> testStepResults = new ArrayList<>();

  public TestCaseResult() {
  }

  public TestCaseResult elapsedTime(BigDecimal elapsedTime) {
    this.elapsedTime = elapsedTime;
    return this;
  }

  /**
   * Elapsed time in milliseconds since the test case beginning
   * @return elapsedTime
   */
  @javax.annotation.Nonnull
  public BigDecimal getElapsedTime() {
    return elapsedTime;
  }

  public void setElapsedTime(BigDecimal elapsedTime) {
    this.elapsedTime = elapsedTime;
  }


  public TestCaseResult operationName(String operationName) {
    this.operationName = operationName;
    return this;
  }

  /**
   * Name of operation this test case is bound to
   * @return operationName
   */
  @javax.annotation.Nonnull
  public String getOperationName() {
    return operationName;
  }

  public void setOperationName(String operationName) {
    this.operationName = operationName;
  }


  public TestCaseResult success(Boolean success) {
    this.success = success;
    return this;
  }

  /**
   * Flag telling if test case is a success
   * @return success
   */
  @javax.annotation.Nonnull
  public Boolean getSuccess() {
    return success;
  }

  public void setSuccess(Boolean success) {
    this.success = success;
  }


  public TestCaseResult testStepResults(List<TestStepResult> testStepResults) {
    this.testStepResults = testStepResults;
    return this;
  }

  public TestCaseResult addTestStepResultsItem(TestStepResult testStepResultsItem) {
    if (this.testStepResults == null) {
      this.testStepResults = new ArrayList<>();
    }
    this.testStepResults.add(testStepResultsItem);
    return this;
  }

  /**
   * Test steps associated to this test case
   * @return testStepResults
   */
  @javax.annotation.Nullable
  public List<TestStepResult> getTestStepResults() {
    return testStepResults;
  }

  public void setTestStepResults(List<TestStepResult> testStepResults) {
    this.testStepResults = testStepResults;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TestCaseResult testCaseResult = (TestCaseResult) o;
    return Objects.equals(this.elapsedTime, testCaseResult.elapsedTime) &&
        Objects.equals(this.operationName, testCaseResult.operationName) &&
        Objects.equals(this.success, testCaseResult.success) &&
        Objects.equals(this.testStepResults, testCaseResult.testStepResults);
  }

  @Override
  public int hashCode() {
    return Objects.hash(elapsedTime, operationName, success, testStepResults);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TestCaseResult {\n");
    sb.append("    elapsedTime: ").append(toIndentedString(elapsedTime)).append("\n");
    sb.append("    operationName: ").append(toIndentedString(operationName)).append("\n");
    sb.append("    success: ").append(toIndentedString(success)).append("\n");
    sb.append("    testStepResults: ").append(toIndentedString(testStepResults)).append("\n");
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
    openapiFields.add("elapsedTime");
    openapiFields.add("operationName");
    openapiFields.add("success");
    openapiFields.add("testStepResults");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("elapsedTime");
    openapiRequiredFields.add("operationName");
    openapiRequiredFields.add("success");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TestCaseResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TestCaseResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TestCaseResult is not found in the empty JSON string", TestCaseResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TestCaseResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TestCaseResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : TestCaseResult.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("operationName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `operationName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("operationName").toString()));
      }
      if (jsonObj.get("testStepResults") != null && !jsonObj.get("testStepResults").isJsonNull()) {
        JsonArray jsonArraytestStepResults = jsonObj.getAsJsonArray("testStepResults");
        if (jsonArraytestStepResults != null) {
          // ensure the json data is an array
          if (!jsonObj.get("testStepResults").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `testStepResults` to be an array in the JSON string but got `%s`", jsonObj.get("testStepResults").toString()));
          }

          // validate the optional field `testStepResults` (array)
          for (int i = 0; i < jsonArraytestStepResults.size(); i++) {
            TestStepResult.validateJsonElement(jsonArraytestStepResults.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TestCaseResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TestCaseResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TestCaseResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TestCaseResult.class));

       return (TypeAdapter<T>) new TypeAdapter<TestCaseResult>() {
           @Override
           public void write(JsonWriter out, TestCaseResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TestCaseResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TestCaseResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TestCaseResult
   * @throws IOException if the JSON string is invalid with respect to TestCaseResult
   */
  public static TestCaseResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TestCaseResult.class);
  }

  /**
   * Convert an instance of TestCaseResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

