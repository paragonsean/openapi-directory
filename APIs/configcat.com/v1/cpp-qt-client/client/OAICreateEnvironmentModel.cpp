/**
 * ConfigCat Public Management API
 * **Base API URL**: https://api.configcat.com  If you prefer the swagger documentation, you can find it here: [Swagger UI](https://api.configcat.com/swagger).  The purpose of this API is to access the ConfigCat platform programmatically.  You can **Create**, **Read**, **Update** and **Delete** any entities like **Feature Flags, Configs, Environments** or **Products** within ConfigCat.   The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON  and JSON+HAL format. Do not use this API for accessing and evaluating feature flag values. Use the [SDKs instead](https://configcat.com/docs/sdk-reference/overview).   # OpenAPI Specification  The complete specification is publicly available here: [swagger.json](v1/swagger.json).  You can use it to generate client libraries in various languages with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) or [Swagger Codegen](https://swagger.io/tools/swagger-codegen/) to interact with this API.  # Authentication This API uses the [Basic HTTP Authentication Scheme](https://en.wikipedia.org/wiki/Basic_access_authentication).   <!-- ReDoc-Inject: <security-definitions> -->  # Throttling and rate limits All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:  | Header | Description | | :- | :- | | X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. | | X-Rate-Limit-Reset     | The time when the current rate limit period resets.        |  When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header. 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@configcat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICreateEnvironmentModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateEnvironmentModel::OAICreateEnvironmentModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateEnvironmentModel::OAICreateEnvironmentModel() {
    this->initializeModel();
}

OAICreateEnvironmentModel::~OAICreateEnvironmentModel() {}

void OAICreateEnvironmentModel::initializeModel() {

    m_color_isSet = false;
    m_color_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAICreateEnvironmentModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateEnvironmentModel::fromJsonObject(QJsonObject json) {

    m_color_isValid = ::OpenAPI::fromJsonValue(m_color, json[QString("color")]);
    m_color_isSet = !json[QString("color")].isNull() && m_color_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAICreateEnvironmentModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateEnvironmentModel::asJsonObject() const {
    QJsonObject obj;
    if (m_color_isSet) {
        obj.insert(QString("color"), ::OpenAPI::toJsonValue(m_color));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAICreateEnvironmentModel::getColor() const {
    return m_color;
}
void OAICreateEnvironmentModel::setColor(const QString &color) {
    m_color = color;
    m_color_isSet = true;
}

bool OAICreateEnvironmentModel::is_color_Set() const{
    return m_color_isSet;
}

bool OAICreateEnvironmentModel::is_color_Valid() const{
    return m_color_isValid;
}

QString OAICreateEnvironmentModel::getDescription() const {
    return m_description;
}
void OAICreateEnvironmentModel::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAICreateEnvironmentModel::is_description_Set() const{
    return m_description_isSet;
}

bool OAICreateEnvironmentModel::is_description_Valid() const{
    return m_description_isValid;
}

QString OAICreateEnvironmentModel::getName() const {
    return m_name;
}
void OAICreateEnvironmentModel::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateEnvironmentModel::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateEnvironmentModel::is_name_Valid() const{
    return m_name_isValid;
}

bool OAICreateEnvironmentModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateEnvironmentModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
