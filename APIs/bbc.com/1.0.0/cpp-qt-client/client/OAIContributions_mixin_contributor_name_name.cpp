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

#include "OAIContributions_mixin_contributor_name_name.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIContributions_mixin_contributor_name_name::OAIContributions_mixin_contributor_name_name(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIContributions_mixin_contributor_name_name::OAIContributions_mixin_contributor_name_name() {
    this->initializeModel();
}

OAIContributions_mixin_contributor_name_name::~OAIContributions_mixin_contributor_name_name() {}

void OAIContributions_mixin_contributor_name_name::initializeModel() {

    m_family_isSet = false;
    m_family_isValid = false;

    m_given_isSet = false;
    m_given_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_presentation_isSet = false;
    m_presentation_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAIContributions_mixin_contributor_name_name::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIContributions_mixin_contributor_name_name::fromJsonObject(QJsonObject json) {

    m_family_isValid = ::OpenAPI::fromJsonValue(m_family, json[QString("family")]);
    m_family_isSet = !json[QString("family")].isNull() && m_family_isValid;

    m_given_isValid = ::OpenAPI::fromJsonValue(m_given, json[QString("given")]);
    m_given_isSet = !json[QString("given")].isNull() && m_given_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_presentation_isValid = ::OpenAPI::fromJsonValue(m_presentation, json[QString("presentation")]);
    m_presentation_isSet = !json[QString("presentation")].isNull() && m_presentation_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAIContributions_mixin_contributor_name_name::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIContributions_mixin_contributor_name_name::asJsonObject() const {
    QJsonObject obj;
    if (m_family_isSet) {
        obj.insert(QString("family"), ::OpenAPI::toJsonValue(m_family));
    }
    if (m_given_isSet) {
        obj.insert(QString("given"), ::OpenAPI::toJsonValue(m_given));
    }
    if (m_name.isSet()) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_presentation_isSet) {
        obj.insert(QString("presentation"), ::OpenAPI::toJsonValue(m_presentation));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

QString OAIContributions_mixin_contributor_name_name::getFamily() const {
    return m_family;
}
void OAIContributions_mixin_contributor_name_name::setFamily(const QString &family) {
    m_family = family;
    m_family_isSet = true;
}

bool OAIContributions_mixin_contributor_name_name::is_family_Set() const{
    return m_family_isSet;
}

bool OAIContributions_mixin_contributor_name_name::is_family_Valid() const{
    return m_family_isValid;
}

QString OAIContributions_mixin_contributor_name_name::getGiven() const {
    return m_given;
}
void OAIContributions_mixin_contributor_name_name::setGiven(const QString &given) {
    m_given = given;
    m_given_isSet = true;
}

bool OAIContributions_mixin_contributor_name_name::is_given_Set() const{
    return m_given_isSet;
}

bool OAIContributions_mixin_contributor_name_name::is_given_Valid() const{
    return m_given_isValid;
}

OAIContributions_mixin_contributor_name_name_name OAIContributions_mixin_contributor_name_name::getName() const {
    return m_name;
}
void OAIContributions_mixin_contributor_name_name::setName(const OAIContributions_mixin_contributor_name_name_name &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIContributions_mixin_contributor_name_name::is_name_Set() const{
    return m_name_isSet;
}

bool OAIContributions_mixin_contributor_name_name::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIContributions_mixin_contributor_name_name::getPresentation() const {
    return m_presentation;
}
void OAIContributions_mixin_contributor_name_name::setPresentation(const QString &presentation) {
    m_presentation = presentation;
    m_presentation_isSet = true;
}

bool OAIContributions_mixin_contributor_name_name::is_presentation_Set() const{
    return m_presentation_isSet;
}

bool OAIContributions_mixin_contributor_name_name::is_presentation_Valid() const{
    return m_presentation_isValid;
}

QString OAIContributions_mixin_contributor_name_name::getTitle() const {
    return m_title;
}
void OAIContributions_mixin_contributor_name_name::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIContributions_mixin_contributor_name_name::is_title_Set() const{
    return m_title_isSet;
}

bool OAIContributions_mixin_contributor_name_name::is_title_Valid() const{
    return m_title_isValid;
}

bool OAIContributions_mixin_contributor_name_name::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_family_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_given_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_presentation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIContributions_mixin_contributor_name_name::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
