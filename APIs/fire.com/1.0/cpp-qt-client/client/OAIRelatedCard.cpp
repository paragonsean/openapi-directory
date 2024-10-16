/**
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRelatedCard.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRelatedCard::OAIRelatedCard(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRelatedCard::OAIRelatedCard() {
    this->initializeModel();
}

OAIRelatedCard::~OAIRelatedCard() {}

void OAIRelatedCard::initializeModel() {

    m_alias_isSet = false;
    m_alias_isValid = false;

    m_card_id_isSet = false;
    m_card_id_isValid = false;

    m_emboss_business_name_isSet = false;
    m_emboss_business_name_isValid = false;

    m_emboss_card_name_isSet = false;
    m_emboss_card_name_isValid = false;

    m_expiry_date_isSet = false;
    m_expiry_date_isValid = false;

    m_masked_pan_isSet = false;
    m_masked_pan_isValid = false;

    m_provider_isSet = false;
    m_provider_isValid = false;
}

void OAIRelatedCard::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRelatedCard::fromJsonObject(QJsonObject json) {

    m_alias_isValid = ::OpenAPI::fromJsonValue(m_alias, json[QString("alias")]);
    m_alias_isSet = !json[QString("alias")].isNull() && m_alias_isValid;

    m_card_id_isValid = ::OpenAPI::fromJsonValue(m_card_id, json[QString("cardId")]);
    m_card_id_isSet = !json[QString("cardId")].isNull() && m_card_id_isValid;

    m_emboss_business_name_isValid = ::OpenAPI::fromJsonValue(m_emboss_business_name, json[QString("embossBusinessName")]);
    m_emboss_business_name_isSet = !json[QString("embossBusinessName")].isNull() && m_emboss_business_name_isValid;

    m_emboss_card_name_isValid = ::OpenAPI::fromJsonValue(m_emboss_card_name, json[QString("embossCardName")]);
    m_emboss_card_name_isSet = !json[QString("embossCardName")].isNull() && m_emboss_card_name_isValid;

    m_expiry_date_isValid = ::OpenAPI::fromJsonValue(m_expiry_date, json[QString("expiryDate")]);
    m_expiry_date_isSet = !json[QString("expiryDate")].isNull() && m_expiry_date_isValid;

    m_masked_pan_isValid = ::OpenAPI::fromJsonValue(m_masked_pan, json[QString("maskedPan")]);
    m_masked_pan_isSet = !json[QString("maskedPan")].isNull() && m_masked_pan_isValid;

    m_provider_isValid = ::OpenAPI::fromJsonValue(m_provider, json[QString("provider")]);
    m_provider_isSet = !json[QString("provider")].isNull() && m_provider_isValid;
}

QString OAIRelatedCard::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRelatedCard::asJsonObject() const {
    QJsonObject obj;
    if (m_alias_isSet) {
        obj.insert(QString("alias"), ::OpenAPI::toJsonValue(m_alias));
    }
    if (m_card_id_isSet) {
        obj.insert(QString("cardId"), ::OpenAPI::toJsonValue(m_card_id));
    }
    if (m_emboss_business_name_isSet) {
        obj.insert(QString("embossBusinessName"), ::OpenAPI::toJsonValue(m_emboss_business_name));
    }
    if (m_emboss_card_name_isSet) {
        obj.insert(QString("embossCardName"), ::OpenAPI::toJsonValue(m_emboss_card_name));
    }
    if (m_expiry_date_isSet) {
        obj.insert(QString("expiryDate"), ::OpenAPI::toJsonValue(m_expiry_date));
    }
    if (m_masked_pan_isSet) {
        obj.insert(QString("maskedPan"), ::OpenAPI::toJsonValue(m_masked_pan));
    }
    if (m_provider_isSet) {
        obj.insert(QString("provider"), ::OpenAPI::toJsonValue(m_provider));
    }
    return obj;
}

QString OAIRelatedCard::getAlias() const {
    return m_alias;
}
void OAIRelatedCard::setAlias(const QString &alias) {
    m_alias = alias;
    m_alias_isSet = true;
}

bool OAIRelatedCard::is_alias_Set() const{
    return m_alias_isSet;
}

bool OAIRelatedCard::is_alias_Valid() const{
    return m_alias_isValid;
}

qint64 OAIRelatedCard::getCardId() const {
    return m_card_id;
}
void OAIRelatedCard::setCardId(const qint64 &card_id) {
    m_card_id = card_id;
    m_card_id_isSet = true;
}

bool OAIRelatedCard::is_card_id_Set() const{
    return m_card_id_isSet;
}

bool OAIRelatedCard::is_card_id_Valid() const{
    return m_card_id_isValid;
}

QString OAIRelatedCard::getEmbossBusinessName() const {
    return m_emboss_business_name;
}
void OAIRelatedCard::setEmbossBusinessName(const QString &emboss_business_name) {
    m_emboss_business_name = emboss_business_name;
    m_emboss_business_name_isSet = true;
}

bool OAIRelatedCard::is_emboss_business_name_Set() const{
    return m_emboss_business_name_isSet;
}

bool OAIRelatedCard::is_emboss_business_name_Valid() const{
    return m_emboss_business_name_isValid;
}

QString OAIRelatedCard::getEmbossCardName() const {
    return m_emboss_card_name;
}
void OAIRelatedCard::setEmbossCardName(const QString &emboss_card_name) {
    m_emboss_card_name = emboss_card_name;
    m_emboss_card_name_isSet = true;
}

bool OAIRelatedCard::is_emboss_card_name_Set() const{
    return m_emboss_card_name_isSet;
}

bool OAIRelatedCard::is_emboss_card_name_Valid() const{
    return m_emboss_card_name_isValid;
}

QDateTime OAIRelatedCard::getExpiryDate() const {
    return m_expiry_date;
}
void OAIRelatedCard::setExpiryDate(const QDateTime &expiry_date) {
    m_expiry_date = expiry_date;
    m_expiry_date_isSet = true;
}

bool OAIRelatedCard::is_expiry_date_Set() const{
    return m_expiry_date_isSet;
}

bool OAIRelatedCard::is_expiry_date_Valid() const{
    return m_expiry_date_isValid;
}

QString OAIRelatedCard::getMaskedPan() const {
    return m_masked_pan;
}
void OAIRelatedCard::setMaskedPan(const QString &masked_pan) {
    m_masked_pan = masked_pan;
    m_masked_pan_isSet = true;
}

bool OAIRelatedCard::is_masked_pan_Set() const{
    return m_masked_pan_isSet;
}

bool OAIRelatedCard::is_masked_pan_Valid() const{
    return m_masked_pan_isValid;
}

QString OAIRelatedCard::getProvider() const {
    return m_provider;
}
void OAIRelatedCard::setProvider(const QString &provider) {
    m_provider = provider;
    m_provider_isSet = true;
}

bool OAIRelatedCard::is_provider_Set() const{
    return m_provider_isSet;
}

bool OAIRelatedCard::is_provider_Valid() const{
    return m_provider_isValid;
}

bool OAIRelatedCard::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_alias_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_card_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_emboss_business_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_emboss_card_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expiry_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_masked_pan_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_provider_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRelatedCard::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
