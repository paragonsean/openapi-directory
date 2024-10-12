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

#include "OAIHash_of_zones.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHash_of_zones::OAIHash_of_zones(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHash_of_zones::OAIHash_of_zones() {
    this->initializeModel();
}

OAIHash_of_zones::~OAIHash_of_zones() {}

void OAIHash_of_zones::initializeModel() {

    m_bytes_billed_isSet = false;
    m_bytes_billed_isValid = false;

    m_bytes_used_isSet = false;
    m_bytes_used_isValid = false;
}

void OAIHash_of_zones::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHash_of_zones::fromJsonObject(QJsonObject json) {

    m_bytes_billed_isValid = ::OpenAPI::fromJsonValue(m_bytes_billed, json[QString("bytes_billed")]);
    m_bytes_billed_isSet = !json[QString("bytes_billed")].isNull() && m_bytes_billed_isValid;

    m_bytes_used_isValid = ::OpenAPI::fromJsonValue(m_bytes_used, json[QString("bytes_used")]);
    m_bytes_used_isSet = !json[QString("bytes_used")].isNull() && m_bytes_used_isValid;
}

QString OAIHash_of_zones::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHash_of_zones::asJsonObject() const {
    QJsonObject obj;
    if (m_bytes_billed_isSet) {
        obj.insert(QString("bytes_billed"), ::OpenAPI::toJsonValue(m_bytes_billed));
    }
    if (m_bytes_used_isSet) {
        obj.insert(QString("bytes_used"), ::OpenAPI::toJsonValue(m_bytes_used));
    }
    return obj;
}

qint32 OAIHash_of_zones::getBytesBilled() const {
    return m_bytes_billed;
}
void OAIHash_of_zones::setBytesBilled(const qint32 &bytes_billed) {
    m_bytes_billed = bytes_billed;
    m_bytes_billed_isSet = true;
}

bool OAIHash_of_zones::is_bytes_billed_Set() const{
    return m_bytes_billed_isSet;
}

bool OAIHash_of_zones::is_bytes_billed_Valid() const{
    return m_bytes_billed_isValid;
}

qint32 OAIHash_of_zones::getBytesUsed() const {
    return m_bytes_used;
}
void OAIHash_of_zones::setBytesUsed(const qint32 &bytes_used) {
    m_bytes_used = bytes_used;
    m_bytes_used_isSet = true;
}

bool OAIHash_of_zones::is_bytes_used_Set() const{
    return m_bytes_used_isSet;
}

bool OAIHash_of_zones::is_bytes_used_Valid() const{
    return m_bytes_used_isValid;
}

bool OAIHash_of_zones::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bytes_billed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bytes_used_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHash_of_zones::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
