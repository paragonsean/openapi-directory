/**
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIArticle_Review_articleSizeRatings.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArticle_Review_articleSizeRatings::OAIArticle_Review_articleSizeRatings(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArticle_Review_articleSizeRatings::OAIArticle_Review_articleSizeRatings() {
    this->initializeModel();
}

OAIArticle_Review_articleSizeRatings::~OAIArticle_Review_articleSizeRatings() {}

void OAIArticle_Review_articleSizeRatings::initializeModel() {

    m_bootleg_width_isSet = false;
    m_bootleg_width_isValid = false;

    m_chest_isSet = false;
    m_chest_isValid = false;

    m_chest_girth_isSet = false;
    m_chest_girth_isValid = false;

    m_collar_size_isSet = false;
    m_collar_size_isValid = false;

    m_cup_size_isSet = false;
    m_cup_size_isValid = false;

    m_hips_or_rear_isSet = false;
    m_hips_or_rear_isValid = false;

    m_leg_fit_isSet = false;
    m_leg_fit_isValid = false;

    m_length_isSet = false;
    m_length_isValid = false;

    m_overall_isSet = false;
    m_overall_isValid = false;

    m_shoe_width_isSet = false;
    m_shoe_width_isValid = false;

    m_shoulders_isSet = false;
    m_shoulders_isValid = false;

    m_sleeves_isSet = false;
    m_sleeves_isValid = false;
}

void OAIArticle_Review_articleSizeRatings::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArticle_Review_articleSizeRatings::fromJsonObject(QJsonObject json) {

    m_bootleg_width_isValid = ::OpenAPI::fromJsonValue(m_bootleg_width, json[QString("BOOTLEG_WIDTH")]);
    m_bootleg_width_isSet = !json[QString("BOOTLEG_WIDTH")].isNull() && m_bootleg_width_isValid;

    m_chest_isValid = ::OpenAPI::fromJsonValue(m_chest, json[QString("CHEST")]);
    m_chest_isSet = !json[QString("CHEST")].isNull() && m_chest_isValid;

    m_chest_girth_isValid = ::OpenAPI::fromJsonValue(m_chest_girth, json[QString("CHEST_GIRTH")]);
    m_chest_girth_isSet = !json[QString("CHEST_GIRTH")].isNull() && m_chest_girth_isValid;

    m_collar_size_isValid = ::OpenAPI::fromJsonValue(m_collar_size, json[QString("COLLAR_SIZE")]);
    m_collar_size_isSet = !json[QString("COLLAR_SIZE")].isNull() && m_collar_size_isValid;

    m_cup_size_isValid = ::OpenAPI::fromJsonValue(m_cup_size, json[QString("CUP_SIZE")]);
    m_cup_size_isSet = !json[QString("CUP_SIZE")].isNull() && m_cup_size_isValid;

    m_hips_or_rear_isValid = ::OpenAPI::fromJsonValue(m_hips_or_rear, json[QString("HIPS_OR_REAR")]);
    m_hips_or_rear_isSet = !json[QString("HIPS_OR_REAR")].isNull() && m_hips_or_rear_isValid;

    m_leg_fit_isValid = ::OpenAPI::fromJsonValue(m_leg_fit, json[QString("LEG_FIT")]);
    m_leg_fit_isSet = !json[QString("LEG_FIT")].isNull() && m_leg_fit_isValid;

    m_length_isValid = ::OpenAPI::fromJsonValue(m_length, json[QString("LENGTH")]);
    m_length_isSet = !json[QString("LENGTH")].isNull() && m_length_isValid;

    m_overall_isValid = ::OpenAPI::fromJsonValue(m_overall, json[QString("OVERALL")]);
    m_overall_isSet = !json[QString("OVERALL")].isNull() && m_overall_isValid;

    m_shoe_width_isValid = ::OpenAPI::fromJsonValue(m_shoe_width, json[QString("SHOE_WIDTH")]);
    m_shoe_width_isSet = !json[QString("SHOE_WIDTH")].isNull() && m_shoe_width_isValid;

    m_shoulders_isValid = ::OpenAPI::fromJsonValue(m_shoulders, json[QString("SHOULDERS")]);
    m_shoulders_isSet = !json[QString("SHOULDERS")].isNull() && m_shoulders_isValid;

    m_sleeves_isValid = ::OpenAPI::fromJsonValue(m_sleeves, json[QString("SLEEVES")]);
    m_sleeves_isSet = !json[QString("SLEEVES")].isNull() && m_sleeves_isValid;
}

QString OAIArticle_Review_articleSizeRatings::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArticle_Review_articleSizeRatings::asJsonObject() const {
    QJsonObject obj;
    if (m_bootleg_width_isSet) {
        obj.insert(QString("BOOTLEG_WIDTH"), ::OpenAPI::toJsonValue(m_bootleg_width));
    }
    if (m_chest_isSet) {
        obj.insert(QString("CHEST"), ::OpenAPI::toJsonValue(m_chest));
    }
    if (m_chest_girth_isSet) {
        obj.insert(QString("CHEST_GIRTH"), ::OpenAPI::toJsonValue(m_chest_girth));
    }
    if (m_collar_size_isSet) {
        obj.insert(QString("COLLAR_SIZE"), ::OpenAPI::toJsonValue(m_collar_size));
    }
    if (m_cup_size_isSet) {
        obj.insert(QString("CUP_SIZE"), ::OpenAPI::toJsonValue(m_cup_size));
    }
    if (m_hips_or_rear_isSet) {
        obj.insert(QString("HIPS_OR_REAR"), ::OpenAPI::toJsonValue(m_hips_or_rear));
    }
    if (m_leg_fit_isSet) {
        obj.insert(QString("LEG_FIT"), ::OpenAPI::toJsonValue(m_leg_fit));
    }
    if (m_length_isSet) {
        obj.insert(QString("LENGTH"), ::OpenAPI::toJsonValue(m_length));
    }
    if (m_overall_isSet) {
        obj.insert(QString("OVERALL"), ::OpenAPI::toJsonValue(m_overall));
    }
    if (m_shoe_width_isSet) {
        obj.insert(QString("SHOE_WIDTH"), ::OpenAPI::toJsonValue(m_shoe_width));
    }
    if (m_shoulders_isSet) {
        obj.insert(QString("SHOULDERS"), ::OpenAPI::toJsonValue(m_shoulders));
    }
    if (m_sleeves_isSet) {
        obj.insert(QString("SLEEVES"), ::OpenAPI::toJsonValue(m_sleeves));
    }
    return obj;
}

qint32 OAIArticle_Review_articleSizeRatings::getBootlegWidth() const {
    return m_bootleg_width;
}
void OAIArticle_Review_articleSizeRatings::setBootlegWidth(const qint32 &bootleg_width) {
    m_bootleg_width = bootleg_width;
    m_bootleg_width_isSet = true;
}

bool OAIArticle_Review_articleSizeRatings::is_bootleg_width_Set() const{
    return m_bootleg_width_isSet;
}

bool OAIArticle_Review_articleSizeRatings::is_bootleg_width_Valid() const{
    return m_bootleg_width_isValid;
}

qint32 OAIArticle_Review_articleSizeRatings::getChest() const {
    return m_chest;
}
void OAIArticle_Review_articleSizeRatings::setChest(const qint32 &chest) {
    m_chest = chest;
    m_chest_isSet = true;
}

bool OAIArticle_Review_articleSizeRatings::is_chest_Set() const{
    return m_chest_isSet;
}

bool OAIArticle_Review_articleSizeRatings::is_chest_Valid() const{
    return m_chest_isValid;
}

qint32 OAIArticle_Review_articleSizeRatings::getChestGirth() const {
    return m_chest_girth;
}
void OAIArticle_Review_articleSizeRatings::setChestGirth(const qint32 &chest_girth) {
    m_chest_girth = chest_girth;
    m_chest_girth_isSet = true;
}

bool OAIArticle_Review_articleSizeRatings::is_chest_girth_Set() const{
    return m_chest_girth_isSet;
}

bool OAIArticle_Review_articleSizeRatings::is_chest_girth_Valid() const{
    return m_chest_girth_isValid;
}

qint32 OAIArticle_Review_articleSizeRatings::getCollarSize() const {
    return m_collar_size;
}
void OAIArticle_Review_articleSizeRatings::setCollarSize(const qint32 &collar_size) {
    m_collar_size = collar_size;
    m_collar_size_isSet = true;
}

bool OAIArticle_Review_articleSizeRatings::is_collar_size_Set() const{
    return m_collar_size_isSet;
}

bool OAIArticle_Review_articleSizeRatings::is_collar_size_Valid() const{
    return m_collar_size_isValid;
}

qint32 OAIArticle_Review_articleSizeRatings::getCupSize() const {
    return m_cup_size;
}
void OAIArticle_Review_articleSizeRatings::setCupSize(const qint32 &cup_size) {
    m_cup_size = cup_size;
    m_cup_size_isSet = true;
}

bool OAIArticle_Review_articleSizeRatings::is_cup_size_Set() const{
    return m_cup_size_isSet;
}

bool OAIArticle_Review_articleSizeRatings::is_cup_size_Valid() const{
    return m_cup_size_isValid;
}

qint32 OAIArticle_Review_articleSizeRatings::getHipsOrRear() const {
    return m_hips_or_rear;
}
void OAIArticle_Review_articleSizeRatings::setHipsOrRear(const qint32 &hips_or_rear) {
    m_hips_or_rear = hips_or_rear;
    m_hips_or_rear_isSet = true;
}

bool OAIArticle_Review_articleSizeRatings::is_hips_or_rear_Set() const{
    return m_hips_or_rear_isSet;
}

bool OAIArticle_Review_articleSizeRatings::is_hips_or_rear_Valid() const{
    return m_hips_or_rear_isValid;
}

qint32 OAIArticle_Review_articleSizeRatings::getLegFit() const {
    return m_leg_fit;
}
void OAIArticle_Review_articleSizeRatings::setLegFit(const qint32 &leg_fit) {
    m_leg_fit = leg_fit;
    m_leg_fit_isSet = true;
}

bool OAIArticle_Review_articleSizeRatings::is_leg_fit_Set() const{
    return m_leg_fit_isSet;
}

bool OAIArticle_Review_articleSizeRatings::is_leg_fit_Valid() const{
    return m_leg_fit_isValid;
}

qint32 OAIArticle_Review_articleSizeRatings::getLength() const {
    return m_length;
}
void OAIArticle_Review_articleSizeRatings::setLength(const qint32 &length) {
    m_length = length;
    m_length_isSet = true;
}

bool OAIArticle_Review_articleSizeRatings::is_length_Set() const{
    return m_length_isSet;
}

bool OAIArticle_Review_articleSizeRatings::is_length_Valid() const{
    return m_length_isValid;
}

qint32 OAIArticle_Review_articleSizeRatings::getOverall() const {
    return m_overall;
}
void OAIArticle_Review_articleSizeRatings::setOverall(const qint32 &overall) {
    m_overall = overall;
    m_overall_isSet = true;
}

bool OAIArticle_Review_articleSizeRatings::is_overall_Set() const{
    return m_overall_isSet;
}

bool OAIArticle_Review_articleSizeRatings::is_overall_Valid() const{
    return m_overall_isValid;
}

qint32 OAIArticle_Review_articleSizeRatings::getShoeWidth() const {
    return m_shoe_width;
}
void OAIArticle_Review_articleSizeRatings::setShoeWidth(const qint32 &shoe_width) {
    m_shoe_width = shoe_width;
    m_shoe_width_isSet = true;
}

bool OAIArticle_Review_articleSizeRatings::is_shoe_width_Set() const{
    return m_shoe_width_isSet;
}

bool OAIArticle_Review_articleSizeRatings::is_shoe_width_Valid() const{
    return m_shoe_width_isValid;
}

qint32 OAIArticle_Review_articleSizeRatings::getShoulders() const {
    return m_shoulders;
}
void OAIArticle_Review_articleSizeRatings::setShoulders(const qint32 &shoulders) {
    m_shoulders = shoulders;
    m_shoulders_isSet = true;
}

bool OAIArticle_Review_articleSizeRatings::is_shoulders_Set() const{
    return m_shoulders_isSet;
}

bool OAIArticle_Review_articleSizeRatings::is_shoulders_Valid() const{
    return m_shoulders_isValid;
}

qint32 OAIArticle_Review_articleSizeRatings::getSleeves() const {
    return m_sleeves;
}
void OAIArticle_Review_articleSizeRatings::setSleeves(const qint32 &sleeves) {
    m_sleeves = sleeves;
    m_sleeves_isSet = true;
}

bool OAIArticle_Review_articleSizeRatings::is_sleeves_Set() const{
    return m_sleeves_isSet;
}

bool OAIArticle_Review_articleSizeRatings::is_sleeves_Valid() const{
    return m_sleeves_isValid;
}

bool OAIArticle_Review_articleSizeRatings::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bootleg_width_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_chest_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_chest_girth_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_collar_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cup_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hips_or_rear_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_leg_fit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_overall_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shoe_width_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shoulders_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sleeves_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArticle_Review_articleSizeRatings::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
