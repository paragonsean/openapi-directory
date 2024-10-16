/**
 * Groundhog Day API
 * This API returns all of North America’s prognosticating animals and their yearly weather predictions.
 *
 * The version of the OpenAPI document: 1.2.1
 * Contact: hello@groundhog-day.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGroundhog.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGroundhog::OAIGroundhog(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGroundhog::OAIGroundhog() {
    this->initializeModel();
}

OAIGroundhog::~OAIGroundhog() {}

void OAIGroundhog::initializeModel() {

    m_active_isSet = false;
    m_active_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_contact_isSet = false;
    m_contact_isValid = false;

    m_coordinates_isSet = false;
    m_coordinates_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_current_prediction_isSet = false;
    m_current_prediction_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_is_groundhog_isSet = false;
    m_is_groundhog_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_predictions_isSet = false;
    m_predictions_isValid = false;

    m_predictions_count_isSet = false;
    m_predictions_count_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_shortname_isSet = false;
    m_shortname_isValid = false;

    m_slug_isSet = false;
    m_slug_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIGroundhog::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGroundhog::fromJsonObject(QJsonObject json) {

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("active")]);
    m_active_isSet = !json[QString("active")].isNull() && m_active_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_contact_isValid = ::OpenAPI::fromJsonValue(m_contact, json[QString("contact")]);
    m_contact_isSet = !json[QString("contact")].isNull() && m_contact_isValid;

    m_coordinates_isValid = ::OpenAPI::fromJsonValue(m_coordinates, json[QString("coordinates")]);
    m_coordinates_isSet = !json[QString("coordinates")].isNull() && m_coordinates_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_current_prediction_isValid = ::OpenAPI::fromJsonValue(m_current_prediction, json[QString("currentPrediction")]);
    m_current_prediction_isSet = !json[QString("currentPrediction")].isNull() && m_current_prediction_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_is_groundhog_isValid = ::OpenAPI::fromJsonValue(m_is_groundhog, json[QString("isGroundhog")]);
    m_is_groundhog_isSet = !json[QString("isGroundhog")].isNull() && m_is_groundhog_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_predictions_isValid = ::OpenAPI::fromJsonValue(m_predictions, json[QString("predictions")]);
    m_predictions_isSet = !json[QString("predictions")].isNull() && m_predictions_isValid;

    m_predictions_count_isValid = ::OpenAPI::fromJsonValue(m_predictions_count, json[QString("predictionsCount")]);
    m_predictions_count_isSet = !json[QString("predictionsCount")].isNull() && m_predictions_count_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_shortname_isValid = ::OpenAPI::fromJsonValue(m_shortname, json[QString("shortname")]);
    m_shortname_isSet = !json[QString("shortname")].isNull() && m_shortname_isValid;

    m_slug_isValid = ::OpenAPI::fromJsonValue(m_slug, json[QString("slug")]);
    m_slug_isSet = !json[QString("slug")].isNull() && m_slug_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIGroundhog::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGroundhog::asJsonObject() const {
    QJsonObject obj;
    if (m_active_isSet) {
        obj.insert(QString("active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_contact_isSet) {
        obj.insert(QString("contact"), ::OpenAPI::toJsonValue(m_contact));
    }
    if (m_coordinates_isSet) {
        obj.insert(QString("coordinates"), ::OpenAPI::toJsonValue(m_coordinates));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_current_prediction_isSet) {
        obj.insert(QString("currentPrediction"), ::OpenAPI::toJsonValue(m_current_prediction));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_is_groundhog_isSet) {
        obj.insert(QString("isGroundhog"), ::OpenAPI::toJsonValue(m_is_groundhog));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_predictions.size() > 0) {
        obj.insert(QString("predictions"), ::OpenAPI::toJsonValue(m_predictions));
    }
    if (m_predictions_count_isSet) {
        obj.insert(QString("predictionsCount"), ::OpenAPI::toJsonValue(m_predictions_count));
    }
    if (m_region_isSet) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_shortname_isSet) {
        obj.insert(QString("shortname"), ::OpenAPI::toJsonValue(m_shortname));
    }
    if (m_slug_isSet) {
        obj.insert(QString("slug"), ::OpenAPI::toJsonValue(m_slug));
    }
    if (m_source_isSet) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

qint32 OAIGroundhog::getActive() const {
    return m_active;
}
void OAIGroundhog::setActive(const qint32 &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAIGroundhog::is_active_Set() const{
    return m_active_isSet;
}

bool OAIGroundhog::is_active_Valid() const{
    return m_active_isValid;
}

QString OAIGroundhog::getCity() const {
    return m_city;
}
void OAIGroundhog::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIGroundhog::is_city_Set() const{
    return m_city_isSet;
}

bool OAIGroundhog::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIGroundhog::getContact() const {
    return m_contact;
}
void OAIGroundhog::setContact(const QString &contact) {
    m_contact = contact;
    m_contact_isSet = true;
}

bool OAIGroundhog::is_contact_Set() const{
    return m_contact_isSet;
}

bool OAIGroundhog::is_contact_Valid() const{
    return m_contact_isValid;
}

QString OAIGroundhog::getCoordinates() const {
    return m_coordinates;
}
void OAIGroundhog::setCoordinates(const QString &coordinates) {
    m_coordinates = coordinates;
    m_coordinates_isSet = true;
}

bool OAIGroundhog::is_coordinates_Set() const{
    return m_coordinates_isSet;
}

bool OAIGroundhog::is_coordinates_Valid() const{
    return m_coordinates_isValid;
}

QString OAIGroundhog::getCountry() const {
    return m_country;
}
void OAIGroundhog::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIGroundhog::is_country_Set() const{
    return m_country_isSet;
}

bool OAIGroundhog::is_country_Valid() const{
    return m_country_isValid;
}

QString OAIGroundhog::getCurrentPrediction() const {
    return m_current_prediction;
}
void OAIGroundhog::setCurrentPrediction(const QString &current_prediction) {
    m_current_prediction = current_prediction;
    m_current_prediction_isSet = true;
}

bool OAIGroundhog::is_current_prediction_Set() const{
    return m_current_prediction_isSet;
}

bool OAIGroundhog::is_current_prediction_Valid() const{
    return m_current_prediction_isValid;
}

QString OAIGroundhog::getDescription() const {
    return m_description;
}
void OAIGroundhog::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIGroundhog::is_description_Set() const{
    return m_description_isSet;
}

bool OAIGroundhog::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIGroundhog::getId() const {
    return m_id;
}
void OAIGroundhog::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGroundhog::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGroundhog::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIGroundhog::getImage() const {
    return m_image;
}
void OAIGroundhog::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAIGroundhog::is_image_Set() const{
    return m_image_isSet;
}

bool OAIGroundhog::is_image_Valid() const{
    return m_image_isValid;
}

qint32 OAIGroundhog::getIsGroundhog() const {
    return m_is_groundhog;
}
void OAIGroundhog::setIsGroundhog(const qint32 &is_groundhog) {
    m_is_groundhog = is_groundhog;
    m_is_groundhog_isSet = true;
}

bool OAIGroundhog::is_is_groundhog_Set() const{
    return m_is_groundhog_isSet;
}

bool OAIGroundhog::is_is_groundhog_Valid() const{
    return m_is_groundhog_isValid;
}

QString OAIGroundhog::getName() const {
    return m_name;
}
void OAIGroundhog::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGroundhog::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGroundhog::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIPrediction> OAIGroundhog::getPredictions() const {
    return m_predictions;
}
void OAIGroundhog::setPredictions(const QList<OAIPrediction> &predictions) {
    m_predictions = predictions;
    m_predictions_isSet = true;
}

bool OAIGroundhog::is_predictions_Set() const{
    return m_predictions_isSet;
}

bool OAIGroundhog::is_predictions_Valid() const{
    return m_predictions_isValid;
}

qint32 OAIGroundhog::getPredictionsCount() const {
    return m_predictions_count;
}
void OAIGroundhog::setPredictionsCount(const qint32 &predictions_count) {
    m_predictions_count = predictions_count;
    m_predictions_count_isSet = true;
}

bool OAIGroundhog::is_predictions_count_Set() const{
    return m_predictions_count_isSet;
}

bool OAIGroundhog::is_predictions_count_Valid() const{
    return m_predictions_count_isValid;
}

QString OAIGroundhog::getRegion() const {
    return m_region;
}
void OAIGroundhog::setRegion(const QString &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAIGroundhog::is_region_Set() const{
    return m_region_isSet;
}

bool OAIGroundhog::is_region_Valid() const{
    return m_region_isValid;
}

QString OAIGroundhog::getShortname() const {
    return m_shortname;
}
void OAIGroundhog::setShortname(const QString &shortname) {
    m_shortname = shortname;
    m_shortname_isSet = true;
}

bool OAIGroundhog::is_shortname_Set() const{
    return m_shortname_isSet;
}

bool OAIGroundhog::is_shortname_Valid() const{
    return m_shortname_isValid;
}

QString OAIGroundhog::getSlug() const {
    return m_slug;
}
void OAIGroundhog::setSlug(const QString &slug) {
    m_slug = slug;
    m_slug_isSet = true;
}

bool OAIGroundhog::is_slug_Set() const{
    return m_slug_isSet;
}

bool OAIGroundhog::is_slug_Valid() const{
    return m_slug_isValid;
}

QString OAIGroundhog::getSource() const {
    return m_source;
}
void OAIGroundhog::setSource(const QString &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIGroundhog::is_source_Set() const{
    return m_source_isSet;
}

bool OAIGroundhog::is_source_Valid() const{
    return m_source_isValid;
}

QString OAIGroundhog::getType() const {
    return m_type;
}
void OAIGroundhog::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIGroundhog::is_type_Set() const{
    return m_type_isSet;
}

bool OAIGroundhog::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIGroundhog::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_contact_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coordinates_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_current_prediction_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_groundhog_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_predictions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_predictions_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shortname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slug_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGroundhog::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_active_isValid && m_city_isValid && m_contact_isValid && m_coordinates_isValid && m_country_isValid && m_current_prediction_isValid && m_description_isValid && m_id_isValid && m_image_isValid && m_is_groundhog_isValid && m_name_isValid && m_region_isValid && m_shortname_isValid && m_slug_isValid && m_source_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
