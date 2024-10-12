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

#include "OAIIntegrationLinkType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIntegrationLinkType::OAIIntegrationLinkType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIntegrationLinkType::OAIIntegrationLinkType() {
    this->initializeModel();
}

OAIIntegrationLinkType::~OAIIntegrationLinkType() {}

void OAIIntegrationLinkType::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIIntegrationLinkType::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIIntegrationLinkType::fromJson(QString jsonString) {
    
    if ( jsonString.compare("trello", Qt::CaseInsensitive) == 0) {
        m_value = eOAIIntegrationLinkType::TRELLO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("jira", Qt::CaseInsensitive) == 0) {
        m_value = eOAIIntegrationLinkType::JIRA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("monday", Qt::CaseInsensitive) == 0) {
        m_value = eOAIIntegrationLinkType::MONDAY;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIIntegrationLinkType::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIIntegrationLinkType::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIIntegrationLinkType::TRELLO:
            val = "trello";
            break;
        case eOAIIntegrationLinkType::JIRA:
            val = "jira";
            break;
        case eOAIIntegrationLinkType::MONDAY:
            val = "monday";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIIntegrationLinkType::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIIntegrationLinkType::eOAIIntegrationLinkType OAIIntegrationLinkType::getValue() const {
    return m_value;
}

void OAIIntegrationLinkType::setValue(const OAIIntegrationLinkType::eOAIIntegrationLinkType& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIIntegrationLinkType::isSet() const {
    
    return m_value_isSet;
}

bool OAIIntegrationLinkType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
