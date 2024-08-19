/**
 * Amazon Interactive Video Service
 * <p> <b>Introduction</b> </p> <p>The Amazon Interactive Video Service (IVS) API is REST compatible, using a standard HTTP API and an Amazon Web Services EventBridge event stream for responses. JSON is used for both requests and responses, including errors.</p> <p>The API is an Amazon Web Services regional service. For a list of supported regions and Amazon IVS HTTPS service endpoints, see the <a href=\"https://docs.aws.amazon.com/general/latest/gr/ivs.html\">Amazon IVS page</a> in the <i>Amazon Web Services General Reference</i>.</p> <p> <i> <b>All API request parameters and URLs are case sensitive. </b> </i> </p> <p>For a summary of notable documentation changes in each release, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/doc-history.html\"> Document History</a>.</p> <p> <b>Allowed Header Values</b> </p> <ul> <li> <p> <code> <b>Accept:</b> </code> application/json</p> </li> <li> <p> <code> <b>Accept-Encoding:</b> </code> gzip, deflate</p> </li> <li> <p> <code> <b>Content-Type:</b> </code>application/json</p> </li> </ul> <p> <b>Resources</b> </p> <p>The following resources contain information about your IVS live stream (see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/getting-started.html\"> Getting Started with Amazon IVS</a>):</p> <ul> <li> <p> <b>Channel</b> — Stores configuration data related to your live stream. You first create a channel and then use the channel’s stream key to start your live stream. See the Channel endpoints for more information. </p> </li> <li> <p> <b>Stream key</b> — An identifier assigned by Amazon IVS when you create a channel, which is then used to authorize streaming. See the StreamKey endpoints for more information. <i> <b>Treat the stream key like a secret, since it allows anyone to stream to the channel.</b> </i> </p> </li> <li> <p> <b>Playback key pair</b> — Video playback may be restricted using playback-authorization tokens, which use public-key encryption. A playback key pair is the public-private pair of keys used to sign and validate the playback-authorization token. See the PlaybackKeyPair endpoints for more information.</p> </li> <li> <p> <b>Recording configuration</b> — Stores configuration related to recording a live stream and where to store the recorded content. Multiple channels can reference the same recording configuration. See the Recording Configuration endpoints for more information.</p> </li> </ul> <p> <b>Tagging</b> </p> <p>A <i>tag</i> is a metadata label that you assign to an Amazon Web Services resource. A tag comprises a <i>key</i> and a <i>value</i>, both set by you. For example, you might set a tag as <code>topic:nature</code> to label a particular video category. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p> <p>Tags can help you identify and organize your Amazon Web Services resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\"> Access Tags</a>). </p> <p>The Amazon IVS API has these tag-related endpoints: <a>TagResource</a>, <a>UntagResource</a>, and <a>ListTagsForResource</a>. The following resources support tagging: Channels, Stream Keys, Playback Key Pairs, and Recording Configurations.</p> <p>At most 50 tags can be applied to a resource. </p> <p> <b>Authentication versus Authorization</b> </p> <p>Note the differences between these concepts:</p> <ul> <li> <p> <i>Authentication</i> is about verifying identity. You need to be authenticated to sign Amazon IVS API requests.</p> </li> <li> <p> <i>Authorization</i> is about granting permissions. Your IAM roles need to have permissions for Amazon IVS API requests. In addition, authorization is needed to view <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Amazon IVS private channels</a>. (Private channels are channels that are enabled for \"playback authorization.\")</p> </li> </ul> <p> <b>Authentication</b> </p> <p>All Amazon IVS API requests must be authenticated with a signature. The Amazon Web Services Command-Line Interface (CLI) and Amazon IVS Player SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS API directly, it’s your responsibility to sign the requests.</p> <p>You generate a signature using valid Amazon Web Services credentials that have permission to perform the requested action. For example, you must sign PutMetadata requests with a signature generated from a user account that has the <code>ivs:PutMetadata</code> permission.</p> <p>For more information:</p> <ul> <li> <p>Authentication and generating signatures — See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon Web Services General Reference</i>.</p> </li> <li> <p>Managing Amazon IVS permissions — See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\">Identity and Access Management</a> on the Security page of the <i>Amazon IVS User Guide</i>.</p> </li> </ul> <p> <b>Amazon Resource Names (ARNs)</b> </p> <p>ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names</a> in the <i>AWS General Reference</i>.</p> <p> <b>Channel Endpoints</b> </p> <ul> <li> <p> <a>CreateChannel</a> — Creates a new channel and an associated stream key to start streaming.</p> </li> <li> <p> <a>GetChannel</a> — Gets the channel configuration for the specified channel ARN.</p> </li> <li> <p> <a>BatchGetChannel</a> — Performs <a>GetChannel</a> on multiple ARNs simultaneously.</p> </li> <li> <p> <a>ListChannels</a> — Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 Conflict Exception).</p> </li> <li> <p> <a>UpdateChannel</a> — Updates a channel's configuration. This does not affect an ongoing stream of this channel. You must stop and restart the stream for the changes to take effect.</p> </li> <li> <p> <a>DeleteChannel</a> — Deletes the specified channel.</p> </li> </ul> <p> <b>StreamKey Endpoints</b> </p> <ul> <li> <p> <a>CreateStreamKey</a> — Creates a stream key, used to initiate a stream, for the specified channel ARN.</p> </li> <li> <p> <a>GetStreamKey</a> — Gets stream key information for the specified ARN.</p> </li> <li> <p> <a>BatchGetStreamKey</a> — Performs <a>GetStreamKey</a> on multiple ARNs simultaneously.</p> </li> <li> <p> <a>ListStreamKeys</a> — Gets summary information about stream keys for the specified channel.</p> </li> <li> <p> <a>DeleteStreamKey</a> — Deletes the stream key for the specified ARN, so it can no longer be used to stream.</p> </li> </ul> <p> <b>Stream Endpoints</b> </p> <ul> <li> <p> <a>GetStream</a> — Gets information about the active (live) stream on a specified channel.</p> </li> <li> <p> <a>GetStreamSession</a> — Gets metadata on a specified stream.</p> </li> <li> <p> <a>ListStreams</a> — Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.</p> </li> <li> <p> <a>ListStreamSessions</a> — Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.</p> </li> <li> <p> <a>StopStream</a> — Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with <a>DeleteStreamKey</a> to prevent further streaming to a channel.</p> </li> <li> <p> <a>PutMetadata</a> — Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed.</p> </li> </ul> <p> <b>Private Channel Endpoints</b> </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p> <ul> <li> <p> <a>ImportPlaybackKeyPair</a> — Imports the public portion of a new key pair and returns its <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> can then be used to generate viewer authorization tokens, to grant viewers access to private channels (channels enabled for playback authorization).</p> </li> <li> <p> <a>GetPlaybackKeyPair</a> — Gets a specified playback authorization key pair and returns the <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels.</p> </li> <li> <p> <a>ListPlaybackKeyPairs</a> — Gets summary information about playback key pairs.</p> </li> <li> <p> <a>DeletePlaybackKeyPair</a> — Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s <code>privateKey</code>.</p> </li> <li> <p> <a>StartViewerSessionRevocation</a> — Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version.</p> </li> <li> <p> <a>BatchStartViewerSessionRevocation</a> — Performs <a>StartViewerSessionRevocation</a> on multiple channel ARN and viewer ID pairs simultaneously.</p> </li> </ul> <p> <b>RecordingConfiguration Endpoints</b> </p> <ul> <li> <p> <a>CreateRecordingConfiguration</a> — Creates a new recording configuration, used to enable recording to Amazon S3.</p> </li> <li> <p> <a>GetRecordingConfiguration</a> — Gets the recording-configuration metadata for the specified ARN.</p> </li> <li> <p> <a>ListRecordingConfigurations</a> — Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.</p> </li> <li> <p> <a>DeleteRecordingConfiguration</a> — Deletes the recording configuration for the specified ARN.</p> </li> </ul> <p> <b>Amazon Web Services Tags Endpoints</b> </p> <ul> <li> <p> <a>TagResource</a> — Adds or updates tags for the Amazon Web Services resource with the specified ARN.</p> </li> <li> <p> <a>UntagResource</a> — Removes tags from the resource with the specified ARN.</p> </li> <li> <p> <a>ListTagsForResource</a> — Gets information about Amazon Web Services tags for the specified ARN.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2020-07-14
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBatchGetChannelResponse.h"
#include "OAIBatchGetChannel_request.h"
#include "OAIBatchGetStreamKeyResponse.h"
#include "OAIBatchGetStreamKey_request.h"
#include "OAIBatchStartViewerSessionRevocationResponse.h"
#include "OAIBatchStartViewerSessionRevocation_request.h"
#include "OAICreateChannelResponse.h"
#include "OAICreateChannel_request.h"
#include "OAICreateRecordingConfigurationResponse.h"
#include "OAICreateRecordingConfiguration_request.h"
#include "OAICreateStreamKeyResponse.h"
#include "OAICreateStreamKey_request.h"
#include "OAIDeleteChannel_request.h"
#include "OAIDeletePlaybackKeyPair_request.h"
#include "OAIDeleteRecordingConfiguration_request.h"
#include "OAIDeleteStreamKey_request.h"
#include "OAIGetChannelResponse.h"
#include "OAIGetChannel_request.h"
#include "OAIGetPlaybackKeyPairResponse.h"
#include "OAIGetPlaybackKeyPair_request.h"
#include "OAIGetRecordingConfigurationResponse.h"
#include "OAIGetRecordingConfiguration_request.h"
#include "OAIGetStreamKeyResponse.h"
#include "OAIGetStreamKey_request.h"
#include "OAIGetStreamResponse.h"
#include "OAIGetStreamSessionResponse.h"
#include "OAIGetStreamSession_request.h"
#include "OAIGetStream_request.h"
#include "OAIImportPlaybackKeyPairResponse.h"
#include "OAIImportPlaybackKeyPair_request.h"
#include "OAIListChannelsResponse.h"
#include "OAIListChannels_request.h"
#include "OAIListPlaybackKeyPairsResponse.h"
#include "OAIListPlaybackKeyPairs_request.h"
#include "OAIListRecordingConfigurationsResponse.h"
#include "OAIListRecordingConfigurations_request.h"
#include "OAIListStreamKeysResponse.h"
#include "OAIListStreamKeys_request.h"
#include "OAIListStreamSessionsResponse.h"
#include "OAIListStreamSessions_request.h"
#include "OAIListStreamsResponse.h"
#include "OAIListStreams_request.h"
#include "OAIListTagsForResourceResponse.h"
#include "OAIObject.h"
#include "OAIPutMetadata_request.h"
#include "OAIStartViewerSessionRevocation_request.h"
#include "OAIStopStream_request.h"
#include "OAITagResource_request.h"
#include "OAIUpdateChannelResponse.h"
#include "OAIUpdateChannel_request.h"
#include <QJsonValue>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  oai_batch_get_channel_request OAIBatchGetChannel_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void batchGetChannel(const OAIBatchGetChannel_request &oai_batch_get_channel_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_batch_get_stream_key_request OAIBatchGetStreamKey_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void batchGetStreamKey(const OAIBatchGetStreamKey_request &oai_batch_get_stream_key_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_batch_start_viewer_session_revocation_request OAIBatchStartViewerSessionRevocation_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void batchStartViewerSessionRevocation(const OAIBatchStartViewerSessionRevocation_request &oai_batch_start_viewer_session_revocation_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_create_channel_request OAICreateChannel_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createChannel(const OAICreateChannel_request &oai_create_channel_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_create_recording_configuration_request OAICreateRecordingConfiguration_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createRecordingConfiguration(const OAICreateRecordingConfiguration_request &oai_create_recording_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_create_stream_key_request OAICreateStreamKey_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createStreamKey(const OAICreateStreamKey_request &oai_create_stream_key_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_delete_channel_request OAIDeleteChannel_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteChannel(const OAIDeleteChannel_request &oai_delete_channel_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_delete_playback_key_pair_request OAIDeletePlaybackKeyPair_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deletePlaybackKeyPair(const OAIDeletePlaybackKeyPair_request &oai_delete_playback_key_pair_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_delete_recording_configuration_request OAIDeleteRecordingConfiguration_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteRecordingConfiguration(const OAIDeleteRecordingConfiguration_request &oai_delete_recording_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_delete_stream_key_request OAIDeleteStreamKey_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteStreamKey(const OAIDeleteStreamKey_request &oai_delete_stream_key_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_get_channel_request OAIGetChannel_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getChannel(const OAIGetChannel_request &oai_get_channel_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_get_playback_key_pair_request OAIGetPlaybackKeyPair_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getPlaybackKeyPair(const OAIGetPlaybackKeyPair_request &oai_get_playback_key_pair_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_get_recording_configuration_request OAIGetRecordingConfiguration_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getRecordingConfiguration(const OAIGetRecordingConfiguration_request &oai_get_recording_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_get_stream_request OAIGetStream_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getStream(const OAIGetStream_request &oai_get_stream_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_get_stream_key_request OAIGetStreamKey_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getStreamKey(const OAIGetStreamKey_request &oai_get_stream_key_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_get_stream_session_request OAIGetStreamSession_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getStreamSession(const OAIGetStreamSession_request &oai_get_stream_session_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_import_playback_key_pair_request OAIImportPlaybackKeyPair_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void importPlaybackKeyPair(const OAIImportPlaybackKeyPair_request &oai_import_playback_key_pair_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_list_channels_request OAIListChannels_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listChannels(const OAIListChannels_request &oai_list_channels_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_list_playback_key_pairs_request OAIListPlaybackKeyPairs_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listPlaybackKeyPairs(const OAIListPlaybackKeyPairs_request &oai_list_playback_key_pairs_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_list_recording_configurations_request OAIListRecordingConfigurations_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listRecordingConfigurations(const OAIListRecordingConfigurations_request &oai_list_recording_configurations_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_list_stream_keys_request OAIListStreamKeys_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listStreamKeys(const OAIListStreamKeys_request &oai_list_stream_keys_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_list_stream_sessions_request OAIListStreamSessions_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listStreamSessions(const OAIListStreamSessions_request &oai_list_stream_sessions_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_list_streams_request OAIListStreams_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listStreams(const OAIListStreams_request &oai_list_streams_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_arn QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void listTagsForResource(const QString &resource_arn, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_put_metadata_request OAIPutMetadata_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void putMetadata(const OAIPutMetadata_request &oai_put_metadata_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_start_viewer_session_revocation_request OAIStartViewerSessionRevocation_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void startViewerSessionRevocation(const OAIStartViewerSessionRevocation_request &oai_start_viewer_session_revocation_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_stop_stream_request OAIStopStream_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void stopStream(const OAIStopStream_request &oai_stop_stream_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_arn QString [required]
    * @param[in]  oai_tag_resource_request OAITagResource_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void tagResource(const QString &resource_arn, const OAITagResource_request &oai_tag_resource_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_arn QString [required]
    * @param[in]  tag_keys QList<QString> [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void untagResource(const QString &resource_arn, const QList<QString> &tag_keys, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_update_channel_request OAIUpdateChannel_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateChannel(const OAIUpdateChannel_request &oai_update_channel_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void batchGetChannelCallback(OAIHttpRequestWorker *worker);
    void batchGetStreamKeyCallback(OAIHttpRequestWorker *worker);
    void batchStartViewerSessionRevocationCallback(OAIHttpRequestWorker *worker);
    void createChannelCallback(OAIHttpRequestWorker *worker);
    void createRecordingConfigurationCallback(OAIHttpRequestWorker *worker);
    void createStreamKeyCallback(OAIHttpRequestWorker *worker);
    void deleteChannelCallback(OAIHttpRequestWorker *worker);
    void deletePlaybackKeyPairCallback(OAIHttpRequestWorker *worker);
    void deleteRecordingConfigurationCallback(OAIHttpRequestWorker *worker);
    void deleteStreamKeyCallback(OAIHttpRequestWorker *worker);
    void getChannelCallback(OAIHttpRequestWorker *worker);
    void getPlaybackKeyPairCallback(OAIHttpRequestWorker *worker);
    void getRecordingConfigurationCallback(OAIHttpRequestWorker *worker);
    void getStreamCallback(OAIHttpRequestWorker *worker);
    void getStreamKeyCallback(OAIHttpRequestWorker *worker);
    void getStreamSessionCallback(OAIHttpRequestWorker *worker);
    void importPlaybackKeyPairCallback(OAIHttpRequestWorker *worker);
    void listChannelsCallback(OAIHttpRequestWorker *worker);
    void listPlaybackKeyPairsCallback(OAIHttpRequestWorker *worker);
    void listRecordingConfigurationsCallback(OAIHttpRequestWorker *worker);
    void listStreamKeysCallback(OAIHttpRequestWorker *worker);
    void listStreamSessionsCallback(OAIHttpRequestWorker *worker);
    void listStreamsCallback(OAIHttpRequestWorker *worker);
    void listTagsForResourceCallback(OAIHttpRequestWorker *worker);
    void putMetadataCallback(OAIHttpRequestWorker *worker);
    void startViewerSessionRevocationCallback(OAIHttpRequestWorker *worker);
    void stopStreamCallback(OAIHttpRequestWorker *worker);
    void tagResourceCallback(OAIHttpRequestWorker *worker);
    void untagResourceCallback(OAIHttpRequestWorker *worker);
    void updateChannelCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void batchGetChannelSignal(OAIBatchGetChannelResponse summary);
    void batchGetStreamKeySignal(OAIBatchGetStreamKeyResponse summary);
    void batchStartViewerSessionRevocationSignal(OAIBatchStartViewerSessionRevocationResponse summary);
    void createChannelSignal(OAICreateChannelResponse summary);
    void createRecordingConfigurationSignal(OAICreateRecordingConfigurationResponse summary);
    void createStreamKeySignal(OAICreateStreamKeyResponse summary);
    void deleteChannelSignal();
    void deletePlaybackKeyPairSignal(OAIObject summary);
    void deleteRecordingConfigurationSignal();
    void deleteStreamKeySignal();
    void getChannelSignal(OAIGetChannelResponse summary);
    void getPlaybackKeyPairSignal(OAIGetPlaybackKeyPairResponse summary);
    void getRecordingConfigurationSignal(OAIGetRecordingConfigurationResponse summary);
    void getStreamSignal(OAIGetStreamResponse summary);
    void getStreamKeySignal(OAIGetStreamKeyResponse summary);
    void getStreamSessionSignal(OAIGetStreamSessionResponse summary);
    void importPlaybackKeyPairSignal(OAIImportPlaybackKeyPairResponse summary);
    void listChannelsSignal(OAIListChannelsResponse summary);
    void listPlaybackKeyPairsSignal(OAIListPlaybackKeyPairsResponse summary);
    void listRecordingConfigurationsSignal(OAIListRecordingConfigurationsResponse summary);
    void listStreamKeysSignal(OAIListStreamKeysResponse summary);
    void listStreamSessionsSignal(OAIListStreamSessionsResponse summary);
    void listStreamsSignal(OAIListStreamsResponse summary);
    void listTagsForResourceSignal(OAIListTagsForResourceResponse summary);
    void putMetadataSignal();
    void startViewerSessionRevocationSignal(OAIObject summary);
    void stopStreamSignal(OAIObject summary);
    void tagResourceSignal(OAIObject summary);
    void untagResourceSignal(OAIObject summary);
    void updateChannelSignal(OAIUpdateChannelResponse summary);


    void batchGetChannelSignalFull(OAIHttpRequestWorker *worker, OAIBatchGetChannelResponse summary);
    void batchGetStreamKeySignalFull(OAIHttpRequestWorker *worker, OAIBatchGetStreamKeyResponse summary);
    void batchStartViewerSessionRevocationSignalFull(OAIHttpRequestWorker *worker, OAIBatchStartViewerSessionRevocationResponse summary);
    void createChannelSignalFull(OAIHttpRequestWorker *worker, OAICreateChannelResponse summary);
    void createRecordingConfigurationSignalFull(OAIHttpRequestWorker *worker, OAICreateRecordingConfigurationResponse summary);
    void createStreamKeySignalFull(OAIHttpRequestWorker *worker, OAICreateStreamKeyResponse summary);
    void deleteChannelSignalFull(OAIHttpRequestWorker *worker);
    void deletePlaybackKeyPairSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deleteRecordingConfigurationSignalFull(OAIHttpRequestWorker *worker);
    void deleteStreamKeySignalFull(OAIHttpRequestWorker *worker);
    void getChannelSignalFull(OAIHttpRequestWorker *worker, OAIGetChannelResponse summary);
    void getPlaybackKeyPairSignalFull(OAIHttpRequestWorker *worker, OAIGetPlaybackKeyPairResponse summary);
    void getRecordingConfigurationSignalFull(OAIHttpRequestWorker *worker, OAIGetRecordingConfigurationResponse summary);
    void getStreamSignalFull(OAIHttpRequestWorker *worker, OAIGetStreamResponse summary);
    void getStreamKeySignalFull(OAIHttpRequestWorker *worker, OAIGetStreamKeyResponse summary);
    void getStreamSessionSignalFull(OAIHttpRequestWorker *worker, OAIGetStreamSessionResponse summary);
    void importPlaybackKeyPairSignalFull(OAIHttpRequestWorker *worker, OAIImportPlaybackKeyPairResponse summary);
    void listChannelsSignalFull(OAIHttpRequestWorker *worker, OAIListChannelsResponse summary);
    void listPlaybackKeyPairsSignalFull(OAIHttpRequestWorker *worker, OAIListPlaybackKeyPairsResponse summary);
    void listRecordingConfigurationsSignalFull(OAIHttpRequestWorker *worker, OAIListRecordingConfigurationsResponse summary);
    void listStreamKeysSignalFull(OAIHttpRequestWorker *worker, OAIListStreamKeysResponse summary);
    void listStreamSessionsSignalFull(OAIHttpRequestWorker *worker, OAIListStreamSessionsResponse summary);
    void listStreamsSignalFull(OAIHttpRequestWorker *worker, OAIListStreamsResponse summary);
    void listTagsForResourceSignalFull(OAIHttpRequestWorker *worker, OAIListTagsForResourceResponse summary);
    void putMetadataSignalFull(OAIHttpRequestWorker *worker);
    void startViewerSessionRevocationSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void stopStreamSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void tagResourceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void untagResourceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateChannelSignalFull(OAIHttpRequestWorker *worker, OAIUpdateChannelResponse summary);

    Q_DECL_DEPRECATED_X("Use batchGetChannelSignalError() instead")
    void batchGetChannelSignalE(OAIBatchGetChannelResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void batchGetChannelSignalError(OAIBatchGetChannelResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchGetStreamKeySignalError() instead")
    void batchGetStreamKeySignalE(OAIBatchGetStreamKeyResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void batchGetStreamKeySignalError(OAIBatchGetStreamKeyResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchStartViewerSessionRevocationSignalError() instead")
    void batchStartViewerSessionRevocationSignalE(OAIBatchStartViewerSessionRevocationResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void batchStartViewerSessionRevocationSignalError(OAIBatchStartViewerSessionRevocationResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createChannelSignalError() instead")
    void createChannelSignalE(OAICreateChannelResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createChannelSignalError(OAICreateChannelResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createRecordingConfigurationSignalError() instead")
    void createRecordingConfigurationSignalE(OAICreateRecordingConfigurationResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createRecordingConfigurationSignalError(OAICreateRecordingConfigurationResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createStreamKeySignalError() instead")
    void createStreamKeySignalE(OAICreateStreamKeyResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createStreamKeySignalError(OAICreateStreamKeyResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteChannelSignalError() instead")
    void deleteChannelSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteChannelSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deletePlaybackKeyPairSignalError() instead")
    void deletePlaybackKeyPairSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deletePlaybackKeyPairSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRecordingConfigurationSignalError() instead")
    void deleteRecordingConfigurationSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRecordingConfigurationSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteStreamKeySignalError() instead")
    void deleteStreamKeySignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteStreamKeySignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getChannelSignalError() instead")
    void getChannelSignalE(OAIGetChannelResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getChannelSignalError(OAIGetChannelResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPlaybackKeyPairSignalError() instead")
    void getPlaybackKeyPairSignalE(OAIGetPlaybackKeyPairResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPlaybackKeyPairSignalError(OAIGetPlaybackKeyPairResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRecordingConfigurationSignalError() instead")
    void getRecordingConfigurationSignalE(OAIGetRecordingConfigurationResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getRecordingConfigurationSignalError(OAIGetRecordingConfigurationResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getStreamSignalError() instead")
    void getStreamSignalE(OAIGetStreamResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getStreamSignalError(OAIGetStreamResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getStreamKeySignalError() instead")
    void getStreamKeySignalE(OAIGetStreamKeyResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getStreamKeySignalError(OAIGetStreamKeyResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getStreamSessionSignalError() instead")
    void getStreamSessionSignalE(OAIGetStreamSessionResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getStreamSessionSignalError(OAIGetStreamSessionResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use importPlaybackKeyPairSignalError() instead")
    void importPlaybackKeyPairSignalE(OAIImportPlaybackKeyPairResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void importPlaybackKeyPairSignalError(OAIImportPlaybackKeyPairResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listChannelsSignalError() instead")
    void listChannelsSignalE(OAIListChannelsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listChannelsSignalError(OAIListChannelsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listPlaybackKeyPairsSignalError() instead")
    void listPlaybackKeyPairsSignalE(OAIListPlaybackKeyPairsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listPlaybackKeyPairsSignalError(OAIListPlaybackKeyPairsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRecordingConfigurationsSignalError() instead")
    void listRecordingConfigurationsSignalE(OAIListRecordingConfigurationsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listRecordingConfigurationsSignalError(OAIListRecordingConfigurationsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listStreamKeysSignalError() instead")
    void listStreamKeysSignalE(OAIListStreamKeysResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listStreamKeysSignalError(OAIListStreamKeysResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listStreamSessionsSignalError() instead")
    void listStreamSessionsSignalE(OAIListStreamSessionsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listStreamSessionsSignalError(OAIListStreamSessionsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listStreamsSignalError() instead")
    void listStreamsSignalE(OAIListStreamsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listStreamsSignalError(OAIListStreamsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listTagsForResourceSignalError() instead")
    void listTagsForResourceSignalE(OAIListTagsForResourceResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listTagsForResourceSignalError(OAIListTagsForResourceResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putMetadataSignalError() instead")
    void putMetadataSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void putMetadataSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use startViewerSessionRevocationSignalError() instead")
    void startViewerSessionRevocationSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void startViewerSessionRevocationSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use stopStreamSignalError() instead")
    void stopStreamSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void stopStreamSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tagResourceSignalError() instead")
    void tagResourceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tagResourceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use untagResourceSignalError() instead")
    void untagResourceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void untagResourceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateChannelSignalError() instead")
    void updateChannelSignalE(OAIUpdateChannelResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateChannelSignalError(OAIUpdateChannelResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use batchGetChannelSignalErrorFull() instead")
    void batchGetChannelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void batchGetChannelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchGetStreamKeySignalErrorFull() instead")
    void batchGetStreamKeySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void batchGetStreamKeySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use batchStartViewerSessionRevocationSignalErrorFull() instead")
    void batchStartViewerSessionRevocationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void batchStartViewerSessionRevocationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createChannelSignalErrorFull() instead")
    void createChannelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createChannelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createRecordingConfigurationSignalErrorFull() instead")
    void createRecordingConfigurationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createRecordingConfigurationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createStreamKeySignalErrorFull() instead")
    void createStreamKeySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createStreamKeySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteChannelSignalErrorFull() instead")
    void deleteChannelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteChannelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deletePlaybackKeyPairSignalErrorFull() instead")
    void deletePlaybackKeyPairSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deletePlaybackKeyPairSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRecordingConfigurationSignalErrorFull() instead")
    void deleteRecordingConfigurationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRecordingConfigurationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteStreamKeySignalErrorFull() instead")
    void deleteStreamKeySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteStreamKeySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getChannelSignalErrorFull() instead")
    void getChannelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getChannelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPlaybackKeyPairSignalErrorFull() instead")
    void getPlaybackKeyPairSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPlaybackKeyPairSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRecordingConfigurationSignalErrorFull() instead")
    void getRecordingConfigurationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getRecordingConfigurationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getStreamSignalErrorFull() instead")
    void getStreamSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getStreamSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getStreamKeySignalErrorFull() instead")
    void getStreamKeySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getStreamKeySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getStreamSessionSignalErrorFull() instead")
    void getStreamSessionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getStreamSessionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use importPlaybackKeyPairSignalErrorFull() instead")
    void importPlaybackKeyPairSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void importPlaybackKeyPairSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listChannelsSignalErrorFull() instead")
    void listChannelsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listChannelsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listPlaybackKeyPairsSignalErrorFull() instead")
    void listPlaybackKeyPairsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listPlaybackKeyPairsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRecordingConfigurationsSignalErrorFull() instead")
    void listRecordingConfigurationsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listRecordingConfigurationsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listStreamKeysSignalErrorFull() instead")
    void listStreamKeysSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listStreamKeysSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listStreamSessionsSignalErrorFull() instead")
    void listStreamSessionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listStreamSessionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listStreamsSignalErrorFull() instead")
    void listStreamsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listStreamsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listTagsForResourceSignalErrorFull() instead")
    void listTagsForResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listTagsForResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putMetadataSignalErrorFull() instead")
    void putMetadataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putMetadataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use startViewerSessionRevocationSignalErrorFull() instead")
    void startViewerSessionRevocationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void startViewerSessionRevocationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use stopStreamSignalErrorFull() instead")
    void stopStreamSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void stopStreamSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tagResourceSignalErrorFull() instead")
    void tagResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tagResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use untagResourceSignalErrorFull() instead")
    void untagResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void untagResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateChannelSignalErrorFull() instead")
    void updateChannelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateChannelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
