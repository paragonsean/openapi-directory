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

#include "OAIShowTranscoderStats_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShowTranscoderStats_200_response::OAIShowTranscoderStats_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShowTranscoderStats_200_response::OAIShowTranscoderStats_200_response() {
    this->initializeModel();
}

OAIShowTranscoderStats_200_response::~OAIShowTranscoderStats_200_response() {}

void OAIShowTranscoderStats_200_response::initializeModel() {

    m_transcoder_isSet = false;
    m_transcoder_isValid = false;
}

void OAIShowTranscoderStats_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShowTranscoderStats_200_response::fromJsonObject(QJsonObject json) {

    m_transcoder_isValid = ::OpenAPI::fromJsonValue(m_transcoder, json[QString("transcoder")]);
    m_transcoder_isSet = !json[QString("transcoder")].isNull() && m_transcoder_isValid;
}

QString OAIShowTranscoderStats_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShowTranscoderStats_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_transcoder.isSet()) {
        obj.insert(QString("transcoder"), ::OpenAPI::toJsonValue(m_transcoder));
    }
    return obj;
}

OAIShm_metrics OAIShowTranscoderStats_200_response::getTranscoder() const {
    return m_transcoder;
}
void OAIShowTranscoderStats_200_response::setTranscoder(const OAIShm_metrics &transcoder) {
    m_transcoder = transcoder;
    m_transcoder_isSet = true;
}

bool OAIShowTranscoderStats_200_response::is_transcoder_Set() const{
    return m_transcoder_isSet;
}

bool OAIShowTranscoderStats_200_response::is_transcoder_Valid() const{
    return m_transcoder_isValid;
}

bool OAIShowTranscoderStats_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_transcoder.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIShowTranscoderStats_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_transcoder_isValid && true;
}

} // namespace OpenAPI
