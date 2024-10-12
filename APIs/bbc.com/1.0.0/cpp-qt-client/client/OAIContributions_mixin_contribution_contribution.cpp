/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIContributions_mixin_contribution_contribution.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIContributions_mixin_contribution_contribution::OAIContributions_mixin_contribution_contribution(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIContributions_mixin_contribution_contribution::OAIContributions_mixin_contribution_contribution() {
    this->initializeModel();
}

OAIContributions_mixin_contribution_contribution::~OAIContributions_mixin_contribution_contribution() {}

void OAIContributions_mixin_contribution_contribution::initializeModel() {

    m_character_name_isSet = false;
    m_character_name_isValid = false;

    m_contribution_isSet = false;
    m_contribution_isValid = false;

    m_contributions_mixin_contributor_isSet = false;
    m_contributions_mixin_contributor_isValid = false;

    m_credit_role_isSet = false;
    m_credit_role_isValid = false;
}

void OAIContributions_mixin_contribution_contribution::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIContributions_mixin_contribution_contribution::fromJsonObject(QJsonObject json) {

    m_character_name_isValid = ::OpenAPI::fromJsonValue(m_character_name, json[QString("character_name")]);
    m_character_name_isSet = !json[QString("character_name")].isNull() && m_character_name_isValid;

    m_contribution_isValid = ::OpenAPI::fromJsonValue(m_contribution, json[QString("contribution")]);
    m_contribution_isSet = !json[QString("contribution")].isNull() && m_contribution_isValid;

    m_contributions_mixin_contributor_isValid = ::OpenAPI::fromJsonValue(m_contributions_mixin_contributor, json[QString("contributions_mixin_contributor")]);
    m_contributions_mixin_contributor_isSet = !json[QString("contributions_mixin_contributor")].isNull() && m_contributions_mixin_contributor_isValid;

    m_credit_role_isValid = ::OpenAPI::fromJsonValue(m_credit_role, json[QString("credit_role")]);
    m_credit_role_isSet = !json[QString("credit_role")].isNull() && m_credit_role_isValid;
}

QString OAIContributions_mixin_contribution_contribution::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIContributions_mixin_contribution_contribution::asJsonObject() const {
    QJsonObject obj;
    if (m_character_name_isSet) {
        obj.insert(QString("character_name"), ::OpenAPI::toJsonValue(m_character_name));
    }
    if (m_contribution.isSet()) {
        obj.insert(QString("contribution"), ::OpenAPI::toJsonValue(m_contribution));
    }
    if (m_contributions_mixin_contributor.isSet()) {
        obj.insert(QString("contributions_mixin_contributor"), ::OpenAPI::toJsonValue(m_contributions_mixin_contributor));
    }
    if (m_credit_role.isSet()) {
        obj.insert(QString("credit_role"), ::OpenAPI::toJsonValue(m_credit_role));
    }
    return obj;
}

QString OAIContributions_mixin_contribution_contribution::getCharacterName() const {
    return m_character_name;
}
void OAIContributions_mixin_contribution_contribution::setCharacterName(const QString &character_name) {
    m_character_name = character_name;
    m_character_name_isSet = true;
}

bool OAIContributions_mixin_contribution_contribution::is_character_name_Set() const{
    return m_character_name_isSet;
}

bool OAIContributions_mixin_contribution_contribution::is_character_name_Valid() const{
    return m_character_name_isValid;
}

OAIContributions_mixin_contribution_contribution_contribution OAIContributions_mixin_contribution_contribution::getContribution() const {
    return m_contribution;
}
void OAIContributions_mixin_contribution_contribution::setContribution(const OAIContributions_mixin_contribution_contribution_contribution &contribution) {
    m_contribution = contribution;
    m_contribution_isSet = true;
}

bool OAIContributions_mixin_contribution_contribution::is_contribution_Set() const{
    return m_contribution_isSet;
}

bool OAIContributions_mixin_contribution_contribution::is_contribution_Valid() const{
    return m_contribution_isValid;
}

OAIContributions_mixin_contributor OAIContributions_mixin_contribution_contribution::getContributionsMixinContributor() const {
    return m_contributions_mixin_contributor;
}
void OAIContributions_mixin_contribution_contribution::setContributionsMixinContributor(const OAIContributions_mixin_contributor &contributions_mixin_contributor) {
    m_contributions_mixin_contributor = contributions_mixin_contributor;
    m_contributions_mixin_contributor_isSet = true;
}

bool OAIContributions_mixin_contribution_contribution::is_contributions_mixin_contributor_Set() const{
    return m_contributions_mixin_contributor_isSet;
}

bool OAIContributions_mixin_contribution_contribution::is_contributions_mixin_contributor_Valid() const{
    return m_contributions_mixin_contributor_isValid;
}

OAIContributions_mixin_contribution_contribution_contribution_credit_role OAIContributions_mixin_contribution_contribution::getCreditRole() const {
    return m_credit_role;
}
void OAIContributions_mixin_contribution_contribution::setCreditRole(const OAIContributions_mixin_contribution_contribution_contribution_credit_role &credit_role) {
    m_credit_role = credit_role;
    m_credit_role_isSet = true;
}

bool OAIContributions_mixin_contribution_contribution::is_credit_role_Set() const{
    return m_credit_role_isSet;
}

bool OAIContributions_mixin_contribution_contribution::is_credit_role_Valid() const{
    return m_credit_role_isValid;
}

bool OAIContributions_mixin_contribution_contribution::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_character_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_contribution.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_contributions_mixin_contributor.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_credit_role.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIContributions_mixin_contribution_contribution::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_contribution_isValid && true;
}

} // namespace OpenAPI
