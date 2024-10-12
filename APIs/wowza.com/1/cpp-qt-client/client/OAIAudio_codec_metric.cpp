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

#include "OAIAudio_codec_metric.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAudio_codec_metric::OAIAudio_codec_metric(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAudio_codec_metric::OAIAudio_codec_metric() {
    this->initializeModel();
}

OAIAudio_codec_metric::~OAIAudio_codec_metric() {}

void OAIAudio_codec_metric::initializeModel() {

    m_status_isSet = false;
    m_status_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;

    m_units_isSet = false;
    m_units_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIAudio_codec_metric::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAudio_codec_metric::fromJsonObject(QJsonObject json) {

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;

    m_units_isValid = ::OpenAPI::fromJsonValue(m_units, json[QString("units")]);
    m_units_isSet = !json[QString("units")].isNull() && m_units_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIAudio_codec_metric::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAudio_codec_metric::asJsonObject() const {
    QJsonObject obj;
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    if (m_units_isSet) {
        obj.insert(QString("units"), ::OpenAPI::toJsonValue(m_units));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIAudio_codec_metric::getStatus() const {
    return m_status;
}
void OAIAudio_codec_metric::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIAudio_codec_metric::is_status_Set() const{
    return m_status_isSet;
}

bool OAIAudio_codec_metric::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIAudio_codec_metric::getText() const {
    return m_text;
}
void OAIAudio_codec_metric::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIAudio_codec_metric::is_text_Set() const{
    return m_text_isSet;
}

bool OAIAudio_codec_metric::is_text_Valid() const{
    return m_text_isValid;
}

QString OAIAudio_codec_metric::getUnits() const {
    return m_units;
}
void OAIAudio_codec_metric::setUnits(const QString &units) {
    m_units = units;
    m_units_isSet = true;
}

bool OAIAudio_codec_metric::is_units_Set() const{
    return m_units_isSet;
}

bool OAIAudio_codec_metric::is_units_Valid() const{
    return m_units_isValid;
}

QString OAIAudio_codec_metric::getValue() const {
    return m_value;
}
void OAIAudio_codec_metric::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIAudio_codec_metric::is_value_Set() const{
    return m_value_isSet;
}

bool OAIAudio_codec_metric::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIAudio_codec_metric::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_units_isSet) {
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

bool OAIAudio_codec_metric::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
