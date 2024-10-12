/**
 * Wowza Streaming Cloud REST API Reference Documentation
 *  # About the REST API  The Wowza Streaming Cloud<sup>TM</sup> REST API (application programming interface) offers complete programmatic control over live streams, transcoders, stream sources, and stream targets. Anything you can do in the Wowza Streaming Cloud UI can also be achieved by making HTTP-based requests to cloud-based servers through the REST API.  The Wowza Streaming Cloud REST API features *cross-origin resource sharing*, or CORS. CORS is a [W3C specification](https://www.w3.org/TR/cors/) that provides headers in HTTP requests to enable a web server to safely make a network request to another domain.  In order to protect shared resources, the Wowza Streaming Cloud REST API is subject to limits. For details, see [Wowza Streaming Cloud REST API limits](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api-limits). # About this documentation This reference documentation is based on the open-source [Swagger framework](http://swagger.io/specification/). It allows you to view the operations, parameters, and request and reponse schemas for every resource. Request samples are presented in cURL (Shell) and JavaScript; some samples also include just the JSON object. Response samples are all JSON.  For more information and examples on using the Wowza Streaming Cloud REST API, see our [library of Wowza Streaming Cloud REST API technical articles](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api).  # Query requirements The Wowza Streaming Cloud REST API uses HTTP requests to retrieve data from cloud-based servers. Requests must contain proper JSON, two authentication keys, and the correct version number in the base path.  ## JSON The Wowza Streaming Cloud REST API uses the [JSON API specification](http://jsonapi.org/format/) to request and return data. This means requests must include the header `Content-Type: application/json` and must include a single resource object in JSON format as primary data.  Responses include HTTP status codes that indicate whether the query was successful. If there was an error, a description explains the problem so that you can fix it and try again.  ## Authentication Requests to the Wowza Streaming Cloud REST API must be authenticated with two keys: an API key and an access key. Each key is a 64-character alphanumeric string that you can find on the **API Access** page in Wowza Streaming Cloud.  Use the `wsc-api-key` and `wsc-access-key` headers to authenticate requests, like this (in cURL):  ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]' ```  <!-- ReDoc-Inject: <security-definitions> -->  ## Version The Wowza Streaming Cloud API is currently at version 1.0.0. Use `v1` in your base path in every request, like this path to the live_streams endpoint: ``` https://api.cloud.wowza.com/api/v1/live_streams ``` ## Example query Here is a complete example POST request, in cURL, with proper JSON syntax, headers, authentication, and version information: ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]'   -H 'Content-Type: application/json' -X POST -d '{     \"live_stream\": {       \"name\": \"My live Stream\",       \"...\": \"...\"     }   }' https://api.cloud.wowza.com/api/v1/live_streams ``` 
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISchedule_4.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISchedule_4::OAISchedule_4(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISchedule_4::OAISchedule_4() {
    this->initializeModel();
}

OAISchedule_4::~OAISchedule_4() {}

void OAISchedule_4::initializeModel() {

    m_action_type_isSet = false;
    m_action_type_isValid = false;

    m_end_repeat_isSet = false;
    m_end_repeat_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_recurrence_data_isSet = false;
    m_recurrence_data_isValid = false;

    m_start_repeat_isSet = false;
    m_start_repeat_isValid = false;

    m_start_transcoder_isSet = false;
    m_start_transcoder_isValid = false;

    m_stop_transcoder_isSet = false;
    m_stop_transcoder_isValid = false;
}

void OAISchedule_4::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISchedule_4::fromJsonObject(QJsonObject json) {

    m_action_type_isValid = ::OpenAPI::fromJsonValue(m_action_type, json[QString("action_type")]);
    m_action_type_isSet = !json[QString("action_type")].isNull() && m_action_type_isValid;

    m_end_repeat_isValid = ::OpenAPI::fromJsonValue(m_end_repeat, json[QString("end_repeat")]);
    m_end_repeat_isSet = !json[QString("end_repeat")].isNull() && m_end_repeat_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_recurrence_data_isValid = ::OpenAPI::fromJsonValue(m_recurrence_data, json[QString("recurrence_data")]);
    m_recurrence_data_isSet = !json[QString("recurrence_data")].isNull() && m_recurrence_data_isValid;

    m_start_repeat_isValid = ::OpenAPI::fromJsonValue(m_start_repeat, json[QString("start_repeat")]);
    m_start_repeat_isSet = !json[QString("start_repeat")].isNull() && m_start_repeat_isValid;

    m_start_transcoder_isValid = ::OpenAPI::fromJsonValue(m_start_transcoder, json[QString("start_transcoder")]);
    m_start_transcoder_isSet = !json[QString("start_transcoder")].isNull() && m_start_transcoder_isValid;

    m_stop_transcoder_isValid = ::OpenAPI::fromJsonValue(m_stop_transcoder, json[QString("stop_transcoder")]);
    m_stop_transcoder_isSet = !json[QString("stop_transcoder")].isNull() && m_stop_transcoder_isValid;
}

QString OAISchedule_4::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISchedule_4::asJsonObject() const {
    QJsonObject obj;
    if (m_action_type_isSet) {
        obj.insert(QString("action_type"), ::OpenAPI::toJsonValue(m_action_type));
    }
    if (m_end_repeat_isSet) {
        obj.insert(QString("end_repeat"), ::OpenAPI::toJsonValue(m_end_repeat));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_recurrence_data_isSet) {
        obj.insert(QString("recurrence_data"), ::OpenAPI::toJsonValue(m_recurrence_data));
    }
    if (m_start_repeat_isSet) {
        obj.insert(QString("start_repeat"), ::OpenAPI::toJsonValue(m_start_repeat));
    }
    if (m_start_transcoder_isSet) {
        obj.insert(QString("start_transcoder"), ::OpenAPI::toJsonValue(m_start_transcoder));
    }
    if (m_stop_transcoder_isSet) {
        obj.insert(QString("stop_transcoder"), ::OpenAPI::toJsonValue(m_stop_transcoder));
    }
    return obj;
}

QString OAISchedule_4::getActionType() const {
    return m_action_type;
}
void OAISchedule_4::setActionType(const QString &action_type) {
    m_action_type = action_type;
    m_action_type_isSet = true;
}

bool OAISchedule_4::is_action_type_Set() const{
    return m_action_type_isSet;
}

bool OAISchedule_4::is_action_type_Valid() const{
    return m_action_type_isValid;
}

QDate OAISchedule_4::getEndRepeat() const {
    return m_end_repeat;
}
void OAISchedule_4::setEndRepeat(const QDate &end_repeat) {
    m_end_repeat = end_repeat;
    m_end_repeat_isSet = true;
}

bool OAISchedule_4::is_end_repeat_Set() const{
    return m_end_repeat_isSet;
}

bool OAISchedule_4::is_end_repeat_Valid() const{
    return m_end_repeat_isValid;
}

QString OAISchedule_4::getName() const {
    return m_name;
}
void OAISchedule_4::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISchedule_4::is_name_Set() const{
    return m_name_isSet;
}

bool OAISchedule_4::is_name_Valid() const{
    return m_name_isValid;
}

QString OAISchedule_4::getRecurrenceData() const {
    return m_recurrence_data;
}
void OAISchedule_4::setRecurrenceData(const QString &recurrence_data) {
    m_recurrence_data = recurrence_data;
    m_recurrence_data_isSet = true;
}

bool OAISchedule_4::is_recurrence_data_Set() const{
    return m_recurrence_data_isSet;
}

bool OAISchedule_4::is_recurrence_data_Valid() const{
    return m_recurrence_data_isValid;
}

QDate OAISchedule_4::getStartRepeat() const {
    return m_start_repeat;
}
void OAISchedule_4::setStartRepeat(const QDate &start_repeat) {
    m_start_repeat = start_repeat;
    m_start_repeat_isSet = true;
}

bool OAISchedule_4::is_start_repeat_Set() const{
    return m_start_repeat_isSet;
}

bool OAISchedule_4::is_start_repeat_Valid() const{
    return m_start_repeat_isValid;
}

QDateTime OAISchedule_4::getStartTranscoder() const {
    return m_start_transcoder;
}
void OAISchedule_4::setStartTranscoder(const QDateTime &start_transcoder) {
    m_start_transcoder = start_transcoder;
    m_start_transcoder_isSet = true;
}

bool OAISchedule_4::is_start_transcoder_Set() const{
    return m_start_transcoder_isSet;
}

bool OAISchedule_4::is_start_transcoder_Valid() const{
    return m_start_transcoder_isValid;
}

QDateTime OAISchedule_4::getStopTranscoder() const {
    return m_stop_transcoder;
}
void OAISchedule_4::setStopTranscoder(const QDateTime &stop_transcoder) {
    m_stop_transcoder = stop_transcoder;
    m_stop_transcoder_isSet = true;
}

bool OAISchedule_4::is_stop_transcoder_Set() const{
    return m_stop_transcoder_isSet;
}

bool OAISchedule_4::is_stop_transcoder_Valid() const{
    return m_stop_transcoder_isValid;
}

bool OAISchedule_4::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_repeat_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recurrence_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_repeat_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_transcoder_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stop_transcoder_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISchedule_4::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_action_type_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
