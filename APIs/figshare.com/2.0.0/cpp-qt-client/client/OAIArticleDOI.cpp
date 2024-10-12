/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIArticleDOI.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArticleDOI::OAIArticleDOI(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArticleDOI::OAIArticleDOI() {
    this->initializeModel();
}

OAIArticleDOI::~OAIArticleDOI() {}

void OAIArticleDOI::initializeModel() {

    m_doi_isSet = false;
    m_doi_isValid = false;
}

void OAIArticleDOI::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArticleDOI::fromJsonObject(QJsonObject json) {

    m_doi_isValid = ::OpenAPI::fromJsonValue(m_doi, json[QString("doi")]);
    m_doi_isSet = !json[QString("doi")].isNull() && m_doi_isValid;
}

QString OAIArticleDOI::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArticleDOI::asJsonObject() const {
    QJsonObject obj;
    if (m_doi_isSet) {
        obj.insert(QString("doi"), ::OpenAPI::toJsonValue(m_doi));
    }
    return obj;
}

QString OAIArticleDOI::getDoi() const {
    return m_doi;
}
void OAIArticleDOI::setDoi(const QString &doi) {
    m_doi = doi;
    m_doi_isSet = true;
}

bool OAIArticleDOI::is_doi_Set() const{
    return m_doi_isSet;
}

bool OAIArticleDOI::is_doi_Valid() const{
    return m_doi_isValid;
}

bool OAIArticleDOI::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_doi_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArticleDOI::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_doi_isValid && true;
}

} // namespace OpenAPI
