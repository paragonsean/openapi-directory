/*
 * OpenFEC
 * This application programming interface (API) allows you to explore the way candidates and committees fund their campaigns.    The Federal Election Commission (FEC) API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There are a lot of data, and a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in the `/schedule_a/` endpoints.    <b class=\"body\" id=\"getting_started_head\">Getting started with the openFEC API</b><br>    If you would like to use the FEC's API programmatically, you can sign up for your own API key using our form. Alternatively, you can still try out our API without an API key by using the web interface and using DEMO_KEY. Note that when you use the openFEC API you are subject to the [Terms of Service](https://github.com/fecgov/FEC/blob/master/TERMS-OF-SERVICE.md) and [Acceptable Use policy](https://github.com/fecgov/FEC/blob/master/ACCEPTABLE-USE-POLICY.md).    Signing up for an API key will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 7,200 calls an hour (120 calls per minute) to <a href=\"mailto:APIinfo@fec.gov\">APIinfo@fec.gov</a>. You can also ask questions and discuss the data in a community led [group](https://groups.google.com/forum/#!forum/fec-data).    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [Inspect our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!    <p><br></p> <h2 class=\"title\" id=\"signup_head\">Sign up for an API key</h2> <div id=\"apidatagov_signup\">Loading signup form...</div>
 *
 * The version of the OpenAPI document: 1.0
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
import java.math.BigDecimal;
import java.util.Arrays;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * ElectioneeringByCandidate
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:12.812386-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ElectioneeringByCandidate {
  public static final String SERIALIZED_NAME_CANDIDATE = "candidate";
  @SerializedName(SERIALIZED_NAME_CANDIDATE)
  private String candidate;

  public static final String SERIALIZED_NAME_CANDIDATE_ID = "candidate_id";
  @SerializedName(SERIALIZED_NAME_CANDIDATE_ID)
  private String candidateId;

  public static final String SERIALIZED_NAME_CANDIDATE_NAME = "candidate_name";
  @SerializedName(SERIALIZED_NAME_CANDIDATE_NAME)
  private String candidateName;

  public static final String SERIALIZED_NAME_COMMITTEE = "committee";
  @SerializedName(SERIALIZED_NAME_COMMITTEE)
  private String committee;

  public static final String SERIALIZED_NAME_COMMITTEE_ID = "committee_id";
  @SerializedName(SERIALIZED_NAME_COMMITTEE_ID)
  private String committeeId;

  public static final String SERIALIZED_NAME_COMMITTEE_NAME = "committee_name";
  @SerializedName(SERIALIZED_NAME_COMMITTEE_NAME)
  private String committeeName;

  public static final String SERIALIZED_NAME_COUNT = "count";
  @SerializedName(SERIALIZED_NAME_COUNT)
  private Integer count;

  public static final String SERIALIZED_NAME_CYCLE = "cycle";
  @SerializedName(SERIALIZED_NAME_CYCLE)
  private Integer cycle;

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private BigDecimal total;

  public ElectioneeringByCandidate() {
  }

  public ElectioneeringByCandidate candidate(String candidate) {
    this.candidate = candidate;
    return this;
  }

  /**
   * Get candidate
   * @return candidate
   */
  @javax.annotation.Nullable
  public String getCandidate() {
    return candidate;
  }

  public void setCandidate(String candidate) {
    this.candidate = candidate;
  }


  public ElectioneeringByCandidate candidateId(String candidateId) {
    this.candidateId = candidateId;
    return this;
  }

  /**
   * Get candidateId
   * @return candidateId
   */
  @javax.annotation.Nullable
  public String getCandidateId() {
    return candidateId;
  }

  public void setCandidateId(String candidateId) {
    this.candidateId = candidateId;
  }


  public ElectioneeringByCandidate candidateName(String candidateName) {
    this.candidateName = candidateName;
    return this;
  }

  /**
   * Get candidateName
   * @return candidateName
   */
  @javax.annotation.Nullable
  public String getCandidateName() {
    return candidateName;
  }

  public void setCandidateName(String candidateName) {
    this.candidateName = candidateName;
  }


  public ElectioneeringByCandidate committee(String committee) {
    this.committee = committee;
    return this;
  }

  /**
   * Get committee
   * @return committee
   */
  @javax.annotation.Nullable
  public String getCommittee() {
    return committee;
  }

  public void setCommittee(String committee) {
    this.committee = committee;
  }


  public ElectioneeringByCandidate committeeId(String committeeId) {
    this.committeeId = committeeId;
    return this;
  }

  /**
   * Get committeeId
   * @return committeeId
   */
  @javax.annotation.Nullable
  public String getCommitteeId() {
    return committeeId;
  }

  public void setCommitteeId(String committeeId) {
    this.committeeId = committeeId;
  }


  public ElectioneeringByCandidate committeeName(String committeeName) {
    this.committeeName = committeeName;
    return this;
  }

  /**
   * Get committeeName
   * @return committeeName
   */
  @javax.annotation.Nullable
  public String getCommitteeName() {
    return committeeName;
  }

  public void setCommitteeName(String committeeName) {
    this.committeeName = committeeName;
  }


  public ElectioneeringByCandidate count(Integer count) {
    this.count = count;
    return this;
  }

  /**
   * Get count
   * @return count
   */
  @javax.annotation.Nullable
  public Integer getCount() {
    return count;
  }

  public void setCount(Integer count) {
    this.count = count;
  }


  public ElectioneeringByCandidate cycle(Integer cycle) {
    this.cycle = cycle;
    return this;
  }

  /**
   * Get cycle
   * @return cycle
   */
  @javax.annotation.Nullable
  public Integer getCycle() {
    return cycle;
  }

  public void setCycle(Integer cycle) {
    this.cycle = cycle;
  }


  public ElectioneeringByCandidate total(BigDecimal total) {
    this.total = total;
    return this;
  }

  /**
   * Get total
   * @return total
   */
  @javax.annotation.Nullable
  public BigDecimal getTotal() {
    return total;
  }

  public void setTotal(BigDecimal total) {
    this.total = total;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ElectioneeringByCandidate electioneeringByCandidate = (ElectioneeringByCandidate) o;
    return Objects.equals(this.candidate, electioneeringByCandidate.candidate) &&
        Objects.equals(this.candidateId, electioneeringByCandidate.candidateId) &&
        Objects.equals(this.candidateName, electioneeringByCandidate.candidateName) &&
        Objects.equals(this.committee, electioneeringByCandidate.committee) &&
        Objects.equals(this.committeeId, electioneeringByCandidate.committeeId) &&
        Objects.equals(this.committeeName, electioneeringByCandidate.committeeName) &&
        Objects.equals(this.count, electioneeringByCandidate.count) &&
        Objects.equals(this.cycle, electioneeringByCandidate.cycle) &&
        Objects.equals(this.total, electioneeringByCandidate.total);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(candidate, candidateId, candidateName, committee, committeeId, committeeName, count, cycle, total);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ElectioneeringByCandidate {\n");
    sb.append("    candidate: ").append(toIndentedString(candidate)).append("\n");
    sb.append("    candidateId: ").append(toIndentedString(candidateId)).append("\n");
    sb.append("    candidateName: ").append(toIndentedString(candidateName)).append("\n");
    sb.append("    committee: ").append(toIndentedString(committee)).append("\n");
    sb.append("    committeeId: ").append(toIndentedString(committeeId)).append("\n");
    sb.append("    committeeName: ").append(toIndentedString(committeeName)).append("\n");
    sb.append("    count: ").append(toIndentedString(count)).append("\n");
    sb.append("    cycle: ").append(toIndentedString(cycle)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
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
    openapiFields.add("candidate");
    openapiFields.add("candidate_id");
    openapiFields.add("candidate_name");
    openapiFields.add("committee");
    openapiFields.add("committee_id");
    openapiFields.add("committee_name");
    openapiFields.add("count");
    openapiFields.add("cycle");
    openapiFields.add("total");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ElectioneeringByCandidate
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ElectioneeringByCandidate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ElectioneeringByCandidate is not found in the empty JSON string", ElectioneeringByCandidate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ElectioneeringByCandidate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ElectioneeringByCandidate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("candidate") != null && !jsonObj.get("candidate").isJsonNull()) && !jsonObj.get("candidate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `candidate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("candidate").toString()));
      }
      if ((jsonObj.get("candidate_id") != null && !jsonObj.get("candidate_id").isJsonNull()) && !jsonObj.get("candidate_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `candidate_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("candidate_id").toString()));
      }
      if ((jsonObj.get("candidate_name") != null && !jsonObj.get("candidate_name").isJsonNull()) && !jsonObj.get("candidate_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `candidate_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("candidate_name").toString()));
      }
      if ((jsonObj.get("committee") != null && !jsonObj.get("committee").isJsonNull()) && !jsonObj.get("committee").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `committee` to be a primitive type in the JSON string but got `%s`", jsonObj.get("committee").toString()));
      }
      if ((jsonObj.get("committee_id") != null && !jsonObj.get("committee_id").isJsonNull()) && !jsonObj.get("committee_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `committee_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("committee_id").toString()));
      }
      if ((jsonObj.get("committee_name") != null && !jsonObj.get("committee_name").isJsonNull()) && !jsonObj.get("committee_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `committee_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("committee_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ElectioneeringByCandidate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ElectioneeringByCandidate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ElectioneeringByCandidate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ElectioneeringByCandidate.class));

       return (TypeAdapter<T>) new TypeAdapter<ElectioneeringByCandidate>() {
           @Override
           public void write(JsonWriter out, ElectioneeringByCandidate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ElectioneeringByCandidate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ElectioneeringByCandidate given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ElectioneeringByCandidate
   * @throws IOException if the JSON string is invalid with respect to ElectioneeringByCandidate
   */
  public static ElectioneeringByCandidate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ElectioneeringByCandidate.class);
  }

  /**
   * Convert an instance of ElectioneeringByCandidate to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

