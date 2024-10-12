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

#include "OAIEnvironmentAccessType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEnvironmentAccessType::OAIEnvironmentAccessType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEnvironmentAccessType::OAIEnvironmentAccessType() {
    this->initializeModel();
}

OAIEnvironmentAccessType::~OAIEnvironmentAccessType() {}

void OAIEnvironmentAccessType::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIEnvironmentAccessType::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIEnvironmentAccessType::fromJson(QString jsonString) {
    
    if ( jsonString.compare("full", Qt::CaseInsensitive) == 0) {
        m_value = eOAIEnvironmentAccessType::FULL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("readOnly", Qt::CaseInsensitive) == 0) {
        m_value = eOAIEnvironmentAccessType::READONLY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("none", Qt::CaseInsensitive) == 0) {
        m_value = eOAIEnvironmentAccessType::NONE;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIEnvironmentAccessType::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIEnvironmentAccessType::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIEnvironmentAccessType::FULL:
            val = "full";
            break;
        case eOAIEnvironmentAccessType::READONLY:
            val = "readOnly";
            break;
        case eOAIEnvironmentAccessType::NONE:
            val = "none";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIEnvironmentAccessType::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIEnvironmentAccessType::eOAIEnvironmentAccessType OAIEnvironmentAccessType::getValue() const {
    return m_value;
}

void OAIEnvironmentAccessType::setValue(const OAIEnvironmentAccessType::eOAIEnvironmentAccessType& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIEnvironmentAccessType::isSet() const {
    
    return m_value_isSet;
}

bool OAIEnvironmentAccessType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
