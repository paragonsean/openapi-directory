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

#include "OAITranscoder_property.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITranscoder_property::OAITranscoder_property(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITranscoder_property::OAITranscoder_property() {
    this->initializeModel();
}

OAITranscoder_property::~OAITranscoder_property() {}

void OAITranscoder_property::initializeModel() {

    m_key_isSet = false;
    m_key_isValid = false;

    m_section_isSet = false;
    m_section_isValid = false;

    m_transcoder_id_isSet = false;
    m_transcoder_id_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAITranscoder_property::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITranscoder_property::fromJsonObject(QJsonObject json) {

    m_key_isValid = ::OpenAPI::fromJsonValue(m_key, json[QString("key")]);
    m_key_isSet = !json[QString("key")].isNull() && m_key_isValid;

    m_section_isValid = ::OpenAPI::fromJsonValue(m_section, json[QString("section")]);
    m_section_isSet = !json[QString("section")].isNull() && m_section_isValid;

    m_transcoder_id_isValid = ::OpenAPI::fromJsonValue(m_transcoder_id, json[QString("transcoder_id")]);
    m_transcoder_id_isSet = !json[QString("transcoder_id")].isNull() && m_transcoder_id_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAITranscoder_property::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITranscoder_property::asJsonObject() const {
    QJsonObject obj;
    if (m_key_isSet) {
        obj.insert(QString("key"), ::OpenAPI::toJsonValue(m_key));
    }
    if (m_section_isSet) {
        obj.insert(QString("section"), ::OpenAPI::toJsonValue(m_section));
    }
    if (m_transcoder_id_isSet) {
        obj.insert(QString("transcoder_id"), ::OpenAPI::toJsonValue(m_transcoder_id));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAITranscoder_property::getKey() const {
    return m_key;
}
void OAITranscoder_property::setKey(const QString &key) {
    m_key = key;
    m_key_isSet = true;
}

bool OAITranscoder_property::is_key_Set() const{
    return m_key_isSet;
}

bool OAITranscoder_property::is_key_Valid() const{
    return m_key_isValid;
}

QString OAITranscoder_property::getSection() const {
    return m_section;
}
void OAITranscoder_property::setSection(const QString &section) {
    m_section = section;
    m_section_isSet = true;
}

bool OAITranscoder_property::is_section_Set() const{
    return m_section_isSet;
}

bool OAITranscoder_property::is_section_Valid() const{
    return m_section_isValid;
}

QString OAITranscoder_property::getTranscoderId() const {
    return m_transcoder_id;
}
void OAITranscoder_property::setTranscoderId(const QString &transcoder_id) {
    m_transcoder_id = transcoder_id;
    m_transcoder_id_isSet = true;
}

bool OAITranscoder_property::is_transcoder_id_Set() const{
    return m_transcoder_id_isSet;
}

bool OAITranscoder_property::is_transcoder_id_Valid() const{
    return m_transcoder_id_isValid;
}

QString OAITranscoder_property::getValue() const {
    return m_value;
}
void OAITranscoder_property::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAITranscoder_property::is_value_Set() const{
    return m_value_isSet;
}

bool OAITranscoder_property::is_value_Valid() const{
    return m_value_isValid;
}

bool OAITranscoder_property::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_section_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transcoder_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITranscoder_property::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
