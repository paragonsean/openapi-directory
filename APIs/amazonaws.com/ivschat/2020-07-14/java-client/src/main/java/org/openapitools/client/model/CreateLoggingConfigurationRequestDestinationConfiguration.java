/*
 * Amazon Interactive Video Service Chat
 * <p> <b>Introduction</b> </p> <p>The Amazon IVS Chat control-plane API enables you to create and manage Amazon IVS Chat resources. You also need to integrate with the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\"> Amazon IVS Chat Messaging API</a>, to enable users to interact with chat rooms in real time.</p> <p>The API is an AWS regional service. For a list of supported regions and Amazon IVS Chat HTTPS service endpoints, see the Amazon IVS Chat information on the <a href=\"https://docs.aws.amazon.com/general/latest/gr/ivs.html\">Amazon IVS page</a> in the <i>AWS General Reference</i>. </p> <p> <b>Notes on terminology:</b> </p> <ul> <li> <p>You create service applications using the Amazon IVS Chat API. We refer to these as <i>applications</i>.</p> </li> <li> <p>You create front-end client applications (browser and Android/iOS apps) using the Amazon IVS Chat Messaging API. We refer to these as <i>clients</i>. </p> </li> </ul> <p> <b>Resources</b> </p> <p>The following resources are part of Amazon IVS Chat:</p> <ul> <li> <p> <b>LoggingConfiguration</b> — A configuration that allows customers to store and record sent messages in a chat room. See the Logging Configuration endpoints for more information.</p> </li> <li> <p> <b>Room</b> — The central Amazon IVS Chat resource through which clients connect to and exchange chat messages. See the Room endpoints for more information.</p> </li> </ul> <p> <b>Tagging</b> </p> <p>A <i>tag</i> is a metadata label that you assign to an AWS resource. A tag comprises a <i>key</i> and a <i>value</i>, both set by you. For example, you might set a tag as <code>topic:nature</code> to label a particular video category. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging AWS Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS Chat has no service-specific constraints beyond what is documented there.</p> <p>Tags can help you identify and organize your AWS resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\">Access Tags</a>).</p> <p>The Amazon IVS Chat API has these tag-related endpoints: <a>TagResource</a>, <a>UntagResource</a>, and <a>ListTagsForResource</a>. The following resource supports tagging: Room.</p> <p>At most 50 tags can be applied to a resource.</p> <p> <b>API Access Security</b> </p> <p>Your Amazon IVS Chat applications (service applications and clients) must be authenticated and authorized to access Amazon IVS Chat resources. Note the differences between these concepts:</p> <ul> <li> <p> <i>Authentication</i> is about verifying identity. Requests to the Amazon IVS Chat API must be signed to verify your identity.</p> </li> <li> <p> <i>Authorization</i> is about granting permissions. Your IAM roles need to have permissions for Amazon IVS Chat API requests.</p> </li> </ul> <p>Users (viewers) connect to a room using secure access tokens that you create using the <a>CreateChatToken</a> endpoint through the AWS SDK. You call CreateChatToken for every user’s chat session, passing identity and authorization information about the user.</p> <p> <b>Signing API Requests</b> </p> <p>HTTP API requests must be signed with an AWS SigV4 signature using your AWS security credentials. The AWS Command Line Interface (CLI) and the AWS SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS Chat HTTP API directly, it’s your responsibility to sign the requests.</p> <p>You generate a signature using valid AWS credentials for an IAM role that has permission to perform the requested action. For example, DeleteMessage requests must be made using an IAM role that has the <code>ivschat:DeleteMessage</code> permission.</p> <p>For more information:</p> <ul> <li> <p>Authentication and generating signatures — See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon Web Services General Reference</i>.</p> </li> <li> <p>Managing Amazon IVS permissions — See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\">Identity and Access Management</a> on the Security page of the <i>Amazon IVS User Guide</i>.</p> </li> </ul> <p> <b>Amazon Resource Names (ARNs)</b> </p> <p>ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names</a> in the <i>AWS General Reference</i>.</p> <p> <b>Messaging Endpoints</b> </p> <ul> <li> <p> <a>DeleteMessage</a> — Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s <code>EventName</code> is <code>aws:DELETE_MESSAGE</code>. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html\"> DeleteMessage</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p> </li> <li> <p> <a>DisconnectUser</a> — Disconnects all connections using a specified user ID from a room. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html\"> DisconnectUser</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p> </li> <li> <p> <a>SendEvent</a> — Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.</p> </li> </ul> <p> <b>Chat Token Endpoint</b> </p> <ul> <li> <p> <a>CreateChatToken</a> — Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.</p> </li> </ul> <p> <b>Room Endpoints</b> </p> <ul> <li> <p> <a>CreateRoom</a> — Creates a room that allows clients to connect and pass messages.</p> </li> <li> <p> <a>DeleteRoom</a> — Deletes the specified room.</p> </li> <li> <p> <a>GetRoom</a> — Gets the specified room.</p> </li> <li> <p> <a>ListRooms</a> — Gets summary information about all your rooms in the AWS region where the API request is processed. </p> </li> <li> <p> <a>UpdateRoom</a> — Updates a room’s configuration.</p> </li> </ul> <p> <b>Logging Configuration Endpoints</b> </p> <ul> <li> <p> <a>CreateLoggingConfiguration</a> — Creates a logging configuration that allows clients to store and record sent messages.</p> </li> <li> <p> <a>DeleteLoggingConfiguration</a> — Deletes the specified logging configuration.</p> </li> <li> <p> <a>GetLoggingConfiguration</a> — Gets the specified logging configuration.</p> </li> <li> <p> <a>ListLoggingConfigurations</a> — Gets summary information about all your logging configurations in the AWS region where the API request is processed.</p> </li> <li> <p> <a>UpdateLoggingConfiguration</a> — Updates a specified logging configuration.</p> </li> </ul> <p> <b>Tags Endpoints</b> </p> <ul> <li> <p> <a>ListTagsForResource</a> — Gets information about AWS tags for the specified ARN.</p> </li> <li> <p> <a>TagResource</a> — Adds or updates tags for the AWS resource with the specified ARN.</p> </li> <li> <p> <a>UntagResource</a> — Removes tags from the resource with the specified ARN.</p> </li> </ul> <p>All the above are HTTP operations. There is a separate <i>messaging</i> API for managing Chat resources; see the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\"> Amazon IVS Chat Messaging API Reference</a>.</p>
 *
 * The version of the OpenAPI document: 2020-07-14
 * Contact: mike.ralphson@gmail.com
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
import org.openapitools.client.model.CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs;
import org.openapitools.client.model.CreateLoggingConfigurationRequestDestinationConfigurationFirehose;
import org.openapitools.client.model.CreateLoggingConfigurationRequestDestinationConfigurationS3;

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
 * CreateLoggingConfigurationRequestDestinationConfiguration
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:28:20.323587-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateLoggingConfigurationRequestDestinationConfiguration {
  public static final String SERIALIZED_NAME_CLOUD_WATCH_LOGS = "cloudWatchLogs";
  @SerializedName(SERIALIZED_NAME_CLOUD_WATCH_LOGS)
  private CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs cloudWatchLogs;

  public static final String SERIALIZED_NAME_FIREHOSE = "firehose";
  @SerializedName(SERIALIZED_NAME_FIREHOSE)
  private CreateLoggingConfigurationRequestDestinationConfigurationFirehose firehose;

  public static final String SERIALIZED_NAME_S3 = "s3";
  @SerializedName(SERIALIZED_NAME_S3)
  private CreateLoggingConfigurationRequestDestinationConfigurationS3 s3;

  public CreateLoggingConfigurationRequestDestinationConfiguration() {
  }

  public CreateLoggingConfigurationRequestDestinationConfiguration cloudWatchLogs(CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs cloudWatchLogs) {
    this.cloudWatchLogs = cloudWatchLogs;
    return this;
  }

  /**
   * Get cloudWatchLogs
   * @return cloudWatchLogs
   */
  @javax.annotation.Nullable
  public CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs getCloudWatchLogs() {
    return cloudWatchLogs;
  }

  public void setCloudWatchLogs(CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs cloudWatchLogs) {
    this.cloudWatchLogs = cloudWatchLogs;
  }


  public CreateLoggingConfigurationRequestDestinationConfiguration firehose(CreateLoggingConfigurationRequestDestinationConfigurationFirehose firehose) {
    this.firehose = firehose;
    return this;
  }

  /**
   * Get firehose
   * @return firehose
   */
  @javax.annotation.Nullable
  public CreateLoggingConfigurationRequestDestinationConfigurationFirehose getFirehose() {
    return firehose;
  }

  public void setFirehose(CreateLoggingConfigurationRequestDestinationConfigurationFirehose firehose) {
    this.firehose = firehose;
  }


  public CreateLoggingConfigurationRequestDestinationConfiguration s3(CreateLoggingConfigurationRequestDestinationConfigurationS3 s3) {
    this.s3 = s3;
    return this;
  }

  /**
   * Get s3
   * @return s3
   */
  @javax.annotation.Nullable
  public CreateLoggingConfigurationRequestDestinationConfigurationS3 getS3() {
    return s3;
  }

  public void setS3(CreateLoggingConfigurationRequestDestinationConfigurationS3 s3) {
    this.s3 = s3;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateLoggingConfigurationRequestDestinationConfiguration createLoggingConfigurationRequestDestinationConfiguration = (CreateLoggingConfigurationRequestDestinationConfiguration) o;
    return Objects.equals(this.cloudWatchLogs, createLoggingConfigurationRequestDestinationConfiguration.cloudWatchLogs) &&
        Objects.equals(this.firehose, createLoggingConfigurationRequestDestinationConfiguration.firehose) &&
        Objects.equals(this.s3, createLoggingConfigurationRequestDestinationConfiguration.s3);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cloudWatchLogs, firehose, s3);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateLoggingConfigurationRequestDestinationConfiguration {\n");
    sb.append("    cloudWatchLogs: ").append(toIndentedString(cloudWatchLogs)).append("\n");
    sb.append("    firehose: ").append(toIndentedString(firehose)).append("\n");
    sb.append("    s3: ").append(toIndentedString(s3)).append("\n");
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
    openapiFields.add("cloudWatchLogs");
    openapiFields.add("firehose");
    openapiFields.add("s3");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateLoggingConfigurationRequestDestinationConfiguration
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateLoggingConfigurationRequestDestinationConfiguration.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateLoggingConfigurationRequestDestinationConfiguration is not found in the empty JSON string", CreateLoggingConfigurationRequestDestinationConfiguration.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateLoggingConfigurationRequestDestinationConfiguration.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateLoggingConfigurationRequestDestinationConfiguration` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `cloudWatchLogs`
      if (jsonObj.get("cloudWatchLogs") != null && !jsonObj.get("cloudWatchLogs").isJsonNull()) {
        CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs.validateJsonElement(jsonObj.get("cloudWatchLogs"));
      }
      // validate the optional field `firehose`
      if (jsonObj.get("firehose") != null && !jsonObj.get("firehose").isJsonNull()) {
        CreateLoggingConfigurationRequestDestinationConfigurationFirehose.validateJsonElement(jsonObj.get("firehose"));
      }
      // validate the optional field `s3`
      if (jsonObj.get("s3") != null && !jsonObj.get("s3").isJsonNull()) {
        CreateLoggingConfigurationRequestDestinationConfigurationS3.validateJsonElement(jsonObj.get("s3"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateLoggingConfigurationRequestDestinationConfiguration.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateLoggingConfigurationRequestDestinationConfiguration' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateLoggingConfigurationRequestDestinationConfiguration> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateLoggingConfigurationRequestDestinationConfiguration.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateLoggingConfigurationRequestDestinationConfiguration>() {
           @Override
           public void write(JsonWriter out, CreateLoggingConfigurationRequestDestinationConfiguration value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateLoggingConfigurationRequestDestinationConfiguration read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateLoggingConfigurationRequestDestinationConfiguration given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateLoggingConfigurationRequestDestinationConfiguration
   * @throws IOException if the JSON string is invalid with respect to CreateLoggingConfigurationRequestDestinationConfiguration
   */
  public static CreateLoggingConfigurationRequestDestinationConfiguration fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateLoggingConfigurationRequestDestinationConfiguration.class);
  }

  /**
   * Convert an instance of CreateLoggingConfigurationRequestDestinationConfiguration to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

