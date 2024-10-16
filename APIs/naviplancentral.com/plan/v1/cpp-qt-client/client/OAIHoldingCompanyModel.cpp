/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHoldingCompanyModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHoldingCompanyModel::OAIHoldingCompanyModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHoldingCompanyModel::OAIHoldingCompanyModel() {
    this->initializeModel();
}

OAIHoldingCompanyModel::~OAIHoldingCompanyModel() {}

void OAIHoldingCompanyModel::initializeModel() {

    m_holding_company_isSet = false;
    m_holding_company_isValid = false;

    m_links_isSet = false;
    m_links_isValid = false;
}

void OAIHoldingCompanyModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHoldingCompanyModel::fromJsonObject(QJsonObject json) {

    m_holding_company_isValid = ::OpenAPI::fromJsonValue(m_holding_company, json[QString("holdingCompany")]);
    m_holding_company_isSet = !json[QString("holdingCompany")].isNull() && m_holding_company_isValid;

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;
}

QString OAIHoldingCompanyModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHoldingCompanyModel::asJsonObject() const {
    QJsonObject obj;
    if (m_holding_company.isSet()) {
        obj.insert(QString("holdingCompany"), ::OpenAPI::toJsonValue(m_holding_company));
    }
    if (m_links.size() > 0) {
        obj.insert(QString("links"), ::OpenAPI::toJsonValue(m_links));
    }
    return obj;
}

OAIIHoldingCompany OAIHoldingCompanyModel::getHoldingCompany() const {
    return m_holding_company;
}
void OAIHoldingCompanyModel::setHoldingCompany(const OAIIHoldingCompany &holding_company) {
    m_holding_company = holding_company;
    m_holding_company_isSet = true;
}

bool OAIHoldingCompanyModel::is_holding_company_Set() const{
    return m_holding_company_isSet;
}

bool OAIHoldingCompanyModel::is_holding_company_Valid() const{
    return m_holding_company_isValid;
}

QList<OAIObjectLink> OAIHoldingCompanyModel::getLinks() const {
    return m_links;
}
void OAIHoldingCompanyModel::setLinks(const QList<OAIObjectLink> &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAIHoldingCompanyModel::is_links_Set() const{
    return m_links_isSet;
}

bool OAIHoldingCompanyModel::is_links_Valid() const{
    return m_links_isValid;
}

bool OAIHoldingCompanyModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_holding_company.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHoldingCompanyModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
