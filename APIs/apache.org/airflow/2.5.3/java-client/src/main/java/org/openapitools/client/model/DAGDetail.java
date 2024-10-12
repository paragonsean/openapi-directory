/*
 * Airflow API (Stable)
 * # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executing via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"name\": \"string\",     \"slots\": 0,     \"occupied_slots\": 0,     \"used_slots\": 0,     \"queued_slots\": 0,     \"open_slots\": 0 } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backends` command as in the example below. ```bash $ airflow config get-value api auth_backends airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, e.g. the resource it tries to create already exists.  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request. 
 *
 * The version of the OpenAPI document: 2.5.3
 * Contact: dev@airflow.apache.org
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ScheduleInterval;
import org.openapitools.client.model.Tag;
import org.openapitools.client.model.TimeDelta;
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
 * DAG details.  For details see: [airflow.models.DAG](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/index.html#airflow.models.DAG) 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:57:16.959637-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DAGDetail {
  public static final String SERIALIZED_NAME_DAG_ID = "dag_id";
  @SerializedName(SERIALIZED_NAME_DAG_ID)
  private String dagId;

  public static final String SERIALIZED_NAME_DEFAULT_VIEW = "default_view";
  @SerializedName(SERIALIZED_NAME_DEFAULT_VIEW)
  private String defaultView;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_FILE_TOKEN = "file_token";
  @SerializedName(SERIALIZED_NAME_FILE_TOKEN)
  private String fileToken;

  public static final String SERIALIZED_NAME_FILELOC = "fileloc";
  @SerializedName(SERIALIZED_NAME_FILELOC)
  private String fileloc;

  public static final String SERIALIZED_NAME_HAS_IMPORT_ERRORS = "has_import_errors";
  @SerializedName(SERIALIZED_NAME_HAS_IMPORT_ERRORS)
  private Boolean hasImportErrors;

  public static final String SERIALIZED_NAME_HAS_TASK_CONCURRENCY_LIMITS = "has_task_concurrency_limits";
  @SerializedName(SERIALIZED_NAME_HAS_TASK_CONCURRENCY_LIMITS)
  private Boolean hasTaskConcurrencyLimits;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "is_active";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_IS_PAUSED = "is_paused";
  @SerializedName(SERIALIZED_NAME_IS_PAUSED)
  private Boolean isPaused;

  public static final String SERIALIZED_NAME_IS_SUBDAG = "is_subdag";
  @SerializedName(SERIALIZED_NAME_IS_SUBDAG)
  private Boolean isSubdag;

  public static final String SERIALIZED_NAME_LAST_EXPIRED = "last_expired";
  @SerializedName(SERIALIZED_NAME_LAST_EXPIRED)
  private OffsetDateTime lastExpired;

  public static final String SERIALIZED_NAME_LAST_PARSED_TIME = "last_parsed_time";
  @SerializedName(SERIALIZED_NAME_LAST_PARSED_TIME)
  private OffsetDateTime lastParsedTime;

  public static final String SERIALIZED_NAME_LAST_PICKLED = "last_pickled";
  @SerializedName(SERIALIZED_NAME_LAST_PICKLED)
  private OffsetDateTime lastPickled;

  public static final String SERIALIZED_NAME_MAX_ACTIVE_RUNS = "max_active_runs";
  @SerializedName(SERIALIZED_NAME_MAX_ACTIVE_RUNS)
  private Integer maxActiveRuns;

  public static final String SERIALIZED_NAME_MAX_ACTIVE_TASKS = "max_active_tasks";
  @SerializedName(SERIALIZED_NAME_MAX_ACTIVE_TASKS)
  private Integer maxActiveTasks;

  public static final String SERIALIZED_NAME_NEXT_DAGRUN = "next_dagrun";
  @SerializedName(SERIALIZED_NAME_NEXT_DAGRUN)
  private OffsetDateTime nextDagrun;

  public static final String SERIALIZED_NAME_NEXT_DAGRUN_CREATE_AFTER = "next_dagrun_create_after";
  @SerializedName(SERIALIZED_NAME_NEXT_DAGRUN_CREATE_AFTER)
  private OffsetDateTime nextDagrunCreateAfter;

  public static final String SERIALIZED_NAME_NEXT_DAGRUN_DATA_INTERVAL_END = "next_dagrun_data_interval_end";
  @SerializedName(SERIALIZED_NAME_NEXT_DAGRUN_DATA_INTERVAL_END)
  private OffsetDateTime nextDagrunDataIntervalEnd;

  public static final String SERIALIZED_NAME_NEXT_DAGRUN_DATA_INTERVAL_START = "next_dagrun_data_interval_start";
  @SerializedName(SERIALIZED_NAME_NEXT_DAGRUN_DATA_INTERVAL_START)
  private OffsetDateTime nextDagrunDataIntervalStart;

  public static final String SERIALIZED_NAME_OWNERS = "owners";
  @SerializedName(SERIALIZED_NAME_OWNERS)
  private List<String> owners = new ArrayList<>();

  public static final String SERIALIZED_NAME_PICKLE_ID = "pickle_id";
  @SerializedName(SERIALIZED_NAME_PICKLE_ID)
  private String pickleId;

  public static final String SERIALIZED_NAME_ROOT_DAG_ID = "root_dag_id";
  @SerializedName(SERIALIZED_NAME_ROOT_DAG_ID)
  private String rootDagId;

  public static final String SERIALIZED_NAME_SCHEDULE_INTERVAL = "schedule_interval";
  @SerializedName(SERIALIZED_NAME_SCHEDULE_INTERVAL)
  private ScheduleInterval scheduleInterval;

  public static final String SERIALIZED_NAME_SCHEDULER_LOCK = "scheduler_lock";
  @SerializedName(SERIALIZED_NAME_SCHEDULER_LOCK)
  private Boolean schedulerLock;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<Tag> tags;

  public static final String SERIALIZED_NAME_TIMETABLE_DESCRIPTION = "timetable_description";
  @SerializedName(SERIALIZED_NAME_TIMETABLE_DESCRIPTION)
  private String timetableDescription;

  public static final String SERIALIZED_NAME_CATCHUP = "catchup";
  @SerializedName(SERIALIZED_NAME_CATCHUP)
  private Boolean catchup;

  public static final String SERIALIZED_NAME_CONCURRENCY = "concurrency";
  @SerializedName(SERIALIZED_NAME_CONCURRENCY)
  private BigDecimal concurrency;

  public static final String SERIALIZED_NAME_DAG_RUN_TIMEOUT = "dag_run_timeout";
  @SerializedName(SERIALIZED_NAME_DAG_RUN_TIMEOUT)
  private TimeDelta dagRunTimeout;

  public static final String SERIALIZED_NAME_DOC_MD = "doc_md";
  @SerializedName(SERIALIZED_NAME_DOC_MD)
  private String docMd;

  public static final String SERIALIZED_NAME_END_DATE = "end_date";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private OffsetDateTime endDate;

  public static final String SERIALIZED_NAME_IS_PAUSED_UPON_CREATION = "is_paused_upon_creation";
  @SerializedName(SERIALIZED_NAME_IS_PAUSED_UPON_CREATION)
  private Boolean isPausedUponCreation;

  public static final String SERIALIZED_NAME_LAST_PARSED = "last_parsed";
  @SerializedName(SERIALIZED_NAME_LAST_PARSED)
  private OffsetDateTime lastParsed;

  public static final String SERIALIZED_NAME_ORIENTATION = "orientation";
  @SerializedName(SERIALIZED_NAME_ORIENTATION)
  private String orientation;

  public static final String SERIALIZED_NAME_PARAMS = "params";
  @SerializedName(SERIALIZED_NAME_PARAMS)
  private Object params;

  public static final String SERIALIZED_NAME_RENDER_TEMPLATE_AS_NATIVE_OBJ = "render_template_as_native_obj";
  @SerializedName(SERIALIZED_NAME_RENDER_TEMPLATE_AS_NATIVE_OBJ)
  private Boolean renderTemplateAsNativeObj;

  public static final String SERIALIZED_NAME_START_DATE = "start_date";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private OffsetDateTime startDate;

  public static final String SERIALIZED_NAME_TEMPLATE_SEARCH_PATH = "template_search_path";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_SEARCH_PATH)
  private List<String> templateSearchPath;

  public static final String SERIALIZED_NAME_TIMEZONE = "timezone";
  @SerializedName(SERIALIZED_NAME_TIMEZONE)
  private String timezone;

  public DAGDetail() {
  }

  public DAGDetail(
     String dagId, 
     String defaultView, 
     String description, 
     String fileToken, 
     String fileloc, 
     Boolean hasImportErrors, 
     Boolean hasTaskConcurrencyLimits, 
     Boolean isActive, 
     Boolean isSubdag, 
     OffsetDateTime lastExpired, 
     OffsetDateTime lastParsedTime, 
     OffsetDateTime lastPickled, 
     Integer maxActiveRuns, 
     Integer maxActiveTasks, 
     OffsetDateTime nextDagrun, 
     OffsetDateTime nextDagrunCreateAfter, 
     OffsetDateTime nextDagrunDataIntervalEnd, 
     OffsetDateTime nextDagrunDataIntervalStart, 
     List<String> owners, 
     String pickleId, 
     String rootDagId, 
     Boolean schedulerLock, 
     List<Tag> tags, 
     String timetableDescription, 
     Boolean catchup, 
     BigDecimal concurrency, 
     String docMd, 
     OffsetDateTime endDate, 
     Boolean isPausedUponCreation, 
     OffsetDateTime lastParsed, 
     String orientation, 
     Object params, 
     Boolean renderTemplateAsNativeObj, 
     OffsetDateTime startDate
  ) {
    this();
    this.dagId = dagId;
    this.defaultView = defaultView;
    this.description = description;
    this.fileToken = fileToken;
    this.fileloc = fileloc;
    this.hasImportErrors = hasImportErrors;
    this.hasTaskConcurrencyLimits = hasTaskConcurrencyLimits;
    this.isActive = isActive;
    this.isSubdag = isSubdag;
    this.lastExpired = lastExpired;
    this.lastParsedTime = lastParsedTime;
    this.lastPickled = lastPickled;
    this.maxActiveRuns = maxActiveRuns;
    this.maxActiveTasks = maxActiveTasks;
    this.nextDagrun = nextDagrun;
    this.nextDagrunCreateAfter = nextDagrunCreateAfter;
    this.nextDagrunDataIntervalEnd = nextDagrunDataIntervalEnd;
    this.nextDagrunDataIntervalStart = nextDagrunDataIntervalStart;
    this.owners = owners;
    this.pickleId = pickleId;
    this.rootDagId = rootDagId;
    this.schedulerLock = schedulerLock;
    this.tags = tags;
    this.timetableDescription = timetableDescription;
    this.catchup = catchup;
    this.concurrency = concurrency;
    this.docMd = docMd;
    this.endDate = endDate;
    this.isPausedUponCreation = isPausedUponCreation;
    this.lastParsed = lastParsed;
    this.orientation = orientation;
    this.params = params;
    this.renderTemplateAsNativeObj = renderTemplateAsNativeObj;
    this.startDate = startDate;
  }

  /**
   * The ID of the DAG.
   * @return dagId
   */
  @javax.annotation.Nullable
  public String getDagId() {
    return dagId;
  }



  /**
   * Get defaultView
   * @return defaultView
   */
  @javax.annotation.Nullable
  public String getDefaultView() {
    return defaultView;
  }



  /**
   * User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents. 
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }



  /**
   * The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change. 
   * @return fileToken
   */
  @javax.annotation.Nullable
  public String getFileToken() {
    return fileToken;
  }



  /**
   * The absolute path to the file.
   * @return fileloc
   */
  @javax.annotation.Nullable
  public String getFileloc() {
    return fileloc;
  }



  /**
   * Whether the DAG has import errors  *New in version 2.3.0* 
   * @return hasImportErrors
   */
  @javax.annotation.Nullable
  public Boolean getHasImportErrors() {
    return hasImportErrors;
  }



  /**
   * Whether the DAG has task concurrency limits  *New in version 2.3.0* 
   * @return hasTaskConcurrencyLimits
   */
  @javax.annotation.Nullable
  public Boolean getHasTaskConcurrencyLimits() {
    return hasTaskConcurrencyLimits;
  }



  /**
   * Whether the DAG is currently seen by the scheduler(s).  *New in version 2.1.1*  *Changed in version 2.2.0*&amp;#58; Field is read-only. 
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }



  public DAGDetail isPaused(Boolean isPaused) {
    this.isPaused = isPaused;
    return this;
  }

  /**
   * Whether the DAG is paused.
   * @return isPaused
   */
  @javax.annotation.Nullable
  public Boolean getIsPaused() {
    return isPaused;
  }

  public void setIsPaused(Boolean isPaused) {
    this.isPaused = isPaused;
  }


  /**
   * Whether the DAG is SubDAG.
   * @return isSubdag
   */
  @javax.annotation.Nullable
  public Boolean getIsSubdag() {
    return isSubdag;
  }



  /**
   * Time when the DAG last received a refresh signal (e.g. the DAG&#39;s \&quot;refresh\&quot; button was clicked in the web UI)  *New in version 2.3.0* 
   * @return lastExpired
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastExpired() {
    return lastExpired;
  }



  /**
   * The last time the DAG was parsed.  *New in version 2.3.0* 
   * @return lastParsedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastParsedTime() {
    return lastParsedTime;
  }



  /**
   * The last time the DAG was pickled.  *New in version 2.3.0* 
   * @return lastPickled
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastPickled() {
    return lastPickled;
  }



  /**
   * Maximum number of active DAG runs for the DAG  *New in version 2.3.0* 
   * @return maxActiveRuns
   */
  @javax.annotation.Nullable
  public Integer getMaxActiveRuns() {
    return maxActiveRuns;
  }



  /**
   * Maximum number of active tasks that can be run on the DAG  *New in version 2.3.0* 
   * @return maxActiveTasks
   */
  @javax.annotation.Nullable
  public Integer getMaxActiveTasks() {
    return maxActiveTasks;
  }



  /**
   * The logical date of the next dag run.  *New in version 2.3.0* 
   * @return nextDagrun
   */
  @javax.annotation.Nullable
  public OffsetDateTime getNextDagrun() {
    return nextDagrun;
  }



  /**
   * Earliest time at which this &#x60;&#x60;next_dagrun&#x60;&#x60; can be created.  *New in version 2.3.0* 
   * @return nextDagrunCreateAfter
   */
  @javax.annotation.Nullable
  public OffsetDateTime getNextDagrunCreateAfter() {
    return nextDagrunCreateAfter;
  }



  /**
   * The end of the interval of the next dag run.  *New in version 2.3.0* 
   * @return nextDagrunDataIntervalEnd
   */
  @javax.annotation.Nullable
  public OffsetDateTime getNextDagrunDataIntervalEnd() {
    return nextDagrunDataIntervalEnd;
  }



  /**
   * The start of the interval of the next dag run.  *New in version 2.3.0* 
   * @return nextDagrunDataIntervalStart
   */
  @javax.annotation.Nullable
  public OffsetDateTime getNextDagrunDataIntervalStart() {
    return nextDagrunDataIntervalStart;
  }



  /**
   * Get owners
   * @return owners
   */
  @javax.annotation.Nullable
  public List<String> getOwners() {
    return owners;
  }



  /**
   * Foreign key to the latest pickle_id  *New in version 2.3.0* 
   * @return pickleId
   */
  @javax.annotation.Nullable
  public String getPickleId() {
    return pickleId;
  }



  /**
   * If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.
   * @return rootDagId
   */
  @javax.annotation.Nullable
  public String getRootDagId() {
    return rootDagId;
  }



  public DAGDetail scheduleInterval(ScheduleInterval scheduleInterval) {
    this.scheduleInterval = scheduleInterval;
    return this;
  }

  /**
   * Get scheduleInterval
   * @return scheduleInterval
   */
  @javax.annotation.Nullable
  public ScheduleInterval getScheduleInterval() {
    return scheduleInterval;
  }

  public void setScheduleInterval(ScheduleInterval scheduleInterval) {
    this.scheduleInterval = scheduleInterval;
  }


  /**
   * Whether (one of) the scheduler is scheduling this DAG at the moment  *New in version 2.3.0* 
   * @return schedulerLock
   */
  @javax.annotation.Nullable
  public Boolean getSchedulerLock() {
    return schedulerLock;
  }



  /**
   * List of tags.
   * @return tags
   */
  @javax.annotation.Nullable
  public List<Tag> getTags() {
    return tags;
  }



  /**
   * Timetable/Schedule Interval description.  *New in version 2.3.0* 
   * @return timetableDescription
   */
  @javax.annotation.Nullable
  public String getTimetableDescription() {
    return timetableDescription;
  }



  /**
   * Get catchup
   * @return catchup
   */
  @javax.annotation.Nullable
  public Boolean getCatchup() {
    return catchup;
  }



  /**
   * Get concurrency
   * @return concurrency
   */
  @javax.annotation.Nullable
  public BigDecimal getConcurrency() {
    return concurrency;
  }



  public DAGDetail dagRunTimeout(TimeDelta dagRunTimeout) {
    this.dagRunTimeout = dagRunTimeout;
    return this;
  }

  /**
   * Get dagRunTimeout
   * @return dagRunTimeout
   */
  @javax.annotation.Nullable
  public TimeDelta getDagRunTimeout() {
    return dagRunTimeout;
  }

  public void setDagRunTimeout(TimeDelta dagRunTimeout) {
    this.dagRunTimeout = dagRunTimeout;
  }


  /**
   * Get docMd
   * @return docMd
   */
  @javax.annotation.Nullable
  public String getDocMd() {
    return docMd;
  }



  /**
   * The DAG&#39;s end date.  *New in version 2.3.0*. 
   * @return endDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEndDate() {
    return endDate;
  }



  /**
   * Whether the DAG is paused upon creation.  *New in version 2.3.0* 
   * @return isPausedUponCreation
   */
  @javax.annotation.Nullable
  public Boolean getIsPausedUponCreation() {
    return isPausedUponCreation;
  }



  /**
   * The last time the DAG was parsed.  *New in version 2.3.0* 
   * @return lastParsed
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastParsed() {
    return lastParsed;
  }



  /**
   * Get orientation
   * @return orientation
   */
  @javax.annotation.Nullable
  public String getOrientation() {
    return orientation;
  }



  /**
   * User-specified DAG params.  *New in version 2.0.1* 
   * @return params
   */
  @javax.annotation.Nullable
  public Object getParams() {
    return params;
  }



  /**
   * Whether to render templates as native Python objects.  *New in version 2.3.0* 
   * @return renderTemplateAsNativeObj
   */
  @javax.annotation.Nullable
  public Boolean getRenderTemplateAsNativeObj() {
    return renderTemplateAsNativeObj;
  }



  /**
   * The DAG&#39;s start date.  *Changed in version 2.0.1*&amp;#58; Field becomes nullable. 
   * @return startDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStartDate() {
    return startDate;
  }



  public DAGDetail templateSearchPath(List<String> templateSearchPath) {
    this.templateSearchPath = templateSearchPath;
    return this;
  }

  public DAGDetail addTemplateSearchPathItem(String templateSearchPathItem) {
    if (this.templateSearchPath == null) {
      this.templateSearchPath = new ArrayList<>();
    }
    this.templateSearchPath.add(templateSearchPathItem);
    return this;
  }

  /**
   * The template search path.  *New in version 2.3.0* 
   * @return templateSearchPath
   */
  @javax.annotation.Nullable
  public List<String> getTemplateSearchPath() {
    return templateSearchPath;
  }

  public void setTemplateSearchPath(List<String> templateSearchPath) {
    this.templateSearchPath = templateSearchPath;
  }


  public DAGDetail timezone(String timezone) {
    this.timezone = timezone;
    return this;
  }

  /**
   * Get timezone
   * @return timezone
   */
  @javax.annotation.Nullable
  public String getTimezone() {
    return timezone;
  }

  public void setTimezone(String timezone) {
    this.timezone = timezone;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DAGDetail daGDetail = (DAGDetail) o;
    return Objects.equals(this.dagId, daGDetail.dagId) &&
        Objects.equals(this.defaultView, daGDetail.defaultView) &&
        Objects.equals(this.description, daGDetail.description) &&
        Objects.equals(this.fileToken, daGDetail.fileToken) &&
        Objects.equals(this.fileloc, daGDetail.fileloc) &&
        Objects.equals(this.hasImportErrors, daGDetail.hasImportErrors) &&
        Objects.equals(this.hasTaskConcurrencyLimits, daGDetail.hasTaskConcurrencyLimits) &&
        Objects.equals(this.isActive, daGDetail.isActive) &&
        Objects.equals(this.isPaused, daGDetail.isPaused) &&
        Objects.equals(this.isSubdag, daGDetail.isSubdag) &&
        Objects.equals(this.lastExpired, daGDetail.lastExpired) &&
        Objects.equals(this.lastParsedTime, daGDetail.lastParsedTime) &&
        Objects.equals(this.lastPickled, daGDetail.lastPickled) &&
        Objects.equals(this.maxActiveRuns, daGDetail.maxActiveRuns) &&
        Objects.equals(this.maxActiveTasks, daGDetail.maxActiveTasks) &&
        Objects.equals(this.nextDagrun, daGDetail.nextDagrun) &&
        Objects.equals(this.nextDagrunCreateAfter, daGDetail.nextDagrunCreateAfter) &&
        Objects.equals(this.nextDagrunDataIntervalEnd, daGDetail.nextDagrunDataIntervalEnd) &&
        Objects.equals(this.nextDagrunDataIntervalStart, daGDetail.nextDagrunDataIntervalStart) &&
        Objects.equals(this.owners, daGDetail.owners) &&
        Objects.equals(this.pickleId, daGDetail.pickleId) &&
        Objects.equals(this.rootDagId, daGDetail.rootDagId) &&
        Objects.equals(this.scheduleInterval, daGDetail.scheduleInterval) &&
        Objects.equals(this.schedulerLock, daGDetail.schedulerLock) &&
        Objects.equals(this.tags, daGDetail.tags) &&
        Objects.equals(this.timetableDescription, daGDetail.timetableDescription) &&
        Objects.equals(this.catchup, daGDetail.catchup) &&
        Objects.equals(this.concurrency, daGDetail.concurrency) &&
        Objects.equals(this.dagRunTimeout, daGDetail.dagRunTimeout) &&
        Objects.equals(this.docMd, daGDetail.docMd) &&
        Objects.equals(this.endDate, daGDetail.endDate) &&
        Objects.equals(this.isPausedUponCreation, daGDetail.isPausedUponCreation) &&
        Objects.equals(this.lastParsed, daGDetail.lastParsed) &&
        Objects.equals(this.orientation, daGDetail.orientation) &&
        Objects.equals(this.params, daGDetail.params) &&
        Objects.equals(this.renderTemplateAsNativeObj, daGDetail.renderTemplateAsNativeObj) &&
        Objects.equals(this.startDate, daGDetail.startDate) &&
        Objects.equals(this.templateSearchPath, daGDetail.templateSearchPath) &&
        Objects.equals(this.timezone, daGDetail.timezone);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(dagId, defaultView, description, fileToken, fileloc, hasImportErrors, hasTaskConcurrencyLimits, isActive, isPaused, isSubdag, lastExpired, lastParsedTime, lastPickled, maxActiveRuns, maxActiveTasks, nextDagrun, nextDagrunCreateAfter, nextDagrunDataIntervalEnd, nextDagrunDataIntervalStart, owners, pickleId, rootDagId, scheduleInterval, schedulerLock, tags, timetableDescription, catchup, concurrency, dagRunTimeout, docMd, endDate, isPausedUponCreation, lastParsed, orientation, params, renderTemplateAsNativeObj, startDate, templateSearchPath, timezone);
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
    sb.append("class DAGDetail {\n");
    sb.append("    dagId: ").append(toIndentedString(dagId)).append("\n");
    sb.append("    defaultView: ").append(toIndentedString(defaultView)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    fileToken: ").append(toIndentedString(fileToken)).append("\n");
    sb.append("    fileloc: ").append(toIndentedString(fileloc)).append("\n");
    sb.append("    hasImportErrors: ").append(toIndentedString(hasImportErrors)).append("\n");
    sb.append("    hasTaskConcurrencyLimits: ").append(toIndentedString(hasTaskConcurrencyLimits)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isPaused: ").append(toIndentedString(isPaused)).append("\n");
    sb.append("    isSubdag: ").append(toIndentedString(isSubdag)).append("\n");
    sb.append("    lastExpired: ").append(toIndentedString(lastExpired)).append("\n");
    sb.append("    lastParsedTime: ").append(toIndentedString(lastParsedTime)).append("\n");
    sb.append("    lastPickled: ").append(toIndentedString(lastPickled)).append("\n");
    sb.append("    maxActiveRuns: ").append(toIndentedString(maxActiveRuns)).append("\n");
    sb.append("    maxActiveTasks: ").append(toIndentedString(maxActiveTasks)).append("\n");
    sb.append("    nextDagrun: ").append(toIndentedString(nextDagrun)).append("\n");
    sb.append("    nextDagrunCreateAfter: ").append(toIndentedString(nextDagrunCreateAfter)).append("\n");
    sb.append("    nextDagrunDataIntervalEnd: ").append(toIndentedString(nextDagrunDataIntervalEnd)).append("\n");
    sb.append("    nextDagrunDataIntervalStart: ").append(toIndentedString(nextDagrunDataIntervalStart)).append("\n");
    sb.append("    owners: ").append(toIndentedString(owners)).append("\n");
    sb.append("    pickleId: ").append(toIndentedString(pickleId)).append("\n");
    sb.append("    rootDagId: ").append(toIndentedString(rootDagId)).append("\n");
    sb.append("    scheduleInterval: ").append(toIndentedString(scheduleInterval)).append("\n");
    sb.append("    schedulerLock: ").append(toIndentedString(schedulerLock)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    timetableDescription: ").append(toIndentedString(timetableDescription)).append("\n");
    sb.append("    catchup: ").append(toIndentedString(catchup)).append("\n");
    sb.append("    concurrency: ").append(toIndentedString(concurrency)).append("\n");
    sb.append("    dagRunTimeout: ").append(toIndentedString(dagRunTimeout)).append("\n");
    sb.append("    docMd: ").append(toIndentedString(docMd)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    isPausedUponCreation: ").append(toIndentedString(isPausedUponCreation)).append("\n");
    sb.append("    lastParsed: ").append(toIndentedString(lastParsed)).append("\n");
    sb.append("    orientation: ").append(toIndentedString(orientation)).append("\n");
    sb.append("    params: ").append(toIndentedString(params)).append("\n");
    sb.append("    renderTemplateAsNativeObj: ").append(toIndentedString(renderTemplateAsNativeObj)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
    sb.append("    templateSearchPath: ").append(toIndentedString(templateSearchPath)).append("\n");
    sb.append("    timezone: ").append(toIndentedString(timezone)).append("\n");
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
    openapiFields.add("dag_id");
    openapiFields.add("default_view");
    openapiFields.add("description");
    openapiFields.add("file_token");
    openapiFields.add("fileloc");
    openapiFields.add("has_import_errors");
    openapiFields.add("has_task_concurrency_limits");
    openapiFields.add("is_active");
    openapiFields.add("is_paused");
    openapiFields.add("is_subdag");
    openapiFields.add("last_expired");
    openapiFields.add("last_parsed_time");
    openapiFields.add("last_pickled");
    openapiFields.add("max_active_runs");
    openapiFields.add("max_active_tasks");
    openapiFields.add("next_dagrun");
    openapiFields.add("next_dagrun_create_after");
    openapiFields.add("next_dagrun_data_interval_end");
    openapiFields.add("next_dagrun_data_interval_start");
    openapiFields.add("owners");
    openapiFields.add("pickle_id");
    openapiFields.add("root_dag_id");
    openapiFields.add("schedule_interval");
    openapiFields.add("scheduler_lock");
    openapiFields.add("tags");
    openapiFields.add("timetable_description");
    openapiFields.add("catchup");
    openapiFields.add("concurrency");
    openapiFields.add("dag_run_timeout");
    openapiFields.add("doc_md");
    openapiFields.add("end_date");
    openapiFields.add("is_paused_upon_creation");
    openapiFields.add("last_parsed");
    openapiFields.add("orientation");
    openapiFields.add("params");
    openapiFields.add("render_template_as_native_obj");
    openapiFields.add("start_date");
    openapiFields.add("template_search_path");
    openapiFields.add("timezone");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DAGDetail
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DAGDetail.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DAGDetail is not found in the empty JSON string", DAGDetail.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DAGDetail.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DAGDetail` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("dag_id") != null && !jsonObj.get("dag_id").isJsonNull()) && !jsonObj.get("dag_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dag_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dag_id").toString()));
      }
      if ((jsonObj.get("default_view") != null && !jsonObj.get("default_view").isJsonNull()) && !jsonObj.get("default_view").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `default_view` to be a primitive type in the JSON string but got `%s`", jsonObj.get("default_view").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("file_token") != null && !jsonObj.get("file_token").isJsonNull()) && !jsonObj.get("file_token").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `file_token` to be a primitive type in the JSON string but got `%s`", jsonObj.get("file_token").toString()));
      }
      if ((jsonObj.get("fileloc") != null && !jsonObj.get("fileloc").isJsonNull()) && !jsonObj.get("fileloc").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fileloc` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fileloc").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("owners") != null && !jsonObj.get("owners").isJsonNull() && !jsonObj.get("owners").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `owners` to be an array in the JSON string but got `%s`", jsonObj.get("owners").toString()));
      }
      if ((jsonObj.get("pickle_id") != null && !jsonObj.get("pickle_id").isJsonNull()) && !jsonObj.get("pickle_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pickle_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pickle_id").toString()));
      }
      if ((jsonObj.get("root_dag_id") != null && !jsonObj.get("root_dag_id").isJsonNull()) && !jsonObj.get("root_dag_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `root_dag_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("root_dag_id").toString()));
      }
      // validate the optional field `schedule_interval`
      if (jsonObj.get("schedule_interval") != null && !jsonObj.get("schedule_interval").isJsonNull()) {
        ScheduleInterval.validateJsonElement(jsonObj.get("schedule_interval"));
      }
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull()) {
        JsonArray jsonArraytags = jsonObj.getAsJsonArray("tags");
        if (jsonArraytags != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tags").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
          }

          // validate the optional field `tags` (array)
          for (int i = 0; i < jsonArraytags.size(); i++) {
            Tag.validateJsonElement(jsonArraytags.get(i));
          };
        }
      }
      if ((jsonObj.get("timetable_description") != null && !jsonObj.get("timetable_description").isJsonNull()) && !jsonObj.get("timetable_description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timetable_description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timetable_description").toString()));
      }
      // validate the optional field `dag_run_timeout`
      if (jsonObj.get("dag_run_timeout") != null && !jsonObj.get("dag_run_timeout").isJsonNull()) {
        TimeDelta.validateJsonElement(jsonObj.get("dag_run_timeout"));
      }
      if ((jsonObj.get("doc_md") != null && !jsonObj.get("doc_md").isJsonNull()) && !jsonObj.get("doc_md").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `doc_md` to be a primitive type in the JSON string but got `%s`", jsonObj.get("doc_md").toString()));
      }
      if ((jsonObj.get("orientation") != null && !jsonObj.get("orientation").isJsonNull()) && !jsonObj.get("orientation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orientation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orientation").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("template_search_path") != null && !jsonObj.get("template_search_path").isJsonNull() && !jsonObj.get("template_search_path").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `template_search_path` to be an array in the JSON string but got `%s`", jsonObj.get("template_search_path").toString()));
      }
      if ((jsonObj.get("timezone") != null && !jsonObj.get("timezone").isJsonNull()) && !jsonObj.get("timezone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timezone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timezone").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DAGDetail.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DAGDetail' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DAGDetail> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DAGDetail.class));

       return (TypeAdapter<T>) new TypeAdapter<DAGDetail>() {
           @Override
           public void write(JsonWriter out, DAGDetail value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DAGDetail read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DAGDetail given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DAGDetail
   * @throws IOException if the JSON string is invalid with respect to DAGDetail
   */
  public static DAGDetail fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DAGDetail.class);
  }

  /**
   * Convert an instance of DAGDetail to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

