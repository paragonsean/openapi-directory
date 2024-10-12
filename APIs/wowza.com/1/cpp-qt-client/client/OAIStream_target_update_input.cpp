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

#include "OAIStream_target_update_input.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStream_target_update_input::OAIStream_target_update_input(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStream_target_update_input::OAIStream_target_update_input() {
    this->initializeModel();
}

OAIStream_target_update_input::~OAIStream_target_update_input() {}

void OAIStream_target_update_input::initializeModel() {

    m_stream_target_isSet = false;
    m_stream_target_isValid = false;
}

void OAIStream_target_update_input::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStream_target_update_input::fromJsonObject(QJsonObject json) {

    m_stream_target_isValid = ::OpenAPI::fromJsonValue(m_stream_target, json[QString("stream_target")]);
    m_stream_target_isSet = !json[QString("stream_target")].isNull() && m_stream_target_isValid;
}

QString OAIStream_target_update_input::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStream_target_update_input::asJsonObject() const {
    QJsonObject obj;
    if (m_stream_target.isSet()) {
        obj.insert(QString("stream_target"), ::OpenAPI::toJsonValue(m_stream_target));
    }
    return obj;
}

OAIStream_target_6 OAIStream_target_update_input::getStreamTarget() const {
    return m_stream_target;
}
void OAIStream_target_update_input::setStreamTarget(const OAIStream_target_6 &stream_target) {
    m_stream_target = stream_target;
    m_stream_target_isSet = true;
}

bool OAIStream_target_update_input::is_stream_target_Set() const{
    return m_stream_target_isSet;
}

bool OAIStream_target_update_input::is_stream_target_Valid() const{
    return m_stream_target_isValid;
}

bool OAIStream_target_update_input::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_stream_target.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStream_target_update_input::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_stream_target_isValid && true;
}

} // namespace OpenAPI
