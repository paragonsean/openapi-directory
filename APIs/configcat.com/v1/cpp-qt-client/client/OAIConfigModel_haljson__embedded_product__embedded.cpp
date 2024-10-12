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

#include "OAIConfigModel_haljson__embedded_product__embedded.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConfigModel_haljson__embedded_product__embedded::OAIConfigModel_haljson__embedded_product__embedded(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConfigModel_haljson__embedded_product__embedded::OAIConfigModel_haljson__embedded_product__embedded() {
    this->initializeModel();
}

OAIConfigModel_haljson__embedded_product__embedded::~OAIConfigModel_haljson__embedded_product__embedded() {}

void OAIConfigModel_haljson__embedded_product__embedded::initializeModel() {

    m_organization_isSet = false;
    m_organization_isValid = false;
}

void OAIConfigModel_haljson__embedded_product__embedded::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConfigModel_haljson__embedded_product__embedded::fromJsonObject(QJsonObject json) {

    m_organization_isValid = ::OpenAPI::fromJsonValue(m_organization, json[QString("organization")]);
    m_organization_isSet = !json[QString("organization")].isNull() && m_organization_isValid;
}

QString OAIConfigModel_haljson__embedded_product__embedded::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConfigModel_haljson__embedded_product__embedded::asJsonObject() const {
    QJsonObject obj;
    if (m_organization.isSet()) {
        obj.insert(QString("organization"), ::OpenAPI::toJsonValue(m_organization));
    }
    return obj;
}

OAIConfigModel_haljson__embedded_product__embedded_organization OAIConfigModel_haljson__embedded_product__embedded::getOrganization() const {
    return m_organization;
}
void OAIConfigModel_haljson__embedded_product__embedded::setOrganization(const OAIConfigModel_haljson__embedded_product__embedded_organization &organization) {
    m_organization = organization;
    m_organization_isSet = true;
}

bool OAIConfigModel_haljson__embedded_product__embedded::is_organization_Set() const{
    return m_organization_isSet;
}

bool OAIConfigModel_haljson__embedded_product__embedded::is_organization_Valid() const{
    return m_organization_isValid;
}

bool OAIConfigModel_haljson__embedded_product__embedded::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_organization.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConfigModel_haljson__embedded_product__embedded::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
